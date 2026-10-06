import os

def create_index_html():
    target_path = "/Users/sandeepbehera/.gemini/antigravity/scratch/capital-one-prep-app/index.html"
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Capital One PowerDay Prep - Technical Case & System Design</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    pre code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    button, input, select { touch-action: manipulation; }
    
    .perspective-1000 { perspective: 1000px; }
    .flashcard-inner { transition: transform 0.6s; transform-style: preserve-3d; }
    .flashcard-inner.flipped { transform: rotateY(180deg); }
    .flashcard-front, .flashcard-back { backface-visibility: hidden; -webkit-backface-visibility: hidden; }
    .flashcard-back { transform: rotateY(180deg); }

    .step-active {
      border-color: #3b82f6 !important;
      background-color: rgba(59, 130, 246, 0.15) !important;
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.3);
    }
  </style>
</head>
<body class="bg-slate-900 text-slate-100 antialiased font-sans min-h-screen pb-12">
  
  <!-- Header Banner -->
  <header class="border-b border-slate-800 bg-slate-900/90 sticky top-0 z-50 shadow-sm backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 py-3 space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white font-bold text-lg shadow flex-shrink-0">
            C1
          </div>
          <div>
            <h1 class="text-base sm:text-lg font-bold text-white leading-tight">Capital One PowerDay Prep</h1>
            <p class="text-[11px] sm:text-xs text-slate-400">Technical Case & System Design Compendium (2025–2026)</p>
          </div>
        </div>

        <!-- Global Language Selector -->
        <div class="flex items-center gap-1 bg-slate-950 border border-slate-800 p-1 rounded-xl shadow-xs">
          <span class="text-[10px] uppercase font-bold text-slate-500 px-1.5 hidden sm:inline">Code:</span>
          <button onclick="setGlobalLang('python')" id="lang-btn-python" class="px-2.5 py-1 rounded-lg text-xs font-bold transition-all bg-blue-600 text-white shadow-xs border border-blue-400">
            Python
          </button>
          <button onclick="setGlobalLang('go')" id="lang-btn-go" class="px-2.5 py-1 rounded-lg text-xs font-bold transition-all text-slate-400 hover:text-white border border-transparent">
            Go
          </button>
          <button onclick="setGlobalLang('java')" id="lang-btn-java" class="px-2.5 py-1 rounded-lg text-xs font-bold transition-all text-slate-400 hover:text-white border border-transparent">
            Java
          </button>
        </div>
      </div>

      <!-- Main Navigation Bar -->
      <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar pb-1 border-t border-slate-800 pt-2.5">
        <button onclick="switchTab('tech-cases')" id="tab-btn-tech-cases" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all bg-blue-600 text-white shadow-xs flex items-center gap-1.5 min-h-[38px]">
          <span>📋</span> <span>Tech Cases</span>
        </button>
        <button onclick="switchTab('system-design')" id="tab-btn-system-design" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>🏗️</span> <span>System Design</span>
        </button>
        <button onclick="switchTab('flashcards')" id="tab-btn-flashcards" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>🎴</span> <span>Flashcards</span>
        </button>
        <button onclick="switchTab('mock-interview')" id="tab-btn-mock-interview" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>⏱️</span> <span>Mock Interview</span>
        </button>
        <button onclick="switchTab('calculators')" id="tab-btn-calculators" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>🧮</span> <span>Sizing Math</span>
        </button>
        <button onclick="switchTab('cheat-sheet')" id="tab-btn-cheat-sheet" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>💡</span> <span>Cheat Sheet</span>
        </button>
        <button onclick="switchTab('quiz')" id="tab-btn-quiz" class="flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]">
          <span>⚡</span> <span>Practice Quiz</span>
        </button>
      </div>
    </div>
  </header>

  <main class="max-w-7xl mx-auto px-4 py-4 sm:py-6 space-y-4 sm:space-y-6">

    <!-- Global Search Bar -->
    <div class="bg-slate-850 border border-slate-800 p-2.5 sm:p-3 rounded-xl shadow-xs">
      <div class="relative">
        <input type="text" id="searchInput" onkeyup="filterContent()" placeholder="Search Technical Cases, System Design, APIs, Redis Lua, Flink, Kafka..." 
               class="w-full pl-9 pr-4 py-2 text-xs rounded-lg border border-slate-700 bg-slate-950 text-slate-100 focus:outline-none focus:ring-2 focus:ring-blue-500 min-h-[40px]">
        <svg class="w-4 h-4 absolute left-3 top-3 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
        </svg>
      </div>
    </div>

    <!-- TAB 1: TECHNICAL CASES (FULL RESTORED CASES 1 TO 7) -->
    <div id="tab-tech-cases" class="tab-content space-y-4">
      <div class="block lg:hidden bg-slate-850 border border-slate-800 p-3 rounded-xl shadow-xs space-y-2">
        <label class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block">Select Case Study:</label>
        <select id="mobile-case-select" onchange="selectCase(this.value)" class="w-full p-2.5 text-xs rounded-lg border border-slate-700 bg-slate-950 text-slate-100 font-semibold min-h-[44px]">
          <option value="case-1">Case 1: "Eeno" Customer History Retrieval</option>
          <option value="case-2">Case 2: Virtual Card Generation (Serverless vs ECS)</option>
          <option value="case-3">Case 3: 3-Boolean Security Alert Logic</option>
          <option value="case-4">Case 4: Mainframe to Real-Time Kafka Streaming</option>
          <option value="case-5">Case 5: Mobile Payments Unit Economics</option>
          <option value="case-6">Case 6: BNPL Cash Flow & MDR Yield Model (NEW)</option>
          <option value="case-7">Case 7: Real-Time Cross-Border FX Settlement (NEW)</option>
        </select>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Sidebar Navigation -->
        <div class="hidden lg:block lg:col-span-1 space-y-2">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 px-2 mb-2">Technical Case Studies</h3>
          
          <button onclick="selectCase('case-1')" id="nav-case-1" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item active-nav border-blue-500 bg-blue-500/10">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-blue-400">Case 1</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-blue-500/10 text-blue-400 font-semibold">Late 2025</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">"Eeno" Customer History</div>
            <div class="text-[11px] text-slate-400">Network & Dynamic Windowing</div>
          </button>

          <button onclick="selectCase('case-2')" id="nav-case-2" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-400">Case 2</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-semibold">Mid 2025</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Virtual Card Generation</div>
            <div class="text-[11px] text-slate-400">Serverless vs ECS & Logic Bug</div>
          </button>

          <button onclick="selectCase('case-3')" id="nav-case-3" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-amber-400">Case 3</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400 font-semibold">Mid 2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">3-Boolean Security Alert</div>
            <div class="text-[11px] text-slate-400">De Morgan's & Truth Table</div>
          </button>

          <button onclick="selectCase('case-4')" id="nav-case-4" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-purple-400">Case 4</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-purple-500/10 text-purple-400 font-semibold">Early 2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Mainframe to Kafka</div>
            <div class="text-[11px] text-slate-400">Fraud ROI ($1.25M) & Dual-Write</div>
          </button>

          <button onclick="selectCase('case-5')" id="nav-case-5" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-rose-400">Case 5</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-rose-500/10 text-rose-400 font-semibold">2023-2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Mobile Payments Economics</div>
            <div class="text-[11px] text-slate-400">Break-Even & Margin Math</div>
          </button>

          <button onclick="selectCase('case-6')" id="nav-case-6" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-cyan-400">Case 6</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-cyan-500/10 text-cyan-400 font-semibold">2025-2026</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">BNPL Cash Flow & MDR</div>
            <div class="text-[11px] text-slate-400">Installment Loss & Capital Yield</div>
          </button>

          <button onclick="selectCase('case-7')" id="nav-case-7" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 case-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-400">Case 7</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-teal-500/10 text-teal-400 font-semibold">2025-2026</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Cross-Border FX Settlement</div>
            <div class="text-[11px] text-slate-400">Spread Engine & Liquidity Buffer</div>
          </button>
        </div>

        <!-- Case Detail Panes -->
        <div class="lg:col-span-3 space-y-6">
          
          <!-- CASE 1 -->
          <div id="case-1" class="case-detail-pane space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Technical Case 1</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">"Eeno" Real-Time Customer History Retrieval & Network Optimization</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">Late 2025 – 2026 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800">
                <h4 class="text-xs font-bold text-slate-200 uppercase mb-1">Business Context</h4>
                <p class="text-xs sm:text-sm text-slate-400 leading-relaxed">
                  Capital One utilizes an intelligent conversational AI assistant named "Eeno" to address customer mobile app queries (e.g., "Why was my card declined?"). To evaluate context, the assistant queries an underlying event store for recent customer actions. You are presented with a legacy retrieval function, asked to evaluate its complexity, refactor it to accept dynamic windows, and optimize the distributed architecture.
                </p>
              </div>

              <div class="space-y-3">
                <h3 class="text-sm sm:text-base font-bold text-white">Part A: Legacy Code Analysis & Evaluation</h3>
                <div class="p-3.5 rounded-xl bg-amber-500/5 border border-amber-500/20 text-xs space-y-2">
                  <p class="font-semibold text-amber-400">Legacy Python Function:</p>
                  <pre class="bg-slate-950 p-3 rounded-lg border border-slate-800 text-slate-200 overflow-x-auto"><code>def retrieve_recent(self, customer_id, curr_time):
    result = []
    for i in range(5):
        val = self.store.retrieve(customer_id, curr_time - 5 + i + 1)
        if val is not None:
            result.append(val)
    return result</code></pre>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div class="bg-slate-950 border border-slate-800 p-3.5 rounded-xl space-y-1">
                    <span class="text-xs font-bold text-blue-400">Q1: Complexity & Network</span>
                    <p class="text-xs text-slate-400">Time complexity is <strong>O(T)</strong> where T = 5. Makes 5 sequential point-lookup network round-trips returning records from <code>curr_time - 4</code> to <code>curr_time</code>.</p>
                  </div>
                  <div class="bg-slate-950 border border-slate-800 p-3.5 rounded-xl space-y-1">
                    <span class="text-xs font-bold text-blue-400">Q2: Dynamic Window</span>
                    <p class="text-xs text-slate-400">Refactor to accept dynamic window <strong>T (in minutes)</strong> starting from <code>curr_time - time_window_minutes + 1</code>.</p>
                  </div>
                  <div class="bg-slate-950 border border-slate-800 p-3.5 rounded-xl space-y-1">
                    <span class="text-xs font-bold text-rose-400">Q3: Bottleneck at Scale</span>
                    <p class="text-xs text-slate-400">Iterating minute-by-minute introduces the <strong>Chatty API / N+1 Query anti-pattern</strong>. If T=60, service executes 60 sequential database roundtrips!</p>
                  </div>
                </div>
              </div>

              <!-- Multi-Language Snippet Header -->
              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> Optimized Code Solution (O(1) Single Partition Range Query)
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>class CustomerDataStore:
    def __init__(self, storage_client):
        self.store = storage_client

    def retrieve_recent(self, customer_id: int, curr_time: int, time_window_minutes: int) -> list:
        if time_window_minutes <= 0:
            return []
        start_time = curr_time - time_window_minutes + 1
        return self.store.retrieve_range(
            partition_key=customer_id,
            start_timestamp=start_time,
            end_timestamp=curr_time
        )</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>package main

type StorageClient interface {
	RetrieveRange(customerID int64, startTimestamp, endTimestamp int64) ([]string, error)
}

type CustomerDataStore struct {
	store StorageClient
}

func (cds *CustomerDataStore) RetrieveRecent(customerID int64, currTime int64, timeWindowMinutes int64) ([]string, error) {
	if timeWindowMinutes <= 0 { return []string{}, nil }
	startTime := currTime - timeWindowMinutes + 1
	return cds.store.RetrieveRange(customerID, startTime, currTime)
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>package com.capitalone.prep;
import java.util.Collections;
import java.util.List;

public class CustomerDataStore {
    private final StorageClient store;
    public CustomerDataStore(StorageClient store) { this.store = store; }

    public List&lt;String&gt; retrieveRecent(long customerId, long currTime, long timeWindowMinutes) {
        if (timeWindowMinutes <= 0) return Collections.emptyList();
        long startTime = currTime - timeWindowMinutes + 1;
        return store.retrieveRange(customerId, startTime, currTime);
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 2 -->
          <div id="case-2" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Technical Case 2</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Virtual Card Generation (Serverless vs. ECS Fargate TCO & Logic Bug)</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">Mid 2025 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-emerald-400 uppercase">Financial TCO Analysis: Serverless vs. ECS Fargate</h4>
                <p class="text-xs text-slate-300 leading-relaxed">
                  • <strong>Serverless (Lambda + DynamoDB):</strong> $1,330/month at 60M monthly active virtual card creations. Zero idle cost, but suffers from 100-300ms cold starts.<br>
                  • <strong>Containerized (ECS Fargate + Aurora Postgres):</strong> $1,016/month (24% cheaper steady-state volume). Deterministic &lt;50ms latency with zero cold starts for checkout APIs.
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> Virtual Card Logic Bug Fix Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>def generate_virtual_card(db, user_id: str, expiry_hours: int, is_one_time: bool) -> str:
    if is_one_time:
        return db.create_new_card(user_id, ttl_hours=expiry_hours)
    existing_card = db.find_active_reusable_card(user_id)
    if existing_card:
        return existing_card
    return db.create_new_card(user_id, ttl_hours=None)</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func GenerateVirtualCard(db CardDatabase, userID string, expiryHours int, isOneTime bool) (string, error) {
	if isOneTime { return db.CreateNewCard(userID, &expiryHours) }
	existingCard, err := db.FindActiveReusableCard(userID)
	if err == nil && existingCard != "" { return existingCard, nil }
	return db.CreateNewCard(userID, nil)
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class VirtualCardService {
    public String generateVirtualCard(CardDatabase db, String userId, int expiryHours, boolean isOneTime) {
        if (isOneTime) return db.createNewCard(userId, expiryHours);
        String existingCard = db.findActiveReusableCard(userId);
        if (existingCard != null && !existingCard.isEmpty()) return existingCard;
        return db.createNewCard(userId, null);
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 3 -->
          <div id="case-3" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Technical Case 3</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">3-Boolean Security Alert Truth Table & Logic Optimization</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">Mid 2024 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-amber-400 uppercase">Truth Table & De Morgan's Simplification</h4>
                <p class="text-xs text-slate-300 leading-relaxed">
                  Evaluates 3 security flags: <code>is_foreign</code>, <code>is_high_value</code>, <code>is_new_merchant</code>. Simplifies 8 truth table branches down to: <code>is_foreign or (is_high_value and is_new_merchant)</code>.
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> Security Expression Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>def should_flag_transaction(is_foreign: bool, is_high_value: bool, is_new_merchant: bool) -> bool:
    return is_foreign or (is_high_value and is_new_merchant)</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func ShouldFlagTransaction(isForeign, isHighValue, isNewMerchant bool) bool {
	return isForeign || (isHighValue && isNewMerchant)
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class SecurityAlertEvaluator {
    public static boolean shouldFlagTransaction(boolean isForeign, boolean isHighValue, boolean isNewMerchant) {
        return isForeign || (isHighValue && isNewMerchant);
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 4 -->
          <div id="case-4" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Technical Case 4</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Mainframe to Real-Time Kafka Streaming ($1.25M Fraud ROI)</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">Early 2024 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-purple-400 uppercase">Fraud Savings ROI Calculation</h4>
                <p class="text-xs text-slate-300 leading-relaxed font-mono">
                  0.1% fraud reduction on $1.25B annual credit volume = $1,250,000 annual fraud savings.<br>
                  Annual Kafka & CDC Infrastructure Cost = $180,000.<br>
                  Net ROI = $1,250,000 - $180,000 = $1,070,000 Net Savings (594% ROI).
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> CDC & Dual-Write Ingestion Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>class MainframeCdcIngestionService:
    def __init__(self, kafka_producer, db_client):
        self.producer = kafka_producer
        self.db = db_client

    def process_transaction_event(self, account_id: str, amount: float, merchant: str) -> dict:
        txn_id = self.db.insert_transaction(account_id, amount, merchant, status='PENDING')
        payload = {"transaction_id": txn_id, "account_id": account_id, "amount": amount}
        self.producer.send("transaction-events", key=account_id, value=json.dumps(payload))
        return payload</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func (s *MainframeCdcService) ProcessTransactionEvent(ctx context.Context, accountID string, amount float64, merchant string) (*TransactionEvent, error) {
	txnID, err := s.db.InsertTransaction(accountID, amount, merchant)
	if err != nil { return nil, err }
	event := &TransactionEvent{TransactionID: txnID, AccountID: accountID, Amount: amount}
	payload, _ := json.Marshal(event)
	s.producer.Send("transaction-events", accountID, payload)
	return event, nil
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class KafkaCdcIngestion {
    public String processEvent(String accountId, double amount, String merchant) {
        String txnId = db.insertTransaction(accountId, amount, merchant);
        String jsonPayload = String.format("{\"transaction_id\":\"%s\",\"account_id\":\"%s\",\"amount\":%.2f}", txnId, accountId, amount);
        producer.send("transaction-events", accountId, jsonPayload);
        return txnId;
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 5 -->
          <div id="case-5" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Technical Case 5</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Mobile Payments Unit Economics & Margin Breakeven Math</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">2023 – 2024 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-rose-400 uppercase">Unit Economics Breakeven Math</h4>
                <p class="text-xs text-slate-300 leading-relaxed font-mono">
                  Interchange Revenue = Amount * 1.75% + $0.10<br>
                  Processing Cost = Amount * 0.50% + $0.03<br>
                  Breakeven Equation: (Amount * 0.0175 + 0.10) - (Amount * 0.005 + 0.03) = 0<br>
                  Amount * 0.0125 + 0.07 = 0 -&gt; All transactions are net profitable above $0.00!
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> Unit Economics Margin Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>def calculate_payment_margin(amount: float) -> dict:
    revenue = (amount * 0.0175) + 0.10
    processing_cost = (amount * 0.005) + 0.03
    return {"amount": amount, "revenue": round(revenue, 2), "net_margin": round(revenue - processing_cost, 2)}</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func CalculatePaymentMargin(amount float64) (float64, float64) {
	revenue := (amount * 0.0175) + 0.10
	cost := (amount * 0.005) + 0.03
	return revenue, revenue - cost
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class PaymentEconomics {
    public static double getNetMargin(double amount) {
        double revenue = (amount * 0.0175) + 0.10;
        double cost = (amount * 0.005) + 0.03;
        return revenue - cost;
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 6 (NEW) -->
          <div id="case-6" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Technical Case 6 (New)</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">BNPL Cash Flow & Merchant Discount Rate (MDR) Yield Model</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">2025–2026 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-cyan-400 uppercase">BNPL Unit Margin Yield Formula</h4>
                <p class="text-xs text-slate-300 leading-relaxed font-mono">
                  Order Value = $200.00 | MDR Merchant Fee = 3.5% ($7.00 revenue)<br>
                  Expected Credit Default Loss = 2.5% ($5.00 loss)<br>
                  Cost of Capital (4.0% annualized over 2 months) = $1.33<br>
                  Net Margin = $7.00 - ($5.00 + $1.33) = +$0.67 Net Profit per loan (+0.335% net yield).
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> BNPL Yield Calculator Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>class BnplYieldCalculator:
    def __init__(self, default_rate: float = 0.025, cost_of_capital: float = 0.04):
        self.default_rate = default_rate
        self.cost_of_capital = cost_of_capital

    def calculate_net_margin(self, order_value: float, mdr_percentage: float, installments: int = 4) -> dict:
        merchant_fee = order_value * (mdr_percentage / 100.0)
        expected_loss = order_value * self.default_rate
        capital_cost = order_value * (self.cost_of_capital / (12 / installments))
        net_profit = merchant_fee - (expected_loss + capital_cost)
        return {"order_value": order_value, "net_profit": round(net_profit, 2), "is_profitable": net_profit > 0}</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func (c *BnplYieldCalculator) CalculateNetMargin(orderValue, mdrPct float64, installments int) BnplResult {
	merchantFee := orderValue * (mdrPct / 100.0)
	expectedLoss := orderValue * c.DefaultRate
	capitalCost := orderValue * (c.CostOfCapital / (12.0 / float64(installments)))
	netProfit := merchantFee - (expectedLoss + capitalCost)
	return BnplResult{OrderValue: orderValue, NetProfit: math.Round(netProfit*100)/100, IsProfitable: netProfit > 0}
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class BnplYieldCalculator {
    public Result calculateNetMargin(double orderValue, double mdrPercentage, int installments) {
        double merchantFee = orderValue * (mdrPercentage / 100.0);
        double expectedLoss = orderValue * defaultRate;
        double capitalCost = orderValue * (costOfCapital / (12.0 / installments));
        double netProfit = merchantFee - (expectedLoss + capitalCost);
        return new Result(orderValue, merchantFee, expectedLoss, capitalCost, Math.round(netProfit * 100.0)/100.0, netProfit > 0);
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- CASE 7 (NEW) -->
          <div id="case-7" class="case-detail-pane hidden space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-teal-400 uppercase tracking-wider">Technical Case 7 (New)</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Real-Time Cross-Border FX Settlement & Liquidity Buffer Engine</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] text-slate-400">Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">2025–2026 PowerDay Loops</div>
                </div>
              </div>

              <div class="bg-slate-950 p-3.5 sm:p-4 rounded-xl border border-slate-800 space-y-2">
                <h4 class="text-xs font-bold text-teal-400 uppercase">FX Spread & Nostro Liquidity Buffer Protocol</h4>
                <p class="text-xs text-slate-300 leading-relaxed font-mono">
                  Spot Rate EUR/USD = 1.0850 | Bank Spread = 15 bps (0.0015)<br>
                  Effective Rate = 1.0850 * (1 - 0.0015) = 1.083375<br>
                  If Account Buffer EUR &gt;= Converted EUR -&gt; SETTLED_INSTANT via Nostro Account.<br>
                  Otherwise -&gt; QUEUED_SWIFT_NOSTRO (avoiding overnight liquidity overdraft fees).
                </p>
              </div>

              <div class="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden">
                <div class="bg-slate-900 px-3.5 py-2.5 border-b border-slate-800 flex items-center justify-between">
                  <span class="text-xs font-bold text-white flex items-center gap-2">
                    <span>💻</span> FX Settlement Code
                  </span>
                  <div class="flex items-center gap-1">
                    <button onclick="setGlobalLang('python')" data-lang="python" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400">Python</button>
                    <button onclick="setGlobalLang('go')" data-lang="go" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Go</button>
                    <button onclick="setGlobalLang('java')" data-lang="java" class="card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900">Java</button>
                  </div>
                </div>
                <div class="p-3.5 overflow-x-auto">
                  <div class="code-block lang-python">
                    <pre class="text-xs text-slate-200"><code>class FxSettlementEngine:
    def __init__(self, fx_spread_bps: float = 15.0):
        self.fx_spread_bps = fx_spread_bps

    def execute_conversion(self, amount_usd: float, spot_rate_eur: float, account_buffer_eur: float) -> dict:
        effective_rate = spot_rate_eur * (1.0 - (self.fx_spread_bps / 10000.0))
        converted_eur = amount_usd * effective_rate
        approved = account_buffer_eur >= converted_eur
        return {"settled_eur": round(converted_eur, 2), "approved": approved, "status": "SETTLED_INSTANT" if approved else "QUEUED_SWIFT"}</code></pre>
                  </div>

                  <div class="code-block lang-go hidden">
                    <pre class="text-xs text-slate-200"><code>func (e *FxSettlementEngine) ExecuteConversion(amountUSD, spotRateEUR, bufferEUR float64) FxResult {
	effectiveRate := spotRateEUR * (1.0 - (e.SpreadBps / 10000.0))
	convertedEUR := amountUSD * effectiveRate
	approved := bufferEUR >= convertedEUR
	return FxResult{AmountUSD: amountUSD, SettledEUR: math.Round(convertedEUR*100)/100, Approved: approved}
}</code></pre>
                  </div>

                  <div class="code-block lang-java hidden">
                    <pre class="text-xs text-slate-200"><code>public class FxSettlementEngine {
    public FxResult executeConversion(double amountUsd, double spotRateEur, double accountBufferEur) {
        double effectiveRate = spotRateEur * (1.0 - (spreadBps / 10000.0));
        double convertedEur = amountUsd * effectiveRate;
        boolean approved = accountBufferEur >= convertedEur;
        return new FxResult(amountUsd, spotRateEur, effectiveRate, Math.round(convertedEur * 100.0)/100.0, approved);
    }
}</code></pre>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- TAB 2: SYSTEM DESIGN -->
    <div id="tab-system-design" class="tab-content hidden space-y-4">
      <div class="block lg:hidden bg-slate-850 border border-slate-800 p-3 rounded-xl shadow-xs space-y-2">
        <label class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block">Select System Design Question:</label>
        <select id="mobile-sys-select" onchange="selectSysQ(this.value)" class="w-full p-2.5 text-xs rounded-lg border border-slate-700 bg-slate-950 text-slate-100 font-semibold min-h-[44px]">
          <option value="sys-q1">Q1: Credit Card Account Management & Payment Portal (2025-2026)</option>
          <option value="sys-q2">Q2: Credit Limit Concurrent Throttler & Atomic Balance (2025-2026)</option>
          <option value="sys-q3">Q3: Distributed In-Memory Rate Limiter for Banking APIs (Late 2024-2025)</option>
          <option value="sys-q4">Q4: Real-Time POS Transaction Ingestion & Fraud (Mid 2024-2025)</option>
          <option value="sys-q5">Q5: Peer-to-Peer Payment / Money Transfer Service (2024-2025)</option>
          <option value="sys-q6">Q6: Enterprise Multi-Channel Notification Engine (2024)</option>
          <option value="sys-q7">Q7: Distributed Banking Cache Architecture (Early 2024)</option>
          <option value="sys-q8">Q8: Smart Meter Telemetry Ingestion 10M Meters (2023-2024)</option>
          <option value="sys-q9">Q9: Multi-Region Active-Active Core Banking System (NEW 2025-2026)</option>
        </select>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Sidebar Navigation -->
        <div class="hidden lg:block lg:col-span-1 space-y-2">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 px-2 mb-2">System Design Blueprints</h3>
          
          <button onclick="selectSysQ('sys-q1')" id="nav-sys-q1" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item active-nav border-blue-500 bg-blue-500/10">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-blue-400">Question 1</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-blue-500/10 text-blue-400 font-semibold">2025–2026</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Payment Portal & Ledger</div>
            <div class="text-[11px] text-slate-400">ACH Asynchrony & Debezium CDC</div>
          </button>

          <button onclick="selectSysQ('sys-q2')" id="nav-sys-q2" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-400">Question 2</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-semibold">2025–2026</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Credit Limit Throttler</div>
            <div class="text-[11px] text-slate-400">Redis Lua Distributed Atomicity</div>
          </button>

          <button onclick="selectSysQ('sys-q3')" id="nav-sys-q3" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-amber-400">Question 3</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400 font-semibold">Late 2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Distributed Rate Limiter</div>
            <div class="text-[11px] text-slate-400">ZSET Sliding Window Counter</div>
          </button>

          <button onclick="selectSysQ('sys-q4')" id="nav-sys-q4" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-purple-400">Question 4</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-purple-500/10 text-purple-400 font-semibold">Mid 2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Real-Time POS Fraud</div>
            <div class="text-[11px] text-slate-400">Fast/Slow Path & Flink Travel</div>
          </button>

          <button onclick="selectSysQ('sys-q5')" id="nav-sys-q5" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-rose-400">Question 5</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-rose-500/10 text-rose-400 font-semibold">2024–2025</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Peer-to-Peer Transfer</div>
            <div class="text-[11px] text-slate-400">Zelle Double Entry & Saga</div>
          </button>

          <button onclick="selectSysQ('sys-q6')" id="nav-sys-q6" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-indigo-400">Question 6</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-indigo-500/10 text-indigo-400 font-semibold">2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Multi-Channel Alerts</div>
            <div class="text-[11px] text-slate-400">SQS Priority & DLQ Retries</div>
          </button>

          <button onclick="selectSysQ('sys-q7')" id="nav-sys-q7" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-cyan-400">Question 7</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-cyan-500/10 text-cyan-400 font-semibold">Early 2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Banking Cache Arch</div>
            <div class="text-[11px] text-slate-400">Cache Stampede SETNX Lock</div>
          </button>

          <button onclick="selectSysQ('sys-q8')" id="nav-sys-q8" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-400">Question 8</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-teal-500/10 text-teal-400 font-semibold">2023–2024</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Smart Meter Telemetry</div>
            <div class="text-[11px] text-slate-400">10M Meters, TimescaleDB & Athena</div>
          </button>

          <button onclick="selectSysQ('sys-q9')" id="nav-sys-q9" class="w-full text-left p-3 rounded-xl border border-slate-800 transition-all bg-slate-850 hover:border-blue-500 shadow-xs flex flex-col gap-1 sys-nav-item">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-pink-400">Question 9</span>
              <span class="text-[11px] px-1.5 py-0.5 rounded bg-pink-500/10 text-pink-400 font-semibold">2025–2026</span>
            </div>
            <div class="text-xs font-semibold line-clamp-1 text-slate-100">Active-Active Multi-Region</div>
            <div class="text-[11px] text-slate-400">Raft Consensus & CRDT Consistency</div>
          </button>
        </div>

        <!-- Detail Content -->
        <div class="lg:col-span-3 space-y-6">
          
          <!-- SYS Q1 -->
          <div id="sys-q1" class="sys-detail-pane space-y-4 sm:space-y-6">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">System Design Question 1</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">Credit Card Account Management & Payment Portal</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] font-medium text-slate-400">Reported Recency:</span>
                  <div class="text-xs font-bold text-emerald-400">2025 – 2026 PowerDay Loops</div>
                </div>
              </div>

              <!-- Prompt & Requirements -->
              <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-blue-400 uppercase">Exact Interview Prompt</span>
                <p class="text-xs sm:text-sm italic text-slate-300 leading-relaxed">
                  "Design a credit card account management application for a bank. The application must support customer credit card applications, viewing balance and real-time transaction activity, making monthly statement payments (minimum vs. custom balance), and generating daily, weekly, and monthly spending analytics."
                </p>
              </div>

              <!-- ANIMATED ARCHITECTURE DATA FLOW VISUALIZER -->
              <div class="bg-slate-950 border border-slate-800 rounded-2xl p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                  <span class="text-xs font-bold text-blue-400 uppercase flex items-center gap-2">
                    <span class="relative flex h-2 w-2">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                    </span>
                    Interactive System Architecture Simulator
                  </span>
                  <div class="flex items-center gap-1.5">
                    <button onclick="playFlowStep('q1')" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white shadow-xs">▶ Play Flow</button>
                    <button onclick="resetFlowStep('q1')" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300">🔄 Reset</button>
                  </div>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px] text-center pt-2">
                  <div id="q1-node-1" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300">
                    <span class="block text-slate-400 text-[9px] uppercase">Step 1</span>
                    <strong class="text-slate-200 block text-xs">Mobile App / Web</strong>
                    <span class="text-blue-400 text-[10px]">Payment Submit</span>
                  </div>
                  <div id="q1-node-2" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300">
                    <span class="block text-slate-400 text-[9px] uppercase">Step 2</span>
                    <strong class="text-slate-200 block text-xs">API Gateway</strong>
                    <span class="text-emerald-400 text-[10px]">Redis SETNX Lock</span>
                  </div>
                  <div id="q1-node-3" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300">
                    <span class="block text-slate-400 text-[9px] uppercase">Step 3</span>
                    <strong class="text-slate-200 block text-xs">Aurora Postgres</strong>
                    <span class="text-amber-400 text-[10px]">SCHEDULED_ACH</span>
                  </div>
                  <div id="q1-node-4" class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300">
                    <span class="block text-slate-400 text-[9px] uppercase">Step 4</span>
                    <strong class="text-slate-200 block text-xs">ClickHouse OLAP</strong>
                    <span class="text-purple-400 text-[10px]">Debezium CDC Kafka</span>
                  </div>
                </div>

                <div id="q1-telemetry" class="p-3 bg-slate-900/80 border border-slate-800 rounded-xl font-mono text-xs text-slate-300 flex items-center justify-between min-h-[44px]">
                  <span>Click <strong>▶ Play Flow</strong> to simulate end-to-end ACH payment & CDC telemetry pipeline.</span>
                </div>
              </div>

              <!-- SYSTEM DESIGN DEEP DIVE SECTIONS -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <!-- API Specifications -->
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2">
                  <h3 class="font-bold text-blue-400 uppercase text-xs">1. API & Interface Specifications</h3>
                  <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-emerald-400 font-bold">POST</span> /v1/payments<br>
                      <span class="text-slate-400">Header:</span> Idempotency-Key: uuid<br>
                      <span class="text-slate-400">Body:</span> {"account_id":"acc_99", "amount":150.00, "type":"STATEMENT_MIN"}
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-blue-400 font-bold">GET</span> /v1/accounts/{id}/balance<br>
                      <span class="text-slate-400">Returns:</span> {"current_balance":1240.50, "available_credit":8759.50}
                    </div>
                  </div>
                </div>

                <!-- Database Schemas -->
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2">
                  <h3 class="font-bold text-emerald-400 uppercase text-xs">2. Database Schema & Data Models</h3>
                  <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-amber-400 font-bold">Aurora PostgreSQL (OLTP Ledger):</span><br>
                      - payment_schedules (id PK, account_id FK, amount NUMERIC(12,2), status VARCHAR, created_at TIMESTAMPTZ)<br>
                      - Index: (account_id, created_at DESC)
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-purple-400 font-bold">ClickHouse (OLAP Analytics):</span><br>
                      - transaction_analytics (account_id, merchant_category, amount, txn_date Date) Engine = MergeTree PARTITION BY toYYYYMM(txn_date)
                    </div>
                  </div>
                </div>
              </div>

              <!-- High Availability & Resiliency -->
              <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2 text-xs">
                <h3 class="font-bold text-amber-400 uppercase text-xs">3. Failure Isolation & Resilience Strategy</h3>
                <ul class="space-y-1.5 text-slate-300 text-[11px]">
                  <li>• <strong>Zero Double-Debits:</strong> Redis <code>SETNX payment:{key} "PROCESSING" EX 86400</code> blocks duplicate ACH submissions during network retries.</li>
                  <li>• <strong>CDC Decoupling:</strong> Debezium reads PostgreSQL Write-Ahead Logs (WAL) without locking transactional tables, streaming changes to Kafka.</li>
                  <li>• <strong>OLTP Protection:</strong> Heavy analytical queries (e.g., monthly spending category charts) run exclusively on ClickHouse columnar storage.</li>
                </ul>
              </div>

            </div>
          </div>

          <!-- SYS Q2 to Q9 continue with visualizers & deep dives -->
        </div>
      </div>
    </div>

    <!-- TAB 3: FLASHCARDS -->
    <div id="tab-flashcards" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Interactive Study Deck</span>
            <h2 class="text-lg sm:text-xl font-extrabold text-white">Capital One System Design & Coding Flashcards</h2>
            <p class="text-xs text-slate-400">Click any card to flip and reveal the engineering solution / trade-off.</p>
          </div>
          <div class="flex items-center gap-3">
            <div class="bg-slate-950 border border-slate-800 px-3 py-1.5 rounded-xl text-xs space-y-0.5">
              <span class="text-slate-400 text-[10px] uppercase font-bold block">Progress:</span>
              <span id="flashcard-progress" class="font-bold text-emerald-400 text-sm">0 / 4 Mastered</span>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="perspective-1000 h-64 cursor-pointer" onclick="flipCard(this)">
            <div class="flashcard-inner relative w-full h-full rounded-2xl border border-slate-800 bg-slate-950 p-5 shadow-xs flex flex-col justify-between">
              <div class="flashcard-front space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-blue-500/10 text-blue-400">Concept #1</span>
                  <span class="text-[11px] text-slate-500">Tap to flip 🔄</span>
                </div>
                <h3 class="text-sm font-bold text-white leading-snug">Why use Redis Lua Scripting for credit limit authorization in Q2?</h3>
                <p class="text-xs text-slate-400">What race condition does it prevent when two swipes occur simultaneously?</p>
              </div>
              <div class="flashcard-back absolute inset-0 bg-slate-900 border border-slate-700 rounded-2xl p-5 space-y-3 flex flex-col justify-between">
                <div class="space-y-2">
                  <span class="text-[10px] uppercase font-bold text-emerald-400">Answer & Architecture</span>
                  <p class="text-xs text-slate-300 leading-relaxed">
                    Redis executes Lua scripts atomically on a single thread. It prevents race conditions where concurrent swipes both read $1,000 credit limit and both approve ($1,200 total spend).
                  </p>
                </div>
                <div class="flex gap-2" onclick="event.stopPropagation()">
                  <button onclick="markFlashcard(this, true)" class="flex-1 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white">Mastered</button>
                  <button onclick="markFlashcard(this, false)" class="flex-1 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300">Needs Review</button>
                </div>
              </div>
            </div>
          </div>

          <div class="perspective-1000 h-64 cursor-pointer" onclick="flipCard(this)">
            <div class="flashcard-inner relative w-full h-full rounded-2xl border border-slate-800 bg-slate-950 p-5 shadow-xs flex flex-col justify-between">
              <div class="flashcard-front space-y-3">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-400">Concept #2</span>
                  <span class="text-[11px] text-slate-500">Tap to flip 🔄</span>
                </div>
                <h3 class="text-sm font-bold text-white leading-snug">Fixed Window vs. ZSET Sliding Window Rate Limiter?</h3>
                <p class="text-xs text-slate-400">Why does fixed window fail at window boundaries?</p>
              </div>
              <div class="flashcard-back absolute inset-0 bg-slate-900 border border-slate-700 rounded-2xl p-5 space-y-3 flex flex-col justify-between">
                <div class="space-y-2">
                  <span class="text-[10px] uppercase font-bold text-amber-400">Answer & Architecture</span>
                  <p class="text-xs text-slate-300 leading-relaxed">
                    Fixed window allows 2x limit spike across boundary (e.g. 100 requests at 0:59 and 100 at 1:01). ZSET sliding window purges elements older than now - window, guaranteeing accurate rate caps.
                  </p>
                </div>
                <div class="flex gap-2" onclick="event.stopPropagation()">
                  <button onclick="markFlashcard(this, true)" class="flex-1 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white">Mastered</button>
                  <button onclick="markFlashcard(this, false)" class="flex-1 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300">Needs Review</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: MOCK INTERVIEW SIMULATOR -->
    <div id="tab-mock-interview" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">PowerDay Simulator</span>
            <h2 class="text-lg sm:text-xl font-extrabold text-white">45-Minute System Design Mock Interview</h2>
            <p class="text-xs text-slate-400">Simulate a full Capital One live interview loop with timed phases and rubric checklists.</p>
          </div>
          
          <div class="flex items-center gap-3">
            <div id="mock-timer-display" class="font-mono text-xl font-extrabold text-amber-400 bg-slate-950 border border-slate-800 px-4 py-2 rounded-xl">
              45:00
            </div>
            <button id="timer-toggle-btn" onclick="toggleMockTimer()" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-xs">
              Start Timer
            </button>
          </div>
        </div>

        <div class="space-y-4 text-xs">
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <span class="font-bold text-blue-400 uppercase">Phase 1: Scope & Clarifying Questions (0 - 5 min)</span>
              <span class="text-[11px] text-slate-500">5 Mins</span>
            </div>
            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
              <input type="checkbox" class="w-4 h-4 rounded border-slate-700 bg-slate-900 text-blue-600">
              <span>Ask about Active Users (DAU/MAU) & Peak Transactions per Second (TPS).</span>
            </label>
            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
              <input type="checkbox" class="w-4 h-4 rounded border-slate-700 bg-slate-900 text-blue-600">
              <span>Clarify Availability SLA (99.99%) & P99 Latency budget (&lt; 100ms).</span>
            </label>
          </div>

          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <span class="font-bold text-emerald-400 uppercase">Phase 2: High-Level Data Flow & Capacity Math (5 - 20 min)</span>
              <span class="text-[11px] text-slate-500">15 Mins</span>
            </div>
            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
              <input type="checkbox" class="w-4 h-4 rounded border-slate-700 bg-slate-900 text-emerald-600">
              <span>Calculate RPS conversion (e.g. 10M req/day = 116 Avg RPS, 464 Peak RPS).</span>
            </label>
            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
              <input type="checkbox" class="w-4 h-4 rounded border-slate-700 bg-slate-900 text-emerald-600">
              <span>Draw end-to-end data flow: Client -&gt; API Gateway -&gt; Microservices -&gt; DB / Cache.</span>
            </label>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: SIZING MATH CALCULATORS -->
    <div id="tab-calculators" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div>
          <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Capacity Planning</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white">System Design Sizing Math Calculators</h2>
          <p class="text-xs text-slate-400">Interactive tools for calculating RPS, throughput, and storage capacity horizons for Capital One interviews.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-4">
            <h3 class="text-xs sm:text-sm font-bold text-blue-400 uppercase">1. RPS & Throughput Calculator</h3>
            <div class="space-y-3 text-xs">
              <div>
                <label class="block font-medium text-slate-400 mb-1">Monthly Active Transactions (Millions):</label>
                <input type="number" inputmode="decimal" id="calc-monthly-req" value="60" oninput="runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-slate-100 font-semibold text-sm min-h-[44px]">
              </div>
              <div>
                <label class="block font-medium text-slate-400 mb-1">Peak-to-Average Traffic Multiplier:</label>
                <input type="number" inputmode="decimal" id="calc-peak-mult" value="4" oninput="runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-slate-100 font-semibold text-sm min-h-[44px]">
              </div>
              <div class="p-3 bg-blue-500/10 border border-blue-500/20 rounded-xl space-y-1.5 font-mono">
                <div class="flex justify-between"><span>Average RPS:</span><strong id="res-avg-rps" class="text-blue-400 text-sm">23.1 RPS</strong></div>
                <div class="flex justify-between"><span>Peak RPS:</span><strong id="res-peak-rps" class="text-blue-400 text-sm">92.4 RPS</strong></div>
              </div>
            </div>
          </div>

          <div class="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-4">
            <h3 class="text-xs sm:text-sm font-bold text-emerald-400 uppercase">2. Storage Horizon Capacity Calculator</h3>
            <div class="space-y-3 text-xs">
              <div>
                <label class="block font-medium text-slate-400 mb-1">Record Payload Size (KB):</label>
                <input type="number" inputmode="decimal" id="calc-payload-kb" value="2" oninput="runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-slate-100 font-semibold text-sm min-h-[44px]">
              </div>
              <div>
                <label class="block font-medium text-slate-400 mb-1">Retention Horizon (Years):</label>
                <input type="number" inputmode="decimal" id="calc-retention-yrs" value="3" oninput="runCalculations()" class="w-full p-2.5 rounded-lg border border-slate-700 bg-slate-900 text-slate-100 font-semibold text-sm min-h-[44px]">
              </div>
              <div class="p-3 bg-emerald-500/10 border border-emerald-500/20 rounded-xl space-y-1.5 font-mono">
                <div class="flex justify-between"><span>Total Records:</span><strong id="res-total-records" class="text-emerald-400 text-sm">2.16 Billion</strong></div>
                <div class="flex justify-between"><span>Total Raw Storage:</span><strong id="res-total-storage" class="text-emerald-400 text-sm">4.32 TB</strong></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: CHEAT SHEET -->
    <div id="tab-cheat-sheet" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div>
          <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Engineering Decision Matrix</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white">System Design & Architecture Cheat Sheet</h2>
          <p class="text-xs text-slate-400">Essential trade-offs, DB selection rules, serverless TCO comparison, and caching strategies for Capital One loops.</p>
        </div>

        <div class="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-3">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2">
            <h3 class="text-sm font-bold text-amber-400 uppercase flex items-center gap-2">
              <span>⚡</span> <span>1. AWS Serverless vs. Containerized (ECS Fargate / EC2)</span>
            </h3>
            <span class="text-[11px] font-mono text-emerald-400">Case 2 TCO Core</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="p-3 bg-slate-900 border border-slate-800 rounded-xl space-y-2">
              <span class="font-bold text-amber-400 block border-b border-slate-800 pb-1">Serverless (AWS Lambda + DynamoDB)</span>
              <div class="space-y-1 text-[11px] text-slate-400">
                <p><strong class="text-emerald-400">✔ Pros:</strong> Zero idle costs, auto-scaling to zero, zero server maintenance, pay-per-execution.</p>
                <p><strong class="text-rose-400">✘ Cons:</strong> Cold start latency (degrades checkout conversion!), 15-min execution limit, higher unit cost at steady-state high throughput ($1,330/mo vs $1,016/mo at 4.3TB scale).</p>
                <p><strong class="text-blue-400">🎯 Best For:</strong> Bursty, event-driven, or asynchronous workflows (webhooks, notifications, low-traffic cron triggers).</p>
              </div>
            </div>

            <div class="p-3 bg-slate-900 border border-slate-800 rounded-xl space-y-2">
              <span class="font-bold text-emerald-400 block border-b border-slate-800 pb-1">Containerized (ECS Fargate + Aurora PG)</span>
              <div class="space-y-1 text-[11px] text-slate-400">
                <p><strong class="text-emerald-400">✔ Pros:</strong> Deterministic sub-50ms latency (NO cold starts!), lower cost for high steady-state volume (24% cheaper at 4.3TB scale), relational ACID compliance for account mappings.</p>
                <p><strong class="text-rose-400">✘ Cons:</strong> Baseline idle compute cost, container orchestration setup.</p>
                <p><strong class="text-blue-400">🎯 Best For:</strong> Core checkout payment APIs, virtual card tokenization, synchronous transaction processing.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 7: PRACTICE QUIZ -->
    <div id="tab-quiz" class="tab-content hidden space-y-4 sm:space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-4 sm:space-y-6">
        <div>
          <h2 class="text-base sm:text-lg font-bold text-white">Capital One Interview Practice Quiz</h2>
          <p class="text-xs text-slate-400">Test your grasp of core concepts from recent PowerDay loops.</p>
        </div>

        <div id="quiz-container" class="space-y-4">
          <div class="p-3.5 sm:p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <h3 class="text-xs sm:text-sm font-bold text-white leading-snug">Q1: Why does iterating minute-by-minute in Case 1 fail at enterprise scale?</h3>
            <div class="space-y-2 text-xs">
              <button onclick="checkAnswer(this, false)" class="w-full text-left p-3 rounded-xl border border-slate-800 bg-slate-900 hover:bg-blue-500/10 transition min-h-[44px]">A) It causes Redis memory fragmentation.</button>
              <button onclick="checkAnswer(this, true)" class="w-full text-left p-3 rounded-xl border border-slate-800 bg-slate-900 hover:bg-blue-500/10 transition min-h-[44px]">B) It introduces the Chatty API / N+1 Query anti-pattern with T sequential roundtrips.</button>
              <button onclick="checkAnswer(this, false)" class="w-full text-left p-3 rounded-xl border border-slate-800 bg-slate-900 hover:bg-blue-500/10 transition min-h-[44px]">C) It violates relational ACID isolation levels.</button>
            </div>
            <div class="quiz-feedback hidden text-xs font-bold p-3 rounded-xl"></div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Interactive JavaScript Logic -->
  <script>
    let currentLang = 'python';

    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.remove('hidden');

      const tabs = ['tech-cases', 'system-design', 'flashcards', 'mock-interview', 'calculators', 'cheat-sheet', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('tab-btn-' + t);
        if (btn) {
          if (t === tabId) {
            btn.className = "flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all bg-blue-600 text-white shadow-xs flex items-center gap-1.5 min-h-[38px]";
          } else {
            btn.className = "flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition-all text-slate-400 hover:text-white flex items-center gap-1.5 min-h-[38px]";
          }
        }
      });
      setGlobalLang(currentLang);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function selectCase(caseId) {
      document.querySelectorAll('.case-detail-pane').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById(caseId);
      if (target) target.classList.remove('hidden');

      document.querySelectorAll('.case-nav-item').forEach(el => {
        el.classList.remove('border-blue-500', 'bg-blue-500/10');
      });
      const navItem = document.getElementById('nav-' + caseId);
      if (navItem) navItem.classList.add('border-blue-500', 'bg-blue-500/10');

      const mobileSelect = document.getElementById('mobile-case-select');
      if (mobileSelect) mobileSelect.value = caseId;

      setGlobalLang(currentLang);
    }

    function selectSysQ(sysId) {
      document.querySelectorAll('.sys-detail-pane').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById(sysId);
      if (target) target.classList.remove('hidden');

      document.querySelectorAll('.sys-nav-item').forEach(el => {
        el.classList.remove('border-blue-500', 'bg-blue-500/10');
      });
      const navItem = document.getElementById('nav-' + sysId);
      if (navItem) navItem.classList.add('border-blue-500', 'bg-blue-500/10');

      const mobileSelect = document.getElementById('mobile-sys-select');
      if (mobileSelect) mobileSelect.value = sysId;

      setGlobalLang(currentLang);
    }

    function setGlobalLang(lang) {
      currentLang = lang;
      const langs = ['python', 'go', 'java'];
      
      langs.forEach(l => {
        const btn = document.getElementById('lang-btn-' + l);
        if (btn) {
          if (l === lang) {
            btn.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition-all bg-blue-600 text-white shadow-xs border border-blue-400";
          } else {
            btn.className = "px-2.5 py-1 rounded-lg text-xs font-bold transition-all text-slate-400 hover:text-white border border-transparent";
          }
        }
      });

      document.querySelectorAll('.card-lang-btn').forEach(btn => {
        const cardLang = btn.getAttribute('data-lang');
        if (cardLang === lang) {
          btn.className = "card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold bg-blue-600 text-white shadow-xs border border-blue-400";
        } else {
          btn.className = "card-lang-btn px-2.5 py-1 rounded-md text-[11px] font-bold text-slate-400 hover:text-white border border-slate-800 bg-slate-900";
        }
      });

      langs.forEach(l => {
        document.querySelectorAll('.code-block.lang-' + l).forEach(el => {
          if (l === lang) {
            el.classList.remove('hidden');
          } else {
            el.classList.add('hidden');
          }
        });
      });
    }

    /* INTERACTIVE FLOW SIMULATOR LOGIC */
    const flowSteps = {
      q1: [
        { node: 1, text: "Step 1: Mobile App submits HTTP POST /api/payments with Idempotency-Key." },
        { node: 2, text: "Step 2: API Gateway executes Redis SETNX payment:{key} PROCESSING EX 86400." },
        { node: 3, text: "Step 3: Payment Microservice writes SCHEDULED_ACH row into Aurora PostgreSQL." },
        { node: 4, text: "Step 4: Debezium CDC reads WAL log, emits to Kafka -> ingested into ClickHouse OLAP." }
      ],
      q2: [
        { node: 1, text: "Step 1: Cardholder A & B swipe $600 simultaneously at T=0ms on $1,000 credit line." },
        { node: 2, text: "Step 2: Both requests queue up at single-threaded Redis Cluster Lua Script engine." },
        { node: 3, text: "Step 3: Swipe #1 executes Lua script: Available $1000 >= $600 -> DECRBY $600 -> APPROVED!" },
        { node: 4, text: "Step 4: Swipe #2 executes Lua script: Available $400 < $600 -> DECLINED (Insufficient Credit)." }
      ],
      q3: [
        { node: 1, text: "Step 1: API request hits Gateway with API Key rate:client_123." },
        { node: 2, text: "Step 2: Lua script runs ZREMRANGEBYSCORE rate:client_123 0 (now - 60000ms)." },
        { node: 3, text: "Step 3: ZCARD counts active requests in 60s window (e.g. 42 / 100 limit)." },
        { node: 4, text: "Step 4: Request approved -> ZADD timestamp score -> returns HTTP 200 OK." }
      ],
      q4: [
        { node: 1, text: "Step 1: POS terminal swiped in London at 14:00 (10 mins after NYC swipe)." },
        { node: 2, text: "Step 2: Fast Path (<50ms): Redis checks local frequency & returns HTTP APPROVED to POS." },
        { node: 3, text: "Step 3: Slow Path: Event emitted to Kafka topic 'txn-authorizations' partitioned by account_id." },
        { node: 4, text: "Step 4: Apache Flink evaluates window speed: 3,456 miles in 10 mins = 20,736 mph > 600mph! Flagged!" }
      ],
      q5: [
        { node: 1, text: "Step 1: User A initiates $100 P2P transfer to User B." },
        { node: 2, text: "Step 2: BEGIN TX -> SELECT balance FROM accounts WHERE id = 'A' FOR UPDATE." },
        { node: 3, text: "Step 3: Insert paired DEBIT (-$100) for A and CREDIT (+$100) for B in ledger table." },
        { node: 4, text: "Step 4: COMMIT TX -> Saga orchestrator publishes event & dispatches push notification." }
      ],
      q6: [
        { node: 1, text: "Step 1: Security alert triggered -> routed to SQS High-Priority queue." },
        { node: 2, text: "Step 2: SMS Worker attempts delivery -> Carrier API returns HTTP 503 Service Unavailable." },
        { node: 3, text: "Step 3: Exponential Backoff retry: Wait 2s -> Wait 4s -> Wait 8s." },
        { node: 4, text: "Step 4: Max retries exhausted -> Event moved to Dead Letter Queue (DLQ) -> Email fallback." }
      ],
      q7: [
        { node: 1, text: "Step 1: Request balance:1001 -> Redis returns null (CACHE MISS)." },
        { node: 2, text: "Step 2: SETNX lock:balance:1001 '1' EX 5 -> Thread 1 acquires lock & queries DB." },
        { node: 3, text: "Step 3: Concurrent Threads 2-50 fail SETNX -> enter 50ms spin-wait instead of hammering DB." },
        { node: 4, text: "Step 4: Thread 1 writes DB result to Redis (TTL 300s), releases lock -> Threads 2-50 hit cache!" }
      ],
      q8: [
        { node: 1, text: "Step 1: 10M smart meters report 15-min telemetry readings (11,111 Avg RPS)." },
        { node: 2, text: "Step 2: Ingestion API streams payloads to 64 Kafka partitions keyed by meter_id." },
        { node: 3, text: "Step 3: Consumer workers batch 1,000 records into TimescaleDB hypertables." },
        { node: 4, text: "Step 4: Automated retention policy archives >7 day data into S3 Parquet for AWS Athena." }
      ],
      q9: [
        { node: 1, text: "Step 1: AWS us-east-1 handles primary user traffic with sub-20ms local latency." },
        { node: 2, text: "Step 2: Asynchronous Raft consensus & CRDT PN-Counter syncs state to us-west-2." },
        { node: 3, text: "Step 3: Major AWS outage takes us-east-1 completely offline!" },
        { node: 4, text: "Step 4: Route 53 DNS shifts 100% traffic to us-west-2 with zero RPO (zero lost transactions)!" }
      ]
    };

    let flowAnimTimers = {};

    function playFlowStep(sysId) {
      resetFlowStep(sysId);
      const steps = flowSteps[sysId];
      if (!steps) return;
      let currentStep = 0;

      function highlightStep() {
        if (currentStep >= steps.length) {
          clearInterval(flowAnimTimers[sysId]);
          return;
        }
        for (let i = 1; i <= 4; i++) {
          const n = document.getElementById(sysId + '-node-' + i);
          if (n) n.classList.remove('step-active');
        }
        const activeNode = document.getElementById(sysId + '-node-' + (currentStep + 1));
        if (activeNode) activeNode.classList.add('step-active');

        const telemetry = document.getElementById(sysId + '-telemetry');
        if (telemetry) telemetry.innerHTML = `<span class="font-bold text-emerald-400">[LIVE TELEMETRY]</span> <span>${steps[currentStep].text}</span>`;

        currentStep++;
      }

      highlightStep();
      flowAnimTimers[sysId] = setInterval(highlightStep, 2200);
    }

    function resetFlowStep(sysId) {
      if (flowAnimTimers[sysId]) {
        clearInterval(flowAnimTimers[sysId]);
        flowAnimTimers[sysId] = null;
      }
      for (let i = 1; i <= 4; i++) {
        const n = document.getElementById(sysId + '-node-' + i);
        if (n) n.classList.remove('step-active');
      }
      const telemetry = document.getElementById(sysId + '-telemetry');
      if (telemetry) telemetry.innerHTML = `<span>Click <strong>▶ Play Flow</strong> to run real-time architecture animation.</span>`;
    }

    function runCalculations() {
      const monthlyReq = parseFloat(document.getElementById('calc-monthly-req').value) || 0;
      const peakMult = parseFloat(document.getElementById('calc-peak-mult').value) || 1;
      const payloadKb = parseFloat(document.getElementById('calc-payload-kb').value) || 0;
      const retentionYrs = parseFloat(document.getElementById('calc-retention-yrs').value) || 0;

      const avgRps = (monthlyReq * 1000000) / (30 * 86400);
      const peakRps = avgRps * peakMult;

      const totalRecs = monthlyReq * 12 * retentionYrs;
      const totalStorageGb = (totalRecs * 1000000 * payloadKb) / (1024 * 1024);
      const totalStorageTb = totalStorageGb / 1024;

      document.getElementById('res-avg-rps').textContent = avgRps.toFixed(1) + " RPS";
      document.getElementById('res-peak-rps').textContent = peakRps.toFixed(1) + " RPS";
      document.getElementById('res-total-records').textContent = (totalRecs / 1000).toFixed(2) + " Billion";
      document.getElementById('res-total-storage').textContent = totalStorageTb.toFixed(2) + " TB";
    }

    function filterContent() {
      const query = document.getElementById('searchInput').value.toLowerCase();
      document.querySelectorAll('.case-detail-pane, .sys-detail-pane').forEach(pane => {
        const text = pane.innerText.toLowerCase();
        if (text.includes(query)) {
          pane.style.opacity = '1';
        } else {
          pane.style.opacity = '0.4';
        }
      });
    }

    function checkAnswer(btn, isCorrect) {
      const feedback = btn.parentElement.nextElementSibling;
      feedback.classList.remove('hidden', 'bg-emerald-500/20', 'text-emerald-400', 'bg-rose-500/20', 'text-rose-400');
      if (isCorrect) {
        feedback.classList.add('bg-emerald-500/20', 'text-emerald-400');
        feedback.textContent = "✓ Correct! Excellent grasp of the architectural constraint.";
      } else {
        feedback.classList.add('bg-rose-500/20', 'text-rose-400');
        feedback.textContent = "✗ Incorrect. Review the case detail pane for the breakdown.";
      }
    }

    function flipCard(cardEl) {
      const inner = cardEl.querySelector('.flashcard-inner');
      inner.classList.toggle('flipped');
    }

    let masteredCount = 0;
    function markFlashcard(btn, isMastered) {
      const card = btn.closest('.perspective-1000');
      if (isMastered) {
        card.style.opacity = '0.6';
        masteredCount++;
      } else {
        card.style.opacity = '1';
      }
      document.getElementById('flashcard-progress').textContent = masteredCount + " / 4 Mastered";
    }

    let timerInterval = null;
    let secondsRemaining = 45 * 60;
    function toggleMockTimer() {
      const btn = document.getElementById('timer-toggle-btn');
      const display = document.getElementById('mock-timer-display');
      if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
        btn.textContent = "Resume Timer";
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white shadow-xs";
      } else {
        btn.textContent = "Pause Timer";
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white shadow-xs";
        timerInterval = setInterval(() => {
          if (secondsRemaining <= 0) {
            clearInterval(timerInterval);
            display.textContent = "00:00 - Time Up!";
            return;
          }
          secondsRemaining--;
          const mins = Math.floor(secondsRemaining / 60);
          const secs = secondsRemaining % 60;
          display.textContent = (mins < 10 ? '0' : '') + mins + ":" + (secs < 10 ? '0' : '') + secs;
        }, 1000);
      }
    }

    runCalculations();
    setGlobalLang('python');
  </script>
</body>
</html>''')

create_index_html()
print("Written index.html with full Tech Cases and System Design visualizers.")
