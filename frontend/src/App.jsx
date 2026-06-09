import React from 'react';
import './index.css';
import DashboardInsights from './components/DashboardInsights';
import EscalationBoard from './components/EscalationBoard';
import { Headphones } from 'lucide-react';

function App() {
  return (
    <div style={{ padding: '32px', maxWidth: '1400px', margin: '0 auto' }} className="flex-col gap-6">
      <header className="flex align-center justify-between" style={{ paddingBottom: '16px', borderBottom: '1px solid var(--border)' }}>
        <div className="flex align-center gap-4">
          <div style={{
            background: 'linear-gradient(135deg, #3b82f6, #8b5cf6)',
            padding: '12px',
            borderRadius: '12px',
            color: 'white'
          }}>
            <Headphones size={28} />
          </div>
          <div>
            <h1 style={{ margin: 0, fontSize: '1.8rem' }}>ShopNow<span className="text-gradient">Voice</span></h1>
            <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Tier-1 AI Operator Dashboard</span>
          </div>
        </div>

        <div className="flex gap-4">
          <div className="glass-panel text-center" style={{ padding: '8px 16px', borderRadius: '24px' }}>
            <span style={{ color: 'var(--success)' }}>● System Online</span>
          </div>
        </div>
      </header>

      <main className="grid" style={{ gridTemplateColumns: 'minmax(0, 3fr) 1fr', gap: '24px' }}>
        <section>
          <DashboardInsights />
        </section>

        <aside>
          <EscalationBoard />
        </aside>
      </main>
    </div>
  );
}

export default App;
