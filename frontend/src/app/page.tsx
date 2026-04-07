'use client';

import React, { useState, useEffect } from 'react';
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, 
  BarChart, Bar, Cell, PieChart, Pie
} from 'recharts';
import { 
  TrendingUp, Users, Globe, AlertCircle, 
  ArrowUpRight, DollarSign, Activity, Award
} from 'lucide-react';

export default function Dashboard() {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/data/dashboard_data.json')
      .then(res => res.json())
      .then(json => {
        setData(json);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error loading data:', err);
        setLoading(false);
      });
  }, []);

  if (loading || !data) {
    return (
      <div style={{ height: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#0f172a', color: '#fff' }}>
        <div className="fade-in">Arquitectando Solución Maestra...</div>
      </div>
    );
  }

  const COLORS = ['#00f2fe', '#4facfe', '#f093fb', '#6366f1'];

  return (
    <main className="main-container">
      {/* Header */}
      <header className="header fade-in">
        <div className="title-section">
          <h1>Social & Economic Analytics</h1>
          <p>Lead Data Architect Execution | República Dominicana Context</p>
        </div>
        <div className="card" style={{ padding: '0.75rem 1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Activity size={18} color="#00f2fe" />
          <span style={{ fontSize: '0.875rem', fontWeight: 600 }}>System Live</span>
        </div>
      </header>

      {/* KPI Grid */}
      <section className="grid fade-in">
        <div className="card">
          <div className="kpi-header">
            <div className="kpi-label">Revenue (USD)</div>
            <DollarSign size={20} color="#00f2fe" />
          </div>
          <div className="kpi-value">${data.sales.total_revenue_usd.toLocaleString()}</div>
          <div className="trend up">
            <ArrowUpRight size={14} /> {data.sales.revenue_growth_wow}% WoW
          </div>
        </div>

        <div className="card">
          <div className="kpi-header">
            <div className="kpi-label">Talent Retention</div>
            <Users size={20} color="#4facfe" />
          </div>
          <div className="kpi-value">{100 - data.talent.turnover_rate}%</div>
          <div className="kpi-label" style={{ fontSize: '0.75rem' }}>Churn Rate: {data.talent.turnover_rate}%</div>
        </div>

        <div className="card">
          <div className="kpi-header">
            <div className="kpi-label">Social Impact</div>
            <Globe size={20} color="#f093fb" />
          </div>
          <div className="kpi-value">{data.social.social_correlation}</div>
          <div className="kpi-label" style={{ fontSize: '0.75rem' }}>Correlation: Connectivity/Edu</div>
        </div>

        <div className="card" style={{ borderLeft: '4px solid #f59e0b' }}>
          <div className="kpi-header">
            <div className="kpi-label">System Alert</div>
            <AlertCircle size={20} color="#f59e0b" />
          </div>
          <div style={{ color: '#f59e0b', fontSize: '0.875rem', fontWeight: 500 }}>
            Brecha de {data.social.internet_gap_years} años detectada en zonas rurales.
          </div>
        </div>
      </section>

      {/* Charts Section */}
      <section className="charts-grid fade-in">
        {/* Sales Trend */}
        <div className="card chart-card">
          <h2 className="chart-title">Economic Impact & Sales Trend</h2>
          <ResponsiveContainer width="100%" height="80%">
            <LineChart data={data.sales.sales_history}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" vertical={false} />
              <XAxis dataKey="month" stroke="#94a3b8" />
              <YAxis stroke="#94a3b8" hide />
              <Tooltip 
                contentStyle={{ background: '#1e293b', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                itemStyle={{ color: '#00f2fe' }}
              />
              <Line 
                type="monotone" 
                dataKey="amount" 
                stroke="url(#colorLine)" 
                strokeWidth={4} 
                dot={{ r: 4, fill: '#00f2fe' }}
              />
              <defs>
                <linearGradient id="colorLine" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#00f2fe" />
                  <stop offset="100%" stopColor="#4facfe" />
                </linearGradient>
              </defs>
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Talent Segmentation */}
        <div className="card chart-card">
          <h2 className="chart-title">9-Box Talent Grid</h2>
          <ResponsiveContainer width="100%" height="80%">
            <PieChart>
              <Pie
                data={data.talent.talent_grid}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={80}
                paddingAngle={5}
                dataKey="count"
              >
                {data.talent.talent_grid.map((entry: any, index: number) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip 
                 contentStyle={{ background: '#1e293b', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
              />
            </PieChart>
          </ResponsiveContainer>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: '1rem', fontSize: '0.75rem' }}>
            {data.talent.talent_grid.map((item: any, i: number) => (
              <div key={i} style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                <div style={{ width: 8, height: 8, borderRadius: '50%', background: COLORS[i % COLORS.length] }}></div>
                <span color="#94a3b8">{item.segment}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer / Social Quote */}
      <footer style={{ marginTop: '3rem', textAlign: 'center', opacity: 0.6 }} className="fade-in">
        <blockquote style={{ fontStyle: 'italic', color: '#94a3b8' }}>
          "{data.social.impact_recommendation}"
        </blockquote>
        <div style={{ marginTop: '1rem', display: 'flex', justifyContent: 'center', gap: '1rem' }}>
          <Award size={16} /> <span>Open Science Compliance</span>
        </div>
      </footer>
    </main>
  );
}
