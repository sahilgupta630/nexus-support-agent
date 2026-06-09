import React, { useState, useEffect } from 'react';
import { AlertCircle, User, Activity, MessageSquare } from 'lucide-react';

const EscalationBoard = () => {
  const [escalations, setEscalations] = useState([
    {
      id: "esc_001",
      customer_name: "Alice Smith",
      issue_summary: "Customer repeatedly expressing negative sentiment regarding a delayed refund for ORD789.",
      sentiment_history: ["NEUTRAL", "NEGATIVE", "NEGATIVE"],
      suggested_tone: "Empathetic, Fast Resolution",
      time: "Just now"
    }
  ]);

  // Mocking live incoming escalations
  useEffect(() => {
    const timer = setTimeout(() => {
      setEscalations(prev => [{
        id: "esc_002",
        customer_name: "David Lee",
        issue_summary: "User frustrated over damaged product delivery. Used negative phrases.",
        sentiment_history: ["NEUTRAL", "NEGATIVE", "NEGATIVE"],
        suggested_tone: "Apologetic, Reassuring",
        time: "Just now"
      }, ...prev]);
    }, 15000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="glass-panel flex-col gap-4 animate-pulse-danger">
      <div className="flex justify-between align-center">
        <h2 className="flex align-center gap-2 text-gradient">
          <AlertCircle size={24} color="var(--danger)" />
          Live Escalation Board
        </h2>
        <span style={{color: 'var(--danger)', fontWeight: 600}}>
          {escalations.length} Active
        </span>
      </div>
      
      <div className="flex-col gap-4">
        {escalations.map((esc) => (
          <div key={esc.id} style={{
            background: 'rgba(239, 68, 68, 0.1)',
            borderLeft: '4px solid var(--danger)',
            padding: '16px',
            borderRadius: '8px'
          }} className="flex-col gap-2">
            
            <div className="flex justify-between">
              <strong className="flex align-center gap-2" style={{color: 'white'}}>
                <User size={16} /> {esc.customer_name}
              </strong>
              <small style={{color: 'var(--text-muted)'}}>{esc.time}</small>
            </div>
            
            <p style={{margin: '8px 0', fontSize: '0.9rem'}}>
              {esc.issue_summary}
            </p>
            
            <div className="flex gap-4" style={{fontSize: '0.85rem'}}>
              <span className="flex align-center gap-2" style={{color: 'var(--warning)'}}>
                <Activity size={14} /> Sentiment: {esc.sentiment_history.join(" ➔ ")}
              </span>
              <span className="flex align-center gap-2" style={{color: 'var(--success)'}}>
                <MessageSquare size={14} /> Tone: {esc.suggested_tone}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EscalationBoard;
