// Technical Cases UI Module
import { casesData } from '../data/casesData.js';

let currentLang = 'python';

export function renderTechnicalCases(containerEl, navContainerEl, mobileSelectEl) {
  if (!containerEl) return;

  // 1. Render Sidebar Nav Buttons
  if (navContainerEl) {
    navContainerEl.innerHTML = casesData.map((c, idx) => `
      <button onclick="window.selectCase('${c.id}')" id="nav-${c.id}" 
              class="w-full text-left p-3 rounded-xl border transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item ${idx === 0 ? 'active-nav border-blue-500 bg-blue-500/10' : 'border-slate-800'}">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-${c.color}-400">Case ${c.num}</span>
          <span class="text-[11px] px-1.5 py-0.5 rounded bg-${c.color}-500/10 text-${c.color}-400 font-semibold">${c.badge}</span>
        </div>
        <div class="text-xs font-semibold line-clamp-1 text-slate-100">${escapeHTML(c.title)}</div>
        <div class="text-[11px] text-slate-400">${escapeHTML(c.category)}</div>
      </button>
    `).join('');
  }

  // 2. Render Mobile Select Options
  if (mobileSelectEl) {
    mobileSelectEl.innerHTML = casesData.map(c => `
      <option value="${c.id}">Case ${c.num}: ${escapeHTML(c.title)} (${c.badge})</option>
    `).join('');
  }

  // 3. Render Case Panes
  containerEl.innerHTML = casesData.map((c, idx) => `
    <div id="${c.id}" class="case-detail-pane space-y-4 sm:space-y-6" style="display: ${idx === 0 ? 'block' : 'none'};">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-5">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
          <div>
            <span class="text-xs font-bold text-${c.color}-400 uppercase tracking-wider">Technical Case Study ${c.num}</span>
            <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">${escapeHTML(c.title)}</h2>
          </div>
          <div class="sm:text-right">
            <span class="text-[11px] font-medium text-slate-400">Recency & Difficulty:</span>
            <div class="text-xs font-bold text-${c.color}-400">${c.difficulty}</div>
          </div>
        </div>

        <!-- Question Prompt -->
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
          <span class="text-xs font-bold text-${c.color}-400 uppercase flex items-center gap-1.5">
            <span>❓</span> <span>Original Interview Question Prompt</span>
          </span>
          <p class="text-xs sm:text-sm italic text-slate-300 leading-relaxed">
            ${escapeHTML(c.prompt)}
          </p>
        </div>

        <!-- Legacy Buggy Code -->
        <div class="bg-slate-950 rounded-xl border border-rose-900/50 overflow-hidden space-y-0">
          <div class="bg-rose-950/60 px-4 py-2 border-b border-rose-900/50 flex items-center justify-between text-xs">
            <span class="font-bold text-rose-400 flex items-center gap-1.5">
              <span>⚠️</span> <span>Legacy Buggy Code (${c.legacyLang})</span>
            </span>
            <span class="text-rose-400/80 font-mono text-[11px]">Inspect & Debug</span>
          </div>
          <div class="p-4 overflow-x-auto font-mono text-xs bg-slate-950">
            <pre class="text-xs text-rose-200 leading-relaxed"><code>${escapeHTML(c.legacyCode)}</code></pre>
          </div>
        </div>

        <!-- Reveal Solution Toggle Button -->
        <div class="pt-2">
          <button onclick="window.toggleSolution('${c.id}')" id="sol-btn-${c.id}" class="w-full py-3 px-4 bg-slate-800 hover:bg-slate-750 text-blue-400 font-bold rounded-xl border border-slate-700 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all">
            <span class="flex items-center gap-2">
              <span>👁️</span> <span>Reveal Answer & Fixed Engineering Solution</span>
            </span>
            <span id="sol-icon-${c.id}">▼</span>
          </button>
        </div>

        <!-- Hidden Solution Container -->
        <div id="sol-container-${c.id}" class="space-y-4 pt-2" style="display: none;">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
              <h4 class="font-bold text-rose-400 uppercase text-xs">Identified Root Causes</h4>
              <ul class="space-y-1 text-slate-400">
                ${c.causes.map(cause => `<li>• ${escapeHTML(cause)}</li>`).join('')}
              </ul>
            </div>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
              <h4 class="font-bold text-emerald-400 uppercase text-xs">Architectural Solution</h4>
              <ul class="space-y-1 text-slate-400">
                ${c.solutions.map(sol => `<li>• ${escapeHTML(sol)}</li>`).join('')}
              </ul>
            </div>
          </div>

          <!-- Production Refactored Code Block -->
          <div class="bg-slate-950 rounded-xl border border-emerald-900/50 overflow-hidden">
            <div class="bg-emerald-950/40 px-4 py-2 border-b border-emerald-900/50 flex items-center justify-between text-xs">
              <span class="font-bold text-emerald-400 flex items-center gap-1.5">
                <span>✅</span> <span>Refactored Production Code</span>
              </span>
              <span class="text-slate-500 font-mono text-[11px]">Multi-Language Solution</span>
            </div>
            <div class="p-4 overflow-x-auto font-mono text-xs">
              <div class="code-block lang-python" style="display: ${currentLang === 'python' ? 'block' : 'none'};">
                <pre class="text-xs text-slate-200"><code>${escapeHTML(c.code.python)}</code></pre>
              </div>
              <div class="code-block lang-go" style="display: ${currentLang === 'go' ? 'block' : 'none'};">
                <pre class="text-xs text-slate-200"><code>${escapeHTML(c.code.go)}</code></pre>
              </div>
              <div class="code-block lang-java" style="display: ${currentLang === 'java' ? 'block' : 'none'};">
                <pre class="text-xs text-slate-200"><code>${escapeHTML(c.code.java)}</code></pre>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  `).join('');
}

export function selectCase(caseId) {
  casesData.forEach(c => {
    const casePane = document.getElementById(c.id);
    const navItem = document.getElementById('nav-' + c.id);
    if (c.id === caseId) {
      if (casePane) casePane.style.display = 'block';
      if (navItem) navItem.classList.add('border-blue-500', 'bg-blue-500/10');
    } else {
      if (casePane) casePane.style.display = 'none';
      if (navItem) navItem.classList.remove('border-blue-500', 'bg-blue-500/10');
    }
  });

  const mobileSelect = document.getElementById('mobile-case-select');
  if (mobileSelect) mobileSelect.value = caseId;
}

export function toggleSolution(caseId) {
  const container = document.getElementById('sol-container-' + caseId);
  const btn = document.getElementById('sol-btn-' + caseId);
  const icon = document.getElementById('sol-icon-' + caseId);

  if (!container || !btn) return;

  if (container.style.display === 'none') {
    container.style.display = 'block';
    btn.className = "w-full py-3 px-4 bg-blue-900/40 hover:bg-blue-900/60 text-blue-300 font-bold rounded-xl border border-blue-500/50 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all";
    btn.querySelector('span:first-child').innerHTML = "<span>🙈</span> <span>Hide Solution & Engineering Breakdown</span>";
    if (icon) icon.textContent = "▲";
  } else {
    container.style.display = 'none';
    btn.className = "w-full py-3 px-4 bg-slate-800 hover:bg-slate-750 text-blue-400 font-bold rounded-xl border border-slate-700 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all";
    btn.querySelector('span:first-child').innerHTML = "<span>👁️</span> <span>Reveal Answer & Fixed Engineering Solution</span>";
    if (icon) icon.textContent = "▼";
  }
}

export function setGlobalLang(lang) {
  currentLang = lang;
  ['python', 'go', 'java'].forEach(l => {
    const btn = document.getElementById('lang-btn-' + l);
    if (btn) {
      btn.className = (l === lang)
        ? "px-2.5 py-1 rounded-lg text-xs font-bold transition-all bg-blue-600 text-white shadow-xs border border-blue-400"
        : "px-2.5 py-1 rounded-lg text-xs font-bold transition-all text-slate-400 hover:text-white border border-transparent";
    }
  });

  document.querySelectorAll('.code-block').forEach(el => {
    if (el.classList.contains('lang-' + lang)) {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
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
