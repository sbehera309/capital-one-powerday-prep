// Flashcards Deck & Review UI Module
import { flashcardsData } from '../data/flashcardsData.js';

let masteredCount = 0;

export function renderFlashcards(containerEl) {
  if (!containerEl) return;

  containerEl.innerHTML = `
    <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Interactive Study Deck</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Capital One Core Concept Flashcards</h2>
        </div>
        <div class="bg-slate-950 px-4 py-2 rounded-xl border border-slate-800 flex items-center gap-3">
          <span class="text-xs text-slate-400 font-medium">Mastery Progress:</span>
          <span id="flashcard-progress" class="text-xs font-bold text-emerald-400">0 / ${flashcardsData.length} Mastered</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        ${flashcardsData.map(card => `
          <div class="perspective-1000 h-64 cursor-pointer" onclick="window.flipCard(this)">
            <div class="flashcard-inner relative w-full h-full duration-500 rounded-2xl">
              <!-- Front -->
              <div class="flashcard-front absolute inset-0 bg-slate-950 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between shadow-md hover:border-indigo-500/50 transition-all">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">${card.category}</span>
                  <span class="text-xs text-slate-500">Click to Flip 🔄</span>
                </div>
                <h3 class="text-sm sm:text-base font-bold text-slate-100 leading-snug">${escapeHTML(card.front)}</h3>
                <div class="text-[11px] text-slate-500 font-mono text-right">Card #${card.id}</div>
              </div>

              <!-- Back -->
              <div class="flashcard-back absolute inset-0 bg-slate-900 border border-slate-700 rounded-2xl p-6 flex flex-col justify-between shadow-lg">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">Answer & Breakdown</span>
                  <span class="text-xs text-slate-500">Click to Flip 🔄</span>
                </div>
                <p class="text-xs sm:text-sm text-slate-200 leading-relaxed">${escapeHTML(card.back)}</p>
                <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                  <button onclick="event.stopPropagation(); window.markFlashcard(this, false)" class="text-[11px] font-bold text-slate-400 hover:text-slate-200">Needs Review</button>
                  <button onclick="event.stopPropagation(); window.markFlashcard(this, true)" class="text-[11px] font-bold text-emerald-400 hover:text-emerald-300 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">Mastered ✓</button>
                </div>
              </div>
            </div>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

export function flipCard(cardEl) {
  const inner = cardEl.querySelector('.flashcard-inner');
  if (inner) inner.classList.toggle('flipped');
}

export function markFlashcard(btn, isMastered) {
  const card = btn.closest('.perspective-1000');
  if (isMastered) {
    if (card) card.style.opacity = '0.5';
    masteredCount++;
  } else {
    if (card) card.style.opacity = '1';
  }
  const disp = document.getElementById('flashcard-progress');
  if (disp) disp.textContent = `${masteredCount} / ${flashcardsData.length} Mastered`;
}

function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
}
