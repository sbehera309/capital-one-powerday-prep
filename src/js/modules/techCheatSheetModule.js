// Technical Case Studies Cheat Sheet Module
import { techCheatSheetData } from '../data/techCheatSheetData.js';

let activeCategory = 'all';

export function renderTechCheatSheet(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      
      <!-- Header & Search -->
      <div class="border-b border-slate-800 pb-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
            <span>🧩</span> <span>Technical Case Study Field Guide</span>
          </span>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white leading-tight mt-1">
            Capital One Tech Case Cheat Sheet & Diagnostic Reference
          </h2>
          <p class="text-xs text-slate-400 mt-1">
            Master the 7 core technical case studies, code debugging patterns, financial formulas, and senior candidate interview talking points.
          </p>
        </div>

        <!-- Search Input -->
        <div class="relative min-w-[240px]">
          <input 
            type="text" 
            id="tech-cs-search" 
            oninput="window.filterTechCheatSheet()" 
            placeholder="Search Keyset, Redis SETNX, MDR, Kafka key..." 
            class="w-full pl-9 pr-4 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-400 focus:ring-1 focus:ring-blue-400 transition-all font-mono"
          />
          <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex flex-wrap items-center gap-2 border-b border-slate-800/80 pb-4">
        <button onclick="window.setTechCheatCategory('all')" id="tcs-btn-all" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-blue-600 text-white shadow-sm">
          🌟 All Tech Cases
        </button>
        <button onclick="window.setTechCheatCategory('db-pagination')" id="tcs-btn-db-pagination" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          🗄️ DB & Keyset Pagination
        </button>
        <button onclick="window.setTechCheatCategory('financial-math')" id="tcs-btn-financial-math" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          💵 Financial Math & Yield
        </button>
        <button onclick="window.setTechCheatCategory('concurrency')" id="tcs-btn-concurrency" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          🔐 Concurrency & Redis Locks
        </button>
        <button onclick="window.setTechCheatCategory('boolean-logic')" id="tcs-btn-boolean-logic" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          🧮 Majority Voting Logic
        </button>
        <button onclick="window.setTechCheatCategory('streaming')" id="tcs-btn-streaming" class="tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          📡 Kafka Partitioning
        </button>
      </div>

      <!-- Main Render Container -->
      <div id="tech-cheatsheet-content-area" class="space-y-8">
        ${renderTechCheatSheetContent()}
      </div>
    </div>
  `;

  // Attach global window handlers
  window.setTechCheatCategory = (cat) => {
    activeCategory = cat;
    document.querySelectorAll('.tcs-cat-btn').forEach(btn => {
      btn.className = 'tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800';
    });
    const activeBtn = document.getElementById(`tcs-btn-${cat}`);
    if (activeBtn) {
      activeBtn.className = 'tcs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-blue-600 text-white shadow-sm';
    }
    const area = document.getElementById('tech-cheatsheet-content-area');
    if (area) area.innerHTML = renderTechCheatSheetContent();
  };

  window.filterTechCheatSheet = () => {
    const input = document.getElementById('tech-cs-search');
    if (!input) return;
    const query = input.value.toLowerCase().trim();

    document.querySelectorAll('.tcs-searchable-card').forEach(card => {
      const text = card.innerText.toLowerCase();
      card.style.display = (!query || text.includes(query)) ? '' : 'none';
    });
  };
}

function renderTechCheatSheetContent() {
  let html = '';
  const showAll = activeCategory === 'all';

  // 1. Case-by-Case Deep-Dive Reference Cards
  html += `
    <div class="space-y-4">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <h3 class="text-base sm:text-lg font-extrabold text-white flex items-center gap-2">
          <span>📚</span> <span>Case-by-Case Deep-Dive Cheat Sheet Reference</span>
        </h3>
        <span class="text-xs text-slate-400 font-medium">7 Cases Covered</span>
      </div>

      <div class="grid grid-cols-1 gap-6">
        ${techCheatSheetData.caseBreakdowns
          .filter(c => showAll || activeCategory === c.category)
          .map(c => renderCaseCard(c)).join('')}
      </div>
    </div>
  `;

  // 2. Anti-Pattern Diagnostic Table
  if (showAll) {
    html += renderAntiPatternTable();
  }

  return html;
}

function renderCaseCard(c) {
  const badgeColors = {
    blue: 'bg-blue-500/10 text-blue-400 border-blue-500/30',
    cyan: 'bg-cyan-500/10 text-cyan-400 border-cyan-500/30',
    teal: 'bg-teal-500/10 text-teal-400 border-teal-500/30',
    indigo: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/30',
    rose: 'bg-rose-500/10 text-rose-400 border-rose-500/30',
    purple: 'bg-purple-500/10 text-purple-400 border-purple-500/30',
    amber: 'bg-amber-500/10 text-amber-400 border-amber-500/30'
  };

  const badgeClass = badgeColors[c.color] || badgeColors.blue;

  return `
    <div class="tcs-searchable-card bg-slate-950 p-4 sm:p-5 rounded-2xl border border-slate-800 space-y-4 shadow-sm hover:border-slate-700 transition-all">
      <!-- Title Bar -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-900 pb-3 gap-2">
        <div class="flex items-center gap-2.5">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border ${badgeClass}">
            Case ${c.caseNum} • ${escapeHTML(c.badge)}
          </span>
          <h4 class="text-base sm:text-lg font-bold text-white">${escapeHTML(c.title)}</h4>
        </div>
      </div>

      <!-- Problem vs Fix Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="bg-rose-950/20 p-3.5 rounded-xl border border-rose-900/40 space-y-1.5">
          <span class="text-[10px] font-bold text-rose-400 uppercase tracking-wider block flex items-center gap-1.5">
            <span>⚠️</span> <span>Legacy Code Flaw & Trap</span>
          </span>
          <p class="text-xs text-rose-200/90 leading-relaxed">${escapeHTML(c.bugDescription)}</p>
        </div>

        <div class="bg-emerald-950/20 p-3.5 rounded-xl border border-emerald-900/40 space-y-1.5">
          <span class="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block flex items-center gap-1.5">
            <span>✅</span> <span>Refactored Production Solution</span>
          </span>
          <p class="text-xs text-emerald-200/90 leading-relaxed">${escapeHTML(c.fixPattern)}</p>
        </div>
      </div>

      <!-- Code Snippet -->
      <div class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden">
        <div class="bg-slate-950 px-4 py-2 border-b border-slate-800 text-[11px] font-mono font-bold text-slate-400 flex items-center justify-between">
          <span>Production Fix Pattern Code</span>
          <span class="text-blue-400 font-normal text-[10px]">Reference Snippet</span>
        </div>
        <div class="p-3.5 overflow-x-auto font-mono text-xs text-slate-200">
          <pre><code>${escapeHTML(c.codeSnippet)}</code></pre>
        </div>
      </div>

      <!-- Formulas & Interviewer Pro Tip -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="bg-slate-900 p-3.5 rounded-xl border border-slate-800 space-y-1.5">
          <span class="text-[10px] font-bold text-cyan-400 uppercase tracking-wider block">Key Formulas & Complexity:</span>
          <ul class="space-y-1 text-slate-300">
            ${c.keyFormulas.map(kf => `<li class="flex items-start gap-1.5"><span class="text-cyan-400 font-bold">•</span> <span>${escapeHTML(kf)}</span></li>`).join('')}
          </ul>
        </div>

        <div class="bg-blue-950/20 p-3.5 rounded-xl border border-blue-900/30 space-y-1.5">
          <span class="text-[10px] font-bold text-blue-400 uppercase tracking-wider block flex items-center gap-1">
            <span>💡</span> <span>Interviewer Talking Point (Pro Tip)</span>
          </span>
          <p class="text-xs text-blue-200 leading-relaxed">${escapeHTML(c.interviewerProTip)}</p>
        </div>
      </div>
    </div>
  `;
}

function renderAntiPatternTable() {
  return `
    <div class="tcs-searchable-card space-y-4">
      <div class="flex items-center gap-2 border-b border-slate-800 pb-3">
        <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border bg-rose-500/10 text-rose-400 border-rose-500/30">
          Anti-Pattern Matrix
        </span>
        <h3 class="text-base sm:text-lg font-bold text-white">Common Technical Case Anti-Patterns & Quick Fixes</h3>
      </div>

      <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950">
        <table class="w-full text-left text-xs">
          <thead class="bg-slate-900 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800">
            <tr>
              <th class="p-3">Category</th>
              <th class="p-3">Buggy Anti-Pattern</th>
              <th class="p-3">Why It Fails (The Flaw)</th>
              <th class="p-3">Production Fix Pattern</th>
              <th class="p-3">Rule of Thumb</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/80 text-slate-200">
            ${techCheatSheetData.antiPatterns.map(ap => `
              <tr class="hover:bg-slate-900/50 transition-colors">
                <td class="p-3 font-bold text-blue-400">${escapeHTML(ap.category)}</td>
                <td class="p-3 font-mono text-rose-400 font-semibold">${escapeHTML(ap.buggyPattern)}</td>
                <td class="p-3 text-slate-300">${escapeHTML(ap.flaw)}</td>
                <td class="p-3 font-mono text-emerald-400 font-semibold">${escapeHTML(ap.fixPattern)}</td>
                <td class="p-3 text-slate-400 italic">${escapeHTML(ap.ruleOfThumb)}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;
}

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
