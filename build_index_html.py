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

    .node-active {
      border-color: #3b82f6 !important;
      background-color: rgba(59, 130, 246, 0.25) !important;
      box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
      transform: scale(1.02);
    }

    @keyframes flowDash {
      0% { stroke-dashoffset: 24; }
      100% { stroke-dashoffset: 0; }
    }
    .flow-line {
      stroke: #334155;
      stroke-width: 2;
      stroke-dasharray: 6 4;
      transition: all 0.3s ease;
    }
    .flow-line-active {
      stroke: #3b82f6;
      stroke-width: 3;
      stroke-dasharray: 6 4;
      animation: flowDash 0.6s linear infinite;
      filter: drop-shadow(0px 0px 6px rgba(59, 130, 246, 0.9));
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

    <!-- TAB 1: TECHNICAL CASES (FULL RESTORED CASES 1 TO 7 WITH LEGACY BUGGY CODE & HIDE/REVEAL SOLUTIONS) -->
    <div id="tab-tech-cases" class="tab-content space-y-4">
      <div class="block lg:hidden bg-slate-850 border border-slate-800 p-3 rounded-xl shadow-xs space-y-2">
        <label class="text-[11px] font-bold uppercase tracking-wider text-slate-400 block">Select Case Study:</label>
        <select id="mobile-case-select" onchange="selectCase(this.value)" class="w-full p-2.5 text-xs rounded-lg border border-slate-700 bg-slate-950 text-slate-100 font-semibold min-h-[44px]">
          <option value="case-1">Case 1: "Eeno" Customer History Retrieval</option>
          <option value="case-2">Case 2: Virtual Card Generation (Serverless vs ECS)</option>
          <option value="case-3">Case 3: 3-Boolean Security Alert Logic</option>
          <option value="case-4">Case 4: Mainframe to Real-Time Kafka Streaming</option>
          <option value="case-5">Case 5: Mobile Payments Unit Economics</option>
          <option value="case-6">Case 6: BNPL Cash Flow & MDR Yield Model</option>
          <option value="case-7">Case 7: Real-Time Cross-Border FX Settlement</option>
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
''')

        # CASES CONFIGURATION (FULL ORIGINAL PROMPT + LEGACY BUGGY CODE + HIDE/REVEAL SOLUTION)
        tech_cases_config = [
            {
                "id": "case-1",
                "tag": "Technical Case Study 1",
                "color": "blue",
                "title": '"Eeno" Customer Transaction History Retrieval',
                "recency": "Late 2025 • High Frequency",
                "prompt": 'Capital One\'s virtual assistant ("Eeno") queries customer transaction histories over mobile networks. When a customer requests 3 years of transaction history, the mobile app freezes or hits a 504 Gateway Timeout over 3G/LTE connections. Inspect the legacy endpoint code below, diagnose why it fails, and rewrite it for sub-100ms response times over low-bandwidth mobile networks.',
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Unbounded database query + 5MB uncompressed JSON payload
def get_all_customer_transactions(account_id: str):
    # BAD: Unbounded query fetches ALL rows into memory without LIMIT or pagination (10,000+ records)
    sql = "SELECT * FROM transactions WHERE account_id = '" + account_id + "' ORDER BY created_at DESC"
    rows = db.execute_query(sql)  # O(N) memory allocation & potential SQL Injection!
    
    # BAD: Serializes full payload into a 5MB+ JSON payload sent uncompressed
    return jsonify(rows)  # Causes 504 Gateway Timeout over mobile 3G/LTE networks!''',
                "root_causes": [
                    "Unbounded DB memory allocation (SELECT * fetching 10,000+ rows).",
                    "SQL Injection vulnerability via string concatenation.",
                    "Mobile CPU spike & memory crash parsing uncompressed 5MB+ JSON arrays."
                ],
                "fix_arch": [
                    "Dynamic Time Windowing: Fetch last 30 days of data first (sub-50ms).",
                    "Keyset Pagination: WHERE (created_at, id) < (:last_date, :last_id) ORDER BY created_at DESC, id DESC LIMIT 50.",
                    "Response Compression: Gzip/Brotli compression shrinks payload size by ~82%."
                ],
                "solution_py": '''def fetch_customer_history(account_id: str, last_date=None, last_id=None, limit=50):
    # ✅ Parameterized query with Keyset Pagination & O(1) index scan
    query = """
        SELECT id, amount, merchant, created_at
        FROM transactions
        WHERE account_id = %s
    """
    params = [account_id]
    if last_date and last_id:
        query += " AND (created_at, id) < (%s, %s)"
        params.extend([last_date, last_id])
    query += " ORDER BY created_at DESC, id DESC LIMIT %s"
    params.append(limit)
    return db.execute(query, params)''',
                "solution_go": '''func FetchCustomerHistory(ctx context.Context, db *sql.DB, accountID string, lastDate time.Time, lastID string, limit int) ([]Transaction, error) {
	query := `SELECT id, amount, merchant, created_at FROM transactions WHERE account_id = $1`
	args := []interface{}{accountID}
	if !lastDate.IsZero() && lastID != "" {
		query += ` AND (created_at, id) < ($2, $3)`
		args = append(args, lastDate, lastID)
	}
	query += ` ORDER BY created_at DESC, id DESC LIMIT ` + fmt.Sprintf("$%d", len(args)+1)
	args = append(args, limit)
	rows, err := db.QueryContext(ctx, query, args...)
	return parseRows(rows), err
}''',
                "solution_java": '''public List<Transaction> fetchCustomerHistory(String accountId, Instant lastDate, String lastId, int limit) {
    String sql = "SELECT id, amount, merchant, created_at FROM transactions WHERE account_id = ?";
    List<Object> params = new ArrayList<>(List.of(accountId));
    if (lastDate != null && lastId != null) {
        sql += " AND (created_at, id) < (?, ?)";
        params.add(lastDate);
        params.add(lastId);
    }
    sql += " ORDER BY created_at DESC, id DESC LIMIT ?";
    params.add(limit);
    return jdbcTemplate.query(sql, params.toArray(), new TransactionRowMapper());
}'''
            },
            {
                "id": "case-2",
                "tag": "Technical Case Study 2",
                "color": "emerald",
                "title": "Virtual Card Number Generation (Serverless vs ECS)",
                "recency": "Mid 2025 • Medium",
                "prompt": "E-commerce shoppers generate temporary virtual card numbers (VCN) for single-use purchases. During Cyber Monday traffic spikes, the VCN generation service experienced 1,500ms latency spikes (AWS Lambda VPC cold starts) and issued invalid cards that were rejected by merchants. Inspect the legacy serverless handler below, identify the boolean logic bug, and propose a low-latency architecture.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Boolean inversion bug + AWS Lambda Cold Start
def lambda_handler(event, context):
    user_id = event['user_id']
    limit = event['limit']
    
    # Generate 16-digit card number
    raw_card = "4" + str(random.randint(100000000000000, 999999999999999))
    
    # 🐛 BUG: Inverted boolean initialization sets card to False (inactive) upon issuance!
    is_active = False  # <--- Merchant authorization fails instantly!
    
    db.save({"user_id": user_id, "card_number": raw_card, "is_active": is_active})
    return {"statusCode": 200, "body": {"vcn": raw_card, "status": "INACTIVE"}}''',
                "root_causes": [
                    "Boolean inversion bug: is_active set to False during issuance.",
                    "AWS Lambda VPC cold starts penalty (800ms-1,500ms during Cyber Monday bursts).",
                    "Missing Luhn algorithm checksum validation on generated card numbers."
                ],
                "fix_arch": [
                    "Corrected boolean initialization (is_active = True).",
                    "Added Luhn algorithm checksum calculation to guarantee valid 16-digit card numbers.",
                    "Migrated high-throughput VCN generation to AWS ECS Fargate provisioned tasks to eliminate cold starts."
                ],
                "solution_py": '''def generate_virtual_card(user_id: str, credit_limit: float) -> dict:
    # ✅ Generates 15 raw digits + calculates 16th Luhn checksum digit
    raw_num = "4" + "".join([str(random.randint(0, 9)) for _ in range(14)])
    checksum = calculate_luhn_checksum(raw_num)
    vcn = raw_num + str(checksum)
    
    # ✅ FIXED: active set to True upon issuance
    return {
        "user_id": user_id,
        "vcn": vcn,
        "credit_limit": credit_limit,
        "is_active": True,
        "status": "ACTIVE"
    }''',
                "solution_go": '''func GenerateVirtualCard(userID string, creditLimit float64) VirtualCard {
	raw := "4" + fmt.Sprintf("%014d", rand.Int64N(10000000000004))
	checksum := calcLuhn(raw)
	return VirtualCard{
		UserID: userID, VCN: raw + strconv.Itoa(checksum),
		CreditLimit: creditLimit, IsActive: true, Status: "ACTIVE",
	}
}''',
                "solution_java": '''public VirtualCard generateVirtualCard(String userId, double creditLimit) {
    String raw = "4" + String.format("%014d", ThreadLocalRandom.current().nextLong(100000000000000L));
    int checksum = calculateLuhn(raw);
    return new VirtualCard(userId, raw + checksum, creditLimit, true, "ACTIVE");
}'''
            },
            {
                "id": "case-3",
                "tag": "Technical Case Study 3",
                "color": "amber",
                "title": "3-Boolean Security Alert Logic Refactoring",
                "recency": "Mid 2024 • Logic & De Morgan",
                "prompt": "Capital One's security engine evaluates 3 risk flags: is_foreign_ip, is_new_device, and is_large_amount. Due to poorly nested legacy if/else statements, high-value foreign transactions failed to trigger security alerts. Simplify and correct the boolean decision logic using De Morgan's laws and a truth table.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Incorrectly nested boolean conditions swallow security alerts
def evaluate_security_risk(is_foreign_ip: bool, is_new_device: bool, is_large_amount: bool) -> bool:
    if is_foreign_ip:
        if is_new_device:
            return True
        else:
            # 🐛 BUG: Returns False even if is_large_amount is True! High-value foreign transactions missed!
            return False 
    else:
        if is_large_amount and not is_new_device:
            return False # 🐛 BUG: Suppresses alert for large transactions on recognized devices!
        return False''',
                "root_causes": [
                    "Poorly nested if/else logic swallowed alerts for high-value foreign transactions (is_foreign_ip = True, is_new_device = False, is_large_amount = True).",
                    "Redundant evaluation branches increased cyclomatic complexity."
                ],
                "fix_arch": [
                    "De Morgan's Laws simplification into a single deterministic truth table.",
                    "Rule: Alert if dual risk (foreign IP + new device) OR high value risk (large amount + foreign IP/new device)."
                ],
                "solution_py": '''def should_trigger_security_alert(is_foreign_ip: bool, is_new_device: bool, is_large_amount: bool) -> bool:
    # ✅ Refactored single-line boolean expression
    has_dual_risk = is_foreign_ip and is_new_device
    has_high_value_risk = is_large_amount and (is_foreign_ip or is_new_device)
    return has_dual_risk or has_high_value_risk''',
                "solution_go": '''func ShouldTriggerSecurityAlert(isForeignIP, isNewDevice, isLargeAmount bool) bool {
	return (isForeignIP && isNewDevice) || (isLargeAmount && (isForeignIP || isNewDevice))
}''',
                "solution_java": '''public boolean shouldTriggerSecurityAlert(boolean isForeignIp, boolean isNewDevice, boolean isLargeAmount) {
    return (isForeignIp && isNewDevice) || (isLargeAmount && (isForeignIp || isNewDevice));
}'''
            },
            {
                "id": "case-4",
                "tag": "Technical Case Study 4",
                "color": "purple",
                "title": "Mainframe Batch Migration to Real-Time Kafka Streaming",
                "recency": "Early 2024 • $1.25M ROI",
                "prompt": "A legacy mainframe batch job exports transaction files every night at midnight to detect fraud. However, fraudulent card activity occurring at 9:00 AM goes undetected for 15 hours. Redesign the batch ingestion system into a real-time event streaming pipeline using Kafka and Change Data Capture (CDC), and quantify the fraud reduction ROI.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: EBCDIC Mainframe Batch Processing (24-Hour Delay)
def process_nightly_batch_file(batch_file_path: str):
    # 🐛 Runs only once per day at 00:00 UTC! Fraudulent activity at 9 AM is undetected for 15 hours.
    with open(batch_file_path, "r") as f:
        for line in f:
            txn = parse_ebcdic_record(line)
            if txn.amount > 5000:
                flag_fraud(txn.account_id)  # Too late! Money already withdrawn/settled.''',
                "root_causes": [
                    "24-hour batch processing window exposes bank to millions in fraudulent card usage before midnight batch run.",
                    "Tight coupling to mainframe EBCDIC flat file exports."
                ],
                "fix_arch": [
                    "Debezium CDC reads PostgreSQL Write-Ahead Logs (WAL) directly from disk.",
                    "Streams changes in real time to Kafka topic c1.mainframe.transactions.v1.",
                    "Yields $1.25 million annual fraud prevention ROI."
                ],
                "solution_py": '''def process_outbox_event(event_id: str, payload: dict, producer):
    # ✅ Real-time Kafka Outbox pattern handler (Sub-second fraud evaluation)
    producer.send(
        topic="c1.mainframe.transactions.v1",
        key=payload["account_id"].encode("utf-8"),
        value=json.dumps(payload).encode("utf-8")
    )
    db.execute("UPDATE outbox SET processed = TRUE WHERE id = %s", [event_id])''',
                "solution_go": '''func ProcessOutboxEvent(ctx context.Context, producer *kafka.Producer, eventID string, payload TxnEvent) error {
	msg, _ := json.Marshal(payload)
	err := producer.Produce(&kafka.Message{
		TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
		Key:            []byte(payload.AccountID), Value: msg,
	}, nil)
	return markOutboxProcessed(ctx, eventID)
}''',
                "solution_java": '''public void processOutboxEvent(String eventId, TxnPayload payload) {
    kafkaTemplate.send("c1.mainframe.transactions.v1", payload.getAccountId(), payload)
        .whenComplete((result, ex) -> {
            if (ex == null) outboxRepository.markProcessed(eventId);
        });
}'''
            },
            {
                "id": "case-5",
                "tag": "Technical Case Study 5",
                "color": "rose",
                "title": "Mobile Payments Unit Economics & Margin Math",
                "recency": "2023 - 2024 • Finance & Math",
                "prompt": "Capital One earns interchange revenue on credit card swipes, but incurs network fees, rewards cashback, and fraud loss reserves. Write a function to calculate the net margin on a transaction and determine the minimum transaction amount required for Capital One to break even.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Over-simplified profit logic ignores fixed network fees
def calculate_profit(amount: float) -> float:
    interchange = amount * 0.0175
    rewards = amount * 0.0100
    # 🐛 BUG: Ignores fixed per-transaction fee ($0.10) and network scheme fee (0.15%)!
    # Falsely marks $1.00 micro-transactions as profitable when bank actually loses money!
    return interchange - rewards''',
                "root_causes": [
                    "Omitted fixed $0.10 per-transaction fee and 0.15% network scheme processing fee.",
                    "Falsely reported positive margins on small micro-transactions under $8.33."
                ],
                "fix_arch": [
                    "Full interchange economics equation: Net Margin = (1.75% * Amount + $0.10) - (0.15% + 1.00% + 0.25%) * Amount.",
                    "Calculates exact break-even transaction size ($8.33)."
                ],
                "solution_py": '''def calculate_transaction_margin(amount: float) -> dict:
    # ✅ Complete interchange unit economics equation
    gross_interchange = (amount * 0.0175) + 0.10
    network_fee = amount * 0.0015
    rewards_cost = amount * 0.0100
    fraud_reserve = amount * 0.0025
    net_margin = gross_interchange - (network_fee + rewards_cost + fraud_reserve)
    return {
        "amount": amount,
        "interchange": round(gross_interchange, 2),
        "net_margin": round(net_margin, 2),
        "is_profitable": net_margin > 0
    }''',
                "solution_go": '''func CalculateTransactionMargin(amount float64) MarginResult {
	interchange := (amount * 0.0175) + 0.10
	costs := (amount * 0.0015) + (amount * 0.0100) + (amount * 0.0025)
	net := interchange - costs
	return MarginResult{Amount: amount, Interchange: interchange, NetMargin: net, IsProfitable: net > 0}
}''',
                "solution_java": '''public MarginResult calculateTransactionMargin(double amount) {
    double interchange = (amount * 0.0175) + 0.10;
    double costs = (amount * 0.0015) + (amount * 0.0100) + (amount * 0.0025);
    double net = interchange - costs;
    return new MarginResult(amount, interchange, net, net > 0);
}'''
            },
            {
                "id": "case-6",
                "tag": "Technical Case Study 6",
                "color": "cyan",
                "title": "BNPL Cash Flow & Merchant Discount Rate (MDR) Yield",
                "recency": "2025 - 2026 • High Impact",
                "prompt": "Buy-Now-Pay-Later (BNPL) splits a $400 order into 4 equal installments of $100. Merchants pay a 4.0% MDR fee up front ($16). However, installment defaults occur across installments 2, 3, and 4 at a 1.2% loss rate. Write a financial cash flow calculator to evaluate net bank yield.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Flawed yield model ignores installment default risk
def calculate_bnpl_profit(order_amount: float) -> float:
    mdr_revenue = order_amount * 0.04
    # 🐛 BUG: Assumes 100% of customers pay all 4 installments! Zero loss reserve factored!
    return mdr_revenue  # Overstates profit by $3.60 on a $400 purchase.''',
                "root_causes": [
                    "Assumed zero installment defaults, overstating net profit margins on BNPL financing products."
                ],
                "fix_arch": [
                    "Factored 1.2% default loss rate across remaining 75% uncollected capital ($3.60 expected loss).",
                    "Net bank profit = $16.00 MDR revenue - $3.60 expected loss = $12.40 net yield."
                ],
                "solution_py": '''def calculate_bnpl_yield(order_val: float, mdr_pct=0.04, default_rate=0.012) -> dict:
    # ✅ Risk-adjusted BNPL installment yield model
    upfront_mdr = order_val * mdr_pct
    merchant_payout = order_val - upfront_mdr
    expected_default_loss = (order_val * 0.75) * default_rate
    net_bank_profit = upfront_mdr - expected_default_loss
    return {
        "order_val": order_val,
        "upfront_mdr": upfront_mdr,
        "merchant_payout": merchant_payout,
        "expected_default_loss": expected_default_loss,
        "net_bank_profit": net_bank_profit
    }''',
                "solution_go": '''func CalculateBnplYield(orderVal float64, mdrPct, defaultRate float64) BnplYield {
	mdr := orderVal * mdrPct
	payout := orderVal - mdr
	loss := (orderVal * 0.75) * defaultRate
	profit := mdr - loss
	return BnplYield{OrderVal: orderVal, UpfrontMDR: mdr, MerchantPayout: payout, NetProfit: profit}
}''',
                "solution_java": '''public BnplYield calculateBnplYield(double orderVal, double mdrPct, double defaultRate) {
    double mdr = orderVal * mdrPct;
    double payout = orderVal - mdr;
    double loss = (orderVal * 0.75) * defaultRate;
    double profit = mdr - loss;
    return new BnplYield(orderVal, mdr, payout, loss, profit);
}'''
            },
            {
                "id": "case-7",
                "tag": "Technical Case Study 7",
                "color": "teal",
                "title": "Real-Time Cross-Border FX Settlement Engine",
                "recency": "2025 - 2026 • High Precision",
                "prompt": "When a U.S. cardholder swipes their card in Europe, the transaction must convert USD to EUR in real-time, apply a 50 basis point (0.50%) FX spread, and check whether the bank's EUR liquidity buffer has sufficient funds to settle. Write an FX conversion engine that enforces precision math.",
                "legacy_code": '''# ❌ LEGACY BUGGY CODE: Inverted spread calculation & floating point precision loss
def convert_currency(usd_amount: float, spot_rate_eur: float) -> float:
    # 🐛 BUG: Adds 5% to spot rate (making EUR more expensive for bank instead of earning spread!)
    effective_rate = spot_rate_eur * 1.05  # Hardcoded 5% instead of 50 bps (0.5%)!
    eur_total = usd_amount * effective_rate
    # 🐛 BUG: Standard float math causes precision loss ($100.00000000000001)
    return eur_total''',
                "root_causes": [
                    "Inverted spread calculation (added 5% fee to spot rate instead of deducting spread).",
                    "Hardcoded 5% fee instead of 50 basis points (0.50%).",
                    "Floating point precision errors during currency conversion."
                ],
                "fix_arch": [
                    "Correct basis point spread formula: effective_rate = spot_rate * (1.0 - (spread_bps / 10000.0)).",
                    "Added EUR liquidity buffer threshold check.",
                    "Exact decimal rounding to 2 decimal places."
                ],
                "solution_py": '''def convert_fx_settlement(amount_usd: float, spot_rate_eur: float, spread_bps=50, buffer_eur=10000.0) -> dict:
    # ✅ Precision FX conversion & liquidity buffer check
    effective_rate = spot_rate_eur * (1.0 - (spread_bps / 10000.0))
    converted_eur = amount_usd * effective_rate
    approved = buffer_eur >= converted_eur
    return {
        "amount_usd": amount_usd,
        "effective_rate": round(effective_rate, 4),
        "converted_eur": round(converted_eur, 2),
        "approved": approved
    }''',
                "solution_go": '''func ExecuteConversion(amountUSD, spotRateEUR, bufferEUR float64) FxResult {
	effectiveRate := spotRateEUR * (1.0 - (50.0 / 10000.0))
	convertedEUR := amountUSD * effectiveRate
	approved := bufferEUR >= convertedEUR
	return FxResult{AmountUSD: amountUSD, SettledEUR: math.Round(convertedEUR*100)/100, Approved: approved}
}''',
                "solution_java": '''public FxResult executeConversion(double amountUsd, double spotRateEur, double accountBufferEur) {
    double effectiveRate = spotRateEur * (1.0 - (50.0 / 10000.0));
    double convertedEur = amountUsd * effectiveRate;
    boolean approved = accountBufferEur >= convertedEur;
    return new FxResult(amountUsd, spotRateEur, effectiveRate, Math.round(convertedEur * 100.0)/100.0, approved);
}'''
            }
        ]

        for case in tech_cases_config:
            c_id = case["id"]
            f.write(f'''
          <!-- {case["tag"].upper()} -->
          <div id="{c_id}" class="case-detail-pane space-y-4 sm:space-y-6 {"hidden" if c_id != "case-1" else ""}">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-5">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-{case["color"]}-400 uppercase tracking-wider">{case["tag"]}</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">{case["title"]}</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] font-medium text-slate-400">Recency & Difficulty:</span>
                  <div class="text-xs font-bold text-{case["color"]}-400">{case["recency"]}</div>
                </div>
              </div>

              <!-- Original Question Prompt -->
              <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-{case["color"]}-400 uppercase flex items-center gap-1.5">
                  <span>❓</span> <span>Original Interview Question Prompt</span>
                </span>
                <p class="text-xs sm:text-sm italic text-slate-300 leading-relaxed">
                  "{case["prompt"]}"
                </p>
              </div>

              <!-- Unmodified Buggy Legacy Code Block -->
              <div class="bg-slate-950 rounded-xl border border-rose-900/50 overflow-hidden space-y-0">
                <div class="bg-rose-950/60 px-4 py-2 border-b border-rose-900/50 flex items-center justify-between text-xs">
                  <span class="font-bold text-rose-400 flex items-center gap-1.5">
                    <span>⚠️</span> <span>Legacy Buggy Code (Inspect & Debug Yourself)</span>
                  </span>
                  <span class="text-rose-400/80 font-mono text-[11px]">Contains Logic Flaws</span>
                </div>
                <div class="p-4 overflow-x-auto font-mono text-xs bg-slate-950">
                  <pre class="text-xs text-rose-200 leading-relaxed"><code>{case["legacy_code"]}</code></pre>
                </div>
              </div>

              <!-- HIDE / REVEAL SOLUTION TOGGLE BUTTON -->
              <div class="pt-2">
                <button onclick="toggleSolution('{c_id}')" id="sol-btn-{c_id}" class="w-full py-3 px-4 bg-slate-800 hover:bg-slate-750 text-blue-400 font-bold rounded-xl border border-slate-700 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all">
                  <span class="flex items-center gap-2">
                    <span>👁️</span> <span>Reveal Answer & Fixed Engineering Solution</span>
                  </span>
                  <span id="sol-icon-{c_id}">▼</span>
                </button>
              </div>

              <!-- HIDDEN SOLUTION CONTAINER -->
              <div id="sol-container-{c_id}" class="hidden space-y-4 pt-2">
                
                <!-- Root Causes & Fix Architecture -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                  <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                    <h4 class="font-bold text-rose-400 uppercase text-xs">Identified Root Causes</h4>
                    <ul class="space-y-1 text-slate-400">
''')
            for rc in case["root_causes"]:
                f.write(f'''                      <li>• {rc}</li>\n''')
            f.write(f'''                    </ul>
                  </div>
                  <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                    <h4 class="font-bold text-emerald-400 uppercase text-xs">Architectural Solution</h4>
                    <ul class="space-y-1 text-slate-400">
''')
            for fa in case["fix_arch"]:
                f.write(f'''                      <li>• {fa}</li>\n''')
            f.write(f'''                    </ul>
                  </div>
                </div>

                <!-- Refactored Solution Code Block -->
                <div class="bg-slate-950 rounded-xl border border-emerald-900/50 overflow-hidden">
                  <div class="bg-emerald-950/40 px-4 py-2 border-b border-emerald-900/50 flex items-center justify-between text-xs">
                    <span class="font-bold text-emerald-400 flex items-center gap-1.5">
                      <span>✅</span> <span>Refactored Production Code</span>
                    </span>
                    <span class="text-slate-500 font-mono text-[11px]">Multi-Language Solution</span>
                  </div>
                  <div class="p-4 overflow-x-auto font-mono text-xs">
                    <div class="code-block lang-python">
                      <pre class="text-xs text-slate-200"><code>{case["solution_py"]}</code></pre>
                    </div>
                    <div class="code-block lang-go hidden">
                      <pre class="text-xs text-slate-200"><code>{case["solution_go"]}</code></pre>
                    </div>
                    <div class="code-block lang-java hidden">
                      <pre class="text-xs text-slate-200"><code>{case["solution_java"]}</code></pre>
                    </div>
                  </div>
                </div>

              </div>

            </div>
          </div>
''')

        f.write('''
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
          <option value="sys-q3">Q3: Distributed API Rate Limiter & Core Banking Gateway (Late 2024)</option>
          <option value="sys-q4">Q4: Real-Time POS Fraud Detection Engine (Mid 2024)</option>
          <option value="sys-q5">Q5: Peer-to-Peer Payment Platform (Zelle / Venmo Clone) (2024-2025)</option>
          <option value="sys-q6">Q6: Enterprise Multi-Channel Notification Engine (2024)</option>
          <option value="sys-q7">Q7: Banking Distributed Cache Architecture & Stampede Guard (Early 2024)</option>
          <option value="sys-q8">Q8: Smart Meter Telemetry 10M Ingestion (2023-2024)</option>
          <option value="sys-q9">Q9: Active-Active Multi-Region Core Banking System (NEW 2025-2026)</option>
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
          
''')
        
        # SYSTEM DESIGN QUESTIONS CONFIGURATION
        sys_questions = [
            {
                "id": "q1",
                "tag": "Question 1",
                "color": "blue",
                "title": "Credit Card Account Management & Payment Portal",
                "recency": "2025 – 2026 PowerDay Loops",
                "prompt": "Design a credit card account management application for a bank. The application must support customer credit card applications, viewing balance and real-time transaction activity, making monthly statement payments (minimum vs. custom balance), and generating daily, weekly, and monthly spending analytics.",
                "apis": [
                    {"method": "POST", "path": "/v1/payments", "headers": "Idempotency-Key: uuid", "body": '{"account_id":"acc_99", "amount":150.00, "type":"STATEMENT_MIN"}'},
                    {"method": "GET", "path": "/v1/accounts/{id}/balance", "headers": "Authorization: Bearer token", "returns": '{"current_balance":1240.50, "available_credit":8759.50}'}
                ],
                "schemas": [
                    {"db": "Aurora PostgreSQL (OLTP Ledger)", "detail": "payment_schedules (id PK, account_id FK, amount NUMERIC(12,2), status VARCHAR, created_at TIMESTAMPTZ)\nIndex: (account_id, created_at DESC)"},
                    {"db": "ClickHouse (OLAP Analytics)", "detail": "transaction_analytics (account_id, merchant_category, amount, txn_date Date) Engine = MergeTree PARTITION BY toYYYYMM(txn_date)"}
                ],
                "resilience": [
                    "Zero Double-Debits: Redis SETNX payment:{key} 'PROCESSING' EX 86400 blocks duplicate ACH submissions during network retries.",
                    "CDC Decoupling: Debezium reads PostgreSQL Write-Ahead Logs (WAL) without locking transactional tables, streaming changes to Kafka.",
                    "OLTP Protection: Heavy analytical queries (e.g., monthly spending category charts) run exclusively on ClickHouse columnar storage."
                ]
            },
            {
                "id": "q2",
                "tag": "Question 2",
                "color": "emerald",
                "title": "Credit Limit Concurrent Throttler & Authorization Engine",
                "recency": "2025 – 2026 PowerDay Loops",
                "prompt": "Design a real-time card authorization engine that enforces credit limits concurrently without allowing over-drafting during simultaneous point-of-sale swipes.",
                "apis": [
                    {"method": "POST", "path": "/v1/authorize", "headers": "X-Merchant-ID: merch_881", "body": '{"card_number_hash":"hash_99", "amount":450.00, "currency":"USD"}'},
                    {"method": "GET", "path": "/v1/limits/{card_id}", "headers": "Authorization: Bearer token", "returns": '{"credit_limit":5000.00, "current_spend":4200.00}'}
                ],
                "schemas": [
                    {"db": "Redis Primary Cluster (In-Memory Auth)", "detail": "Key: card_limit:{card_id} -> Hash { limit: 5000, current_spend: 4200 }\nLua Script: Executes GET + CHECK + DECRBY atomically on single thread."},
                    {"db": "DynamoDB (Audit Log)", "detail": "auth_events (card_id PK, timestamp SK, amount, decision, merchant_id)\nTTL: 90 days for PCI compliance audit."}
                ],
                "resilience": [
                    "Atomic Lua Execution: Prevents race condition where two simultaneous $400 swipes on a $500 remaining balance both succeed.",
                    "Primary Node Failover: Redis Sentinel promotes replica in < 2 seconds if master crashes.",
                    "Database Pessimistic Lock Fallback: If Redis cluster unavailable, falls back to Postgres SELECT FOR UPDATE."
                ]
            },
            {
                "id": "q3",
                "tag": "Question 3",
                "color": "amber",
                "title": "Distributed API Rate Limiter & Core Banking Gateway",
                "recency": "Late 2024 – 2025",
                "prompt": "Design a high-throughput distributed rate limiter for Capital One's developer gateway serving 100k RPS across mobile apps and third-party fintech partner APIs.",
                "apis": [
                    {"method": "ALL", "path": "/v1/*", "headers": "X-API-Key: key_partner_99", "body": "Standard HTTP Request"},
                    {"method": "RESPONSE", "path": "429 Too Many Requests", "headers": "Retry-After: 12s, X-RateLimit-Remaining: 0", "returns": '{"error":"RATE_LIMIT_EXCEEDED"}'}
                ],
                "schemas": [
                    {"db": "Redis Cluster (Sorted Set Sliding Window)", "detail": "Key: rate:{client_id} -> ZSET of timestamps\nLua Script: ZREMRANGEBYSCORE 0 (now - 60s) -> ZCARD -> IF ZCARD < limit THEN ZADD now"},
                    {"db": "Memory Cache (Local Envoy)", "detail": "Local LRU Cache stores client quota tiers to avoid remote Redis calls for invalid API keys."}
                ],
                "resilience": [
                    "Sliding Window ZSET: Eliminates fixed-window boundary burst spikes (where 2x traffic slips through at minute boundaries).",
                    "Soft Failover: If Redis fails, gateway falls back to local token bucket in Envoy sidecar rather than blocking user traffic.",
                    "Multi-Tenant Tiering: Tiered limits (10k RPS for Tier-1 partners vs 100 RPS for Standard Keys)."
                ]
            },
            {
                "id": "q4",
                "tag": "Question 4",
                "color": "purple",
                "title": "Real-Time POS Fraud Detection Engine",
                "recency": "Mid 2024 – 2025",
                "prompt": "Design a real-time card transaction fraud detection engine that evaluates every transaction in < 50ms and flags suspicious travel/location anomalies using streaming window state.",
                "apis": [
                    {"method": "POST", "path": "/v1/fraud/evaluate", "headers": "X-POS-Terminal: term_991", "body": '{"card_id":"c_4821", "amount":1200.00, "lat":35.6762, "lng":139.6503}'},
                    {"method": "EVENT", "path": "Kafka Topic: c1.fraud.alerts", "headers": "Partition: card_id hash", "returns": '{"alert_type":"IMPOSSIBLE_TRAVEL", "score":94}'}
                ],
                "schemas": [
                    {"db": "Apache Flink RocksDB State", "detail": "Keyed Stream by card_id -> Stores last 5 transaction locations & timestamps in RocksDB embedded state."},
                    {"db": "Feast Feature Store (Redis)", "detail": "entity: card_id -> feature: avg_transaction_amount_30d, home_country, velocity_1h."}
                ],
                "resilience": [
                    "Fast / Slow Path Architecture: Fast Path returns sub-50ms score; Slow Path performs deep ML enrichment via Flink.",
                    "RocksDB Incremental Checkpoints: Flink saves state to S3 every 10s for instant worker recovery.",
                    "Decline Guard: High-risk scores (90+) automatically push SMS OTP verification before transaction settlement."
                ]
            },
            {
                "id": "q5",
                "tag": "Question 5",
                "color": "rose",
                "title": "Peer-to-Peer Payment Platform (Zelle / Venmo Clone)",
                "recency": "2024 – 2025",
                "prompt": "Design a real-time peer-to-peer money transfer application supporting instant bank transfers, ledger integrity, and saga orchestration for cross-bank transfers.",
                "apis": [
                    {"method": "POST", "path": "/v1/p2p/transfers", "headers": "Idempotency-Key: p2p_uuid_88", "body": '{"sender_id":"u_11", "receiver_id":"u_22", "amount":200.00}'},
                    {"method": "GET", "path": "/v1/p2p/status/{transfer_id}", "headers": "Authorization: Bearer token", "returns": '{"status":"COMPLETED", "settled_at":"2026-10-06T13:00:00Z"}'}
                ],
                "schemas": [
                    {"db": "Aurora Postgres (Double-Entry Ledger)", "detail": "ledger_entries (id PK, transfer_id FK, account_id, type ENUM('DEBIT','CREDIT'), amount NUMERIC(12,2))\nConstraint: SUM(amount) WHERE transfer_id = X MUST EQUAL 0."},
                    {"db": "Saga State Store (DynamoDB)", "detail": "p2p_sagas (transfer_id PK, current_step, status, compensating_action)"}
                ],
                "resilience": [
                    "Double-Entry Bookkeeping: Prevents money creation/loss by enforcing debit = credit in single DB transaction.",
                    "Saga Orchestration: If receiver bank rejects credit, compensating saga step un-reserves sender funds automatically.",
                    "Outbox Pattern: Guarantees event delivery to notification engine without distributed 2PC locking."
                ]
            },
            {
                "id": "q6",
                "tag": "Question 6",
                "color": "indigo",
                "title": "Enterprise Multi-Channel Notification Engine",
                "recency": "2024",
                "prompt": "Design an enterprise notification system for Capital One that delivers transactional SMS, push notifications, and emails with SLA guarantees, priority queues, and rate-limiting.",
                "apis": [
                    {"method": "POST", "path": "/v1/notifications/send", "headers": "X-Service-ID: srv_fraud", "body": '{"user_id":"u_99", "channel":"SMS", "priority":"HIGH", "template":"FRAUD_ALERT"}'},
                    {"method": "WEBHOOK", "path": "/v1/webhooks/twilio", "headers": "X-Twilio-Signature: sig", "returns": '{"status":"DELIVERED"}'}
                ],
                "schemas": [
                    {"db": "AWS SQS Priority Queues", "detail": "Queues: high-priority-fraud.fifo, medium-priority-txn.fifo, low-priority-promo.fifo"},
                    {"db": "PostgreSQL (Notification History)", "detail": "notifications (id PK, user_id, channel, status, retries, created_at)"}
                ],
                "resilience": [
                    "Priority Bypass: High-priority fraud SMS alerts skip promotional queues and execute under 2-second SLA.",
                    "Provider Circuit Breakers: Automatic failover from Twilio to AWS SNS if SMS gateway error rate > 5%.",
                    "Quiet Hours Suppressor: Low-priority push notifications held in queue during user-defined sleep hours."
                ]
            },
            {
                "id": "q7",
                "tag": "Question 7",
                "color": "cyan",
                "title": "Banking Distributed Cache Architecture & Stampede Guard",
                "recency": "Early 2024",
                "prompt": "Design a distributed caching layer for high-volume banking account balance and customer profile queries, preventing cache stampedes (thundering herd) during hot key invalidation.",
                "apis": [
                    {"method": "GET", "path": "/v1/accounts/{id}/profile", "headers": "Authorization: Bearer token", "returns": '{"user_id":"u_99", "tier":"VentureX", "credit_limit":15000}'},
                    {"method": "POST", "path": "/v1/cache/invalidate", "headers": "X-System-Key: internal", "body": '{"key":"profile:acc_992"}'}
                ],
                "schemas": [
                    {"db": "Redis Cluster (Read-Heavy Cache)", "detail": "Key: profile:{acc_id} -> JSON string (TTL 300s)\nKey: lock:profile:{acc_id} -> Mutex Lock (TTL 5s)"},
                    {"db": "PostgreSQL Primary Ledger", "detail": "accounts (id PK, user_id, tier, limit) -> Source of truth for cache misses."}
                ],
                "resilience": [
                    "Singleflight Mutex Lock: Prevents 10,000 concurrent cache miss requests from hammering the database when a key expires.",
                    "Cache-Aside Pattern: Read from Redis -> Miss -> Acquire SETNX Mutex -> Query DB -> Update Redis -> Release Mutex.",
                    "CDC Cache Invalidation: PostgreSQL WAL changes automatically invalidate Redis keys via Kafka in < 10ms."
                ]
            },
            {
                "id": "q8",
                "tag": "Question 8",
                "color": "teal",
                "title": "Smart Meter Telemetry 10M Ingestion Engine",
                "recency": "2023 – 2024",
                "prompt": "Design an IoT telemetry ingestion system collecting power/water usage data from 10 million smart meters every 15 seconds, storing time-series data for real-time alerting and batch analytics.",
                "apis": [
                    {"method": "MQTT", "path": "telemetry/meters/{meter_id}", "headers": "TLS 1.3 Client Cert", "body": '{"meter_id":"m_881", "kw_usage":4.2, "timestamp":1775480000}'},
                    {"method": "GET", "path": "/v1/analytics/usage", "headers": "Authorization: Bearer token", "returns": '{"meter_id":"m_881", "daily_avg_kw":3.8}'}
                ],
                "schemas": [
                    {"db": "TimescaleDB (Hypertables)", "detail": "meter_telemetry (time TIMESTAMPTZ, meter_id UUID, kw_usage DOUBLE PRECISION)\nPartitioned by 1-day time chunks."},
                    {"db": "S3 Parquet Data Lake", "detail": "s3://c1-telemetry-lake/year=2026/month=10/day=06/part-001.parquet (Columnar storage for Athena)"}
                ],
                "resilience": [
                    "Kinesis Shard Partitioning: 64 Kinesis shards handle 700,000 incoming telemetry messages per second.",
                    "Flink Out-of-Order Watermarking: Bounded-out-of-orderness watermark handles 15-minute delayed sensor readings smoothly.",
                    "Tiered Storage Archival: Moves data > 7 days to S3 Parquet, reducing DB storage costs by 85%."
                ]
            },
            {
                "id": "q9",
                "tag": "Question 9",
                "color": "pink",
                "title": "Active-Active Multi-Region Core Banking System",
                "recency": "2025 – 2026 PowerDay Loops",
                "prompt": "Design an Active-Active multi-region core banking backend across US-East (N. Virginia) and US-West (Oregon) that maintains zero RPO (no lost transactions) and < 3 sec RTO during a total region outage.",
                "apis": [
                    {"method": "POST", "path": "/v1/transactions", "headers": "X-Region-Origin: us-east-1", "body": '{"account_id":"acc_99", "amount":500.00, "type":"DEPOSIT"}'},
                    {"method": "GET", "path": "/v1/health/region", "headers": "Route53-HealthCheck: ok", "returns": '{"status":"HEALTHY", "region":"us-east-1"}'}
                ],
                "schemas": [
                    {"db": "CockroachDB / Aurora Global (Raft Consensus)", "detail": "accounts (id UUID PK, balance NUMERIC, region_owner VARCHAR)\nSynchronous Raft replication across 3 Availability Zones + 2 Regions."},
                    {"db": "Confluent MirrorMaker 2", "detail": "Replicates Kafka event streams bi-directionally between us-east-1 and us-west-2."}
                ],
                "resilience": [
                    "Zero RPO Outage Failover: Route 53 Anycast DNS shifts traffic to healthy region in < 3s with 0 transaction loss.",
                    "CRDT Conflict Resolution: Conflict-Free Replicated Data Types resolve concurrent balance updates deterministically.",
                    "Split-Brain Prevention: Quorum requirement ensures minority region isolates itself if cross-region link drops."
                ]
            }
        ]

        for q in sys_questions:
            q_id = q["id"]
            f.write(f'''
          <!-- SYS {q["tag"].upper()} -->
          <div id="sys-{q_id}" class="sys-detail-pane space-y-4 sm:space-y-6 {"hidden" if q_id != "q1" else ""}">
            <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-slate-800 pb-4 gap-2">
                <div>
                  <span class="text-xs font-bold text-{q["color"]}-400 uppercase tracking-wider">System Design {q["tag"]}</span>
                  <h2 class="text-lg sm:text-xl font-extrabold text-white leading-tight">{q["title"]}</h2>
                </div>
                <div class="sm:text-right">
                  <span class="text-[11px] font-medium text-slate-400">Reported Recency:</span>
                  <div class="text-xs font-bold text-{q["color"]}-400">{q["recency"]}</div>
                </div>
              </div>

              <!-- Prompt & Requirements -->
              <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-{q["color"]}-400 uppercase">Exact Interview Prompt</span>
                <p class="text-xs sm:text-sm italic text-slate-300 leading-relaxed">
                  "{q["prompt"]}"
                </p>
              </div>

              <!-- VISUAL SYSTEM DESIGN FRAMEWORK DIAGRAM (MATCHING USER REFERENCE LAYOUT) -->
              <div class="bg-slate-950 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-md overflow-hidden relative">
                <!-- Top Bar: Title, Scenario Selector & Controls -->
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 border-b border-slate-800 pb-3">
                  <div class="flex items-center gap-2">
                    <span class="relative flex h-2.5 w-2.5">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-{q["color"]}-400 opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-{q["color"]}-500"></span>
                    </span>
                    <span class="text-xs font-bold text-{q["color"]}-400 uppercase tracking-wider">
                      Interactive Visual System Architecture Topology
                    </span>
                  </div>

                  <div class="flex flex-wrap items-center gap-2">
                    <!-- Scenario Selector -->
                    <select id="{q_id}-scenario-select" onchange="changeScenario('{q_id}', this.value)" class="px-2.5 py-1 text-xs rounded-lg border border-slate-700 bg-slate-900 text-slate-200 font-semibold focus:outline-none min-h-[36px]">
                      <!-- Options rendered dynamically -->
                    </select>

                    <!-- Player Controls -->
                    <div class="flex items-center gap-1 bg-slate-900 border border-slate-800 p-1 rounded-lg">
                      <button onclick="playFlow('{q_id}')" id="{q_id}-play-btn" class="px-2.5 py-1 rounded-md text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white transition-all shadow-xs flex items-center gap-1">
                        <span>▶</span> <span>Play</span>
                      </button>
                      <button onclick="pauseFlow('{q_id}')" class="px-2 py-1 rounded-md text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-all">
                        <span>⏸</span>
                      </button>
                      <button onclick="stepPrevFlow('{q_id}')" class="px-2 py-1 rounded-md text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-all">
                        <span>⏮</span>
                      </button>
                      <button onclick="stepNextFlow('{q_id}')" class="px-2 py-1 rounded-md text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-all">
                        <span>⏭</span>
                      </button>
                      <button onclick="resetFlow('{q_id}')" class="px-2 py-1 rounded-md text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 transition-all">
                        <span>🔄</span>
                      </button>
                    </div>
                  </div>
                </div>

                <!-- TOPOLOGY CANVAS & INTERACTIVE NODE NETWORK -->
                <div class="relative py-2 px-1 space-y-4">
                  
                  <!-- ROW 1: Client Edge & Cloud CDNs -->
                  <div class="grid grid-cols-3 gap-3 text-center text-xs">
                    <div class="p-2.5 rounded-xl border border-slate-800 bg-slate-900/80 flex items-center justify-center gap-2">
                      <span class="text-lg">🌐</span>
                      <div>
                        <strong class="block text-slate-200 text-[11px]">Route 53 DNS</strong>
                        <span class="text-slate-400 text-[9px]">Global Anycast</span>
                      </div>
                    </div>

                    <div id="{q_id}-node-1" onclick="jumpToStep('{q_id}', 0)" class="cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300 relative group">
                      <div class="flex items-center justify-between text-[9px] text-slate-400 uppercase font-bold mb-1">
                        <span>Step 1</span>
                        <span id="{q_id}-node-1-badge" class="px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 text-[8px]">IDLE</span>
                      </div>
                      <div class="text-base mb-0.5">📱</div>
                      <strong id="{q_id}-node-1-title" class="text-slate-100 block text-xs truncate">Client App</strong>
                      <span id="{q_id}-node-1-sub" class="text-blue-400 text-[10px] block truncate">HTTP Request</span>
                    </div>

                    <div class="p-2.5 rounded-xl border border-slate-800 bg-slate-900/80 flex items-center justify-center gap-2">
                      <span class="text-lg">⚡</span>
                      <div>
                        <strong class="block text-slate-200 text-[11px]">Cloudflare CDN</strong>
                        <span class="text-slate-400 text-[9px]">Static Content</span>
                      </div>
                    </div>
                  </div>

                  <!-- CONNECTING SVG FLOW LINES BETWEEN ROW 1 & ROW 2 -->
                  <div class="w-full h-8 relative my-1">
                    <svg class="w-full h-full absolute inset-0" preserveAspectRatio="none" viewBox="0 0 400 30">
                      <path id="{q_id}-line-0-1" class="flow-line" d="M 200 0 L 200 30" />
                    </svg>
                  </div>

                  <!-- ROW 2: Load Balancer & API Gateway -->
                  <div class="grid grid-cols-2 gap-4 text-center text-xs max-w-2xl mx-auto">
                    <div class="p-2.5 rounded-xl border border-slate-800 bg-slate-900/90 flex items-center justify-center gap-2">
                      <span class="text-lg">⚖️</span>
                      <div>
                        <strong class="block text-slate-200 text-[11px]">AWS ALB / Load Balancer</strong>
                        <span class="text-slate-400 text-[9px]">TLS Termination</span>
                      </div>
                    </div>

                    <div id="{q_id}-node-2" onclick="jumpToStep('{q_id}', 1)" class="cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300 relative group">
                      <div class="flex items-center justify-between text-[9px] text-slate-400 uppercase font-bold mb-1">
                        <span>Step 2</span>
                        <span id="{q_id}-node-2-badge" class="px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 text-[8px]">IDLE</span>
                      </div>
                      <div class="text-base mb-0.5">🔑</div>
                      <strong id="{q_id}-node-2-title" class="text-slate-100 block text-xs truncate">API Gateway</strong>
                      <span id="{q_id}-node-2-sub" class="text-emerald-400 text-[10px] block truncate">Auth & Lock</span>
                    </div>
                  </div>

                  <!-- CONNECTING SVG FLOW LINES BETWEEN ROW 2 & ROW 3 -->
                  <div class="w-full h-8 relative my-1">
                    <svg class="w-full h-full absolute inset-0" preserveAspectRatio="none" viewBox="0 0 400 30">
                      <path id="{q_id}-line-1-2" class="flow-line" d="M 200 0 L 100 30 M 200 0 L 300 30" />
                    </svg>
                  </div>

                  <!-- ROW 3: Core Microservices & Database / Event Bus Tier -->
                  <div class="grid grid-cols-2 sm:grid-cols-2 gap-4 text-center text-xs max-w-3xl mx-auto">
                    <div id="{q_id}-node-3" onclick="jumpToStep('{q_id}', 2)" class="cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300 relative group">
                      <div class="flex items-center justify-between text-[9px] text-slate-400 uppercase font-bold mb-1">
                        <span>Step 3</span>
                        <span id="{q_id}-node-3-badge" class="px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 text-[8px]">IDLE</span>
                      </div>
                      <div class="text-base mb-0.5">🗄️</div>
                      <strong id="{q_id}-node-3-title" class="text-slate-100 block text-xs truncate">Primary Storage</strong>
                      <span id="{q_id}-node-3-sub" class="text-amber-400 text-[10px] block truncate">Postgres / Redis</span>
                    </div>

                    <div id="{q_id}-node-4" onclick="jumpToStep('{q_id}', 3)" class="cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300 relative group">
                      <div class="flex items-center justify-between text-[9px] text-slate-400 uppercase font-bold mb-1">
                        <span>Step 4</span>
                        <span id="{q_id}-node-4-badge" class="px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 text-[8px]">IDLE</span>
                      </div>
                      <div class="text-base mb-0.5">🌊</div>
                      <strong id="{q_id}-node-4-title" class="text-slate-100 block text-xs truncate">Async Stream & Workers</strong>
                      <span id="{q_id}-node-4-sub" class="text-purple-400 text-[10px] block truncate">Kafka CDC / ClickHouse</span>
                    </div>
                  </div>
                </div>

                <!-- LIVE MESSAGE PAYLOAD INSPECTION CONSOLE -->
                <div id="{q_id}-console" class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5 space-y-2.5 font-mono text-xs">
                  <div class="flex items-center justify-between border-b border-slate-800/80 pb-2">
                    <div class="flex items-center gap-2">
                      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                      <span id="{q_id}-step-title" class="font-bold text-white text-xs">Step Title</span>
                    </div>
                    <span id="{q_id}-step-protocol" class="text-[10px] px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 font-bold">Protocol</span>
                  </div>

                  <!-- Headers & Payload Split Grid -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-[11px]">
                    <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800/60 space-y-1">
                      <span class="text-[10px] text-slate-400 uppercase font-bold block">Protocol Headers:</span>
                      <pre id="{q_id}-step-headers" class="text-[10px] text-emerald-400 overflow-x-auto no-scrollbar">Headers...</pre>
                    </div>
                    <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800/60 space-y-1">
                      <span class="text-[10px] text-slate-400 uppercase font-bold block">In-Flight Message Body (JSON / SQL):</span>
                      <pre id="{q_id}-step-body" class="text-[10px] text-cyan-300 overflow-x-auto no-scrollbar">Body JSON...</pre>
                    </div>
                  </div>

                  <!-- Action Explanation & Egress Packet -->
                  <div class="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800/60 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-[11px]">
                    <div class="space-y-0.5 flex-1">
                      <span class="text-[10px] text-amber-400 uppercase font-bold block">Internal System Action:</span>
                      <p id="{q_id}-step-action" class="text-slate-300 text-xs leading-relaxed">Action description...</p>
                    </div>
                    <div class="sm:border-l sm:border-slate-800 sm:pl-3 min-w-[200px]">
                      <span class="text-[10px] text-purple-400 uppercase font-bold block">Egress Response Packet:</span>
                      <span id="{q_id}-step-response" class="text-emerald-400 font-bold text-[11px]">Response...</span>
                    </div>
                  </div>
                </div>
              </div>

              <!-- SYSTEM DESIGN DEEP DIVE SECTIONS -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <!-- API Specifications -->
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2">
                  <h3 class="font-bold text-{q["color"]}-400 uppercase text-xs">1. API & Interface Specifications</h3>
                  <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
''')
            for api in q["apis"]:
                f.write(f'''
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-emerald-400 font-bold">{api.get("method","POST")}</span> {api.get("path","")}<br>
                      <span class="text-slate-400">Header:</span> {api.get("headers","")}<br>
                      <span class="text-slate-400">Body/Return:</span> {api.get("body", api.get("returns",""))}
                    </div>
''')
            f.write(f'''
                  </div>
                </div>

                <!-- Database Schemas -->
                <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2">
                  <h3 class="font-bold text-emerald-400 uppercase text-xs">2. Database Schema & Data Models</h3>
                  <div class="space-y-1.5 font-mono text-[11px] text-slate-300">
''')
            for schema in q["schemas"]:
                f.write(f'''
                    <div class="p-2 bg-slate-900 rounded border border-slate-800">
                      <span class="text-amber-400 font-bold">{schema.get("db","")}:</span><br>
                      {schema.get("detail","").replace(chr(10), "<br>")}
                    </div>
''')
            f.write(f'''
                  </div>
                </div>
              </div>

              <!-- High Availability & Resiliency -->
              <div class="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-2 text-xs">
                <h3 class="font-bold text-amber-400 uppercase text-xs">3. Failure Isolation & Resilience Strategy</h3>
                <ul class="space-y-1.5 text-slate-300 text-[11px]">
''')
            for res in q["resilience"]:
                f.write(f'''                  <li>• {res}</li>\n''')
            f.write('''
                </ul>
              </div>

            </div>
          </div>
''')

        f.write('''
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
            <p class="text-slate-300 leading-relaxed">
              Ask about DAU/MAU, read:write ratios, latency SLAs (e.g. sub-50ms POS auth), and consistency requirements (strong consistency for account ledger vs eventual for analytics).
            </p>
          </div>

          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <span class="font-bold text-emerald-400 uppercase">Phase 2: High-Level Architecture (5 - 20 min)</span>
              <span class="text-[11px] text-slate-500">15 Mins</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Draw box components: Client App -> API Gateway -> Microservices -> Cache / Primary DB -> Kafka -> Analytics Engine. Define gRPC vs REST interfaces.
            </p>
          </div>

          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <span class="font-bold text-purple-400 uppercase">Phase 3: Deep Dive & Failure Modes (20 - 40 min)</span>
              <span class="text-[11px] text-slate-500">20 Mins</span>
            </div>
            <p class="text-slate-300 leading-relaxed">
              Address concurrency (Redis Lua scripts), cache stampedes (mutex locks), double-debits (idempotency keys), and multi-region failovers (Raft consensus & DNS routing).
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: SIZING MATH CALCULATOR -->
    <div id="tab-calculators" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div class="border-b border-slate-800 pb-4">
          <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Back-Of-The-Envelope Math</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white">RPS & Storage Horizon Calculator</h2>
          <p class="text-xs text-slate-400">Interactive tools for calculating RPS, throughput, and storage capacity horizons for Capital One interviews.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-xs">
          <div class="space-y-4 bg-slate-950 p-4 rounded-xl border border-slate-800">
            <h3 class="font-bold text-blue-400 uppercase text-xs">Input System Parameters</h3>
            
            <div class="space-y-1">
              <label class="text-[11px] text-slate-400">Monthly Active Requests (Millions):</label>
              <input type="number" id="calc-monthly-req" value="300" oninput="runCalculations()" class="w-full p-2 bg-slate-900 border border-slate-700 rounded-lg text-white font-mono">
            </div>

            <div class="space-y-1">
              <label class="text-[11px] text-slate-400">Peak Multiplier (e.g. 3x for Cyber Monday):</label>
              <input type="number" id="calc-peak-mult" value="3" oninput="runCalculations()" class="w-full p-2 bg-slate-900 border border-slate-700 rounded-lg text-white font-mono">
            </div>

            <div class="space-y-1">
              <label class="text-[11px] text-slate-400">Average Payload Size per Record (KB):</label>
              <input type="number" id="calc-payload-kb" value="2" oninput="runCalculations()" class="w-full p-2 bg-slate-900 border border-slate-700 rounded-lg text-white font-mono">
            </div>

            <div class="space-y-1">
              <label class="text-[11px] text-slate-400">Retention Period (Years):</label>
              <input type="number" id="calc-retention-yrs" value="3" oninput="runCalculations()" class="w-full p-2 bg-slate-900 border border-slate-700 rounded-lg text-white font-mono">
            </div>
          </div>

          <div class="space-y-4 bg-slate-950 p-4 rounded-xl border border-slate-800">
            <h3 class="font-bold text-emerald-400 uppercase text-xs">Calculated Sizing Horizons</h3>
            
            <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 space-y-1">
              <span class="text-[10px] uppercase font-bold text-slate-400">Average Throughput (RPS):</span>
              <div id="res-avg-rps" class="text-lg font-bold text-blue-400 font-mono">115.7 RPS</div>
            </div>

            <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 space-y-1">
              <span class="text-[10px] uppercase font-bold text-slate-400">Peak Throughput Capacity (RPS):</span>
              <div id="res-peak-rps" class="text-lg font-bold text-amber-400 font-mono">347.2 RPS</div>
            </div>

            <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 space-y-1">
              <span class="text-[10px] uppercase font-bold text-slate-400">Total Records (3 Years):</span>
              <div id="res-total-records" class="text-lg font-bold text-emerald-400 font-mono">10.8 Billion</div>
            </div>

            <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 space-y-1">
              <span class="text-[10px] uppercase font-bold text-slate-400">Raw Storage Horizon (TB):</span>
              <div id="res-total-storage" class="text-lg font-bold text-purple-400 font-mono">20.59 TB</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: CHEAT SHEET -->
    <div id="tab-cheat-sheet" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div class="border-b border-slate-800 pb-4 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Quick Reference & Interview Cheat Sheet</span>
            <h2 class="text-lg sm:text-xl font-extrabold text-white">System Design Trade-offs & Cloud Architectural Primitives</h2>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-lg bg-purple-500/10 text-purple-400 border border-purple-500/30 font-bold self-start sm:self-auto">
            PowerDay 2025–2026 Core Reference
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-xs">
          <!-- Card 1: Postgres vs DynamoDB -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-emerald-400 uppercase text-xs flex items-center gap-1.5">
                <span>🗄️</span> <span>1. PostgreSQL vs. DynamoDB</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Database Trade-off</span>
            </div>
            
            <div class="space-y-2 text-[11px] text-slate-300">
              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-emerald-400 font-bold text-xs block">PostgreSQL (Relational RDBMS / OLTP)</strong>
                <p>• <strong>When to Use:</strong> Double-entry payment ledgers, account balances, strict foreign-key relations, multi-table transactions, and keyset pagination.</p>
                <p>• <strong>Pros:</strong> Full ACID compliance, strong consistency, rich SQL expressions, flexible secondary indexes.</p>
                <p>• <strong>Cons:</strong> Write scaling requires complex sharding; connection pooling overhead (HikariCP / PgBouncer required).</p>
              </div>

              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-amber-400 font-bold text-xs block">DynamoDB (NoSQL Key-Value / Document)</strong>
                <p>• <strong>When to Use:</strong> Single-key lookups (Partition Key + Sort Key), idempotency key logs, user session tokens, and PCI audit trails.</p>
                <p>• <strong>Pros:</strong> Single-digit millisecond latency at any scale, serverless (unlimited write auto-scaling, no connection pools).</p>
                <p>• <strong>Cons:</strong> No JOINs, multi-attribute queries require Global Secondary Indexes (GSIs), hard 400 KB item size limit.</p>
              </div>
            </div>
          </div>

          <!-- Card 2: Redis SETNX vs ElastiCache -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-blue-400 uppercase text-xs flex items-center gap-1.5">
                <span>⚡</span> <span>2. ElastiCache vs. Redis SETNX Lock</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Concurrency Primitives</span>
            </div>
            
            <div class="space-y-2 text-[11px] text-slate-300">
              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-blue-400 font-bold text-xs block">AWS ElastiCache (Redis Managed Cluster)</strong>
                <p>• The <strong>managed cloud infrastructure / cluster software</strong> that hosts in-memory data (multi-AZ failover, cluster sharding, replication, and memory persistence).</p>
              </div>

              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-cyan-300 font-bold text-xs block">Redis SETNX (`SET if Not eXists`) Atomic Command</strong>
                <p>• An <strong>atomic command / lock primitive</strong> executed inside Redis (<code>SET key val NX EX 30</code>).</p>
                <p>• Returns <code>1</code> if key is new (lock acquired), or <code>0</code> if key already exists (lock denied).</p>
                <p>• <strong>Idempotency Use Case:</strong> Blocks duplicate payment requests (double-charging) in 1.2ms without hitting PostgreSQL.</p>
                <p>• <strong>Cache Stampede Mutex:</strong> Ensures only 1 thread queries PostgreSQL on a cache miss while 10,000 requests wait for Redis to refresh.</p>
              </div>
            </div>
          </div>

          <!-- Card 3: Debezium CDC -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-purple-400 uppercase text-xs flex items-center gap-1.5">
                <span>🔄</span> <span>3. Debezium Change Data Capture (CDC)</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Event Streaming</span>
            </div>
            
            <div class="space-y-2 text-[11px] text-slate-300">
              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-purple-400 font-bold text-xs block">What is Debezium CDC?</strong>
                <p>• An open-source Kafka Connect connector that captures database row changes in real time by reading the database's internal transaction log (<strong>PostgreSQL WAL</strong> or MySQL Binlog) directly from disk.</p>
              </div>

              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-purple-300 font-bold text-xs block">Why Use CDC in Banking Architectures?</strong>
                <p>• <strong>Zero OLTP DB Impact:</strong> Reads disk logs asynchronously with ZERO <code>SELECT</code> queries or table locks on PostgreSQL.</p>
                <p>• <strong>Solves Dual-Write Bug:</strong> Eliminates inconsistencies caused by apps writing to DB and Kafka in separate steps.</p>
                <p>• <strong>Real-Time Analytics Ingestion:</strong> Streams committed ledger changes into ClickHouse (for monthly spending category charts) or Elasticsearch in &lt; 10ms.</p>
              </div>
            </div>
          </div>

          <!-- Card 4: Lambda vs ECS -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-amber-400 uppercase text-xs flex items-center gap-1.5">
                <span>☁️</span> <span>4. AWS Lambda vs. AWS ECS Fargate</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Compute Strategy</span>
            </div>
            
            <div class="space-y-2 text-[11px] text-slate-300">
              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-amber-400 font-bold text-xs block">AWS Serverless (Lambda)</strong>
                <p>• <strong>Pros:</strong> Auto-scales to 0 (zero cost when idle), zero OS management, ideal for event triggers (SQS/S3).</p>
                <p>• <strong>Cons:</strong> Cold starts (~800ms VPC setup), 15-minute execution limit, unsuited for long-running WebSockets/gRPC.</p>
              </div>

              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-yellow-300 font-bold text-xs block">AWS ECS Fargate (Containerized Microservices)</strong>
                <p>• <strong>Pros:</strong> Zero cold starts, predictable low latency, supports long-running gRPC/WebSocket streams and high sustained RPS.</p>
                <p>• <strong>Cons:</strong> Pay for baseline idle capacity; requires container orchestration tuning.</p>
              </div>
            </div>
          </div>

          <!-- Card 5: Consistency Models -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-rose-400 uppercase text-xs flex items-center gap-1.5">
                <span>⚖️</span> <span>5. Strong Consistency vs. Eventual Consistency</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">CAP Theorem</span>
            </div>
            
            <div class="space-y-2 text-[11px] text-slate-300">
              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-rose-400 font-bold text-xs block">Strong Consistency (PostgreSQL / Raft Consensus / Redis Lua)</strong>
                <p>• <strong>Use Cases:</strong> Account ledger balances, credit limit authorizations, P2P money transfers.</p>
                <p>• <strong>Trade-off:</strong> Higher latency (must wait for cross-node sync/locks); rejects writes if network split occurs (CAP: C over A).</p>
              </div>

              <div class="p-2.5 bg-slate-900/90 rounded-lg border border-slate-800 space-y-1">
                <strong class="text-rose-300 font-bold text-xs block">Eventual Consistency (Debezium CDC → Kafka → ClickHouse)</strong>
                <p>• <strong>Use Cases:</strong> Monthly spending analytics charts, push notifications, audit logs.</p>
                <p>• <strong>Trade-off:</strong> Sub-second propagation delay before updates reflect on analytics dashboards; maximum write throughput and 99.999% availability.</p>
              </div>
            </div>
          </div>

          <!-- Card 6: Interview Strategy -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
              <h3 class="font-bold text-teal-400 uppercase text-xs flex items-center gap-1.5">
                <span>⏱️</span> <span>6. PowerDay 45-Minute System Design Framework</span>
              </h3>
              <span class="text-[10px] font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">Interview Strategy</span>
            </div>
            
            <div class="space-y-1.5 text-[11px] text-slate-300">
              <p>• <strong>0 – 5 min: Scope & Clarifying Questions</strong> (Establish RPS, SLAs, Read:Write ratio, Consistency requirements).</p>
              <p>• <strong>5 – 20 min: High-Level Architecture Diagram</strong> (Draw boxes: Client → Gateway → Service → DB → Event Bus → Analytics).</p>
              <p>• <strong>20 – 40 min: Deep Dives & Bottleneck Mitigations</strong> (Compare PostgreSQL vs DynamoDB, Redis SETNX locks, CDC WAL streaming, Raft consensus).</p>
              <p>• <strong>40 – 45 min: Summary & Retrospective</strong> (Address single points of failure, security, and trade-offs).</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 7: PRACTICE QUIZ -->
    <div id="tab-quiz" class="tab-content hidden space-y-6">
      <div class="bg-slate-850 border border-slate-800 rounded-2xl p-4 sm:p-6 shadow-sm space-y-6">
        <div class="border-b border-slate-800 pb-4">
          <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Self-Assessment</span>
          <h2 class="text-lg sm:text-xl font-extrabold text-white">Capital One Architecture Practice Quiz</h2>
        </div>

        <div class="space-y-6 text-xs">
          <!-- Question 1 -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <p class="font-bold text-white text-xs sm:text-sm">
              1. Two payment swipes of $600 occur simultaneously for a user with a $1,000 credit limit. What mechanism prevents both from approving ($1,200 total)?
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">A) PostgreSQL READ COMMITTED isolation level</button>
              <button onclick="checkAnswer(this, true)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-blue-500">B) Redis single-threaded Lua script executing atomic check-and-decrement</button>
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">C) AWS Lambda provisioned concurrency</button>
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">D) Kafka partition key set to merchant_id</button>
            </div>
            <div class="quiz-feedback hidden p-2.5 rounded-lg font-bold text-xs"></div>
          </div>

          <!-- Question 2 -->
          <div class="p-4 bg-slate-950 border border-slate-800 rounded-xl space-y-3">
            <p class="font-bold text-white text-xs sm:text-sm">
              2. Why is Keyset Pagination preferred over OFFSET/LIMIT for querying customer transaction history in Case 1?
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <button onclick="checkAnswer(this, true)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-blue-500">A) OFFSET N still scans N rows in the index, leading to O(N) performance degradations on deep pages</button>
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">B) Keyset pagination compresses JSON payloads automatically</button>
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">C) OFFSET is not supported in PostgreSQL</button>
              <button onclick="checkAnswer(this, false)" class="p-2.5 rounded-lg border border-slate-800 bg-slate-900 text-left text-slate-300 hover:border-slate-700">D) Keyset pagination guarantees eventual consistency</button>
            </div>
            <div class="quiz-feedback hidden p-2.5 rounded-lg font-bold text-xs"></div>
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
      const activeTab = document.getElementById('tab-' + tabId);
      if (activeTab) activeTab.classList.remove('hidden');

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

    function toggleSolution(caseId) {
      const container = document.getElementById('sol-container-' + caseId);
      const btn = document.getElementById('sol-btn-' + caseId);
      const icon = document.getElementById('sol-icon-' + caseId);

      if (container.classList.contains('hidden')) {
        container.classList.remove('hidden');
        btn.className = "w-full py-3 px-4 bg-blue-900/40 hover:bg-blue-900/60 text-blue-300 font-bold rounded-xl border border-blue-500/50 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all";
        btn.querySelector('span:first-child').innerHTML = "<span>🙈</span> <span>Hide Solution & Engineering Breakdown</span>";
        if (icon) icon.textContent = "▲";
      } else {
        container.classList.add('hidden');
        btn.className = "w-full py-3 px-4 bg-slate-800 hover:bg-slate-750 text-blue-400 font-bold rounded-xl border border-slate-700 flex items-center justify-between text-xs sm:text-sm shadow-xs transition-all";
        btn.querySelector('span:first-child').innerHTML = "<span>👁️</span> <span>Reveal Answer & Fixed Engineering Solution</span>";
        if (icon) icon.textContent = "▼";
      }
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

    /* ENHANCED MULTI-SCENARIO SYSTEM DESIGN MESSAGE TRAJECTORY ENGINE */
    const sysSimData = {
      q1: {
        scenarios: [
          {
            name: "Scenario 1: Happy Path - ACH Statement Payment",
            nodes: [
              { title: "Mobile App", sub: "HTTP POST /payments" },
              { title: "API Gateway", sub: "Redis SETNX Lock" },
              { title: "Aurora Postgres", sub: "SCHEDULED_ACH Write" },
              { title: "ClickHouse OLAP", sub: "Debezium CDC Stream" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Mobile Client Payment Submission", protocol: "HTTP/2 POST (TLS 1.3)", headers: "Idempotency-Key: idemp_9921-a482\\nAuthorization: Bearer eyJhbGciOi...\\nX-Trace-ID: trc_88192a", body: "{\\n  \\"account_id\\": \\"acc_48210\\",\\n  \\"amount\\": 250.00,\\n  \\"type\\": \\"STATEMENT_MIN\\"\\n}", action: "Client initiates statement payment request with unique Idempotency-Key header.", response: "202 Accepted (Pending)", badge: "200 OK" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Gateway Redis SETNX Idempotency Lock", protocol: "Redis TCP (SETNX Command)", headers: "Redis-Cmd: SETNX lock:pay:idemp_9921-a482 PROCESSING EX 86400\\nTTL: 86400s", body: "{\\n  \\"lock_acquired\\": true,\\n  \\"execution_time_ms\\": 1.4\\n}", action: "Gateway checks Redis for duplicate request. Key does not exist, lock acquired atomically.", response: "Lock Granted (1.4ms)", badge: "LOCKED" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Aurora PostgreSQL OLTP Ledger Write", protocol: "PostgreSQL Wire Protocol", headers: "Transaction-Iso: READ COMMITTED\\nSQL-Op: INSERT payment_schedules", body: "INSERT INTO payment_schedules (id, account_id, amount, status)\\nVALUES ('tx_9981', 'acc_48210', 250.00, 'SCHEDULED');", action: "Payment Microservice writes ledger row into PostgreSQL Write-Ahead Log (WAL).", response: "DB Insert Committed (LSN 0/16B2940)", badge: "COMMITTED" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Debezium CDC Streaming into ClickHouse OLAP", protocol: "Kafka Protocol (c1.ledger.payments.v1)", headers: "Topic: c1.ledger.payments.v1\\nPartition: 3\\nKey: acc_48210", body: "{\\n  \\"event\\": \\"PaymentScheduledEvent\\",\\n  \\"txn_id\\": \\"tx_9981\\",\\n  \\"amount\\": 250.00\\n}", action: "Debezium streams Postgres WAL change event without table locks into ClickHouse analytics.", response: "202 Accepted { txn_id: 'tx_9981' }", badge: "COMPLETED" }
            ]
          },
          {
            name: "Scenario 2: Duplicate Request - Redis Lock Rejection",
            nodes: [
              { title: "Mobile Client", sub: "Retry POST" },
              { title: "API Gateway", sub: "Redis Check" },
              { title: "Aurora Postgres", sub: "BYPASSED" },
              { title: "ClickHouse", sub: "BYPASSED" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Mobile App Retries Payment Request", protocol: "HTTP/2 POST /payments (Retry)", headers: "Idempotency-Key: idemp_9921-a482 (REUSED)\\nX-Retry-Attempt: 2", body: "{\\n  \\"account_id\\": \\"acc_48210\\",\\n  \\"amount\\": 250.00\\n}", action: "Client experiences network timeout and re-submits exact same request with identical Idempotency-Key.", response: "Pending...", badge: "RETRY" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Gateway Redis SETNX Lock Returns 0 (Duplicate)", protocol: "Redis TCP (SETNX Command)", headers: "Redis-Cmd: SETNX lock:pay:idemp_9921-a482 PROCESSING\\nRedis-Result: 0 (KEY EXISTS)", body: "{\\n  \\"error\\": \\"DUPLICATE_REQUEST_IN_FLIGHT\\",\\n  \\"original_txn_id\\": \\"tx_9981\\"\\n}", action: "Redis returns 0! Gateway detects duplicate request in-flight, suppresses duplicate DB write, and returns cached payload.", response: "409 Conflict / 202 Cached Response", badge: "REJECTED" }
            ]
          }
        ]
      },
      q2: {
        scenarios: [
          {
            name: "Scenario 1: POS Card Swipe Approval (Lua Atomic Check)",
            nodes: [
              { title: "POS Terminal", sub: "ISO 8583 Swipe" },
              { title: "Auth Gateway", sub: "Decrypt PAN" },
              { title: "Redis Primary", sub: "Lua Atomic Script" },
              { title: "DynamoDB Audit", sub: "Async Log" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Merchant Swipes Card for $150", protocol: "ISO 8583 Message (TLS 1.3)", headers: "Merchant-ID: merch_appl_99\\nTerminal-ID: term_9912", body: "{\\n  \\"pan_hash\\": \\"card_88192\\",\\n  \\"amount\\": 150.00\\n}", action: "POS terminal transmits authorization request for $150 transaction.", response: "Pending Auth Decision", badge: "SWIPED" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Auth Gateway Decrypts PAN & Routes to Redis", protocol: "gRPC Auth Service", headers: "X-Correlation-ID: auth_77192a", body: "{\\n  \\"card_id\\": \\"c_48210\\",\\n  \\"amount\\": 150.00\\n}", action: "Gateway checks cache cluster for card's real-time remaining balance.", response: "Routing to Redis Master", badge: "ROUTED" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Single-Threaded Redis Lua Script Execution", protocol: "Redis EVALSHA (Atomic)", headers: "Script: check_and_decr.lua\\nKey: card_limit:c_48210", body: "{\\n  \\"limit\\": 1000.00,\\n  \\"current_spend\\": 400.00,\\n  \\"new_spend\\": 550.00,\\n  \\"approved\\": true\\n}", action: "Redis executes Lua script: 400 + 150 <= 1000 -> Updates spend to $550 atomically.", response: "APPROVED (00)", badge: "APPROVED" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Async Audit Event Published to DynamoDB", protocol: "AWS SDK DynamoDB PutItem", headers: "Table: auth_events\\nTTL: 90 Days", body: "{\\n  \\"card_id\\": \\"c_48210\\",\\n  \\"amount\\": 150.00,\\n  \\"decision\\": \\"APPROVED\\"\\n}", action: "Approval log written asynchronously to DynamoDB without blocking ISO 8583 response.", response: "HTTP 200 OK (ISO 8583 Resp: 00)", badge: "AUDITED" }
            ]
          }
        ]
      },
      q3: {
        scenarios: [
          {
            name: "Scenario 1: Under Quota Request (200 OK)",
            nodes: [
              { title: "Partner App", sub: "HTTP Request" },
              { title: "Envoy Gateway", sub: "Extract API Key" },
              { title: "Redis ZSET", sub: "Sliding Window" },
              { title: "Core Banking", sub: "Process Request" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Partner API Request", protocol: "HTTP/1.1 GET /v1/accounts", headers: "X-API-Key: key_partner_99", body: "{}", action: "Partner app sends GET request to core banking API.", response: "Pending...", badge: "REQUEST" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Envoy Gateway Key Check", protocol: "Envoy Filter Engine", headers: "Key: key_partner_99", body: "{\\n  \\"client_id\\": \\"client_fintech_99\\",\\n  \\"limit_per_min\\": 100\\n}", action: "Envoy extracts client ID and fetches rate limit quota profile.", response: "Routing to Redis Limiter", badge: "PROFILE OK" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Redis ZSET Sliding Window Counter", protocol: "Redis Pipeline (ZREMRANGEBYSCORE + ZCARD + ZADD)", headers: "ZSET-Key: rate:client_fintech_99\\nWindow: 60s", body: "{\\n  \\"active_count_in_window\\": 42,\\n  \\"limit\\": 100,\\n  \\"allowed\\": true\\n}", action: "Redis purges timestamps older than (now - 60s). Count = 42 < 100 limit. Timestamp added.", response: "Allowed (42/100)", badge: "ZSET PASS" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Core Banking Service Responds with 200 OK", protocol: "gRPC Core Banking", headers: "X-RateLimit-Limit: 100\\nX-RateLimit-Remaining: 57", body: "{\\n  \\"status\\": \\"SUCCESS\\",\\n  \\"data\\": []\\n}", action: "Core banking service returns account data with remaining quota headers.", response: "200 OK (Remaining: 57)", badge: "200 OK" }
            ]
          }
        ]
      },
      q4: {
        scenarios: [
          {
            name: "Scenario 1: Normal Local POS Purchase (Happy Path)",
            nodes: [
              { title: "Merchant POS", sub: "NYC Swipe $45" },
              { title: "Ingress Gateway", sub: "Fast Path Fork" },
              { title: "Flink Stream", sub: "Velocity Check" },
              { title: "ML Scorer", sub: "Score 8/100 (Low)" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Merchant Swipes Card in New York City", protocol: "POS Auth Request", headers: "Terminal: NYC_Starbucks_102\\nCard-ID: c_9921", body: "{\\n  \\"amount\\": 45.00,\\n  \\"city\\": \\"New York\\",\\n  \\"country\\": \\"USA\\"\\n}", action: "POS terminal sends swipe data to fraud evaluation service.", response: "Pending Evaluation", badge: "SWIPED" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Fast Path Authorization Sub-50ms", protocol: "gRPC Pipeline", headers: "X-Trace-ID: trc_nyc_1", body: "{\\n  \\"fast_path_allowed\\": true\\n}", action: "Fast path verifies pin & card status, approving POS in 22ms while emitting event to Kafka for Flink.", response: "POS Approved (22ms)", badge: "APPROVED" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Flink Window Evaluates Distance Velocity", protocol: "Flink Stateful Stream", headers: "State: NYC (10 mins ago) -> NYC (now)\\nVelocity: 0 mph", body: "{\\n  \\"distance_miles\\": 0,\\n  \\"time_delta_mins\\": 10\\n}", action: "Flink confirms distance between purchases is 0 miles. Normal pattern.", response: "Velocity Normal", badge: "FLINK OK" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Machine Learning Inference Score = 8/100", protocol: "Triton ML Model", headers: "Model: Fraud_v4_GBDT", body: "{\\n  \\"fraud_score\\": 8,\\n  \\"decision\\": \\"PASS\\"\\n}", action: "ML model scores transaction 8/100 risk. Transaction settled normally.", response: "Status: 200 OK", badge: "LOW RISK" }
            ]
          }
        ]
      },
      q5: {
        scenarios: [
          {
            name: "Scenario 1: Instant P2P Transfer (Double-Entry Ledger)",
            nodes: [
              { title: "Sender Mobile App", sub: "Transfer $200" },
              { title: "API Gateway", sub: "Auth & Idempotency" },
              { title: "Saga Orchestrator", sub: "Double Entry Ledger" },
              { title: "Kafka Event Bus", sub: "Push Notification" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: User A Transfers $200 to User B", protocol: "HTTP/2 POST /v1/p2p/transfers", headers: "Idempotency-Key: p2p_99182a\\nAuth: Bearer sender_token", body: "{\\n  \\"sender_id\\": \\"usr_A\\",\\n  \\"receiver_id\\": \\"usr_B\\",\\n  \\"amount\\": 200.00\\n}", action: "Sender submits instant P2P transfer request.", response: "202 Accepted", badge: "SUBMITTED" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Gateway Validates Balance & Acquires Lock", protocol: "gRPC Validation", headers: "Redis-Lock: lock:p2p:p2p_99182a", body: "{\\n  \\"sender_balance\\": 1250.00,\\n  \\"valid\\": true\\n}", action: "Gateway verifies sender has $1,250 balance > $200 transfer.", response: "Validation Passed", badge: "VALIDATED" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Double-Entry DB Transaction (PostgreSQL)", protocol: "PostgreSQL BEGIN ... COMMIT", headers: "Txn-Iso: SERIALIZABLE", body: "BEGIN;\\nINSERT INTO ledger (acc, type, amt) VALUES ('A', 'DEBIT', -200.00);\\nINSERT INTO ledger (acc, type, amt) VALUES ('B', 'CREDIT', 200.00);\\nCOMMIT;", action: "Executes paired DEBIT (-$200) and CREDIT (+$200). Sum of debits and credits = $0.", response: "DB Transaction Committed", badge: "LEDGER COMMITTED" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Kafka Event Trigger & Push Notification", protocol: "Kafka c1.p2p.events", headers: "Event: P2PTransferCompleted", body: "{\\n  \\"transfer_id\\": \\"trf_881\\",\\n  \\"receiver_id\\": \\"usr_B\\",\\n  \\"amount\\": 200.00\\n}", action: "Kafka event published. Receiver receives push notification: 'You received $200 from Bob!'", response: "Transfer Complete (200 OK)", badge: "COMPLETED" }
            ]
          }
        ]
      },
      q6: {
        scenarios: [
          {
            name: "Scenario 1: High-Priority Fraud SMS Alert",
            nodes: [
              { title: "Fraud Service", sub: "Emit High Priority" },
              { title: "Notification Router", sub: "Preference Check" },
              { title: "SQS FIFO Queue", sub: "high-priority.fifo" },
              { title: "Twilio Worker", sub: "Delivered in <1.2s" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: Fraud Service Emits Alert Event", protocol: "gRPC Internal", headers: "Priority: HIGH\\nAlert-Type: FRAUD_SUSPECTED", body: "{\\n  \\"user_id\\": \\"u_9921\\",\\n  \\"card\\": \\"c_4821\\",\\n  \\"channel\\": \\"SMS\\"\\n}", action: "Fraud engine emits critical alert to notification engine.", response: "Routing Alert", badge: "EMITTED" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Preference Check Bypasses Quiet Hours", protocol: "User Preference DB", headers: "Is-Fraud: TRUE (Bypass Quiet Hours)", body: "{\\n  \\"phone\\": \\"+15550192834\\",\\n  \\"quiet_hours_active\\": true,\\n  \\"bypass\\": true\\n}", action: "Fraud severity overrides quiet hours settings.", response: "Queued to High Priority", badge: "BYPASSED" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Pushed to High-Priority SQS FIFO Queue", protocol: "AWS SQS SendMessage", headers: "QueueUrl: high-priority-alerts.fifo", body: "{\\n  \\"msg_id\\": \\"msg_88192\\",\\n  \\"dedup_id\\": \\"fraud_c_4821\\"\\n}", action: "Alert pushes to dedicated high-priority queue, bypassing marketing batches.", response: "Enqueued (0ms delay)", badge: "PRIORITY QUEUED" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Twilio Worker Delivers SMS to User Phone", protocol: "HTTPS POST to Twilio REST API", headers: "Host: api.twilio.com", body: "{\\n  \\"sid\\": \\"SM88192a\\",\\n  \\"status\\": \\"delivered\\",\\n  \\"latency_ms\\": 1180\\n}", action: "SMS delivered to user's phone in 1.18 seconds!", response: "DELIVERED (1.18s)", badge: "DELIVERED" }
            ]
          }
        ]
      },
      q7: {
        scenarios: [
          {
            name: "Scenario 1: Cache Miss Thundering Herd (Singleflight Mutex Lock)",
            nodes: [
              { title: "10,000 Concurrent Reqs", sub: "GET /profile/acc_99" },
              { title: "Redis Cache Cluster", sub: "CACHE MISS (Expired)" },
              { title: "Singleflight Mutex", sub: "1 Thread Queries DB" },
              { title: "Redis Cache Update", sub: "9,999 Served from Redis" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: 10,000 Concurrent Requests for Hot Key", protocol: "HTTP GET /v1/profile/acc_99", headers: "Concurrent-Connections: 10,000", body: "{}", action: "Hot cache key profile:acc_99 expires. 10,000 requests hit gateway simultaneously.", response: "Cache Lookup", badge: "10K REQS" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Redis Cluster Returns Cache Miss", protocol: "Redis GET profile:acc_99", headers: "Result: NULL (EXPIRED)", body: "{\\n  \\"key\\": \\"profile:acc_99\\",\\n  \\"hit\\": false\\n}", action: "Redis indicates key is missing.", response: "CACHE MISS", badge: "CACHE MISS" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Singleflight Mutex Lock Granted to Thread 1", protocol: "Redis SETNX lock:profile:acc_99 EX 5", headers: "Lock-Result: Thread 1 = GRANTED, Threads 2-10,000 = WAIT", body: "{\\n  \\"thread_1_granted\\": true,\\n  \\"waiting_threads\\": 9999\\n}", action: "Thread 1 acquires lock & queries DB. Threads 2-10,000 enter 50ms spin-wait.", response: "DB Query In Flight (1 Thread)", badge: "MUTEX LOCK" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Thread 1 Populates Redis -> 9,999 Requests Hit Cache!", protocol: "Redis SET profile:acc_99 EX 300", headers: "TTL: 300s\\nDB-Load: 1 Query total!", body: "{\\n  \\"cache_populated\\": true,\\n  \\"served_from_redis\\": 9999\\n}", action: "Thread 1 writes profile to Redis and releases mutex. 9,999 waiting requests fetch result from Redis instantly!", response: "200 OK (DB Protected)", badge: "STAMPEDE GUARDED" }
            ]
          }
        ]
      },
      q8: {
        scenarios: [
          {
            name: "Scenario 1: 10M Smart Meter Telemetry Ingestion",
            nodes: [
              { title: "10M Smart Meters", sub: "15s Telemetry Pulse" },
              { title: "AWS IoT MQTT Broker", sub: "700k msgs/sec Ingest" },
              { title: "Flink Windowing", sub: "5-min Rolling Avg" },
              { title: "TimescaleDB & S3", sub: "Hypertables & Parquet" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: 10 Million Smart Meters Transmit Data", protocol: "MQTT over TLS 1.3", headers: "Topic: telemetry/meters/m_88192", body: "{\\n  \\"meter_id\\": \\"m_88192\\",\\n  \\"kw_usage\\": 4.2,\\n  \\"timestamp\\": 1775480000\\n}", action: "Meters stream usage data every 15 seconds.", response: "MQTT Ack", badge: "MQTT INGEST" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Kinesis Shards Aggregate Stream Data", protocol: "AWS Kinesis Data Streams", headers: "Shards: 64\\nPartitionKey: m_88192", body: "{\\n  \\"throughput_msgs_sec\\": 700000\\n}", action: "64 Kinesis shards ingest 700,000 messages/sec smoothly.", response: "Kinesis Partitioned", badge: "KINESIS OK" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Flink Windowing Detects Grid Overload Surges", protocol: "Flink Tumbling Window (5m)", headers: "Window: 13:00 - 13:05", body: "{\\n  \\"avg_kw\\": 4.1,\\n  \\"status\\": \\"NORMAL\\"\\n}", action: "Flink computes 5-minute rolling averages per transformer district.", response: "Stream Windowed", badge: "FLINK STREAM" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Batch Writes to TimescaleDB & S3 Parquet", protocol: "TimescaleDB Hypertable & S3 Firehose", headers: "Table: meter_telemetry\\nS3: s3://telemetry/year=2026/", body: "{\\n  \\"inserted_rows\\": 1000,\\n  \\"parquet_compressed\\": true\\n}", action: "Data written to TimescaleDB for dashboards and archived to S3 Parquet for Athena billing queries.", response: "Stored & Archived", badge: "TIMESCALEDB" }
            ]
          }
        ]
      },
      q9: {
        scenarios: [
          {
            name: "Scenario 1: Multi-Region Active-Active Consensus & Failover",
            nodes: [
              { title: "Route 53 Anycast", sub: "Traffic to us-east-1" },
              { title: "us-east-1 Cluster", sub: "Primary Deposit" },
              { title: "CockroachDB Raft", sub: "Cross-Region Sync" },
              { title: "Region Blackout", sub: "DNS Failover to us-west-2" }
            ],
            steps: [
              { nodeIdx: 0, lineId: "line-0-1", title: "Step 1: User Deposited $500 in US-East-1", protocol: "HTTP POST /v1/transactions", headers: "Host: api.capitalone.com\\nGeo: US-East", body: "{\\n  \\"account_id\\": \\"acc_992\\",\\n  \\"amount\\": 500.00\\n}", action: "Route 53 routes request to nearest US-East data center.", response: "Processing...", badge: "US-EAST-1" },
              { nodeIdx: 1, lineId: "line-1-2", title: "Step 2: Raft Consensus Synchronizes Across Regions", protocol: "Raft Consensus (CockroachDB)", headers: "Quorum: 3/5 Replicas Ack", body: "{\\n  \\"us_east_1_ack\\": true,\\n  \\"us_west_2_ack\\": true,\\n  \\"raft_term\\": 42\\n}", action: "Raft consensus writes transaction synchronously to US-East & US-West nodes before acknowledging user.", response: "Raft Committed (Zero RPO)", badge: "RAFT SYNC" },
              { nodeIdx: 2, lineId: "line-1-2", title: "Step 3: Total AWS US-East-1 Regional Outage Occurs!", protocol: "Route 53 Health Check", headers: "us-east-1: UNHEALTHY (503)", body: "{\\n  \\"outage_type\\": \\"TOTAL_DATACENTER_FAILURE\\"\\n}", action: "AWS US-East-1 loses total power. Health check fails after 2 consecutive probes.", response: "Health Check Failed", badge: "OUTAGE ALERT" },
              { nodeIdx: 3, lineId: "line-1-2", title: "Step 4: Route 53 DNS Failover to US-West-2 in 2.8s", protocol: "DNS Anycast Failover", headers: "Active-Region: us-west-2\\nRTO: 2.8s, RPO: 0s", body: "{\\n  \\"traffic_shifted\\": \\"100% to us-west-2\\",\\n  \\"lost_transactions\\": 0\\n}", action: "Route 53 shifts 100% traffic to US-West-2. Zero transaction data lost!", response: "100% Recovered in US-West (2.8s)", badge: "ZERO RPO FAILOVER" }
            ]
          }
        ]
      }
    };

    let activeSimState = {};

    function initSimulators() {
      Object.keys(sysSimData).forEach(qId => {
        activeSimState[qId] = {
          scenarioIdx: 0,
          stepIdx: 0,
          timer: null,
          isPlaying: false
        };

        const selectEl = document.getElementById(qId + '-scenario-select');
        if (selectEl) {
          selectEl.innerHTML = '';
          sysSimData[qId].scenarios.forEach((sc, idx) => {
            const opt = document.createElement('option');
            opt.value = idx;
            opt.textContent = sc.name;
            selectEl.appendChild(opt);
          });
        }
        renderSimStep(qId);
      });
    }

    function changeScenario(qId, scenarioIdx) {
      if (activeSimState[qId].timer) clearInterval(activeSimState[qId].timer);
      activeSimState[qId].scenarioIdx = parseInt(scenarioIdx);
      activeSimState[qId].stepIdx = 0;
      activeSimState[qId].isPlaying = false;
      updatePlayBtnText(qId);
      renderSimStep(qId);
    }

    function renderSimStep(qId) {
      const state = activeSimState[qId];
      const scenario = sysSimData[qId].scenarios[state.scenarioIdx];
      const step = scenario.steps[state.stepIdx];

      // Update Connector SVG Line Animation
      ['line-0-1', 'line-1-2'].forEach(lId => {
        const lineEl = document.getElementById(qId + '-' + lId);
        if (lineEl) {
          if (step.lineId === lId) {
            lineEl.className.baseVal = "flow-line-active";
          } else {
            lineEl.className.baseVal = "flow-line";
          }
        }
      });

      // Update Node Boxes
      for (let i = 1; i <= 4; i++) {
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
              badgeEl.className = "px-1.5 py-0.2 rounded bg-blue-600 text-white font-bold text-[8px]";
            }
          } else if (i - 1 < step.nodeIdx) {
            nodeEl.className = "cursor-pointer p-3 rounded-xl border border-emerald-500/40 bg-emerald-500/10 transition-all duration-300 relative group opacity-85";
            if (badgeEl) {
              badgeEl.textContent = 'DONE';
              badgeEl.className = "px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-400 font-bold text-[8px]";
            }
          } else {
            nodeEl.className = "cursor-pointer p-3 rounded-xl border border-slate-800 bg-slate-900 transition-all duration-300 relative group opacity-60";
            if (badgeEl) {
              badgeEl.textContent = 'IDLE';
              badgeEl.className = "px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 text-[8px]";
            }
          }
        }
      }

      // Update Console Elements
      document.getElementById(qId + '-step-title').textContent = step.title;
      document.getElementById(qId + '-step-protocol').textContent = step.protocol;
      document.getElementById(qId + '-step-headers').textContent = step.headers.replace(/\\\\n/g, '\\n');
      document.getElementById(qId + '-step-body').textContent = step.body.replace(/\\\\n/g, '\\n');
      document.getElementById(qId + '-step-action').textContent = step.action;
      document.getElementById(qId + '-step-response').textContent = step.response;
    }

    function playFlow(qId) {
      const state = activeSimState[qId];
      const scenario = sysSimData[qId].scenarios[state.scenarioIdx];

      if (state.isPlaying) {
        pauseFlow(qId);
        return;
      }

      state.isPlaying = true;
      updatePlayBtnText(qId);

      state.timer = setInterval(() => {
        if (state.stepIdx < scenario.steps.length - 1) {
          state.stepIdx++;
          renderSimStep(qId);
        } else {
          pauseFlow(qId);
        }
      }, 2400);
    }

    function pauseFlow(qId) {
      const state = activeSimState[qId];
      if (state.timer) {
        clearInterval(state.timer);
        state.timer = null;
      }
      state.isPlaying = false;
      updatePlayBtnText(qId);
    }

    function stepNextFlow(qId) {
      pauseFlow(qId);
      const state = activeSimState[qId];
      const scenario = sysSimData[qId].scenarios[state.scenarioIdx];
      if (state.stepIdx < scenario.steps.length - 1) {
        state.stepIdx++;
        renderSimStep(qId);
      }
    }

    function stepPrevFlow(qId) {
      pauseFlow(qId);
      const state = activeSimState[qId];
      if (state.stepIdx > 0) {
        state.stepIdx--;
        renderSimStep(qId);
      }
    }

    function resetFlow(qId) {
      pauseFlow(qId);
      activeSimState[qId].stepIdx = 0;
      renderSimStep(qId);
    }

    function jumpToStep(qId, stepIdx) {
      pauseFlow(qId);
      const scenario = sysSimData[qId].scenarios[activeSimState[qId].scenarioIdx];
      if (stepIdx < scenario.steps.length) {
        activeSimState[qId].stepIdx = stepIdx;
        renderSimStep(qId);
      }
    }

    function updatePlayBtnText(qId) {
      const btn = document.getElementById(qId + '-play-btn');
      if (btn) {
        if (activeSimState[qId].isPlaying) {
          btn.innerHTML = "<span>⏸</span> <span>Pause</span>";
          btn.className = "px-2.5 py-1 rounded-md text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition-all shadow-xs flex items-center gap-1";
        } else {
          btn.innerHTML = "<span>▶</span> <span>Play</span>";
          btn.className = "px-2.5 py-1 rounded-md text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white transition-all shadow-xs flex items-center gap-1";
        }
      }
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

    // Initialize Page & Simulators
    initSimulators();
    runCalculations();
    setGlobalLang('python');
  </script>
</body>
</html>''')

create_index_html()
print("Written index.html with original prompts, legacy buggy code blocks, and interactive hide/reveal solutions for all Tech Cases.")
