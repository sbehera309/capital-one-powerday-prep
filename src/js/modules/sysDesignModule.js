// System Design UI & Interactive SVG Simulator Module
import { sysDesignQuestions, sysSimData } from '../data/sysDesignData.js';

let activeSimState = {};

export function renderSystemDesign(containerEl, navContainerEl, mobileSelectEl) {
  if (!containerEl) return;

  // 1. Render Sidebar Nav Buttons
  if (navContainerEl) {
    navContainerEl.innerHTML = sysDesignQuestions.map((q, idx) => `
      <button onclick="window.selectSysQ('${q.id}')" id="nav-${q.id}" 
              class="w-full text-left p-3 rounded-xl border transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item ${idx === 0 ? 'active-nav border-blue-500 bg-blue-500/10' : 'border-slate-800'}">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-${q.color}-400">Question ${q.num}</span>
          <span class="text-[11px] px-1.5 py-0.5 rounded bg-${q.color}-500/10 text-${q.color}-400 font-semibold">${q.recency.split('•')[0]}</span>
        </div>
        <div class="text-xs font-semibold line-clamp-1 text-slate-100">${escapeHTML(q.title)}</div>
        <div class="text-[11px] text-slate-400">${escapeHTML(q.archBadge)}</div>
      </button>
    `).join('');
  }

  // 2. Render Mobile Select Options
  if (mobileSelectEl) {
    mobileSelectEl.innerHTML = sysDesignQuestions.map(q => `
      <option value="${q.id}">Q${q.num}: ${escapeHTML(q.title)} (${q.recency.split('•')[0]})</option>
    `).join('');
  }

  // 3. Render System Design Panes & Interactive Topology Simulators
  containerEl.innerHTML = sysDesignQuestions.map((q, idx) => {
    const simKey = q.id.replace('sys-', '');
    const sim = sysSimData[simKey] || sysSimData['q1'];
    const nodes = sim.scenarios[0].nodes;

    return `
      <div id="${q.id}" class="sys-detail-pane space-y-4 sm:space-y-6" style="display: ${idx === 0 ? 'block' : 'none'};">
        <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
            <div>
              <span class="text-xs font-bold text-${q.color}-400 uppercase tracking-wider">System Design Question ${q.num}</span>
              <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">${escapeHTML(q.title)}</h2>
            </div>
            <div class="sm:text-right">
              <span class="text-[11px] font-medium text-slate-400">Recency & Impact:</span>
              <div class="text-xs font-bold text-${q.color}-400">${q.recency}</div>
            </div>
          </div>

          <!-- Requirements -->
          <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-xs font-bold text-${q.color}-400 uppercase flex items-center gap-1.5">
              <span>📋</span> <span>Key System Requirements & Scale</span>
            </span>
            <ul class="space-y-1 text-xs text-slate-300">
              ${q.requirements.map(req => `<li>• ${escapeHTML(req)}</li>`).join('')}
            </ul>
          </div>

          <!-- Interactive Topology Simulator Header -->
          <div class="border border-blue-500/30 bg-slate-900 rounded-2xl overflow-hidden shadow-lg">
            <div class="bg-slate-950 px-4 py-3 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <span class="text-xs font-bold text-white uppercase tracking-wider">Live Animated Topology Simulator</span>
              </div>
              <div class="flex items-center gap-2">
                <label class="text-[11px] font-medium text-slate-400">Scenario:</label>
                <select id="${simKey}-scenario-select" onchange="window.changeScenario('${simKey}', this.value)" class="bg-slate-850 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:outline-none focus:border-blue-500">
                  ${sim.scenarios.map((scen, sIdx) => `<option value="${sIdx}">${escapeHTML(scen.name)}</option>`).join('')}
                </select>
              </div>
            </div>

            <!-- Dynamic Multi-Tier Architectural Topology Diagram Area -->
            <div class="p-4 sm:p-6 space-y-4">
              <div class="grid grid-cols-1 gap-1 relative">
                ${nodes.map((node, nIdx) => `
                  <!-- Node ${nIdx + 1} -->
                  <div id="${simKey}-node-${nIdx + 1}" class="cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-950 transition-all duration-300 relative group ${nIdx === 0 ? 'border-blue-500 bg-blue-500/20 node-active' : ''}">
                    <div class="flex items-center justify-between">
                      <span id="${simKey}-node-${nIdx + 1}-title" class="text-xs font-bold text-white">${escapeHTML(node.title)}</span>
                      <span id="${simKey}-node-${nIdx + 1}-badge" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 font-bold text-[9px]">${nIdx === 0 ? 'ACTIVE' : 'WAITING'}</span>
                    </div>
                    <div id="${simKey}-node-${nIdx + 1}-sub" class="text-[11px] text-slate-400 mt-0.5">${escapeHTML(node.sub)}</div>
                  </div>

                  ${nIdx < nodes.length - 1 ? `
                    <!-- Flow Line ${nIdx} -> ${nIdx + 1} -->
                    <div class="w-full h-6 relative my-0.5">
                      <svg class="w-full h-full absolute inset-0 pointer-events-none" preserveAspectRatio="none" viewBox="0 0 400 24">
                        <path id="${simKey}-line-${nIdx}-${nIdx + 1}" class="flow-line" d="M 200 0 L 200 24" />
                      </svg>
                    </div>
                  ` : ''}
                `).join('')}
              </div>

              <!-- Interactive Step Inspector Controls -->
              <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                  <span id="${simKey}-step-title" class="text-xs font-bold text-blue-400">Step 1: Initiation</span>
                  <span id="${simKey}-step-protocol" class="text-[11px] font-mono text-cyan-400">HTTP/2 TLS 1.3</span>
                </div>
                <p id="${simKey}-step-action" class="text-xs text-slate-300 leading-relaxed">Click play or step through to simulate high-throughput traffic flow.</p>
                <div class="flex items-center gap-2 pt-1">
                  <button onclick="window.stepPrevFlow('${simKey}')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300">⏮ Prev</button>
                  <button id="${simKey}-play-btn" onclick="window.playFlow('${simKey}')" class="px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow-xs">▶ Play Animation</button>
                  <button onclick="window.stepNextFlow('${simKey}')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300">Next ⏭</button>
                  <button onclick="window.resetFlow('${simKey}')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-400 ml-auto">🔄 Reset</button>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    `;
  }).join('');

  // Initialize simulator state for Q1 to Q9
  initSimulators();
}

export function selectSysQ(sysId) {
  sysDesignQuestions.forEach(sq => {
    const sysPane = document.getElementById(sq.id);
    const navItem = document.getElementById('nav-' + sq.id);
    if (sq.id === sysId) {
      if (sysPane) sysPane.style.display = 'block';
      if (navItem) navItem.classList.add('border-blue-500', 'bg-blue-500/10');
    } else {
      if (sysPane) sysPane.style.display = 'none';
      if (navItem) navItem.classList.remove('border-blue-500', 'bg-blue-500/10');
    }
  });

  const mobileSelect = document.getElementById('mobile-sys-select');
  if (mobileSelect) mobileSelect.value = sysId;

  const qId = sysId.replace('sys-', '');
  if (activeSimState[qId]) {
    renderSimStep(qId);
  }
}

export function initSimulators() {
  ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'].forEach(qId => {
    activeSimState[qId] = {
      scenarioIdx: 0,
      stepIdx: 0,
      isPlaying: false,
      timer: null
    };
    renderSimStep(qId);
  });
}

export function changeScenario(qId, sIdx) {
  if (!activeSimState[qId]) return;
  if (activeSimState[qId].timer) clearInterval(activeSimState[qId].timer);
  activeSimState[qId].scenarioIdx = parseInt(sIdx);
  activeSimState[qId].stepIdx = 0;
  activeSimState[qId].isPlaying = false;
  updatePlayBtnText(qId);
  renderSimStep(qId);
}

export function playFlow(qId) {
  if (!activeSimState[qId]) return;
  const state = activeSimState[qId];
  if (state.isPlaying) {
    pauseFlow(qId);
  } else {
    state.isPlaying = true;
    updatePlayBtnText(qId);
    state.timer = setInterval(() => {
      const data = sysSimData[qId] || sysSimData['q1'];
      const maxSteps = data.scenarios[state.scenarioIdx].steps.length;
      state.stepIdx = (state.stepIdx + 1) % maxSteps;
      renderSimStep(qId);
    }, 2000);
  }
}

export function pauseFlow(qId) {
  if (!activeSimState[qId]) return;
  const state = activeSimState[qId];
  state.isPlaying = false;
  if (state.timer) clearInterval(state.timer);
  updatePlayBtnText(qId);
}

export function stepNextFlow(qId) {
  if (!activeSimState[qId]) return;
  pauseFlow(qId);
  const data = sysSimData[qId] || sysSimData['q1'];
  const maxSteps = data.scenarios[activeSimState[qId].scenarioIdx].steps.length;
  activeSimState[qId].stepIdx = (activeSimState[qId].stepIdx + 1) % maxSteps;
  renderSimStep(qId);
}

export function stepPrevFlow(qId) {
  if (!activeSimState[qId]) return;
  pauseFlow(qId);
  const data = sysSimData[qId] || sysSimData['q1'];
  const maxSteps = data.scenarios[activeSimState[qId].scenarioIdx].steps.length;
  activeSimState[qId].stepIdx = (activeSimState[qId].stepIdx - 1 + maxSteps) % maxSteps;
  renderSimStep(qId);
}

export function resetFlow(qId) {
  if (!activeSimState[qId]) return;
  pauseFlow(qId);
  activeSimState[qId].stepIdx = 0;
  renderSimStep(qId);
}

function renderSimStep(qId) {
  const state = activeSimState[qId];
  const data = sysSimData[qId] || sysSimData['q1'];
  if (!state || !data) return;

  const scenario = data.scenarios[state.scenarioIdx];
  const step = scenario.steps[state.stepIdx];
  const nodeCount = scenario.nodes.length;

  // Dynamically update SVG line highlighting
  for (let l = 0; l < nodeCount - 1; l++) {
    const lId = `line-${l}-${l + 1}`;
    const lineEl = document.getElementById(qId + '-' + lId);
    if (lineEl) {
      lineEl.setAttribute('class', (step.lineId === lId) ? "flow-line-active" : "flow-line");
    }
  }

  // Dynamically update Node states
  for (let i = 1; i <= nodeCount; i++) {
    const nodeEl = document.getElementById(qId + '-node-' + i);
    const titleEl = document.getElementById(qId + '-node-' + i + '-title');
    const subEl = document.getElementById(qId + '-node-' + i + '-sub');
    const badgeEl = document.getElementById(qId + '-node-' + i + '-badge');

    const nodeData = scenario.nodes[i - 1];
    if (nodeData && titleEl && subEl) {
      titleEl.textContent = nodeData.title;
      subEl.textContent = nodeData.sub;
    }

    if (nodeEl) {
      if (i - 1 === step.nodeIdx) {
        nodeEl.className = "cursor-pointer p-3 rounded-xl border border-blue-500 bg-blue-500/25 shadow-lg shadow-blue-500/25 transition-all duration-300 relative group node-active";
        if (badgeEl) {
          badgeEl.textContent = step.badge || 'ACTIVE';
          badgeEl.className = "px-1.5 py-0.5 rounded bg-blue-600 text-white font-bold text-[9px]";
        }
      } else if (i - 1 < step.nodeIdx) {
        nodeEl.className = "cursor-pointer p-3 rounded-xl border border-emerald-500/40 bg-emerald-500/10 transition-all duration-300 relative group opacity-85";
        if (badgeEl) {
          badgeEl.textContent = 'DONE';
          badgeEl.className = "px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold text-[9px]";
        }
      } else {
        nodeEl.className = "cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-950 transition-all duration-300 relative group opacity-60";
        if (badgeEl) {
          badgeEl.textContent = 'WAITING';
          badgeEl.className = "px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 font-bold text-[9px]";
        }
      }
    }
  }

  // Update Inspector Panel
  const titleInspector = document.getElementById(qId + '-step-title');
  const protoInspector = document.getElementById(qId + '-step-protocol');
  const actionInspector = document.getElementById(qId + '-step-action');

  if (titleInspector) titleInspector.textContent = step.title;
  if (protoInspector) protoInspector.textContent = step.protocol;
  if (actionInspector) actionInspector.textContent = step.action;
}

function updatePlayBtnText(qId) {
  const btn = document.getElementById(qId + '-play-btn');
  if (btn && activeSimState[qId]) {
    if (activeSimState[qId].isPlaying) {
      btn.textContent = "⏸ Pause";
      btn.className = "px-4 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow-xs";
    } else {
      btn.textContent = "▶ Play Animation";
      btn.className = "px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow-xs";
    }
  }
}

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
