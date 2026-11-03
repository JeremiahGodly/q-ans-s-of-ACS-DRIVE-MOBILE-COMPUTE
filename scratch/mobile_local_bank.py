# scratch/mobile_local_bank.py
# Complete Manglish & Malayalam (മലയാളം) Local Explanations for all 38 Mobile Computing questions (CST415).
# Written in friendly Kerala B.Tech campus lecturer & study group tone.

MOBILE_LOCAL_ANSWERS = {
    # -------------------------------------------------------------------------
    # mobile-q1: Middleware Components and Gateways
    # -------------------------------------------------------------------------
    'mobile-q1': {
        'manglish': {
            'title': "Mobile Computing-il Middleware-um Gateways-um enthinaanu use cheyyunnath?",
            'remember_this': {
                'title': "⚡ Core Role & Examples",
                'eq': r"$$\text{Mobile App (Android/iOS)} \longleftrightarrow \text{Middleware} \longleftrightarrow \text{Gateway} \longleftrightarrow \text{Enterprise Server}$$",
                'text': r"<strong>Ormavekkan:</strong> Middleware = Device heterogeneity hide cheyyunna software layer (RPC, caching). Gateway = Protocol mismatch pariharikunna translator (WAP Gateway, SMS Gateway, GGSN)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <h4>1. Middleware:</h4>
    <p>Mobile device OS-ukal (Android, iOS) pala tharathil aayirikkum. Middleware oru software abstraction layer aayi ninnu ee differences hide cheyyunnu. Remote Procedure Call (RPC), data serialization, offline caching, and location queries ithaanu handle cheyyunnath.</p>
    <h4>2. Gateways:</h4>
    <p>Mobile network protocols (eg. WAP, SMS, cellular air interface)-ine backend internet protocols (HTTP, TCP/IP, SQL)-umaayi translate cheyyunna conversion bridge aanu Gateways. Eg: WAP Gateway, SMS Gateway, GPRS GGSN.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru videsha rajyathu travel cheyyunna karyam alochikku: <strong>Middleware</strong> nammude laptop charge cheyyan ulla Universal Power Adapter pole aanu &mdash; enthu socket aayalum adjust cheythu smooth aayi power tharum! <strong>Gateway</strong> airport-le Immigration & Currency Exchange counter pole aanu &mdash; Indian Rupee vangi Dollar aakki tharunnu, language translate cheythu akathottu vidunnu!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ കമ്പ്യൂട്ടിംഗിൽ Middleware-ഉം Gateway-കളും എന്താണ് ചെയ്യുന്നത്?",
            'remember_this': {
                'title': "⚡ പ്രധാന പങ്ക്",
                'eq': r"$$\text{Client (Mobile)} \longleftrightarrow \text{Middleware / Gateway} \longleftrightarrow \text{Server}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> Middleware ഉപകരണങ്ങളുടെ വ്യത്യാസങ്ങൾ മറയ്ക്കുന്നു (Heterogeneity). Gateway വ്യത്യസ്ത പ്രോട്ടോക്കോളുകൾ പരസ്പരം വിവർത്തനം ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <ul>
        <li><strong>Middleware:</strong> വ്യത്യസ്ത മൊബൈൽ ഓപ്പറേറ്റിംഗ് സിസ്റ്റങ്ങൾക്കും സെർവറുകൾക്കും ഇടയിൽ പ്രവർത്തിക്കുന്ന സോഫ്റ്റ്‌വെയർ ലെയർ.</li>
        <li><strong>Gateway:</strong> വയർലെസ് നെറ്റ്‌വർക്ക് പ്രോട്ടോക്കോളുകളെ ഇന്റർനെറ്റ് പ്രോട്ടോക്കോളുകളാക്കി മാറ്റുന്ന വിവർത്തകൻ.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>യൂണിവേഴ്സൽ പവർ അഡാപ്റ്റർ പോലെയാണ് Middleware. എയർപോർട്ടിലെ കറൻസി എക്സ്ചേഞ്ചും ഇമിഗ്രേഷനും പോലെയാണ് Gateway!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q2: The Internet as Ubiquitous Backbone
    # -------------------------------------------------------------------------
    'mobile-q2': {
        'manglish': {
            'title': "Internet enganeyanu mobile computing-te ubiquitous backbone aayi maariyath?",
            'remember_this': {
                'title': "⚡ Universal IP Interconnection",
                'eq': r"$$\text{TCP/IP Stack} \implies \text{Any Device, Any Network, Anywhere}$$",
                'text': r"<strong>Ormavekkan:</strong> Standardized TCP/IP protocol suite cellular (4G/5G), Wi-Fi, and satellite networks-ine single global backbone-umaayi connect cheyyunnu. Cloud computing and web APIs ubiquitous data access tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Standardized Protocol Layer:</strong> Device enthaayalum (iPhone, Android phone, smart watch), uniform TCP/IP protocol vazhi internet-il communicate cheyyaan pattum.</p>
    <p>2. <strong>Global Packet Routing:</strong> Mobile IP and DNS vazhi user travel cheythaalum continuous data sessions maintain cheyyam.</p>
    <p>3. <strong>Cloud Backend:</strong> Storage and heavy computing cloud servers-il distribute cheyyunnu.</p>
</div>
""",
            'understand_simply': r"""
<p>Internet oru national highway network pole aanu: Car, bus, lorry, cycle &mdash; enthu vandi aayalum ore tar road vazhi travel cheyyunnathu pole, Wi-Fi, 4G, 5G ellaam internet enna global highway-ilekku connect aavunnu!</p>
"""
        },
        'ml': {
            'title': "ഇന്റർനെറ്റ് എങ്ങനെയാണ് മൊബൈൽ കമ്പ്യൂട്ടിംഗിന്റെ ആഗോള നട്ടെല്ലായി മാറിയത്?",
            'remember_this': {
                'title': "⚡ ആഗോള ഐപി ശൃംഖല",
                'eq': r"$$\text{TCP/IP പ്രോട്ടോക്കോൾ വഴി ഏത് നെറ്റ്‌വർക്കും പരസ്പരം ബന്ധിപ്പിക്കുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 4G, 5G, വൈ-ഫൈ തുടങ്ങിയ ഏത് നെറ്റ്‌വർക്കിലും ഇന്റർനെറ്റ് പ്രോട്ടോക്കോൾ വഴിയാണ് വിവരങ്ങൾ കൈമാറുന്നത്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>യൂണിഫോം TCP/IP പ്രോട്ടോക്കോളും ക്ലൗഡ് കമ്പ്യൂട്ടിംഗും ചേർന്നാണ് ലോകമെമ്പാടും മൊബൈൽ കണക്റ്റിവിറ്റി സാധ്യമാക്കുന്നത്.</p>
</div>
""",
            'understand_simply': r"""
<p>ഏത് വാഹനത്തിനും ഒരേ ദേശീയ പാതയിലൂടെ സഞ്ചരിക്കാമെന്നത് പോലെ എല്ലാ മൊബൈൽ ഡാറ്റയും ഇന്റർനെറ്റിലൂടെ സഞ്ചരിക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q3: Network Segmentation (Core, Edge, Access)
    # -------------------------------------------------------------------------
    'mobile-q3': {
        'manglish': {
            'title': "Mobile network segmentation (Core, Edge, and Access Networks) explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 3-Tier Network Hierarchy",
                'eq': r"$$\text{User Device} \longleftrightarrow \text{Access Network (RAN)} \longleftrightarrow \text{Edge Network (MEC)} \longleftrightarrow \text{Core Network (EPC/5GC)}$$",
                'text': r"<strong>Ormavekkan:</strong> Access = Radio towers (gNodeB/eNodeB) connecting phones; Edge = Low-latency compute closer to base stations; Core = High-speed routing, subscriber authentication, and billing."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Access Network (RAN):</strong> Base stations (BTS/NodeB/gNodeB) and towers that provide radio frequency air interface to user devices.</li>
        <li><strong>2. Edge Network (MEC):</strong> Data centers located close to cell towers to execute AI and video caching with ultra-low latency (&lt;5 ms).</li>
        <li><strong>3. Core Network:</strong> Central high-speed brain (SGW, PGW, HSS, UPF) responsible for mobility management, authentication, and internet routing.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Amazon delivery network pole aanu: Access network delivery boy pole aanu (user-te veettilekku ethikkunnu). Edge network local district warehouse pole aanu (pettennu deliver cheyyan). Core network central head office pole aanu (billing and order tracking)!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ നെറ്റ്‌വർക്ക് സെഗ്മെന്റേഷൻ (Core, Edge, Access) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 3 നെറ്റ്‌വർക്ക് ലെയറുകൾ",
                'eq': r"$$\text{Access (ടവർ) } \to \text{ Edge (ഡാറ്റാ സെന്റർ) } \to \text{ Core (ഹെഡ് ഓഫീസ്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ആക്സസ് നെറ്റ്‌വർക്ക് ഫോണുകളിലേക്ക് റേഡിയോ സിഗ്നൽ നൽകുന്നു; എഡ്ജ് വേഗത കൂട്ടുന്നു; കോർ നെറ്റ്‌വർക്ക് സെർവറുകളിലേക്ക് എത്തിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>റേഡിയോ ആക്സസ്, എഡ്ജ് കമ്പ്യൂട്ടിംഗ്, കോർ നെറ്റ്‌വർക്ക് എന്നിവയുടെ റോളുകൾ വ്യക്തമായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഡെലിവറി ബോയ് (ആക്സസ്), ലോക്കൽ വെയർഹൗസ് (എഡ്ജ്), ഹെഡ് ഓഫീസ് (കോർ) എന്നിവ ചേർന്ന സംവിധാനം പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q4: Intrinsic Physical Limitations of Mobile Computing
    # -------------------------------------------------------------------------
    'mobile-q4': {
        'manglish': {
            'title': "Mobile Computing-te intrinsic physical limitations enthokke aanu?",
            'remember_this': {
                'title': "⚡ 4 Major Bottlenecks",
                'eq': r"$$\text{Battery Power, Wireless Bandwidth, High Latency \& Jitter, Security Risks}$$",
                'text': r"<strong>Ormavekkan:</strong> Desktop computers-ine kaal mobile devices-il 4 natural constraints undu: Limited battery life, fluctuating radio bandwidth, frequent disconnections during mobility, and broadcast vulnerability to eavesdropping."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Battery Power Limitation:</strong> Battery capacity chemical limits ulla karyamaanu; heavy computation battery drains quickly.</li>
        <li><strong>2. Bandwidth & Variable Channel:</strong> Multipath fading, weather, and distance from cell tower make bandwidth dynamic.</li>
        <li><strong>3. Intermittent Disconnections:</strong> Underground tunnels, elevators, and cell handovers cause packet drops.</li>
        <li><strong>4. Physical Security:</strong> Devices easily lost or stolen; wireless air interface open to packet sniffing.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Desktop PC direct plug-il unlimited power-um optic fiber cable-um vechu work cheyyunnu. Pakshe mobile phone backpack-il battery vechu travel cheyyunna yatrikan pole aanu &mdash; energy sookshichu use cheyyanam, network signal ethaanum marayum!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ കമ്പ്യൂട്ടിംഗിന്റെ സ്വാഭാവികമായ പരിമിതികൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ 4 പ്രധാന പരിമിതികൾ",
                'eq': r"$$\text{ബാറ്ററി, ബാൻഡ്‌വിഡ്ത്ത്, തടസ്സങ്ങൾ, സുരക്ഷ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പരിമിതമായ ബാറ്ററി ലൈഫ്, തരംഗങ്ങളുടെ ഏറ്റക്കുറച്ചിലുകൾ, അടിക്കടിയുള്ള കണക്ഷൻ നഷ്ടങ്ങൾ, സുരക്ഷാ ഭീഷണികൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ബാറ്ററി, വേരിയബിൾ റേഡിയോ ചാനൽ, ഡിസ്കണക്ഷൻ, സെക്യൂരിറ്റി എന്നിവ 4 പോയിന്റുകളായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഡെസ്ക്ടോപ്പ് കമ്പ്യൂട്ടറുകളെ അപേക്ഷിച്ച് മൊബൈലിൽ ബാറ്ററിയും നെറ്റ്‌വർക്കും പരിമിതമായിരിക്കും!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q5: Three-Tier Architecture of Mobile Computing
    # -------------------------------------------------------------------------
    'mobile-q5': {
        'manglish': {
            'title': "Mobile Computing-te Three-Tier Architecture detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 3-Tier Layered Model",
                'eq': r"$$\text{Tier 1: Presentation (Client GUI)} \longleftrightarrow \text{Tier 2: Application / Business Logic} \longleftrightarrow \text{Tier 3: Database / Enterprise Store}$$",
                'text': r"<strong>Ormavekkan:</strong> Tier-1 UI render cheyyunnu (Thin client); Tier-2 heavy processing and authentication cheyyunnu; Tier-3 databases and transactions preserve cheyyunnu (ACID properties)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>Tier 1: Presentation Tier (Client Layer):</strong> User interface rendered on mobile handset (HTML5, Flutter, Swift, React Native). Captures user inputs and displays results.</li>
        <li><strong>Tier 2: Application Tier (Business Logic):</strong> Runs on middle application servers. Executes business algorithms, data validation, encryption, session management, and transacting.</li>
        <li><strong>Tier 3: Data Tier (Enterprise Backend):</strong> High-reliability relational / NoSQL databases (Oracle, PostgreSQL, MongoDB, Mainframe) storing master subscriber records and transactions.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru restaurant alochichu nokku: <strong>Tier 1</strong> dining table & menu card (Client UI). <strong>Tier 2</strong> kitchen-le chef (order eduthu paachakam cheyyunnu). <strong>Tier 3</strong> store room & refrigerator (raw materials and groceries store cheyyunnu)!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ കമ്പ്യൂട്ടിംഗിന്റെ ത്രീ-ടയർ (3-Tier) ആർക്കിടെക്ചർ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 3-ടയർ മോഡൽ",
                'eq': r"$$\text{ടയർ 1: പ്രസന്റേഷൻ } \to \text{ ടയർ 2: ആപ്ലിക്കേഷൻ ലോജിക് } \to \text{ ടയർ 3: ഡാറ്റാബേസ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> യൂസർ ഇന്റർഫേസ്, ബിസിനസ്സ് ലോജിക്, ഡാറ്റാബേസ് എന്നിവയെ 3 തട്ടുകളായി തിരിച്ച് ഭാരം കുറയ്ക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>3 ടയറുകളുടെയും ബ്ലോക്ക് ഡയഗ്രം വരച്ച് അവ തമ്മിലുള്ള ഡാറ്റാ കൈമാറ്റം വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു റെസ്റ്റോറന്റിലെ ഡൈനിംഗ് ടേബിൾ (ടയർ 1), അടുക്കളയിലെ ഷെഫ് (ടയർ 2), സ്റ്റോർ റൂം (ടയർ 3) പോലെയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q6: Design Considerations for Mobile Computing
    # -------------------------------------------------------------------------
    'mobile-q6': {
        'manglish': {
            'title': "Mobile Computing systems design cheyyumbol nokkenda main considerations enthokke aanu?",
            'remember_this': {
                'title': "⚡ 5 Key Design Pillars",
                'eq': r"$$\text{Context Awareness, Thin Client Architecture, Offline Caching, Bandwidth Conservation, Power Efficiency}$$",
                'text': r"<strong>Ormavekkan:</strong> Energy-efficient algorithms, asynchronous RPC, screen resolution adaptation, delta data synchronization, and end-to-end security protocols."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Power Conservation:</strong> CPU sleeping states optimize cheyyuka, continuous background GPS polling thadayuka.</li>
        <li><strong>2. Bandwidth Optimization:</strong> Heavy image/video compression, sending only changed delta records instead of full database.</li>
        <li><strong>3. Disconnection Handling:</strong> Offline local SQLite database caching; network thirichu varumbol auto-sync.</li>
        <li><strong>4. User Interface Adaptability:</strong> Dynamic responsive UI for diverse screen sizes, orientations, and touch inputs.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>WhatsApp alochikku: Airplane mode-il polum message type cheythu 'Send' adikkaam (Offline caching). Internet varumbol tick mark aavum (Sync). Profile photos auto-compress cheythu data labhikkunnu &mdash; ithellam mobile design considerations aanu!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ സിസ്റ്റങ്ങൾ രൂപകൽപ്പന ചെയ്യുമ്പോൾ ശ്രദ്ധിക്കേണ്ട പ്രധാന കാര്യങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ ഡിസൈൻ തത്വങ്ങൾ",
                'eq': r"$$\text{ഡാറ്റാ കംപ്രഷൻ, ഓഫ്‌ലൈൻ കാഷിംഗ്, കുറഞ്ഞ ബാറ്ററി ഉപയോഗം}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> നെറ്റ്‌വർക്ക് ഇല്ലാത്തപ്പോഴും പ്രവർത്തിക്കാനും, കുറഞ്ഞ ഡാറ്റയും ബാറ്ററിയും ഉപയോഗിക്കാനും കഴിയണം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ബാറ്ററി സംരക്ഷണം, ബാൻഡ്‌വിഡ്ത്ത് കംപ്രഷൻ, ഓഫ്‌ലൈൻ സിൻക്രൊണൈസേഷൻ, യുഐ അഡാപ്റ്റേഷൻ എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>നെറ്റ്‌വർക്ക് പോയാലും വാട്സാപ്പിൽ മെസ്സേജ് അയച്ചു വെക്കാനും കണക്റ്റിവിറ്റി വരുമ്പോൾ ഓട്ടോമാറ്റിക്കായി സെൻഡ് ആവാനും സഹായിക്കുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q7: Context-Aware System Management
    # -------------------------------------------------------------------------
    'mobile-q7': {
        'manglish': {
            'title': "Context-Aware System Management in Mobile Computing explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 4 Context Dimensions",
                'eq': r"$$\text{Context} = \{\text{Location, Identity, Activity, Time/Environment}\}$$",
                'text': r"<strong>Ormavekkan:</strong> User-te current surroundings (GPS location, movement speed, ambient light, network status) sense cheythu app behavior automatically adapt cheyyunna smart system."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Context Sourcing:</strong> Hardware sensors (GPS, Accelerometer, Gyroscope, Ambient Light sensor) and software context (Calendar, battery level, Wi-Fi SSID).</p>
    <p>2. <strong>Context Abstraction & Reasoning:</strong> Raw sensor coordinates $(lat, long)$-ine semantic context ('At College' or 'Driving a Car') aakki translate cheyyunnu.</p>
    <p>3. <strong>Context Adaptation:</strong> Driving mode auto-trigger cheyyuka, night time-il dark theme switch cheyyuka, battery low aavumbol location polling frequency kurakkuka.</p>
</div>
""",
            'understand_simply': r"""
<p>Google Maps alochikku: Vandi odikkumbol automatic aayi 'Driving' mode aavunnu, tunnel-il kayarumbol Dark mode aavunnu, night aavumbol screen dimmer aavunnu &mdash; user parayathe thanne surroundings manasilakki app adjust cheyyunnathaanu Context Awareness!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ കമ്പ്യൂട്ടിംഗിലെ കോൺടെക്സ്റ്റ്-അവയർ (Context-Aware) മാനേജ്മെന്റ് വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ കോൺടെക്സ്റ്റ് ഘടകങ്ങൾ",
                'eq': r"$$\text{ലൊക്കേഷൻ, സമയം, ആക്റ്റിവിറ്റി, പരിസ്ഥിതി}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഉപഭോക്താവിന്റെ ചുറ്റുപാടുകൾ സെൻസറുകൾ വഴി മനസ്സിലാക്കി ആപ്പുകൾ സ്വയം ക്രമീകരിക്കുന്നു (ഡ്രൈവിംഗ് മോഡ്, ഡാർക്ക് തീം)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സെൻസറുകൾ വഴി വിവരങ്ങൾ ശേഖരിക്കുന്നതും, വിശകലനം ചെയ്യുന്നതും, അതനുസരിച്ച് ആപ്പുകൾ മാറുന്നതും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>രാത്രിയാകുമ്പോൾ ഫോൺ സ്വയം ഡാർക്ക് മോഡിലേക്കും, വാഹനം ഓടിക്കുമ്പോൾ ഡ്രൈവിംഗ് മോഡിലേക്കും മാറുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q8: Content Adaptation and Transcoding
    # -------------------------------------------------------------------------
    'mobile-q8': {
        'manglish': {
            'title': "Content Adaptation-um Transcoding techniques-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Transcoding Classifications",
                'eq': r"$$\text{Format Conversion, Spatial Scaling, Color Depth Reduction, Semantic Compression}$$",
                'text': r"<strong>Ormavekkan:</strong> High-bandwidth desktop media content (4K video, heavy PNGs)-ine mobile screen size-num network speed-num thakkavannam proxy gateway-il vechu convert cheyyunnathaanu transcoding."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Spatial Scaling (Resolution reduction):</strong> 4K/1080p images-ne 360p or 480p mobile screen display-lekku downscale cheyyunnu.</li>
        <li><strong>2. Format Transcoding:</strong> Heavy BMP/TIFF images-ne WebP or JPEG aakki maattunnu; WAV audio-ne AAC/MP3 aakkunnu.</li>
        <li><strong>3. Color Depth Reduction:</strong> 24-bit true color-ine 8-bit or grayscale aakki file size 70% kuraykkunnu.</li>
        <li><strong>4. Semantic Content Adaptation:</strong> Mobile screen-il flash animations remove cheythu plain text and static thumbnail aakki maattunnu.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>YouTube adaptive streaming nokku: Nalla Wi-Fi ullapol 1080p full clarity-il varum. Travel cheythu train tunnel-il ethumbol buffering aavathe automatic aayi 360p or 240p-ilottu resolution kurachu smooth aayi play aavunnu &mdash; ithaanu Content Adaptation!</p>
"""
        },
        'ml': {
            'title': "കണ്ടന്റ് അഡാപ്റ്റേഷനും ട്രാൻസ്കോഡിംഗും (Transcoding) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ട്രാൻസ്കോഡിംഗ് രീതികൾ",
                'eq': r"$$\text{റെസൊല്യൂഷൻ മാറ്റം, ഫോർമാറ്റ് മാറ്റം, കളർ ഡെപ്ത് കുറയ്ക്കൽ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> മൊബൈൽ സ്ക്രീനിനും ഇന്റർനെറ്റ് സ്പീഡിനും അനുയോജ്യമായ രീതിയിൽ മീഡിയ ഫയലുകൾ ചെറുതാക്കി മാറ്റുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>റെസൊല്യൂഷൻ മാറ്റം, ഫോർമാറ്റ് മാറ്റം, കളർ കുറയ്ക്കൽ എന്നിവ ഉദാഹരണ സഹിതം എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>യൂട്യൂബിൽ ഇന്റർനെറ്റ് സ്പീഡ് കുറയുമ്പോൾ തനിയെ ക്വാളിറ്റി കുറഞ്ഞ് വീഡിയോ മുടങ്ങാതെ ഓടുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q9: Seamless Communication and Roaming Facets
    # -------------------------------------------------------------------------
    'mobile-q9': {
        'manglish': {
            'title': "Roaming time-il Seamless Communication maintain cheyyunna facets enthokke aanu?",
            'remember_this': {
                'title': "⚡ 3 Core Mobility Facets",
                'eq': r"$$\text{Session Continuity, Location Transparency, QoS \& Security Continuity}$$",
                'text': r"<strong>Ormavekkan:</strong> User oru cell tower-il ninnu matroru network-ilottu move cheythaalum: Phone call cut aavalle (Handover), subscriber-te address maaralle (Location update), encrypted communication interrupt aavalle."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>Location Transparency:</strong> Caller-nu subscriber evideyaanu ennu ariyenda karyamilla; HLR and VLR automatically locate cheythu call route cheyyum.</li>
        <li><strong>Session Continuity:</strong> Active voice call or TCP data stream break aavathe seamless seamless soft/hard handover nadakkunnu.</li>
        <li><strong>Service Uniformity:</strong> Roaming network-ilum caller ID, SMS, and VoLTE services home network pole thanne execute aavunnu.</li>
        <li><strong>Security Continuity:</strong> Authentication vectors (RAND, SRES, $K_c$) home HLR/AuC-il ninnu foreign VLR-lekku secure aayi transfer cheyyunnu.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>KSRTC bus-il irunnu WhatsApp call cheythu travel cheyyunna karyam alochikku: Bus 100 km travel cheythu 20 towers maaripoyaalum call disconnect aavilla, friend-te screen-il cut aavathe sound continuous aayi kelkkam &mdash; ithaanu Seamless Mobility!</p>
"""
        },
        'ml': {
            'title': "റോമിംഗ് സമയത്ത് സുഗമമായ ആശയവിനിമയം (Seamless Communication) നിലനിർത്തുന്ന ഘടകങ്ങൾ ഏവ?",
            'remember_this': {
                'title': "⚡ മൊബിലിറ്റി ഘടകങ്ങൾ",
                'eq': r"$$\text{സെഷൻ കണ്ടിന്യൂയിറ്റി, ലൊക്കേഷൻ സുതാര്യത, സുരക്ഷ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> യാത്ര ചെയ്യുമ്പോൾ ടവറുകൾ മാറിയാലും കോൾ കട്ടാവാതെയും ഡാറ്റാ നഷ്ടപ്പെടാതെയും സൂക്ഷിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ലൊക്കേഷൻ അപ്‌ഡേറ്റ്, ഹാൻഡ്ഓവർ, സർവ്വീസ് തുല്യത എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>യാത്ര ചെയ്യുമ്പോൾ എത്ര ടവറുകൾ മാറിയാലും സംസാരിക്കുന്ന ഫോൺ കോൾ കട്ടാവാതെ നിൽക്കുന്ന മാജിക്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q10: Satellite Systems Comparison (GEO, LEO, MEO)
    # -------------------------------------------------------------------------
    'mobile-q10': {
        'manglish': {
            'title': "Satellite communication systems: GEO, LEO, and MEO compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Satellite Orbit Altitude & Latency",
                'eq': r"$$\text{LEO: } 500\text{--}1500\text{ km } (20\text{--}40\text{ ms}); \;\; \text{MEO: } 5000\text{--}12000\text{ km } (100\text{--}150\text{ ms}); \;\; \text{GEO: } 35786\text{ km } (\sim 250\text{ ms})$$",
                'text': r"<strong>Ormavekkan:</strong> GEO: 3 satellites give global coverage, high latency (TV broadcast). LEO: Starlink pole thousands of satellites, ultra-low latency, high handover frequency (High-speed internet)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Parameter</th><th>LEO (Low Earth Orbit)</th><th>MEO (Medium Earth Orbit)</th><th>GEO (Geostationary Orbit)</th></tr></thead>
        <tbody>
            <tr><td><strong>Altitude</strong></td><td>$500\text{--}1,500\text{ km}$</td><td>$5,000\text{--}12,000\text{ km}$</td><td>$35,786\text{ km}$</td></tr>
            <tr><td><strong>Round-trip Latency</strong></td><td>Very low ($20\text{--}40\text{ ms}$)</td><td>Moderate ($100\text{--}150\text{ ms}$)</td><td>High ($\approx 250\text{ ms}$ delay)</td></tr>
            <tr><td><strong>Satellites for Global Cover</strong></td><td>Constellation of 50 to thousands</td><td>10 to 24 satellites</td><td>Just 3 satellites spaced $120^\circ$ apart!</td></tr>
            <tr><td><strong>Handover & Tracking</strong></td><td>Frequent handovers (satellites move fast)</td><td>Moderate handovers</td><td>No handovers (Stationary relative to Earth)</td></tr>
            <tr><td><strong>Applications</strong></td><td>Starlink broadband, OneWeb, Earth imaging</td><td>GPS navigation, GLONASS, Galileo</td><td>DTH TV (Tata Play), Weather forecasting</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Street light vs Moon alochikku: GEO oru chanthiran pole aanu &mdash; valare mukalil aanu, 3 aalukal ninnu motham bhoomiye kaanam, pakshe light ethitt thirichu varan samayam edukkkum (High delay). LEO street lights pole aanu &mdash; thazheyaanu, vegam signal ethum (Low latency), pakshe thousands of lights venam (Starlink)!</p>
"""
        },
        'ml': {
            'title': "ഉപഗ്രഹ വിനിമയ സംവിധാനങ്ങൾ: GEO, LEO, MEO എന്നിവ താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ ഉപഗ്രഹ താരതമ്യം",
                'eq': r"$$\text{GEO (35,786 km - ടിവി)}, \quad \text{MEO (GPS)}, \quad \text{LEO (സ്റ്റാർലിങ്ക്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> LEO കുറഞ്ഞ ഉയരവും ലേറ്റൻസിയും നൽകുന്നു; GEO ഉയർന്ന ഉയരത്തിൽ 3 ഉപഗ്രഹങ്ങൾ കൊണ്ട് ആഗോള കവറേജ് നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ ഉയരം, ലേറ്റൻസി, ഉപഗ്രഹങ്ങളുടെ എണ്ണം, ആപ്ലിക്കേഷനുകൾ എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ചന്ദ്രനെപ്പോലെ ഉയരത്തിൽ നിൽക്കുന്നതാണ് GEO; അടുത്തുകൂടി അതിവേഗം കറങ്ങുന്നതാണ് ഇന്റർനെറ്റ് നൽകുന്ന സ്റ്റാർലിങ്ക് LEO!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q11: Mobile Station Identifiers (IMEI, IMSI, MSISDN, TMSI)
    # -------------------------------------------------------------------------
    'mobile-q11': {
        'manglish': {
            'title': "Cellular mobile identifiers: IMEI, IMSI, MSISDN, and TMSI detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 4 Cellular Identifiers",
                'eq': r"$$\text{IMEI: Handset (15 digits)}, \;\; \text{IMSI: SIM Card (15 digits)}, \;\; \text{MSISDN: Phone Number}, \;\; \text{TMSI: Temporary Privacy}$$",
                'text': r"<strong>Ormavekkan:</strong> IMEI device-te identity aanu (*#06#); IMSI SIM-inte global ID aanu; MSISDN aalukal dial cheyyunna mobile number aanu; TMSI air interface-il eavesdropper-il ninnu IMSI hide cheyyan ulla temporary code aanu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>IMEI (International Mobile Equipment Identity):</strong> 15-digit unique hardware serial number burnt into handset. Stored in EIR (White, Gray, Black lists for stolen tracking).</li>
        <li><strong>IMSI (International Mobile Subscriber Identity):</strong> 15-digit unique identity stored inside SIM chip (MCC + MNC + MSIN). Secretly identifies subscriber in HLR.</li>
        <li><strong>MSISDN (Mobile Station ISDN Number):</strong> Nammal dial cheyyunna ordinary telephone number (CC + NDC + SN, eg. +91 98470XXXXX).</li>
        <li><strong>TMSI (Temporary Mobile Subscriber Identity):</strong> Random temporary number assigned by VLR. Transmitted over radio channels to prevent eavesdroppers from tracking user's true IMSI.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru person-te identity nokkiyaal: <strong>IMEI</strong> ningalude Fingerprint pole aanu (physical body). <strong>IMSI</strong> ningalude Aadhaar Card number pole aanu (permanent secret ID). <strong>MSISDN</strong> ningalude pet name / calling name pole aanu (friends vilikkan use cheyyunnu). <strong>TMSI</strong> bank token number pole aanu (privacy-kku vendi token number mathram vilikkunnu)!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ ഐഡന്റിഫയറുകൾ: IMEI, IMSI, MSISDN, TMSI എന്നിവ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 4 ഐഡന്റിഫയറുകൾ",
                'eq': r"$$\text{IMEI (ഫോൺ)}, \quad \text{IMSI (സിം കാർഡ്)}, \quad \text{MSISDN (ഫോൺ നമ്പർ)}, \quad \text{TMSI (രഹസ്യ കോഡ്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> IMEI ഫോണിനെയും, IMSI സിം കാർഡിനെയും, MSISDN ഡയൽ ചെയ്യുന്ന നമ്പറിനെയും, TMSI സുരക്ഷാ രഹസ്യ നമ്പറിനെയും സൂചിപ്പിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>4 ഐഡന്റിഫയറുകളുടെയും ഘടനയും ഉപയോഗങ്ങളും വ്യക്തമായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഫിംഗർപ്രിന്റ് (IMEI), ആധാർ നമ്പർ (IMSI), വിളിക്കുന്ന പേര് (MSISDN), ബാങ്ക് ടോക്കൺ നമ്പർ (TMSI) പോലെയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q12: Call Progress Indication Mechanisms
    # -------------------------------------------------------------------------
    'mobile-q12': {
        'manglish': {
            'title': "Cellular telephony-il Call Progress Indication mechanisms enganeyaanu work cheyyunnath?",
            'remember_this': {
                'title': "⚡ Acoustic Tones & Digital Status Codes",
                'eq': r"$$\text{Dial Tone} \to \text{Ringback Tone (400 Hz)} \to \text{Busy Tone (480 Hz)} \to \text{Network Congestion / Fast Busy}$$",
                'text': r"<strong>Ormavekkan:</strong> Calling party-kku call setup status ariyikkan audible acoustic tones-um digital screen signaling messages-um (ISUP Call Progress CPG, Alerting, Connect) generate cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Dial Tone:</strong> Exchange ready to accept digits (continuous tone).</li>
        <li><strong>2. Ringback Tone (RBT):</strong> Informs caller that called mobile is ringing (intermittent tone: 0.4s on, 0.2s off, etc.).</li>
        <li><strong>3. Busy Tone:</strong> Called subscriber is already engaged on another call (fast rhythmic tone).</li>
        <li><strong>4. Congestion / Reorder Tone (Fast Busy):</strong> Radio network or trunk lines are overloaded; no voice channel available.</li>
        <li><strong>5. Recorded Voice Announcements:</strong> 'Subscriber is currently switched off or out of coverage area' (Triggered when VLR returns IMSI detached).</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Oru friend-ine phone vilikkumbol cheviyil kelkkunna rhythmic sounds aanu Call Progress: First oru click, pinne 'trrr-trrr' ring sound, friend busy aaneel beep-beep busy tone, or network switch-off announcement &mdash; call enth stage-il ethittundu ennu ee signals vazhi namukku ariyaam!</p>
"""
        },
        'ml': {
            'title': "സെല്ലുലാർ ഫോണിലെ കോൾ പ്രോഗ്രസ് ഇൻഡിക്കേഷൻ രീതികൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പ്രധാന ടോണുകൾ",
                'eq': r"$$\text{റിംഗ് ബാക്ക് ടോൺ, ബിസി ടോൺ, കൺജഷൻ ടോൺ, വോയ്സ് അനൗൺസ്മെന്റ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> കോൾ കണക്റ്റ് ആകുന്നതിന്റെ ഓരോ ഘട്ടങ്ങളും ഉപഭോക്താവിനെ അറിയിക്കുന്ന സിഗ്നലുകൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡയൽ ടോൺ, റിംഗ്ബാക്ക് ടോൺ, ബിസി ടോൺ, നെറ്റ്‌വർക്ക് തകരാർ അറിയിപ്പുകൾ എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>നമ്മൾ ഫോൺ വിളിക്കുമ്പോൾ കേൾക്കുന്ന റിംഗ് സൗണ്ട്, ബിസി സൗണ്ട്, സ്വിച്ച്ഡ് ഓഫ് അനൗൺസ്മെന്റുകൾ എന്നിവയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q13: Multiple Access Procedures (FDMA, TDMA, CDMA, SDMA)
    # -------------------------------------------------------------------------
    'mobile-q13': {
        'manglish': {
            'title': "Cellular-il FDMA, TDMA, CDMA, SDMA procedures detail aayi compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Multiple Access Domains",
                'eq': r"$$\text{FDMA: Frequency Slicing (1G)}, \;\; \text{TDMA: Time Slots (2G GSM)}, \;\; \text{CDMA: Orthogonal Codes (3G)}, \;\; \text{SDMA: Smart Beams (5G)}$$",
                'text': r"<strong>Comparison:</strong> FDMA divides spectrum into channels; TDMA divides channels into time slots; CDMA shares full spectrum simultaneously via unique mathematical codes; SDMA focuses narrow radio beams in physical space."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Technique</th><th>Division Domain</th><th>Channel Sharing</th><th>Guard Requirement</th><th>Standard</th></tr></thead>
        <tbody>
            <tr><td><strong>FDMA</strong></td><td>Frequency</td><td>Dedicated frequency per user</td><td>Guard bands between channels</td><td>1G AMPS</td></tr>
            <tr><td><strong>TDMA</strong></td><td>Time</td><td>Dedicated time slot on shared carrier</td><td>Guard time between slots</td><td>2G GSM</td></tr>
            <tr><td><strong>CDMA</strong></td><td>Mathematical Code</td><td>All users share full bandwidth simultaneously</td><td>Orthogonal codes (Walsh codes)</td><td>3G UMTS, cdmaOne</td></tr>
            <tr><td><strong>SDMA</strong></td><td>Spatial Location</td><td>Directional smart antenna beams</td><td>Spatial angular separation</td><td>4G / 5G Massive MIMO</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Oru hall-il pala aalukal samsarikkan irikkunna meeting alochikku:</p>
<ul>
    <li><strong>FDMA:</strong> Oro aalkkum separate small soundproof rooms kodukkunnu (Frequency).</li>
    <li><strong>TDMA:</strong> Ellaavarum ore mic-il oro minute maarimaari samsarikkunnu (Time).</li>
    <li><strong>CDMA:</strong> Ellaavarum ore samayam samsarikkunnu, oral Malayalam, oral English, oral French &mdash; kelkkunnavar avarkkulla language matram decode cheythu kelkkunnu (Code)!</li>
    <li><strong>SDMA:</strong> Parayunnavarude mukhathekku directional beam microphone target cheyyunnu (Space).</li>
</ul>
"""
        },
        'ml': {
            'title': "സെല്ലുലാർ മൾട്ടിപ്പിൾ ആക്സസ് രീതികൾ (FDMA, TDMA, CDMA, SDMA) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 4 മൾട്ടിപ്പിൾ ആക്സസ് രീതികൾ",
                'eq': r"$$\text{FDMA (ഫ്രീക്വൻസി), TDMA (സമയം), CDMA (കോഡ്), SDMA (സ്ഥലം)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഒരേ എയർ സ്പേസ് ഒരുപാട് ആളുകൾ തമ്മിൽ വീതിച്ചെടുക്കാനുള്ള 4 സാങ്കേതിക വിദ്യകൾ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ ഡിവിഷൻ രീതി, ചാനൽ ഷെയറിംഗ്, ഗാർഡ് ബാൻഡ്, ജനറേഷൻ എന്നിവ താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു മുറിയിൽ പലർ സംസാരിക്കുമ്പോൾ മുറികൾ തിരിക്കുന്നതും (FDMA), ഊഴം വെക്കുന്നതും (TDMA), പല ഭാഷകളിൽ സംസാരിക്കുന്നതും (CDMA) പോലെയാണിത്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q14: Comprehensive GSM Architecture
    # -------------------------------------------------------------------------
    'mobile-q14': {
        'manglish': {
            'title': "GSM Network Architecture-nte complete subsystems-um interfaces-um detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 3 Core GSM Subsystems",
                'eq': r"$$\text{MS} \overset{U_m}{\longleftrightarrow} \text{BSS [BTS } \overset{A_{bis}}{\leftrightarrow} \text{BSC]} \overset{A}{\longleftrightarrow} \text{NSS [MSC, HLR, VLR, AuC, EIR]} \longleftrightarrow \text{OSS [OMC]}$$",
                'text': r"<strong>Ormavekkan:</strong> MS = Mobile Station; BSS = Radio transmission (BTS + BSC); NSS = Call switching and mobility databases (MSC, HLR, VLR, AuC, EIR); OSS = Operation & maintenance."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Subsystem Breakdown:</strong></p>
    <ol>
        <li><strong>BSS (Base Station Subsystem):</strong>
            <ul>
                <li><strong>BTS (Base Transceiver Station):</strong> Tower radio antennas, channel coding, signal transmission over $U_m$ air interface.</li>
                <li><strong>BSC (Base Station Controller):</strong> Radio channel allocation, frequency hopping, and handover control for 20-30 BTS units. Connected via $A_{bis}$ interface.</li>
            </ul>
        </li>
        <li><strong>NSS (Network & Switching Subsystem):</strong>
            <ul>
                <li><strong>MSC (Mobile Switching Center):</strong> Telephone exchange for call setup and routing via $A$ interface.</li>
                <li><strong>HLR (Home Location Register):</strong> Master database storing permanent subscriber profile and current VLR location.</li>
                <li><strong>VLR (Visitor Location Register):</strong> Temporary local database for subscribers roaming in this MSC area.</li>
                <li><strong>AuC (Authentication Center):</strong> Generates triplets (RAND, SRES, $K_c$) for cryptographic authentication.</li>
                <li><strong>EIR (Equipment Identity Register):</strong> Tracks handset IMEI against stolen blacklists.</li>
            </ul>
        </li>
        <li><strong>OSS (Operation Support Subsystem):</strong> OMC monitors network traffic, fault logs, and performance metrics.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>GSM network oru post office system pole aanu: Handset aanu letter. Mobile tower (BSS) aanu local post box. MSC aanu main district sorting center. HLR aanu ningalude permanent ration card. VLR aanu hotel-il check-in cheyyumbol ezhutunna temporary register. AuC signature verify cheyyunna officer aanu!</p>
"""
        },
        'ml': {
            'title': "GSM നെറ്റ്‌വർക്ക് ആർക്കിടെക്ചർ പൂർണ്ണമായി വിശദീകരിക്കുക (BSS, NSS, OSS)",
            'remember_this': {
                'title': "⚡ 3 പ്രധാന സബ്സിസ്റ്റങ്ങൾ",
                'eq': r"$$\text{MS (ഫോൺ) } \to \text{ BSS (ടവർ) } \to \text{ NSS (സ്വിച്ചിംഗ്) } \to \text{ OSS (കൺട്രോൾ)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> BSS റേഡിയോ സിഗ്നലും, NSS കോൾ സ്വിച്ചിംഗും ഡാറ്റാബേസുകളും, OSS നെറ്റ്‌വർക്ക് നിരീക്ഷണവും നിർവ്വഹിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ആർക്കിടെക്ചർ ഗൈഡ്</span></div>
    <p>ആർക്കിടെക്ചർ ഡയഗ്രം വരച്ച് BTS, BSC, MSC, HLR, VLR, AuC, EIR എന്നിവയുടെ റോളുകൾ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>തപാൽ പെട്ടി (ടവർ), ഹെഡ് പോസ്റ്റ് ഓഫീസ് (സ്വിച്ചിംഗ്), ആധാർ രേഖ (HLR), ഹോട്ടൽ രജിസ്റ്റർ (VLR) എന്നിവ ചേർന്ന തപാൽ ശൃംഖല പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q15: GSM Call Routing (MTC & MOC) and Handover vs Roaming
    # -------------------------------------------------------------------------
    'mobile-q15': {
        'manglish': {
            'title': "GSM-il MTC (Mobile Terminated Call) & MOC (Mobile Originated Call) flows-um Handover vs Roaming-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ MTC Call Routing Chain & MSRN",
                'eq': r"$$\text{PSTN} \to \text{GMSC} \xrightarrow{\text{Query HLR}} \text{VLR generates MSRN} \to \text{GMSC routes to Target MSC} \to \text{Paging } \to \text{Call Connected}$$",
                'text': r"<strong>Ormavekkan:</strong> MSRN (Mobile Station Roaming Number) target MSC-lekku call route cheyyan ulla temporary routing address aanu. Handover active call cut aavathe tower maattunnu; Roaming different operator coverage-il register cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. MTC (Incoming Call) Routing Steps:</strong></p>
    <ol>
        <li>Calling party dials MSISDN $\to$ call lands on Gateway MSC (GMSC).</li>
        <li>GMSC queries subscriber's HLR.</li>
        <li>HLR contacts current visiting VLR and requests a temporary routing number (MSRN).</li>
        <li>VLR sends MSRN back via HLR to GMSC.</li>
        <li>GMSC routes call trunk to target MSC, which broadcasts Paging request over BSS $\to$ Mobile rings!</li>
    </ol>
    <p><strong>2. Handover vs Roaming:</strong> Handover occurs in milliseconds during an ongoing active call between cells. Roaming is the location update registration when moving into a different service area or operator network.</p>
</div>
""",
            'understand_simply': r"""
<p>Oru parcel delivery alochikku: GMSC parcel reception desk aanu. Receiption desk HLR-il call cheythu ningal ippol ethu hotel-il aanu ennu chodikkunnu (MSRN). Aa hotel room-ilekku direct aayi parcel deliver cheyyunnu (MTC Call Setup)!</p>
"""
        },
        'ml': {
            'title': "GSM കോൾ റൂട്ടിംഗ് (MTC, MOC), ഹാൻഡ്ഓവർ vs റോമിംഗ് എന്നിവ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ MSRN കോൾ റൂട്ടിംഗ്",
                'eq': r"$$\text{കോൾ } \to \text{ GMSC } \to \text{ HLR } \to \text{ MSRN } \to \text{ ടാർഗെറ്റ് MSC } \to \text{ റിംഗ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻകമിംഗ് കോൾ വരുമ്പോൾ MSRN നമ്പർ വഴിയാണ് മൊബൈൽ എവിടെയാണെന്ന് കണ്ടെത്തി കോൾ എത്തിക്കുന്നത്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>MTC ഫ്ലോ ഡയഗ്രം വരച്ച് GMSC, HLR, VLR, MSRN റോളുകളും ഹാൻഡ്ഓവർ vs റോമിംഗ് വ്യത്യാസവും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>പാഴ്സൽ വരുമ്പോൾ ഹെഡ് ഓഫീസ് നിങ്ങളുടെ നിലവിലെ ഹോട്ടൽ റൂം നമ്പർ (MSRN) വാങ്ങി കൃത്യമായി എത്തിക്കുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q16: Interactive Voice Response (IVR) Architecture
    # -------------------------------------------------------------------------
    'mobile-q16': {
        'manglish': {
            'title': "Interactive Voice Response (IVR) system-te architecture-um call flow-um detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Core IVR Components",
                'eq': r"$$\text{Telephony Interface (SIP/PSTN)} \longleftrightarrow \text{DTMF Decoder / ASR} \longleftrightarrow \text{IVR Engine (VXML)} \longleftrightarrow \text{TTS / Database}$$",
                'text': r"<strong>Ormavekkan:</strong> 'Malayalathinu 1 amarthuka' &mdash; User dial pad keypad chavittumbol Dual-Tone Multi-Frequency (DTMF) decode cheythu database query execute cheythu automated speech output (TTS/Pre-recorded audio) tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>Telephony Interface Card:</strong> E1/T1 PRI lines or SIP VoIP trunk lines handle incoming telephone calls.</li>
        <li><strong>DTMF Tone Detector:</strong> Keypad press (digits 0-9, *, #) generate dual-frequency tones that are decoded into numbers.</li>
        <li><strong>Automated Speech Recognition (ASR):</strong> Modern IVR spoken voice input understand cheyyunnu.</li>
        <li><strong>VoiceXML / IVR Logic Engine:</strong> Decision tree execution (eg: if choice == 1, query account balance).</li>
        <li><strong>Text-to-Speech (TTS) & Audio Player:</strong> Plays bank account balance or queued music back to the caller.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Customer care-il vilikkumbol: 'Malayalathil samsarikkaan 1 amarthuka... Balance ariyaan 2 amarthuka...' ennu computer voice parayunnathaanu IVR! Nammal 1 amarthumbol keypad DTMF sound computer decode cheythu account database check cheythu marupadi tharunnu!</p>
"""
        },
        'ml': {
            'title': "ഇന്ററാക്ടീവ് വോയ്സ് റെസ്പോൺസ് (IVR) ആർക്കിടെക്ചറും പ്രവർത്തനവും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പ്രധാന IVR ഘടകങ്ങൾ",
                'eq': r"$$\text{ടെലിഫോണി ഇന്റർഫേസ്, DTMF ഡീകോഡർ, വോയ്സ് എഞ്ചിൻ, ഡാറ്റാബേസ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> 'മലയാളത്തിന് 1 അമർത്തുക' &mdash; കീപാഡ് അമർത്തുമ്പോൾ DTMF ടോണുകൾ മനസ്സിലാക്കി കമ്പ്യൂട്ടർ സ്വയം പ്രതികരിക്കുന്ന സംവിധാനം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>DTMF ഡിറ്റക്ഷൻ, വോയ്സ് XML ലോജിക്, ടെക്സ്റ്റ്-ടു-സ്പീച്ച് എന്നിവ ബ്ലോക്ക് ഡയഗ്രം സഹിതം എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>കസ്റ്റമർ കെയറിൽ വിളിക്കുമ്പോൾ കമ്പ്യൂട്ടർ സംസാരിക്കുകയും കീപാഡ് അമർത്തുമ്പോൾ സർവ്വീസ് നൽകുകയും ചെയ്യുന്ന സംവിധാനം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q17: GSM Security Architecture (A3, A8, A5)
    # -------------------------------------------------------------------------
    'mobile-q17': {
        'manglish': {
            'title': "GSM Security Architecture: Authentication (A3), Key Generation (A8), and Encryption (A5) algorithms explain cheyyuka.",
            'remember_this': {
                'title': "⚡ GSM Security Trio",
                'eq': r"$$\text{A3: } \text{RAND} + K_i \to \text{SRES} \text{ (Auth)}; \;\; \text{A8: } \text{RAND} + K_i \to K_c \text{ (Key Gen)}; \;\; \text{A5: Voice Stream Cipher with } K_c$$",
                'text': r"<strong>Ormavekkan:</strong> Secret key $K_i$ SIM-ilum AuC-ilum mathrame undavoo (Never sent over air!). Network random challenge RAND ayakkunnu; SIM calculate cheytha SRES-um network SRES-um match aaneel authenticated! Encryption key $K_c$ vechu A5 cipher voice encrypt cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Three Cryptographic Algorithms:</strong></p>
    <ol>
        <li><strong>A3 Algorithm (Authentication):</strong> Network sends 128-bit random number RAND over air. SIM runs A3 algorithm using secret subscriber key $K_i$: $\text{SRES} = A3(RAND, K_i)$. SIM sends 32-bit SRES back. Network checks if $\text{SRES}_{\text{SIM}} == \text{SRES}_{\text{AuC}}$.</li>
        <li><strong>A8 Algorithm (Ciphering Key Generation):</strong> SIM and network simultaneously run A8 using same RAND and $K_i$: $K_c = A8(RAND, K_i)$ (64-bit session key).</li>
        <li><strong>A5 Algorithm (Air-Interface Encryption):</strong> Hardware stream cipher inside handset. Uses $K_c$ and TDMA frame number to encrypt every voice/data bit before transmitting over radio air interface.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Oru bank locker security pole aanu: Secret master key $K_i$ ningalude SIM-il bhadramaayi irikkunnu. Tower oru random challenge (RAND) tharunnu. SIM-te ullil vechu thanne signature undakki thirichu kodukkunnu (A3). Secret key puratheku pokathathukond aarkkum hack cheyyan pattilla!</p>
"""
        },
        'ml': {
            'title': "GSM സുരക്ഷാ ആർക്കിടെക്ചർ: A3, A8, A5 അൽഗോരിതങ്ങൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 3 സുരക്ഷാ അൽഗോരിതങ്ങൾ",
                'eq': r"$$\text{A3 (ഓതന്റിക്കേഷൻ), A8 (കീ ജനറേഷൻ), A5 (വോയ്സ് എൻക്രിപ്ഷൻ)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> രഹസ്യ കീ $K_i$ റേഡിയോ തരംഗങ്ങളിലൂടെ അയക്കാതെ സിം കാർഡിനുള്ളിൽ തന്നെ സൂക്ഷിച്ചാണ് സുരക്ഷ ഉറപ്പാക്കുന്നത്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>RAND, SRES, $K_c$ എന്നിവയുടെ ഫ്ലോ ഡയഗ്രം വരച്ച് A3, A8, A5 പ്രവർത്തനങ്ങൾ വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ബാങ്ക് ഒടിപി പോലെ രഹസ്യ നമ്പർ പുറത്തുവിടാതെ ഒപ്പുകൾ പരിശോധിച്ച് ഫോൺ സുരക്ഷിതമാക്കുന്ന രീതി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q18: Short Message Service (SMS) Strengths
    # -------------------------------------------------------------------------
    'mobile-q18': {
        'manglish': {
            'title': "Short Message Service (SMS)-inte architectural strengths-um distinctiveness-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Out-of-Band Signaling Delivery",
                'eq': r"$$\text{SMS uses SS7 Signaling Channels (SDCCH / SACCH) &mdash; NOT Traffic Channels (TCH)}$$",
                'text': r"<strong>Ormavekkan:</strong> Phone call samsarichu kondirikkumbol polum SMS deliver aavum! Store-and-Forward architecture via SMSC: Phone switched off aaneel SMS SMSC-il save aayi phone on aavumbol deliver cheyyum."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Out-of-Band Delivery:</strong> SMS dedicated voice traffic channel use cheyyunnilla. Control signaling channels (SDCCH or SACCH) vazhi background-il transmit cheyyunnu.</li>
        <li><strong>2. Store-and-Forward:</strong> Point-to-Point direct call alla. SMSC message store cheythu vekkunnu; receiver available aavumbol deliver cheythu Delivery Report tharunnu.</li>
        <li><strong>3. 160-Character Optimization:</strong> 7-bit default alphabet encoding use cheythu 140 bytes payload-il 160 characters compact aayi pack cheyyunnu ($140 \times 8 / 7 = 160$).</li>
        <li><strong>4. Universal Device Compatibility:</strong> 2G basic feature phone muthal latest 5G smartphone vare 100% devices-il internet illathe polum work cheyyunnu (Banking OTPs)!</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Ordinary phone call oru train track pole aanu &mdash; track full aaneel call povilla. Pakshe SMS track-te side-lulla small path vazhi povaan pattunna cycle pole aanu &mdash; voice call nadannu kondirikkumbolum background-il silent aayi SMS message deliver aavum!</p>
"""
        },
        'ml': {
            'title': "എസ്എംഎസ് (SMS) സാങ്കേതികവിദ്യയുടെ പ്രധാന മേന്മകളും പ്രത്യേകതകളും എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ സിഗ്നലിംഗ് ചാനൽ ഡെലിവറി",
                'eq': r"$$\text{കൺട്രോൾ സിഗ്നലിംഗ് ചാനലുകൾ വഴി പ്രവർത്തിക്കുന്നു (വോയ്സ് ട്രാഫിക് ചാനലല്ല)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഫോൺ കോൾ സംസാരിച്ചുകൊണ്ടിരിക്കുമ്പോഴും, ഫോൺ ഓഫ് ആണെങ്കിൽ SMSC-യിൽ സൂക്ഷിച്ചുവെച്ചും എസ്എംഎസ് ഡെലിവർ ചെയ്യുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സ്റ്റോർ-ആൻഡ്-ഫോർവേഡ്, സിഗ്നലിംഗ് ചാനൽ ഉപയോഗം, 160 ക്യാരക്ടർ ഒപ്റ്റിമൈസേഷൻ എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഇന്റർനെറ്റ് ഇല്ലാതെയും ബാങ്ക് ഒടിപികളും സന്ദേശങ്ങളും 100% ഫോണുകളിലും കൃത്യമായി എത്തുന്നതിന്റെ രഹസ്യം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q19: Bottlenecks of GPRS
    # -------------------------------------------------------------------------
    'mobile-q19': {
        'manglish': {
            'title': "General Packet Radio Service (GPRS)-nte limitations-um bottlenecks-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 2.5G GPRS Constraints",
                'eq': r"$$\text{Theoretical Max: } 171.2\text{ kbps}, \;\; \text{Practical: } 30\text{--}50\text{ kbps}, \;\; \text{CS-1 to CS-4 Coding}$$",
                'text': r"<strong>Ormavekkan:</strong> GMSK modulation bit rate limit cheyyunnu; voice calls-nu primary priority ullathukond data channels pre-empt cheyyappadunnu; high latency (hundreds of ms); half-duplex radio restrictions."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Low Data Rates:</strong> Max 8 time slots combine cheythaalum practical speed 30-50 kbps matrame kittoo.</li>
        <li><strong>2. Voice Pre-emption:</strong> GSM cellular network voice calls-nu highest priority tharunnu. Tower-il traffic koodumbol data slots cut cheythu voice-lekku allocate cheyyunnu.</li>
        <li><strong>3. High Latency & Jitter:</strong> Round-trip latency 600 ms to 1 second vare aavum, making real-time video calls or gaming impossible.</li>
        <li><strong>4. GMSK Modulation limitation:</strong> GMSK carries only 1 bit per symbol (EDGE 8-PSK use cheythanu ithu pariharichath).</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Pandathe 2G GPRS internet alochikku: Oru photo open aavan 2 minute thirinju kondirikkum! Road-il VIP cars (Voice calls) varumbol normal vehicles (GPRS data packets) roadside-il nirthi idunnathu pole aanu voice priority!</p>
"""
        },
        'ml': {
            'title': "ജിപിആർഎസ് (GPRS) സാങ്കേതികവിദ്യയുടെ പ്രധാന പരിമിതികൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ ജിപിആർഎസ് പരിമിതികൾ",
                'eq': r"$$\text{കുറഞ്ഞ സ്പീഡ് (30-50 kbps), ഉയർന്ന ലേറ്റൻസി, വോയ്സ് കോൾ മുൻഗണന}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> വോയ്സ് കോളുകൾക്ക് കൂടുതൽ മുൻഗണന നൽകുന്നതിനാലും കുറഞ്ഞ മോഡുലേഷൻ രീതിയായതിനാലും സ്പീഡ് വളരെ കുറവായിരുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡാറ്റാ സ്പീഡ് പരിമിതികൾ, വോയ്സ് പ്രയോറിറ്റി, ലേറ്റൻസി പ്രശ്നങ്ങൾ എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>പഴയ കാലത്ത് ഒരു ഫോട്ടോ ലോഡാവാൻ മിനിറ്റുകൾ കറങ്ങി നിന്നിരുന്ന 2G ഇന്റർനെറ്റ് അനുഭവം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q20: Billing and Charging Mechanisms in GPRS
    # -------------------------------------------------------------------------
    'mobile-q20': {
        'manglish': {
            'title': "GPRS-il Billing & Charging mechanisms (Volume, Duration, QoS, and CDRs) enganeyaanu implement cheythittullath?",
            'remember_this': {
                'title': "⚡ Packet-Based Billing via CDRs",
                'eq': r"$$\text{CDR Types: S-CDR (from SGSN)} \quad \text{and} \quad \text{G-CDR (from GGSN)} \longrightarrow \text{Billing Gateway (BG)}$$",
                'text': r"<strong>Ormavekkan:</strong> Traditional voice call connection duration vechu bill cheyyumbol, GPRS transmitted data volume (Kilobytes / Megabytes) vechanu bill cheyyunnath (Always Connected, pay only for bytes transferred)!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>Volume-based Charging:</strong> Transmitted and received data byte count (uplink & downlink megabytes).</li>
        <li><strong>Duration-based Charging:</strong> Active PDP Context duration (time connected to corporate APN).</li>
        <li><strong>QoS-based Charging:</strong> Premium high-priority low-latency traffic-nu kooduthal tariff.</li>
        <li><strong>Call Detail Records (CDRs):</strong>
            <ul>
                <li><strong>S-CDR:</strong> SGSN generates record of radio resources and location.</li>
                <li><strong>G-CDR:</strong> GGSN generates record of external IP data traffic volume and external destination.</li>
            </ul>
        </li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Electric bill vs Landline bill: Landline-il phone eduthu vecha samayam count cheyyunnu (Duration). GPRS water meter pole aanu &mdash; pipe eppozhum open aayirikkum, pakshe ethra litre vellam (MBs) use cheytho athinu mathram pay cheythaal mathi!</p>
"""
        },
        'ml': {
            'title': "ജിപിആർഎസിലെ ബില്ലിംഗ് രീതികൾ (Volume, Duration, QoS, CDR) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പാക്കറ്റ് അധിഷ്ഠിത ബില്ലിംഗ്",
                'eq': r"$$\text{ഉപയോഗിച്ച ഡാറ്റാ വോളിയം (MB) അനുസരിച്ച് ബില്ലിംഗ് (S-CDR, G-CDR)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> കണക്റ്റഡ് ആയിരിക്കുന്ന സമയത്തിനല്ല, കൈമാറ്റം ചെയ്ത ഡാറ്റയുടെ അളവിനാണ് പണം നൽകേണ്ടത്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡാറ്റാ വോളിയം ബില്ലിംഗ്, S-CDR, G-CDR വ്യത്യാസങ്ങൾ, ക്വാളിറ്റി ഓഫ് സർവ്വീസ് ചാർജ്ജിംഗ് എന്നിവ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വാട്ടർ മീറ്റർ പോലെ എത്ര ലിറ്റർ വെള്ളം ഉപയോഗിച്ചോ അതിന് മാത്രം കാശ് കൊടുക്കുന്ന രീതി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q21: SMS Architecture and Delivery (SM-MT & SM-MO)
    # -------------------------------------------------------------------------
    'mobile-q21': {
        'manglish': {
            'title': "SMS Architecture-um delivery mechanisms (SM-MO & SM-MT) detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ SM-MO vs SM-MT Flows",
                'eq': r"$$\text{SM-MO: MS} \to \text{BTS} \to \text{MSC} \to \text{SMS-IWMSC} \to \text{SMSC}; \;\; \text{SM-MT: SMSC} \to \text{SMS-GMSC} \xrightarrow{\text{HLR}} \text{VMSC} \to \text{MS}$$",
                'text': r"<strong>Ormavekkan:</strong> SM-MO (Mobile Originated) message mobile-il ninnu SMSC-ilottu submit cheyyunnu; SM-MT (Mobile Terminated) SMSC-il ninnu destination mobile-ilekku deliver cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Mobile Originated (SM-MO) Flow:</strong></p>
    <ol>
        <li>User types SMS and presses send $\to$ transmits over SDCCH signaling channel to BTS $\to$ BSC $\to$ MSC.</li>
        <li>MSC passes message to SMS-IWMSC (Interworking MSC).</li>
        <li>SMS-IWMSC forwards to Short Message Service Center (SMSC). SMSC stores message safely in database and sends acknowledgement back to sender.</li>
    </ol>
    <p><strong>2. Mobile Terminated (SM-MT) Flow:</strong></p>
    <ol>
        <li>SMSC initiates delivery via SMS-GMSC (Gateway MSC).</li>
        <li>SMS-GMSC queries recipient's HLR for current location $\to$ HLR returns current serving MSC/VLR address.</li>
        <li>SMS-GMSC transfers message to target MSC.</li>
        <li>Target MSC pages the mobile and delivers SMS over air interface $\to$ returns Delivery Receipt to SMSC.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Post office delivery process: Ningal letter post box-il idunnu $\to$ van eduthu central post office-il (SMSC) vekkunnu (SM-MO). Pinne postman friend-inte veedu kandupidichu kondupoi kodukkunnu (SM-MT)!</p>
"""
        },
        'ml': {
            'title': "എസ്എംഎസ് ആർക്കിടെക്ചറും ഡെലിവറി രീതികളും (SM-MO, SM-MT) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ എസ്എംഎസ് ഡെലിവറി ഫ്ലോ",
                'eq': r"$$\text{SM-MO (അയക്കുന്നത്) } \to \text{ SMSC } \to \text{ SM-MT (ലഭിക്കുന്നത്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> അയക്കുന്ന സന്ദേശം SMSC-യിൽ എത്തുന്നു (MO); അവിടെനിന്ന് സ്വീകർത്താവിന്റെ ഫോണിലേക്ക് എത്തിക്കുന്നു (MT)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>SMSC, SMS-GMSC, SMS-IWMSC ബ്ലോക്ക് ഡയഗ്രം വരച്ച് MO, MT ഫ്ലോകൾ വ്യക്തമാക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>നമ്മൾ തപാൽ പെട്ടിയിൽ കത്ത് ഇടുന്നതും (MO), പോസ്റ്റ്മാൻ അത് കൊണ്ടുപോയി വീട്ടിൽ കൊടുക്കുന്നതും (MT) പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q22: GPRS Architecture, Protocol Stack, and Operations
    # -------------------------------------------------------------------------
    'mobile-q22': {
        'manglish': {
            'title': "GPRS Network Architecture, Protocol Stack, and SGSN/GGSN functions explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 2 Core GPRS Nodes",
                'eq': r"$$\text{MS} \longleftrightarrow \text{BSS [PCU]} \overset{Gb}{\longleftrightarrow} \text{SGSN} \overset{Gn}{\longleftrightarrow} \text{GGSN} \overset{Gi}{\longleftrightarrow} \text{Public Internet}$$",
                'text': r"<strong>Ormavekkan:</strong> SGSN (Serving GPRS Support Node) packet routing and ciphering cheyyunnu; GGSN (Gateway GPRS Support Node) public internet gateway aayi external IP allocation and firewalling cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>Core Entities:</strong></p>
    <ol>
        <li><strong>PCU (Packet Control Unit):</strong> BSS-il add cheytha hardware; voice traffic-ne circuit switch-ilottum packet data-ye GPRS SGSN-ilottum split cheyyunnu.</li>
        <li><strong>SGSN:</strong> Mobility management, packet security, logical link control (LLC), and routing within service area ($Gb$ interface).</li>
        <li><strong>GGSN:</strong> Anchor gateway connecting to external internet ($Gi$ interface). Assigns dynamic IP address to mobile and handles GTP tunneling.</li>
        <li><strong>GTP (GPRS Tunneling Protocol):</strong> User IP packets-ine GPRS backbone vazhi tunnel cheythu carry cheyyunnu.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>SGSN oru local post sorting office pole aanu &mdash; user evideyaanu ennu nokki packet route cheyyunnu. GGSN international airport cargo hub pole aanu &mdash; local packets-ine global internet-umaayi connect cheyyunnu!</p>
"""
        },
        'ml': {
            'title': "ജിപിആർഎസ് ആർക്കിടെക്ചറും പ്രോട്ടോക്കോൾ സ്റ്റാക്കും (SGSN, GGSN) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പ്രധാന GPRS നോഡുകൾ",
                'eq': r"$$\text{SGSN (ലോക്കൽ പാക്കറ്റ് റൂട്ടിംഗ്) } \longleftrightarrow \text{ GGSN (ഇന്റർനെറ്റ് ഗേറ്റ്‌വേ)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> SGSN മൊബിലിറ്റിയും പാക്കറ്റ് ഡെലിവറിയും നോക്കുന്നു; GGSN ഇന്റർനെറ്റിലേക്ക് കണക്ഷൻ നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം ആർക്കിടെക്ചർ ഗൈഡ്</span></div>
    <p>ആർക്കിടെക്ചർ ഡയഗ്രം വരച്ച് PCU, SGSN, GGSN, GTP പ്രോട്ടോക്കോൾ എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ജില്ലാ പോസ്റ്റ് ഓഫീസ് പോലെ SGSN-ഉം, അന്താരാഷ്ട്ര എയർപോർട്ട് കാർഗോ പോലെ GGSN-ഉം പ്രവർത്തിക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q23: Quality of Service (QoS) Parameters in GPRS
    # -------------------------------------------------------------------------
    'mobile-q23': {
        'manglish': {
            'title': "GPRS-ile Quality of Service (QoS) parameters (Delay, Precedence, Reliability, Throughput) explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 5 QoS Attributes Profile",
                'eq': r"$$\text{QoS Profile} = \{\text{Precedence, Delay, Reliability, Peak Throughput, Mean Throughput}\}$$",
                'text': r"<strong>Ormavekkan:</strong> High-priority real-time packets-nu low delay class allocate cheyyunnu; background email downloads-nu high delay class koduthu network bandwidth optimize cheyyunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Precedence Class (Priority):</strong> High, Normal, Low. Network congestion varumbol low precedence packets drop cheyyunnu.</li>
        <li><strong>2. Delay Class:</strong> Classes 1 to 4 specifying maximum end-to-end packet transfer latency (Class 1: &lt;0.5s for 128 bytes; Class 4: unspecified best-effort).</li>
        <li><strong>3. Reliability Class:</strong> Probability of corrupted, duplicated, or lost packets (GTP/LLC retransmission enabled for high reliability).</li>
        <li><strong>4. Throughput Class:</strong> Guaranteed Peak throughput (up to 2048 kbps) and Mean throughput rates.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Courier service booking pole aanu: Speed Post (High precedence, low delay &mdash; expensive) vs Normal Post (Best effort, slow &mdash; cheap). GPRS network packet-inte nature nokki delivery speed theerumanikkunnu!</p>
"""
        },
        'ml': {
            'title': "ജിപിആർഎസിലെ ക്വാളിറ്റി ഓഫ് സർവ്വീസ് (QoS) ഘടകങ്ങൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 4 QoS ഘടകങ്ങൾ",
                'eq': r"$$\text{പ്രിസിഡൻസ് (മുൻഗണന), ഡിലേ (താമസം), റിലയബിലിറ്റി, ത്രൂപുട്ട്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഡാറ്റയുടെ പ്രാധാന്യം അനുസരിച്ച് വേഗതയും മുൻഗണനയും നൽകുന്ന സംവിധാനം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>പ്രിസിഡൻസ്, ഡിലേ ക്ലാസുകൾ, റിലയബിലിറ്റി, ത്രൂപുട്ട് എന്നിവ പോയിന്റുകളായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സ്പീഡ് പോസ്റ്റും ഓർഡിനറി പോസ്റ്റും തമ്മിലുള്ള വ്യത്യാസം പോലെ പാക്കറ്റുകൾക്ക് മുൻഗണന നൽകുന്ന രീതി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q24: WLAN Architecture: Infrastructure Mode vs Ad-Hoc Mode
    # -------------------------------------------------------------------------
    'mobile-q24': {
        'manglish': {
            'title': "IEEE 802.11 WLAN Architecture: Infrastructure Mode-um Ad-Hoc Mode-um compare cheyyuka.",
            'remember_this': {
                'title': "⚡ BSS vs IBSS Comparison",
                'eq': r"$$\text{Infrastructure (BSS): Central AP present} \iff \text{Ad-Hoc (IBSS): Peer-to-Peer without AP}$$",
                'text': r"<strong>Ormavekkan:</strong> Infrastructure BSS-il central Access Point (AP) distribution system (DS) vazhi wired LAN-umaayi connect cheyyunnu. Ad-Hoc IBSS-il devices direct aayi P2P share cheyyunnu (eg: AirDrop, Wi-Fi Direct)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Feature</th><th>Infrastructure Mode (BSS / ESS)</th><th>Independent Ad-Hoc Mode (IBSS)</th></tr></thead>
        <tbody>
            <tr><td><strong>Central Controller</strong></td><td>Requires dedicated Access Point (AP / Wi-Fi Router).</td><td>No Access Point required (Decentralized peer-to-peer).</td></tr>
            <tr><td><strong>Internet / LAN Access</strong></td><td>Connects to wired backbone network via Distribution System.</td><td>Isolated standalone local cluster between nearby devices.</td></tr>
            <tr><td><strong>Scalability</strong></td><td>Highly scalable by connecting multiple APs into an ESS.</td><td>Limited to few nearby nodes due to packet collision.</td></tr>
            <tr><td><strong>Examples</strong></td><td>Home Wi-Fi router, College campus Wi-Fi, Airport hotspot.</td><td>Apple AirDrop, Wi-Fi Direct sharing, Battlefield rescue mesh.</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>College classroom vs Friends chat: Infrastructure mode classroom teacher (Access Point) ulla pole aanu &mdash; ella communication-um teacher vazhi control cheyyunnu. Ad-hoc mode teacher illatha samayathu friends thammil direct aayi whisper cheythu samsarikkunna P2P group pole aanu (AirDrop)!</p>
"""
        },
        'ml': {
            'title': "വയർലെസ് ലാൻ (WLAN) ആർക്കിടെക്ചർ: ഇൻഫ്രാസ്ട്രക്ചർ vs അഡ്-ഹോക്ക് മോഡ് താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ WLAN താരതമ്യം",
                'eq': r"$$\text{ഇൻഫ്രാസ്ട്രക്ചർ (റൂട്ടർ ഉണ്ട്) } \quad \text{vs} \quad \text{അഡ്-ഹോക്ക് (ഡയറക്ട് P2P)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഇൻഫ്രാസ്ട്രക്ചർ മോഡിൽ വൈ-ഫൈ റൂട്ടർ വഴി ഇന്റർനെറ്റ് ലഭിക്കുന്നു; അഡ്-ഹോക്ക് മോഡിൽ ഫോണുകൾ പരസ്പരം നേരിട്ട് കണക്റ്റ് ആകുന്നു (എയർഡ്രോപ്പ്)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>BSS, ESS, IBSS വ്യത്യാസങ്ങളും ആക്സസ് പോയിന്റിന്റെ റോളും ടേബിളിൽ എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വീട്ടിലെ വൈ-ഫൈ റൂട്ടർ വഴിയുള്ള കണക്ഷനും, രണ്ടു ഫോണുകൾ തമ്മിൽ എയർഡ്രോപ്പ് വഴി നേരിട്ട് ഫയൽ ഷെയർ ചെയ്യുന്നതും പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q25: Interframe Spaces (IFS) in IEEE 802.11 MAC
    # -------------------------------------------------------------------------
    'mobile-q25': {
        'manglish': {
            'title': "IEEE 802.11 MAC-ile Interframe Spaces (SIFS, PIFS, DIFS, EIFS) explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Priority Ranking by Duration",
                'eq': r"$$\text{SIFS} < \text{PIFS} < \text{DIFS} < \text{EIFS} \implies \text{Shorter IFS means Higher Channel Priority}$$",
                'text': r"<strong>Ormavekkan:</strong> Time gap kurayumbol medium pettennu grab cheyyam: SIFS = ACK and CTS packets (Highest priority); PIFS = Polling access point; DIFS = Normal asynchronous data; EIFS = Error retransmission (Lowest priority)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>SIFS (Short IFS):</strong> Shortest waiting duration ($\approx 10\text{--}16\text{ }\mu\text{s}$). Used for time-critical control frames: ACK, CTS, and fragmented frames. Guarantees other stations cannot interrupt an ongoing handshake!</li>
        <li><strong>PIFS (PCF IFS):</strong> Intermediate duration ($\text{SIFS} + 1\text{ slot}$). Access Point uses this during Point Coordination Function to grab priority for polling.</li>
        <li><strong>DIFS (DCF IFS):</strong> Normal standard wait duration ($\text{SIFS} + 2\text{ slots}$). Stations wishing to transmit standard asynchronous data frames must wait for medium to be idle for at least DIFS before starting random backoff.</li>
        <li><strong>EIFS (Extended IFS):</strong> Longest duration. Triggered when a corrupted packet with CRC error is detected; forces node to wait longer to avoid colliding with remaining transmissions.</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Hospital emergency priority pole aanu: Ambulance-nu shortest waiting time (SIFS &mdash; highest priority ACK). Normal doctors-nu intermediate wait (PIFS). General public-nu standard queue wait (DIFS). Faulty registration slip ullavarkku longest wait (EIFS)!</p>
"""
        },
        'ml': {
            'title': "IEEE 802.11-ലെ ഇന്റർഫ്രെയിം സ്പേസുകൾ (SIFS, PIFS, DIFS, EIFS) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പ്രയോറിറ്റി ഓർഡർ",
                'eq': r"$$\text{SIFS} < \text{PIFS} < \text{DIFS} < \text{EIFS}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> കാത്തിരിപ്പ് സമയം കുറയുന്തോറും മുൻഗണന കൂടുന്നു. ACK മെസ്സേജുകൾക്ക് ഏറ്റവും കുറഞ്ഞ സമയമായ SIFS നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>സമയ ദൈർഘ്യ ക്രമത്തിൽ 4 ഇന്റർഫ്രെയിം സ്പേസുകളുടെയും ഉപയോഗങ്ങൾ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ആശുപത്രിയിൽ ആംബുലൻസിന് മുൻഗണന നൽകുന്നത് പോലെ അടിയന്തര ഡാറ്റയ്ക്ക് കുറഞ്ഞ കാത്തിരിപ്പ് സമയം നൽകുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q26: Comparative Analysis: Wi-Fi vs Cellular (3G/4G)
    # -------------------------------------------------------------------------
    'mobile-q26': {
        'manglish': {
            'title': "Wi-Fi (IEEE 802.11)-um Cellular Networks (3G/4G)-um compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Unlicensed vs Licensed Spectrum",
                'eq': r"$$\text{Wi-Fi: Unlicensed 2.4/5 GHz, Local Coverage (100m); Cellular: Licensed Spectrum, Wide Area Mobility (kms)}$$",
                'text': r"<strong>Ormavekkan:</strong> Wi-Fi free unlicensed band use cheyyunnu, high local speed tharunnu pakshe no seamless high-speed vehicular handover. Cellular expensive licensed spectrum use cheyyunnu, fast vehicle handover and guaranteed QoS tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Parameter</th><th>Wi-Fi (IEEE 802.11)</th><th>Cellular Networks (3G / 4G LTE)</th></tr></thead>
        <tbody>
            <tr><td><strong>Spectrum License</strong></td><td>Unlicensed ISM bands ($2.4\text{ GHz}, 5\text{ GHz}, 6\text{ GHz}$). Free to deploy.</td><td>Licensed spectrum auctioned by government (telecom operators).</td></tr>
            <tr><td><strong>Coverage Range</strong></td><td>Short range ($30\text{--}100\text{ meters}$ per AP).</td><td>Wide area ($1\text{--}15\text{ km}$ per cell tower).</td></tr>
            <tr><td><strong>Mobility Support</strong></td><td>Stationary or slow walking speed; handovers cause drops.</td><td>Seamless handovers up to $250\text{--}350\text{ km/h}$ (High-speed trains).</td></tr>
            <tr><td><strong>Deployment Cost</strong></td><td>Very inexpensive router setup.</td><td>Billion-dollar towers, core networks, and base stations.</td></tr>
            <tr><td><strong>QoS & Contention</strong></td><td>CSMA/CA contention; throughput drops with many users.</td><td>Centralized scheduling (OFDMA); deterministic QoS.</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Wi-Fi veedinte ullilulla cordless phone pole aanu &mdash; super clarity, pakshe gate kadannal cut aavum. Cellular network mobile phone pole aanu &mdash; Kerala muthal Delhi vare travel cheythaalum continuous aayi work cheyyum!</p>
"""
        },
        'ml': {
            'title': "വൈ-ഫൈയും (Wi-Fi) സെല്ലുലാർ (3G/4G) നെറ്റ്‌വർക്കുകളും തമ്മിലുള്ള വ്യത്യാസങ്ങൾ എന്തൊക്കെയാണ്?",
            'remember_this': {
                'title': "⚡ പ്രധാന താരതമ്യം",
                'eq': r"$$\text{വൈ-ഫൈ (ചെറിയ പരിധി, സൗജന്യം) } \quad \text{vs} \quad \text{സെല്ലുലാർ (വലിയ പരിധി, ലൈസൻസ്ഡ്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> വൈ-ഫൈ വീടുകളിൽ കുറഞ്ഞ ചെലവിൽ ഉയർന്ന വേഗത നൽകുമ്പോൾ, സെല്ലുലാർ അതിവേഗ യാത്രകളിലും തടസ്സമില്ലാത്ത കവറേജ് നൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ സ്പെക്ട്രം, പരിധി, മൊബിലിറ്റി, ചിലവ്, ക്വാളിറ്റി ഓഫ് സർവ്വീസ് എന്നിവ താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>വീട്ടിലെ കോർഡ്‌ലെസ്സ് ഫോൺ (വൈ-ഫൈ) പോലെയും, എവിടെ പോയാലും കിട്ടുന്ന മൊബൈൽ ഫോൺ (സെല്ലുലാർ) പോലെയും!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q27: Hidden and Exposed Terminal Problems & RTS/CTS
    # -------------------------------------------------------------------------
    'mobile-q27': {
        'manglish': {
            'title': "Hidden and Exposed Terminal Problems-um RTS/CTS virtual carrier sensing mechanics-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Hidden/Exposed Problem & Solution",
                'eq': r"$$\text{Hidden: } A \to B \leftarrow C \implies \text{Collision at } B; \quad \text{Exposed: } B \to A \text{ prevents } C \to D \implies \text{Wasted Bandwidth}$$",
                'text': r"<strong>Ormavekkan:</strong> Solution: RTS (Request to Send) + CTS (Clear to Send) with NAV (Network Allocation Vector). CTS hearing neighbouring nodes keep silent, completely eliminating hidden node collisions!"
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Hidden Terminal Problem:</strong> Node $A$ and Node $C$ cannot hear each other (out of radio range), but both are in range of central Node $B$. If both send packets to $B$ simultaneously, collision occurs at $B$!</p>
    <p>2. <strong>Exposed Terminal Problem:</strong> Node $B$ is sending to $A$. Node $C$ wants to send to $D$. $C$ hears $B$ transmitting and unnecessarily waits, even though transmitting to $D$ would not interfere with $A$!</p>
    <p>3. <strong>RTS/CTS Handshake Solution:</strong></p>
    <ul>
        <li>Sender $A$ sends small RTS packet containing duration.</li>
        <li>Receiver $B$ replies with CTS packet broadcast to all neighbours.</li>
        <li>Hidden node $C$ hears CTS and sets its <strong>NAV (Network Allocation Vector)</strong> timer, keeping quiet until $A$'s transmission finishes!</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Oru teacher-inte (Node B) randu vashathum madhilinte appurathum ippurathum aayi 2 students irikkunnu ($A$ and $C$). Randu perkum thammil thammil kaanan pattilla (Hidden). Randu perum ore samayam doubt chodichaal teacher-te cheviyil koottithallu aavum (Collision)! RTS/CTS teacher mic-il parayunnu: '$A$ doubt chodikkukayaanu, $C$ 1 minute mindathirikku' (CTS broadcast)!</p>
"""
        },
        'ml': {
            'title': "ഹിഡൻ ആൻഡ് എക്സ്പോസ്ഡ് ടെർമിനൽ പ്രശ്നങ്ങളും RTS/CTS പരിഹാരവും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പ്രശ്നവും പരിഹാരവും",
                'eq': r"$$\text{RTS/CTS ഹാൻഡ്‌ഷേക്ക് വഴി കൊളീഷനുകൾ പൂർണ്ണമായി ഒഴിവാക്കുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പരസ്പരം കാണാൻ കഴിയാത്ത നോഡുകൾ ഒരേ റിസീവറിലേക്ക് ഡാറ്റ അയക്കുമ്പോൾ ഉണ്ടാകുന്ന കൊളീഷനാണ് ഹിഡൻ ടെർമിനൽ പ്രശ്നം."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഡയഗ്രം വരച്ച് ഹിഡൻ, എക്സ്പോസ്ഡ് പ്രശ്നങ്ങളും RTS/CTS, NAV ടൈമർ പ്രവർത്തനവും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>മതിലിന്റെ ഇരുവശത്തിരിക്കുന്ന രണ്ടുപേർ ഒരേ അധ്യാപകനോട് ഒരേസമയം സംസാരിക്കുമ്പോൾ ഉണ്ടാകുന്ന ആശയക്കുഴപ്പവും അതിനുള്ള പരിഹാരവും!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q28: Wireless Local Loop (WLL)
    # -------------------------------------------------------------------------
    'mobile-q28': {
        'manglish': {
            'title': "Wireless Local Loop (WLL / Fixed Wireless Access) engane work cheyyunnu?",
            'remember_this': {
                'title': "⚡ WLL Architecture Chain",
                'eq': r"$$\text{PSTN Switch} \longleftrightarrow \text{WAC} \longleftrightarrow \text{Base Station Transceiver (BST)} \overset{\text{RF Air}}{\longleftrightarrow} \text{Subscriber Unit (FAU)}$$",
                'text': r"<strong>Ormavekkan:</strong> Road kuzhichu copper cable idenda aavashyamilla. Quick deployment, low copper maintenance cost, rural areas-il telephone connection kodukkan best option."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>Concept:</strong> Traditional landline telephone network-il central exchange-il ninnu veettilekku varunna underground copper cable-nu pakaram wireless radio link use cheyyunna system aanu WLL.</li>
        <li><strong>Components:</strong>
            <ul>
                <li><strong>PSTN Central Switch:</strong> Standard telephone exchange.</li>
                <li><strong>WAC (Wireless Access Controller):</strong> Radio resource management and authentication.</li>
                <li><strong>BST (Base Station Transceiver):</strong> Tower transceiver transmitting RF link.</li>
                <li><strong>FAU (Fixed Access Unit):</strong> Transceiver unit with directional rooftop antenna installed at subscriber home.</li>
            </ul>
        </li>
        <li><strong>Advantages:</strong> Rapid roll-out in hours, zero copper cable theft, ideal for rocky/hilly terrains.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Pandokke veettil landline phone venamenkil telephone exchange-il ninnu road kuzhichu copper wire konduvaranam aayirunnu. WLL athinu pakaram veedinte mukalil oru cheriya radio receiver fix cheythu wireless radio vazhi connection kodukkunnu. No road digging, no wire cuts!</p>
"""
        },
        'ml': {
            'title': "വയർലെസ് ലോക്കൽ ലൂപ്പ് (WLL) ആർക്കിടെക്ചറും ഉപയോഗങ്ങളും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ WLL സിസ്റ്റം",
                'eq': r"$$\text{കേബിളുകൾക്ക് പകരം റേഡിയോ തരംഗങ്ങൾ വഴി ലാൻഡ്‌ലൈൻ കണക്ഷൻ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> റോഡ് കുഴിച്ച് കേബിൾ ഇടാതെ എയറിലൂടെ അതിവേഗം വീടുകളിലേക്ക് ഫോൺ കണക്ഷൻ നൽകാൻ WLL സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ആർക്കിടെക്ചർ വരച്ച് PSTN, WAC, BST, സബ്സ്ക്രൈബർ യൂണിറ്റ് ഘടകങ്ങളും ഗുണങ്ങളും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>റോഡ് കുഴിച്ച് വയറുകൾ വലിക്കാതെ വീടിന്റെ മുകളിലെ ചെറിയ ആന്റിന വഴി ഫോൺ കണക്ഷൻ നൽകുന്ന രീതി!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q29: WLAN Security Evolution (WEP, WPA, WPA2, WPA3)
    # -------------------------------------------------------------------------
    'mobile-q29': {
        'manglish': {
            'title': "WLAN Security Evolution: WEP Vulnerabilities, WPA, WPA2 (802.11i), and WPA3 compare cheyyuka.",
            'remember_this': {
                'title': "⚡ Security Evolution Generations",
                'eq': r"$$\text{WEP (Broken RC4)} \to \text{WPA (TKIP)} \to \text{WPA2 (AES-CCMP)} \to \text{WPA3 (SAE Dragonfly + 192-bit)}$$",
                'text': r"<strong>Ormavekkan:</strong> WEP-le 24-bit small IV reuse aayathukond packets sniff cheythu 5 minutes-il crack cheyyam (FMS attack). WPA2 AES block cipher vechu secure aakki; WPA3 Dragonfly handshake vechu dictionary attacks eliminate cheythu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Generation</th><th>Cipher Algorithm</th><th>Key Integrity / Mechanism</th><th>Security Status</th></tr></thead>
        <tbody>
            <tr><td><strong>WEP</strong></td><td>RC4 Stream Cipher</td><td>24-bit static IV, CRC-32 (No key rotation)</td><td>Completely Broken (cracked in minutes)</td></tr>
            <tr><td><strong>WPA</strong></td><td>RC4 + TKIP</td><td>48-bit IV, per-packet key mixing, Michael MIC</td><td>Deprecated (transitional fix for WEP hardware)</td></tr>
            <tr><td><strong>WPA2 (802.11i)</strong></td><td>AES Block Cipher</td><td>CCMP (Counter Mode CBC-MAC), 128-bit key</td><td>Industry Standard (vulnerable to KRACK attack)</td></tr>
            <tr><td><strong>WPA3</strong></td><td>AES-GCM / 192-bit CNSA</td><td>SAE (Simultaneous Authentication of Equals)</td><td>Current State-of-the-Art (resists offline dictionary attacks)</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Door lock evolution pole aanu: <strong>WEP</strong> oru simple lock aanu &mdash; hairpin vechu kuttikkalikkarku polum thurakkam! <strong>WPA</strong> alpam koodi nalla lock. <strong>WPA2</strong> digital electronic fingerprint lock. <strong>WPA3</strong> face recognition ulla bank locker lock &mdash; wrong password adichu guess cheyyan polum hacker-nu chance kodukkilla!</p>
"""
        },
        'ml': {
            'title': "വൈ-ഫൈ സുരക്ഷാ പരിണാമം: WEP, WPA, WPA2, WPA3 എന്നിവ താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ സുരക്ഷാ പരിണാമം",
                'eq': r"$$\text{WEP (തകർന്നത്)} \to \text{WPA} \to \text{WPA2 (AES)} \to \text{WPA3 (ഏറ്റവും സുരക്ഷിതം)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> WEP വളരെ എളുപ്പത്തിൽ ഹാക്ക് ചെയ്യാമായിരുന്നതിനാൽ AES എൻക്രിപ്ഷനും SAE സാങ്കേതികവിദ്യയും കൊണ്ടുവന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ അൽഗോരിതം, കീ നീളം, അറ്റാക്കുകൾക്കെതിരെയുള്ള പ്രതിരോധം എന്നിവ താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഹെയർപിൻ വെച്ച് തുറക്കാമായിരുന്ന പഴയ പൂട്ട് (WEP) മാറി അത്യാധുനിക ഫേസ് റെക്കഗ്നിഷൻ ഡിജിറ്റൽ പൂട്ടിലേക്ക് (WPA3) മാറിയത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q30: HIPERLAN Communication Models and MAC
    # -------------------------------------------------------------------------
    'mobile-q30': {
        'manglish': {
            'title': "HIPERLAN standards (HIPERLAN 1 vs HIPERLAN 2) and EY-NPMA MAC protocol explain cheyyuka.",
            'remember_this': {
                'title': "⚡ EY-NPMA Mechanism",
                'eq': r"$$\text{EY-NPMA: Elimination-Yield Non-Preemptive Multiple Access in 5 GHz band}$$",
                'text': r"<strong>Ormavekkan:</strong> HIPERLAN 1 peer-to-peer ad-hoc architecture EY-NPMA contention protocol use cheyyunnu; HIPERLAN 2 cellular-like centralized ATM-based architecture with dynamic TDMA/TDD frames and OFDM tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>EY-NPMA MAC Protocol (HIPERLAN 1):</strong></p>
    <ul>
        <li><strong>Prioritization Phase:</strong> Channel idle aavumbol high priority packets compete cheyyunnu.</li>
        <li><strong>Contention Elimination Phase:</strong> Nodes transmit continuous energy burst pulses; shorter pulse burst ullavan eliminate aavunnu!</li>
        <li><strong>Yield Phase:</strong> Surviving nodes listen for a random slot duration. First node to finish transmits, guaranteeing collision-free delivery!</li>
    </ul>
    <p>2. <strong>HIPERLAN 2:</strong> Centralized Access Point, connection-oriented ATM cells, dynamic TDD frame structure, QoS for multimedia voice/video.</p>
</div>
""",
            'understand_simply': r"""
<p>Musical chairs game alochikku: Song stop aavumbol ellavarum odunnu, oro round-ilum aalukal eliminate aavunnu (Elimination phase). Last nilkkunna aalkku mathram chair kittunnu (Yield phase)! Ithanu EY-NPMA collision avoidance!</p>
"""
        },
        'ml': {
            'title': "ഹൈപ്പർലാൻ (HIPERLAN 1 vs HIPERLAN 2) കമ്മ്യൂണിക്കേഷൻ മോഡലുകൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ EY-NPMA പ്രോട്ടോക്കോൾ",
                'eq': r"$$\text{എലിമിനേഷൻ-യീൽഡ് രീതി വഴി കൊളീഷനുകൾ ഒഴിവാക്കുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> യൂറോപ്യൻ സ്റ്റാൻഡേർഡായ HIPERLAN 5 GHz ബാൻഡിൽ അതിവേഗ വയർലെസ്സ് വിനിമയം സാധ്യമാക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>EY-NPMA യുടെ 3 ഘട്ടങ്ങളും HIPERLAN 1, 2 താരതമ്യവും വ്യക്തമായി എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>മ്യൂസിക്കൽ ചെയർ കളിയിൽ ആളുകൾ ഓരോന്നായി പുറത്തായി ഒടുവിൽ ഒരാൾക്ക് മാത്രം കസേര കിട്ടുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q31: Extended CIA Triad in Information Security
    # -------------------------------------------------------------------------
    'mobile-q31': {
        'manglish': {
            'title': "Information Security-le Extended CIA Triad (Confidentiality, Integrity, Availability, Non-Repudiation, Authenticity) explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Extended CIA Pillars",
                'eq': r"$$\text{Confidentiality (Encryption), Integrity (Hashing), Availability (Redundancy), Authenticity, Non-Repudiation}$$",
                'text': r"<strong>Ormavekkan:</strong> Confidentiality = Unauthorised reading thadayunnu; Integrity = Data change aavathe nokkunnu (SHA-256); Availability = System 24x7 up aayirikkunnu; Non-Repudiation = 'Njan ayachathalla' ennu parayan pattilla (Digital signature)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ul>
        <li><strong>1. Confidentiality:</strong> Preventing unauthorized viewing of data (Symmetric/Asymmetric encryption like AES/RSA).</li>
        <li><strong>2. Integrity:</strong> Ensuring message is not modified or tampered with in transit (Cryptographic Hash functions, HMAC).</li>
        <li><strong>3. Availability:</strong> Ensuring services remain accessible to authorized users (Anti-DDoS, server redundancy, UPS).</li>
        <li><strong>4. Authenticity:</strong> Verifying true identity of sender (Digital Certificates, Multi-Factor Authentication).</li>
        <li><strong>5. Non-Repudiation:</strong> Sender cannot deny having sent the message (Public key Digital Signature).</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Bank cheque alochikku: Envelope-il ittu sealed aakki ayakkunnu (Confidentiality). Amount arum thiruthi ezhuthilla (Integrity). Bank branch 10 AM-nu open aayirikkunnu (Availability). Account holder-te official signature undu (Authenticity). Cheque koduthitt 'Njan ithu ezhuthi thന്നathalla' ennu owner-nu pinnedu deny cheyyan pattilla (Non-repudiation)!</p>
"""
        },
        'ml': {
            'title': "ഇൻഫർമേഷൻ സെക്യൂരിറ്റിയിലെ എക്സ്റ്റൻഡഡ് CIA ട്രയാഡ് ഘടകങ്ങൾ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ 5 സുരക്ഷാ സ്തംഭങ്ങൾ",
                'eq': r"$$\text{കോൺഫിഡെൻഷ്യാലിറ്റി, ഇന്റഗ്രിറ്റി, അവൈലബിലിറ്റി, ഓതന്റിസിറ്റി, നോൺ-റിപ്യൂഡിയേഷൻ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> വിവരങ്ങൾ രഹസ്യമായി സൂക്ഷിക്കാനും, മാറ്റങ്ങൾ വരുത്താതെ സംരക്ഷിക്കാനും, എപ്പോഴും ലഭ്യമാക്കാനും ഇത് ഉറപ്പുനൽകുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>5 ഘടകങ്ങളുടെയും നിർവ്വചനങ്ങളും അവയ്ക്കായി ഉപയോഗിക്കുന്ന ക്രിപ്റ്റോഗ്രാഫിക് മാർഗ്ഗങ്ങളും എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു ബാങ്ക് ചെക്കിൽ ഒപ്പിട്ട് നൽകുന്നത് പോലെ &mdash; ഒപ്പ് മാറ്റാനോ, തുക തിരുത്താനോ, ഒപ്പിട്ടത് ഞാനല്ലെന്ന് പറയാനോ കഴിയില്ല!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q32: Classification of Security Attacks
    # -------------------------------------------------------------------------
    'mobile-q32': {
        'manglish': {
            'title': "Mobile Computing-ile Security Attacks: Passive vs Active (Static vs Dynamic) classify cheyyuka.",
            'remember_this': {
                'title': "⚡ Attack Taxonomy",
                'eq': r"$$\text{Passive / Static: Eavesdropping, Sniffing (No data change); Active / Dynamic: Replay, Man-in-the-Middle, Spoofing, DoS}$$",
                'text': r"<strong>Ormavekkan:</strong> Passive attacks detect cheyyan paadanu (encryption vazhi prevent cheyyanam); Active attacks easily detect cheyyam (tampering, fake sender, server crashing)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p><strong>1. Passive Attacks (Eavesdropping):</strong></p>
    <ul>
        <li>Hacker packets intercept cheythu monitor cheyyunnu without altering data content.</li>
        <li>Eg: Wi-Fi packet sniffing (Wireshark), traffic pattern analysis, IMSI catching. Prevention: Strong encryption (WPA3, TLS).</li>
    </ul>
    <p><strong>2. Active Attacks (Modification & Impersonation):</strong></p>
    <ul>
        <li><strong>Masquerading / Spoofing:</strong> Attacker pretends to be legitimate base station or router (Rogue AP / Evil Twin).</li>
        <li><strong>Replay Attack:</strong> Valid authentication message record cheythu pinnedu reuse cheythu unauthorized login undakkunnu.</li>
        <li><strong>Message Modification:</strong> Changing bank transaction amount or destination account number.</li>
        <li><strong>Denial of Service (DoS):</strong> Radio jamming or flooding server to crash wireless connection.</li>
    </ul>
</div>
""",
            'understand_simply': r"""
<p>Spying vs Robbery: <strong>Passive attack</strong> oru charan (spy) door-te purathu ninnu secret samsaram olinju kelkkunnathu pole aanu (No noise, no modification). <strong>Active attack</strong> oru kallan vathil pottichu akathu kayari money thiruthi ezhuthunnathu pole aanu (Direct modification)!</p>
"""
        },
        'ml': {
            'title': "മൊബൈൽ നെറ്റ്‌വർക്കിലെ സെക്യൂരിറ്റി അറ്റാക്കുകൾ: പാസീവ് vs ആക്ടീവ് അറ്റാക്കുകൾ തരംതിരിക്കുക",
            'remember_this': {
                'title': "⚡ അറ്റാക്ക് വർഗ്ഗീകരണം",
                'eq': r"$$\text{പാസീവ് (ഒളിഞ്ഞു കേൾക്കൽ) } \quad \text{vs} \quad \text{ആക്ടീവ് (ഡാറ്റ മാറ്റിയെഴുതൽ, DoS)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പാസീവ് അറ്റാക്കിൽ ഡാറ്റ മാറ്റമില്ലാതെ ചോർത്തുന്നു; ആക്ടീവ് അറ്റാക്കിൽ വ്യാജ സന്ദേശങ്ങളും മാറ്റങ്ങളും വരുത്തുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>പാസീവ് (സ്നിഫിംഗ്, ട്രാഫിക് അനാലിസിസ്), ആക്ടീവ് (സ്പൂഫിംഗ്, റീപ്ലേ, DoS) എന്നിവ ഉദാഹരണ സഹിതം എഴുതുക.</p>
</div>
""",
            'understand_simply': r"""
<p>രഹസ്യം ഒളിഞ്ഞു കേൾക്കുന്നത് പാസീവ് അറ്റാക്കും, കത്ത് തിരുത്തിയെഴുതുന്നത് ആക്ടീവ് അറ്റാക്കുമാണ്!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q33: Security Protocols: SSL, TLS, and Mobile VPN
    # -------------------------------------------------------------------------
    'mobile-q33': {
        'manglish': {
            'title': "Mobile networks-ile Security Protocols: SSL, TLS, and Mobile VPN detail aayi explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Secure Transport Protocols",
                'eq': r"$$\text{TLS 1.3: Asymmetric Handshake (ECDHE) } \to \text{ Symmetric Session Key (AES-GCM)} \to \text{Encrypted Tunnel}$$",
                'text': r"<strong>Ormavekkan:</strong> SSL obsolete aayi, TLS (Transport Layer Security) aanu modern standard (HTTPS). Mobile VPN (IPsec / WireGuard) cellular roaming-il IP address maarumbol polum secure encrypted tunnel intact aakki nirthunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <ol>
        <li><strong>SSL / TLS Architecture:</strong> Operates between Application Layer (HTTP) and Transport Layer (TCP).
            <ul>
                <li><strong>TLS Handshake Protocol:</strong> Server authenticates using X.509 certificate. Both parties agree on cipher suite and generate symmetric session key using Diffie-Hellman.</li>
                <li><strong>TLS Record Protocol:</strong> Encrypts application payloads using AES-GCM and verifies HMAC integrity.</li>
            </ul>
        </li>
        <li><strong>Mobile VPN (MOBIKE / IPsec):</strong> Traditional VPN network maarumbol disconnect aavum. Mobile VPN uses MOBIKE (IKEv2 Mobility) to seamlessly switch tunnels between Wi-Fi and 5G without re-login!</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Public Wi-Fi (railway station Wi-Fi) oru open road pole aanu &mdash; aarkkum nokkaam. TLS oru bulletproof tinted car pole aanu &mdash; akathirikkunna data purathullavarkku kaanan pattilla. Mobile VPN car Wi-Fi road-il ninnu 5G highway-ilekku maariyaalum travel stop aavathe protect cheyyunnu!</p>
"""
        },
        'ml': {
            'title': "സുരക്ഷാ പ്രോട്ടോക്കോളുകൾ: SSL, TLS, മൊബൈൽ വിപിഎൻ (VPN) എന്നിവ വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ സുരക്ഷിത പ്രോട്ടോക്കോളുകൾ",
                'eq': r"$$\text{HTTPS = HTTP + TLS എൻക്രിപ്ഷൻ ടണൽ}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഡാറ്റയെ പബ്ലിക് ഇന്റർനെറ്റിലൂടെ ആർക്കും ചോർത്താൻ കഴിയാത്ത സുരക്ഷിത തുരങ്കം വഴി കടത്തിവിടുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>TLS ഹാൻഡ്‌ഷേക്ക് ഘട്ടങ്ങളും മൊബൈൽ വിപിഎൻ റോമിംഗ് ഗുണങ്ങളും വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>തുറന്ന റോഡിലൂടെ പോകുന്നതിന് പകരം ആർക്കും കാണാൻ കഴിയാത്ത ഒരു ഭൂഗർഭ തുരങ്കത്തിലൂടെ സുരക്ഷിതമായി ഡാറ്റ അയക്കുന്നത് പോലെ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q34: Public Key Cryptography and Complete RSA Numerical
    # -------------------------------------------------------------------------
    'mobile-q34': {
        'manglish': {
            'title': "RSA Algorithm step-by-step working explain cheythu numerical solve cheyyuka ($p=3, q=11, e=7$).",
            'remember_this': {
                'title': "⚡ RSA Formula & Keys",
                'eq': r"$$n = p \cdot q, \quad \phi(n) = (p-1)(q-1), \quad e \cdot d \equiv 1 \pmod{\phi(n)}, \quad C = M^e \bmod n, \quad M = C^d \bmod n$$",
                'text': r"<strong>Ormavekkan:</strong> Public key $(e, n)$ &mdash; anyone can encrypt; Private key $(d, n)$ &mdash; only owner can decrypt! Large prime factorization difficulty aanu RSA-yude unbreakable security."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Numerical Solution</span></div>
    <p><strong>Step-by-Step Calculation:</strong></p>
    <ol>
        <li>Choose two prime numbers: $p = 3, \;\; q = 11$.</li>
        <li>Compute modulus: $n = p \cdot q = 3 \times 11 = 33$.</li>
        <li>Compute Euler totient: $\phi(n) = (p - 1)(q - 1) = (3 - 1)(11 - 1) = 2 \times 10 = 20$.</li>
        <li>Choose public exponent $e = 7$ (check $\gcd(7, 20) = 1$, valid!).</li>
        <li>Calculate private key $d$: $e \cdot d \equiv 1 \pmod{\phi(n)} \implies 7d \equiv 1 \pmod{20}$.
            <br>Multiples of 20: $21, 41, 61 \dots$ Notice that $7 \times 3 = 21 = 1 \pmod{20}$.
            <br>$\therefore d = 3$!</li>
        <li><strong>Encryption of Message $M = 2$:</strong>
            $$C = M^e \bmod n = 2^7 \bmod 33 = 128 \bmod 33 = 29$$
            $\therefore$ Ciphertext $C = 29$!</li>
        <li><strong>Decryption of Ciphertext $C = 29$:</strong>
            $$M = C^d \bmod n = 29^3 \bmod 33$$
            $29 \equiv -4 \pmod{33} \implies 29^3 \equiv (-4)^3 = -64 \pmod{33}$.
            $-64 + 2 \times 33 = -64 + 66 = 2$.
            $\therefore$ Decrypted Message $M = 2$! (Verified 100% correct).</li>
    </ol>
</div>
""",
            'understand_simply': r"""
<p>Padlock and Key analogy: Public key $(e, n)$ oru thuranna padlock aanu &mdash; lokathil aarkku venamenkilum aa lock vechu box poottam (Encryption). Pakshe aa lock thurakkan ulla orotta key $(d, n)$ ningalude kayyil mathrame ullu (Decryption)!</p>
"""
        },
        'ml': {
            'title': "RSA അൽഗോരിതം വിശദീകരിച്ച് ഉദാഹരണ കണക്ക് ചെയ്യുക ($p=3, q=11, e=7$)",
            'remember_this': {
                'title': "⚡ RSA സമവാക്യങ്ങൾ",
                'eq': r"$$n = p \cdot q, \quad C = M^e \bmod n, \quad M = C^d \bmod n$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> പബ്ലിക് കീ $(e, n)$ ഉപയോഗിച്ച് ആർക്കും എൻക്രിപ്റ്റ് ചെയ്യാം; പ്രൈവറ്റ് കീ $(d, n)$ ഉള്ളയാൾക്ക് മാത്രമേ ഡീക്രിപ്റ്റ് ചെയ്യാൻ സാധിക്കൂ."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം കണക്കുകൂട്ടൽ</span></div>
    <p>$p=3, q=11 \implies n=33, \phi(n)=20$. $e=7$ ആകുമ്പോൾ $d=3$. സന്ദേശം $M=2$ ആകുമ്പോൾ $C = 2^7 \bmod 33 = 29$. തിരികെ $M = 29^3 \bmod 33 = 2$ എന്ന് തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>തുറന്ന പൂട്ട് പബ്ലിക് കീയും, അത് തുറക്കാനുള്ള ഒരേയൊരു താക്കോൽ പ്രൈവറ്റ് കീയും ആയ അത്ഭുത ഗണിതശാസ്ത്ര വിദ്യ!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q35: Diffie-Hellman Key Exchange Algorithm
    # -------------------------------------------------------------------------
    'mobile-q35': {
        'manglish': {
            'title': "Diffie-Hellman Key Exchange Algorithm derivation-um numerical example-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Diffie-Hellman Shared Secret",
                'eq': r"$$K = (Y_B)^{X_A} \bmod q = (Y_A)^{X_B} \bmod q = \alpha^{X_A X_B} \bmod q$$",
                'text': r"<strong>Ormavekkan:</strong> Alice-um Bob-um insecure public channel vazhi secret share cheyyathe thanne ore shared symmetric key $K$ calculate cheyyunnu! Discrete Logarithm Problem solve cheyyan mathamatically kazhiyilla ennullathaanu security."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Step-by-Step Guide</span></div>
    <p>1. Global Public Parameters: Prime $q = 11$, Primitive root $\alpha = 2$.</p>
    <p>2. <strong>Alice:</strong> Selects secret private key $X_A = 3$. Calculates public key:
       $$Y_A = \alpha^{X_A} \bmod q = 2^3 \bmod 11 = 8$$
       Sends $Y_A = 8$ across public network to Bob.</p>
    <p>3. <strong>Bob:</strong> Selects secret private key $X_B = 4$. Calculates public key:
       $$Y_B = \alpha^{X_B} \bmod q = 2^4 \bmod 11 = 16 \bmod 11 = 5$$
       Sends $Y_B = 5$ across public network to Alice.</p>
    <p>4. <strong>Shared Secret Key Calculation:</strong>
       <br>Alice computes: $K = (Y_B)^{X_A} \bmod q = 5^3 \bmod 11 = 125 \bmod 11 = 4$.
       <br>Bob computes: $K = (Y_A)^{X_B} \bmod q = 8^4 \bmod 11 = 4096 \bmod 11 = 4$.
       <br>Both independently obtained identical key $K = 4$ without transmitting it!</p>
</div>
""",
            'understand_simply': r"""
<p>Paint mixing trick alochikku: Alice and Bob common yellow paint edukkunnu. Alice thante secret blue color mix cheythu intermediate color Bob-nu ayakkunnu. Bob thante secret red color mix cheythu Alice-nu ayakkunnu. Ippo randu perum avarkk kitiya mix-il thante secret color koodi add cheythaal, randu perkkum exact same final brown color kitum! Eavesdropper-nu intermediate mix kandu secret color theerumanikkan pattilla!</p>
"""
        },
        'ml': {
            'title': "ഡിഫി-ഹെൽമാൻ കീ എക്സ്ചേഞ്ച് അൽഗോരിതവും കണക്കുകൂട്ടലും വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ പങ്കിട്ട രഹസ്യ കീ",
                'eq': r"$$K = Y_B^{X_A} \bmod q = Y_A^{X_B} \bmod q$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> രഹസ്യ കീ പുറത്തുവിടാതെ തന്നെ രണ്ട് വ്യക്തികൾക്ക് ഒരേ പൊതു കീ ഉണ്ടാക്കിയെടുക്കാൻ സഹായിക്കുന്ന രീതി."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം കണക്കുകൂട്ടൽ</span></div>
    <p>$q=11, \alpha=2$ എടുത്ത് $X_A=3, X_B=4$ ആണെങ്കിൽ ഇരുവർക്കും ലഭിക്കുന്ന പൊതു കീ $K=4$ എന്ന് കണക്കുകൂട്ടി തെളിയിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>പെയിന്റുകൾ കൂട്ടിക്കലർത്തി പൊതുവായ ഒരു പുതിയ നിറം ഉണ്ടാക്കുന്നത് പോലെ ആർക്കും ചോർത്താനാവാത്ത രഹസ്യ കീ ഉണ്ടാക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q36: Orthogonal Frequency Division Multiplexing (OFDM)
    # -------------------------------------------------------------------------
    'mobile-q36': {
        'manglish': {
            'title': "OFDM (Orthogonal Frequency Division Multiplexing) principles-um Cyclic Prefix-um explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Orthogonality & Cyclic Prefix",
                'eq': r"$$\Delta f = \frac{1}{T_{\text{sym}}}, \quad \int_0^T \cos(2\pi f_i t)\cos(2\pi f_j t) dt = 0 \quad (i \ne j), \quad T_{CP} > \tau_{\max}$$",
                'text': r"<strong>Ormavekkan:</strong> High-speed serial stream-ne parallel low-speed subcarriers aakki split cheyyunnu. Subcarriers mathematically orthogonal aayathukond spectrum overlap cheythaalum zero interference! Cyclic prefix ISI (Inter-Symbol Interference) completely eliminate cheyyunnu (4G LTE, 5G, Wi-Fi 6)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>Orthogonal Subcarriers:</strong> Peak of one subcarrier occurs exactly at the zero-crossings of all other subcarriers ($\Delta f = 1/T_s$). No guard bands required, maximizing spectral efficiency!</p>
    <p>2. <strong>FFT / IFFT Implementation:</strong> Transmitter uses IFFT to convert frequency symbols into time domain; receiver uses FFT to decode.</p>
    <p>3. <strong>Cyclic Prefix (CP):</strong> End of the OFDM symbol is copied and pasted to the beginning. As long as $T_{CP} > \text{multipath delay spread } \tau_{\max}$, multipath reflections from tall buildings will fall inside CP and won't corrupt the main data symbol &mdash; zero Inter-Symbol Interference (ISI)!</p>
</div>
""",
            'understand_simply': r"""
<p>Oru valiya heavy load oru single big lorry-il kondupoyaal narrow road-il traffic block aavum (Single carrier ISI). Athinu pakaram 100 small auto-rickshaws-il aakki parallel aayi ayachaal (OFDM parallel subcarriers), oru road block aayalum delivery smooth aayi nadakkum! 4G, 5G, Wi-Fi ellaam ee auto-rickshaw fleet pole aanu!</p>
"""
        },
        'ml': {
            'title': "ഒഎഫ്ഡിഎം (OFDM) തത്വങ്ങളും സൈക്ലിക് പ്രിഫിക്സും (Cyclic Prefix) വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ OFDM തത്വം",
                'eq': r"$$\Delta f = \frac{1}{T_{sym}} \implies \text{ഇന്റർ-സിംബൽ ഇന്റർഫെറൻസ് (ISI) ഒഴിവാക്കുന്നു}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> ഒരു വലിയ ഡാറ്റയെ നിരവധി ചെറിയ സബ്-കാരിയറുകളാക്കി മാറ്റി സ്പെക്ട്രം കാര്യക്ഷമമായി ഉപയോഗിക്കുന്നു (4G, 5G, Wi-Fi 6)."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>ഓർത്തോഗൊണാലിറ്റി കണ്ടീഷൻ, IFFT/FFT പ്രോസസ്സിംഗ്, സൈക്ലിക് പ്രിഫിക്സ് ISI തടയുന്ന വിധം എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ഒരു വലിയ ലോറിക്ക് പകരം 100 ചെറിയ വണ്ടികളിൽ ഒരേസമയം سامانങ്ങൾ കയറ്റി അയക്കുന്നത് പോലെ സുഗമമായ ഡാറ്റാ വിനിമയം!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q37: Multimedia Broadcast and Multicast Services (MBMS) & MPLS
    # -------------------------------------------------------------------------
    'mobile-q37': {
        'manglish': {
            'title': "MBMS (Multimedia Broadcast Multicast Service) and MPLS in mobile cellular networks explain cheyyuka.",
            'remember_this': {
                'title': "⚡ Single Transmission for Millions",
                'eq': r"$$\text{Unicast: } N \text{ copies}; \quad \text{Multicast (MBMS): } 1 \text{ single radio broadcast copy for } N \text{ users!}$$",
                'text': r"<strong>Ormavekkan:</strong> Live cricket match stadium-il ulla 50,000 aalukal kaanumbol: Unicast aaneel tower collapse aavum! MBMS single radio stream broadcast cheythu ella phone-ilum deliver cheyyunnu. MPLS 20-bit short labels vechu core network-il ultra-fast routing tharunnu."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Study Guide</span></div>
    <p>1. <strong>MBMS Architecture:</strong> BM-SC (Broadcast Multicast Service Center) schedules live stream. Single packet stream flows from GGSN/PGW to cell towers. Over the air, all handsets in the cell tune to the same shared radio channel.</p>
    <p>2. <strong>MPLS (Multiprotocol Label Switching):</strong> Router long IP headers (32-bit/128-bit) complex routing table lookup cheyyunnathinu pakaram, simple 20-bit numeric labels swap cheythu high-speed hardware forwarding nadathunnu. Guarantees QoS and traffic engineering in mobile backhaul.</p>
</div>
""",
            'understand_simply': r"""
<p>TV broadcast vs Individual phone calls: 10,000 aalukal TV-il live match kaanumbol Doordarshan oro aalkkum separate cable idunnundo? Illa &mdash; single broadcast signal mathi! Ithanu MBMS. Tower collapse aavathe live video lakshakkinakkinu aalukalilekk ethikkunnu!</p>
"""
        },
        'ml': {
            'title': "മൾട്ടിമീഡിയ ബ്രോഡ്കാസ്റ്റ് മൾട്ടികാസ്റ്റ് സർവ്വീസും (MBMS) MPLS-ഉം വിശദീകരിക്കുക",
            'remember_this': {
                'title': "⚡ ബ്രോഡ്കാസ്റ്റ് കാര്യക്ഷമത",
                'eq': r"$$\text{ഒറ്റ ട്രാൻസ്മിഷൻ വഴി ഒരേസമയം ലക്ഷക്കണക്കിന് ആളുകൾക്ക് തത്സമയ സ്ട്രീമിംഗ്}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> തത്സമയ ക്രിക്കറ്റ് മത്സരങ്ങളും വാർത്തകളും നെറ്റ്‌വർക്ക് ജാമാവാതെ എല്ലാവരിലേക്കും എത്തിക്കാൻ MBMS സഹായിക്കുന്നു."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം പഠന സഹായി</span></div>
    <p>BM-SC നോഡ്, ഷെയർഡ് റേഡിയോ ചാനൽ, MPLS ലേബൽ സ്വിച്ചിംഗ് എന്നിവ വിശദീകരിക്കുക.</p>
</div>
""",
            'understand_simply': r"""
<p>ടിവിയിൽ ഒരേസമയം എല്ലാവരും ക്രിക്കറ്റ് കളി കാണുന്നത് പോലെ ഒരു നെറ്റ്‌വർക്ക് സ്ട്രീം കൊണ്ട് ലക്ഷക്കണക്കിന് ആളുകളിലേക്ക് വീഡിയോ എത്തിക്കുന്നു!</p>
"""
        }
    },

    # -------------------------------------------------------------------------
    # mobile-q38: Cellular Network Evolution (2G to 5G)
    # -------------------------------------------------------------------------
    'mobile-q38': {
        'manglish': {
            'title': "Cellular Network Generations: 2G muthal 5G vareyulla architectural and performance comparison explain cheyyuka.",
            'remember_this': {
                'title': "⚡ 2G to 5G Evolution Metric",
                'eq': r"$$\text{2G: 64 kbps (Voice)} \to \text{3G: 2 Mbps (Data)} \to \text{4G: 100 Mbps (All-IP)} \to \text{5G: 20 Gbps, } <1\text{ ms (eMBB, URLLC, mMTC)}$$",
                'text': r"<strong>Ormavekkan:</strong> 2G Circuit switched TDMA voice; 3G WCDMA mobile internet; 4G All-IP LTE OFDM (Flat architecture, EPC); 5G Service-Based Architecture (SBA), Network Slicing, Massive MIMO, and mmWave."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🌴 Manglish Evolution Guide</span></div>
    <table class="exam-table">
        <thead><tr><th>Generation</th><th>Primary Technology</th><th>Peak Data Rate</th><th>Latency</th><th>Core Network Architecture</th><th>Key Services</th></tr></thead>
        <tbody>
            <tr><td><strong>2G (GSM)</strong></td><td>TDMA / FDMA</td><td>$64\text{ kbps}$</td><td>$300\text{--}500\text{ ms}$</td><td>Circuit Switched (MSC, HLR, VLR)</td><td>Digital voice calls, SMS</td></tr>
            <tr><td><strong>3G (UMTS)</strong></td><td>W-CDMA</td><td>$2\text{ Mbps}$</td><td>$100\text{--}150\text{ ms}$</td><td>Dual (Circuit voice + Packet GPRS)</td><td>Mobile web browsing, video calls</td></tr>
            <tr><td><strong>4G (LTE)</strong></td><td>OFDMA + SC-FDMA</td><td>$100\text{--}1000\text{ Mbps}$</td><td>$20\text{--}40\text{ ms}$</td><td>All-IP Flat Evolved Packet Core (EPC)</td><td>HD video streaming, VoLTE</td></tr>
            <tr><td><strong>5G (NR)</strong></td><td>Scalable OFDMA + Massive MIMO</td><td>$10\text{--}20\text{ Gbps}$</td><td>$<1\text{ ms}$</td><td>Cloud-Native Service Based Architecture (SBA)</td><td>eMBB, URLLC (remote surgery), mMTC (IoT)</td></tr>
        </tbody>
    </table>
</div>
""",
            'understand_simply': r"""
<p>Vandi speed evolution pole aanu: <strong>2G</strong> oru cycle pole (basic SMS/Voice). <strong>3G</strong> oru scooter pole (photos and email). <strong>4G</strong> oru sports car pole (YouTube HD video streaming). <strong>5G</strong> oru rocket pole (ultra-low latency, self-driving autonomous cars, robotic remote surgery, and smart cities)!</p>
"""
        },
        'ml': {
            'title': "സെല്ലുലാർ നെറ്റ്‌വർക്ക് പരിണാമം: 2G മുതൽ 5G വരെയുള്ള മാറ്റങ്ങൾ താരതമ്യം ചെയ്യുക",
            'remember_this': {
                'title': "⚡ തലമുറകളുടെ പരിണാമം",
                'eq': r"$$\text{2G (വോയ്സ്) } \to \text{ 3G (വെബ്) } \to \text{ 4G (വീഡിയോ) } \to \text{ 5G (അതിവേഗം, IoT, റോബോട്ടിക്സ്)}$$",
                'text': r"<strong>ഓർത്തു വെക്കാൻ:</strong> വേഗത കിലോബൈറ്റിൽ നിന്നും ഗിഗാബൈറ്റിലേക്കും, ലേറ്റൻസി മില്ലിസെക്കൻഡിൽ താഴേക്കും കുറഞ്ഞ സാങ്കേതിക കുതിപ്പ്."
            },
            'exam_guide': r"""
<div class="local-lang-guide">
    <div class="lang-guide-banner"><span class="guide-badge">🇮🇳 മലയാളം താരതമ്യം</span></div>
    <p>ടേബിളിൽ സ്പീഡ്, ലേറ്റൻസി, പ്രോട്ടോക്കോൾ, ആർക്കിടെക്ചർ, സേവനങ്ങൾ എന്നിവ വ്യക്തമായി താരതമ്യം ചെയ്യുക.</p>
</div>
""",
            'understand_simply': r"""
<p>സൈക്കിളിൽ (2G) നിന്ന് തുടങ്ങി റോക്കറ്റ് വേഗതയിലേക്ക് (5G) കുതിച്ചുയർന്ന മൊബൈൽ സാങ്കേതിക വിപ്ലവം!</p>
"""
        }
    }
}
