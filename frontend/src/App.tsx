import { useState } from 'react';
import GenerateTab from './components/GenerateTab';
import VaultTab from './components/VaultTab';
import ScoreTab from './components/ScoreTab';
import { PasswordEntry, loadPasswords, savePasswords } from './fortress';

type Tab = 'generate' | 'vault' | 'analyze';

function ShieldIcon() {
  return (
    <svg width="18" height="20" viewBox="0 0 18 20" fill="none">
      <path d="M9 1L1 4.5V9c0 4.418 3.134 8.556 8 9.5C13.866 17.556 17 13.418 17 9V4.5L9 1z" fill="white" opacity="0.9"/>
      <path d="M6 10l2 2 4-4" stroke="#4f8ef7" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
    </svg>
  );
}

export default function App() {
  const [tab, setTab] = useState<Tab>('generate');
  const [entries, setEntries] = useState<PasswordEntry[]>(() => loadPasswords());

  const updateEntries = (newEntries: PasswordEntry[]) => {
    setEntries(newEntries);
    savePasswords(newEntries);
  };

  const tabs: { id: Tab; label: string; icon: string }[] = [
    { id: 'generate', label: 'Generate', icon: '⚡' },
    { id: 'vault', label: 'Vault', icon: '🔐' },
    { id: 'analyze', label: 'Analyze', icon: '📊' },
  ];

  return (
    <>
      <header className="header">
        <div className="header-logo">
          <div className="header-icon"><ShieldIcon /></div>
          <div>
            <div className="header-title">FORT<span>RESS</span></div>
            <div className="header-subtitle">Password Manager</div>
          </div>
        </div>
        <div className="header-badge">Educational Use Only</div>
      </header>

      <nav className="nav">
        {tabs.map(t => (
          <button
            key={t.id}
            className={`nav-btn${tab === t.id ? ' active' : ''}`}
            onClick={() => setTab(t.id)}
          >
            <span>{t.icon}</span>
            {t.label}
            {t.id === 'vault' && entries.length > 0 && (
              <span className="nav-count">{entries.length}</span>
            )}
          </button>
        ))}
      </nav>

      <main className="main">
        {tab === 'generate' && (
          <GenerateTab entries={entries} updateEntries={updateEntries} />
        )}
        {tab === 'vault' && (
          <VaultTab entries={entries} updateEntries={updateEntries} />
        )}
        {tab === 'analyze' && <ScoreTab />}
      </main>

      <footer className="footer">
        ⚠️ Fortress uses educational encryption only — not intended for storing real credentials.
        All data is stored locally in your browser.
      </footer>
    </>
  );
}
