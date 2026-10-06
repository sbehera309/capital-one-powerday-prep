// Cheat Sheet & Global Search Filter Module
import { cheatsheetData } from '../data/cheatsheetData.js';

export function renderCheatSheet(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      <div class="border-b border-slate-800 pb-4 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Quick Reference</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Capital One System Design & Architecture Patterns</h2>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${cheatsheetData.systemDesignPatterns.map(p => `
          <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
            <h3 class="text-xs font-bold text-cyan-400 uppercase flex items-center gap-1.5">
              <span>💡</span> <span>${escapeHTML(p.title)}</span>
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">${escapeHTML(p.desc)}</p>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

export function filterContent() {
  const searchInput = document.getElementById('searchInput');
  if (!searchInput) return;

  const query = searchInput.value.toLowerCase();
  document.querySelectorAll('.case-detail-pane, .sys-detail-pane').forEach(pane => {
    const text = pane.innerText.toLowerCase();
    pane.style.opacity = text.includes(query) ? '1' : '0.3';
  });
}

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
