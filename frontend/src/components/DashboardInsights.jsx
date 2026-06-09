import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, PieChart, Pie, Cell } from 'recharts';
import { Phone, CheckCircle, TrendingUp, AlertTriangle } from 'lucide-react';

const DashboardInsights = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        // Fetch mock capabilities from the backend API we built
        fetch('http://localhost:8000/api/dashboard/daily')
            .then(res => res.json())
            .then(json => setData(json))
            .catch(err => {
                console.error("Failed to fetch APIs. Using fallback data.", err);
                // Fallback for demonstration if backend is not running
                setData({
                    kpis: { total_calls: 42050, resolution_rate: "89.4%", active_escalations: 3, csat_score: 4.8 },
                    intent_volume: [
                        { intent: "Order Status", count: 18000 },
                        { intent: "Returns", count: 12000 },
                        { intent: "Delivery", count: 6000 },
                        { intent: "Payment", count: 4050 },
                        { intent: "Query", count: 2000 }
                    ],
                    sentiment_by_language: [
                        { name: "Positive", value: 66, color: "#10b981" },
                        { name: "Neutral", value: 25, color: "#3b82f6" },
                        { name: "Negative", value: 9, color: "#ef4444" }
                    ]
                });
            });
    }, []);

    if (!data) return <div className="glass-panel text-center">Loading insights...</div>;

    return (
        <div className="flex-col gap-6">
            {/* KPI Row */}
            <div className="grid grid-cols-4 gap-6">
                {[
                    { label: "Total Handled", val: data.kpis.total_calls.toLocaleString(), icon: <Phone size={24} />, color: "var(--accent-primary)" },
                    { label: "Resolution Rate", val: data.kpis.resolution_rate, icon: <CheckCircle size={24} />, color: "var(--success)" },
                    { label: "Active Escalations", val: data.kpis.active_escalations, icon: <AlertTriangle size={24} />, color: "var(--danger)" },
                    { label: "CSAT Score", val: data.kpis.csat_score, icon: <TrendingUp size={24} />, color: "var(--warning)" },
                ].map((kpi, i) => (
                    <div key={i} className="glass-panel flex-col gap-2">
                        <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }} className="flex justify-between">
                            {kpi.label}
                            <span style={{ color: kpi.color }}>{kpi.icon}</span>
                        </span>
                        <h2 style={{ fontSize: '2rem', margin: 0 }}>{kpi.val}</h2>
                    </div>
                ))}
            </div>

            {/* Charts Row */}
            <div className="grid grid-cols-2 gap-6">
                <div className="glass-panel" style={{ height: '350px' }}>
                    <h3 className="text-gradient">Intent Volume Details</h3>
                    <ResponsiveContainer width="100%" height="85%">
                        <BarChart data={data.intent_volume} layout="vertical" margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                            <XAxis type="number" stroke="var(--text-muted)" />
                            <YAxis dataKey="intent" type="category" stroke="var(--text-muted)" width={100} />
                            <Tooltip cursor={{ fill: 'rgba(255,255,255,0.05)' }} contentStyle={{ background: 'var(--bg-panel)', border: 'none', borderRadius: '8px', color: '#fff' }} />
                            <Bar dataKey="count" fill="var(--accent-primary)" radius={[0, 4, 4, 0]} />
                        </BarChart>
                    </ResponsiveContainer>
                </div>

                <div className="glass-panel" style={{ height: '350px' }}>
                    <h3 className="text-gradient">Overall Sentiment Distribution</h3>
                    <ResponsiveContainer width="100%" height="85%">
                        <PieChart>
                            <Pie data={data.sentiment_by_language || [{ name: "Pos", value: 60 }, { name: "Neu", value: 30 }, { name: "Neg", value: 10 }]}
                                cx="50%" cy="50%" innerRadius={60} outerRadius={100} paddingAngle={5} dataKey="value">
                                {
                                    (data.sentiment_by_language || []).map((entry, index) => (
                                        <Cell key={`cell-${index}`} fill={entry.color || 'var(--accent-primary)'} />
                                    ))
                                }
                            </Pie>
                            <Tooltip contentStyle={{ background: 'var(--bg-panel)', border: 'none', borderRadius: '8px', color: '#fff' }} />
                        </PieChart>
                    </ResponsiveContainer>
                </div>
            </div>
        </div>
    );
};

export default DashboardInsights;
