# scratch/acs_local_bank.py
# Complete Manglish & Malayalam (മലയാളം) Local Explanations for all 29 ACS questions (EET401).
# Written in friendly Kerala B.Tech campus lecturer & study group tone.

ACS_LOCAL_ANSWERS = {
    # -------------------------------------------------------------------------
    # acs-q1: State Space Concepts
    # -------------------------------------------------------------------------
    'acs-q1': {
        'manglish': {
            'title': "State Space concepts enthokke aanu? (State, State Variables, State Vector, State Space)",
            'remember_this': {
                'title': "⚡ Key Equation & Ormavekkan",
                'eq': r"$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t), \quad \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t)$$",
                'text': r"<strong>Ormavekkan:</strong> State enn paranjal dynamic system-te memory aanu (energy store cheyyunna $i_L, v_C$ pole). Present state-um input-um arinjaal future motham predict cheyyam."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner">
        <span class="guide-badge">🌴 Manglish Study Guide</span>
        <p><strong>4 Main Terms:</strong> Exam paper-il ee 4 terms-um heading aakki ezhuthanam:</p>
    </div>
    <ul>
        <li><strong>1. State:</strong> Oru dynamic system-te minimum number of variables $\{x_1, x_2, \dots, x_n\}$ aanu state. Time $t_0$-il ee variables-inte value-um, $t \ge t_0$-il kodukkunna input $u(t)$-um arinjaal, future-il system-te ella behaviour-um output-um 100% theerumanikkan pattum.</li>
        <li><strong>2. State Variables:</strong> System-il energy store cheythu vekkunna independent physical elements-inte variables aanu ithu. Electrical circuit-il inductor current $i_L$-um capacitor voltage $v_C$-um; mechanical-il position-um velocity-um.</li>
        <li><strong>3. State Vector:</strong> Ee ella state variables-ineyum koodi oru single column matrix aakki ezhuthiyathaanu state vector: $\mathbf{x}(t) = [x_1, x_2, \dots, x_n]^T \in \mathbb{R}^n$.</li>
        <li><strong>4. State Space:</strong> Ee $n$ state variables coordinate axes aayi varunna $n$-dimensional vector space aanu State Space. Oro samayathum system-te state ee space-il oru single point aayirikkum!</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Think of tracking a cricket ball in flight. Ee nimisham ball-inte current position $(x, y, z)$-um speed $(v_x, v_y, v_z)$-um namukku ariyaamenkil, pinne kaattum gravity-um koodi nokkiyaal ball engottaanu pokunnath ennu 100% parayan pattum. 5 minute munpu ball evidairunnu ennu nokkenda aavashyame illa!</p>
<p>Ee position-um speed-um aanu <strong>state variables</strong>. Avaye oru list aakki ezhuthiyathaanu <strong>state vector</strong>. Athu varayunna graph aanu <strong>state space</strong>!</p>
"""
        },
        'ml': {
            'title': "എന്തൊക്കെയാണ് State Space അടിസ്ഥാന ആശയങ്ങൾ? (State, State Variables, State Vector, State Space)",
            'remember_this': {
                'title': "⚡ Key Equation & ഓർത്തു വെക്കാൻ",
                'eq': r"$$\dot{\mathbf{x}}(t) = A\mathbf{x}(t) + B\mathbf{u}(t), \quad \mathbf{y}(t) = C\mathbf{x}(t) + D\mathbf{u}(t)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> State എന്നാൽ സിസ്റ്റത്തിന്റെ dynamic memory ആണ് (ഊർജ്ജം സൂക്ഷിക്കുന്ന $i_L, v_C$ പോലെ). നിലവിലെ അവസ്ഥയും ഇൻപുട്ടും അറിഞ്ഞാൽ ഭാവി പൂർണ്ണമായി മുൻകൂട്ടി കണക്കാക്കാം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner">
        <span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span>
        <p><strong>4 പ്രധാന നിർവ്വചനങ്ങൾ:</strong></p>
    </div>
    <ul>
        <li><strong>1. State (അവസ്ഥ):</strong> സിസ്റ്റത്തിന്റെ ഭാവി പ്രതികരണങ്ങൾ കൃത്യമായി മുൻകൂട്ടി കാണാൻ ആവശ്യമായ ഏറ്റവും കുറഞ്ഞ വേരിയബിളുകളുടെ കൂട്ടമാണ് state.</li>
        <li><strong>2. State Variables:</strong> സിസ്റ്റത്തിൽ ഊർജ്ജം സംഭരിച്ചു വെക്കുന്ന ഘടകങ്ങളുടെ വേരിയബിളുകൾ (ഇൻഡക്ടറിലെ കറന്റ് $i_L$, കപ്പാസിറ്ററിലെ വോൾട്ടേജ് $v_C$).</li>
        <li><strong>3. State Vector:</strong> എല്ലാ state variables-നെയും ഒരു കോളത്തിൽ അടുക്കി എഴുതിയ മാട്രിക്സ്: $\mathbf{x}(t) = [x_1, x_2, \dots, x_n]^T$.</li>
        <li><strong>4. State Space:</strong> ഈ വേരിയബിളുകൾ അക്ഷങ്ങളായി വരുന്ന $n$-ഡൈമൻഷണൽ ഗ്രാഫിക്കൽ സ്പേസ്.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>ക്രിക്കറ്റ് കളിയിൽ ബോൾ എറിയുന്നത് ആലോചിച്ചു നോക്കൂ. ഈ നിമിഷത്തിൽ ബോളിന്റെ സ്ഥാനവും വേഗതയും നമുക്കറിയാമെങ്കിൽ, കാറ്റും ഗുരുത്വാകർഷണവും വെച്ച് അടുത്ത നിമിഷങ്ങളിൽ ബോൾ എവിടെയെത്തും എന്ന് കൃത്യമായി കണക്കാക്കാം. ഈ സ്ഥാനവും വേഗതയുമാണ് state variables!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q2: Phase Variables
    # -------------------------------------------------------------------------
    'acs-q2': {
        'manglish': {
            'title': "Enthane phase variable enn ariyo? Oru n-th order differential equation engane phase variables vechu state space aakkam?",
            'remember_this': {
                'title': "⚡ Key Equation & Ormavekkan",
                'eq': r"$$x_1 = y, \quad x_2 = \dot{y}, \quad x_3 = \ddot{y}, \quad \dots, \quad x_n = y^{(n-1)}$$",
                'text': r"<strong>Ormavekkan:</strong> Output adya state ayum adutha ella state um adinte derivative ayumane phase variable choose cheyanathe. Matrix $A$-yude last row direct aayi characteristic equation-te coefficients tharum (Companion form)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner">
        <span class="guide-badge">🌴 Manglish Study Guide</span>
        <p><strong>Campus Tone Note:</strong> Exam-il English-il ezhuthanda points step-by-step aayi ivide explain cheythittundu. Formula-sum matrix-um exact aayi nokkuka!</p>
    </div>
    <h4>1. Enthaanu Phase Variables? (Definition)</h4>
    <p>Phase variables enn paranjaal, nammude system output $y(t)$-ne adyathe state variable $x_1$ aayi set cheyyunu. Athu kazhinju varunna oro state-um തൊട്ടു munpathe state-inte exact time derivative aayi choose cheyyunu:</p>
    <div class="math-block-highlight">
        $$x_1 = y(t), \quad x_2 = \dot{y} = \dot{x}_1, \quad x_3 = \ddot{y} = \dot{x}_2, \quad \dots, \quad x_n = y^{(n-1)} = \dot{x}_{n-1}$$
    </div>
    <h4>2. Companion Matrix Formulation:</h4>
    <p>General equation: $y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_0 y = b_0 u(t)$.</p>
    <p>Highest derivative $\dot{x}_n = -a_0 x_1 - a_1 x_2 - \dots - a_{n-1} x_n + b_0 u$.</p>
    <p>Matrix $A$-yude super-diagonal-il 1s varum, bottom row-il negative coefficients $[-a_0, -a_1, \dots, -a_{n-1}]$ varum!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru car drive cheyyunna karyam alochichu nokku. Car-inte road-ile position aanu $x_1$. Car-inte speed (position-te first derivative $\dot{x}_1$) aanu $x_2$. Car-inte acceleration (speed-inte derivative $\dot{x}_2$) aanu $x_3$.</p>
<p>Oru valiya complicated differential equation-ine cheriya simple integrator steps aakki maatan ulla super techniqua-anu phase variables! Output adya state ayum adutha ella state um adinte derivative ayumane phase variable choose cheyanathe. Simple alle?</p>
"""
        },
        'ml': {
            'title': "എന്താണ് phase variables എന്ന് അറിയോ? ഒരു n-th order differential equation എങ്ങനെ phase variables ഉപയോഗിച്ച് state space രൂപത്തിലാക്കാം?",
            'remember_this': {
                'title': "⚡ Key Equation & ഓർത്തു വെക്കാൻ",
                'eq': r"$$x_1 = y, \quad x_2 = \dot{y}, \quad x_3 = \ddot{y}, \quad \dots, \quad x_n = y^{(n-1)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> Output ആദ്യ state ആയും അടുത്ത എല്ലാ state-ഉം അതിന്റെ derivative ആയുമാണ് phase variable choose ചെയ്യുന്നത്. Matrix $A$-യുടെ അവസാന വരി നേരിട്ട് differential equation-ന്റെ coefficients നൽകും (Companion form)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner">
        <span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span>
        <p><strong>പരീക്ഷാ ഗൈഡ്:</strong> പ്രധാന സമവാക്യങ്ങളും സ്റ്റെപ്പുകളും താഴെ കാണുക:</p>
    </div>
    <p>സിസ്റ്റത്തിന്റെ output $y(t)$-നെ $x_1$ ആയും, തുടർന്നുള്ള ഓരോ ഡെറിവേറ്റീവുകളെയും അടുത്തടുത്ത states ആയും എടുക്കുന്ന രീതിയാണ് phase variables.</p>
    $$\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ -a_0 & -a_1 & \dots & -a_{n-1} \end{bmatrix}\mathbf{x} + \begin{bmatrix} 0 \\ \vdots \\ b_0 \end{bmatrix}u$$
</div>
""",
            'understand_simply': r"""
<p>ഒരു കാർ ഓടിക്കുന്ന കാര്യം ആലോചിച്ചു നോക്കൂ. റോഡിലെ കാറിന്റെ സ്ഥാനമാണ് $x_1$. കാറിന്റെ വേഗത $x_2$. കാറിന്റെ ആക്സിലറേഷൻ $x_3$. വളരെ സങ്കീർണ്ണമായ ഒരു വലിയ സമവാക്യത്തെ ലളിതമായ പടവുകളാക്കി മാറ്റുന്ന വിദ്യയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q3: Block Diagram Representation
    # -------------------------------------------------------------------------
    'acs-q3': {
        'manglish': {
            'title': "LTI State-Space system-te continuous-time block diagram engane varakkam?",
            'remember_this': {
                'title': "⚡ Integrator Heart & 4 Matrices",
                'eq': r"$$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x} + D\mathbf{u}$$",
                'text': r"<strong>Ormavekkan:</strong> State variables eppozhum integrators ($\frac{1}{s}$)-te output aayirikkum. $A$ feedback loop aanu, $B$ input gain, $C$ output observation, $D$ direct feedthrough."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Block Diagram Connection Logic:</strong></p>
    <ol>
        <li>Nammal center-il $n$ integrators ($\int$ or $\frac{1}{s}$) varakkunnu. Integrator-te input $\dot{\mathbf{x}}$ aanu, output $\mathbf{x}$ aanu!</li>
        <li>Input $\mathbf{u}$ matrix $B$ vazhi oru summing junction-ilottu pokunnu.</li>
        <li>State $\mathbf{x}$ thirichu matrix $A$ vazhi loop aayi summing junction-il add cheythu $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}$ create cheyyunnu.</li>
        <li>Output junction-il $C\mathbf{x}$-um $D\mathbf{u}$-um add cheythu $\mathbf{y}$ undakkunnu.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru water tank alochichu nokku: Tank-ilottu ozhukivarunna vellathinte flow rate aanu $\dot{x}$ (derivative). Tank-inte ullil sambharicha total vellam aanu $x$ (integrated state). Tank oru integrator pole aanu &mdash; flow-ne kooti vellathinte level aakkunnu!</p>
"""
        },
        'ml': {
            'title': "LTI State-Space സിസ്റ്റത്തിന്റെ ബ്ലോക്ക് ഡയഗ്രം എങ്ങനെ വരയ്ക്കാം?",
            'remember_this': {
                'title': "⚡ പ്രധാന മാട്രിക്സ് ബന്ധങ്ങൾ",
                'eq': r"$$\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x} + D\mathbf{u}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> State variables എപ്പോഴും ഇന്റഗ്രേറ്ററുകളുടെ ഔട്ട്പുട്ട് ആയിരിക്കും. $A, B, C, D$ മാട്രിക്സുകളാണ് മറ്റ് കണക്ഷനുകൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഇന്റഗ്രേറ്ററുകൾക്ക് മുൻപിൽ $\dot{\mathbf{x}}$-ഉം, ഔട്ട്പുട്ടിൽ $\mathbf{x}$-ഉം വരുന്നു. മാട്രിക്സ് $A$ ഫീഡ്‌ബാക്ക് ലൂപ്പായും, $B$ ഇൻപുട്ട് ഗെയിനായും, $C$ ഔട്ട്പുട്ട് മാട്രിക്സായും പ്രവർത്തിക്കുന്നു.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു വാട്ടർ ടാങ്ക് പോലെയാണ് ഇന്റഗ്രേറ്റർ. ഒഴുകിയെത്തുന്ന വെള്ളത്തിന്റെ സ്പീഡ് ($\dot{x}$) ടാങ്കിൽ ചേർന്ന് ജലനിരപ്പായി ($x$) മാറുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q4: Non-Uniqueness of State Space Models
    # -------------------------------------------------------------------------
    'acs-q4': {
        'manglish': {
            'title': "State space representation unique alla ennu engane prove cheyyam? (Similarity Transformation)",
            'remember_this': {
                'title': "⚡ Similarity Transformation Rules",
                'eq': r"$$\bar{A} = P^{-1}AP, \quad \bar{B} = P^{-1}B, \quad \bar{C} = CP, \quad \bar{D} = D$$",
                'text': r"<strong>Ormavekkan:</strong> Non-singular matrix $P$ vechu state coordinate maattinaalum eigenvalues-um transfer function $G(s)$-um maarilla (Strictly Invariant)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Proof Steps:</strong> Let $\mathbf{x} = P\mathbf{z}$, where $P$ is an $n \times n$ invertible matrix ($\det(P) \ne 0$).</p>
    <p>$\dot{\mathbf{x}} = P\dot{\mathbf{z}} = A P\mathbf{z} + B\mathbf{u}$. Both sides $P^{-1}$ premultiply cheythal: $\dot{\mathbf{z}} = (P^{-1}AP)\mathbf{z} + (P^{-1}B)\mathbf{u} = \bar{A}\mathbf{z} + \bar{B}\mathbf{u}$.</p>
    <p>Characteristic equation: $\det(sI - \bar{A}) = \det(sI - P^{-1}AP) = \det(P^{-1}(sI - A)P) = \det(sI - A)$. So poles are identical!</p>
</div>
""",
            'understand_simply': r"""
<p>Temperature alakkunna karyam alochikku: Celsius-il paranjaalum Fahrenheit-il paranjaalum choodu maarunnundo? Illa! Units maarum, pakshe physical temperature same aanu. Athu pole aanu coordinate transformation &mdash; numbers maarum, system dynamics same aayirikkum!</p>
"""
        },
        'ml': {
            'title': "സ്റ്റേറ്റ് സ്പേസ് മോഡൽ unique അല്ല എന്ന് എങ്ങനെ തെളിയിക്കാം? (Similarity Transformation)",
            'remember_this': {
                'title': "⚡ ട്രാൻസ്ഫോർമേഷൻ സമവാക്യം",
                'eq': r"$$\bar{A} = P^{-1}AP, \quad \bar{B} = P^{-1}B, \quad \bar{C} = CP, \quad \bar{D} = D$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മാട്രിക്സ് $P$ മാറിയാലും സിസ്റ്റത്തിന്റെ ഐഗൻവാല്യൂസും ട്രാൻസ്ഫർ ഫങ്ഷനും ഒരിക്കലും മാറില്ല."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>$\mathbf{x} = P\mathbf{z}$ എന്ന് നൽകി മാട്രിക്സ് പുനഃക്രമീകരിക്കുമ്പോൾ ഐഗൻവാല്യൂകൾ മാറ്റമില്ലാതെ തുടരുന്നു എന്ന് കാണിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>താപനില സെൽഷ്യസിലോ ഫാരൻഹീറ്റിലോ പറഞ്ഞാലും ചൂട് ഒന്നാണ്. അതുപോലെ കോർഡിനേറ്റ് മാറ്റിയാലും സിസ്റ്റം ഫിസിക്സ് മാറുന്നില്ല!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q4b: Transfer Function Matrix Derivation
    # -------------------------------------------------------------------------
    'acs-q4b': {
        'manglish': {
            'title': "State Space model-il ninnu Transfer Function Matrix engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Key Derivation Result",
                'eq': r"$$G(s) = C(sI - A)^{-1}B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$",
                'text': r"<strong>Main Point:</strong> Zero initial condition ($\mathbf{x}(0) = \mathbf{0}$) koduthu Laplace transform edukuka. Denominator $\det(sI - A) = 0$ aayirikkum system poles."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Derivation Guide</span></div>
    <p><strong>Step 1:</strong> $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u} \implies s\mathbf{X}(s) - A\mathbf{X}(s) = B\mathbf{U}(s) \implies (sI - A)\mathbf{X}(s) = B\mathbf{U}(s)$.</p>
    <p><strong>Step 2:</strong> $\mathbf{X}(s) = (sI - A)^{-1}B\mathbf{U}(s)$.</p>
    <p><strong>Step 3:</strong> $\mathbf{Y}(s) = C\mathbf{X}(s) + D\mathbf{U}(s) = [C(sI - A)^{-1}B + D]\mathbf{U}(s) \implies G(s) = C(sI - A)^{-1}B + D$.</p>
</div>
""",
            'understand_simply': r"""
<p>Classical control-il transfer function $G(s)$ oru black box pole aanu &mdash; input kodukkunnu, output edukkunnu. State Space ullile energy variables $\mathbf{X}(s)$ thurannu kaanikkunnu. Ee derivation classical-neyum modern state space-neyum connect cheyyunna palam aanu!</p>
"""
        },
        'ml': {
            'title': "State Space മോഡലിൽ നിന്നും Transfer Function Matrix എങ്ങനെ കണ്ടുപിടിക്കാം?",
            'remember_this': {
                'title': "⚡ പ്രധാന സമവാക്യം",
                'eq': r"$$G(s) = C(sI - A)^{-1}B + D = \frac{C \operatorname{adj}(sI - A) B}{\det(sI - A)} + D$$",
                'text': r"<strong>പ്രധാന പോയിന്റ്:</strong> പൂജ്യം പ്രാരംഭ അവസ്ഥ ($\mathbf{x}(0) = \mathbf{0}$) നൽകി Laplace transform എടുക്കുക. ഛേദമായ $\det(sI - A) = 0$ ആണ് സിസ്റ്റത്തിന്റെ ധ്രുവങ്ങൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ഡെറിവേഷൻ</span></div>
    <p>ലാപ്ലേസ് ട്രാൻസ്ഫോർം എടുത്ത് $\mathbf{X}(s)$ വേർതിരിച്ച് ഔട്ട്പുട്ട് സമവാക്യത്തിൽ ചേർക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ക്ലാസിക്കൽ ബ്ലാക്ക് ബോക്സ് രീതിയെയും മോഡേൺ സ്റ്റേറ്റ് സ്പേസ് രീതിയെയും തമ്മിൽ ബന്ധിപ്പിക്കുന്ന സമവാക്യമാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q5: Series RLC Circuit State Modeling
    # -------------------------------------------------------------------------
    'acs-q5': {
        'manglish': {
            'title': "Series RLC circuit-inte State-Space model engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ RLC State Equations",
                'eq': r"$$\begin{bmatrix} \dot{i}_L \\ \dot{v}_C \end{bmatrix} = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix} \begin{bmatrix} i_L \\ v_C \end{bmatrix} + \begin{bmatrix} 1/L \\ 0 \end{bmatrix} v_{in}(t)$$",
                'text': r"<strong>Ormavekkan:</strong> State variables eppozhum energy storage elements aanu: Inductor current $i_L$ (magnetic energy) and capacitor voltage $v_C$ (electrostatic energy)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>KVL & KCL Equations:</strong></p>
    <ul>
        <li>Loop-il KVL: $v_{in}(t) = R i_L + L \frac{di_L}{dt} + v_C \implies \frac{di_L}{dt} = -\frac{R}{L}i_L - \frac{1}{L}v_C + \frac{1}{L}v_{in}$.</li>
        <li>Capacitor current relation: $i_C = C \frac{dv_C}{dt} = i_L \implies \frac{dv_C}{dt} = \frac{1}{C}i_L$.</li>
        <li>Matrix form: $A = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix}$, $B = \begin{bmatrix} 1/L \\ 0 \end{bmatrix}$, $C = \begin{bmatrix} 0 & 1 \end{bmatrix}$ (output $v_C$ aaneel).</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Circuit-le battery off aakkiyaalum, inductor-il magnetic field aayum capacitor-il electric charge aayum energy baaki nilkkum. Ee rendu energy-ne kurikkunna variables aanu $i_L$-um $v_C$-um. Avaye states aayi eduthaal circuit-te complete katha parayan pattum!</p>
"""
        },
        'ml': {
            'title': "ഒരു സീരീസ് RLC സർക്യൂട്ടിന്റെ സ്റ്റേറ്റ് സ്പേസ് മോഡൽ എങ്ങനെ ഉണ്ടാക്കാം?",
            'remember_this': {
                'title': "⚡ RLC സ്റ്റേറ്റ് മാട്രിക്സ്",
                'eq': r"$$\dot{\mathbf{x}} = \begin{bmatrix} -R/L & -1/L \\ 1/C & 0 \end{bmatrix}\mathbf{x} + \begin{bmatrix} 1/L \\ 0 \end{bmatrix}v_{in}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻഡക്ടർ കറന്റും ($i_L$) കപ്പാസിറ്റർ വോൾട്ടേജും ($v_C$) ആണ് സ്വാഭാവിക സ്റ്റേറ്റ് വേരിയബിളുകൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>KVL സമവാക്യം എഴുതി $\frac{di_L}{dt}$-ഉം, കപ്പാസിറ്റർ സമവാക്യത്തിൽ നിന്ന് $\frac{dv_C}{dt}$-ഉം കണ്ടെത്തി മാട്രിക്സ് രൂപത്തിലാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വൈദ്യുതി നിലച്ചാലും ഇൻഡക്ടറിലും കപ്പാസിറ്ററിലും സൂക്ഷിച്ചിരിക്കുന്ന ഊർജ്ജമാണ് സർക്യൂട്ടിന്റെ അവസ്ഥ നിർണ്ണയിക്കുന്നത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q6: Armature-Controlled DC Motor
    # -------------------------------------------------------------------------
    'acs-q6': {
        'manglish': {
            'title': "Armature-Controlled DC motor-te state space equations engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ DC Motor 3x3 State Model",
                'eq': r"$$\begin{bmatrix} \dot{i}_a \\ \dot{\omega} \\ \dot{\theta} \end{bmatrix} = \begin{bmatrix} -R_a/L_a & -K_b/L_a & 0 \\ K_t/J & -B/J & 0 \\ 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} i_a \\ \omega \\ \theta \end{bmatrix} + \begin{bmatrix} 1/L_a \\ 0 \\ 0 \end{bmatrix} v_a$$",
                'text': r"<strong>Ormavekkan:</strong> 3 states: Armature current $i_a$, rotor speed $\omega$, angular position $\theta$. Torque $T = K_t i_a$, Back-EMF $e_b = K_b \omega$."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Two Coupled Domains:</strong></p>
    <ol>
        <li><strong>Electrical:</strong> $v_a = R_a i_a + L_a \frac{di_a}{dt} + e_b \implies \frac{di_a}{dt} = -\frac{R_a}{L_a}i_a - \frac{K_b}{L_a}\omega + \frac{1}{L_a}v_a$.</li>
        <li><strong>Mechanical:</strong> $T = J \frac{d\omega}{dt} + B\omega \implies \frac{d\omega}{dt} = \frac{K_t}{J}i_a - \frac{B}{J}\omega$.</li>
        <li><strong>Position kinematics:</strong> $\frac{d\theta}{dt} = \omega$.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Electrical wire-il koodi ozhukunna current motor-te shaft-ine mechanical motion aakki thirikkunnu. Thiriyumbol motor thaniye oru generator pole act cheythu back-EMF $e_b$ undakki current-ine oppose cheyyunnu. Ee electro-mechanical interaction aanu motor equations!</p>
"""
        },
        'ml': {
            'title': "ആർമേച്ചർ നിയന്ത്രിത DC മോട്ടോറിന്റെ സ്റ്റേറ്റ് സ്പേസ് സമവാക്യങ്ങൾ രൂപീകരിക്കുക",
            'remember_this': {
                'title': "⚡ മോട്ടോർ സ്റ്റേറ്റ് സമവാക്യം",
                'eq': r"$$\dot{\mathbf{x}} = \begin{bmatrix} -R_a/L_a & -K_b/L_a & 0 \\ K_t/J & -B/J & 0 \\ 0 & 1 & 0 \end{bmatrix}\mathbf{x} + \begin{bmatrix} 1/L_a \\ 0 \\ 0 \end{bmatrix}v_a$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇലക്ട്രിക്കൽ ആർമേച്ചർ സമവാക്യവും മെക്കാനിക്കൽ റോട്ടർ സമവാക്യവും ബാക്ക്-ഇഎംഎഫ് വഴി പരസ്പരം ബന്ധപ്പെട്ടിരിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ആർമേച്ചർ ലൂപ്പിൽ KVL ഉപയോഗിച്ച് $\frac{di_a}{dt}$-ഉം, ന്യൂട്ടന്റെ റൊട്ടേഷണൽ നിയമം ഉപയോഗിച്ച് $\frac{d\omega}{dt}$-ഉം കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>കറന്റ് കൊടുക്കുമ്പോൾ മോട്ടോർ കറങ്ങുന്നു, കറങ്ങുമ്പോൾ തിരിച്ച് ബാക്ക്-ഇഎംഎഫ് ഉണ്ടാകുന്നു. ഇവ തമ്മിലുള്ള സംയോജനമാണ് ഡിസി മോട്ടോർ മോഡൽ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q7: Canonical Forms (Controllable & Diagonal/Jordan)
    # -------------------------------------------------------------------------
    'acs-q7': {
        'manglish': {
            'title': "Controllable Canonical Form-um Diagonal (Jordan) Canonical Form-um engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Canonical Forms Comparison",
                'eq': r"$$\Lambda = M^{-1}AM = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n), \quad \dot{\mathbf{z}} = \Lambda \mathbf{z} + M^{-1}B u$$",
                'text': r"<strong>Ormavekkan:</strong> Controllable canonical form pole-placement eluppamaakkunnu. Diagonal form modes-ine decouple cheythu oro mode-um independently solve cheyyan sahayikkunnu (using modal matrix $M$ of eigenvectors)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Controllable Form:</strong> Companion matrix format. Last row gives $-a_0, -a_1, \dots, -a_{n-1}$. Matrix $B = [0, 0, \dots, 1]^T$. Direct state feedback $u = -Kx$ calculate cheyyan ithaanu best.</p>
    <p><strong>2. Diagonal Form:</strong> Matrix $A$-yude eigenvectors $v_1, v_2, \dots, v_n$ eduthu modal matrix $M = [v_1 \dots v_n]$ undakkuka. Athu vechu transform cheythaal $\Lambda = M^{-1}AM = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. Coupling full maaripoyitt oro first-order equation separate aayi kitum!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru complex dance troupe alochikku: Ellaavarum koottikuzhanju kalichaal aaraanu thettu cheyyunnathennu ariyilla (Coupled system). Pakshe ellaavarkkum separate rows koduthu mathram nirthiyaal (Diagonalization), oro aaludeyum performance independently evaluate cheyyam!</p>
"""
        },
        'ml': {
            'title': "കൺട്രോളബിൾ കാനോനിക്കൽ ഫോമും ഡയഗണൽ (ജോർദാൻ) ഫോമും എങ്ങനെ കണ്ടുപിടിക്കാം?",
            'remember_this': {
                'title': "⚡ ഡയഗണൽ മാട്രിക്സ്",
                'eq': r"$$\Lambda = \operatorname{diag}(\lambda_1, \lambda_2, \dots, \lambda_n) = M^{-1}AM$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഐഗൻവെക്ടറുകളുടെ മോഡൽ മാട്രിക്സ് ഉപയോഗിച്ച് സിസ്റ്റം വേരിയബിളുകളെ പരസ്പരം വേർപെടുത്താം (Decoupling)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>കൺട്രോളബിൾ ഫോം പോൾ പ്ലേസ്‌മെന്റിനും, ഡയഗണൽ ഫോം ഓരോ മോഡുകളെയും വെവ്വേറെ വിശകലനം ചെയ്യാനും ഉപയോഗിക്കുന്നു.</p>
</div>
""",
            'understand_simply': r"""
<p>കെട്ടുപിണഞ്ഞു കിടക്കുന്ന നൂലുകളെ നേരെയാക്കി വെവ്വേറെയാക്കുന്നത് പോലെയാണ് ഡയഗണലൈസേഷൻ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q7b: Field-Controlled DC Servomotor
    # -------------------------------------------------------------------------
    'acs-q7b': {
        'manglish': {
            'title': "Field-Controlled DC Servomotor-te State-Space Model engane undakkam?",
            'remember_this': {
                'title': "⚡ Field-Controlled 2x2 Model",
                'eq': r"$$\begin{bmatrix} \frac{di_f}{dt} \\ \frac{d\omega}{dt} \end{bmatrix} = \begin{bmatrix} -R_f/L_f & 0 \\ K_{tf}/J & -B/J \end{bmatrix} \begin{bmatrix} i_f \\ \omega \end{bmatrix} + \begin{bmatrix} 1/L_f \\ 0 \end{bmatrix} v_f$$",
                'text': r"<strong>Ormavekkan:</strong> Armature current $I_a$ constant aanu. So back-EMF feedback loop-e illa! Field circuit-il ninnu mechanical rotor-lekku matram unidirectional drive aanu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Field circuit: $v_f = R_f i_f + L_f \frac{di_f}{dt} \implies \frac{di_f}{dt} = -\frac{R_f}{L_f}i_f + \frac{1}{L_f}v_f$.</p>
    <p>2. Torque: $T_e = K_f \phi I_a = K_{tf} i_f = J \dot{\omega} + B\omega \implies \dot{\omega} = \frac{K_{tf}}{J}i_f - \frac{B}{J}\omega$.</p>
    <p>Matrix $A$-yude top-right element $0$ aanu, because motor speed field current-ine thirichu affect cheyyilla!</p>
</div>
""",
            'understand_simply': r"""
<p>Armature control-il motor thiriyumbol back-EMF undaayi circuit-ine thirichu distrub cheyyum. Pakshe field control-il armature current constant aayathukond back-EMF feedback illa &mdash; ithu oru one-way street pole aanu!</p>
"""
        },
        'ml': {
            'title': "ഫീൽഡ് നിയന്ത്രിത DC സെർവോമോട്ടോറിന്റെ സ്റ്റേറ്റ് സ്പേസ് മോഡൽ രൂപീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഫീൽഡ് മോഡൽ മാട്രിക്സ്",
                'eq': r"$$\dot{\mathbf{x}} = \begin{bmatrix} -R_f/L_f & 0 \\ K_{tf}/J & -B/J \end{bmatrix}\mathbf{x} + \begin{bmatrix} 1/L_f \\ 0 \end{bmatrix}v_f$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ആർമേച്ചർ കറന്റ് സ്ഥിരമായതിനാൽ ബാക്ക്-ഇഎംഎഫ് ഫീഡ്‌ബാക്ക് ഉണ്ടാകുന്നില്ല."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഫീൽഡ് വോൾട്ടേജ് സമവാക്യവും റോട്ടർ ടോർക്ക് സമവാക്യവും എഴുതുക. ബാക്ക്-ഇഎംഎഫ് ഇല്ലാത്തതിനാൽ മാട്രിക്സ് ലളിതമാണ്.</p>
</div>
""",
            'understand_simply': r"""
<p>ഇവിടെ ഇൻപുട്ട് കൺട്രോൾ സിഗ്നൽ ഒരു വൺ-വേ ട്രാഫിക് പോലെയാണ്, മോട്ടോർ സ്പീഡ് സർക്യൂട്ടിനെ തിരിച്ചൊന്നും ബാധിക്കില്ല!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q8: Solution of Autonomous State Equations (Zero-Input Response)
    # -------------------------------------------------------------------------
    'acs-q8': {
        'manglish': {
            'title': "Autonomous state equation $\\dot{\\mathbf{x}} = A\\mathbf{x}$-nte solution engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Autonomous Solution Formula",
                'eq': r"$$\mathbf{x}(t) = \mathcal{L}^{-1}\{(sI - A)^{-1}\} \mathbf{x}(0) = e^{At} \mathbf{x}(0) = \Phi(t) \mathbf{x}(0)$$",
                'text': r"<strong>Ormavekkan:</strong> External input illatha samayathu ($u(t) = 0$), initial energy $\mathbf{x}(0)$ karanam undakunna response aanu Zero-Input Response (ZIR). Resolvent matrix $(sI - A)^{-1}$-te inverse Laplace eduthal State Transition Matrix $\Phi(t)$ kitum."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Given: $\dot{\mathbf{x}}(t) = A\mathbf{x}(t), \quad \mathbf{x}(0) = \mathbf{x}_0$.</p>
    <p>2. Laplace transform: $s\mathbf{X}(s) - \mathbf{x}(0) = A\mathbf{X}(s) \implies (sI - A)\mathbf{X}(s) = \mathbf{x}(0)$.</p>
    <p>3. $\mathbf{X}(s) = (sI - A)^{-1}\mathbf{x}(0)$.</p>
    <p>4. Taking inverse Laplace: $\mathbf{x}(t) = \mathcal{L}^{-1}\{(sI - A)^{-1}\}\mathbf{x}(0) = e^{At}\mathbf{x}(0)$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru unjal (swing) thallividatha samayathu, alpam mukalilekku valichu pidichu vittal athu thaniye aadi aadi nilkkunna response aanu Zero-Input Response. Ee aattathinte pattern theerumanikkunnath matrix exponential $e^{At}$ aanu!</p>
"""
        },
        'ml': {
            'title': "ഹോമോജീനിയസ് സ്റ്റേറ്റ് സമവാക്യത്തിന്റെ പരിഹാരം എങ്ങനെ കണ്ടെത്താം?",
            'remember_this': {
                'title': "⚡ ZIR സമവാക്യം",
                'eq': r"$$\mathbf{x}(t) = e^{At}\mathbf{x}(0) = \Phi(t)\mathbf{x}(0)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പുറത്തുനിന്ന് ഇൻപുട്ട് ഇല്ലാതെ പ്രാരംഭ ഊർജ്ജം കൊണ്ടുമാത്രം ഉണ്ടാകുന്ന പ്രതികരണമാണിത്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ലാപ്ലേസ് ട്രാൻസ്ഫോർം എടുത്ത് $(sI - A)^{-1}$ ന്റെ ഇൻവേഴ്സ് എടുക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു ഊഞ്ഞാൽ പുറത്തുനിന്ന് തള്ളാതെ, ആദ്യം ഒരല്പം ഉയർത്തി വിട്ടാൽ സ്വയം ആടുന്നതാണ് സീറോ-ഇൻപുട്ട് റെസ്‌പോൺസ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q9: Properties of State Transition Matrix
    # -------------------------------------------------------------------------
    'acs-q9': {
        'manglish': {
            'title': "State Transition Matrix $\\Phi(t) = e^{At}$-nte 5 main properties enthokke aanu?",
            'remember_this': {
                'title': "⚡ 5 Core STM Properties",
                'eq': r"$$\Phi(0) = I, \;\; \Phi^{-1}(t) = \Phi(-t), \;\; \Phi(t_1+t_2) = \Phi(t_1)\Phi(t_2), \;\; [\Phi(t)]^k = \Phi(kt), \;\; \dot{\Phi}(t) = A\Phi(t)$$",
                'text': r"<strong>Ormavekkan:</strong> Exam-il ee 5 properties ezhuthi proof kodukkanam: $\Phi(0)=e^0=I$; time reverse cheythaal inverse $\Phi(-t) = \Phi^{-1}(t)$; matrix derivative $\dot{\Phi} = A e^{At} = A\Phi$."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>Property 1:</strong> $\Phi(0) = e^{A \cdot 0} = I$ (Identity matrix).</li>
        <li><strong>Property 2:</strong> $\Phi^{-1}(t) = [e^{At}]^{-1} = e^{-At} = \Phi(-t)$ (Time reversal gives inverse).</li>
        <li><strong>Property 3:</strong> $\Phi(t_1 + t_2) = e^{A(t_1+t_2)} = e^{At_1} \cdot e^{At_2} = \Phi(t_1)\Phi(t_2)$ (Semigroup property).</li>
        <li><strong>Property 4:</strong> $[\Phi(t)]^k = \Phi(kt)$.</li>
        <li><strong>Property 5:</strong> $\frac{d}{dt}\Phi(t) = \frac{d}{dt}(e^{At}) = A e^{At} = A \Phi(t) = \Phi(t) A$.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>STM oru time machine pole aanu: $\Phi(t_1)$ vechu time $t_1$-lekku travel cheyyam, pinne $\Phi(t_2)$ vechu $t_2$-lekku travel cheyyam &mdash; athu direct aayi $\Phi(t_1 + t_2)$ travel cheyyunnathinu equal aanu! Negative time $-\Phi(-t)$ travel cheythal thirichu start cheytha sthalathu thanne ethum!</p>
"""
        },
        'ml': {
            'title': r"സ്റ്റേറ്റ് ട്രാൻസിഷൻ മാട്രിക്സിന്റെ ($\Phi(t)$) പ്രധാന സവിശേഷതകൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ 5 പ്രധാന സവിശേഷതകൾ",
                'eq': r"$$\Phi(0) = I, \quad \Phi(-t) = \Phi^{-1}(t), \quad \Phi(t_1+t_2) = \Phi(t_1)\Phi(t_2)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> സമയം പൂജ്യമാകുമ്പോൾ ഐഡന്റിറ്റി മാട്രിക്സ് ലഭിക്കുന്നു; നെഗറ്റീവ് സമയം മാട്രിക്സിന്റെ ഇൻവേഴ്സ് നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>5 പ്രോപ്പർട്ടികളും അവയുടെ ചെറിയ തെളിവുകളും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സിസ്റ്റത്തെ ഒരു സമയത്തുനിന്ന് മറ്റൊരു സമയത്തേക്ക് കൊണ്ടുപോകുന്ന ഒരു ടൈം-ട്രാവൽ മാട്രിക്സാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q9b: Discrete-Time State Space Analysis
    # -------------------------------------------------------------------------
    'acs-q9b': {
        'manglish': {
            'title': "Discrete-Time State Space model-um Pulse Transfer Function-um engane define cheyyam?",
            'remember_this': {
                'title': "⚡ Discrete State Equations & Pulse TF",
                'eq': r"$$\mathbf{x}(k+1) = G\mathbf{x}(k) + H\mathbf{u}(k), \quad \mathbf{y}(k) = C\mathbf{x}(k) + D\mathbf{u}(k), \quad G(z) = C(zI - G)^{-1}H + D$$",
                'text': r"<strong>Ormavekkan:</strong> Continuous time-le derivative $\dot{\mathbf{x}}$-nu pakaram sample index $\mathbf{x}(k+1)$ varunnu. $s$-domain-le $(sI - A)$-nu pakaram $z$-transform-il $(zI - G)$ varunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Continuous model-il sampling period $T$ apply cheythal: $G = e^{AT}$, $H = \int_0^T e^{A\tau} B d\tau$.</p>
    <p>2. Taking $z$-transform with zero initial conditions: $z\mathbf{X}(z) - G\mathbf{X}(z) = H\mathbf{U}(z) \implies \mathbf{X}(z) = (zI - G)^{-1}H\mathbf{U}(z)$.</p>
    <p>3. Output: $\mathbf{Y}(z) = [C(zI - G)^{-1}H + D]\mathbf{U}(z) \implies G(z) = \frac{\mathbf{Y}(z)}{\mathbf{U}(z)} = C(zI - G)^{-1}H + D$.</p>
</div>
""",
            'understand_simply': r"""
<p>Continuous time oru flowing video pole aanu (continuous stream). Discrete time athile oro photography frames pole aanu &mdash; frame $k$-il ninnu frame $k+1$-lekku maattunna matrix aanu $G$!</p>
"""
        },
        'ml': {
            'title': "ഡിസ്ക്രീറ്റ്-ടൈം സ്റ്റേറ്റ് സ്പേസ് മോഡലും പൾസ് ട്രാൻസ്ഫർ ഫങ്ഷനും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഡിസ്ക്രീറ്റ് ട്രാൻസ്ഫർ ഫങ്ഷൻ",
                'eq': r"$$G(z) = C(zI - G)^{-1}H + D$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> $z$-ട്രാൻസ്ഫോർം ഉപയോഗിച്ച് ഡിജിറ്റൽ കൺട്രോൾ സിസ്റ്റങ്ങളിൽ വിശകലനം ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സാമ്പ്ലിംഗ് ഇൻഡക്സ് $k$-ലും $z$-ഡൊമൈനിലും സമവാക്യങ്ങൾ രൂപീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വീഡിയോയിൽ നിന്ന് ഓരോ ഫോട്ടോകളായി സാമ്പിൾ ചെയ്ത് ഡിജിറ്റൽ കമ്പ്യൂട്ടറിൽ പ്രോസസ്സ് ചെയ്യുന്ന രീതിയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q10: Cayley-Hamilton Theorem for STM
    # -------------------------------------------------------------------------
    'acs-q10': {
        'manglish': {
            'title': "Cayley-Hamilton Theorem use cheythu State Transition Matrix $e^{At}$ engane kandupidikkam?",
            'remember_this': {
                'title': "⚡ Cayley-Hamilton Matrix Polynomial",
                'eq': r"$$\Delta(A) = A^n + a_{n-1}A^{n-1} + \dots + a_0 I = \mathbf{0}, \quad e^{At} = \alpha_0(t)I + \alpha_1(t)A + \dots + \alpha_{n-1}(t)A^{n-1}$$",
                'text': r"<strong>Ormavekkan:</strong> Statement: 'Every square matrix satisfies its own characteristic equation'. Infinite series $e^{At}$-ne finite $(n-1)$-th order polynomial aakki maattam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Step-by-Step Procedure:</strong></p>
    <ol>
        <li>Find characteristic equation: $\det(\lambda I - A) = 0 \implies \lambda_1, \lambda_2, \dots, \lambda_n$.</li>
        <li>Set scalar equation for each eigenvalue: $e^{\lambda_i t} = \alpha_0(t) + \alpha_1(t)\lambda_i + \dots + \alpha_{n-1}(t)\lambda_i^{n-1}$.</li>
        <li>Solve for unknown scalar functions $\alpha_0(t), \alpha_1(t), \dots$.</li>
        <li>Substitute scalars into matrix equation: $e^{At} = \alpha_0(t)I + \alpha_1(t)A + \dots + \alpha_{n-1}(t)A^{n-1}$.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>$e^{At} = I + At + \frac{A^2t^2}{2!} + \dots$ ennath infinite terms ulla oru valiya list aanu. Pakshe Cayley-Hamilton theorem oru shortcut tharunnu: $A^n$-ne lower powers $A^{n-1}, \dots, I$ aakki substitute cheythu finite terms aakki mathram calculate cheythaal mathi!</p>
"""
        },
        'ml': {
            'title': "കെയ്‌ലി-ഹാമിൽട്ടൺ തിയറം ഉപയോഗിച്ച് സ്റ്റേറ്റ് ട്രാൻസിഷൻ മാട്രിക്സ് എങ്ങനെ കണക്കാക്കാം?",
            'remember_this': {
                'title': "⚡ തിയറം പ്രസ്താവന",
                'eq': r"$$e^{At} = \alpha_0 I + \alpha_1 A + \dots + \alpha_{n-1} A^{n-1}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 'ഓരോ സ്ക്വയർ മാട്രിക്സും സ്വന്തം സ്വഭാവ സമവാക്യം അനുസരിക്കുന്നു.' അനന്തമായ പദങ്ങളെ പരിമിതമായ മാട്രിക്സ് രൂപത്തിലാക്കാം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഐഗൻവാല്യൂസ് കണ്ടെത്തി $\alpha_i(t)$ കണ്ടുപിടിച്ച് $e^{At}$ മാട്രിക്സ് പോളിനോമിയലിൽ സബ്സ്റ്റിറ്റ്യൂട്ട് ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>അനന്തമായി നീളുന്ന സീരീസിനെ ചുരുക്കി എളുപ്പത്തിൽ കണക്കുകൂട്ടാനുള്ള കുറുക്കുവഴിയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q11: Complete Solution of Non-Homogeneous State Equations
    # -------------------------------------------------------------------------
    'acs-q11': {
        'manglish': {
            'title': "Non-Homogeneous State Equation $\\dot{\\mathbf{x}} = A\\mathbf{x} + B\\mathbf{u}$-nte complete solution engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Complete Response = ZIR + ZSR",
                'eq': r"$$\mathbf{x}(t) = \underbrace{e^{At}\mathbf{x}(0)}_{\text{Zero-Input Response (ZIR)}} + \underbrace{\int_0^t e^{A(t - \tau)} B \mathbf{u}(\tau) d\tau}_{\text{Zero-State Response (ZSR)}}$$",
                'text': r"<strong>Ormavekkan:</strong> Total response = Initial condition response (ZIR) + External input convolution integral response (ZSR). Integrating factor $e^{-At}$ premultiply cheythu direct aayi integrate cheyyam."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Rewrite: $\dot{\mathbf{x}} - A\mathbf{x} = B\mathbf{u}$.</p>
    <p>2. Premultiply by integrating factor $e^{-At}$: $e^{-At}\dot{\mathbf{x}} - e^{-At}A\mathbf{x} = \frac{d}{dt}[e^{-At}\mathbf{x}(t)] = e^{-At}B\mathbf{u}(t)$.</p>
    <p>3. Integrate from $0$ to $t$: $e^{-At}\mathbf{x}(t) - \mathbf{x}(0) = \int_0^t e^{-A\tau}B\mathbf{u}(\tau)d\tau$.</p>
    <p>4. Premultiply by $e^{At}$: $\mathbf{x}(t) = e^{At}\mathbf{x}(0) + \int_0^t e^{A(t - \tau)}B\mathbf{u}(\tau)d\tau$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru car-inte total speed nokkiyaal: 1) Initial speed karanam rolling cheyyunna part (ZIR), plus 2) Driver accelerator pedal chavitti kodukkunna power karanam koodunna speed (ZSR). Ee randum koodi add cheythaal total speed kitum!</p>
"""
        },
        'ml': {
            'title': "നോൺ-ഹോമോജീനിയസ് സ്റ്റേറ്റ് സമവാക്യത്തിന്റെ പൂർണ്ണ പരിഹാരം എങ്ങനെ കണ്ടെത്താം?",
            'remember_this': {
                'title': "⚡ പൂർണ്ണ പ്രതികരണം",
                'eq': r"$$\mathbf{x}(t) = e^{At}\mathbf{x}(0) + \int_0^t e^{A(t - \tau)} B \mathbf{u}(\tau) d\tau$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ആകെ പ്രതികരണം = പ്രാരംഭ അവസ്ഥയുടെ പ്രതികരണം (ZIR) + ഇൻപുട്ട് കൊണ്ടുണ്ടാകുന്ന പ്രതികരണം (ZSR)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>$e^{-At}$ കൊണ്ട് ഗുണിച്ച് ഇന്റഗ്രേറ്റ് ചെയ്ത് പരിഹാരം കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വാഹനത്തിന്റെ മുൻപത്തെ വേഗതയും ആക്സിലറേറ്റർ അമർത്തുമ്പോൾ കൂടുന്ന വേഗതയും തമ്മിൽ കൂട്ടുന്നതാണ് ആകെ വേഗത!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q12: Kalman's Duality Principle
    # -------------------------------------------------------------------------
    'acs-q12': {
        'manglish': {
            'title': "Kalman's Duality Principle between Controllability and Observability explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Duality Principle Mapping",
                'eq': r"$$[A, B] \text{ is Controllable} \iff [A^T, B^T] \text{ is Observable}, \quad Q_o(A^T, B^T) = Q_c^T(A, B)$$",
                'text': r"<strong>Ormavekkan:</strong> Controllability problem-ine transpose matrix $A^T, C^T$ vechu direct aayi observability problem aakki maattam. Control controller design-um observer design-um duals aanu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. System $S_1 = (A, B, C)$. Controllability matrix $Q_c = [B \;\; AB \;\; \dots \;\; A^{n-1}B]$.</p>
    <p>2. Dual system $S_2 = (A^T, C^T, B^T)$. Observability matrix $Q_o = [C^T \;\; A^T C^T \;\; \dots]^T$.</p>
    <p>3. Notice that $Q_o(A^T, B^T) = Q_c^T(A, B)$. So $\operatorname{rank}(Q_c) = n \iff \operatorname{rank}(Q_o) = n$.</p>
    <p>Significance: Ackermann's pole placement code transpose cheythaal Luenberger observer design direct aayi cheyyam!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru mirror reflection pole aanu duality: Mirror-te oru vashathu controller design irunnal, thirichulla reflection aanu observer design. Mathematics same aanu, matrics transpose cheythaal mathi!</p>
"""
        },
        'ml': {
            'title': "കാൽമാന്റെ ഡ്യുവാലിറ്റി തത്വം (Duality Principle) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഡ്യുവാലിറ്റി തത്വം",
                'eq': r"$$[A, B] \text{ controllable} \iff [A^T, B^T] \text{ observable}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> കൺട്രോളബിലിറ്റിയും ഒബ്സർവബിലിറ്റിയും ഗണിതശാസ്ത്രപരമായി ഒന്നിന്റെ ട്രാൻസ്പോസ് മറ്റൊന്നായ ഡ്യുവൽ പ്രോപ്പർട്ടികളാണ്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>മാട്രിക്സ് ട്രാൻസ്പോസ് വഴി $Q_o = Q_c^T$ എന്ന് കാണിച്ച് തുല്യത തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു കണ്ണാടിയിൽ നോക്കുന്നത് പോലെയാണ് &mdash; കൺട്രോളർ ഡിസൈൻ നേരെയാണെങ്കിൽ ഒബ്സർവർ ഡിസൈൻ അതിന്റെ പ്രതിബിംബമാണ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q13: Gilbert's Method
    # -------------------------------------------------------------------------
    'acs-q13': {
        'manglish': {
            'title': "Gilbert's Method use cheythu Controllability-um Observability-um engane test cheyyam?",
            'remember_this': {
                'title': "⚡ Gilbert's Non-Zero Row/Column Test",
                'eq': r"$$\dot{\mathbf{z}} = \Lambda \mathbf{z} + \bar{B}\mathbf{u}, \quad \mathbf{y} = \bar{C}\mathbf{z}, \quad \bar{B} = M^{-1}B, \quad \bar{C} = CM$$",
                'text': r"<strong>Ormavekkan:</strong> Distinct eigenvalues aayirikkumbol: $\bar{B}$-il oru row full zero aaneel uncontrollable! $\bar{C}$-il oru column full zero aaneel unobservable!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Steps:</strong></p>
    <ol>
        <li>Diagonalize system: $\Lambda = M^{-1}AM = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.</li>
        <li>Compute transformed input matrix $\bar{B} = M^{-1}B$. Check each row: if row $i$ has all zeros, mode $\lambda_i$ cannot be controlled!</li>
        <li>Compute transformed output matrix $\bar{C} = CM$. Check each column: if column $j$ has all zeros, mode $\lambda_j$ cannot be observed!</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru switchboard nokku: Oro bulb-num oro switch undu (Diagonalized modes). Oru bulb-ilottu wire connect cheythittillel ($\bar{B}$ row zero), switch ittaalum bulb kathilla (uncontrollable). Oru bulb kathunnathu puratheku kaanan glass window illel ($\bar{C}$ column zero), athu unobservable aanu!</p>
"""
        },
        'ml': {
            'title': "ഗിൽബർട്ട്സ് രീതി (Gilbert's Method) ഉപയോഗിച്ച് കൺട്രോളബിലിറ്റിയും ഒബ്സർവബിലിറ്റിയും എങ്ങനെ പരിശോധിക്കാം?",
            'remember_this': {
                'title': "⚡ ഗിൽബർട്ട്സ് നിബന്ധന",
                'eq': r"$$\bar{B} \text{ row zero } \implies \text{Uncontrollable}, \quad \bar{C} \text{ col zero } \implies \text{Unobservable}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഡയഗണൽ രൂപത്തിൽ $\bar{B}$-യിലെ ഒരു വരി മുഴുവൻ പൂജ്യമായാൽ uncontrollable; $\bar{C}$-യിലെ കോളം പൂജ്യമായാൽ unobservable."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡയഗണലൈസ് ചെയ്ത് $\bar{B}, \bar{C}$ മാട്രിക്സുകളിലെ പൂജ്യങ്ങൾ പരിശോധിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വയർ കണക്ട് ചെയ്യാത്ത സ്വിച്ച് പോലെയാണ് അൺകൺട്രോളബിൾ മോഡ് &mdash; അമർത്തിയാലും ഫാൻ ഓടില്ല!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q13b: PBH Rank Tests
    # -------------------------------------------------------------------------
    'acs-q13b': {
        'manglish': {
            'title': "Popov-Belevitch-Hautus (PBH) Rank Tests for Controllability and Observability explain cheyyuka.",
            'remember_this': {
                'title': "⚡ PBH Rank Conditions",
                'eq': r"$$\operatorname{rank}[sI - A \quad B] = n, \quad \operatorname{rank}\begin{bmatrix} sI - A \\ C \end{bmatrix} = n \quad \forall s = \lambda_i$$",
                'text': r"<strong>Ormavekkan:</strong> Matrix $A$-yude oro eigenvalue $\lambda_i$ eduthu substitute cheythu check cheythal mathi. Kalman test pole high powers $A^{n-1}$ calculate cheyyenda aavashyame illa!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>PBH Controllability:</strong> System controllable aakanamenkil, matrix $M_c(s) = [sI - A \;\; B]$ has rank $n$ for all eigenvalues $s = \lambda_1, \dots, \lambda_n$.</p>
    <p>2. <strong>PBH Observability:</strong> System observable aakanamenkil, matrix $M_o(s) = \begin{bmatrix} sI - A \\ C \end{bmatrix}$ has rank $n$ for all eigenvalues $s = \lambda_i$.</p>
    <p>Advantage: Repeated eigenvalues varumbolum PBH test accurate aayi work cheyyum!</p>
</div>
""",
            'understand_simply': r"""
<p>Kalman test oru valiya powers calculating procedure aanu ($A, A^2, A^3 \dots$). Pakshe PBH test direct aayi eigenvalues substitute cheythu matrix rank nokkunna valare smart and fast method aanu!</p>
"""
        },
        'ml': {
            'title': "PBH (Popov-Belevitch-Hautus) റാങ്ക് ടെസ്റ്റുകൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ PBH റാങ്ക് നിബന്ധന",
                'eq': r"$$\operatorname{rank}[\lambda_i I - A \quad B] = n, \quad \operatorname{rank}\begin{bmatrix} \lambda_i I - A \\ C \end{bmatrix} = n$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> എല്ലാ ഐഗൻവാല്യൂസിനും മാട്രിക്സ് റാങ്ക് $n$ ആണെങ്കിൽ സിസ്റ്റം കൺട്രോളബിളും ഒബ്സർവബിളും ആയിരിക്കും."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഓരോ ഐഗൻവാല്യൂവിലും മാട്രിക്സ് റാങ്ക് $n$ ആണെന്ന് കാണിച്ച് ടെസ്റ്റ് വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വലിയ ഗുണനങ്ങളില്ലാതെ നേരിട്ട് ഐഗൻവാല്യൂസ് വെച്ച് പരിശോധിക്കാനുള്ള എളുപ്പവഴിയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q14: State Feedback by Pole Placement (Ackermann's Formula)
    # -------------------------------------------------------------------------
    'acs-q14': {
        'manglish': {
            'title': "Pole Placement State Feedback Controller design (Ackermann's Formula) engane cheyyam?",
            'remember_this': {
                'title': "⚡ Ackermann's Formula",
                'eq': r"$$K = \begin{bmatrix} 0 & 0 & \dots & 1 \end{bmatrix} Q_c^{-1} \phi_d(A), \quad u = -K\mathbf{x} + r$$",
                'text': r"<strong>Ormavekkan:</strong> Closed-loop poles desired locations-ilottu move cheyyan state feedback $u = -K\mathbf{x}$ use cheyyunnu. $\phi_d(A)$ desired characteristic polynomial-il matrix $A$ substitute cheythathaanu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Design Steps:</strong></p>
    <ol>
        <li>Check controllability: $\det(Q_c) \ne 0$.</li>
        <li>Write desired characteristic polynomial from given poles $\mu_1, \dots, \mu_n$: $\phi_d(s) = (s - \mu_1)\dots(s - \mu_n) = s^n + \alpha_{n-1}s^{n-1} + \dots + \alpha_0$.</li>
        <li>Form matrix $\phi_d(A) = A^n + \alpha_{n-1}A^{n-1} + \dots + \alpha_0 I$.</li>
        <li>Calculate $K = [0 \;\; 0 \dots 1] Q_c^{-1} \phi_d(A)$.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru unstable boat-il aalukal irikkunna karyam alochikku: Boat chavitti aadumbol, aalukal thirichu weight shift cheythu ($u = -Kx$) boat-ine stable aakki nirthunnu. Athupole unstable poles-ine namukku ishtamulla stable sthalathekku maati nirthunna technique aanu pole placement!</p>
"""
        },
        'ml': {
            'title': "പോൾ പ്ലേസ്‌മെന്റ് സ്റ്റേറ്റ് ഫീഡ്‌ബാക്ക് കൺട്രോളർ ഡിസൈൻ (അക്കർമാൻസ് ഫോർമുല) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ അക്കർമാൻസ് സമവാക്യം",
                'eq': r"$$K = [0 \quad \dots \quad 1] Q_c^{-1} \phi_d(A)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പോളുകളെ ഇഷ്ടമുള്ള സ്ഥാനങ്ങളിലേക്ക് മാറ്റി സിസ്റ്റത്തെ സ്റ്റേബിൾ ആക്കാനുള്ള ഫീഡ്‌ബാക്ക് ഗെയിൻ മാട്രിക്സ് ($K$)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>കൺട്രോളബിലിറ്റി ഉറപ്പുവരുത്തി, ആഗ്രഹിക്കുന്ന പോളുകളിൽ നിന്ന് $\phi_d(A)$ ഉണ്ടാക്കി ഗെയിൻ $K$ കണ്ടുപിടിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ആടിയുലയുന്ന ബോട്ടിനെ ആളുകൾ ബാലൻസ് ചെയ്തു നിർത്തുന്നത് പോലെ അൺസ്റ്റേബിൾ സിസ്റ്റത്തെ സ്റ്റേബിളാക്കുന്ന വിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q15: Full-Order State Observer
    # -------------------------------------------------------------------------
    'acs-q15': {
        'manglish': {
            'title': "Full-Order State Observer (Luenberger Observer) engane design cheyyam?",
            'remember_this': {
                'title': "⚡ Observer Dynamics & Error Equation",
                'eq': r"$$\dot{\hat{\mathbf{x}}} = A\hat{\mathbf{x}} + B\mathbf{u} + L(\mathbf{y} - C\hat{\mathbf{x}}), \quad \dot{\mathbf{e}} = (A - LC)\mathbf{e}$$",
                'text': r"<strong>Ormavekkan:</strong> Output measurement error $(\mathbf{y} - C\hat{\mathbf{x}})$ observer-lekku feedback koduthu states estimate cheyyunnu. Observer poles controller poles-inekkalum 2 to 5 times faster aayirikkannam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Actual system: $\dot{\mathbf{x}} = A\mathbf{x} + B\mathbf{u}, \quad \mathbf{y} = C\mathbf{x}$.</p>
    <p>2. Observer estimate: $\dot{\hat{\mathbf{x}}} = A\hat{\mathbf{x}} + B\mathbf{u} + L(\mathbf{y} - \hat{\mathbf{y}})$, where $\hat{\mathbf{y}} = C\hat{\mathbf{x}}$.</p>
    <p>3. Estimation error $\mathbf{e}(t) = \mathbf{x}(t) - \hat{\mathbf{x}}(t) \implies \dot{\mathbf{e}} = \dot{\mathbf{x}} - \dot{\hat{\mathbf{x}}} = (A - LC)\mathbf{e}$.</p>
    <p>4. Design $L$ such that eigenvalues of $(A - LC)$ are in the far left-half $s$-plane so error decays rapidly to zero!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru submarine വെള്ളത്തിനടിയിൽ pokumbol direct aayi kannu vechu nokkaan pattilla. So sonar signals vechum speed meters vechum computer ullil oru virtual submarine simulation run cheyyunnu. Real output-um simulated output-um compare cheythu error zero aakkunna system aanu Observer!</p>
"""
        },
        'ml': {
            'title': "ഫുൾ-ഓർഡർ സ്റ്റേറ്റ് ഒബ്സർവർ (Luenberger Observer) ഡിസൈൻ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഒബ്സർവർ എറർ സമവാക്യം",
                'eq': r"$$\dot{\mathbf{e}} = (A - LC)\mathbf{e}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> അളക്കാൻ കഴിയാത്ത ആന്തരിക അവസ്ഥകളെ ഔട്ട്പുട്ട് ഫീഡ്‌ബാക്ക് വഴി കണക്കാക്കാൻ ഒബ്സർവർ സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>എസ്റ്റിമേഷൻ എറർ $\mathbf{e} = \mathbf{x} - \hat{\mathbf{x}}$ പൂജ്യത്തിലേക്ക് വേഗത്തിൽ കുറയുന്ന തരത്തിൽ ഗെയിൻ $L$ ഡിസൈൻ ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വെള്ളത്തിനടിയിലെ മുങ്ങിക്കപ്പലിന്റെ സ്ഥാനം സെൻസറുകൾ വെച്ച് കമ്പ്യൂട്ടറിൽ കൃത്യമായി പ്രവചിക്കുന്നത് പോലെയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q16: Characteristics of Non-Linear Systems
    # -------------------------------------------------------------------------
    'acs-q16': {
        'manglish': {
            'title': "Non-Linear control systems-nte main characteristics & physical phenomena enthokke aanu?",
            'remember_this': {
                'title': "⚡ 5 Unique Non-Linear Phenomena",
                'eq': r"$$\text{Superposition Fails: } f(x_1 + x_2) \ne f(x_1) + f(x_2), \quad f(\alpha x) \ne \alpha f(x)$$",
                'text': r"<strong>Ormavekkan:</strong> Linear systems-il kaanatha 5 phenomena: Jump Resonance, Subharmonic Oscillations, Limit Cycles (sustained oscillations without external input), Frequency-dependent stability, and Multiple Equilibrium points."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Superposition fails:</strong> Response to sum of inputs is not the sum of individual responses.</li>
        <li><strong>2. Limit Cycles:</strong> Fixed amplitude and frequency-il self-sustained oscillations (neither grows to infinity nor dies to zero).</li>
        <li><strong>3. Jump Resonance:</strong> Input frequency smooth aayi vary cheyyumbol output amplitude-il sudden discontinuous jump undaakunnu.</li>
        <li><strong>4. Subharmonic Oscillations:</strong> Input frequency $\omega$ aaneel output-il $\omega/2, \omega/3$ frequencies kaanunnu.</li>
        <li><strong>5. Multiple Isolated Singular Points:</strong> Linear system-il single equilibrium point matram; non-linear-il multiple stable/unstable points varum.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Linear system oru obedient student pole aanu &mdash; 1 hour padichaal 10 mark, 2 hours padichaal 20 mark. Pakshe Non-linear system oru mood ulla aalaanu &mdash; kurachu neram nannayi kekkum, sudden aayi jump cheyyum, thante thanne frequency-il aadi kondirikkum (Limit cycle)!</p>
"""
        },
        'ml': {
            'title': "നോൺ-ലീനിയർ സിസ്റ്റങ്ങളുടെ പ്രത്യേകതകളും സവിശേഷ പ്രതിഭാസങ്ങളും എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ നോൺ-ലീനിയർ പ്രത്യേകതകൾ",
                'eq': r"$$\text{Superposition തത്വം ബാധകമല്ല}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ലിമിറ്റ് സൈക്കിളുകൾ, ജമ്പ് റെസൊണൻസ്, സബ്-ഹാർമോണിക് ഓസിലേഷനുകൾ എന്നിവ നോൺ-ലീനിയർ സിസ്റ്റങ്ങളിൽ മാത്രം കാണപ്പെടുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സൂപ്പർപൊസിഷൻ പരാജയപ്പെടുന്നതും, ലിമിറ്റ് സൈക്കിളുകൾ, ജമ്പ് റെസൊണൻസ് തുടങ്ങിയ പ്രതിഭാസങ്ങളും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഇൻപുട്ടിന് ആനുപാതികമല്ലാതെ പെട്ടെന്ന് വലിയ മാറ്റങ്ങൾ കാണിക്കുന്ന സ്വഭാവമാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q16b: Describing Function of Ideal Relay & Relay with Dead-Zone
    # -------------------------------------------------------------------------
    'acs-q16b': {
        'manglish': {
            'title': "Ideal Relay-udeyum Relay with Dead-Zone-nteyum Describing Function derive cheyyuka.",
            'remember_this': {
                'title': "⚡ Relay Describing Functions",
                'eq': r"$$N(X)_{\text{Ideal}} = \frac{4M}{\pi X}, \quad N(X)_{\text{Dead-Zone}} = \frac{4M}{\pi X}\sqrt{1 - \left(\frac{D}{X}\right)^2} \quad (X \ge D)$$",
                'text': r"<strong>Ormavekkan:</strong> Non-linearity-lekku sinusoidal input $x(t) = X \sin(\omega t)$ koduthu fundamental harmonic output $Y_1$ Fourier series vechu kandupidikkunnathaanu Describing Function $N(X) = \frac{Y_1}{X}$."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Ideal Relay:</strong> Output square wave with height $\pm M$. Fourier fundamental coefficient $B_1 = \frac{4}{\pi}\int_0^{\pi/2} M \sin\theta d\theta = \frac{4M}{\pi}$. Hence $N(X) = \frac{B_1}{X} = \frac{4M}{\pi X}$. Phase angle $0^\circ$.</p>
    <p>2. <strong>Relay with Dead-Zone $D$:</strong> Relay switches only when $X \sin\theta \ge D \implies \theta_1 = \sin^{-1}(D/X)$. Fundamental $B_1 = \frac{4M}{\pi}\cos\theta_1 = \frac{4M}{\pi}\sqrt{1 - (D/X)^2}$. Hence $N(X) = \frac{4M}{\pi X}\sqrt{1 - (D/X)^2}$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru geyser thermostat nokku: Choodu kurayumbol ON aavunnu, choodu koodumbol OFF aavunnu. Ithu square wave tharum. Square wave-le fundamental sine wave matram filter cheythu edukkunna mathematical glass aanu Describing Function!</p>
"""
        },
        'ml': {
            'title': "ഐഡിയൽ റിലേയുടെയും ഡെഡ്-സോൺ റിലേയുടെയും ഡിസ്ക്രൈബിംഗ് ഫങ്ഷൻ കണ്ടുപിടിക്കുക",
            'remember_this': {
                'title': "⚡ റിലേ ഡിസ്ക്രൈബിംഗ് ഫങ്ഷൻ",
                'eq': r"$$N(X)_{\text{Ideal}} = \frac{4M}{\pi X}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഫൂറിയർ സീരീസ് ഉപയോഗിച്ച് ഔട്ട്പുട്ടിന്റെ ഫണ്ടമെന്റൽ ഹാർമോണിക് ഘടകം കണ്ടെത്തുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സ്ക്വയർ വേവ് ഔട്ട്പുട്ടിന്റെ ഫണ്ടമെന്റൽ കോഫിഷ്യന്റ് $B_1 = \frac{4M}{\pi}$ കണ്ടുപിടിച്ച് $N(X) = \frac{B_1}{X}$ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സ്ക്വയർ വേവ് ഔട്ട്പുട്ടിൽ നിന്നും പ്രധാനപ്പെട്ട സൈൻ വേവ് ഘടകത്തെ മാത്രം അരിച്ചെടുക്കുന്ന രീതിയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q17: Describing Function of Symmetrical Saturation
    # -------------------------------------------------------------------------
    'acs-q17': {
        'manglish': {
            'title': "Symmetrical Saturation non-linearity-ude Describing Function derive cheyyuka.",
            'remember_this': {
                'title': "⚡ Saturation Describing Function",
                'eq': r"$$N(X) = \frac{2k}{\pi}\left[\sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2}\right] \quad (X > S)$$",
                'text': r"<strong>Ormavekkan:</strong> Input amplitude $X \le S$ aaneel no saturation, $N(X) = k$ (pure linear gain). $X > S$ aavumbol amplitude koodumthorum gain $N(X)$ kuranju kuranju varum!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Saturation threshold angle $\theta_1 = \sin^{-1}(S/X)$.</p>
    <p>2. Output waveform is sinusoidal up to $\theta_1$, then clipped flat at $kS$ from $\theta_1$ to $\pi/2$.</p>
    <p>3. Fundamental Fourier integral: $B_1 = \frac{4}{\pi}\left[\int_0^{\theta_1} k X \sin^2\theta d\theta + \int_{\theta_1}^{\pi/2} k S \sin\theta d\theta\right]$.</p>
    <p>4. Evaluating integrals gives: $N(X) = \frac{B_1}{X} = \frac{2k}{\pi}[\theta_1 + \sin\theta_1 \cos\theta_1] = \frac{2k}{\pi}[\sin^{-1}(S/X) + \frac{S}{X}\sqrt{1 - (S/X)^2}]$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru amplifier-il volume kooduthal vachaal paattu pottitherichu clip aavunnathu pole aanu Saturation. Input cheriya value aayirikkumbol full paattum neat aayi varum ($N=k$). Pakshe input valuthavumbol peaks thalachethi flat aakkunnu, so effective gain kurayunnu!</p>
"""
        },
        'ml': {
            'title': "സിമെട്രിക്കൽ സാച്ചുറേഷൻ നോൺ-ലീനിയാരിറ്റിയുടെ ഡിസ്ക്രൈബിംഗ് ഫങ്ഷൻ സമവാക്യം കണ്ടെത്തുക",
            'remember_this': {
                'title': "⚡ സാച്ചുറേഷൻ സമവാക്യം",
                'eq': r"$$N(X) = \frac{2k}{\pi}\left[\sin^{-1}\left(\frac{S}{X}\right) + \frac{S}{X}\sqrt{1 - \left(\frac{S}{X}\right)^2}\right]$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻപുട്ട് പരിധി വിടുമ്പോൾ ഔട്ട്പുട്ട് ഫ്ലാറ്റായി കട്ട് ചെയ്യപ്പെടുന്നു. ആംപ്ലിറ്റ്യൂഡ് കൂടുന്തോറും ഗെയിൻ കുറയുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ആംഗിൾ $\theta_1$ വരെ ലീനിയറായും ബാക്കി ഭാഗം കോൺസ്റ്റന്റായും ഇന്റഗ്രേറ്റ് ചെയ്ത് സമവാക്യം രൂപീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഓഡിയോ ആംപ്ലിഫയറിൽ ശബ്ദം വല്ലാതെ കൂട്ടുമ്പോൾ പാട്ടിന്റെ അഗ്രങ്ങൾ പരന്ന് വികൃതമാകുന്ന പ്രതിഭാസമാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q17b: Describing Function of Dead-Zone Non-Linearity
    # -------------------------------------------------------------------------
    'acs-q17b': {
        'manglish': {
            'title': "Dead-Zone Non-Linearity-ude Describing Function engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Dead-Zone Describing Function",
                'eq': r"$$N(X) = k - \frac{2k}{\pi}\left[\sin^{-1}\left(\frac{D}{X}\right) + \frac{D}{X}\sqrt{1 - \left(\frac{D}{X}\right)^2}\right] \quad (X > D)$$",
                'text': r"<strong>Ormavekkan:</strong> Input amplitude $X \le D$ aaneel dead-zone kaaranam output zero aayirikkum ($N(X) = 0$). $X > D$ aavumbol mathrame signal kadannupovoo!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Angle $\theta_1 = \sin^{-1}(D/X)$. Between $0$ and $\theta_1$, output is $0$.</p>
    <p>2. For $\theta_1 \le \theta \le \pi/2$, output is $k(X \sin\theta - D)$.</p>
    <p>3. Fundamental integral: $B_1 = \frac{4}{\pi}\int_{\theta_1}^{\pi/2} k(X \sin\theta - D)\sin\theta d\theta$.</p>
    <p>4. Result gives $N(X) = \frac{B_1}{X} = k - \frac{2k}{\pi}[\sin^{-1}(D/X) + \frac{D}{X}\sqrt{1 - (D/X)^2}]$.</p>
</div>
""",
            'understand_simply': r"""
<p>Car-inte steering wheel alpam thirichalum tyre thiriyatha cheriya loose play undallo &mdash; athanu Dead-Zone! Cheriya movements full ignore cheyyum. Pakshe steering nannayi thirichaal ($X > D$) matrame car thiriyoo!</p>
"""
        },
        'ml': {
            'title': "ഡെഡ്-സോൺ നോൺ-ലീനിയാരിറ്റിയുടെ ഡിസ്ക്രൈബിംഗ് ഫങ്ഷൻ സമവാക്യം കണ്ടെത്തുക",
            'remember_this': {
                'title': "⚡ ഡെഡ്-സോൺ സമവാക്യം",
                'eq': r"$$N(X) = k\left[1 - \frac{2}{\pi}\left(\sin^{-1}\frac{D}{X} + \frac{D}{X}\sqrt{1 - \frac{D^2}{X^2}}\right)\right]$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻപുട്ട് ഡെഡ്-സോണിനേക്കാൾ ($D$) ചെറുതാണെങ്കിൽ ഔട്ട്പുട്ട് പൂജ്യമായിരിക്കും."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡെഡ്-സോൺ കഴിഞ്ഞുള്ള ഭാഗം മാത്രം ഇന്റഗ്രേറ്റ് ചെയ്ത് ഫങ്ഷൻ കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സ്റ്റിയറിംഗിന്റെ ലൂസ് പ്ലേ പോലെ ചെറിയ അനക്കങ്ങൾ സിസ്റ്റം പരിഗണിക്കാത്ത അവസ്ഥയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q18: Limit Cycle Stability via Describing Function
    # -------------------------------------------------------------------------
    'acs-q18': {
        'manglish': {
            'title': "Limit Cycle-nte existence-um stability-um Describing Function vechu engane kandupidikkam?",
            'remember_this': {
                'title': "⚡ Limit Cycle Criterion & Stability",
                'eq': r"$$G(j\omega) = -\frac{1}{N(X)} \iff 1 + N(X)G(j\omega) = 0$$",
                'text': r"<strong>Ormavekkan:</strong> Nyquist plot of $G(j\omega)$-um $-1/N(X)$ curve-um intersect cheyyunna point-il limit cycle undaakum! Stable limit cycle aavan: Amplitude $X$ koodumbol operating point $-1/N(X)$ curve vazhi stable region-ilekk (outside $G(j\omega)$ encirclement) pokanam."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Characteristic equation: $1 + N(X)G(j\omega) = 0 \implies G(j\omega) = -\frac{1}{N(X)}$.</p>
    <p>2. Polar plot-il $G(j\omega)$ varakkuka. Same graph-il $-\frac{1}{N(X)}$ locus-um varakkuka (with arrow pointing in direction of increasing $X$).</p>
    <p>3. Intersection point gives limit cycle frequency $\omega_0$ and amplitude $X_0$.</p>
    <p>4. <strong>Stability rule:</strong> Point $P$-il ninnu $X$ kuranjaal point unstable region-il (inside enclosure) varunnu, so oscillation valuthavunnu. $X$ koodiyaal stable region-il varunnu, so oscillation kurayunnu $\implies$ <strong>Stable Limit Cycle</strong>!</p>
</div>
""",
            'understand_simply': r"""
<p>Limit cycle ennathu system-te oru permanent self-oscillation aanu &mdash; chila fan-ukal speed koodiyaal oru steady rhythm-il sound undakki karangunnathu pole! Describing function ee sound-inte frequency-um amplitude-um graph intersect cheythu accurate aayi kandupidichu tharum.</p>
"""
        },
        'ml': {
            'title': "ഡിസ്ക്രൈബിംഗ് ഫങ്ഷൻ ഉപയോഗിച്ച് ലിമിറ്റ് സൈക്കിളുകൾ എങ്ങനെ കണ്ടെത്താം?",
            'remember_this': {
                'title': "⚡ ലിമിറ്റ് സൈക്കിൾ നിബന്ധന",
                'eq': r"$$G(j\omega) = -\frac{1}{N(X)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> $G(j\omega)$ ഗ്രാഫും $-1/N(X)$ ഗ്രാഫും കൂട്ടിമുട്ടുന്ന ബിന്ദുവിൽ ലിമിറ്റ് സൈക്കിൾ രൂപപ്പെടുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>രണ്ട് ഗ്രാഫുകളും ഒരേ പ്ലോട്ടിൽ വരച്ച് കൂട്ടിമുട്ടുന്ന പോയിന്റിലെ ആംപ്ലിറ്റ്യൂഡും ഫ്രീക്വൻസിയും സ്റ്റെബിലിറ്റിയും കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ബാഹ്യ പ്രേരണകളില്ലാതെ സിസ്റ്റം സ്ഥിരമായി ഒരു നിശ്ചിത ആവൃത്തിയിൽ പ്രകമ്പനം കൊള്ളുന്ന അവസ്ഥയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q19: Phase Plane Concepts
    # -------------------------------------------------------------------------
    'acs-q19': {
        'manglish': {
            'title': "Phase Plane, Phase Trajectories, and Phase Portrait concepts explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Phase Plane Definitions",
                'eq': r"$$\text{Slope: } \frac{dx_2}{dx_1} = \frac{f_2(x_1, x_2)}{f_1(x_1, x_2)}, \quad x_1 = y, \; x_2 = \dot{y}$$",
                'text': r"<strong>Ormavekkan:</strong> Phase Plane = 2-dimensional state plane ($x_1$ vs $x_2$). Phase Trajectory = Time progress cheyyumbol state point varakkunna curve. Phase Portrait = Ella initial conditions-teyum trajectories koodiya family of curves."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>Phase Plane:</strong> Second-order systems-ine graphically study cheyyan ulla 2D plane ($x_1$ on x-axis, $x_2 = \dot{x}_1$ on y-axis).</li>
        <li><strong>Phase Trajectory:</strong> Oru particular initial condition $(x_1(0), x_2(0))$-il ninnu system move cheyyumbol state point trace cheyyunna path. Slope $S = \frac{dx_2}{dx_1} = \frac{\dot{x}_2}{\dot{x}_1}$.</li>
        <li><strong>Phase Portrait:</strong> Pala initial points-il ninnulla ella trajectories-um koodiya complete visual map. System stable aano unstable aano ennu ഒറ്റ glance-il manasilakkam!</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Oru roller-coaster-te map nokkunnathu pole aanu Phase Portrait: X-axis-il position-um Y-axis-il speed-um varakkunnu. Cart engottu pokum, evide stop aavum ennu aa graph-ile curves nokkiyaal direct aayi parayan pattum!</p>
"""
        },
        'ml': {
            'title': "ഫേസ് പ്ലെയിൻ, ഫേസ് ട്രാജക്ടറി, ഫേസ് പോർട്രെയിറ്റ് എന്നിവ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഫേസ് പ്ലെയിൻ സമവാക്യം",
                'eq': r"$$\frac{dx_2}{dx_1} = \frac{\dot{x}_2}{\dot{x}_1}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> രണ്ടാമത്തെ ഓർഡർ സിസ്റ്റങ്ങളെ ഗ്രാഫിക്കലായി പഠിക്കാൻ ഉപയോഗിക്കുന്ന 2D പ്ലെയിനാണ് ഫേസ് പ്ലെയിൻ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>മൂന്ന് നിർവ്വചനങ്ങളും അവയുടെ ഗ്രാഫിക്കൽ പ്രാധാന്യവും വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>റോലർ കോസ്റ്ററിന്റെ വേഗതയും സ്ഥാനവും അടയാളപ്പെടുത്തിയ ട്രാഫിക് മാപ്പ് പോലെയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q20: Sign Definiteness & Sylvester's Criterion
    # -------------------------------------------------------------------------
    'acs-q20': {
        'manglish': {
            'title': "Scalar Function-te Sign Definiteness-um Sylvester's Criterion-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Sylvester's Criterion",
                'eq': r"$$V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x} > 0 \iff \Delta_1 > 0, \;\; \Delta_2 > 0, \;\; \dots, \;\; \Delta_n > 0$$",
                'text': r"<strong>Ormavekkan:</strong> Positive Definite: $V(\mathbf{0}) = 0$ and $V(\mathbf{x}) > 0 \;\; \forall \mathbf{x} \ne \mathbf{0}$. Sylvester test: Matrix $P$-yude all principal leading minors strictly positive aayirikkannam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Sign Classifications:</strong></p>
    <ul>
        <li><strong>Positive Definite:</strong> $V(\mathbf{x}) > 0$ for all $\mathbf{x} \ne \mathbf{0}$, and $V(\mathbf{0}) = 0$. (Bowl shape).</li>
        <li><strong>Positive Semi-Definite:</strong> $V(\mathbf{x}) \ge 0$. (Can be zero even when $\mathbf{x} \ne \mathbf{0}$).</li>
        <li><strong>Negative Definite:</strong> $V(\mathbf{x}) < 0$ for all $\mathbf{x} \ne \mathbf{0}$.</li>
        <li><strong>Indefinite:</strong> Takes both positive and negative values.</li>
    </ul>
    <p><strong>2. Sylvester's Criterion:</strong> For $P = \begin{bmatrix} p_{11} & p_{12} \\ p_{21} & p_{22} \end{bmatrix}$, check $\Delta_1 = p_{11} > 0$ and $\Delta_2 = \det(P) = p_{11}p_{22} - p_{12}^2 > 0$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru chaya kinnam (tea bowl) alochikku: Kinnathinte nadukku matram height zero aanu, baaki ella sthalathum height positive aanu &mdash; ithanu Positive Definite function! Athil oru marble ittaal eppozhum nadukkilekku thanne urundu veezhum (Stability)!</p>
"""
        },
        'ml': {
            'title': "സൈൻ ഡെഫിനിറ്റ്നസും സിൽവെസ്റ്റേഴ്സ് മാനദണ്ഡവും (Sylvester's Criterion) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ സിൽവെസ്റ്റേഴ്സ് ടെസ്റ്റ്",
                'eq': r"$$\Delta_1 > 0, \quad \Delta_2 > 0, \quad \dots, \quad \Delta_n > 0 \implies \text{Positive Definite}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മാട്രിക്സ് $P$-യുടെ എല്ലാ ലീഡിംഗ് പ്രിൻസിപ്പൽ മൈനറുകളും പോസിറ്റീവ് ആണെങ്കിൽ ഫങ്ഷൻ പോസിറ്റീവ് ഡെഫിനിറ്റ് ആണ്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>പോസിറ്റീവ് ഡെഫിനിറ്റ്, നെഗറ്റീവ് ഡെഫിനിറ്റ് വ്യവസ്ഥകളും മൈനർ ഡിറ്റർമിനന്റുകളും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു ചായക്കോപ്പയുടെ അടിത്തട്ടിൽ മാത്രമേ ഉയരം പൂജ്യമാകൂ, ബാക്കി എല്ലായിടത്തും ഉയരം പോസിറ്റീവാണ് &mdash; ഇതാണ് പോസിറ്റീവ് ഡെഫിനിറ്റ് എനർജി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q20b: Generation of Lyapunov Functions
    # -------------------------------------------------------------------------
    'acs-q20b': {
        'manglish': {
            'title': "Lyapunov function generate cheyyunna methods (Krasovskii's & Variable Gradient) explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Krasovskii's Theorem Formula",
                'eq': r"$$V(\mathbf{x}) = \mathbf{f}^T(\mathbf{x}) P \mathbf{f}(\mathbf{x}), \quad J(\mathbf{x}) = \frac{\partial \mathbf{f}}{\partial \mathbf{x}}, \quad \hat{F} = J^T P + P J < 0$$",
                'text': r"<strong>Ormavekkan:</strong> Non-linear systems-inu Lyapunov function kandupidikkan trial-and-error venda: Krasovskii method Jacobian matrix $J(\mathbf{x})$ use cheyyunnu; Variable gradient method $\nabla V$ assume cheythu line integral edukkunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Krasovskii's Method:</strong> For $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$, form Jacobian $J = \frac{\partial f_i}{\partial x_j}$. Define matrix $\hat{F} = J + J^T$. If $\hat{F}$ is negative definite, then $V(\mathbf{x}) = \mathbf{f}^T \mathbf{f}$ is a valid Lyapunov function and system is asymptotically stable!</p>
    <p><strong>2. Variable Gradient Method:</strong> Assume gradient vector $\nabla V = [g_1(\mathbf{x}), g_2(\mathbf{x})]^T$. Apply curl condition $\frac{\partial g_1}{\partial x_2} = \frac{\partial g_2}{\partial x_1}$. Compute line integral $V(\mathbf{x}) = \int_0^{\mathbf{x}} \nabla V \cdot d\mathbf{x}$. Ensure $\dot{V} = \nabla V^T \mathbf{f} \le 0$.</p>
</div>
""",
            'understand_simply': r"""
<p>Kunnin mukalil ninnu thazhottu vellam ozhukunna path kandupidikkunnathu pole aanu ithu: Krasovskii method slope (Jacobian) check cheythu thazhottanu pokunnath ennu urappakkunnu. Variable gradient method oru compass vechu step-by-step aayi route integrate cheyyunnu!</p>
"""
        },
        'ml': {
            'title': "ലയപുനോവ് ഫങ്ഷനുകൾ നിർമ്മിക്കുന്ന രീതികൾ (Krasovskii's & Variable Gradient) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ക്രസോവ്സ്കി സമവാക്യം",
                'eq': r"$$\hat{F} = J + J^T < 0 \implies \text{Asymptotically Stable}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ജക്കോബിയൻ മാട്രിക്സ് ഉപയോഗിച്ച് നോൺ-ലീനിയർ സിസ്റ്റങ്ങൾക്ക് കൃത്യമായ എനർജി ഫങ്ഷൻ കണ്ടെത്താം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ജക്കോബിയൻ മാട്രിക്സും വേരിയബിൾ ഗ്രേഡിയന്റ് ലൈൻ ഇന്റഗ്രലും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>കുന്നിൻ മുകളിൽ നിന്നും താഴേക്ക് പോകുന്ന ചെരിവ് കണക്കുകൂട്ടി സിസ്റ്റം സ്റ്റേബിളാണോ എന്ന് ഉറപ്പുവരുത്തുന്ന വിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q21: Singular Points Analysis
    # -------------------------------------------------------------------------
    'acs-q21': {
        'manglish': {
            'title': "Singular Points-nte Classification explain cheyyuka (Node, Saddle, Focus, Center).",
            'remember_this': {
                'title': "⚡ Singular Points by Eigenvalues",
                'eq': r"$$\text{Node: Real, same sign} \quad \text{Saddle: Real, opposite signs} \quad \text{Focus: Complex conjugates} \quad \text{Center: Purely imaginary}$$",
                'text': r"<strong>Ormavekkan:</strong> $\dot{x}_1 = 0$ and $\dot{x}_2 = 0$ aavunna equilibrium points aanu singular points. Eigenvalues $\lambda_1, \lambda_2$-nte nature nokki nature direct aayi theerumanikkam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Singular Point</th><th>Eigenvalues $\lambda_1, \lambda_2$</th><th>Stability</th></tr></thead>
        <tbody>
            <tr><td><strong>Stable Node</strong></td><td>Real, distinct, both negative ($\lambda_2 < \lambda_1 < 0$)</td><td>Asymptotically Stable</td></tr>
            <tr><td><strong>Unstable Node</strong></td><td>Real, distinct, both positive ($\lambda_2 > \lambda_1 > 0$)</td><td>Unstable</td></tr>
            <tr><td><strong>Saddle Point</strong></td><td>Real, opposite signs ($\lambda_1 < 0 < \lambda_2$)</td><td>Always Unstable</td></tr>
            <tr><td><strong>Stable Focus</strong></td><td>Complex conjugates with negative real part ($\sigma \pm j\omega, \sigma < 0$)</td><td>Stable (spirals inward)</td></tr>
            <tr><td><strong>Unstable Focus</strong></td><td>Complex conjugates with positive real part ($\sigma \pm j\omega, \sigma > 0$)</td><td>Unstable (spirals outward)</td></tr>
            <tr><td><strong>Center (Vortex)</strong></td><td>Purely imaginary ($\pm j\omega, \sigma = 0$)</td><td>Marginally Stable (concentric circles)</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Different types of water whirlpools alochikku:</p>
<ul>
    <li><strong>Stable Node:</strong> Vellam nerae sink hole-ilottu nere ozhuki pokunnu.</li>
    <li><strong>Stable Focus:</strong> Vellam karangi karangi spiraling aayi thazhottu pokunnu.</li>
    <li><strong>Center:</strong> Vellam arikilottu pokathe round aayi mathram karangikondirikkunnu (planets orbit pole).</li>
    <li><strong>Saddle:</strong> Oru horse saddle pole &mdash; oru side-il ninnu varunnavan nere thazhottu therichu pokunnu!</li>
</ul>
"""
        },
        'ml': {
            'title': "സിംഗുലർ പോയിന്റുകളുടെ വർഗ്ഗീകരണം വിശദീകരിക്കുക (Node, Saddle, Focus, Center)",
            'remember_this': {
                'title': "⚡ പോയിന്റ് വർഗ്ഗീകരണം",
                'eq': r"$$\text{Node (Real)}, \quad \text{Focus (Complex)}, \quad \text{Center (Imaginary)}, \quad \text{Saddle (Opposite)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഐഗൻവാല്യൂകളുടെ സ്വഭാവം നോക്കി സിംഗുലർ പോയിന്റുകളുടെ ടൈപ്പും സ്റ്റെബിലിറ്റിയും കണ്ടെത്തുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ടേബിൾ രൂപത്തിൽ ഐഗൻവാല്യൂസും അവ നൽകുന്ന പോയിന്റുകളും വരച്ച് വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വെള്ളത്തിന്റെ ചുഴി പോലെയാണ് &mdash; അകത്തേക്ക് കറങ്ങി വീഴുന്നത് ഫോക്കസും, ചുറ്റും കറങ്ങുന്നത് സെന്ററുമാണ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # acs-q22: Lyapunov Direct Method & Matrix Equation A^T P + P A = -Q
    # -------------------------------------------------------------------------
    'acs-q22': {
        'manglish': {
            'title': "Lyapunov Direct Method-um Matrix Equation $A^T P + P A = -Q$ derivation-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Lyapunov Matrix Equation",
                'eq': r"$$A^T P + P A = -Q, \quad V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x}, \quad \dot{V}(\mathbf{x}) = -\mathbf{x}^T Q \mathbf{x}$$",
                'text': r"<strong>Ormavekkan:</strong> Oru linear system $\dot{\mathbf{x}} = A\mathbf{x}$ asymptotically stable aakanamenkil: Any arbitrary positive definite matrix $Q$ (eg: $Q = I$) eduthaal, $A^T P + PA = -Q$ solve cheyyumbol kittunna matrix $P$-yum strictly positive definite aayirikkannam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Step-by-step Derivation:</strong></p>
    <ol>
        <li>Choose quadratic candidate energy: $V(\mathbf{x}) = \mathbf{x}^T P \mathbf{x}$, with $P = P^T > 0$.</li>
        <li>Time derivative: $\dot{V}(\mathbf{x}) = \dot{\mathbf{x}}^T P \mathbf{x} + \mathbf{x}^T P \dot{\mathbf{x}}$.</li>
        <li>Substitute $\dot{\mathbf{x}} = A\mathbf{x}$: $\dot{V} = (A\mathbf{x})^T P \mathbf{x} + \mathbf{x}^T P (A\mathbf{x}) = \mathbf{x}^T A^T P \mathbf{x} + \mathbf{x}^T P A \mathbf{x} = \mathbf{x}^T (A^T P + P A) \mathbf{x}$.</li>
        <li>For asymptotic stability, we require $\dot{V}(\mathbf{x}) = -\mathbf{x}^T Q \mathbf{x} < 0$, where $Q > 0$.</li>
        <li>Equating both terms gives the celebrated Lyapunov equation: $A^T P + P A = -Q$.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru dynamic system-te total stored energy aanu $V(x)$. System stable aavan: Energy eppozhum positive aayirikkannam ($P > 0$), pinne samayam pokumthorum energy kuranju kuranju varanam ($\dot{V} = -Q < 0$, dissipation). Friction pole energy consume cheythu system rest-ilekk ethum!</p>
"""
        },
        'ml': {
            'title': "ലയപുനോവിന്റെ ഡയറക്ട് രീതിയും $A^T P + P A = -Q$ സമവാക്യവും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ലയപുനോവ് മാട്രിക്സ് സമവാക്യം",
                'eq': r"$$A^T P + P A = -Q$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പോസിറ്റീവ് ഡെഫിനിറ്റ് ആയ $Q$-ന് ലഭിക്കുന്ന $P$ പോസിറ്റീവ് ഡെഫിനിറ്റ് ആണെങ്കിൽ സിസ്റ്റം അസിംപ്റ്റോട്ടിക്കലി സ്റ്റേബിൾ ആണ്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>എനർജി ഫങ്ഷൻ $V = \mathbf{x}^T P \mathbf{x}$-ന്റെ ഡെറിവേറ്റീവ് എടുത്ത് $A^T P + P A = -Q$ തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സിസ്റ്റത്തിലെ ഊർജ്ജം എപ്പോഴും പോസിറ്റീവായിരിക്കുകയും, സമയം കഴിയുന്തോറും കുറഞ്ഞു കുറഞ്ഞു വരികയും ചെയ്താൽ സിസ്റ്റം സ്റ്റേബിളാകും!</p>
"""
        }
    }
}
