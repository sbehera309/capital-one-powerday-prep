// Sizing Math & System Design Calculators Module
import { cheatsheetData } from '../data/cheatsheetData.js';

export function renderCalculators(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      <div class="border-b border-slate-800 pb-4">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Back-of-the-Envelope Math</span>
        <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">System Sizing & Capacity Calculators</h2>
      </div>

      <!-- Reference Rules of Thumb -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        ${cheatsheetData.sizingMath.map(item => `
          <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1">
            <span class="text-[11px] font-bold text-amber-400 uppercase">${escapeHTML(item.label)}</span>
            <div class="text-sm font-extrabold text-slate-100">${escapeHTML(item.value)}</div>
          </div>
        `).join('')}
      </div>

      <!-- Interactive QPS & Storage Calculator -->
      <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-4">
        <h3 class="text-sm font-bold text-white uppercase flex items-center gap-2">
          <span>🧮</span> <span>Interactive Capacity Estimator</span>
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs">
          <div>
            <label class="block text-slate-400 mb-1 font-medium">Daily Active Users (DAU):</label>
            <input type="number" id="calc-dau" value="10000000" oninput="window.runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-white font-mono font-bold">
          </div>
          <div>
            <label class="block text-slate-400 mb-1 font-medium">Requests / User / Day:</label>
            <input type="number" id="calc-req" value="20" oninput="window.runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-white font-mono font-bold">
          </div>
          <div>
            <label class="block text-slate-400 mb-1 font-medium">Avg Request Size (KB):</label>
            <input type="number" id="calc-size" value="2" oninput="window.runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-white font-mono font-bold">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-3 border-t border-slate-800 text-center">
          <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-[11px] text-slate-400 block">Average QPS</span>
            <span id="res-avg-qps" class="text-lg font-extrabold text-cyan-400">2,314 QPS</span>
          </div>
          <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-[11px] text-slate-400 block">Peak QPS (2x)</span>
            <span id="res-peak-qps" class="text-lg font-extrabold text-blue-400">4,629 QPS</span>
          </div>
          <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-[11px] text-slate-400 block">Daily Storage Bandwidth</span>
            <span id="res-storage" class="text-lg font-extrabold text-emerald-400">400 GB / Day</span>
          </div>
        </div>
      </div>
    </div>
  `;

  runCalculations();
}

export function runCalculations() {
  const dauEl = document.getElementById('calc-dau');
  const reqEl = document.getElementById('calc-req');
  const sizeEl = document.getElementById('calc-size');

  if (!dauEl || !reqEl || !sizeEl) return;

  const dau = parseFloat(dauEl.value) || 0;
  const req = parseFloat(reqEl.value) || 0;
  const sizeKb = parseFloat(sizeEl.value) || 0;

  const totalReqPerDay = dau * req;
  const avgQps = Math.round(totalReqPerDay / 86400);
  const peakQps = Math.round(avgQps * 2);
  const dailyGb = (totalReqPerDay * sizeKb) / (1024 * 1024);

  const avgQpsEl = document.getElementById('res-avg-qps');
  const peakQpsEl = document.getElementById('res-peak-qps');
  const storageEl = document.getElementById('res-storage');

  if (avgQpsEl) avgQpsEl.textContent = avgQps.toLocaleString() + " QPS";
  if (peakQpsEl) peakQpsEl.textContent = peakQps.toLocaleString() + " QPS";
  if (storageEl) storageEl.textContent = dailyGb.toFixed(1) + " GB / Day";
}

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
