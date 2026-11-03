# scratch/drive_local_bank.py
# Complete Manglish & Malayalam (മലയാളം) Local Explanations for all 27 Electric Drives questions (EET413).
# Written in friendly Kerala B.Tech campus lecturer & study group tone.

DRIVE_LOCAL_ANSWERS = {
    # -------------------------------------------------------------------------
    # drive-q1: Elements and Block Diagram of Modern Electric Drive
    # -------------------------------------------------------------------------
    'drive-q1': {
        'manglish': {
            'title': "Modern Electric Drive system-il enthokke main blocks aanu ulla?",
            'remember_this': {
                'title': "⚡ 5 Essential Blocks",
                'eq': r"$$\text{Power Source} \to \text{Power Modulator} \to \text{Motor} \to \text{Load} \quad [\text{Sensing} \to \text{Control}]$$",
                'text': r"<strong>Ormavekkan:</strong> 5 blocks: Source, Modulator (Converter/Inverter), Motor, Load, and Control Unit. Feedback loop vechanu speed-um torque-um accurate aayi maintain cheyyunnath."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>Power Source:</strong> Electrical power tharunnu (1-phase/3-phase AC or DC battery).</li>
        <li><strong>Power Modulator:</strong> Fixed AC/DC-ye motor-nu aavashyamaaya variable voltage/frequency aakki maattunnu (Inverters, Choppers).</li>
        <li><strong>Electric Motor:</strong> Electrical energy-ye mechanical motion aakki maattunna prime mover.</li>
        <li><strong>Mechanical Load:</strong> Fans, Pumps, Conveyors, Lifts pole karakkenda industrial machine.</li>
        <li><strong>Control Unit & Sensors:</strong> Speed sensor-il ninnu feedback eduthu firing angle / PWM duty cycle adjust cheyyunnu.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru Electric Car (EV) alochichu nokku: Battery aanu Power Source, Inverter aanu Power Modulator, Motor chakrathe thirikkunnu, Road-um car-um Load aanu, Accelerator pedal-um computer-um Control Unit aanu!</p>
"""
        },
        'ml': {
            'title': "ഒരു ഇലക്ട്രിക് ഡ്രൈവ് സിസ്റ്റത്തിലെ പ്രധാന ഭാഗങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ പ്രധാന 5 ഘടകങ്ങൾ",
                'eq': r"$$\text{Power Source} \to \text{Power Modulator} \to \text{Motor} \to \text{Load}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> സോഴ്സ്, പവർ മോഡുലേറ്റർ (കൺവെർട്ടർ), മോട്ടോർ, ലോഡ്, കൺട്രോൾ യൂണിറ്റ് എന്നിവയാണ് 5 പ്രധാന ഭാഗങ്ങൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>5 പ്രധാന ബ്ലോക്കുകളും അവയുടെ പ്രവർത്തനങ്ങളും ഫീഡ്‌ബാക്ക് ലൂപ്പും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു ഇലക്ട്രിക് കാർ പോലെയാണ്: ബാറ്ററി (സോഴ്സ്), ഇൻവെർട്ടർ (മോഡുലേറ്റർ), മോട്ടോർ, റോഡ് (ലോഡ്), ആക്സിലറേറ്റർ (കൺട്രോൾ യൂണിറ്റ്)!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q2: Advantages of Electric Drives
    # -------------------------------------------------------------------------
    'drive-q2': {
        'manglish': {
            'title': "Mechanical/Diesel drives-ine kaal Electric Drives-inte main advantages enthokke aanu?",
            'remember_this': {
                'title': "⚡ Key Advantages Summary",
                'eq': r"$$\eta_{\text{electric}} \approx 90\text{--}95\% \gg \eta_{\text{diesel}} \approx 30\text{--}40\%$$",
                'text': r"<strong>Ormavekkan:</strong> High efficiency, four-quadrant operation, fast dynamic response, regenerative braking (energy thirichu kittunnu), zero local emissions, wide speed control range."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Wide speed and torque control:</strong> Zero rpm muthal maximum rated speed vare smooth aayi control cheyyam.</li>
        <li><strong>2. Four-Quadrant capability:</strong> Forward/reverse motoring and regenerative braking seamlessly cheyyam.</li>
        <li><strong>3. Energy Conservation:</strong> Braking cheyyumbol mechanical energy-ye thirichu electrical energy aakki grid-ilottu feed cheyyam (Regenerative braking).</li>
        <li><strong>4. Clean & Silent:</strong> Smoke, exhaust gas, or high noise pollution illa.</li>
        <li><strong>5. Compact & High Power-to-weight ratio:</strong> Diesel engine pole heavy gearbox venda.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Diesel auto-yum Electric auto-yum compare cheythu nokku: Diesel auto-yil gearbox maarano, vibration, sound, puka! Pakshe Electric auto smooth accelerator, silent running, brake pidikkumbol battery thaniye charge aavunnu!</p>
"""
        },
        'ml': {
            'title': "ഇലക്ട്രിക് ഡ്രൈവുകളുടെ പ്രധാന ഗുണങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ പ്രധാന മേന്മകൾ",
                'eq': r"$$\text{High Efficiency, Regenerative Braking, Zero Pollution}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഉയർന്ന കാര്യക്ഷമത, ശബ്ദ-പുക മലിനീകരണമില്ലായ്മ, റീജനറേറ്റീവ് ബ്രേക്കിംഗ് വഴി ഊർജ്ജ ലാഭം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡീസൽ/സ്റ്റീം എൻജിനുകളെ അപേക്ഷിച്ച് ഉയർന്ന കാര്യക്ഷമതയും കൃത്യമായ വേഗത നിയന്ത്രണവും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഡീസൽ വണ്ടികളിലെ പുകയും ശബ്ദവും ഗിയർ മാറ്റുന്ന ബുദ്ധിമുട്ടുമില്ലാതെ അതിവേഗം നിയന്ത്രിക്കാം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q3: Classification and Nature of Industrial Load Torques
    # -------------------------------------------------------------------------
    'drive-q3': {
        'manglish': {
            'title': "Industrial Load Torques engane classify cheyyam? (Active vs Passive)",
            'remember_this': {
                'title': "⚡ Core Comparison Rule",
                'eq': r"$$T_L(\text{Active}) \ne f(\operatorname{sgn} \omega), \quad T_L(\text{Passive}) \propto \operatorname{sgn}(\omega)$$",
                'text': r"<strong>Main Difference:</strong> Active torque rotation direction nokkilla, eppozhum constant direction (eg: Hoist Gravity). Passive torque motion-te ethire matrame varoo (eg: Friction, Windage)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Active Load Torques:</strong> Gravitational potential energy karanam undakunnu. Motor off aaneel polum load thaniye movement create cheyyum! Direction eppozhum downward/same direction.</p>
    <p><strong>2. Passive Load Torques:</strong> Friction, windage, and cutting action karanam undakunnu. Motor motion-te nere opposite direction-il matrame act cheyyoo ($T_L \propto -\operatorname{sgn}(\omega)$).</p>
</div>
""",
            'understand_simply': r"""
<p>Oru kayattam ulla road-il oru vandi thallunna karyam alochikku: Gravity eppozhum thazhottu valikkunnu (Active Load). Tyre-te friction vandi engottaano pokunnath athinte nere ethire varunnu (Passive Load)!</p>
"""
        },
        'ml': {
            'title': "ലോഡ് ടോർക്കുകളെ എങ്ങനെ തരംതിരിക്കാം? (Active vs Passive Torques)",
            'remember_this': {
                'title': "⚡ പ്രധാന വ്യത്യാസം",
                'eq': r"$$T_L(\text{Active}) = \text{Constant direction}, \quad T_L(\text{Passive}) \text{ opposes } \omega$$",
                'text': r"<strong>പ്രധാന പോയിന്റ്:</strong> Active torque മോട്ടോറിന്റെ ദിശയെ ആശ്രയിക്കുന്നില്ല (ഗ്രാവിറ്റി). എന്നാൽ Passive torque മോട്ടോറിന്റെ ചലനത്തെ എതിർത്തു മാത്രമേ നിൽക്കൂ (ഘർഷണം)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ആക്ടീവ്, പാസീവ് ടോർക്കുകളുടെ സവിശേഷതകളും ഉദാഹരണങ്ങളും ടേബിളിൽ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>കയറ്റത്തിൽ വണ്ടിയെ എപ്പോഴും താഴോട്ട് വലിക്കുന്ന ഗ്രാവിറ്റി ആക്ടീവ് ലോഡും, ടയറിന്റെ ഘർഷണം പാസീവ് ലോഡുമാണ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q3b: Critical Speed and Torsional Resonance
    # -------------------------------------------------------------------------
    'drive-q3b': {
        'manglish': {
            'title': "Critical Speed-um Torsional Resonance-um electric drives-il enthinaanu study cheyyunnath?",
            'remember_this': {
                'title': "⚡ Resonance Condition",
                'eq': r"$$\omega_{\text{operating}} = \omega_n = \sqrt{\frac{K_{\text{shaft}}}{J_{\text{eq}}}} \implies \text{Severe Mechanical Vibrations & Shaft Breakage}$$",
                'text': r"<strong>Ormavekkan:</strong> Motor speed shaft-inte natural frequency $\omega_n$-umaayi match aavumbol violent resonance undaayi shaft potti pokum. Acceleration time-il ee critical speed zone vegam pass cheyyanam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Critical Speed:</strong> Shaft rotational frequency matching natural frequency of transverse/torsional vibration.</p>
    <p>2. <strong>Consequences:</strong> Shaft deflection rapidly builds up, bearings destroy aavunnu, catastrophic coupling failure.</p>
    <p>3. <strong>Mitigation:</strong> V/f controller-il 'Skip Frequency' band set cheyyuka, flexible couplings use cheyyuka, acceleration fast aakkuka.</p>
</div>
""",
            'understand_simply': r"""
<p>Washing machine spin cycle-il oru particular speed ethumbol padapada ennu sound undakki violently aadunnathu kandittille? Athu critical speed aanu! Aa speed kazhinjaal pinne smooth aavum. Electric motor-il ee speed-il continuous run cheythaal shaft potti thundu thundaavum!</p>
"""
        },
        'ml': {
            'title': "ക്രിട്ടിക്കൽ സ്പീഡും ടോർഷണൽ റെസൊണൻസും ഡ്രൈവുകളിൽ വരുത്തുന്ന പ്രശ്നങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ റെസൊണൻസ് നിബന്ധന",
                'eq': r"$$\omega = \omega_n \implies \text{വൻതോതിലുള്ള പ്രകമ്പനം (Shaft Resonance)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മോട്ടോർ വേഗത ഷാഫ്റ്റിന്റെ സ്വാഭാവിക ആവൃത്തിക്ക് തുല്യമാകുമ്പോൾ വലിയ പ്രകമ്പനമുണ്ടായി ഷാഫ്റ്റ് ഒടിയാൻ സാധ്യതയുണ്ട്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ക്രിട്ടിക്കൽ സ്പീഡിന്റെ കാരണങ്ങളും, അത് ഒഴിവാക്കാനുള്ള സ്കിപ്പ് ഫ്രീക്വൻസി രീതികളും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വാഷിംഗ് മെഷീൻ ഒരു പ്രത്യേക സ്പീഡിൽ കറങ്ങുമ്പോൾ ആടിയുലയുന്നത് പോലെ ഷാഫ്റ്റുകൾ തകരാറിലാകുന്ന പ്രതിഭാസമാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q4: Fundamental Dynamic Torque Equation
    # -------------------------------------------------------------------------
    'drive-q4': {
        'manglish': {
            'title': "Fundamental Dynamic Torque Equation $J \\frac{d\\omega_m}{dt} = T - T_L$ engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Fundamental Drive Torque Equation",
                'eq': r"$$J \frac{d\omega_m}{dt} = T - T_L \quad \implies \quad T = T_L + J \frac{d\omega_m}{dt} + B\omega_m$$",
                'text': r"<strong>Ormavekkan:</strong> Motor develop cheyyunna torque $T$ load torque $T_L$-um inertia dynamic torque $J \frac{d\omega_m}{dt}$-um friction loss $B\omega_m$-um balance cheyyannam. Acceleration $\frac{d\omega}{dt} > 0$ aavan $T > T_L$ aayirikkannam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Derivation Guide</span></div>
    <p>1. <strong>Energy Balance:</strong> Electrical input mechanical power $P_{\text{net}} = T\omega_m - T_L\omega_m$.</p>
    <p>2. Rotational kinetic energy $E_k = \frac{1}{2}J\omega_m^2$.</p>
    <p>3. Rate of change of kinetic energy: $\frac{dE_k}{dt} = \frac{d}{dt}\left(\frac{1}{2}J\omega_m^2\right) = J\omega_m \frac{d\omega_m}{dt}$.</p>
    <p>4. Equating net power to energy change: $(T - T_L)\omega_m = J\omega_m \frac{d\omega_m}{dt} \implies T - T_L = J\frac{d\omega_m}{dt}$.</p>
    <p>Cases: 1) $T > T_L \implies$ Acceleration; 2) $T < T_L \implies$ Deceleration; 3) $T = T_L \implies$ Steady-state constant speed.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru bike accelerator kodukkumbol: Engine undakkunna torque $T$. Road-le kayattavum kaattum $T_L$. Engine torque road load-inekaal kooduthal aanenkil ($T > T_L$), vandi speed koodi koodi accelerate cheyyum ($J \frac{d\omega}{dt}$). Randum equal aayirikkumbol constant speed-il smooth aayi pokum!</p>
"""
        },
        'ml': {
            'title': "ഡൈനാമിക് ടോർക്ക് അടിസ്ഥാന സമവാക്യം ($J \\frac{d\\omega_m}{dt} = T - T_L$) എങ്ങനെ തെളിയിക്കാം?",
            'remember_this': {
                'title': "⚡ അടിസ്ഥാന ഡ്രൈവ് സമവാക്യം",
                'eq': r"$$J \frac{d\omega_m}{dt} = T - T_L$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മോട്ടോർ ടോർക്ക് ($T$) ലോഡ് ടോർക്കിനേക്കാൾ ($T_L$) കൂടുതലാണെങ്കിൽ വാഹനം ആക്സിലറേറ്റ് ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ഡെറിവേഷൻ</span></div>
    <p>കൈനറ്റിക് എനർജിയുടെ ഡെറിവേറ്റീവ് എടുത്ത് പവർ ബാലൻസ് സമവാക്യവുമായി സമീകരിച്ച് തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>എഞ്ചിൻ ടോർക്ക് റോഡിലെ പ്രതിരോധത്തേക്കാൾ കൂടുമ്പോൾ വണ്ടി വേഗത കൂട്ടുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q5: Four-Quadrant Operation of Hoist Load
    # -------------------------------------------------------------------------
    'drive-q5': {
        'manglish': {
            'title': "Hoist-nte Four-Quadrant operation detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Hoist 4 Quadrants Summary",
                'eq': r"$$Q1: \omega>0, T>0 \; (\text{Hoist Up}), \quad Q2: \omega>0, T<0 \; (\text{Stop Up}), \quad Q3: \omega<0, T<0 \; (\text{Drive Down}), \quad Q4: \omega<0, T>0 \; (\text{Braking Down})$$",
                'text': r"<strong>Ormavekkan:</strong> Hoist load gravity active load aanu. Quadrant 1 = Upward motoring. Quadrant 4 = Heavy load thazhottu varumbol gravity pottitherichu veezhathe motor generator aayi hold cheythu control cheythu irakkunnu (Regenerative braking)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>Quadrant 1 (Forward Motoring):</strong> Lifting loaded cage upward ($\omega > 0, T > 0, P > 0$). Motor fights gravity.</li>
        <li><strong>Quadrant 2 (Forward Braking):</strong> Stopping upward motion rapidly ($\omega > 0, T < 0, P < 0$).</li>
        <li><strong>Quadrant 3 (Reverse Motoring):</strong> Driving empty cage downward against counterweight ($\omega < 0, T < 0, P > 0$).</li>
        <li><strong>Quadrant 4 (Reverse Regenerative Braking):</strong> Lowering heavy loaded cage smoothly ($\omega < 0, T > 0, P < 0$). Gravity pulls cage down, motor provides upward holding torque and sends power back to supply!</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Oru elevator (lift) alochikku: Aalukalumaayi mukalilottu pokunnu (Q1). Aalukalumaayi thazhottu varumbol gravity vegam pottitherichu thazhe veezhikkum! Athu thadayan motor generator pole thirichu pidichu slow aayi irakkunnu (Q4 Regenerative Braking)!</p>
"""
        },
        'ml': {
            'title': "ഒരു ക്രെയിൻ/ഹോയിസ്റ്റ് ലോഡിന്റെ ഫോർ-ക്വാഡ്രന്റ് പ്രവർത്തനം വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 4 ക്വാഡ്രന്റുകൾ",
                'eq': r"$$Q1: P>0 \; (\text{ഉയർത്തുന്നു}), \quad Q4: P<0 \; (\text{സുരക്ഷിതമായി ഇറക്കുന്നു})$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ക്വാഡ്രന്റ് 1-ൽ ഭാരം മുകളിലേക്ക് ഉയർത്തുന്നു; ക്വാഡ്രന്റ് 4-ൽ വലിയ ഭാരം താഴേക്ക് പതിക്കാതെ റീജനറേറ്റീവ് ബ്രേക്കിംഗ് നൽകി ഇറക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>4 ക്വാഡ്രന്റുകളിലെയും സ്പീഡ്, ടോർക്ക്, പവർ ദിശകൾ ഡയഗ്രം സഹിതം എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ലിഫ്റ്റിൽ ആളുകളുമായി താഴേക്ക് വരുമ്പോൾ താഴെ വീഴാതെ മോട്ടോർ ബ്രേക്ക് നൽകി സാവധാനം ഇറക്കുന്നതാണ് ക്വാഡ്രന്റ് 4!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q6: Condition for Steady-State Stability
    # -------------------------------------------------------------------------
    'drive-q6': {
        'manglish': {
            'title': "Steady-State Stability criterion $\\frac{dT_L}{d\\omega_m} > \\frac{dT}{d\\omega_m}$ engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Stability Inequality",
                'eq': r"$$\frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m} > 0 \iff \frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m}$$",
                'text': r"<strong>Ormavekkan:</strong> Operating point-il speed alpam koodiyaal: Load torque motor torque-inekaal kooduthal aavanam ($T_L > T$), ennal matrame motor speed kuranju operating point-ilekk thirichu varoo!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Derivation Guide</span></div>
    <p>1. Equilibrium: $T_0 = T_{L0}$ at speed $\omega_{m0}$.</p>
    <p>2. Give small perturbation: $\omega_m = \omega_{m0} + \Delta\omega_m, \;\; T = T_0 + \Delta T, \;\; T_L = T_{L0} + \Delta T_L$.</p>
    <p>3. Taylor series approximation: $\Delta T = \left(\frac{dT}{d\omega_m}\right)\Delta\omega_m, \;\; \Delta T_L = \left(\frac{dT_L}{d\omega_m}\right)\Delta\omega_m$.</p>
    <p>4. Dynamic equation: $J \frac{d(\Delta\omega_m)}{dt} = \Delta T - \Delta T_L = \left[\frac{dT}{d\omega_m} - \frac{dT_L}{d\omega_m}\right]\Delta\omega_m$.</p>
    <p>5. Solution $\Delta\omega_m(t) = \Delta\omega_{m0} \exp\left[-\frac{1}{J}\left(\frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m}\right)t\right]$. For exponential decay to zero, exponent must be negative: $\frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m}$.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru ball bowl-te nadukku nilkkunnu: Ball-ne alpam thalliyaal, slope karanam opposing force undaayi thirichu nadukkilekk varum (Stable). Pakshe thalathiricha bowl aaneel, alpam thalliyaal nere thazhottu urundu pokum (Unstable). Slope $\frac{dT_L}{d\omega} > \frac{dT}{d\omega}$ aayirikkunnathaanu stabilizing bowl!</p>
"""
        },
        'ml': {
            'title': "സ്റ്റെഡി-സ്റ്റേറ്റ് സ്റ്റെബിലിറ്റി നിബന്ധന ($\\frac{dT_L}{d\\omega_m} > \\frac{dT}{d\\omega_m}$) എങ്ങനെ തെളിയിക്കാം?",
            'remember_this': {
                'title': "⚡ സ്റ്റെബിലിറ്റി സമവാക്യം",
                'eq': r"$$\frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> സ്പീഡ് കൂടുമ്പോൾ ലോഡ് ടോർക്കിന്റെ വർദ്ധനവ് മോട്ടോർ ടോർക്കിനേക്കാൾ കൂടുതലായിരിക്കണം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ഡെറിവേഷൻ</span></div>
    <p>ചെറിയൊരു വ്യതിയാനം ($\Delta\omega_m$) നൽകി ലീനിയറൈസ് ചെയ്ത് എക്സ്പോണൻഷ്യൽ ഡിക്കേ വഴി സമവാക്യം തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ചായക്കോപ്പയുടെ അടിത്തട്ടിൽ ഇരിക്കുന്ന ബോൾ പോലെ വ്യതിയാനമുണ്ടായാലും തനിയെ പൂർവ്വസ്ഥിതിയിലേക്ക് മടങ്ങിയെത്തുന്ന അവസ്ഥ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q6b: Thermal Heating and Cooling Dynamics
    # -------------------------------------------------------------------------
    'drive-q6b': {
        'manglish': {
            'title': "Electric motor-te Thermal Heating & Cooling dynamics equation engane derive cheyyam?",
            'remember_this': {
                'title': "⚡ Heating and Cooling Exponentials",
                'eq': r"$$\text{Heating: } \theta(t) = \theta_{ss}(1 - e^{-t/\tau_h}), \quad \text{Cooling: } \theta(t) = \theta_{initial} e^{-t/\tau_c}, \quad \tau = \frac{C}{A}$$",
                'text': r"<strong>Ormavekkan:</strong> Heating time constant $\tau_h$ cooling time constant $\tau_c$-inekaal ചെറുതായിരിക്കും ($\tau_c > \tau_h$), because motor off aakumbo shaft fan nilkkunnathukond cooling slow aayirikkum!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Heat balance: $p \cdot dt = C \cdot d\theta + A \theta \cdot dt$, where $p$ is power loss, $C$ heat capacity, $A$ heat dissipation.</p>
    <p>2. Differential equation: $\frac{d\theta}{dt} + \frac{A}{C}\theta = \frac{p}{C}$.</p>
    <p>3. Steady state temperature rise $\theta_{ss} = \frac{p}{A}$, time constant $\tau = \frac{C}{A}$.</p>
    <p>4. Heating solution: $\theta(t) = \theta_{ss}(1 - e^{-t/\tau}) + \theta_1 e^{-t/\tau}$.</p>
    <p>5. Cooling: when power $p = 0$, $\theta(t) = \theta_0 e^{-t/\tau_c}$.</p>
</div>
""",
            'understand_simply': r"""
<p>Mobile phone-il heavy game kalikkumbol choodu pettennu kayarunnu (Heating exponential). Game close cheythu vechaal phone thត្រുത്ത് thണുക്കാൻ kooduthal samayam edukkkunnu (Cooling exponential with larger time constant)!</p>
"""
        },
        'ml': {
            'title': "ഇലക്ട്രിക് മോട്ടോറിന്റെ ചൂടാകലും തണുക്കലും സംബന്ധിച്ച സമവാക്യങ്ങൾ കണ്ടെത്തുക",
            'remember_this': {
                'title': "⚡ തെർമൽ സമവാക്യം",
                'eq': r"$$\theta(t) = \theta_{ss}(1 - e^{-t/\tau_h})$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മോട്ടോർ പ്രവർത്തിക്കുമ്പോൾ താപനില എക്സ്പോണൻഷ്യലായി ഉയരുന്നു; നിർത്തുമ്പോൾ സാവധാനം തണുക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഹീറ്റ് ബാലൻസ് സമവാക്യം $p \cdot dt = C \cdot d\theta + A \theta \cdot dt$ സോൾവ് ചെയ്ത് താപനില കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>മൊബൈലിൽ ഗെയിം കളിക്കുമ്പോൾ പെട്ടെന്ന് ചൂടാവുകയും, വെറുതെ വെച്ചാൽ സാവധാനം തണുക്കുകയും ചെയ്യുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q7: Armature Voltage Control vs Field Weakening
    # -------------------------------------------------------------------------
    'drive-q7': {
        'manglish': {
            'title': "DC Motor-il Armature Voltage Control-um Field Weakening Control-um compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Constant Torque vs Constant Power",
                'eq': r"$$\text{Below Base Speed: } V_a \uparrow, \phi \text{ const } \implies \text{Constant Torque}; \quad \text{Above Base Speed: } V_a = V_{\text{rated}}, \phi \downarrow \implies \text{Constant Power}$$",
                'text': r"<strong>Ormavekkan:</strong> Base speed-nu thazhe: Armature voltage vary cheyyunnu (Constant torque region). Base speed-nu mukalil: Field flux $\phi$ kurachu speed kootunnu (Field weakening / Constant power region)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Feature</th><th>Armature Voltage Control</th><th>Field Weakening Control</th></tr></thead>
        <tbody>
            <tr><td><strong>Speed Range</strong></td><td>Below rated base speed ($0 \le \omega \le \omega_{\text{base}}$).</td><td>Above rated base speed ($\omega_{\text{base}} \le \omega \le 2\text{--}3\omega_{\text{base}}$).</td></tr>
            <tr><td><strong>Control Variable</strong></td><td>$V_a$ varies from 0 to $V_{\text{rated}}$, Field flux $\phi$ rated.</td><td>$V_a = V_{\text{rated}}$, Field current $I_f \downarrow \implies \phi \downarrow$.</td></tr>
            <tr><td><strong>Torque Capability</strong></td><td><strong>Constant Torque:</strong> $T_{\max} = K_t \phi_{\text{rated}} I_{a,\text{rated}} = \text{const}$.</td><td>Torque drops inversely with speed: $T \propto 1/\omega$.</td></tr>
            <tr><td><strong>Power Capability</strong></td><td>Power increases linearly: $P = T \cdot \omega \propto \omega$.</td><td><strong>Constant Power:</strong> $P_{\max} = V_{\text{rated}} I_{a,\text{rated}} = \text{const}$.</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Car gear shifts pole aanu: 1st/2nd gear-il speed kuravaanu pakshe pull cheyyan kooduthal torque undu (Constant Torque). 5th gear-il high speed kittum pakshe heavy load pull cheyyan pattilla, power constant aanu (Field Weakening Constant Power)!</p>
"""
        },
        'ml': {
            'title': "ആർമേച്ചർ വോൾട്ടേജ് കൺട്രോളും ഫീൽഡ് വീക്കനിംഗ് കൺട്രോളും താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ പ്രധാന തത്വം",
                'eq': r"$$\text{ബേസ് സ്പീഡിന് താഴെ: Constant Torque; മുകളിൽ: Constant Power}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ബേസ് സ്പീഡിന് താഴെ വോൾട്ടേജ് മാറ്റിയും, മുകളിൽ ഫീൽഡ് കറന്റ് കുറച്ചും വേഗത നിയന്ത്രിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ സ്പീഡ് റേഞ്ച്, ടോർക്ക്, പവർ സവിശേഷതകൾ വ്യക്തമായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വണ്ടിയുടെ 1st ഗിയറിൽ ഉയർന്ന ടോർക്കും (ആർമേച്ചർ കൺട്രോൾ), ടോപ്പ് ഗിയറിൽ ഉയർന്ന വേഗതയും (ഫീൽഡ് കൺട്രോൾ) ലഭിക്കുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q7b: Three-Phase Semi-Converter Fed DC Motor
    # -------------------------------------------------------------------------
    'drive-q7b': {
        'manglish': {
            'title': "Three-Phase Semi-Converter Fed DC Motor Drive-inte working-um output voltage equation-um ezhuthuka.",
            'remember_this': {
                'title': "⚡ Semi-Converter Average Voltage",
                'eq': r"$$V_0 = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha), \quad \omega_m = \frac{V_0 - I_a R_a}{K_m}$$",
                'text': r"<strong>Ormavekkan:</strong> 3 Thyristors + 3 Diodes + Freewheeling diode. Single quadrant motoring operation matrame pattu ($V_0 > 0, I_a > 0$). Inversion or regenerative braking cheyyan pattilla!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Output Voltage:</strong> $V_0 = \frac{3}{2\pi}\int_{\alpha + \pi/3}^{\pi} V_{ml}\sin(\omega t) d(\omega t) = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha)$.</p>
    <p>2. <strong>Advantages:</strong> Full converter-inekaal better power factor, freewheeling diode ഉള്ളതുകൊണ്ട് load current highly continuous aanu, cost kuravaanu.</p>
    <p>3. <strong>Limitation:</strong> Output voltage negative aakilla, so regenerative braking cheyyan pattilla.</p>
</div>
""",
            'understand_simply': r"""
<p>Semi-converter oru one-way valve pole aanu &mdash; current-ine forward matrame vidu, power motor-lekku pokum. Motor-il ninnu supply-ilottu power thirichu vidanulla reverse path ithil illa!</p>
"""
        },
        'ml': {
            'title': "ത്രീ-ഫേസ് സെമി-കൺവെർട്ടർ DC മോട്ടോർ ഡ്രൈവിന്റെ പ്രവർത്തനവും വോൾട്ടേജ് സമവാക്യവും എഴുതുക",
            'remember_this': {
                'title': "⚡ ശരാശരി വോൾട്ടേജ് സമവാക്യം",
                'eq': r"$$V_0 = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഒരു ക്വാഡ്രന്റിൽ മാത്രം (മോട്ടോറിംഗ്) പ്രവർത്തിക്കുന്നു. കുറഞ്ഞ ചിലവും ഉയർന്ന പവർ ഫാക്ടറും നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>3 തൈറിസ്റ്ററുകളും 3 ഡയോഡുകളും ചേർന്ന സർക്യൂട്ടിൽ $V_0 = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha)$ തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വൈദ്യുതി മോട്ടോറിലേക്ക് മാത്രം നൽകാൻ കഴിയുന്ന വൺ-വേ വാൽവ് പോലെ പ്രവർത്തിക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q8: Single-Phase Full Converter Fed DC Motor
    # -------------------------------------------------------------------------
    'drive-q8': {
        'manglish': {
            'title': "Single-Phase Full Converter Fed DC Motor-te operation-um waveforms-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Single-Phase Full Converter Equations",
                'eq': r"$$V_0 = \frac{2V_m}{\pi}\cos\alpha, \quad \omega_m = \frac{\frac{2V_m}{\pi}\cos\alpha - I_a R_a}{K_m}$$",
                'text': r"<strong>Ormavekkan:</strong> $\alpha < 90^\circ \implies V_0 > 0$ (Motoring). $\alpha > 90^\circ \implies V_0 < 0$ (Regenerative braking inverting mode). Two-quadrant capability ($+I_a, \pm V_0$)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Average Voltage:</strong> $V_0 = \frac{1}{\pi}\int_{\alpha}^{\pi+\alpha} V_m \sin(\omega t) d(\omega t) = \frac{2V_m}{\pi}\cos\alpha$.</p>
    <p>2. <strong>Motoring Mode ($\alpha < 90^\circ$):</strong> $V_0$ positive, power flows from AC source to DC motor.</p>
    <p>3. <strong>Regenerative Braking Mode ($\alpha > 90^\circ$):</strong> If motor back-EMF is reversed, $V_0$ becomes negative, acting as a line-commutated inverter feeding energy back to AC supply!</p>
    <p>4. Continuous vs Discontinuous conduction: Light load aavumbol current zero aayi discontinuous aavum, which causes poor speed regulation.</p>
</div>
""",
            'understand_simply': r"""
<p>Firing angle $\alpha$-ye oru accelerator pedal pole kaanaam: $\alpha$ kurayumbol ($30^\circ, 45^\circ$) nalla voltage kitunnu. $\alpha > 90^\circ$ aakkiyaal converter generator aayi maarukayum energy AC line-ilottu thirichu poyikondirikkukayum cheyyum!</p>
"""
        },
        'ml': {
            'title': "സിംഗിൾ-ഫേസ് ഫുൾ കൺവെർട്ടർ DC മോട്ടോർ ഡ്രൈവിന്റെ പ്രവർത്തനവും തരംഗരൂപങ്ങളും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഫുൾ കൺവെർട്ടർ സമവാക്യം",
                'eq': r"$$V_0 = \frac{2V_m}{\pi}\cos\alpha$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> $\alpha < 90^\circ$ ആകുമ്പോൾ മോട്ടോറിംഗും, $\alpha > 90^\circ$ ആകുമ്പോൾ റീജനറേറ്റീവ് ബ്രേക്കിംഗും ലഭിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>$V_0$ സമവാക്യം ഇന്റഗ്രേറ്റ് ചെയ്ത് കണ്ടെത്തുക. $\alpha < 90^\circ$, $\alpha > 90^\circ$ അവസ്ഥകൾ വേവ്ഫോം സഹിതം എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ആക്സിലറേറ്റർ പോലെ ഫയറിംഗ് ആംഗിൾ മാറ്റി വേഗത കൂട്ടാനും, ബ്രേക്കിംഗ് നൽകി വൈദ്യുതി തിരികെ നൽകാനും സാധിക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q8b: Three-Phase Full Converter Fed DC Motor
    # -------------------------------------------------------------------------
    'drive-q8b': {
        'manglish': {
            'title': "Three-Phase Full Converter Fed Separately Excited DC Motor-te analysis explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 3-Phase Full Converter Voltage",
                'eq': r"$$V_0 = \frac{3V_{ml}}{\pi}\cos\alpha, \quad \omega_m = \frac{\frac{3V_{ml}}{\pi}\cos\alpha - I_a R_a}{K_m}$$",
                'text': r"<strong>Ormavekkan:</strong> Ripple frequency $6f_s = 300\text{ Hz}$ (single phase-il $100\text{ Hz}$ mathram). High power industrial applications-il low ripple current and smooth torque tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. 6-pulse bridge converter using 6 Thyristors ($T_1$ to $T_6$).</p>
    <p>2. Average voltage: $V_0 = \frac{3}{\pi}\int_{\pi/3+\alpha}^{2\pi/3+\alpha} V_{ml}\sin(\omega t) d(\omega t) = \frac{3V_{ml}}{\pi}\cos\alpha$.</p>
    <p>3. Two quadrant operation: Quadrant 1 ($\alpha < 90^\circ$ Forward Motoring), Quadrant 4 ($\alpha > 90^\circ$ Forward Inversion / Braking).</p>
    <p>4. Ripple is 6-pulse, so filtering filter size is very small compared to 1-phase converters!</p>
</div>
""",
            'understand_simply': r"""
<p>Single phase engine oru 2-cylinder car pole aanu (alpam shaking undaakum). Pakshe 3-phase full converter oru V6 engine pole super smooth aanu &mdash; ripple valare kuravaanu, heavy rolling mills-il accurate power tharum!</p>
"""
        },
        'ml': {
            'title': "ത്രീ-ഫേസ് ഫുൾ കൺവെർട്ടർ DC മോട്ടോർ ഡ്രൈവിന്റെ സവിശേഷതകൾ വിശകലനം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ 3-ഫേസ് ഔട്ട്പുട്ട് സമവാക്യം",
                'eq': r"$$V_0 = \frac{3V_{ml}}{\pi}\cos\alpha$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 6-പൾസ് റിപ്പിൾ ആയതിനാൽ കറന്റ് വളരെ സ്മൂത്തായിരിക്കും; വലിയ ഇൻഡസ്ട്രിയൽ മോട്ടോറുകളിൽ ഉപയോഗിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>6 തൈറിസ്റ്ററുകളുടെ കണ്ടക്ഷൻ സീക്വൻസും $V_0 = \frac{3V_{ml}}{\pi}\cos\alpha$ സമവാക്യവും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു വി-6 എഞ്ചിൻ പോലെ വളരെ സ്മൂത്തായി യാതൊരു വിറയലുമില്ലാതെ പവർ നൽകുന്ന സിസ്റ്റമാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q9: Motoring Control using Class-A Chopper
    # -------------------------------------------------------------------------
    'drive-q9': {
        'manglish': {
            'title': "Class-A Step-Down Chopper use cheythu DC motor-ne motoring mode-il engane control cheyyam?",
            'remember_this': {
                'title': "⚡ Class-A Chopper Relations",
                'eq': r"$$V_0 = \delta \cdot V_s = \left(\frac{t_{on}}{T}\right)V_s, \quad \omega_m = \frac{\delta V_s - I_a R_a}{K_m}$$",
                'text': r"<strong>Ormavekkan:</strong> First quadrant operation ($V_0 > 0, I_a > 0$). Switch $S$ ON aavumbol source energy load-lekku pokunnu; switch OFF aavumbol freewheeling diode $D$ vazhi inductor current continuous aayi circulate cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Mode 1 (Switch ON, $0 \le t \le t_{on}$):</strong> $v_0 = V_s$. Supply current flows into armature: $L_a \frac{di_a}{dt} + R_a i_a + E_b = V_s$. Armature current rises exponentially.</p>
    <p>2. <strong>Mode 2 (Switch OFF, $t_{on} \le t \le T$):</strong> Switch opens. $v_0 = 0$. Inductor forces current through freewheeling diode $D$: $L_a \frac{di_a}{dt} + R_a i_a + E_b = 0$. Current decays exponentially.</p>
    <p>Duty ratio $\delta = t_{on}/T$ vary cheythu motor terminal voltage $0$ muthal $V_s$ vare smooth aayi control cheyyam!</p>
</div>
""",
            'understand_simply': r"""
<p>Battery-il ninnu fan-ilekku switch vegam vegam ON-um OFF-um aakkunnathu pole aanu chopper: 70% time ON aakkiyaal fan nannayi karangum, 20% time mathram ON aakkiyaal fan slow aayi karangum!</p>
"""
        },
        'ml': {
            'title': "ക്ലാസ്സ്-A ചോപ്പർ ഉപയോഗിച്ച് DC മോട്ടോറിന്റെ വേഗത എങ്ങനെ നിയന്ത്രിക്കാം?",
            'remember_this': {
                'title': "⚡ സ്റ്റെപ്പ്-ഡൗൺ സമവാക്യം",
                'eq': r"$$V_0 = \delta V_s$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഡ്യൂട്ടി സൈക്കിൾ $\delta$ മാറ്റി വോൾട്ടേജ് പൂജ്യം മുതൽ $V_s$ വരെ സുഗമമായി ക്രമീകരിക്കാം (First Quadrant Motoring)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സ്വിച്ച് ഓൺ, ഓഫ് മോഡുകളിലെ കറന്റ് സമവാക്യങ്ങളും സർക്യൂട്ടും വരച്ച് വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സ്വിച്ച് അതിവേഗം ഓണും ഓഫും ചെയ്ത് ശരാശരി വോൾട്ടേജ് നിയന്ത്രിക്കുന്ന രീതിയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q9b: Regenerative Braking using Class-B Chopper
    # -------------------------------------------------------------------------
    'drive-q9b': {
        'manglish': {
            'title': "Class-B Step-Up Chopper use cheythu DC motor-il Regenerative Braking engane cheyyam?",
            'remember_this': {
                'title': "⚡ Class-B Boost Equation",
                'eq': r"$$V_0 = (1 - \delta)V_s \text{ or } V_s = \frac{E_b}{1 - \delta}, \quad I_a < 0 \implies \text{Energy returned to Battery}$$",
                'text': r"<strong>Ormavekkan:</strong> Second quadrant operation ($V_0 > 0, I_a < 0$). Motor back-EMF $E_b$ battery voltage $V_s$-inekaal ചെറുതാണെങ്കിൽ polum, inductor boost action vazhi battery charge cheyyan kazhiyum!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Mode 1 (Switch ON):</strong> Switch $S$ closes. Armature short-circuits through $S$: $L_a \frac{di_a}{dt} + R_a i_a = E_b$. Kinetic energy inductor-il magnetic field aayi store cheyyunnu.</p>
    <p>2. <strong>Mode 2 (Switch OFF):</strong> Switch opens. Inductor polarity reverses: total voltage becomes $E_b + L_a \frac{di_a}{dt} > V_s$! This forces current through diode $D$ into the positive terminal of battery $V_s$.</p>
    <p>Result: Motor acts as a generator, mechanical vehicle slows down (braking), and battery gets recharged!</p>
</div>
""",
            'understand_simply': r"""
<p>Electric scooter brake pidikkumbol: Motor kinetic energy eduthu oru boost pump pole battery-ilottu current thallividunnu. Vandi brake aavukayum cheyyum, battery charge aavukayum cheyyum &mdash; free energy recovery!</p>
"""
        },
        'ml': {
            'title': "ക്ലാസ്സ്-B ചോപ്പർ ഉപയോഗിച്ച് റീജനറേറ്റീവ് ബ്രേക്കിംഗ് എങ്ങനെ സാധ്യമാക്കാം?",
            'remember_this': {
                'title': "⚡ ബൂസ്റ്റ് ബ്രേക്കിംഗ് സമവാക്യം",
                'eq': r"$$E_b + L\frac{di}{dt} > V_s \implies \text{ബാറ്ററിയിലേക്ക് കറന്റ് തിരികെ കയറുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻഡക്ടർ ബൂസ്റ്റ് പ്രവർത്തനം വഴി ബാക്ക്-ഇഎംഎഫ് കുറവാണെങ്കിലും ബാറ്ററി ചാർജ്ജ് ചെയ്യാൻ സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സ്വിച്ച് ഓണാകുമ്പോൾ ഇൻഡക്ടറിൽ എനർജി സൂക്ഷിക്കുന്നതും, ഓഫാകുമ്പോൾ ബാറ്ററിയിലേക്ക് ഡിസ്ചാർജ് ചെയ്യുന്നതും വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ബ്രേക്ക് ചെയ്യുമ്പോൾ ഉണ്ടാകുന്ന ഊർജ്ജം കൊണ്ട് ബാറ്ററി ചാർജ് ചെയ്യുന്ന അത്ഭുത വിദ്യയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q10: Two-Quadrant Class-C Chopper Fed DC Motor
    # -------------------------------------------------------------------------
    'drive-q10': {
        'manglish': {
            'title': "Two-Quadrant Class-C Chopper fed DC Motor Drive-nte operation detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Class-C Chopper Operation",
                'eq': r"$$V_0 > 0, \;\; I_a > 0 \text{ (Quadrant 1 Motoring)} \iff V_0 > 0, \;\; I_a < 0 \text{ (Quadrant 2 Regenerative Braking)}$$",
                'text': r"<strong>Ormavekkan:</strong> Combination of Class-A and Class-B choppers (2 switches $S_1, S_2$ and 2 diodes $D_1, D_2$). Voltage eppozhum positive aayirikkum, current can reverse seamlessly."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Quadrant 1 (Motoring):</strong> $S_1$ and $D_2$ operate. When $S_1$ ON, current flows from source to motor ($+I_a$). When $S_1$ OFF, current freewheels through $D_2$.</p>
    <p>2. <strong>Quadrant 2 (Braking):</strong> $S_2$ and $D_1$ operate. When $S_2$ ON, motor current builds up in reverse through $L_a$. When $S_2$ OFF, current is pumped into source through $D_1$.</p>
    <p>Crucial protection: $S_1$-um $S_2$-um ore samayathu ON aavalle (Dead-time kodukkanam, illenkil DC source direct short-circuit aayi pottitherikkum)!</p>
</div>
""",
            'understand_simply': r"""
<p>Electric car accelerator chavittumbol $S_1$ vazhi power edukkkunnu (Q1 Motoring). Accelerator vidumbozh thanne $S_2$ vazhi instantaneous aayi regenerative brake cheythu battery charge aakkunnu (Q2 Braking) &mdash; Single pedal driving!</p>
"""
        },
        'ml': {
            'title': "ക്ലാസ്സ്-C ടൂ-ക്വാഡ്രന്റ് ചോപ്പർ DC മോട്ടോർ ഡ്രൈവിന്റെ പ്രവർത്തനം വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ടൂ-ക്വാഡ്രന്റ് പ്രവർത്തനം",
                'eq': r"$$\text{Quadrant 1 (Motoring) } + \text{ Quadrant 2 (Regenerative Braking)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> രണ്ട് സ്വിച്ചുകളും രണ്ട് ഡയോഡുകളും ഉപയോഗിച്ച് ഒരേസമയം മോട്ടോറിംഗും ബ്രേക്കിംഗും സാധ്യമാക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സർക്യൂട്ട് ഡയഗ്രം വരച്ച് $S_1, D_2$ (മോട്ടോറിംഗ്), $S_2, D_1$ (ബ്രേക്കിംഗ്) പ്രവർത്തനങ്ങൾ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ആക്സിലറേറ്റർ കൊടുക്കുമ്പോൾ ഓടുകയും, കാലെടുക്കുമ്പോൾ തനിയെ ബ്രേക്ക് ചെയ്ത് ചാർജ്ജാവുകയും ചെയ്യുന്ന സിസ്റ്റം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q10b: Four-Quadrant Class-E Chopper Fed DC Motor (H-Bridge)
    # -------------------------------------------------------------------------
    'drive-q10b': {
        'manglish': {
            'title': "Four-Quadrant Class-E Chopper (H-Bridge) Fed DC Motor Drive-nte operation explain cheyyuka.",
            'remember_this': {
                'title': "⚡ H-Bridge 4 Quadrants",
                'eq': r"$$Q1: (S_1, S_4) \implies +V, +I; \quad Q2: (D_1, D_4) \implies +V, -I; \quad Q3: (S_2, S_3) \implies -V, -I; \quad Q4: (D_2, D_3) \implies -V, +I$$",
                'text': r"<strong>Ormavekkan:</strong> 4 switches ($S_1\text{--}S_4$) and 4 antiparallel diodes ($D_1\text{--}D_4$). Motor-ine forward motoring, forward braking, reverse motoring, and reverse braking &mdash; ella 4 quadrants-ilum complete control tharunnu!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Quadrant</th><th>Mode</th><th>Active Switches / Diodes</th><th>Voltage & Current</th></tr></thead>
        <tbody>
            <tr><td><strong>Q1</strong></td><td>Forward Motoring</td><td>$S_1$ ON, $S_4$ modulated (or both ON)</td><td>$V_0 > 0, I_a > 0$</td></tr>
            <tr><td><strong>Q2</strong></td><td>Forward Braking</td><td>$S_2$ switched, feedback through $D_1, D_4$</td><td>$V_0 > 0, I_a < 0$</td></tr>
            <tr><td><strong>Q3</strong></td><td>Reverse Motoring</td><td>$S_3$ ON, $S_2$ modulated</td><td>$V_0 < 0, I_a < 0$</td></tr>
            <tr><td><strong>Q4</strong></td><td>Reverse Braking</td><td>$S_4$ switched, feedback through $D_2, D_3$</td><td>$V_0 < 0, I_a > 0$</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Oru toy RC car or industrial robot alochikku: Mukhathottu odikkanam (Q1), brake pidikkanam (Q2), pinnilottu reverse odikkanam (Q3), reverse brake pidikkanam (Q4) &mdash; ithu motham oru single H-bridge circuit vechanu cheyyunnath!</p>
"""
        },
        'ml': {
            'title': "എച്ച്-ബ്രിഡ്ജ് (ക്ലാസ്സ്-E) ഫോർ-ക്വാഡ്രന്റ് ചോപ്പർ DC മോട്ടോർ ഡ്രൈവ് വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 4-ക്വാഡ്രന്റ് സമവാക്യം",
                'eq': r"$$\pm V_0, \quad \pm I_a \implies \text{Full Four Quadrant Control}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 4 സ്വിച്ചുകൾ ഉപയോഗിച്ച് മോട്ടോറിനെ മുന്നോട്ടും പിന്നോട്ടും ഓടിക്കാനും ബ്രേക്ക് ചെയ്യാനും സാധിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>എച്ച്-ബ്രിഡ്ജ് സർക്യൂട്ട് വരച്ച് 4 ക്വാഡ്രന്റുകളിലെയും സ്വിച്ചിംഗ് കോമ്പിനേഷനുകൾ ടേബിളിൽ വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>റിമോട്ട് കൺട്രോൾ കാറുകളിലും റോബോട്ടുകളിലും മുന്നോട്ടും പിന്നോട്ടും ഓടിക്കാനും ബ്രേക്ക് ചെയ്യാനും ഉപയോഗിക്കുന്ന എച്ച്-ബ്രിഡ്ജ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q11: Closed-Loop Speed Control Architecture
    # -------------------------------------------------------------------------
    'drive-q11': {
        'manglish': {
            'title': "Inner Current Loop ulla Closed-Loop Speed Control Architecture explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Cascade Control Loops",
                'eq': r"$$\text{Outer Loop: Speed Controller (PI)} \to I_a^* \text{ (Current Limit)} \to \text{Inner Loop: Current Controller (PI)} \to \text{Firing Angle } \alpha$$",
                'text': r"<strong>Ormavekkan:</strong> 2 loops: Outer slow speed loop reference current $I_a^*$ generate cheyyunnu. Inner fast current loop motor armature current-ine rated limit-il (1.5 $I_{\text{rated}}$) protect cheyyunnu!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Control Hierarchy:</strong></p>
    <ol>
        <li>Speed error $e_\omega = \omega^* - \omega$ Speed Controller (PI)-ilottu pokunnu.</li>
        <li>Speed controller-te output oru <strong>Current Limiter</strong> vazhi pass cheythu reference current $I_a^*$ aakkunnu (Starting time-il motor burn aavathirikkan ithu aavashyamaanu!).</li>
        <li>Current error $e_i = I_a^* - I_a$ Current Controller (PI)-ilottu pokunnu.</li>
        <li>Output firing circuit-lekku control voltage $V_c$ koduthu converter firing angle $\alpha$ theerumanikkunnu.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru company hierarchy pole aanu: Managing Director (Speed Controller) order kodukkunnu: 'Production 100 units kootanam'. Production Manager (Current Controller) nokkunnu: 'Machines overload aavumo?' Overload aavathe safe current limit-il nirthi speed kootunnu!</p>
"""
        },
        'ml': {
            'title': "ഇന്നർ കറന്റ് ലൂപ്പുള്ള ക്ലോസ്ഡ്-ലൂപ്പ് സ്പീഡ് കൺട്രോൾ ആർക്കിടെക്ചർ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ കാസ്കേഡ് കൺട്രോൾ",
                'eq': r"$$\text{ഔട്ടർ സ്പീഡ് ലൂപ്പ് } \to \text{കറന്റ് ലിമിറ്റർ } \to \text{ഇന്നർ കറന്റ് ലൂപ്പ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> സ്പീഡ് കൃത്യമാക്കുന്നതിനൊപ്പം മോട്ടോർ കറന്റ് സുരക്ഷിത പരിധിക്കുള്ളിൽ നിർത്താൻ ഇന്നർ ലൂപ്പ് സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ബ്ലോക്ക് ഡയഗ്രം വരച്ച് സ്പീഡ് കൺട്രോളർ, കറന്റ് ലിമിറ്റർ, കറന്റ് കൺട്രോളർ എന്നിവയുടെ പങ്ക് വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഡ്രൈവർ വേഗത കൂട്ടാൻ ആഗ്രഹിച്ചാലും എഞ്ചിൻ ഓവർഹീറ്റാവാതെ സുരക്ഷിത പരിധിയിൽ നിയന്ത്രിക്കുന്ന സ്മാർട്ട് സിസ്റ്റം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q12: Stator Voltage Control of Induction Motors
    # -------------------------------------------------------------------------
    'drive-q12': {
        'manglish': {
            'title': "Induction Motor-il Stator Voltage Control-te limitations-um application boundaries-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Torque-Voltage Squared Law",
                'eq': r"$$T \propto V^2, \quad T_{\max} \propto V^2, \quad s_{\max} = \text{const}$$",
                'text': r"<strong>Ormavekkan:</strong> Voltage kurayumbol torque $V^2$ aayi drastical aayi kurayunnu! Pull-out slip $s_m$ same aanu. Efficiency poor aanu, motor overheats at low speeds. Only fan/pump loads-nu matrame suitable aakoo."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Maximum breakdown torque: $T_{\max} = \frac{3}{2\omega_s}\frac{V^2}{2 X_2} \propto V^2$. Voltage 50% aakkiyaal torque 25% aayi kurayum!</p>
    <p>2. Stable speed range is very narrow (only from synchronous speed to $s_m \approx 0.1\text{--}0.15$).</p>
    <p>3. Rotor copper loss $P_{cr} = s P_g$. Low speed-il slip $s$ valuthavumbol rotor nannayi overheat aavum.</p>
    <p>Applications: Fan regulator, centrifugal pumps, appliance blowers where load torque drops with square of speed ($T_L \propto \omega^2$).</p>
</div>
""",
            'understand_simply': r"""
<p>Ceiling fan regulator nokku: Electronic regulator voltage kurachu kodukkumbol fan speed kurayunnu. Fan load aayathukond ithu work cheyyum. Pakshe heavy lift-il stator voltage control ittaal lift thazhottu veezhum, because torque $V^2$ aayi thazhe poyikkolum!</p>
"""
        },
        'ml': {
            'title': "ഇൻഡക്ഷൻ മോട്ടോറുകളിൽ സ്റ്റേറ്റർ വോൾട്ടേജ് കൺട്രോളിന്റെ പരിമിതികൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ ടോർക്ക്-വോൾട്ടേജ് ബന്ധം",
                'eq': r"$$T \propto V^2$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> വോൾട്ടേജ് കുറയുമ്പോൾ ടോർക്ക് വർഗ്ഗാനുപാതത്തിൽ കുറയുന്നു ($V^2$); കാര്യക്ഷമത കുറവായതിനാൽ ഫാനുകളിൽ മാത്രമേ ഉപയോഗിക്കാനാകൂ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>$T \propto V^2$ സവിശേഷതയും, ഉയർന്ന റോട്ടർ കോപ്പർ നഷ്ടവും, ഫാൻ ലോഡുകളിൽ മാത്രമുള്ള ഉപയോഗവും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സീലിംഗ് ഫാനുകളിൽ സ്പീഡ് കുറയ്ക്കാൻ ഇത് മതിയാകും, പക്ഷേ വലിയ ഫാക്ടറി മെഷീനുകളിൽ ടോർക്ക് നഷ്ടപ്പെടും!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q12b: Comparison between VSI and CSI Drives
    # -------------------------------------------------------------------------
    'drive-q12b': {
        'manglish': {
            'title': "Voltage Source Inverter (VSI) drives-um Current Source Inverter (CSI) drives-um compare cheyyuka.",
            'remember_this': {
                'title': "⚡ VSI vs CSI Core Rule",
                'eq': r"$$\text{VSI: DC Link Capacitor } (C), \text{ stiff } V; \quad \text{CSI: DC Link Inductor } (L), \text{ stiff } I$$",
                'text': r"<strong>Ormavekkan:</strong> VSI uses fast IGBTs with PWM (Dominates 95% modern drives). CSI uses Thyristors with large DC inductor, inherently capable of 4-quadrant regeneration without extra antiparallel bridge."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Parameter</th><th>Voltage Source Inverter (VSI)</th><th>Current Source Inverter (CSI)</th></tr></thead>
        <tbody>
            <tr><td><strong>DC Link Element</strong></td><td>Large Capacitor ($C$) acting as constant voltage source.</td><td>Large Inductor ($L$) acting as constant current source.</td></tr>
            <tr><td><strong>Output Waveforms</strong></td><td>Voltage is PWM stepped pulses; Current is sinusoidal.</td><td>Current is 6-step block; Voltage is sinusoidal.</td></tr>
            <tr><td><strong>Regeneration</strong></td><td>Requires antiparallel dual converter or braking chopper.</td><td>Inherent regeneration by simply reversing DC link voltage polarity!</td></tr>
            <tr><td><strong>Short-circuit Safety</strong></td><td>Shoot-through causes destructive fuse blow.</td><td>Inherently protected against short-circuit by DC inductor.</td></tr>
            <tr><td><strong>Market Adoption</strong></td><td>Universal choice (EVs, HVAC, Servo drives, Industrial VFDs).</td><td>Only very large multi-megawatt fans/pumps.</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>VSI oru nalla water tank pole aanu (pressure/voltage constant). CSI oru continuous water pump pole aanu (flow/current constant). VSI modern electronics-il super flexible aayathukond ella electric car-ilum VSI aanu use cheyyunnath!</p>
"""
        },
        'ml': {
            'title': "വോൾട്ടേജ് സോഴ്സ് ഇൻവെർട്ടറും (VSI) കറന്റ് സോഴ്സ് ഇൻവെർട്ടറും (CSI) തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ പ്രധാന താരതമ്യം",
                'eq': r"$$\text{VSI (Capacitor DC Link)} \quad \text{vs} \quad \text{CSI (Inductor DC Link)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> VSI-യിൽ കപ്പാസിറ്റർ ഉപയോഗിച്ച് വോൾട്ടേജ് സ്ഥിരമാക്കുന്നു; CSI-യിൽ ഇൻഡക്ടർ ഉപയോഗിച്ച് കറന്റ് സ്ഥിരമാക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ ഡിസി ലിങ്ക്, ഔട്ട്പുട്ട് വേവ്ഫോം, റീജനറേഷൻ, ഷോർട്ട് സർക്യൂട്ട് പ്രൊട്ടക്ഷൻ എന്നിവ താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഇന്നത്തെ എല്ലാ ഇലക്ട്രിക് കാറുകളിലും ഇൻഡസ്ട്രികളിലും ഉപയോഗിക്കുന്ന സൂപ്പർ താരമാണ് VSI!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q13: Constant V/f Speed Control of Induction Motors
    # -------------------------------------------------------------------------
    'drive-q13': {
        'manglish': {
            'title': "Induction Motor-te Constant V/f Speed Control theory and derivation detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Constant Flux & Torque Relation",
                'eq': r"$$\phi_m \approx \frac{V_1}{4.44 f_1 K_w N_1} = \text{const} \iff \frac{V}{f} = \text{const} \implies T_{\max} = \text{Constant at all speeds}$$",
                'text': r"<strong>Ormavekkan:</strong> Frequency $f$ mathram kurachaal flux $\phi \propto V/f$ koodi core saturate aayi motor burn aavum. So frequency kuraykkumbol voltage-um proportionally kuraykkunnu. Low frequencies-il stator resistance drop compensate cheyyan 'Voltage Boost' kodukkanam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Derivation Guide</span></div>
    <p>1. <strong>Air-gap flux:</strong> $E_1 = 4.44 f_1 K_w N_1 \phi_m \approx V_1 \implies \phi_m \propto \frac{V_1}{f_1}$.</p>
    <p>2. Keeping $\frac{V_1}{f_1} = c$ prevents magnetic core saturation and excessive magnetizing current.</p>
    <p>3. <strong>Maximum Torque:</strong> $T_{\max} \approx \frac{3}{2\omega_s}\frac{V_1^2}{2 X_2} = \frac{3}{2(2\pi f_1/P)}\frac{V_1^2}{2(2\pi f_1 L_2)} \propto \left(\frac{V_1}{f_1}\right)^2 = \text{Constant!}$</p>
    <p>4. <strong>Low-frequency Voltage Boost:</strong> At low $f$, stator resistance $I_1 R_1$ dominates over $2\pi f L_1$, causing flux to drop. So additional boost voltage $V_{\text{boost}}$ is added.</p>
</div>
""",
            'understand_simply': r"""
<p>Chaya-yil paalum vellavum correct ratio-il ozhikkunna karyam alochikku: Paal mathram koodiyaal katti koodi povum (Core Saturation), vellam koodiyaal taste povum (Weak torque). Frequency maarumbol voltage-um athinte koode match cheythu maintain cheyyunnathaanu $V/f$ ratio!</p>
"""
        },
        'ml': {
            'title': "കോൺസ്റ്റന്റ് V/f ഇൻഡക്ഷൻ മോട്ടോർ സ്പീഡ് കൺട്രോൾ തത്വവും സമവാക്യങ്ങളും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ V/f സ്ഥിരത സമവാക്യം",
                'eq': r"$$\phi \propto \frac{V}{f} = \text{Constant} \implies T_{\max} = \text{Constant}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഫ്രീക്വൻസിയും വോൾട്ടേജും ഒരേ അനുപാതത്തിൽ നിലനിർത്തി കോർ സാച്ചുറേഷൻ ഒഴിവാക്കുകയും ടോർക്ക് സ്ഥിരമാക്കുകയും ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>മാഗ്നറ്റിക് ഫ്ലക്സ് സമവാക്യം, മാക്സിമം ടോർക്ക് സ്ഥിരത, ലോ-ഫ്രീക്വൻസി വോൾട്ടേജ് ബൂസ്റ്റ് എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>എല്ലാ സ്പീഡിലും ഒരേപോലെ ഉയർന്ന ശക്തി (ടോർക്ക്) നിലനിർത്താൻ വോൾട്ടേജും ഫ്രീക്വൻസിയും ഒന്നിച്ച് കൂട്ടുകയും കുറയ്ക്കുകയും ചെയ്യുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q14: Static Rotor Resistance Control
    # -------------------------------------------------------------------------
    'drive-q14': {
        'manglish': {
            'title': "Wound-Rotor Induction Motor-il Chopper-controlled Static Rotor Resistance Speed Control engane work cheyyunnu?",
            'remember_this': {
                'title': "⚡ Effective Rotor Resistance",
                'eq': r"$$R_{\text{eff}} = R_{ext}(1 - \delta), \quad R_{\text{total}} = R_2 + R_{\text{eff}}, \quad s \propto R_{\text{total}}$$",
                'text': r"<strong>Ormavekkan:</strong> 3-phase diode bridge rotor slip frequency AC-ye DC aakkunnu. Chopper duty cycle $\delta = t_{on}/T$ smoothly vary cheythu effective resistance step-less aayi control cheyyam!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Slip-ring induction motor rotor terminals diode bridge rectifier-ilottu connect cheyyunnu.</p>
    <p>2. DC side-il oru smoothing inductor $L_d$, parallel external resistor $R$, and an electronic chopper switch $S$ undu.</p>
    <p>3. When chopper is ON ($\delta$), resistor is shorted ($R_{\text{eff}} = 0$). When OFF ($1 - \delta$), resistor is in circuit.</p>
    <p>4. Average equivalent resistance seen by rotor: $R_{\text{eq}} = R(1 - \delta)$.</p>
    <p>Advantage: Old mechanical contactors maati smooth, electronic, stepless speed control kittum!</p>
</div>
""",
            'understand_simply': r"""
<p>Olden days-il cinema theatre fans-il വലിയ coil resistance rotary knob thirichu maattumayirunnu (spark-um choodum). Athinu pakaram oru high speed transistor chopper switch vechu resistor-ine on/off cheythu smooth aayi control cheyyunna technique aanu ithu!</p>
"""
        },
        'ml': {
            'title': "സ്റ്റാറ്റിക് റോട്ടർ റെസിസ്റ്റൻസ് ചോപ്പർ സ്പീഡ് കൺട്രോൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ റോട്ടർ റെസിസ്റ്റൻസ് സമവാക്യം",
                'eq': r"$$R_{\text{eff}} = R(1 - \delta)$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ചോപ്പർ ഡ്യൂട്ടി സൈക്കിൾ $\delta$ മാറ്റി റോട്ടർ റെസിസ്റ്റൻസും വേഗതയും സ്റ്റെപ്പ്-ലെസ്സ് ആയി നിയന്ത്രിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>റെക്റ്റിഫയറും ചോപ്പറും ചേർന്ന സർക്യൂട്ട് വരച്ച് $R_{\text{eff}} = R(1 - \delta)$ പ്രവർത്തന തത്വം വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>പഴയ റെസിസ്റ്റൻസ് കോയിലുകൾ മാറ്റി ഇലക്ട്രോണിക് സ്വിച്ച് വഴി സ്പീഡ് സുഗമമായി നിയന്ത്രിക്കുന്ന രീതി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q14b: Slip Power Recovery Schemes (Static Kramer vs Scherbius)
    # -------------------------------------------------------------------------
    'drive-q14b': {
        'manglish': {
            'title': "Slip Power Recovery Schemes: Static Kramer vs Static Scherbius systems compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Kramer vs Scherbius Core Difference",
                'eq': r"$$\text{Static Kramer: Sub-synchronous only } (\omega < \omega_s); \quad \text{Static Scherbius: Sub and Super-synchronous } (\omega \gtrless \omega_s)$$",
                'text': r"<strong>Ormavekkan:</strong> Rotor slip power $s P_g$ resistor-il heat aayi kalayunnathinu pakaram inverter vazhi thirichu AC supply-ilottu feed cheythu huge energy save cheyyunnu! Kramer uses diode bridge + line inverter; Scherbius uses bidirectional cycloconverter/dual VSI."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Feature</th><th>Static Kramer Drive</th><th>Static Scherbius Drive</th></tr></thead>
        <tbody>
            <tr><td><strong>Power Converters</strong></td><td>Diode Bridge Rectifier + Line Commutated Inverter.</td><td>Bidirectional Cycloconverter or Dual PWM Inverters.</td></tr>
            <tr><td><strong>Speed Range</strong></td><td>Only below synchronous speed ($\omega < \omega_s$, Sub-synchronous).</td><td>Both below and above synchronous speed ($\omega < \omega_s$ and $\omega > \omega_s$).</td></tr>
            <tr><td><strong>Power Flow</strong></td><td>Unidirectional: from rotor to AC mains only.</td><td>Bidirectional: rotor to mains and mains to rotor.</td></tr>
            <tr><td><strong>Application</strong></td><td>Large pumps, blowers, cement mills.</td><td>Variable-speed wind turbines (DFIG), pumped hydro storage.</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Rotor slip power ennathu factory chimney-il ninnu purathupokunna waste steam pole aanu. Aa steam-ine waste aayi kalayathe turbine karakki electricity undakkunnathaanu Slip Power Recovery! Kramer sub-speed-il mathram, Scherbius double direction super-speed-ilum work cheyyum!</p>
"""
        },
        'ml': {
            'title': "സ്ലിപ്പ് പവർ റിക്കവറി സ്കീമുകൾ: സ്റ്റാറ്റിക് ക്രാമറും ഷെർബിയസും താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ സ്ലിപ്പ് പവർ റിക്കവറി",
                'eq': r"$$\text{വേസ്റ്റ് ആകുന്ന റോട്ടർ പവർ തിരികെ മെയിൻസിലേക്ക് നൽകുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ക്രാമർ സബ്-സിൻക്രണസ് വേഗതയിൽ മാത്രം; ഷെർബിയസ് സബ്-സിൻക്രണസ്, സൂപ്പർ-സിൻക്രണസ് വേഗതകളിൽ പ്രവർത്തിക്കുന്നു (വിൻഡ് ടർബൈനുകൾ)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ കൺവെർട്ടർ തരം, വേഗത പരിധി, പവർ ഫ്ലോ ദിശ, ആപ്ലിക്കേഷനുകൾ എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വേസ്റ്റ് ആയി പോകുന്ന ചൂട് ഊർജ്ജത്തെ തിരികെ വൈദ്യുതിയാക്കി മാറ്റി ലാഭിക്കുന്ന അത്യാധുനിക വിൻഡ് മിൽ സാങ്കേതികവിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q15: True Synchronous Mode vs Self-Controlled Mode
    # -------------------------------------------------------------------------
    'drive-q15': {
        'manglish': {
            'title': "Synchronous Motor-il True Synchronous Mode-um Self-Controlled Mode-um compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Self-Control = Elimination of Hunting",
                'eq': r"$$\text{True Sync: Independent Oscillator } f \implies \text{Risk of Hunting \& Pull-out}; \quad \text{Self-Controlled: Rotor Position Sensor feeds } f \implies \text{Never loses synchronism}$$",
                'text': r"<strong>Ormavekkan:</strong> Self-controlled mode-il shaft position encoder inverter-te firing control cheyyunnu. Rotor speed maarumbol inverter frequency thaniye match aavunnu, so motor never pulls out of synchronism (Electronic Commutation)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. True Synchronous Mode:</strong> Inverter frequency external frequency generator control cheyyunnu. Sudden load change vannal rotor hunting cheyyum or pull out of synchronism aayi stall aavum. Damper windings strictly needed.</li>
        <li><strong>2. Self-Controlled Mode:</strong> Rotor position sensor (Hall sensor or optical encoder) continuously measures rotor angle $\theta_r$ and triggers inverter switches. Frequency is locked to actual rotor speed. Acts like an inverted DC motor (Brushless DC / PMSM)! No hunting, superior stability.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>True synchronous mode oru marching band pole aanu &mdash; leader drum adikkanam, ellavarum koode odanam. Kaalu thettiyaal veezhum! Self-controlled mode-il ningalude oro footstep-um sensor measure cheythu athinu anusarichu drum adikkanam &mdash; kaalu thetti veezhanna prashname illa!</p>
"""
        },
        'ml': {
            'title': "ട്രൂ സിൻക്രണസ് മോഡും സെൽഫ്-കൺട്രോൾഡ് മോഡും താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ സെൽഫ് കൺട്രോൾ തത്വം",
                'eq': r"$$\text{റോട്ടർ പൊസിഷൻ അനുസരിച്ച് ഇൻവെർട്ടർ സ്വിച്ച് ചെയ്യുന്നു (BLDC തത്വം)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> സെൽഫ്-കൺട്രോൾഡ് മോഡിൽ ഹണ്ടിംഗോ സിൻക്രണൈസേഷൻ നഷ്ടപ്പെടലോ ഉണ്ടാകുന്നില്ല."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>എക്സ്റ്റേണൽ ഫ്രീക്വൻസിയും റോട്ടർ പൊസിഷൻ സെൻസറും തമ്മിലുള്ള വ്യത്യാസം താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>റോട്ടർ തിരിയുന്നതിനനുസരിച്ച് മാത്രം ഇൻവെർട്ടർ പ്രവർത്തിക്കുന്നതിനാൽ മോട്ടോർ ഒരിക്കലും നിന്നുപോവില്ല!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q15b: Load-Commutated Inverter (LCI) Fed Synchronous Motor
    # -------------------------------------------------------------------------
    'drive-q15b': {
        'manglish': {
            'title': "Load-Commutated Inverter (LCI) Fed Synchronous Motor Drive-inte working detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Leading PF Commutation",
                'eq': r"$$\text{Overexcited Synchronous Motor} \implies \text{Leading Power Factor} \implies \text{Natural Load Commutation of Thyristors}$$",
                'text': r"<strong>Ormavekkan:</strong> Expensive forced commutation circuits or IGBTs venda! Motor over-excite cheythu leading power factor-il run cheythaal, motor-te back-EMF thaniye thyristors-ine turn-off cheythu tharum (Natural Commutation). Multi-megawatt gas turbines and compressors-il use cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Circuit consists of 3-phase line-side converter, large DC link inductor $L_d$, and load-side thyristor inverter.</p>
    <p>2. Synchronous motor is intentionally operated at leading power factor by overexciting the field winding.</p>
    <p>3. Motor back-EMF acts like an AC source for the load inverter, naturally commutating the thyristors without any external force.</p>
    <p>4. <strong>Starting issue:</strong> At zero speed, motor back-EMF is zero! So 'Pulsed DC Link Commutation' is used until motor reaches 10% rated speed.</p>
</div>
""",
            'understand_simply': r"""
<p>Thyristors-ne turn-off cheyyan external electronic circuits aavashyamilla &mdash; motor thanne oru AC generator pole behave cheythu thyristor-inte gate off aakki kodukkum! Valare heavy megawatt pumps-il super reliable system aanu LCI.</p>
"""
        },
        'ml': {
            'title': "ലോഡ്-കമ്മ്യൂട്ടേറ്റഡ് ഇൻവെർട്ടർ (LCI) സിൻക്രണസ് മോട്ടോർ ഡ്രൈവ് വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ലോഡ് കമ്മ്യൂട്ടേഷൻ",
                'eq': r"$$\text{ലീഡിംഗ് പവർ ഫാക്ടർ വഴി തൈറിസ്റ്ററുകൾ സ്വയം ഓഫ് ആകുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മോട്ടോർ ഓവർ-എക്സൈറ്റ് ചെയ്യുമ്പോൾ ഉണ്ടാകുന്ന ബാക്ക്-ഇഎംഎഫ് തൈറിസ്റ്ററുകളെ കമ്മ്യൂട്ടേറ്റ് ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സർക്യൂട്ട് ഡയഗ്രം വരച്ച് ലീഡിംഗ് പവർ ഫാക്ടർ വഴിയുള്ള സ്വാഭാവിക കമ്മ്യൂട്ടേഷനും സ്റ്റാർട്ടിംഗ് പൾസിംഗ് രീതിയും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>മോട്ടോർ തന്നെ തിരികെ വോൾട്ടേജ് നൽകി സ്വിച്ചുകളെ ഓഫാക്കുന്ന അത്ഭുതകരമായ മെഗാവാട്ട് സാങ്കേതികവിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q16: Mathematical Derivation of Clarke and Park Transformations
    # -------------------------------------------------------------------------
    'drive-q16': {
        'manglish': {
            'title': "Clarke ($abc \\to \\alpha\\beta$) and Park ($\\alpha\\beta \\to dq$) Reference Frame Transformations derive cheyyuka.",
            'remember_this': {
                'title': "⚡ Clarke & Park Transformation Matrices",
                'eq': r"$$\begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix} = \frac{2}{3}\begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}, \quad \begin{bmatrix} i_d \\ i_q \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}\begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix}$$",
                'text': r"<strong>Ormavekkan:</strong> Clarke transform 3-phase stationary axes ($a, b, c$) 2-phase stationary orthogonal axes ($\alpha, \beta$)-lekku maattunnu. Park transform stationary frame-ine rotor rotating frame ($d, q$)-lekku maatti AC quantities-ine DC pole constant aakkunnu!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Derivation Guide</span></div>
    <p>1. <strong>Clarke Transform ($abc \to \alpha\beta 0$):</strong> Projects 3-phase sinusoidal quantities separated by $120^\circ$ onto two orthogonal axes $\alpha$ (aligned with $a$) and $\beta$ (at $90^\circ$). Factor $\frac{2}{3}$ maintains amplitude invariant scaling.</p>
    <p>2. <strong>Park Transform ($\alpha\beta \to dq$):</strong> Rotates the coordinate system by angle $\theta$ (rotor flux angle). Direct axis $i_d$ controls flux, Quadrature axis $i_q$ controls torque independently!</p>
    <p>3. <strong>Grand Result:</strong> Induction motor-te complicated sinusoidal AC equations DC machine pole simple linear algebraic equations aayi maarunnu!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru merry-go-round (karousel) karangunnathu purathu ninnu nokkiyaal aalukal aadi thiriyunna AC sine wave pole thonnum (Stationary frame). Pakshe ningalum aa karousel-il kayari irunnaal (Park Rotating frame), koodeyullavan nere munpil oru DC value pole static aayi irikkunnathayi kaanaam! Ithanu Park transform-te magic!</p>
"""
        },
        'ml': {
            'title': "ക്ലാർക്ക്, പാർക്ക് റഫറൻസ് ഫ്രെയിം ട്രാൻസ്ഫോർമേഷനുകൾ തെളിയിക്കുക",
            'remember_this': {
                'title': "⚡ ട്രാൻസ്ഫോർമേഷൻ മാട്രിക്സുകൾ",
                'eq': r"$$abc \xrightarrow{\text{Clarke}} \alpha\beta \xrightarrow{\text{Park}} dq$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 3-ഫേസ് എസി കറന്റുകളെ റൊട്ടേറ്റിംഗ് ഫ്രെയിമിലേക്ക് മാറ്റി ഡിസി പോലെ ലളിതമായി നിയന്ത്രിക്കാൻ സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ഡെറിവേഷൻ</span></div>
    <p>ക്ലാർക്ക് ($2/3$ പ്രൊജക്ഷൻ മാട്രിക്സ്), പാർക്ക് (റൊട്ടേഷൻ മാട്രിക്സ്) എന്നിവ സ്റ്റെപ്പ്-ബൈ-സ്റ്റെപ്പായി എഴുതി $i_d, i_q$ കണ്ടെത്തുക.</p>
</div>
""",
            'understand_simply': r"""
<p>കറങ്ങുന്ന തൊട്ടിലിൽ കയറി ഇരുന്നാൽ കൂടെയുള്ളവർ അനങ്ങാതെ ഇരിക്കുന്നത് പോലെ, എസി തരംഗങ്ങളെ ഡിസി ആക്കി മാറ്റുന്ന വിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q17: Space Vector Pulse Width Modulation (SVPWM)
    # -------------------------------------------------------------------------
    'drive-q17': {
        'manglish': {
            'title': "Space Vector PWM (SVPWM): Principles, 6 Sectors, and Switching Dwell Times detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ SVPWM Sector Dwell Times",
                'eq': r"$$T_1 = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}} \sin\left(\frac{\pi}{3} - \alpha\right), \quad T_2 = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}} \sin(\alpha), \quad T_0 = T_s - T_1 - T_2$$",
                'text': r"<strong>Ormavekkan:</strong> 8 switching states: 6 active vectors ($V_1\text{--}V_6$) spaced $60^\circ$ apart, and 2 zero vectors ($V_0[000], V_7[111]$). Standard SPWM-inekaal 15.5% kooduthal DC bus utilization tharunnu ($V_{\max} = V_{dc}/\sqrt{3}$ vs $V_{dc}/2$)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. Hexagon with 6 sectors of $60^\circ$ each. Reference vector $V_{ref}$ with angle $\alpha$ sits in Sector 1 between $V_1(100)$ and $V_2(110)$.</p>
    <p>2. Volt-second balance: $V_{ref} T_s = V_1 T_1 + V_2 T_2 + V_0 T_0$.</p>
    <p>3. Resolving along axes gives dwell times $T_1$ and $T_2$. Remaining time $T_0$ is split equally between zero states $V_0(000)$ and $V_7(111)$.</p>
    <p>4. Symmetrical switching pattern: $000 \to 100 \to 110 \to 111 \to 110 \to 100 \to 000$ eliminates high harmonic ripples!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru painter 6 primary color paints vechu intermediate colors mix cheyyunnathu pole aanu SVPWM: 2 adjacent voltage vectors-ine oro cheriya samayam ($T_1, T_2$) switch cheythu smooth rotating circle vector undakkunnu. Normal sine PWM-inekaal 15.5% kooduthal voltage car motor-ilottu squeeze cheyyam!</p>
"""
        },
        'ml': {
            'title': "സ്പേസ് വെക്ടർ പിഡബ്ല്യുഎം (SVPWM) തത്വങ്ങളും സ്വിച്ചിംഗ് സമയങ്ങളും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ SVPWM സമവാക്യം",
                'eq': r"$$V_{ref} T_s = V_1 T_1 + V_2 T_2 + V_0 T_0, \quad 15.5\% \text{ കൂടുതൽ വോൾട്ടേജ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 6 സെക്ടറുകളിലായി ആക്ടീവ് വെക്ടറുകളും സീറോ വെക്ടറുകളും സമയബന്ധിതമായി സ്വിച്ച് ചെയ്ത് സ്മൂത്ത് വോൾട്ടേജ് നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഹെക്സാഗൺ ഡയഗ്രം വരച്ച് $T_1, T_2, T_0$ സമയങ്ങളും സിമെട്രിക്കൽ സ്വിച്ചിംഗ് സീക്വൻസും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ബാറ്ററിയിൽ നിന്ന് 15.5% കൂടുതൽ പവർ മോട്ടോറിലേക്ക് എത്തിക്കാൻ സഹായിക്കുന്ന ആധുനിക പിഡബ്ല്യുഎം വിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # drive-q18: Field-Oriented Control (FOC / Vector Control)
    # -------------------------------------------------------------------------
    'drive-q18': {
        'manglish': {
            'title': "Three-Phase Induction Motor-te Field-Oriented Control (FOC / Vector Control) detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Decoupled Flux and Torque in FOC",
                'eq': r"$$\psi_{rq} = 0, \quad \psi_{rd} = \psi_r = L_m i_{sd} \implies \text{Flux control via } i_{sd}, \quad T_e = \frac{3}{2}\frac{P}{2}\frac{L_m}{L_r}\psi_r i_{sq} \implies \text{Torque control via } i_{sq}$$",
                'text': r"<strong>Ormavekkan:</strong> FOC rotor flux vector $\psi_r$-ine direct axis $d$-il align cheyyunnu ($\psi_{rq} = 0$). Ithu kaaranam induction motor direct aayi oru Separately Excited DC motor pole decouple aavunnu &mdash; $i_{sd}$ flux control cheyyunnu, $i_{sq}$ torque control cheyyunnu!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>FOC Architecture Steps:</strong></p>
    <ol>
        <li>Stator currents $i_a, i_b, i_c$ measure cheythu Clarke transform vazhi $i_\alpha, i_\beta$ aakkunnu.</li>
        <li>Rotor flux angle $\theta_e$ use cheythu Park transform vazhi $i_d, i_q$ aakkunnu.</li>
        <li>Alignment condition: Align $d$-axis with rotor flux vector $\implies \psi_{rq} = 0, \;\; \psi_{rd} = \psi_r$.</li>
        <li>Now, flux depends solely on $i_d$: $\psi_r = \frac{L_m i_{sd}}{1 + s \tau_r}$.</li>
        <li>Torque depends linearly on $i_q$: $T_e = \frac{3}{2} \frac{P}{2} \frac{L_m}{L_r} \psi_r i_{sq}$.</li>
        <li>Two independent PI controllers generate $v_d^*, v_q^*$, which undergo Inverse Park and drive the motor via SVPWM!</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Induction motor-te problem enthayirunnu? Speed maattumbol flux-um torque-um thammil thallukoodi kidakkunnu. FOC athine separate cheythu: Oru accelerator pedal flux-inu mathram ($i_d$), matroru pedal torque-inu mathram ($i_q$) aakki maatti! Tesla, Tata EV, high speed trains ellaam run cheyyunnath FOC vechanu!</p>
"""
        },
        'ml': {
            'title': "ഇൻഡക്ഷൻ മോട്ടോറിന്റെ ഫീൽഡ്-ഓറിയന്റഡ് കൺട്രോൾ (വെക്ടർ കൺട്രോൾ) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ഫ്ലക്സ്-ടോർക്ക് വിഭജനം",
                'eq': r"$$\text{ഫ്ലക്സ് } \propto i_{sd}, \quad \text{ടോർക്ക് } \propto i_{sq}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> റോട്ടർ ഫ്ലക്സിനെ $d$-ആക്സിസുമായി അലൈൻ ചെയ്ത് ഇൻഡക്ഷൻ മോട്ടോറിനെ ഡിസി മോട്ടോർ പോലെ സ്വതന്ത്രമായി നിയന്ത്രിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ക്ലാർക്ക്-പാർക്ക് ട്രാൻസ്ഫോർമേഷനുകളും, $\psi_{rq} = 0$ അലൈൻമെന്റും, ഇൻഡിപെൻഡന്റ് കൺട്രോളർ ബ്ലോക്ക് ഡയഗ്രവും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഇൻഡക്ഷൻ മോട്ടോറിനെ ഒരു ഡിസി മോട്ടോർ പോലെ എളുപ്പത്തിൽ കൃത്യമായി നിയന്ത്രിക്കുന്ന ആധുനിക ഇവി വിദ്യ!</p>
"""
        }
    }
}
