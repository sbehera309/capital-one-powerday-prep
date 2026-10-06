// Mock Interview & Self-Assessment Quiz UI Module

let timerInterval = null;
let timerSeconds = 2700; // 45 minutes

export function renderMockInterview(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Simulated PowerDay Session</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">45-Minute PowerDay Case Simulator</h2>
        </div>
        <div class="flex items-center gap-3 bg-slate-950 px-4 py-2 rounded-xl border border-slate-800">
          <span id="mock-timer-display" class="text-base font-extrabold text-amber-400 font-mono">45:00</span>
          <button id="mock-timer-btn" onclick="window.toggleMockTimer()" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-500 text-xs font-bold text-white shadow-xs">Start Timer</button>
        </div>
      </div>

      <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800 space-y-4">
        <h3 class="text-xs font-bold text-rose-400 uppercase tracking-wider">PowerDay Interview Strategy Protocol</h3>
        <ol class="space-y-2 text-xs text-slate-300 list-decimal list-inside">
          <li><strong>00:00 – 05:00:</strong> Solicit scale & non-functional requirements (QPS, RPO/RTO, read/write ratio).</li>
          <li><strong>05:00 – 15:00:</strong> Define high-level API schema and core database entities (OLTP vs OLAP).</li>
          <li><strong>15:00 – 35:00:</strong> Draw component topology, state machines, locking strategy, and message queue partitioning.</li>
          <li><strong>35:00 – 45:00:</strong> Address single points of failure, multi-region failover, and rate limiting limits.</li>
        </ol>
      </div>
    </div>
  `;
}

export function renderQuiz(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      <div class="border-b border-slate-800 pb-4">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Self-Assessment</span>
        <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">System Design & Tech Case Rapid Quiz</h2>
      </div>

      <div class="space-y-4">
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h3 class="text-xs font-bold text-slate-100">Q1: Which pagination technique prevents duplicate records under concurrent database writes?</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <button onclick="window.checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-xs text-left hover:border-slate-700">A) SQL OFFSET / LIMIT</button>
            <button onclick="window.checkAnswer(this, true)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-xs text-left hover:border-slate-700">B) Keyset / Cursor Pagination</button>
          </div>
          <div class="quiz-feedback hidden p-3 rounded-lg text-xs font-bold"></div>
        </div>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h3 class="text-xs font-bold text-slate-100">Q2: What is the optimal Redis lock acquisition command pattern?</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <button onclick="window.checkAnswer(this, true)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-xs text-left hover:border-slate-700">A) SET key val NX PX 5000</button>
            <button onclick="window.checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-xs text-left hover:border-slate-700">B) SETNX followed by EXPIRE</button>
          </div>
          <div class="quiz-feedback hidden p-3 rounded-lg text-xs font-bold"></div>
        </div>
      </div>
    </div>
  `;
}

export function toggleMockTimer() {
  const btn = document.getElementById('mock-timer-btn');
  const disp = document.getElementById('mock-timer-display');

  if (timerInterval) {
    clearInterval(timerInterval);
    timerInterval = null;
    if (btn) btn.textContent = "Resume Timer";
  } else {
    if (btn) btn.textContent = "Pause Timer";
    timerInterval = setInterval(() => {
      if (timerSeconds > 0) {
        timerSeconds--;
        const mins = Math.floor(timerSeconds / 60);
        const secs = timerSeconds % 60;
        if (disp) disp.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
      } else {
        clearInterval(timerInterval);
        if (disp) disp.textContent = "TIME EXPIRED!";
      }
    }, 1000);
  }
}

export function checkAnswer(btn, isCorrect) {
  const feedback = btn.parentElement.nextElementSibling;
  if (!feedback) return;
  feedback.classList.remove('hidden', 'bg-emerald-500/20', 'text-emerald-400', 'bg-rose-500/20', 'text-rose-400');
  if (isCorrect) {
    feedback.classList.add('bg-emerald-500/20', 'text-emerald-400');
    feedback.textContent = "✓ Correct! Excellent grasp of the architectural constraint.";
  } else {
    feedback.classList.add('bg-rose-500/20', 'text-rose-400');
    feedback.textContent = "✗ Incorrect. Review the case detail pane for the breakdown.";
  }
}
