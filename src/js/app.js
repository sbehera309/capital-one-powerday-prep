// Master Application Orchestrator & Router

import { renderTechnicalCases, selectCase, toggleSolution, setGlobalLang } from './modules/casesModule.js';
import { renderTechCheatSheet } from './modules/techCheatSheetModule.js';
import { renderSystemDesign, selectSysQ, initSimulators, changeScenario, playFlow, pauseFlow, stepNextFlow, stepPrevFlow, resetFlow } from './modules/sysDesignModule.js';
import { renderFlashcards, flipCard, markFlashcard } from './modules/flashcardsModule.js';
import { renderCalculators, runCalculations } from './modules/calculatorsModule.js';
import { renderCheatSheet, filterContent } from './modules/cheatSheetModule.js';
import { renderMockInterview, renderQuiz, toggleMockTimer, checkAnswer } from './modules/quizModule.js';

// Expose handlers to global window object for HTML onclick bindings
window.switchTab = switchTab;
window.selectCase = selectCase;
window.selectSysQ = selectSysQ;
window.toggleSolution = toggleSolution;
window.setGlobalLang = setGlobalLang;
window.changeScenario = changeScenario;
window.playFlow = playFlow;
window.pauseFlow = pauseFlow;
window.stepNextFlow = stepNextFlow;
window.stepPrevFlow = stepPrevFlow;
window.resetFlow = resetFlow;
window.flipCard = flipCard;
window.markFlashcard = markFlashcard;
window.runCalculations = runCalculations;
window.filterContent = filterContent;
window.toggleMockTimer = toggleMockTimer;
window.checkAnswer = checkAnswer;

// Tab Navigation Manager
export function switchTab(tabId) {
  const tabs = [
    'tech-cases', 
    'tech-cheat-sheet', 
    'system-design', 
    'flashcards', 
    'mock-interview', 
    'calculators', 
    'cheat-sheet', 
    'quiz'
  ];
  
  tabs.forEach(t => {
    const tabEl = document.getElementById('tab-' + t);
    const btn = document.getElementById('tab-btn-' + t);
    if (t === tabId) {
      if (tabEl) tabEl.style.display = 'block';
      if (btn) {
        btn.className = "flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all bg-blue-600 text-white shadow-xs flex items-center gap-1.5 min-h-[38px]";
      }
    } else {
      if (tabEl) tabEl.style.display = 'none';
      if (btn) {
        btn.className = "flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]";
      }
    }
  });
}

// Initialize App on DOM Content Loaded
document.addEventListener('DOMContentLoaded', () => {
  // Render Tab Views dynamically from ES Modules
  renderTechnicalCases(
    document.getElementById('tech-cases-content'),
    document.getElementById('tech-cases-sidebar'),
    document.getElementById('mobile-case-select')
  );

  renderTechCheatSheet(document.getElementById('tab-tech-cheat-sheet'));

  renderSystemDesign(
    document.getElementById('system-design-content'),
    document.getElementById('system-design-sidebar'),
    document.getElementById('mobile-sys-select')
  );

  renderFlashcards(document.getElementById('tab-flashcards'));
  renderCalculators(document.getElementById('tab-calculators'));
  renderCheatSheet(document.getElementById('tab-cheat-sheet'));
  renderMockInterview(document.getElementById('tab-mock-interview'));
  renderQuiz(document.getElementById('tab-quiz'));

  // Default Tab State
  switchTab('tech-cases');
  selectCase('case-1');
  selectSysQ('sys-q1');
  setGlobalLang('python');
});
