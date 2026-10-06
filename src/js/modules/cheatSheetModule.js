// Comprehensive Cheat Sheet & Architectural Trade-offs Renderer Module
import { cheatsheetData } from '../data/cheatsheetData.js';

let activeCategory = 'all';

export function renderCheatSheet(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      
      <!-- Header & Quick Search -->
      <div class="border-b border-slate-800 pb-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-1.5">
            <span>⚡</span> <span>System Design & Cloud Architecture Field Guide</span>
          </span>
          <h2 class="text-xl sm:text-2xl font-extrabold text-white leading-tight mt-1">
            Capital One Enterprise Architecture & Trade-Offs
          </h2>
          <p class="text-xs text-slate-400 mt-1">
            Production-grade comparisons for AWS compute, database engines, networking, streaming, and distributed design patterns.
          </p>
        </div>

        <!-- Search input inside Cheat Sheet -->
        <div class="relative min-w-[240px]">
          <input 
            type="text" 
            id="cheatsheet-search" 
            oninput="window.filterCheatSheet()" 
            placeholder="Search Fargate, CDC, Redis, NLB..." 
            class="w-full pl-9 pr-4 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400 transition-all font-mono"
          />
          <svg class="w-4 h-4 text-slate-500 absolute left-3 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
        </div>
      </div>

      <!-- Navigation Category Filter Pills -->
      <div class="flex flex-wrap items-center gap-2 border-b border-slate-800/80 pb-4">
        <button onclick="window.setCheatCategory('all')" id="cs-btn-all" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-cyan-500 text-slate-950 shadow-sm">
          🌟 All Topics
        </button>
        <button onclick="window.setCheatCategory('compute')" id="cs-btn-compute" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          💻 AWS Compute Strategy
        </button>
        <button onclick="window.setCheatCategory('databases')" id="cs-btn-databases" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          🛢️ DB & Storage Matrix
        </button>
        <button onclick="window.setCheatCategory('networking')" id="cs-btn-networking" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          🌐 Networking & Load Balancers
        </button>
        <button onclick="window.setCheatCategory('streaming')" id="cs-btn-streaming" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          📡 Streaming & Messaging
        </button>
        <button onclick="window.setCheatCategory('patterns')" id="cs-btn-patterns" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          📐 Design Patterns & Guarantees
        </button>
        <button onclick="window.setCheatCategory('latency')" id="cs-btn-latency" class="cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800">
          ⏱️ Latency & SLA Reference
        </button>
      </div>

      <!-- Main Render Container -->
      <div id="cheatsheet-content-area" class="space-y-8">
        ${renderCheatSheetContent()}
      </div>
    </div>
  `;

  // Attach global functions for window interactivity
  window.setCheatCategory = (cat) => {
    activeCategory = cat;
    document.querySelectorAll('.cs-cat-btn').forEach(btn => {
      btn.className = 'cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-slate-800';
    });
    const activeBtn = document.getElementById(`cs-btn-${cat}`);
    if (activeBtn) {
      activeBtn.className = 'cs-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all bg-cyan-500 text-slate-950 shadow-sm';
    }
    const area = document.getElementById('cheatsheet-content-area');
    if (area) area.innerHTML = renderCheatSheetContent();
  };

  window.filterCheatSheet = () => {
    const input = document.getElementById('cheatsheet-search');
    if (!input) return;
    const query = input.value.toLowerCase().trim();
    
    document.querySelectorAll('.cs-searchable-card').forEach(card => {
      const text = card.innerText.toLowerCase();
      if (!query || text.includes(query)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  };
}

function renderCheatSheetContent() {
  let html = '';

  const showAll = activeCategory === 'all';

  // 1. Comparative Matrix Cards (Compute, Databases, Networking, Streaming)
  cheatsheetData.comparisons.forEach(comp => {
    if (showAll || activeCategory === comp.id) {
      html += renderComparisonSection(comp);
    }
  });

  // 2. System Design Architecture Patterns
  if (showAll || activeCategory === 'patterns') {
    html += renderPatternsSection();
  }

  // 3. Latency Numbers & SLA Reference
  if (showAll || activeCategory === 'latency') {
    html += renderLatencySection();
  }

  return html;
}

function renderComparisonSection(comp) {
  const badgeColors = {
    cyan: 'bg-cyan-500/10 text-cyan-400 border-cyan-500/30',
    emerald: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
    indigo: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/30',
    purple: 'bg-purple-500/10 text-purple-400 border-purple-500/30'
  };

  const currentBadgeClass = badgeColors[comp.color] || badgeColors.cyan;

  return `
    <div class="cs-searchable-card space-y-4">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border ${currentBadgeClass}">
            ${escapeHTML(comp.badge)}
          </span>
          <h3 class="text-base sm:text-lg font-bold text-white">${escapeHTML(comp.title)}</h3>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-${Math.min(comp.items.length, 3)} gap-4">
        ${comp.items.map(item => `
          <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col justify-between space-y-3 hover:border-slate-700 transition-all">
            <div>
              <h4 class="text-sm font-extrabold text-cyan-300 border-b border-slate-900 pb-2 mb-2 flex items-center justify-between">
                <span>${escapeHTML(item.name)}</span>
                ${item.type ? `<span class="text-[10px] text-slate-400 font-mono font-normal">(${escapeHTML(item.type)})</span>` : ''}
                ${item.layer ? `<span class="text-[10px] text-indigo-400 font-mono font-normal">${escapeHTML(item.layer)}</span>` : ''}
              </h4>

              ${item.bestFor ? `
                <div class="mb-3">
                  <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Target Use Case:</span>
                  <p class="text-xs text-slate-200 leading-relaxed font-medium mt-0.5">${escapeHTML(item.bestFor)}</p>
                </div>
              ` : ''}

              ${item.latency ? `
                <div class="mb-3 flex items-center gap-2 bg-slate-900/80 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
                  <span class="text-[10px] font-semibold text-slate-400">Latency Overhead:</span>
                  <span class="text-xs font-mono font-bold text-emerald-400">${escapeHTML(item.latency)}</span>
                </div>
              ` : ''}

              ${item.features ? `
                <div class="mb-3">
                  <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Key Features:</span>
                  <p class="text-xs text-slate-300 leading-relaxed mt-0.5">${escapeHTML(item.features)}</p>
                </div>
              ` : ''}

              ${item.pros ? `
                <div class="space-y-1 mb-2">
                  <span class="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block">PROS:</span>
                  <ul class="space-y-1 text-xs text-slate-300">
                    ${item.pros.map(p => `<li class="flex items-start gap-1.5"><span class="text-emerald-400 font-bold">✓</span> <span>${escapeHTML(p)}</span></li>`).join('')}
                  </ul>
                </div>
              ` : ''}

              ${item.cons ? `
                <div class="space-y-1 mb-2">
                  <span class="text-[10px] font-bold text-rose-400 uppercase tracking-wider block">CONS / LIMITATIONS:</span>
                  <ul class="space-y-1 text-xs text-slate-300">
                    ${item.cons.map(c => `<li class="flex items-start gap-1.5"><span class="text-rose-400 font-bold">✗</span> <span>${escapeHTML(c)}</span></li>`).join('')}
                  </ul>
                </div>
              ` : ''}

              ${item.keyPoints ? `
                <div class="space-y-1 mb-2">
                  <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Key Operational Highlights:</span>
                  <ul class="space-y-1 text-xs text-slate-300">
                    ${item.keyPoints.map(kp => `<li class="flex items-start gap-1.5"><span class="text-cyan-400">•</span> <span>${escapeHTML(kp)}</span></li>`).join('')}
                  </ul>
                </div>
              ` : ''}
            </div>

            ${item.verdict ? `
              <div class="pt-2 border-t border-slate-900 bg-cyan-950/20 p-2 rounded-lg border border-cyan-900/30">
                <span class="text-[10px] font-bold text-cyan-400 uppercase block">Capital One Architecture Verdict:</span>
                <p class="text-[11px] text-cyan-200 leading-tight mt-0.5">${escapeHTML(item.verdict)}</p>
              </div>
            ` : ''}
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function renderPatternsSection() {
  return `
    <div class="cs-searchable-card space-y-4">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border bg-amber-500/10 text-amber-400 border-amber-500/30">
            Design Patterns
          </span>
          <h3 class="text-base sm:text-lg font-bold text-white">Core System Architecture Design Patterns & Guarantees</h3>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        ${cheatsheetData.patterns.map(pat => `
          <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3 hover:border-slate-700 transition-all flex flex-col justify-between">
            <div class="space-y-2">
              <h4 class="text-sm font-extrabold text-amber-300 flex items-center gap-2">
                <span>${pat.icon}</span> <span>${escapeHTML(pat.title)}</span>
              </h4>
              
              <div class="bg-rose-950/20 p-3 rounded-lg border border-rose-900/30">
                <span class="text-[10px] font-bold text-rose-400 uppercase tracking-wider block">The Problem / Trap:</span>
                <p class="text-xs text-rose-200/90 leading-relaxed mt-0.5">${escapeHTML(pat.problem)}</p>
              </div>

              <div class="bg-emerald-950/20 p-3 rounded-lg border border-emerald-900/30">
                <span class="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block">Production Solution / Industry Standard:</span>
                <p class="text-xs text-emerald-200/90 leading-relaxed mt-0.5">${escapeHTML(pat.solution)}</p>
              </div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function renderLatencySection() {
  return `
    <div class="cs-searchable-card space-y-6">
      <!-- Latency Rules of Thumb -->
      <div class="space-y-3">
        <div class="flex items-center gap-2 border-b border-slate-800 pb-3">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border bg-cyan-500/10 text-cyan-400 border-cyan-500/30">
            Latency Matrix
          </span>
          <h3 class="text-base sm:text-lg font-bold text-white">Numbers Every Systems Architect Should Know</h3>
        </div>

        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-900 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800">
              <tr>
                <th class="p-3">Operation / Storage Layer</th>
                <th class="p-3">Typical Latency</th>
                <th class="p-3">Architectural Notes</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/80 text-slate-200">
              ${cheatsheetData.latencies.map(lat => `
                <tr class="hover:bg-slate-900/50 transition-colors">
                  <td class="p-3 font-semibold text-white">${escapeHTML(lat.operation)}</td>
                  <td class="p-3 font-mono font-bold text-cyan-400">${escapeHTML(lat.time)}</td>
                  <td class="p-3 text-slate-400">${escapeHTML(lat.notes)}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- Uptime SLA Breakdown -->
      <div class="space-y-3">
        <div class="flex items-center gap-2 border-b border-slate-800 pb-3">
          <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase border bg-amber-500/10 text-amber-400 border-amber-500/30">
            SLA & Downtime
          </span>
          <h3 class="text-base sm:text-lg font-bold text-white">Service Level Agreement (SLA) Downtime Budget</h3>
        </div>

        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-900 text-slate-400 uppercase text-[10px] font-bold tracking-wider border-b border-slate-800">
              <tr>
                <th class="p-3">Availability Level</th>
                <th class="p-3">Allowed Downtime / Year</th>
                <th class="p-3">Allowed Downtime / Month</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/80 text-slate-200">
              ${cheatsheetData.slas.map(s => `
                <tr class="hover:bg-slate-900/50 transition-colors">
                  <td class="p-3 font-extrabold text-amber-400 font-mono">${escapeHTML(s.sla)}</td>
                  <td class="p-3 font-mono text-slate-200">${escapeHTML(s.downtimeYear)}</td>
                  <td class="p-3 font-mono text-slate-400">${escapeHTML(s.downtimeMonth)}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
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
