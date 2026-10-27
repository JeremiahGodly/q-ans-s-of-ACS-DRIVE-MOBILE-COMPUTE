import os

BASE_DIR = "/Users/godlyvarghese/Desktop/q ans s of ACS,DRIVE,MOBILE COMPUTE"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. HERO BANNER SVG
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="50%" stop-color="#0c1322"/>
      <stop offset="100%" stop-color="#111a2e"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe"/>
      <stop offset="100%" stop-color="#4facfe"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b176fc"/>
      <stop offset="100%" stop-color="#e056fd"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.9"/>
    </linearGradient>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.75" stroke-opacity="0.6"/>
      <circle cx="40" cy="0" r="1.5" fill="#38bdf8" fill-opacity="0.3"/>
    </pattern>
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="1200" height="480" fill="url(#bgGrad)"/>
  <rect width="1200" height="480" fill="url(#gridPattern)"/>

  <circle cx="150" cy="80" r="180" fill="#38bdf8" fill-opacity="0.08" filter="url(#glowCyan)"/>
  <circle cx="1050" cy="380" r="220" fill="#a855f7" fill-opacity="0.08" filter="url(#glowCyan)"/>

  <g transform="translate(60, 42)">
    <rect width="330" height="30" rx="15" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.6"/>
    <circle cx="18" cy="15" r="5" fill="#00f2fe" filter="url(#glowCyan)"/>
    <text x="34" y="20" font-family="'Inter', -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#38bdf8" letter-spacing="1.2">COGNITIVE WARFARE SPECIFICATION</text>
  </g>

  <text x="60" y="122" font-family="'Inter', -apple-system, sans-serif" font-size="44" font-weight="900" fill="#ffffff" letter-spacing="-0.5">
    THE <tspan fill="url(#cyanGrad)">30-PAGE / 3-HOUR</tspan> EXAM ENGINE
  </text>
  <text x="60" y="162" font-family="'Inter', -apple-system, sans-serif" font-size="18.5" font-weight="500" fill="#94a3b8">
    A Neuro-Specialist's Operational Blueprint for Engineering Students: Deconstruct Paragraphs &amp; Conquer University Semesters
  </text>

  <g transform="translate(60, 195)">
    <g transform="translate(0, 0)">
      <rect width="250" height="74" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.2"/>
      <rect x="0" y="0" width="6" height="74" rx="3" fill="#00f2fe"/>
      <text x="22" y="32" font-family="'Inter', sans-serif" font-size="20" font-weight="800" fill="#ffffff">180 Mins = 30 Pgs</text>
      <text x="22" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="500" fill="#38bdf8">Exact 6.0 min/page Velocity</text>
    </g>

    <g transform="translate(270, 0)">
      <rect width="250" height="74" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.2"/>
      <rect x="0" y="0" width="6" height="74" rx="3" fill="#a855f7"/>
      <text x="22" y="32" font-family="'Inter', sans-serif" font-size="20" font-weight="800" fill="#ffffff">Miller's 7±2 Law</text>
      <text x="22" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="500" fill="#c084fc">Synaptic Chunk Deconstruction</text>
    </g>

    <g transform="translate(540, 0)">
      <rect width="250" height="74" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.2"/>
      <rect x="0" y="0" width="6" height="74" rx="3" fill="#10b981"/>
      <text x="22" y="32" font-family="'Inter', sans-serif" font-size="20" font-weight="800" fill="#ffffff">Dual-Coding Model</text>
      <text x="22" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="500" fill="#34d399">40% Visual + 30% Math + 30% Text</text>
    </g>

    <g transform="translate(810, 0)">
      <rect width="270" height="74" rx="12" fill="url(#cardGrad)" stroke="#334155" stroke-width="1.2"/>
      <rect x="0" y="0" width="6" height="74" rx="3" fill="#f59e0b"/>
      <text x="22" y="32" font-family="'Inter', sans-serif" font-size="20" font-weight="800" fill="#ffffff">100% Pass Guarantee</text>
      <text x="22" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="500" fill="#fbbf24">Guaranteed Distinction Framework</text>
    </g>
  </g>

  <g transform="translate(60, 305)">
    <g transform="translate(0, 0)">
      <rect width="345" height="120" rx="14" fill="#111827" stroke="#1f2937" stroke-width="1.5"/>
      <rect x="0" y="0" width="345" height="120" rx="14" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-opacity="0.4"/>
      <circle cx="36" cy="38" r="18" fill="#0369a1" fill-opacity="0.4"/>
      <text x="36" y="44" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#38bdf8" text-anchor="middle">⚡</text>
      <text x="68" y="34" font-family="'Inter', sans-serif" font-size="15" font-weight="800" fill="#ffffff">Advanced Control Systems</text>
      <text x="68" y="52" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600" fill="#64748b">EET401 • State-Space • Lyapunov</text>
      <line x1="20" y1="70" x2="325" y2="70" stroke="#1f2937" stroke-width="1"/>
      <text x="20" y="96" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">5 PYQ Modules • 26 Vector Plots • Full Keys</text>
    </g>

    <g transform="translate(365, 0)">
      <rect width="345" height="120" rx="14" fill="#111827" stroke="#1f2937" stroke-width="1.5"/>
      <rect x="0" y="0" width="345" height="120" rx="14" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-opacity="0.4"/>
      <circle cx="36" cy="38" r="18" fill="#6b21a8" fill-opacity="0.4"/>
      <text x="36" y="44" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#c084fc" text-anchor="middle">⚙️</text>
      <text x="68" y="34" font-family="'Inter', sans-serif" font-size="15" font-weight="800" fill="#ffffff">Electric Drives &amp; Traction</text>
      <text x="68" y="52" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600" fill="#64748b">Choppers • V/f Inverters • FOC • Hoists</text>
      <line x1="20" y1="70" x2="325" y2="70" stroke="#1f2937" stroke-width="1"/>
      <text x="20" y="96" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">9 PYQ Modules • 28 Circuit Blueprints</text>
    </g>

    <g transform="translate(730, 0)">
      <rect width="350" height="120" rx="14" fill="#111827" stroke="#1f2937" stroke-width="1.5"/>
      <rect x="0" y="0" width="350" height="120" rx="14" fill="none" stroke="#10b981" stroke-width="1.5" stroke-opacity="0.4"/>
      <circle cx="36" cy="38" r="18" fill="#065f46" fill-opacity="0.4"/>
      <text x="36" y="44" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#34d399" text-anchor="middle">📡</text>
      <text x="68" y="34" font-family="'Inter', sans-serif" font-size="15" font-weight="800" fill="#ffffff">Mobile Computing</text>
      <text x="68" y="52" font-family="'Inter', sans-serif" font-size="11.5" font-weight="600" fill="#64748b">Cellular Handoff • Mobile IP • MANET</text>
      <line x1="20" y1="70" x2="325" y2="70" stroke="#1f2937" stroke-width="1"/>
      <text x="20" y="96" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">4 PYQ Modules • 30 Protocol Topologies</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero_banner.svg"), "w") as f:
    f.write(hero_svg)

# 2. COGNITIVE COMPRESSION FUNNEL SVG
funnel_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 520" width="100%" height="100%">
  <defs>
    <linearGradient id="fnBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="fnCard" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="arrowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <filter id="glowF" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <rect width="1100" height="520" fill="url(#fnBg)"/>
  
  <!-- Header Title -->
  <text x="50" y="55" font-family="'Inter', sans-serif" font-size="28" font-weight="900" fill="#ffffff">
    THE NEURAL DE-CHUNKING PIPELINE
  </text>
  <text x="50" y="82" font-family="'Inter', sans-serif" font-size="15" font-weight="500" fill="#94a3b8">
    Cognitive Science in Action: Transforming 500-Word Textbook Walls into High-Velocity 3-Page Exam Assets
  </text>

  <!-- 4 Step Flow Columns -->

  <!-- STEP 1: Dense Paragraph -->
  <g transform="translate(50, 120)">
    <rect width="215" height="340" rx="14" fill="url(#fnCard)" stroke="#ef4444" stroke-width="1.5" stroke-opacity="0.7"/>
    <rect x="15" y="15" width="60" height="24" rx="6" fill="#ef4444" fill-opacity="0.2"/>
    <text x="45" y="31" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#ef4444" text-anchor="middle">STAGE 1</text>
    
    <text x="15" y="65" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">Raw Dense Text</text>
    <text x="15" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">Textbook / Key Paragraph</text>
    
    <!-- Visual wall of text simulation -->
    <g transform="translate(15, 105)">
      <rect width="185" height="8" rx="4" fill="#475569"/>
      <rect y="14" width="165" height="8" rx="4" fill="#475569"/>
      <rect y="28" width="185" height="8" rx="4" fill="#475569"/>
      <rect y="42" width="140" height="8" rx="4" fill="#475569"/>
      <rect y="56" width="175" height="8" rx="4" fill="#475569"/>
      <rect y="70" width="150" height="8" rx="4" fill="#475569"/>
    </g>

    <rect x="15" y="200" width="185" height="120" rx="10" fill="#450a0a" fill-opacity="0.5" stroke="#ef4444" stroke-width="1" stroke-opacity="0.4"/>
    <text x="25" y="222" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#fca5a5">⚠️ Cognitive Pathology:</text>
    <text x="25" y="242" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#fecaca">• Working memory choke</text>
    <text x="25" y="262" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#fecaca">• Illusion of competence</text>
    <text x="25" y="282" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#fecaca">• 0% Spatial layout</text>
    <text x="25" y="302" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#fecaca">• Result: Blank paper panic</text>
  </g>

  <!-- Flow Connector 1 -->
  <g transform="translate(275, 270)">
    <circle cx="10" cy="10" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="10" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#38bdf8" text-anchor="middle">→</text>
  </g>

  <!-- STEP 2: Neuro Filter -->
  <g transform="translate(305, 120)">
    <rect width="215" height="340" rx="14" fill="url(#fnCard)" stroke="#f59e0b" stroke-width="1.5" stroke-opacity="0.7"/>
    <rect x="15" y="15" width="60" height="24" rx="6" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="45" y="31" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#f59e0b" text-anchor="middle">STAGE 2</text>
    
    <text x="15" y="65" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">Synaptic Filter</text>
    <text x="15" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">Miller's 7±2 Law &amp; Extraction</text>
    
    <g transform="translate(15, 105)">
      <rect width="185" height="36" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="23" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#fbbf24">1. Keyword Compression</text>
      
      <rect y="44" width="185" height="36" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="67" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#fbbf24">2. Dual-Code Anchoring</text>

      <rect y="88" width="185" height="36" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1"/>
      <text x="12" y="111" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#fbbf24">3. Mathematical Isolate</text>
    </g>

    <rect x="15" y="240" width="185" height="80" rx="10" fill="#78350f" fill-opacity="0.3" stroke="#f59e0b" stroke-width="1" stroke-opacity="0.4"/>
    <text x="25" y="262" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#fde68a">🧠 Neuro Extraction:</text>
    <text x="25" y="282" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#fef3c7">Convert 500 words to 3 nodes: [Definition + Diagram + Formula]</text>
  </g>

  <!-- Flow Connector 2 -->
  <g transform="translate(530, 270)">
    <circle cx="10" cy="10" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="10" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#38bdf8" text-anchor="middle">→</text>
  </g>

  <!-- STEP 3: The 5-Part Modular Scaffold -->
  <g transform="translate(560, 120)">
    <rect width="235" height="340" rx="14" fill="url(#fnCard)" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="15" y="15" width="60" height="24" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="45" y="31" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#38bdf8" text-anchor="middle">STAGE 3</text>
    
    <text x="15" y="65" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">5-Part Scaffold</text>
    <text x="15" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">Modular Writing Blueprint</text>

    <g transform="translate(15, 105)">
      <rect width="205" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">A. Definition (2-Line Core)</text>

      <rect y="38" width="205" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="58" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#38bdf8">B. Vector Diagram (40% Page)</text>

      <rect y="76" width="205" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">C. Equation Box (Framed)</text>

      <rect y="114" width="205" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="134" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#e0f2fe">D. Bullet Steps (3 Key Subsections)</text>

      <rect y="152" width="205" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="10" y="172" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#38bdf8">E. Comparison / Param Matrix</text>
    </g>

    <rect x="15" y="295" width="205" height="30" rx="6" fill="#0369a1" fill-opacity="0.3"/>
    <text x="117" y="315" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#7dd3fc" text-anchor="middle">Fills 2.5 - 3.0 Pages Easily!</text>
  </g>

  <!-- Flow Connector 3 -->
  <g transform="translate(805, 270)">
    <circle cx="10" cy="10" r="14" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="10" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#10b981" text-anchor="middle">→</text>
  </g>

  <!-- STEP 4: 30-Page Exam Warfare Output -->
  <g transform="translate(835, 120)">
    <rect width="215" height="340" rx="14" fill="url(#fnCard)" stroke="#10b981" stroke-width="1.5"/>
    <rect x="15" y="15" width="60" height="24" rx="6" fill="#10b981" fill-opacity="0.2"/>
    <text x="45" y="31" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#10b981" text-anchor="middle">STAGE 4</text>
    
    <text x="15" y="65" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">30-Page Victory</text>
    <text x="15" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#94a3b8">180 Mins • Flawless Execution</text>

    <!-- Mini Book simulation -->
    <g transform="translate(15, 105)">
      <rect width="185" height="110" rx="8" fill="#064e3b" fill-opacity="0.4" stroke="#10b981" stroke-width="1"/>
      <text x="92" y="35" font-family="'Inter', sans-serif" font-size="24" font-weight="900" fill="#34d399" text-anchor="middle">30 / 30</text>
      <text x="92" y="55" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#a7f3d0" text-anchor="middle">PAGES PACKED</text>
      <text x="92" y="80" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#d1fae5" text-anchor="middle">100% Exam Pass</text>
      <text x="92" y="98" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#6ee7b7" text-anchor="middle">S-Grade Guaranteed</text>
    </g>

    <rect x="15" y="230" width="185" height="92" rx="10" fill="#022c22" fill-opacity="0.6" stroke="#10b981" stroke-width="1" stroke-opacity="0.5"/>
    <text x="25" y="252" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#6ee7b7">🎯 Examiner Brain Effect:</text>
    <text x="25" y="272" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#a7f3d0">• "Mastery Bias" triggered</text>
    <text x="25" y="290" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#a7f3d0">• Instant 13-14 / 14 marks</text>
    <text x="25" y="308" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#a7f3d0">• Flawless speed &amp; zero cramp</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "cognitive_compression_funnel.svg"), "w") as f:
    f.write(funnel_svg)

# 3. EXAM PACING TIMELINE SVG
pacing_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 480" width="100%" height="100%">
  <defs>
    <linearGradient id="pcBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080d1a"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="timeBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="25%" stop-color="#818cf8"/>
      <stop offset="55%" stop-color="#c084fc"/>
      <stop offset="85%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="480" fill="url(#pcBg)"/>

  <!-- Title Section -->
  <text x="50" y="55" font-family="'Inter', sans-serif" font-size="28" font-weight="900" fill="#ffffff">
    THE 180-MINUTE / 30-PAGE CHRONO-PACING ARCHITECTURE
  </text>
  <text x="50" y="82" font-family="'Inter', sans-serif" font-size="15" font-weight="500" fill="#94a3b8">
    Eliminating Panic, Writer's Cramp, and Time Choke with High-Yield Neuro-Pacing (Exact 6.0 min/page velocity)
  </text>

  <!-- Main Time Gradient Bar -->
  <rect x="50" y="115" width="1000" height="18" rx="9" fill="url(#timeBar)"/>

  <!-- Tick Marks & Time Labels -->
  <g font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b">
    <text x="50" y="152">00:00 (START)</text>
    <text x="105" y="152">00:10 (10m)</text>
    <text x="360" y="152">01:00 (60m)</text>
    <text x="640" y="152">01:50 (110m)</text>
    <text x="900" y="152">02:40 (160m)</text>
    <text x="1020" y="152" fill="#34d399">03:00 (180m)</text>
  </g>

  <!-- 5 Tactical Phase Blocks -->
  <g transform="translate(50, 175)">
    <!-- Phase 0: 0-10m -->
    <g transform="translate(0, 0)">
      <rect width="90" height="255" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="45" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#38bdf8" text-anchor="middle">PHASE 0</text>
      <text x="45" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#94a3b8" text-anchor="middle">0 - 10 Min</text>
      
      <line x1="10" y1="56" x2="80" y2="56" stroke="#334155" stroke-width="1"/>
      <text x="45" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">Neuro-Triage</text>
      <text x="10" y="105" font-family="'Inter', sans-serif" font-size="9.5" font-weight="500" fill="#cbd5e1">• Scan paper</text>
      <text x="10" y="125" font-family="'Inter', sans-serif" font-size="9.5" font-weight="500" fill="#cbd5e1">• Choose 5 sets</text>
      <text x="10" y="145" font-family="'Inter', sans-serif" font-size="9.5" font-weight="500" fill="#cbd5e1">• Margin notes</text>
      <text x="10" y="165" font-family="'Inter', sans-serif" font-size="9.5" font-weight="500" fill="#cbd5e1">• Calm breath</text>

      <rect x="8" y="200" width="74" height="40" rx="6" fill="#0284c7" fill-opacity="0.3"/>
      <text x="45" y="217" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#38bdf8" text-anchor="middle">PAGES 0</text>
      <text x="45" y="232" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#e0f2fe" text-anchor="middle">Mental Maps</text>
    </g>

    <!-- Phase 1: 10-60m -->
    <g transform="translate(100, 0)">
      <rect width="240" height="255" rx="10" fill="#1e293b" stroke="#818cf8" stroke-width="1.2"/>
      <text x="120" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#818cf8" text-anchor="middle">PHASE 1 (10 - 60 Min)</text>
      <text x="120" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">High Dopamine Blitzkrieg</text>
      
      <line x1="15" y1="56" x2="225" y2="56" stroke="#334155" stroke-width="1"/>
      <text x="15" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Module I &amp; II (Q1 &amp; Q2)</text>
      <text x="15" y="105" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Peak cognitive freshness</text>
      <text x="15" y="125" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Maximum handwriting neatness</text>
      <text x="15" y="145" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Heavy vector diagrams (Class-A/FOC/Kalman)</text>
      <text x="15" y="165" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• 2 full 14-mark answers</text>

      <rect x="15" y="195" width="210" height="45" rx="8" fill="#4338ca" fill-opacity="0.3"/>
      <text x="120" y="215" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#a5b4fc" text-anchor="middle">PAGES 1 TO 9 (9 Pages)</text>
      <text x="120" y="232" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" fill="#e0e7ff" text-anchor="middle">Target Pace: 5.5 min / page</text>
    </g>

    <!-- Phase 2: 60-110m -->
    <g transform="translate(350, 0)">
      <rect width="250" height="255" rx="10" fill="#1e293b" stroke="#c084fc" stroke-width="1.2"/>
      <text x="125" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#c084fc" text-anchor="middle">PHASE 2 (60 - 110 Min)</text>
      <text x="125" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">Steady Grapho-Motor Cruise</text>
      
      <line x1="15" y1="56" x2="235" y2="56" stroke="#334155" stroke-width="1"/>
      <text x="15" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Module III &amp; IV (Q3 &amp; Q4)</text>
      <text x="15" y="105" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Water sip at 60m (prevent dehydration)</text>
      <text x="15" y="125" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Mathematical derivations with framed boxes</text>
      <text x="15" y="145" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Structured bullet mechanics</text>
      <text x="15" y="165" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Moderate grip tension release</text>

      <rect x="15" y="195" width="220" height="45" rx="8" fill="#7e22ce" fill-opacity="0.3"/>
      <text x="125" y="215" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#d8b4fe" text-anchor="middle">PAGES 10 TO 18 (9 Pages)</text>
      <text x="125" y="232" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" fill="#f3e8ff" text-anchor="middle">Cumulative: 18 Pages Locked</text>
    </g>

    <!-- Phase 3: 110-160m -->
    <g transform="translate(610, 0)">
      <rect width="250" height="255" rx="10" fill="#1e293b" stroke="#fb7185" stroke-width="1.2"/>
      <text x="125" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#fb7185" text-anchor="middle">PHASE 3 (110 - 160 Min)</text>
      <text x="125" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">The Final Strike Climax</text>
      
      <line x1="15" y1="56" x2="235" y2="56" stroke="#334155" stroke-width="1"/>
      <text x="15" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#ffffff">Module V &amp; Short Notes (Q5 &amp; Q6)</text>
      <text x="15" y="105" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• High-speed comparison tables</text>
      <text x="15" y="125" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Protocol topologies &amp; waveforms</text>
      <text x="15" y="145" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Maximum space utilization</text>
      <text x="15" y="165" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Punchy closing summaries</text>

      <rect x="15" y="195" width="220" height="45" rx="8" fill="#be123c" fill-opacity="0.3"/>
      <text x="125" y="215" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#fda4af" text-anchor="middle">PAGES 19 TO 27 (9 Pages)</text>
      <text x="125" y="232" font-family="'Inter', sans-serif" font-size="10.5" font-weight="600" fill="#ffe4e6" text-anchor="middle">Cumulative: 27 Pages Locked</text>
    </g>

    <!-- Phase 4: 160-180m -->
    <g transform="translate(870, 0)">
      <rect width="130" height="255" rx="10" fill="#1e293b" stroke="#34d399" stroke-width="1.2"/>
      <text x="65" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#34d399" text-anchor="middle">PHASE 4</text>
      <text x="65" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#94a3b8" text-anchor="middle">160 - 180 Min</text>
      
      <line x1="10" y1="56" x2="120" y2="56" stroke="#334155" stroke-width="1"/>
      <text x="65" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">Cosmetic Audit</text>
      <text x="10" y="105" font-family="'Inter', sans-serif" font-size="9" font-weight="500" fill="#cbd5e1">• Pages 28-30</text>
      <text x="10" y="125" font-family="'Inter', sans-serif" font-size="9" font-weight="500" fill="#cbd5e1">• Pencil underline</text>
      <text x="10" y="145" font-family="'Inter', sans-serif" font-size="9" font-weight="500" fill="#cbd5e1">• Box equations</text>
      <text x="10" y="165" font-family="'Inter', sans-serif" font-size="9" font-weight="500" fill="#cbd5e1">• Q-number check</text>

      <rect x="8" y="195" width="114" height="45" rx="8" fill="#047857" fill-opacity="0.3"/>
      <text x="65" y="215" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#6ee7b7" text-anchor="middle">PAGES 28 TO 30</text>
      <text x="65" y="232" font-family="'Inter', sans-serif" font-size="9" font-weight="600" fill="#a7f3d0" text-anchor="middle">30 FULL PAGES</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "exam_pacing_timeline.svg"), "w") as f:
    f.write(pacing_svg)

# 4. PAGE SPATIAL ARCHITECTURE SVG
page_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 580" width="100%" height="100%">
  <defs>
    <linearGradient id="spBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadowP" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect width="1100" height="580" fill="url(#spBg)"/>

  <!-- Title Section -->
  <text x="50" y="48" font-family="'Inter', sans-serif" font-size="28" font-weight="900" fill="#ffffff">
    THE SPATIAL GEOMETRY OF A PERFECT EXAM PAGE
  </text>
  <text x="50" y="74" font-family="'Inter', sans-serif" font-size="14.5" font-weight="500" fill="#94a3b8">
    The 40 / 30 / 30 Rule: Maximizing Page Volume, Examiner Dopamine, and Marks per Square Inch
  </text>

  <!-- Two Booklet Pages Side-by-Side -->

  <!-- PAGE 1 (Left Sheet) -->
  <g transform="translate(60, 105)" filter="url(#shadowP)">
    <rect width="320" height="440" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <!-- Left red margin line -->
    <line x1="45" y1="0" x2="45" y2="440" stroke="#f87171" stroke-width="1.5"/>
    
    <!-- Margin Question Number -->
    <text x="22" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#1e293b" text-anchor="middle">Q3.(a)</text>

    <!-- Question Title -->
    <text x="55" y="30" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a">KALMAN TEST FOR CONTROLLABILITY</text>
    <line x1="55" y1="35" x2="295" y2="35" stroke="#0284c7" stroke-width="1.5"/>

    <!-- Section 1: Definition Box -->
    <rect x="55" y="48" width="250" height="45" rx="4" fill="#f1f5f9" stroke="#94a3b8" stroke-width="0.8"/>
    <text x="62" y="63" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0369a1">1. Fundamental Axiom &amp; Definition:</text>
    <text x="62" y="76" font-family="'Inter', sans-serif" font-size="8.5" font-weight="500" fill="#334155">A system is state controllable if any initial state x(0)</text>
    <text x="62" y="87" font-family="'Inter', sans-serif" font-size="8.5" font-weight="500" fill="#334155">can be transferred to desired x(t) in finite time t &gt; 0.</text>

    <!-- Section 2: Large Vector Schematic Diagram (40% of Page) -->
    <rect x="55" y="105" width="250" height="155" rx="6" fill="#e2e8f0" stroke="#0284c7" stroke-width="1.2"/>
    <text x="180" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0369a1" text-anchor="middle">Fig 3.1: LTI State Feedback Topology</text>
    
    <!-- Inner Schematic Lines -->
    <rect x="75" y="140" width="45" height="30" rx="3" fill="#ffffff" stroke="#334155" stroke-width="1"/>
    <text x="97" y="159" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">B</text>

    <line x1="120" y1="155" x2="145" y2="155" stroke="#334155" stroke-width="1.5"/>
    <circle cx="152" cy="155" r="7" fill="#ffffff" stroke="#334155" stroke-width="1"/>
    <text x="152" y="159" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">+</text>

    <line x1="159" y1="155" x2="185" y2="155" stroke="#334155" stroke-width="1.5"/>
    <rect x="185" y="140" width="45" height="30" rx="3" fill="#ffffff" stroke="#334155" stroke-width="1"/>
    <text x="207" y="159" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">∫ (sI-A)⁻¹</text>

    <line x1="230" y1="155" x2="275" y2="155" stroke="#334155" stroke-width="1.5"/>
    <text x="282" y="159" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0f172a">x(t)</text>

    <!-- Feedback loop -->
    <line x1="250" y1="155" x2="250" y2="200" stroke="#334155" stroke-width="1.2"/>
    <line x1="250" y1="200" x2="210" y2="200" stroke="#334155" stroke-width="1.2"/>
    <rect x="175" y="188" width="35" height="24" rx="3" fill="#ffffff" stroke="#334155" stroke-width="1"/>
    <text x="192" y="204" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0f172a" text-anchor="middle">-K</text>
    <line x1="175" y1="200" x2="152" y2="200" stroke="#334155" stroke-width="1.2"/>
    <line x1="152" y1="200" x2="152" y2="162" stroke="#334155" stroke-width="1.2"/>

    <text x="180" y="245" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#64748b" text-anchor="middle">[High visual density occupies 1.5 pages easily]</text>

    <!-- Section 3: Framed Governing Formula -->
    <rect x="55" y="275" width="250" height="52" rx="5" fill="#f8fafc" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="62" y="292" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#2563eb">2. Kalman Controllability Matrix (Qc):</text>
    <text x="180" y="314" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">Qc = [ B | AB | A²B | ... | Aⁿ⁻¹B ]</text>

    <!-- Section 4: Rank Condition Criteria -->
    <text x="55" y="348" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#0f172a">3. Necessary &amp; Sufficient Condition:</text>
    <text x="55" y="365" font-family="'Inter', sans-serif" font-size="8.5" font-weight="500" fill="#334155">• Rank(Qc) = n (Dimension of state vector)</text>
    <text x="55" y="380" font-family="'Inter', sans-serif" font-size="8.5" font-weight="500" fill="#334155">• Determinant |Qc| ≠ 0 (Non-singular square matrix)</text>
    <text x="55" y="395" font-family="'Inter', sans-serif" font-size="8.5" font-weight="500" fill="#334155">• Uncontrollable mode present if det(Qc) = 0</text>

    <!-- Bottom Page Number -->
    <text x="180" y="428" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#94a3b8" text-anchor="middle">- Page 1 -</text>
  </g>

  <!-- PAGE 2 (Right Sheet) -->
  <g transform="translate(420, 105)" filter="url(#shadowP)">
    <rect width="320" height="440" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
    <line x1="45" y1="0" x2="45" y2="440" stroke="#f87171" stroke-width="1.5"/>
    
    <text x="22" y="32" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#64748b" text-anchor="middle">(cont.)</text>
    <text x="55" y="30" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a">STEP-WISE COMPUTATION &amp; TEST MATRIX</text>
    <line x1="55" y1="35" x2="295" y2="35" stroke="#0284c7" stroke-width="1.5"/>

    <!-- Section 5: Bulleted Mechanical Steps -->
    <text x="55" y="55" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0369a1">4. Algorithmic Solution Steps:</text>
    
    <rect x="55" y="65" width="250" height="26" rx="4" fill="#f1f5f9"/>
    <text x="62" y="81" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#0f172a">Step 1: Identify System Order (n) from [A] matrix</text>

    <rect x="55" y="96" width="250" height="26" rx="4" fill="#f1f5f9"/>
    <text x="62" y="112" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#0f172a">Step 2: Form Matrix Powers: AB, A²B ... Aⁿ⁻¹B</text>

    <rect x="55" y="127" width="250" height="26" rx="4" fill="#f1f5f9"/>
    <text x="62" y="143" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#0f172a">Step 3: Construct Composite Matrix [Qc]</text>

    <rect x="55" y="158" width="250" height="26" rx="4" fill="#f1f5f9"/>
    <text x="62" y="174" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#0f172a">Step 4: Perform Gaussian Elimination / Determinant</text>

    <!-- Section 6: Comparison / Summary Table -->
    <text x="55" y="202" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#0369a1">5. Kalman vs Gilbert Comparison Matrix:</text>
    
    <!-- Table Simulation -->
    <g transform="translate(55, 212)">
      <rect width="250" height="120" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
      <rect width="250" height="24" rx="4" fill="#0f172a"/>
      <text x="10" y="16" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Feature</text>
      <text x="80" y="16" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Kalman's Test</text>
      <text x="170" y="16" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">Gilbert's Test</text>
      <line x1="0" y1="24" x2="250" y2="24" stroke="#cbd5e1" stroke-width="1"/>

      <line x1="70" y1="0" x2="70" y2="120" stroke="#cbd5e1" stroke-width="1"/>
      <line x1="160" y1="0" x2="160" y2="120" stroke="#cbd5e1" stroke-width="1"/>

      <text x="6" y="42" font-family="'Inter', sans-serif" font-size="8" font-weight="600" fill="#334155">Eigenvalues</text>
      <text x="75" y="42" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#334155">Any form</text>
      <text x="165" y="42" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#334155">Distinct / Jordan</text>
      <line x1="0" y1="52" x2="250" y2="52" stroke="#e2e8f0" stroke-width="1"/>

      <text x="6" y="70" font-family="'Inter', sans-serif" font-size="8" font-weight="600" fill="#334155">Transform</text>
      <text x="75" y="70" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#334155">Not required</text>
      <text x="165" y="70" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#334155">Requires Modal (M)</text>
      <line x1="0" y1="82" x2="250" y2="82" stroke="#e2e8f0" stroke-width="1"/>

      <text x="6" y="102" font-family="'Inter', sans-serif" font-size="8" font-weight="600" fill="#334155">Speed</text>
      <text x="75" y="102" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#16a34a">Fast algebraic</text>
      <text x="165" y="102" font-family="'Inter', sans-serif" font-size="7.5" font-weight="500" fill="#334155">Diagonal dependent</text>
    </g>

    <!-- Section 7: Key Engineering Takeaway -->
    <rect x="55" y="348" width="250" height="42" rx="4" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
    <text x="62" y="364" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#047857">Engineering Significance:</text>
    <text x="62" y="378" font-family="'Inter', sans-serif" font-size="8" font-weight="500" fill="#065f46">Essential for State Feedback Regulator (u = -Kx) pole placement.</text>

    <text x="180" y="428" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#94a3b8" text-anchor="middle">- Page 2 -</text>
  </g>

  <!-- Side Explanatory Annotations (Callout cards) -->
  <g transform="translate(775, 120)">
    <rect width="280" height="110" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <circle cx="20" cy="22" r="6" fill="#38bdf8"/>
    <text x="35" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#ffffff">The 40% Visual Anchor</text>
    <text x="15" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#94a3b8">A large, neat vector schematic:</text>
    <text x="15" y="70" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Consumes 40% of the page cleanly</text>
    <text x="15" y="88" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Takes only 90 seconds to draw</text>
    <text x="15" y="104" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#38bdf8">• Awards 50% marks in 3 seconds</text>
  </g>

  <g transform="translate(775, 250)">
    <rect width="280" height="110" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1"/>
    <circle cx="20" cy="22" r="6" fill="#a855f7"/>
    <text x="35" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#ffffff">Framed Equations</text>
    <text x="15" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#94a3b8">Examiners look for formulas:</text>
    <text x="15" y="70" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Boxed with dashed/solid borders</text>
    <text x="15" y="88" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Centered with clear variable keys</text>
    <text x="15" y="104" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#c084fc">• Prevents formula skipping</text>
  </g>

  <g transform="translate(775, 380)">
    <rect width="280" height="110" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <circle cx="20" cy="22" r="6" fill="#10b981"/>
    <text x="35" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#ffffff">Tables &amp; Bold Bullets</text>
    <text x="15" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#94a3b8">Never write unbroken text blocks:</text>
    <text x="15" y="70" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Tables fill 1/3 page with pure data</text>
    <text x="15" y="88" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#cbd5e1">• Action-verbs in bold lead-ins</text>
    <text x="15" y="104" font-family="'Inter', sans-serif" font-size="11" font-weight="500" fill="#34d399">• Total Pages: 2.5 - 3 per 14-marks!</text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "page_spatial_architecture.svg"), "w") as f:
    f.write(page_svg)

# 5. SUBJECT TRIAD MATRIX SVG
triad_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 460" width="100%" height="100%">
  <defs>
    <linearGradient id="trBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="trCard1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="1100" height="460" fill="url(#trBg)"/>

  <!-- Title Section -->
  <text x="50" y="50" font-family="'Inter', sans-serif" font-size="28" font-weight="900" fill="#ffffff">
    THE TRI-SUBJECT NEURAL REPOSITORY
  </text>
  <text x="50" y="76" font-family="'Inter', sans-serif" font-size="15" font-weight="500" fill="#94a3b8">
    Pre-Compiled, High-Scoring University PYQ Solutions &amp; Engineering Diagrams
  </text>

  <!-- 3 Big Subject Cards -->
  <g transform="translate(50, 110)">
    <!-- CARD 1: ACS -->
    <g transform="translate(0, 0)">
      <rect width="315" height="300" rx="14" fill="url(#trCard1)" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="0" y="0" width="315" height="6" rx="3" fill="#38bdf8"/>
      
      <circle cx="35" cy="40" r="18" fill="#0284c7" fill-opacity="0.3"/>
      <text x="35" y="46" font-family="'Inter', sans-serif" font-size="18" font-weight="900" fill="#38bdf8" text-anchor="middle">⚡</text>
      
      <text x="65" y="38" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">Advanced Control Systems</text>
      <text x="65" y="55" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#38bdf8">Course Code: EET401</text>

      <line x1="20" y1="72" x2="295" y2="72" stroke="#334155" stroke-width="1"/>

      <text x="20" y="98" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#cbd5e1">Core Cognitive Modules:</text>
      <text x="20" y="120" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• State-Space Modeling &amp; Phase Variables</text>
      <text x="20" y="138" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Kalman &amp; Gilbert Controllability</text>
      <text x="20" y="156" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Ackermann's Pole Placement &amp; Observers</text>
      <text x="20" y="174" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Lyapunov Direct &amp; Krasovskii Stability</text>
      <text x="20" y="192" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Describing Functions &amp; Limit Cycles</text>

      <rect x="20" y="215" width="275" height="65" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
      <text x="32" y="235" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#38bdf8">📦 Included Assets:</text>
      <text x="32" y="252" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 5 Verified Answer Keys (2024-2026)</text>
      <text x="32" y="268" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 26 Vectorized Engineering Plots</text>
    </g>

    <!-- CARD 2: ELECTRIC DRIVES -->
    <g transform="translate(345, 0)">
      <rect width="315" height="300" rx="14" fill="url(#trCard1)" stroke="#a855f7" stroke-width="1.5"/>
      <rect x="0" y="0" width="315" height="6" rx="3" fill="#a855f7"/>
      
      <circle cx="35" cy="40" r="18" fill="#7e22ce" fill-opacity="0.3"/>
      <text x="35" y="46" font-family="'Inter', sans-serif" font-size="18" font-weight="900" fill="#c084fc" text-anchor="middle">⚙️</text>
      
      <text x="65" y="38" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">Electric Drives &amp; Traction</text>
      <text x="65" y="55" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#c084fc">Industrial Drives &amp; Power</text>

      <line x1="20" y1="72" x2="295" y2="72" stroke="#334155" stroke-width="1"/>

      <text x="20" y="98" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#cbd5e1">Core Cognitive Modules:</text>
      <text x="20" y="120" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• 4-Quadrant Dynamics &amp; Hoist Loads</text>
      <text x="20" y="138" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Class A to E DC Chopper Drives</text>
      <text x="20" y="156" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Scalar V/f &amp; Slip Power Recovery</text>
      <text x="20" y="174" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Field Oriented Vector Control (FOC)</text>
      <text x="20" y="192" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Regenerative &amp; Dynamic Braking</text>

      <rect x="20" y="215" width="275" height="65" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
      <text x="32" y="235" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#c084fc">📦 Included Assets:</text>
      <text x="32" y="252" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 9 PYQ Answer Keys (2021-2025)</text>
      <text x="32" y="268" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 28 Circuit &amp; Quadrant Waveforms</text>
    </g>

    <!-- CARD 3: MOBILE COMPUTING -->
    <g transform="translate(690, 0)">
      <rect width="315" height="300" rx="14" fill="url(#trCard1)" stroke="#10b981" stroke-width="1.5"/>
      <rect x="0" y="0" width="315" height="6" rx="3" fill="#10b981"/>
      
      <circle cx="35" cy="40" r="18" fill="#047857" fill-opacity="0.3"/>
      <text x="35" y="46" font-family="'Inter', sans-serif" font-size="18" font-weight="900" fill="#34d399" text-anchor="middle">📡</text>
      
      <text x="65" y="38" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#ffffff">Mobile Computing</text>
      <text x="65" y="55" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#34d399">Wireless &amp; Ad-Hoc Networks</text>

      <line x1="20" y1="72" x2="295" y2="72" stroke="#334155" stroke-width="1"/>

      <text x="20" y="98" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#cbd5e1">Core Cognitive Modules:</text>
      <text x="20" y="120" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Cellular Geometry &amp; Handoff (Hard/Soft)</text>
      <text x="20" y="138" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Mobile IP &amp; Triangular Routing (COA)</text>
      <text x="20" y="156" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• MAC Protocols (MACA, MACAW, 802.11)</text>
      <text x="20" y="174" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• Wireless TCP (Snoop, I-TCP, M-TCP)</text>
      <text x="20" y="192" font-family="'Inter', sans-serif" font-size="11.5" font-weight="500" fill="#94a3b8">• MANET Routing (DSDV, AODV, DSR)</text>

      <rect x="20" y="215" width="275" height="65" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
      <text x="32" y="235" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#34d399">📦 Included Assets:</text>
      <text x="32" y="252" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 4 PYQ Answer Keys (2019-2024)</text>
      <text x="32" y="268" font-family="'Inter', sans-serif" font-size="10.5" font-weight="500" fill="#cbd5e1">• 30 Protocol Stack Schematics</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "subject_triad_matrix.svg"), "w") as f:
    f.write(triad_svg)

print("Generated all 5 SVGs successfully!")
