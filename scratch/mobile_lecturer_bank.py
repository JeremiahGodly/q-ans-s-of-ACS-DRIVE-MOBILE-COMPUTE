# scratch/mobile_lecturer_bank.py
# Complete KTU Exam-Ready Answers for Subject 3: Mobile Computing (CST415)
# Written in simple, direct local English with rich core content, clear bullet points,
# step-by-step protocols, comparison tables, and intuitive everyday engineering analogies.

MOBILE_ANSWERS = {
    # =========================================================================
    # MODULE 1: Mobile Computing Architecture, Three-Tier Design & Context
    # =========================================================================
    'mobile-q1': {
        "title": "Middleware Components and Gateways in Mobile Computing",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Middleware abstracts heterogeneous devices and OS platforms; Gateways bridge wireless and wired networks with protocol translation and content transcoding."
        },
        "exam_answer": r"""
<p><strong>1. Role of Middleware in Mobile Computing:</strong></p>
<ul>
    <li><strong>Definition:</strong> Middleware is a software abstraction layer situated between heterogeneous client mobile operating systems (Android, iOS) and backend enterprise server databases.</li>
    <li><strong>Core Functions:</strong>
        <ul>
            <li><strong>Data Synchronization &amp; Offline Caching:</strong> Stores data locally (SQLite) when the device is disconnected, and automatically synchronizes updates with the enterprise server upon reconnection.</li>
            <li><strong>RPC &amp; Asynchronous Message Queuing:</strong> Enables remote procedure calls across unreliable, high-latency wireless links.</li>
            <li><strong>Location &amp; Context Management:</strong> Collects GPS, network cell ID, and sensor data, presenting uniform APIs to applications.</li>
        </ul>
    </li>
</ul>

<p><strong>2. Role of Mobile Gateways:</strong></p>
<ul>
    <li><strong>Definition:</strong> Network translation servers that connect wireless cellular/WLAN access networks to the wired Internet backbone.</li>
    <li><strong>Core Functions:</strong>
        <ul>
            <li><strong>Protocol Conversion:</strong> Translates lightweight mobile-optimized protocols (WAP, CoAP, MQTT) to standard wired protocols (HTTP/TCP/IP).</li>
            <li><strong>Content Adaptation &amp; Transcoding:</strong> Dynamically compresses large images, strips unnecessary HTML/CSS, and converts media formats to match mobile screen resolutions and bandwidth constraints.</li>
            <li><strong>Security Enforcement:</strong> Terminates mobile wireless encryption tunnels (WTLS) and establishes wired SSL/TLS sessions to enterprise servers.</li>
        </ul>
    </li>
</ul>
""",
        "understand_simply": r"""
<p>Think of traveling to a foreign country:</p>
<ul>
    <li><strong>Middleware:</strong> A universal power adapter that lets your laptop plug into any wall socket regardless of the local voltage or plug shape.</li>
    <li><strong>Gateway:</strong> A bilingual airport customs officer who translates foreign documents and shrinks bulky luggage so it fits into an overhead cabin locker!</li>
</ul>
"""
    },

    'mobile-q2': {
        "title": "The Internet as the Ubiquitous Backbone of Mobile Computing",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "The Internet provides a vendor-neutral, packet-switched IP foundation connecting cellular (4G/5G) and Wi-Fi networks to cloud services."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Role:</strong><br>
The Internet acts as the universal, packet-switched transport backbone that interconnects diverse mobile wireless access networks (Cellular 3G/4G/5G, Wi-Fi, Satellite) with backend cloud data centers and enterprise services.</p>

<p><strong>2. Core Functions as a Backbone:</strong></p>
<ol>
    <li><strong>Universal IP Interoperability:</strong> TCP/IP (IPv4/IPv6) provides a vendor-neutral network protocol. A mobile phone on cellular data communicates seamlessly with a web server on a fiber-optic LAN.</li>
    <li><strong>Support for Mobile IP:</strong> Mobile IP protocols (Home Agent, Foreign Agent, Care-of-Address) allow mobile nodes to maintain active TCP connections and session continuity while roaming across different IP subnets.</li>
    <li><strong>Content Delivery &amp; Cloud Scalability:</strong> Cloud servers and Content Delivery Networks (CDNs) cache media geographically close to mobile base stations, drastically reducing latency for mobile clients.</li>
    <li><strong>Decoupling Access Technology from Applications:</strong> End-user applications (WhatsApp, Banking, Streaming) run identically whether the mobile station is connected via 5G, Wi-Fi 6, or satellite.</li>
</ol>
""",
        "understand_simply": r"""
<p>The Internet is like the national highway network. Whether you travel to the highway entrance on a bicycle (Wi-Fi), an auto-rickshaw (4G), or an electric scooter (5G), once you merge onto the highway (the Internet backbone), everyone travels along the same smooth multi-lane road to reach any destination in the country.</p>
"""
    },

    'mobile-q3': {
        "title": "Network Segmentation: Core Network, Edge Network, and Access Network",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Access Network: Over-the-air radio connection (RAN); Edge Network: Local routing & caching (MEC); Core Network: Central switching, authentication, and billing."
        },
        "exam_answer": r"""
<p>Mobile telecommunication architectures segment network infrastructure into three distinct hierarchical tiers to optimize latency, scalability, and security:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Segment</th>
            <th>Components &amp; Technologies</th>
            <th>Primary Functions</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Access Network (RAN)</strong></td>
            <td>Radio towers, antennas, Base Transceiver Stations (BTS/NodeB/gNodeB), Wi-Fi Access Points (APs).</td>
            <td>Manages physical radio frequency transmission over the air ($U_m$ interface), modulation, channel coding, and mobile station association.</td>
        </tr>
        <tr>
            <td><strong>Edge Network</strong></td>
            <td>Base Station Controllers (BSC/RNC), Multi-access Edge Computing (MEC) servers, local security gateways.</td>
            <td>Handles local packet routing, intra-radio handovers, radio resource management, and edge caching to reduce latency.</td>
        </tr>
        <tr>
            <td><strong>Core Network</strong></td>
            <td>MSC, SGSN/GGSN, 5G UPF/AMF, HLR/HSS subscriber databases, AuC, billing servers.</td>
            <td>Centralized call switching, end-to-end IP routing, subscriber mobility management, global authentication, and charging/CDR generation.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Think of postal mail delivery in Kerala:</p>
<ul>
    <li><strong>Access Network:</strong> The local postman visiting your house on a motorbike to drop off your letters.</li>
    <li><strong>Edge Network:</strong> The town post office sorting letters for nearby neighborhoods.</li>
    <li><strong>Core Network:</strong> The central state sorting hub in Ernakulam directing mail trucks across India and maintaining master address records.</li>
</ul>
"""
    },

    'mobile-q4': {
        "title": "Intrinsic Physical Limitations of Mobile Computing Environments",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Bottlenecks: Limited battery energy, hostile wireless channel (fading/interference), handheld form-factor constraints, and vulnerability to theft/interception."
        },
        "exam_answer": r"""
<p>Mobile computing faces four fundamental physical and technical constraints compared to fixed desktop computing:</p>
<ol>
    <li><strong>Finite Battery Energy Storage:</strong> Mobile devices depend on electrochemical lithium-ion batteries with limited energy density. Power consumption from radio transmission, CPU processing, and screen backlighting must be strictly optimized to prevent premature battery drain.</li>
    <li><strong>Hostile &amp; Variable Wireless Channels:</strong> Radio channels suffer from severe path loss, multipath fading, Doppler frequency shift, shadowing from buildings, and radio interference, resulting in unpredictable bandwidth and packet loss.</li>
    <li><strong>Resource &amp; Ergonomic Constraints:</strong> Handheld form factors limit physical dimensions, thermal dissipation without cooling fans, memory (RAM), processor clock frequency, and screen size.</li>
    <li><strong>Heightened Security Vulnerability:</strong> Portable devices are easily lost or stolen, risking data exposure. Broadcast radio channels are inherently open to eavesdropping and jamming by malicious adversaries.</li>
</ol>
""",
        "understand_simply": r"""
<p>A desktop PC at an office is plugged into unlimited wall power and high-speed fiber internet. A mobile phone is like a hiker in the forest: it has only a small water bottle (battery), must communicate by shouting through stormy weather (wireless interference), and carries only what fits into a small pocket backpack (compact processor and memory)!</p>
"""
    },

    'mobile-q5': {
        "title": "Comprehensive Three-Tier Architecture of Mobile Computing Systems",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Tier 1: Presentation (Thin/Fat Client) $\\leftrightarrow$ Tier 2: Application/Logic (Middleware/Gateways) $\\leftrightarrow$ Tier 3: Enterprise Data (RDBMS/Cloud)."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Overview:</strong><br>
The three-tier architecture separates mobile application responsibilities into three distinct layers to minimize wireless transmission overhead and overcome mobile device limitations:</p>

<p><strong>2. Tier 1: Presentation Layer (Client Tier):</strong></p>
<ul>
    <li>Runs directly on the user's mobile device (smartphone, tablet).</li>
    <li>Responsible for capturing user inputs, displaying graphics, and rendering responses.</li>
    <li><strong>Thin Client Model:</strong> Uses a mobile web browser. All business logic and rendering calculations are offloaded to Tier 2. Requires continuous network connectivity.</li>
    <li><strong>Fat Client Model:</strong> Native mobile app (Android APK / iOS). Contains local caching (SQLite) and local business logic, allowing full offline operation when network connectivity is lost.</li>
</ul>

<p><strong>3. Tier 2: Application / Business Logic Layer (Middleware Tier):</strong></p>
<ul>
    <li>Runs on powerful backend application servers, web servers, or mobile enterprise application platforms (MEAP).</li>
    <li>Executes business algorithms, evaluates transaction rules, and handles user authentication and session states.</li>
    <li><strong>Content Adaptation &amp; Transcoding:</strong> Shrinks image resolutions, strips heavy HTML tags, and transcodes multimedia files into mobile-friendly formats before transmission.</li>
    <li><strong>Data Synchronization Manager:</strong> Resolves synchronization conflicts between cached mobile client updates and master databases.</li>
</ul>

<p><strong>4. Tier 3: Data / Enterprise Tier (Database Layer):</strong></p>
<ul>
    <li>Comprises relational database management systems (Oracle, MySQL, PostgreSQL), mainframe databases, and enterprise cloud storage.</li>
    <li>Guarantees ACID transaction properties, persistent storage, security, and integration with legacy banking/ERP systems.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of ordering food at a restaurant:</p>
<ul>
    <li><strong>Tier 1 (Presentation):</strong> The customer looking at the printed menu and placing an order.</li>
    <li><strong>Tier 2 (Application / Middleware):</strong> The waiter who takes the order, checks with the chef, translates special food requests, and serves the meal.</li>
    <li><strong>Tier 3 (Data):</strong> The kitchen pantry and refrigerator where ingredients are stored securely.</li>
</ul>
"""
    },

    'mobile-q6': {
        "title": "Comprehensive Design Considerations for Mobile Computing Systems",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Design pillars: Energy efficiency, network heterogeneity & disconnected operation, context awareness, data synchronization, and end-to-end security."
        },
        "exam_answer": r"""
<p>Architecting software and network systems for mobile environments requires addressing unique operational challenges across five design pillars:</p>
<ol>
    <li><strong>Energy Awareness &amp; Power Optimization:</strong>
        <ul>
            <li>Mobile devices operate on battery power. Software must minimize radio wake-ups by batching data requests together.</li>
            <li>Use power-efficient sleep states, low-power display modes (dark themes), and avoid aggressive background CPU polling.</li>
        </ul>
    </li>
    <li><strong>Support for Disconnected &amp; Weakly Connected Operation:</strong>
        <ul>
            <li>Mobile devices regularly lose signal in elevators, basements, or rural areas.</li>
            <li>Applications must support <em>hoarding/prefetching</em> and local persistent caching so users can continue working offline.</li>
            <li>Implement asynchronous optimistic replication with automated conflict resolution when connectivity resumes.</li>
        </ul>
    </li>
    <li><strong>Adaptive Quality of Service (QoS) &amp; Network Heterogeneity:</strong>
        <ul>
            <li>Devices switch dynamically between 5G, 4G, and Wi-Fi. Software must dynamically adjust video bitrates and payload compression to match changing bandwidth.</li>
        </ul>
    </li>
    <li><strong>Context-Aware Adaptation:</strong>
        <ul>
            <li>Applications should adapt behavior based on physical location (GPS), user speed, ambient light, battery percentage, and network cost (Wi-Fi vs metered cellular).</li>
        </ul>
    </li>
    <li><strong>End-to-End Security &amp; Privacy:</strong>
        <ul>
            <li>Enforce multi-factor authentication, biometric logins, on-device encryption (AES-256 for local SQLite), and secure socket communication (TLS 1.3) to safeguard lost or stolen devices.</li>
        </ul>
    </li>
</ol>
""",
        "understand_simply": r"""
<p>Designing a desktop app is like designing a boat for a calm indoor swimming pool. Designing a mobile app is like building a boat for the rough open sea: it must survive sudden storms (lost network signal), carry its own emergency fresh water (battery energy), and carry spare navigation maps (offline local caching)!</p>
"""
    },

    'mobile-q7': {
        "title": "Context-Aware System Management in Mobile Computing",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Context components: User context (identity, preferences), Physical context (location, sensors), Network context (bandwidth, cost), Device context (battery, RAM)."
        },
        "exam_answer": r"""
<p><strong>1. Definition of Context Awareness:</strong><br>
A system is <strong>context-aware</strong> if it uses contextual information about its operating environment to dynamically adapt its behavior, interface, and services without explicit manual user intervention.</p>

<p><strong>2. Categories of Contextual Information:</strong></p>
<ul>
    <li><strong>Physical &amp; Environmental Context:</strong> Current geographical location (GPS coordinates, cell ID), velocity/motion (accelerometer), orientation (gyroscope), ambient light level, and temperature.</li>
    <li><strong>Device Context:</strong> Remaining battery capacity, CPU workload, available RAM, screen size, and audio output mode (earphones vs loudspeaker).</li>
    <li><strong>Network &amp; Communication Context:</strong> Connected interface type (Wi-Fi vs 5G), network bandwidth, transmission latency, signal strength (RSSI), and connection monetary cost.</li>
    <li><strong>User &amp; Social Context:</strong> User identity, calendar schedule (e.g., "In a Meeting"), user activity (walking, driving, sleeping), and privacy preferences.</li>
</ul>

<p><strong>3. Four Core Context Managers in Mobile Architecture:</strong></p>
<ol>
    <li><strong>Client Context Manager:</strong> Gathers raw sensor and hardware readings, filters out sensor noise, and converts raw data into high-level context events (e.g., converting accelerometer shakes into "User is Driving").</li>
    <li><strong>Policy Manager:</strong> Evaluates business rules and user preferences against the current context (e.g., "IF Battery &lt; 20% THEN disable automatic video playback").</li>
    <li><strong>Adaptability Manager:</strong> Executes adaptation actions—such as transcoding images, toggling screen brightness, or switching from cellular to Wi-Fi.</li>
    <li><strong>Security &amp; Privacy Manager:</strong> Enforces access permissions, ensuring location and health context are shared only with authorized applications.</li>
</ol>
""",
        "understand_simply": r"""
<p>Context awareness is like having an attentive personal assistant: when you enter a movie theater, your assistant automatically mutes your ringtone; when you start driving your car, it switches your maps to large bold buttons and reads text messages aloud; and when your battery drops below $15\%$, it dims the screen without you asking!</p>
"""
    },

    'mobile-q8': {
        "title": "Content Adaptation Attributes and Classifications of Transcoding",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Transcoding transforms media to fit device constraints; Classified into Syntactic (format), Structural (layout/compression), and Semantic (content substitution)."
        },
        "exam_answer": r"""
<p><strong>1. Concept of Content Adaptation:</strong><br>
Content adaptation dynamically modifies multimedia resources (images, video, web documents) on intermediate gateways or proxy servers before delivery, ensuring content displays perfectly on resource-constrained mobile devices.</p>

<p><strong>2. Three Major Classifications of Transcoding:</strong></p>
<ol>
    <li><strong>Syntactic Transcoding (Format Conversion):</strong>
        <ul>
            <li>Modifies the data representation syntax without altering the underlying content or structure.</li>
            <li><strong>Examples:</strong> Converting a desktop BMP or PNG image into a compressed WebP/JPEG format; converting an uncompressed WAV audio file into MP3/AAC; converting a PDF document into plain text.</li>
        </ul>
    </li>
    <li><strong>Structural Transcoding (Content Re-structuring &amp; Scaling):</strong>
        <ul>
            <li>Alters the internal structure, dimensions, and visual density of content to suit small mobile displays and low bandwidth.</li>
            <li><strong>Examples:</strong>
                <ul>
                    <li>Image spatial downscaling: Resizing a $4K$ ($3840 \times 2160$) image down to mobile screen resolution ($720 \times 1280$).</li>
                    <li>Video temporal subsampling: Reducing video frame rate from $60\text{ fps}$ to $24\text{ fps}$ on slow 3G networks.</li>
                    <li>Document splitting: Breaking a heavy 20-page web portal into numbered mobile pages.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Semantic Transcoding (Information Substitution):</strong>
        <ul>
            <li>Replaces high-bandwidth media items with completely different semantic representations that convey the same core message.</li>
            <li><strong>Examples:</strong>
                <ul>
                    <li>Replacing an embedded video stream with a static thumbnail image containing a text summary.</li>
                    <li>Replacing an image banner with its HTML <code>alt</code> text description when the user is on an emergency low-battery mode.</li>
                    <li>Converting voice messages into text via speech-to-text engines.</li>
                </ul>
            </li>
        </ul>
    </li>
</ol>
""",
        "understand_simply": r"""
<p>Think of packing a large tent into a small backpack:</p>
<ul>
    <li><strong>Syntactic:</strong> Rolling the canvas into a different shape so it fits in the bag.</li>
    <li><strong>Structural:</strong> Leaving behind the heavy steel poles and using lightweight folding aluminum poles instead.</li>
    <li><strong>Semantic:</strong> Leaving the tent at home entirely and packing a lightweight emergency rain poncho instead!</li>
</ul>
"""
    },

    'mobile-q9': {
        "title": "Seamless Communication and Essential Facets Maintained During Roaming",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Seamless roaming maintains: Session continuity (TCP/IP), Quality of Service (QoS), Security credentials, and Charging/Accounting without call drops."
        },
        "exam_answer": r"""
<p><strong>1. Concept of Seamless Communication:</strong><br>
Seamless communication enables a mobile subscriber to maintain continuous, uninterrupted active voice calls, video streaming, and data sessions while physically moving across different cell boundaries, radio technologies (e.g., Wi-Fi to 5G), or different telecom operators without noticeable interruption.</p>

<p><strong>2. Four Essential Facets Maintained During Seamless Handover:</strong></p>
<ol>
    <li><strong>Session &amp; Network Continuity:</strong>
        <ul>
            <li>Active TCP connections and application sessions must not reset when IP address changes.</li>
            <li>Achieved through Mobile IP (using Home Agent / Care-of-Address tunneling) or Session Initiation Protocol (SIP) re-INVITE procedures.</li>
        </ul>
    </li>
    <li><strong>Quality of Service (QoS) &amp; Latency Guarantees:</strong>
        <ul>
            <li>The target network cell must reserve sufficient bandwidth and radio channel capacity before the mobile station breaks connection with the old cell (<em>Make-Before-Break soft handover</em>).</li>
            <li>Handover latency must remain under $50\text{ ms}$ for real-time voice calls to prevent audible clicks or call drops.</li>
        </ul>
    </li>
    <li><strong>Security Association &amp; Mutual Authentication:</strong>
        <ul>
            <li>User encryption keys ($K_c$) and security contexts must transfer securely between base stations without requiring the user to re-enter passwords. Fast BSS Transition (IEEE 802.11r) caches security keys to avoid full re-authentication delays.</li>
        </ul>
    </li>
    <li><strong>Accounting, Billing &amp; Location Management:</strong>
        <ul>
            <li>Network databases (HLR, VLR) must update the subscriber's location area immediately so incoming calls are routed accurately. Call Detail Records (CDRs) must combine split billing records accurately across foreign networks.</li>
        </ul>
    </li>
</ol>
""",
        "understand_simply": r"""
<p>Seamless communication is like talking on a phone call while riding on a train. As your phone leaves one mobile tower and connects to the next tower 5 km away, the handover happens so fast (in milliseconds) that neither you nor the person on the other end ever hears a single glitch or silence!</p>
"""
    },

    # =========================================================================
    # MODULE 2: Communication Systems, Multiple Access & GSM Architecture
    # =========================================================================
    'mobile-q10': {
        "title": "Comparative Analysis of Satellite Systems: GEO, LEO, and MEO",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "GEO: 36,000 km, stationary, high latency (250 ms), 3 satellites for global cover; LEO: 500-1500 km, low latency (10-30 ms), constellation of 66+."
        },
        "exam_answer": r"""
<p>Satellite communication systems are classified by their orbital altitude, propagation latency, and footprint coverage:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>GEO (Geostationary Earth Orbit)</th>
            <th>MEO (Medium Earth Orbit)</th>
            <th>LEO (Low Earth Orbit)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Orbital Altitude</strong></td>
            <td>$\approx 35,786\text{ km}$ (circular equatorial).</td>
            <td>$5,000\text{ to } 20,000\text{ km}$.</td>
            <td>$500\text{ to } 1,500\text{ km}$.</td>
        </tr>
        <tr>
            <td><strong>Round-Trip Delay (Latency)</strong></td>
            <td>High: $250\text{ to } 280\text{ ms}$ (causes noticeable voice lag).</td>
            <td>Moderate: $70\text{ to } 120\text{ ms}$.</td>
            <td>Low: $10\text{ to } 30\text{ ms}$ (comparable to terrestrial cellular/broadband).</td>
        </tr>
        <tr>
            <td><strong>Global Coverage Constellation</strong></td>
            <td>Minimum <strong>3 satellites</strong> provide near-global coverage (excluding polar regions).</td>
            <td><strong>10 to 12 satellites</strong> in multiple inclined orbits.</td>
            <td>Large constellations: <strong>66 to thousands</strong> of satellites required (e.g., Iridium, Starlink).</td>
        </tr>
        <tr>
            <td><strong>Handset Power &amp; Tracking</strong></td>
            <td>Requires fixed high-gain directional dishes; Doppler shift is zero.</td>
            <td>Moderate power; tracking antennas required.</td>
            <td>Compact handheld omnidirectional antennas; rapid satellite handover and high Doppler shift.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Imagine lighting up a stadium:</p>
<ul>
    <li><strong>GEO:</strong> One giant spotlight mounted on a mountain 35 km away. It lights the whole stadium, but the beam takes noticeable time to travel back and forth.</li>
    <li><strong>LEO:</strong> A swarm of small camera drones flying just 50 meters above the grass. Each drone covers only a small patch, so you need dozens of them—but the light reaches the ground with zero delay!</li>
</ul>
"""
    },

    'mobile-q11': {
        "title": "Mobile Station Identifiers: IMEI, IMSI, MSISDN, and TMSI",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "IMEI = Handset hardware; IMSI = Subscriber SIM secret; MSISDN = Public phone number; TMSI = Temporary radio privacy pseudonym."
        },
        "exam_answer": r"""
<p>GSM cellular networks use four distinct identifiers to distinguish handsets, subscriber subscriptions, public phone numbers, and radio security:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Identifier</th>
            <th>Full Name &amp; Format</th>
            <th>Storage Location</th>
            <th>Primary Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>IMEI</strong></td>
            <td><strong>International Mobile Equipment Identity</strong><br>15 decimal digits ($TAC + SNR + CD$)</td>
            <td>Handset hardware (EEPROM); EIR database</td>
            <td>Identifies the physical mobile phone device. Used by EIR to blacklist stolen or non-certified handsets.</td>
        </tr>
        <tr>
            <td><strong>IMSI</strong></td>
            <td><strong>International Mobile Subscriber Identity</strong><br>Max 15 digits ($MCC + MNC + MSIN$)</td>
            <td>SIM card; HLR &amp; VLR databases</td>
            <td>Uniquely identifies the subscriber within the global cellular network. Never exposed publicly.</td>
        </tr>
        <tr>
            <td><strong>MSISDN</strong></td>
            <td><strong>Mobile Station ISDN Number</strong><br>Up to 15 digits ($CC + NDC + SN$)</td>
            <td>HLR database (mapped to IMSI); phone directory</td>
            <td>The public telephone number dialed by external callers to reach the subscriber.</td>
        </tr>
        <tr>
            <td><strong>TMSI</strong></td>
            <td><strong>Temporary Mobile Subscriber Identity</strong><br>4 bytes (local hex code)</td>
            <td>VLR database; stored temporarily in SIM</td>
            <td>Temporary pseudonym assigned locally by VLR to prevent eavesdroppers from tracking subscriber location over the radio link.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Think of traveling through an international airport:</p>
<ul>
    <li><strong>IMEI:</strong> The serial number stamped on your laptop. It identifies the metal machine, not the person carrying it.</li>
    <li><strong>IMSI:</strong> Your confidential national ID / passport number. The network uses this secret number to look up your account.</li>
    <li><strong>MSISDN:</strong> Your public phone number printed on your business card that friends use to call you.</li>
    <li><strong>TMSI:</strong> The temporary visitor sticker badge clipped to your shirt at security. It hides your real passport number from strangers in the hallway.</li>
</ul>
"""
    },

    'mobile-q12': {
        "title": "Call Progress Indication Mechanisms in Cellular Telephony",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Signaling messages (Alerting, Connect, Progress) inform user of call status via in-band tones (dial tone, ringback) and out-of-band screen notifications."
        },
        "exam_answer": r"""
<p><strong>1. Purpose of Call Progress Indication:</strong><br>
Informs the calling subscriber about the status of an ongoing call setup attempt through audible acoustic tones and digital visual screen messages.</p>

<p><strong>2. Core Progress States &amp; Signals:</strong></p>
<ol>
    <li><strong>Dial Tone:</strong> Confirms that the mobile station has acquired a dedicated control channel (SDCCH) and the network is ready to receive dialed digits.</li>
    <li><strong>Ringback Tone (Audible Ringing):</strong> Generated when the destination MSC confirms the called mobile is reachable, channel assigned, and ringing (signaled via SS7 / ISUP <code>Address Complete Message (ACM)</code>).</li>
    <li><strong>Busy Tone:</strong> Indicates that the called subscriber is currently engaged in another call (without call waiting active).</li>
    <li><strong>Fast Busy (Reorder Tone):</strong> Indicates that network trunk circuits or radio channels are fully congested.</li>
    <li><strong>Recorded Announcements:</strong> Spoken voice notifications triggered by network routing failures: "The number you have dialed is currently switched off or out of coverage area."</li>
</ol>
<p><strong>Mechanisms:</strong> Delivered as <em>in-band</em> audio tones over the traffic channel (TCH) or as <em>out-of-band</em> digital signaling packets (e.g., SIP <code>180 Ringing</code>, <code>486 Busy Here</code>) displayed as text prompts on modern smartphones.</p>
""",
        "understand_simply": r"""
<p>When you dial a friend's phone number, Call Progress Indication is the sequence of auditory feedback you hear in your ear: the initial click, the rhythmic "trr-trr" ringing sound, or the voice saying "Subscriber is out of coverage." It keeps you informed so you know whether the call is connecting or failing.</p>
"""
    },

    'mobile-q13': {
        "title": "Multiple Access Procedures: FDMA, TDMA, CDMA, and SDMA",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": r"$$\text{FDMA: Split Freq; TDMA: Split Time Slots; CDMA: Unique Orthogonal Codes } (c_i \cdot c_j = 0); \text{SDMA: Spatial Beams}$$",
            "text": "Multiple access allows hundreds of mobile subscribers to share the same limited radio spectrum without mutual interference."
        },
        "exam_answer": r"""
<p>Multiple access techniques allow multiple mobile users to share common radio bandwidth simultaneously. The four foundational techniques are compared below:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Technique</th>
            <th>Division Criterion</th>
            <th>Operating Principle</th>
            <th>Primary Examples</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>FDMA</strong><br>(Frequency Division)</td>
            <td>Frequency spectrum is split into dedicated narrowband channels.</td>
            <td>Each user is assigned a unique carrier frequency for the entire call duration. Users must not transmit on adjacent channels (requires guard bands).</td>
            <td>1G AMPS, traditional FM radio.</td>
        </tr>
        <tr>
            <td><strong>TDMA</strong><br>(Time Division)</td>
            <td>A shared radio carrier is divided into cyclical time slots.</td>
            <td>Users share the same carrier frequency, but transmit in non-overlapping, periodic time slots (e.g., 8 time slots per frame in GSM). Synchronization is critical.</td>
            <td>2G GSM, D-AMPS.</td>
        </tr>
        <tr>
            <td><strong>CDMA</strong><br>(Code Division)</td>
            <td>Users share both the entire frequency band and all time slots simultaneously.</td>
            <td>Each user's signal is multiplied by a unique, orthogonal Pseudo-Noise (PN) chip code (Walsh code). Cross-correlation is zero ($\sum c_i c_j = 0$), so the receiver reconstructs only its own signal while all other users appear as low-level background noise.</td>
            <td>3G UMTS, CDMA2000, GPS.</td>
        </tr>
        <tr>
            <td><strong>SDMA</strong><br>(Space Division)</td>
            <td>Separation by physical spatial direction using phased-array smart antennas.</td>
            <td>Directional beamforming focuses narrow radio beams toward specific users in different spatial angles, allowing frequency reuse within the same cell!</td>
            <td>4G LTE-Advanced, 5G Massive MIMO.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Imagine a cocktail party in a large hall where many people want to talk:</p>
<ul>
    <li><strong>FDMA:</strong> Putting people into separate soundproof rooms (different frequencies).</li>
    <li><strong>TDMA:</strong> Everyone stands in the same room, but people take turns speaking for 5 seconds each (time slots).</li>
    <li><strong>CDMA:</strong> Everyone speaks at the same time in the same room, but each pair speaks a completely different foreign language (English, Malayalam, French). You easily tune in to your language while the rest sounds like soft murmur!</li>
    <li><strong>SDMA:</strong> Using parabolic mega-phones directed only at specific people across the room.</li>
</ul>
"""
    },

    'mobile-q14': {
        "title": "Comprehensive Architecture of the Global System for Mobile Communication (GSM)",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "BSS (Radio access: BTS, BSC via Um, A-bis) + NSS (Switching & databases: MSC, HLR, VLR, AuC, EIR via A) + OSS."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Overview:</strong><br>
The GSM (2G) cellular network architecture is structured into three primary functional subsystems:</p>

<p><strong>2. Base Station Subsystem (BSS) — Radio Access Network:</strong></p>
<ul>
    <li><strong>Mobile Station (MS):</strong> Comprises Mobile Equipment (the phone hardware) and the Subscriber Identity Module (SIM card).</li>
    <li><strong>Base Transceiver Station (BTS):</strong> Housing radio transmitters, receivers, and antennas that form a radio cell. Handles radio signal modulation, demodulation, and signal measurements.</li>
    <li><strong>Base Station Controller (BSC):</strong> Controls a cluster of multiple BTSs. Manages radio channel allocation, transmitter power control, and intra-BSS handovers between adjacent cells.</li>
    <li><em>Standard Interfaces:</em> $U_m$ (air radio interface between MS and BTS), A-bis (between BTS and BSC), and A-interface (between BSC and MSC).</li>
</ul>

<p><strong>3. Network and Switching Subsystem (NSS) — Core Network:</strong></p>
<ul>
    <li><strong>Mobile Switching Center (MSC):</strong> The central telephone exchange responsible for call routing, setup, switching, and inter-system handovers.</li>
    <li><strong>Home Location Register (HLR):</strong> Master permanent database storing subscriber profiles, IMSI, subscribed telephone services, and the current location pointer (VLR address).</li>
    <li><strong>Visitor Location Register (VLR):</strong> Temporary local database co-located with an MSC. Stores profile data of all mobile stations currently roaming inside that MSC area.</li>
    <li><strong>Authentication Center (AuC):</strong> Secure database storing subscriber secret key $K_i$ to generate authentication triplets ($RAND, SRES, K_c$).</li>
    <li><strong>Equipment Identity Register (EIR):</strong> Database maintaining White (valid), Grey (faulty/monitored), and Black (stolen/barred) lists of IMEI hardware numbers.</li>
</ul>

<p><strong>4. Operation and Support Subsystem (OSS):</strong></p>
<ul>
    <li>Centralized administrative platform used by telecom engineers for network traffic monitoring, alarm logging, cell reconfiguration, and billing data management.</li>
</ul>
""",
        "understand_simply": r"""
<p>A mobile network works just like a nationwide parcel courier company:</p>
<ul>
    <li><strong>BTS (Radio Towers):</strong> Neighborhood delivery vans that directly hand parcels to customers over the air.</li>
    <li><strong>BSC:</strong> Local branch dispatch manager directing which van drives down which road.</li>
    <li><strong>MSC:</strong> Central regional sorting warehouse connecting trucks between different cities.</li>
    <li><strong>HLR:</strong> Head office master ledger storing every registered customer's permanent home address.</li>
    <li><strong>VLR:</strong> Hotel guestbook recording which visitors from other cities are temporarily staying in this district today.</li>
</ul>
"""
    },

    'mobile-q15': {
        "title": "GSM Call Routing (MTC and MOC) and Handover vs Roaming",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "MTC Routing: Caller $\\to$ GMSC $\\to$ HLR $\\to$ VLR (gets MSRN) $\\to$ Target MSC $\\to$ BSC $\\to$ Paging. Handover = live active call switch; Roaming = registration in foreign network."
        },
        "exam_answer": r"""
<p><strong>1. Mobile Terminated Call (MTC) Step-by-Step Routing Flow:</strong><br>
When an external telephone calls a mobile subscriber's public MSISDN:</p>
<ol>
    <li>The call is routed through the PSTN to the <strong>Gateway MSC (GMSC)</strong> of the subscriber's network.</li>
    <li>The GMSC queries the subscriber's permanent <strong>Home Location Register (HLR)</strong> using the dialed MSISDN.</li>
    <li>The HLR determines which local <strong>Visitor Location Register (VLR)</strong> is currently servicing the mobile and requests a <strong>Mobile Station Roaming Number (MSRN)</strong>.</li>
    <li>The serving VLR assigns a temporary routing number (MSRN) and returns it through the HLR back to the GMSC.</li>
    <li>The GMSC routes the call trunk line directly to the serving MSC using the MSRN.</li>
    <li>The serving MSC queries the local VLR to locate the exact Location Area (LA).</li>
    <li>The MSC commands the Base Station Controllers (BSCs) in that Location Area to broadcast a <strong>Paging Request</strong> over the Paging Channel (PCH).</li>
    <li>The destination Mobile Station hears its identity, sends a Paging Response, authenticates, and connects to an assigned Traffic Channel (TCH). The phone rings!</li>
</ol>

<p><strong>2. Handover vs. Roaming Comparison:</strong></p>
<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Handover (Handoff)</th>
            <th>Roaming</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Operational State</strong></td>
            <td>Occurs during an <strong>active ongoing call or data session</strong>.</td>
            <td>Occurs while the mobile is <strong>idle or registering</strong> in a different service area.</td>
        </tr>
        <tr>
            <td><strong>Trigger</strong></td>
            <td>Deteriorating radio signal strength (low RSSI/high BER) or cell capacity balance.</td>
            <td>Physical movement outside home network coverage into a visited network.</td>
        </tr>
        <tr>
            <td><strong>Execution Time</strong></td>
            <td>Executes in milliseconds ($< 50\text{ ms}$) without dropping the live call.</td>
            <td>Takes several seconds to exchange registration and location updates between VLR and HLR.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>When someone calls your phone, how does the network find you if you travelled to Bangalore? The network looks up your home address (HLR), calls the local hotel in Bangalore where you checked in (VLR), gets a temporary room extension number (MSRN), connects the call to that room, and rings your phone!</p>
"""
    },

    'mobile-q16': {
        "title": "Interactive Voice Response (IVR) Architecture and Call Flow",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "IVR integrates telephony trunking (E1/T1/SIP), VoiceXML dialog manager, DTMF/ASR decoder, TTS, and database backend."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Components of an IVR System:</strong></p>
<ul>
    <li><strong>Telephony Interface Card / VoIP Gateway:</strong> Interfaces with telecom carrier lines (E1/ISDN-PRI or SIP/VoIP). Manages line ringing, call answer, and disconnect signaling.</li>
    <li><strong>DTMF Tone Detector:</strong> Decodes dual-tone multi-frequency keypresses pressed by the caller (e.g., "Press 1 for English").</li>
    <li><strong>Automatic Speech Recognition (ASR) Engine:</strong> Converts caller spoken words into digitized text.</li>
    <li><strong>Text-to-Speech (TTS) &amp; Audio Player:</strong> Plays pre-recorded audio prompts or dynamically converts database text to synthetic speech.</li>
    <li><strong>IVR Dialog Manager (VoiceXML Engine):</strong> Executes the menu call-flow logic and navigates user menus.</li>
    <li><strong>Enterprise Database Backend:</strong> Database storing business records (e.g., ticket availability, seat numbers, bank balances).</li>
</ul>

<p><strong>2. Call Flow for a Movie Theatre Ticket Booking System:</strong></p>
<ol>
    <li><strong>Call Arrival:</strong> Customer dials theatre hotline. IVR answers and plays welcome prompt: <em>"Welcome to Cineplex. Press 1 for Malayalam, 2 for English."</em></li>
    <li><strong>Language Selection:</strong> User presses '1' (DTMF decoded). Dialog manager switches language profile.</li>
    <li><strong>Movie Selection:</strong> IVR prompts: <em>"Press 1 for Movie A, Press 2 for Movie B."</em> Caller selects '1'.</li>
    <li><strong>Showtime Selection:</strong> System queries database for show schedules: <em>"Press 1 for Matinee 2:00 PM, Press 2 for Evening 6:30 PM."</em> Caller selects '2'.</li>
    <li><strong>Seat Availability Check:</strong> Dialog manager queries backend RDBMS via SQL: <code>SELECT available_seats FROM shows WHERE show_id=102</code>. Prompts: <em>"Enter number of tickets."</em> Caller enters '3'.</li>
    <li><strong>Booking Confirmation &amp; SMS Dispatch:</strong> Database reserves 3 seats. IVR generates an SMS booking confirmation sent via SMSC gateway to caller's mobile number: <em>"Your booking is confirmed! Booking ID: 4892."</em></li>
    <li><strong>Call Termination:</strong> <em>"Thank you for calling Cineplex!"</em> IVR releases the line.</li>
</ol>
""",
        "understand_simply": r"""
<p>An IVR is an automated robot telephone operator. When you call customer service, it listens to your button presses (DTMF) or spoken words, checks the company database, reads back your account balance, and sends you a confirmation text—all without needing a human call center agent!</p>
"""
    },

    'mobile-q17': {
        "title": "GSM Security Architecture: Authentication (A3), Key Generation (A8), and Encryption (A5)",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$SRES = A3(RAND, K_i), \quad K_c = A8(RAND, K_i), \quad \text{Ciphertext} = A5(K_c, \text{Frame No.}, \text{Data})$$",
            "text": "Shared secret key $K_i$ never leaves SIM or AuC; challenge-response verification prevents eavesdropping."
        },
        "exam_answer": r"""
<p><strong>1. GSM Security Objectives:</strong> Protect subscriber identity confidentiality, authenticate legitimate users to prevent SIM cloning, and encrypt over-the-air voice and data against radio interception.</p>

<p><strong>2. Core Security Parameters:</strong></p>
<ul>
    <li>$K_i$: 128-bit master secret key stored exclusively in the SIM card and AuC database. It is <em>never</em> transmitted over the radio link.</li>
    <li>$RAND$: 128-bit pseudo-random challenge generated by the Authentication Center (AuC).</li>
</ul>

<p><strong>3. Step-by-Step Security and Authentication Process:</strong></p>

<p><strong>Step 1: Triplet Generation at the Authentication Center (AuC)</strong><br>
When a subscriber registers, AuC generates a random 128-bit number $RAND$ and runs two algorithms using the subscriber's secret $K_i$:
$$SRES = A3(RAND, K_i) \quad \text{[Signed Response, 32 bits]}$$
$$K_c = A8(RAND, K_i) \quad \text{[Cipher Key, 64 bits]}$$
The triplet $(RAND, SRES, K_c)$ is delivered securely to the local serving VLR.</p>

<p><strong>Step 2: Challenge-Response Authentication (Algorithm A3)</strong></p>
<ol>
    <li>The VLR transmits only the 128-bit challenge $RAND$ over the radio air interface to the Mobile Station.</li>
    <li>The mobile handset passes $RAND$ into the tamper-resistant SIM card.</li>
    <li>The SIM executes algorithm A3 internally using $RAND$ and its secret $K_i$ to produce an answer $SRES' = A3(RAND, K_i)$.</li>
    <li>The mobile transmits the 32-bit $SRES'$ back to the VLR.</li>
    <li>The VLR compares $SRES'$ with the expected $SRES$. If $SRES' == SRES$, access is granted. If not, the connection is immediately severed.</li>
</ol>

<p><strong>Step 3: Cipher Key Generation (Algorithm A8)</strong><br>
Concurrently within the SIM, algorithm A8 uses the same $RAND$ and $K_i$ to compute the 64-bit session key:
$$K_c = A8(RAND, K_i)$$
$K_c$ is passed from the SIM to the mobile equipment (ME) ciphering hardware.</p>

<p><strong>Step 4: Over-the-Air Stream Encryption (Algorithm A5)</strong><br>
Algorithm A5 (e.g., A5/1 or A5/3) is an encryption stream cipher running on the mobile hardware and BTS. It uses session key $K_c$ and the 22-bit TDMA frame sequence number to generate a pseudo-random bitstream that is XORed with speech and data frames. Decryption occurs at the BTS before traversing the secure wired core network.</p>
""",
        "understand_simply": r"""
<p>How do you prove who you are without shouting your secret password over a public radio channel where anyone could eavesdrop?</p>
<p>GSM uses a clever "challenge-response" test. The network sends your phone a random math riddle ($RAND$). Your SIM card uses your secret password ($K_i$) to solve it ($SRES$) and sends back only the final answer. The network already calculated the expected answer in advance. If your answers match, you are verified—and your secret password never had to touch the airwaves!</p>
"""
    },

    # =========================================================================
    # MODULE 3: Short Messaging Service (SMS) & GPRS
    # =========================================================================
    'mobile-q18': {
        "title": "Strengths and Architectural Distinctiveness of Short Message Service (SMS)",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "160 alphanumeric characters (7-bit GSM default alphabet); uses out-of-band signaling channels (SDCCH/SACCH) with Store-and-Forward delivery via SMSC."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Distinctiveness:</strong></p>
<ul>
    <li><strong>Store-and-Forward Model:</strong> SMS messages are not delivered directly between phones. They are sent to a central <strong>Short Message Service Center (SMSC)</strong>, which stores the message and retries delivery if the recipient is powered off or out of coverage.</li>
    <li><strong>Uses Out-of-Band Signaling Channels:</strong> SMS transmits over signaling control channels (SDCCH during call setup, or SACCH during an active call) rather than voice traffic channels. A subscriber can receive an SMS <em>while simultaneously speaking on a phone call</em> without interruption!</li>
    <li><strong>Payload Limit:</strong> Maximum 140 bytes, which equals <strong>160 characters</strong> in 7-bit GSM default alphabet (or 70 characters in 16-bit Unicode).</li>
</ul>

<p><strong>2. Core Strengths:</strong></p>
<ul>
    <li><strong>High Reliability:</strong> Guaranteed delivery confirmation receipt. Messages are never lost when mobile is off.</li>
    <li><strong>Universal Reach:</strong> Operates on $100\%$ of mobile handsets without requiring mobile data plans, internet access, or smartphone apps.</li>
    <li><strong>Critical for 2FA:</strong> Foundation for bank One-Time Passwords (OTP) and emergency disaster alerts.</li>
</ul>
""",
        "understand_simply": r"""
<p>Voice calls are like talking on a walkie-talkie—both people must be listening live. SMS is like leaving a sealed envelope in a post office box (SMSC). If your friend's phone is off, the post office holds the envelope and delivers it the moment your friend turns their phone back on!</p>
"""
    },

    'mobile-q19': {
        "title": "Limitations and Bottlenecks of General Packet Radio Service (GPRS)",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Bottlenecks: Theoretical max 171.2 kbps (practical 40-50 kbps), CS-1 to CS-4 coding schemes, high latency (300-800 ms), voice preempts data."
        },
        "exam_answer": r"""
<p>GPRS (2.5G) introduced packet-switched mobile internet over existing GSM networks, but suffered from five major technical bottlenecks:</p>
<ol>
    <li><strong>Low Data Rates:</strong> Although theoretical maximum throughput is $171.2\text{ kbps}$ (aggregating all 8 time slots under CS-4 coding), real-world practical speeds were only $40\text{ to } 50\text{ kbps}$ due to error protection overhead.</li>
    <li><strong>Subordinate Priority to Voice:</strong> GSM gives absolute priority to voice calls over GPRS data. During peak traffic hours, GPRS time slots are dynamically reallocated to voice, throttling data speeds to near zero.</li>
    <li><strong>High Latency &amp; Round-Trip Times:</strong> Latency between mobile and gateway ranges from $300\text{ to } 800\text{ ms}$, causing sluggish interactive web browsing and making real-time gaming or VoIP impossible.</li>
    <li><strong>Gaussian Minimum Shift Keying (GMSK) Modulation Limits:</strong> Spectral efficiency is low ($1\text{ bit/symbol}$); later upgraded by EDGE using 8-PSK ($3\text{ bits/symbol}$).</li>
    <li><strong>Class-B Terminal Limitations:</strong> Most mobile handsets were Class-B, meaning they could not transmit packet data and receive a voice call simultaneously. Data paused whenever a phone call arrived!</li>
</ol>
""",
        "understand_simply": r"""
<p>GPRS was the grandfather of mobile internet. It was like driving a tiny scooter down the shoulder of a highway: whenever a big bus (voice call) came by, you had to pull over and wait for the bus to pass before you could squeeze forward again!</p>
"""
    },

    'mobile-q20': {
        "title": "Billing and Charging Mechanisms in GPRS: Volume, Duration, QoS, and CDRs",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Charging Gateway Function (CGF) aggregates Call Detail Records (S-CDRs from SGSN, G-CDRs from GGSN) based on volume (MB), duration, and QoS."
        },
        "exam_answer": r"""
<p><strong>1. Packet-Switched Charging Principles:</strong><br>
Unlike circuit-switched GSM (which bills purely by call connection time), GPRS bills subscribers primarily based on <strong>actual data volume transferred (in Megabytes/Gigabytes)</strong>, because packet radio uses channel resources only when packets are transmitted ("Always-On" connectivity).</p>

<p><strong>2. Core Billing Parameters:</strong></p>
<ul>
    <li><strong>Volume-Based Charging:</strong> Number of octets (bytes) successfully transferred in uplink and downlink directions.</li>
    <li><strong>Time/Duration-Based Charging:</strong> Duration of active Packet Data Protocol (PDP) context connection.</li>
    <li><strong>Quality of Service (QoS) Level:</strong> Higher tariff applied for premium low-latency guaranteed bit-rate traffic.</li>
    <li><strong>Destination &amp; APN Based:</strong> Different billing rates for public Internet APN vs corporate intranet APNs.</li>
</ul>

<p><strong>3. Charging Architecture:</strong></p>
<ul>
    <li>The <strong>SGSN</strong> monitors radio data transfers and produces <em>S-CDRs (SGSN Charging Data Records)</em>.</li>
    <li>The <strong>GGSN</strong> monitors external IP traffic and produces <em>G-CDRs</em>.</li>
    <li>The <strong>Charging Gateway Function (CGF)</strong> collects, filters, and consolidates S-CDRs and G-CDRs before forwarding them to the telecom operator's central billing system.</li>
</ul>
""",
        "understand_simply": r"""
<p>Old landline calls were billed like a metered taxi ride—you paid for every minute you sat in the taxi even if you were stuck in traffic. GPRS billing is like buying water at a supermarket: you pay for the number of liters of water you actually drink (Megabytes downloaded), not how long the bottle sits on your table!</p>
"""
    },

    'mobile-q21': {
        "title": "Comprehensive Architecture and Delivery Mechanisms of SMS (SM-MT and SM-MO)",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "SM-MO: MS $\\to$ BTS $\\to$ BSC $\\to$ MSC $\\to$ SMS-IWMSC $\\to$ SMSC. SM-MT: SMSC $\\to$ SMS-GMSC $\\to$ HLR $\\to$ MSC/VLR $\\to$ BSC $\\to$ BTS $\\to$ MS."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Entities in SMS:</strong></p>
<ul>
    <li><strong>Short Message Service Center (SMSC):</strong> The central store-and-forward server that queues, routes, and guarantees message delivery.</li>
    <li><strong>SMS-Gateway MSC (SMS-GMSC):</strong> Gateway receiving messages from SMSC, interrogating HLR for recipient location, and forwarding to destination MSC.</li>
    <li><strong>SMS-Interworking MSC (SMS-IWMSC):</strong> Gateway receiving submitted messages from mobile MSC and forwarding them into the SMSC.</li>
    <li><strong>HLR / VLR:</strong> Provides routing address of the recipient's serving MSC.</li>
</ul>

<p><strong>2. Mobile Originated Short Message (SM-MO) Delivery Flow:</strong></p>
<ol>
    <li>Subscriber types text and presses send. Mobile Station transmits message over SDCCH/SACCH signaling channel to Base Station (BTS/BSC).</li>
    <li>BSC delivers message to the originating Mobile Switching Center (MSC/VLR).</li>
    <li>MSC verifies subscriber authorization with VLR and forwards message to <strong>SMS-IWMSC</strong>.</li>
    <li>SMS-IWMSC transfers the message to the central <strong>SMSC</strong>.</li>
    <li>SMSC stores message in its database and returns a delivery confirmation receipt to the sender.</li>
</ol>

<p><strong>3. Mobile Terminated Short Message (SM-MT) Delivery Flow:</strong></p>
<ol>
    <li>SMSC queues message for delivery and passes it to <strong>SMS-GMSC</strong>.</li>
    <li>SMS-GMSC queries recipient's <strong>HLR</strong> using destination MSISDN (Send Routing Info for SM).</li>
    <li>HLR checks recipient status and returns current serving MSC address. (If recipient is unavailable, HLR flags <em>Message Waiting</em>).</li>
    <li>SMS-GMSC forwards message to serving MSC/VLR.</li>
    <li>MSC pages recipient mobile station via BSC.</li>
    <li>Mobile answers page, establishes SDCCH connection, receives the SMS message, and sends an ACK acknowledgment back to SMSC.</li>
</ol>
""",
        "understand_simply": r"""
<p>Sending an SMS is like sending a registered letter through speed post: you drop your letter into the local post office (SM-MO to SMSC). The post office stamps it, stores it, looks up the recipient's current residential address in a master telephone directory (HLR), and dispatches a delivery van (SM-MT) straight to their door with an acknowledgment receipt!</p>
"""
    },

    'mobile-q22': {
        "title": "Comprehensive Architecture, Protocol Stack, and Network Operations of GPRS",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Key nodes: SGSN (mobility, ciphering, session management) and GGSN (gateway to external IP networks). GTP tunnels packets between SGSN & GGSN."
        },
        "exam_answer": r"""
<p><strong>1. GPRS Architectural Elements:</strong><br>
GPRS overlays two new core packet-switching nodes onto the existing circuit-switched GSM infrastructure:</p>
<ol>
    <li><strong>Serving GPRS Support Node (SGSN):</strong>
        <ul>
            <li>Equivalent to an MSC for packet data.</li>
            <li>Handles packet routing, ciphering, session management, and mobility management (cell updates, routing area updates).</li>
            <li>Connects to BSS via the <strong>Gb interface</strong> (using Frame Relay or IP).</li>
        </ul>
    </li>
    <li><strong>Gateway GPRS Support Node (GGSN):</strong>
        <ul>
            <li>The gateway router connecting GPRS core to external Packet Data Networks (PDNs like the public Internet or corporate intranets).</li>
            <li>Allocates dynamic IP addresses to mobile devices and performs firewall filtering and billing.</li>
            <li>Connects to SGSN via the <strong>Gn interface</strong> using GPRS Tunneling Protocol (GTP).</li>
        </ul>
    </li>
    <li><strong>Packet Control Unit (PCU):</strong> Hardware board added to BSC that separates packet data from voice circuits.</li>
</ol>

<p><strong>2. Core Network Procedures:</strong></p>
<ul>
    <li><strong>GPRS Attach:</strong> Mobile registers its presence with the SGSN; identity verified and ciphering established.</li>
    <li><strong>PDP Context Activation:</strong> Mobile requests data access by specifying an Access Point Name (APN). GGSN assigns an IP address and establishes a virtual IP tunnel (GTP tunnel) between GGSN and SGSN, allowing mobile to browse the Internet.</li>
</ul>

<p><strong>3. GPRS Protocol Stack:</strong></p>
<ul>
    <li><strong>Application Layer:</strong> HTTP, FTP, TCP/UDP, IP.</li>
    <li><strong>SNDCP (Sub-Network Dependent Convergence Protocol):</strong> Compresses IP headers and multiplexes packet streams.</li>
    <li><strong>LLC (Logical Link Control):</strong> Provides ciphered, reliable logical link across the radio path.</li>
    <li><strong>RLC/MAC (Radio Link Control / Medium Access Control):</strong> Segments packets into radio blocks and handles radio contention.</li>
</ul>
""",
        "understand_simply": r"""
<p>GSM was built purely for voice telephone calls. GPRS added two new internet routers to the network: the <strong>SGSN</strong> acts like a local router following you around as you move from cell to cell, while the <strong>GGSN</strong> acts like the master internet modem connecting the entire telecom network out to Google and the worldwide web.</p>
"""
    },

    'mobile-q23': {
        "title": "Quality of Service (QoS) Parameters in GPRS and Packet Data Networks",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": None,
            "text": "5 QoS Attributes: Precedence Class (Priority), Delay Class (Latency), Reliability Class (Packet Loss), Peak Throughput, and Mean Throughput."
        },
        "exam_answer": r"""
<p>GPRS defines a structured Quality of Service (QoS) profile negotiated during PDP Context activation, characterized by five technical parameters:</p>
<ol>
    <li><strong>Service Precedence (Priority Class):</strong>
        <ul>
            <li>Specifies packet delivery priority during network congestion.</li>
            <li><em>Class 1: High Priority</em> (network control signaling and emergency services).</li>
            <li><em>Class 2: Normal Priority</em> (interactive banking transactions).</li>
            <li><em>Class 3: Low Priority</em> (background downloads, batch emails).</li>
        </ul>
    </li>
    <li><strong>Delay Class (Transmission Latency):</strong>
        <ul>
            <li>Defines maximum end-to-end packet transfer delay across the network:
                <ul>
                    <li>Delay Class 1: $< 0.5\text{ s}$ (real-time interactive applications).</li>
                    <li>Delay Class 2: $< 5\text{ s}$ (web browsing).</li>
                    <li>Delay Class 3: $< 50\text{ s}$ (interactive transactions).</li>
                    <li>Delay Class 4: Best effort (unspecified delay for background batch sync).</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><strong>Reliability Class:</strong>
        <ul>
            <li>Defines residual packet error rates and duplicate protection using RLC and LLC retransmission protocols. Class 1 guarantees error-free non-real-time data; Class 5 provides best-effort transport without retransmissions (ideal for streaming audio).</li>
        </ul>
    </li>
    <li><strong>Peak Throughput Class:</strong>
        <ul>
            <li>Guaranteed maximum burst data rate available across radio interface (from $8\text{ kbps}$ up to $256\text{ kbps}$).</li>
        </ul>
    </li>
    <li><strong>Mean Throughput Class:</strong>
        <ul>
            <li>Expected average throughput across an active session (ranging from $0.22\text{ bps}$ up to $111\text{ kbps}$).</li>
        </ul>
    </li>
</ol>
""",
        "understand_simply": r"""
<p>QoS is like airline ticket classes: First Class (high precedence) boards first, gets priority seats, and never gets bumped. Economy Class (best-effort) gets you to the same destination, but if the flight is overbooked, your luggage waits for the next flight!</p>
"""
    },

    # =========================================================================
    # MODULE 4: Wireless LAN (WLAN) & IEEE 802.11 Standards
    # =========================================================================
    'mobile-q24': {
        "title": "WLAN Architecture: Infrastructure Mode vs Independent Ad-Hoc Mode (IBSS)",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Infrastructure Mode: Central Access Point (AP) coordinates all traffic and connects to DS; Ad-Hoc (IBSS): Peer-to-peer without any AP."
        },
        "exam_answer": r"""
<p>IEEE 802.11 defines two fundamental operating topologies for Wireless Local Area Networks:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Infrastructure Mode (BSS / ESS)</th>
            <th>Ad-Hoc Mode (Independent BSS / IBSS)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Central Coordinator</strong></td>
            <td>Requires a central hardware <strong>Access Point (AP)</strong>. All client transmissions must route through the AP.</td>
            <td><strong>No Access Point required.</strong> Mobile stations communicate directly peer-to-peer (P2P).</td>
        </tr>
        <tr>
            <td><strong>Connection to Wired Internet</strong></td>
            <td>AP connects to a wired backbone network via a <strong>Distribution System (DS)</strong> (Ethernet switch/router).</td>
            <td>Isolated island network; no natural connection to wired external networks or internet.</td>
        </tr>
        <tr>
            <td><strong>Scalability &amp; Roaming</strong></td>
            <td>Highly scalable. Multiple APs can be linked together into an <strong>Extended Service Set (ESS)</strong> allowing seamless roaming.</td>
            <td>Limited to small group of nearby nodes within direct mutual radio transmission range.</td>
        </tr>
        <tr>
            <td><strong>Typical Use Cases</strong></td>
            <td>Home Wi-Fi routers, university campus networks, corporate offices, airports.</td>
            <td>Quick file sharing (Apple AirDrop, Wi-Fi Direct), multiplayer mobile gaming without router, emergency search and rescue.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p><strong>Infrastructure Mode</strong> is like a classroom with a teacher at the front: every student raises their hand and speaks only through the teacher. <strong>Ad-Hoc Mode</strong> is like students whispering directly to each other in the corridor during break time without any teacher present.</p>
"""
    },

    'mobile-q25': {
        "title": "Interframe Spaces (IFS) in IEEE 802.11 MAC: SIFS, PIFS, DIFS, and EIFS",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\text{Priority: } \text{SIFS} < \text{PIFS} < \text{DIFS} < \text{EIFS}$$",
            "text": "Shorter waiting times grant higher medium access priority: SIFS (ACKs) > PIFS (AP Polling) > DIFS (Asynchronous Data) > EIFS (Error Recovery)."
        },
        "exam_answer": r"""
<p>IEEE 802.11 MAC prioritizes channel access without collisions by requiring transmitting stations to sense the channel idle for distinct time intervals called Interframe Spaces (IFS):</p>
<ol>
    <li><strong>SIFS (Short Interframe Space):</strong> Shortest waiting period ($10\text{ to } 16\,\mu\text{s}$). Grants highest transmission priority. Used for immediate critical responses: ACK frames, Clear to Send (CTS), and fragment bursts.</li>
    <li><strong>PIFS (PCF Interframe Space):</strong> Intermediate duration ($\text{PIFS} = \text{SIFS} + \text{SlotTime}$). Used exclusively by the Access Point in Point Coordination Function (PCF) to poll stations for real-time contention-free traffic.</li>
    <li><strong>DIFS (DCF Interframe Space):</strong> Standard duration ($\text{DIFS} = \text{SIFS} + 2 \times \text{SlotTime}$). Used by all normal stations under Distributed Coordination Function (DCF) before attempting to transmit regular data frames.</li>
    <li><strong>EIFS (Extended Interframe Space):</strong> Longest duration. Triggered when a frame is received with an error (bad checksum). Forces the station to wait extra time to avoid corrupting a valid frame being acknowledged by another node.</li>
</ol>
""",
        "understand_simply": r"""
<p>Think of a debate in a formal conference room where people wait for silence before speaking:</p>
<ul>
    <li><strong>SIFS:</strong> The chairperson giving a one-word reply ("Approved!") gets top priority—only waits 1 second.</li>
    <li><strong>PIFS:</strong> The moderator asking a specific speaker to talk gets priority 2—waits 2 seconds.</li>
    <li><strong>DIFS:</strong> Normal audience members raising their hands to ask general questions—must wait 3 seconds.</li>
    <li><strong>EIFS:</strong> If someone drops a microphone with loud screeching feedback, everyone freezes and waits 5 seconds for the room to settle down.</li>
</ul>
"""
    },

    'mobile-q26': {
        "title": "Comparative Technical Analysis: Wi-Fi (IEEE 802.11) vs 3G/Cellular Networks",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Wi-Fi: Unlicensed spectrum (2.4/5 GHz), low cost, high local speed, short range (100m); Cellular: Licensed spectrum, high cost, global coverage & seamless mobility."
        },
        "exam_answer": r"""
<p>Wi-Fi and Cellular networks represent complementary wireless communication paradigms:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Technical Parameter</th>
            <th>Wi-Fi (IEEE 802.11 WLAN)</th>
            <th>3G / 4G Cellular Networks</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Radio Frequency Spectrum</strong></td>
            <td><strong>Unlicensed ISM bands</strong> ($2.4\text{ GHz}, 5\text{ GHz}, 6\text{ GHz}$). Free to use, but prone to radio interference from microwaves and neighboring routers.</td>
            <td><strong>Licensed spectrum bands</strong> ($700\text{ MHz} \to 2.6\text{ GHz}$). Exclusive spectrum purchased at high auction cost; zero external interference.</td>
        </tr>
        <tr>
            <td><strong>Coverage Range &amp; Cell Size</strong></td>
            <td>Short-range / Micro-cells: $30\text{ to } 100\text{ meters}$ radius per Access Point.</td>
            <td>Wide-area coverage / Macro-cells: $1\text{ to } 10\text{ km}$ radius per cellular base station tower.</td>
        </tr>
        <tr>
            <td><strong>Mobility Support</strong></td>
            <td>Limited mobility; designed for stationary or pedestrian walking speeds. Session disconnects at high speed.</td>
            <td>High-speed seamless mobility; engineered for high-speed cars, trains, and planes moving up to $350\text{ km/h}$.</td>
        </tr>
        <tr>
            <td><strong>Medium Access Protocol</strong></td>
            <td>Contention-based CSMA/CA (random backoff; throughput collapses if hundreds of users compete).</td>
            <td>Centrally coordinated scheduled access (CDMA/OFDMA); guaranteed quality of service and bandwidth reservation.</td>
        </tr>
        <tr>
            <td><strong>Deployment &amp; User Cost</strong></td>
            <td>Inexpensive consumer router hardware; free connection for end users in home/offices.</td>
            <td>Billion-dollar carrier infrastructure cost; metered billing per GB data plan for end users.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Wi-Fi is like the private elevator inside your own house: it is fast, free to use, and convenient, but it only takes you within your own building. Cellular is like the public highway system: you have to pay road tolls, but it connects you across the entire country even when you are driving at 100 km/h!</p>
"""
    },

    'mobile-q27': {
        "title": "Hidden and Exposed Terminal Problems and Virtual Carrier Sensing via RTS/CTS",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\text{RTS/CTS Handshake: } \text{Station A} \xrightarrow{\text{RTS}} \text{AP} \xrightarrow{\text{CTS}} \text{Station A} \to \text{Data} \to \text{ACK}$$",
            "text": "RTS/CTS uses Virtual Carrier Sensing via Network Allocation Vector (NAV) to silence hidden competitors."
        },
        "exam_answer": r"""
<p><strong>1. Hidden Terminal Problem:</strong></p>
<ul>
    <li><strong>Scenario:</strong> Station A and Station C are both within radio range of central Access Point B, but A and C are out of radio range of each other (hidden by distance or physical walls).</li>
    <li><strong>Problem:</strong> When Station A transmits a packet to B, Station C senses the medium, hears silence, and begins transmitting its own packet to B. Both signals arrive simultaneously at B, causing a catastrophic <strong>packet collision</strong>!</li>
</ul>

<p><strong>2. Exposed Terminal Problem:</strong></p>
<ul>
    <li><strong>Scenario:</strong> Station B is transmitting data to Station A. Nearby Station C wants to transmit to an independent Station D (away from A and B).</li>
    <li><strong>Problem:</strong> Station C senses the medium, hears Station B's transmission, and wrongly assumes the channel is busy. Station C needlessly defers its transmission, causing <strong>wasted channel throughput</strong> even though transmission from C to D would not interfere with reception at A.</li>
</ul>

<p><strong>3. Solution: RTS/CTS Handshake Mechanism:</strong><br>
IEEE 802.11 solves the hidden terminal problem through a 4-way handshake using Virtual Carrier Sensing:</p>
<ol>
    <li>Before sending a large data packet, Station A sends a short <strong>RTS (Request to Send)</strong> control frame to AP B. The RTS contains the required transmission duration.</li>
    <li>If AP B is free, it broadcasts a <strong>CTS (Clear to Send)</strong> control frame back to Station A.</li>
    <li>Because CTS is broadcast from central AP B, hidden Station C hears the CTS! Station C reads the duration field and sets its internal timer called the <strong>Network Allocation Vector (NAV)</strong>, silencing itself until A completes its transmission.</li>
    <li>Station A safely transmits its data frame without collisions and receives an ACK from B.</li>
</ol>
""",
        "understand_simply": r"""
<p><strong>Hidden Terminal:</strong> Imagine two students sitting in opposite corners of a large library. Both can whisper to the teacher in the middle, but cannot hear each other. If both start whispering to the teacher at the exact same moment, the teacher hears only garbled gibberish!</p>
<p><strong>The Fix (RTS/CTS):</strong> The first student raises her hand and asks, "May I speak for 30 seconds?" (RTS). The teacher announces loudly to the whole room, "Yes, you have the floor for 30 seconds!" (CTS). The second student in the far corner hears the teacher, lowers his hand, and waits quietly.</p>
"""
    },

    'mobile-q28': {
        "title": "Comprehensive Architecture and Analysis of Wireless Local Loop (WLL)",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "WLL replaces traditional copper 'last-mile' telephone cables with fixed wireless radio links connecting subscribers to the local telephone exchange."
        },
        "exam_answer": r"""
<p><strong>1. Concept of Wireless Local Loop (WLL):</strong><br>
Wireless Local Loop (also called Fixed Wireless Access) replaces traditional underground copper telephone cables connecting homes/offices to the central telephone exchange with point-to-multipoint radio links.</p>

<p><strong>2. Core Architectural Blocks:</strong></p>
<ol>
    <li><strong>PSTN / Central Telephone Exchange:</strong> Standard public telephone switching exchange.</li>
    <li><strong>Wireless Access Unit (WAU) / Base Station:</strong> Transceiver tower located at the central office covering a suburban/rural radius of $5\text{ to } 30\text{ km}$.</li>
    <li><strong>Radio Interface Link:</strong> Fixed directional microwave radio links operating over licensed frequencies (using technologies like cdmaOne, DECT, or WiMAX).</li>
    <li><strong>Wireless Fixed Terminal (WFT) / Subscriber Unit:</strong> Directional rooftop Yagi or dish antenna mounted on customer's premises connected to an indoor wall-box telephone unit.</li>
</ol>

<p><strong>3. Major Advantages over Wired Copper Loops:</strong></p>
<ul>
    <li><strong>Rapid Deployment:</strong> An entire town or rural district can be provided telephone and internet connectivity in weeks, without digging roads or laying hundreds of kilometers of copper wire.</li>
    <li><strong>Lower Capital Cost in Rural Areas:</strong> Copper cable cost scales with distance; WLL infrastructure cost depends only on the number of base station towers.</li>
    <li><strong>Immunity to Cable Theft &amp; Weather Damage:</strong> Copper cables are frequently stolen, cut during road construction, or waterlogged during monsoons. Fixed wireless eliminates physical cable maintenance.</li>
</ul>
""",
        "understand_simply": r"""
<p>In the old days, connecting a landline phone required digging trenches along the road to bury copper cables all the way from the telephone exchange to your house. Wireless Local Loop replaces that trench with a wireless radio beam between the telephone exchange tower and a small antenna on your rooftop!</p>
"""
    },

    'mobile-q29': {
        "title": "WLAN Security Evolution: WEP Vulnerabilities, WPA, WPA2 (802.11i), and WPA3",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Evolution: WEP (Weak RC4, 24-bit IV crackable in mins) $\\to$ WPA (TKIP) $\\to$ WPA2 (AES-CCMP) $\\to$ WPA3 (SAE against dictionary attacks)."
        },
        "exam_answer": r"""
<p>The security protocols for IEEE 802.11 Wi-Fi networks evolved over four distinct generations:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Security Standard</th>
            <th>Cipher Algorithm &amp; Key Size</th>
            <th>Integrity Check</th>
            <th>Vulnerabilities &amp; Upgrades</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>WEP</strong><br>(Wired Equivalent Privacy, 1999)</td>
            <td>Stream cipher <strong>RC4</strong> (40-bit or 104-bit key) with 24-bit Initialization Vector (IV).</td>
            <td>CRC-32 (linear and cryptographically unsecure).</td>
            <td><strong>Severely Broken:</strong> 24-bit IV is too short; IVs repeat every few thousand packets. Hackers can crack WEP keys within 5 minutes using tools like Aircrack-ng.</td>
        </tr>
        <tr>
            <td><strong>WPA</strong><br>(Wi-Fi Protected Access, 2003)</td>
            <td><strong>RC4 with TKIP</strong> (Temporal Key Integrity Protocol, 128-bit key).</td>
            <td>Michael Message Integrity Code (MIC).</td>
            <td>Interim upgrade; introduced per-packet key mixing and extended 48-bit IV to eliminate IV reuse. Still vulnerable to TKIP forgery attacks.</td>
        </tr>
        <tr>
            <td><strong>WPA2</strong><br>(IEEE 802.11i, 2004)</td>
            <td><strong>AES-CCMP</strong> (Counter Mode Cipher Block Chaining MAC Protocol, 128-bit key).</td>
            <td>CBC-MAC (strong cryptographic integrity).</td>
            <td>Industry standard for over 15 years; provides military-grade encryption. Vulnerable to offline dictionary brute-force attacks and KRACK key reinstallation attacks.</td>
        </tr>
        <tr>
            <td><strong>WPA3</strong><br>(2018)</td>
            <td><strong>AES-GCMP</strong> (128-bit in WPA3-Personal, 192-bit in WPA3-Enterprise).</td>
            <td>GMAC (Galois Message Authentication Code).</td>
            <td>Replaces Pre-Shared Key with <strong>Simultaneous Authentication of Equals (SAE)</strong>; completely defeats offline dictionary attacks and provides Forward Secrecy.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Wi-Fi security evolution is like upgrading door locks: WEP was a flimsy wooden latch that thieves learned to pick with a paperclip in 2 minutes. WPA was an iron bolt added to the latch. WPA2 was a heavy steel deadbolt (AES). And WPA3 is a modern biometric fingerprint scanner that locks you out completely if you guess wrong!</p>
"""
    },

    'mobile-q30': {
        "title": "HIPERLAN Communication Models and Medium Access Control: HIPERLAN 1 vs HIPERLAN 2",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "HIPERLAN/1: EY-NPMA contention protocol (23.5 Mbps, 5 GHz); HIPERLAN/2: Connection-oriented dynamic TDMA/TDD with OFDM (54 Mbps, ATM-like QoS)."
        },
        "exam_answer": r"""
<p><strong>1. Introduction to HIPERLAN:</strong><br>
HIPERLAN (High Performance Radio Local Area Network) is a European telecommunications standard (ETSI) operating in the $5\text{ GHz}$ unlicensed band, designed as a European alternative to IEEE 802.11.</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>HIPERLAN / 1 (1996)</th>
            <th>HIPERLAN / 2 (2000)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Physical Data Rate</strong></td>
            <td>Up to $23.5\text{ Mbps}$.</td>
            <td>Up to $54\text{ Mbps}$ (uses 52-carrier OFDM modulation, identical to 802.11a).</td>
        </tr>
        <tr>
            <td><strong>Medium Access Protocol</strong></td>
            <td><strong>EY-NPMA</strong> (Elimination Yield - Non-Preemptive Multiple Access). Contention-based priority mechanism.</td>
            <td><strong>Centralized Dynamic TDMA/TDD</strong>. Contention-free scheduled time slots controlled by an Access Point.</td>
        </tr>
        <tr>
            <td><strong>Communication Model</strong></td>
            <td>Connectionless packet transfer; supports ad-hoc peer-to-peer and multi-hop forwarding.</td>
            <td><strong>Connection-oriented:</strong> Requires explicit connection setup; supports ATM cells, Ethernet frames, and IP packets.</td>
        </tr>
        <tr>
            <td><strong>Quality of Service (QoS)</strong></td>
            <td>Prioritized channel access based on packet lifetime and priority class.</td>
            <td>Guaranteed QoS with negotiated bandwidth, strict latency limits, and cellular-style handovers.</td>
        </tr>
    </tbody>
</table>

<p><strong>2. Working of EY-NPMA Protocol (HIPERLAN/1):</strong></p>
<ol>
    <li><strong>Prioritization Phase:</strong> Stations with higher priority transmit an RF burst first. Stations with lower priority hear the channel busy and eliminate themselves immediately.</li>
    <li><strong>Contention Phase (Elimination &amp; Yield):</strong> Competing stations transmit a burst of random length. The station with the longest burst survives. Surviving stations then listen for a random yield period. The first station to complete its yield period transmits its packet.</li>
</ol>
""",
        "understand_simply": r"""
<p>HIPERLAN/1's EY-NPMA protocol is like a musical chairs game with sound: all contestants yell as loud as they can. Whoever yells the longest knocks out the others, and the last person standing gets to speak!</p>
"""
    },

    # =========================================================================
    # MODULE 5: Mobile Security, Cryptography & Next Generation Networks
    # =========================================================================
    'mobile-q31': {
        "title": "Foundational Components of Information Security: The Extended CIA Triad",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "CIA-AAN: Confidentiality (Encryption), Integrity (Hashes), Availability (Redundancy), Authenticity (Certs), Non-Repudiation (Digital Signatures)."
        },
        "exam_answer": r"""
<p>Information security in mobile networks relies on five core pillars (the Extended CIA Triad):</p>
<ol>
    <li><strong>Confidentiality:</strong> Ensures that information is accessible only to authorized entities and kept secret from eavesdroppers. Achieved using symmetric encryption (AES, 3DES) and asymmetric encryption (RSA).</li>
    <li><strong>Integrity:</strong> Guarantees that data is not altered, tampered with, or corrupted during wireless transit. Enforced using cryptographic hash functions (SHA-256, HMAC).</li>
    <li><strong>Availability:</strong> Ensures that network services, servers, and data remain accessible to authorized users whenever needed. Protected by deploying firewalls, redundant servers, and Anti-DDoS mitigation.</li>
    <li><strong>Authenticity:</strong> Verifies the true identity of the communicating parties or devices (preventing spoofing and impersonation). Enforced through digital certificates (X.509) and Challenge-Response authentication.</li>
    <li><strong>Non-Repudiation:</strong> Prevents a sender or receiver from denying having sent or received a transaction. Enforced via asymmetric Digital Signatures.</li>
</ol>
""",
        "understand_simply": r"""
<p>Think of sending money through mobile banking:</p>
<ul>
    <li><strong>Confidentiality:</strong> No one looking over your shoulder can see your bank PIN.</li>
    <li><strong>Integrity:</strong> No hacker can change your transfer amount from ₹100 to ₹10,000 mid-flight.</li>
    <li><strong>Availability:</strong> The banking app opens and works even during peak festival hours.</li>
    <li><strong>Non-Repudiation:</strong> Once you send the money with your digital signature, you cannot claim "I never sent that!"</li>
</ul>
"""
    },

    'mobile-q32': {
        "title": "Classification of Security Attacks in Mobile Computing: Static vs Dynamic",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Static attacks eavesdrop/monitor without modifying data (Passive); Dynamic attacks intercept, alter, delete, or inject fake data (Active/Man-in-the-Middle)."
        },
        "exam_answer": r"""
<p>Security attacks targeting mobile communication environments are classified into two major categories:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Attack Category</th>
            <th>Nature of Threat</th>
            <th>Primary Examples &amp; Impact</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Static (Passive) Attacks</strong></td>
            <td>The attacker monitors, sniffs, and listens to traffic <strong>without altering the data or interrupting the connection</strong>. Undetectable by the sender/receiver.</td>
            <td>
                <ul>
                    <li><strong>Eavesdropping / Packet Sniffing:</strong> Intercepting unencrypted Wi-Fi packets using Wireshark.</li>
                    <li><strong>Traffic Analysis:</strong> Monitoring transmission frequency and packet size to deduce user habits or location.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><strong>Dynamic (Active) Attacks</strong></td>
            <td>The attacker actively <strong>modifies, tampers with, deletes, replays, or injects fake packets</strong> into the data stream, disrupting normal service.</td>
            <td>
                <ul>
                    <li><strong>Man-in-the-Middle (MitM):</strong> Rogue Access Point ("Evil Twin") intercepting and altering banking traffic.</li>
                    <li><strong>Denial of Service (DoS / Jamming):</strong> Flooding cellular towers with RF noise to knock phones offline.</li>
                    <li><strong>Replay Attack:</strong> Capturing a valid authentication token and retransmitting it later to gain unauthorized entry.</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p><strong>Static attack:</strong> Someone sitting quietly behind you on a bus reading your private WhatsApp messages over your shoulder. You have no idea they are watching.</p>
<p><strong>Dynamic attack:</strong> A thief snatching your phone out of your hands, typing a fake message to your boss, and throwing the phone onto the road!</p>
"""
    },

    'mobile-q33': {
        "title": "Security Protocols in Mobile Networks: SSL, TLS, and Mobile VPN",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "TLS encrypts transport layer (HTTPS); Mobile VPN (IPsec/WireGuard) creates encrypted IP tunnel that survives IP address changes during mobile roaming."
        },
        "exam_answer": r"""
<p><strong>1. SSL / TLS Architecture:</strong></p>
<ul>
    <li>Transport Layer Security (TLS 1.3, superseding obsolete SSL) operates above TCP to provide end-to-end encrypted sessions (HTTPS).</li>
    <li>Comprises two sub-protocols:
        <ul>
            <li><strong>TLS Handshake Protocol:</strong> Uses asymmetric cryptography (RSA / Elliptic Curve Diffie-Hellman) to authenticate server identity via X.509 certificates and negotiate a shared symmetric session key.</li>
            <li><strong>TLS Record Protocol:</strong> Encrypts payload data using fast symmetric ciphers (AES-GCM / ChaCha20) and verifies message integrity via HMAC.</li>
        </ul>
    </li>
</ul>

<p><strong>2. Mobile Virtual Private Network (Mobile VPN):</strong></p>
<ul>
    <li>A standard VPN drops connection whenever a mobile phone switches from Wi-Fi to 4G (because the client's local IP address changes).</li>
    <li>A <strong>Mobile VPN</strong> (using IPsec with MOBIKE / IKEv2 or WireGuard) maintains a persistent virtual IP tunnel. When the physical IP address changes, the Mobile VPN updates the tunnel endpoint seamlessly without interrupting enterprise database sessions or forcing the user to log in again.</li>
</ul>
""",
        "understand_simply": r"""
<p>When you connect to free public Wi-Fi at a railway station, anyone nearby could snoop on your internet packets. <strong>TLS (HTTPS)</strong> puts your web browsing into sealed envelopes. A <strong>Mobile VPN</strong> takes it a step further: it creates an armored underground tunnel from your phone all the way to your office computer, shielding all your apps!</p>
"""
    },

    'mobile-q34': {
        "title": "Public Key Cryptography and Complete Step-by-Step Numerical of RSA Cryptosystem",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$n = p \cdot q, \quad \phi(n) = (p-1)(q-1), \quad e \cdot d \equiv 1 \pmod{\phi(n)}, \quad C = M^e \pmod n, \quad M = C^d \pmod n$$",
            "text": "Public key $(e, n)$ encrypts; Private key $(d, n)$ decrypts; security rests on prime factorization hardness of $n$."
        },
        "exam_answer": r"""
<p><strong>1. RSA Algorithm Mathematical Framework:</strong></p>
<ol>
    <li>Choose two large distinct prime numbers $p$ and $q$.</li>
    <li>Calculate modulus $n = p \cdot q$.</li>
    <li>Calculate Euler's totient function $\phi(n) = (p - 1)(q - 1)$.</li>
    <li>Select an encryption public exponent $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.</li>
    <li>Calculate private decryption key $d$ using Extended Euclidean algorithm:
    $$d \cdot e \equiv 1 \pmod{\phi(n)} \implies d \equiv e^{-1} \pmod{\phi(n)}$$</li>
    <li><strong>Encryption:</strong> For plaintext message $M < n$, ciphertext is $C = M^e \pmod n$.</li>
    <li><strong>Decryption:</strong> Plaintext is recovered via $M = C^d \pmod n$.</li>
</ol>

<p><strong>2. Complete Step-by-Step Numerical Example:</strong><br>
Let prime numbers be $p = 3$ and $q = 11$, and message plaintext $M = 2$.</p>
<ul>
    <li><strong>Step 1: Compute $n$</strong><br>
    $$n = p \cdot q = 3 \times 11 = 33$$</li>
    <li><strong>Step 2: Compute $\phi(n)$</strong><br>
    $$\phi(n) = (p - 1)(q - 1) = (3 - 1)(11 - 1) = 2 \times 10 = 20$$</li>
    <li><strong>Step 3: Select Public Key $e$</strong><br>
    Choose $e = 3$. Check: $1 < 3 < 20$ and $\gcd(3, 20) = 1$. (Valid)</li>
    <li><strong>Step 4: Compute Private Key $d$</strong><br>
    Solve $3 \cdot d \equiv 1 \pmod{20} \implies 3d = 20k + 1$:<br>
    For $k = 1$: $3d = 21 \implies d = 7$. (Valid)<br>
    Public Key: $(e=3, n=33)$, Private Key: $(d=7, n=33)$.</li>
    <li><strong>Step 5: Encryption</strong><br>
    $$C = M^e \pmod n = 2^3 \pmod{33} = 8 \pmod{33} = 8$$
    The encrypted ciphertext is <strong>$C = 8$</strong>.</li>
    <li><strong>Step 6: Decryption (Verification)</strong><br>
    $$M = C^d \pmod n = 8^7 \pmod{33}$$
    Using modular exponentiation:
    $$8^2 = 64 \equiv -2 \pmod{33}$$
    $$8^4 = (-2)^2 = 4 \pmod{33}$$
    $$8^7 = 8^4 \times 8^2 \times 8^1 = 4 \times (-2) \times 8 = -64 \equiv 2 \pmod{33}$$
    The original message <strong>$M = 2$</strong> is recovered correctly.</li>
</ul>
""",
        "understand_simply": r"""
<p>Imagine a padlock that has an open position and a special key:</p>
<p>Anyone can click the padlock shut ($e$)—that is the <strong>Public Key</strong>. You can distribute thousands of open padlocks to anyone in the world. Anyone can put a secret message into a box and snap your lock shut. But only you hold the unique brass key ($d$) that can unlock it—that is the <strong>Private Key</strong>.</p>
"""
    },

    'mobile-q35': {
        "title": "Diffie-Hellman Key Exchange Algorithm and Discrete Logarithm Problem",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$A = g^a \pmod p, \quad B = g^b \pmod p, \quad K = B^a \pmod p = A^b \pmod p = g^{ab} \pmod p$$",
            "text": "Alice and Bob establish a shared secret $K$ over an insecure public channel without transmitting secrets $a$ or $b$."
        },
        "exam_answer": r"""
<p><strong>1. Mathematical Foundation:</strong><br>
Diffie-Hellman key exchange enables two communicating parties (Alice and Bob) to establish a shared symmetric secret key over an unencrypted public radio link. Its security relies on the computational difficulty of the <strong>Discrete Logarithm Problem (DLP)</strong>: given large prime $p$, generator $g$, and $Y = g^X \pmod p$, it is computationally infeasible to compute the secret exponent $X$ in polynomial time.</p>

<p><strong>2. Step-by-Step Protocol Execution:</strong></p>
<ol>
    <li><strong>Public Parameter Agreement:</strong> Alice and Bob publicly agree on a large prime modulus $p$ and a primitive root generator $g$ ($g < p$). An eavesdropper (Eve) can see both $p$ and $g$.</li>
    <li><strong>Secret Exponent Selection:</strong>
    <ul>
        <li>Alice chooses a secret private integer $a$ ($1 < a < p$).</li>
        <li>Bob chooses a secret private integer $b$ ($1 < b < p$).</li>
    </ul></li>
    <li><strong>Public Key Computation and Exchange:</strong>
    <ul>
        <li>Alice computes public key $A = g^a \pmod p$ and transmits $A$ over the channel to Bob.</li>
        <li>Bob computes public key $B = g^b \pmod p$ and transmits $B$ over the channel to Alice.</li>
    </ul></li>
    <li><strong>Shared Secret Key Calculation:</strong>
    <ul>
        <li>Alice computes the shared key: $K = B^a \pmod p = (g^b)^a \pmod p = g^{ab} \pmod p$.</li>
        <li>Bob computes the shared key: $K = A^b \pmod p = (g^a)^b \pmod p = g^{ab} \pmod p$.</li>
    </ul></li>
    <li>Both parties possess the identical shared secret session key $K = g^{ab} \pmod p$.</li>
</ol>

<p><strong>3. Numerical Example:</strong><br>
Let public parameters be prime $p = 23$, generator $g = 5$.</p>
<ul>
    <li>Alice picks private $a = 6 \implies A = 5^6 \pmod{23} = 15625 \pmod{23} = 8$. (Sends $A=8$)</li>
    <li>Bob picks private $b = 15 \implies B = 5^{15} \pmod{23} = 19$. (Sends $B=19$)</li>
    <li>Alice computes: $K = B^a \pmod p = 19^6 \pmod{23} = 2$.</li>
    <li>Bob computes: $K = A^b \pmod p = 8^{15} \pmod{23} = 2$.</li>
    <li>Shared Secret Key: <strong>$K = 2$</strong>.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of mixing paint colors in plain view of an eavesdropper:</p>
<p>Alice and Bob agree on a common background color (Yellow). Alice secretly adds her private color (Teal) to make a blended muddy color, which she sends to Bob. Bob secretly adds his private color (Orange) to Yellow, creating a different blend, and sends it to Alice. Now, Alice adds her secret Teal to Bob's blend, and Bob adds his secret Orange to Alice's blend. Both end up with the exact same final mixture! An eavesdropper saw all the blended paints travel across the room, but cannot separate the original secret colors.</p>
"""
    },

    'mobile-q36': {
        "title": "Orthogonal Frequency Division Multiplexing (OFDM) in Next-Generation Mobile Networks",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\Delta f = \frac{1}{T_s}, \quad \int_0^{T_s} \cos(2\pi f_i t)\cos(2\pi f_j t)dt = 0 \quad (i \ne j)$$",
            "text": "OFDM splits wideband channel into orthogonal narrowband subcarriers; Cyclic Prefix (CP) eliminates Intersymbol Interference (ISI)."
        },
        "exam_answer": r"""
<p><strong>1. Motivation for OFDM:</strong><br>
In high-speed wireless networks (4G LTE, 5G NR, Wi-Fi 6), transmitting data at high symbol rates over a single carrier causes the symbol duration $T_s$ to become smaller than the channel multipath delay spread $T_d$ ($T_s < T_d$). This produces severe frequency-selective fading and destructive <strong>Intersymbol Interference (ISI)</strong>.</p>

<p><strong>2. Core Mathematical Principle of Orthogonality:</strong><br>
OFDM splits a single high-speed serial data stream into $N$ parallel low-speed substreams modulated onto closely spaced subcarriers. The subcarrier frequency spacing is chosen to be:
$$\Delta f = \frac{1}{T_s}$$
Over symbol period $T_s$, the subcarriers are mathematically orthogonal:
$$\frac{1}{T_s} \int_0^{T_s} e^{j 2\pi f_i t} \cdot e^{-j 2\pi f_j t} \, dt = \begin{cases} 1, & i = j \\ 0, & i \ne j \end{cases}$$
Because subcarriers are orthogonal, their spectral lobes overlap heavily without causing cross-talk! This yields maximum spectral efficiency without needing guard bands between subcarriers.</p>

<p><strong>3. Role of the Cyclic Prefix (CP):</strong></p>
<ul>
    <li>To completely eliminate Intersymbol Interference caused by multipath echoes from buildings, a guard interval is inserted before each OFDM symbol.</li>
    <li>Instead of leaving the guard interval empty (which would destroy subcarrier orthogonality), the end portion of the OFDM symbol is copied and pasted onto the beginning of the symbol. This is called the <strong>Cyclic Prefix (CP)</strong>.</li>
    <li>As long as the cyclic prefix length exceeds the channel delay spread ($T_{\text{CP}} > T_{\text{delay}}$), multipath echoes fall harmlessly inside the CP window, preserving zero ISI and zero Inter-Carrier Interference (ICI).</li>
</ul>

<p><strong>4. Generation via IFFT/FFT:</strong><br>
Modulation is performed digitally using an Inverse Fast Fourier Transform (IFFT) at the transmitter, and demodulation is executed using an FFT at the receiver, making hardware implementation highly efficient.</p>
""",
        "understand_simply": r"""
<p>Imagine transporting 100 passengers across a busy bridge. If you put everyone into one gigantic, long trailer truck (single carrier), it easily gets jammed and delayed around tight corners (ISI). But if you put the 100 passengers into 50 small parallel cars (OFDM subcarriers) driving side by side, each car moves at a relaxed, safe pace and arrives without getting stuck!</p>
"""
    },

    'mobile-q37': {
        "title": "Multimedia Broadcast and Multicast Services (MBMS) and MPLS in Mobile Networks",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": None,
            "text": "MBMS transmits one single radio stream to unlimited users simultaneously (Point-to-Multipoint); MPLS uses 32-bit labels for wire-speed core packet forwarding."
        },
        "exam_answer": r"""
<p><strong>1. Multimedia Broadcast Multicast Service (MBMS):</strong></p>
<ul>
    <li><strong>Problem:</strong> If 1,000 mobile subscribers in a stadium stream a live football match via standard unicast, the mobile tower must transmit 1,000 separate radio streams, instantly crashing the cellular network.</li>
    <li><strong>MBMS Solution:</strong> MBMS transmits a single broadcast radio bearer over the cell. All 1,000 subscribers listen to that single radio stream simultaneously (Point-to-Multipoint), conserving $99.9\%$ of radio spectrum!</li>
    <li><strong>Core Architecture:</strong>
        <ul>
            <li><strong>BM-SC (Broadcast Multicast Service Center):</strong> Central server authenticating broadcast content providers and scheduling content streams.</li>
            <li><strong>MBMS Gateway:</strong> Replicates IP multicast packets to serving base stations.</li>
        </ul>
    </li>
</ul>

<p><strong>2. Multi-Protocol Label Switching (MPLS) in Mobile Backhaul:</strong></p>
<ul>
    <li>Traditional IP routing inspects destination IP addresses at every single hop, causing router latency bottlenecks.</li>
    <li><strong>MPLS Principle:</strong> Packets entering the mobile core network are stamped with a short <strong>32-bit Label</strong>. Core routers (Label Switch Routers, LSRs) inspect <em>only</em> this label and forward packets along pre-established Label Switched Paths (LSP) using fast hardware lookups.</li>
    <li><strong>Benefits for Mobile Networks:</strong>
        <ul>
            <li>Enables deterministic Quality of Service (QoS) and traffic engineering for latency-sensitive 5G voice and video streams.</li>
            <li>Enables rapid network protection switching ($< 50\text{ ms}$ rerouting if a fiber link breaks).</li>
        </ul>
    </li>
</ul>
""",
        "understand_simply": r"""
<p><strong>MBMS:</strong> Instead of having 50 separate televisions in a sports bar each playing their own private stream of the football game, you put one big screen on the wall that all 50 people watch together!</p>
<p><strong>MPLS:</strong> Instead of postal workers reading the full destination country, state, city, street, and house address on every single letter at every street corner, they stamp a simple 2-digit color tag on the envelope so sorting machines zip it along at lightning speed!</p>
"""
    },

    'mobile-q38': {
        "title": "Cellular Network Evolution: 2G to 5G Architectural and Functional Comparison",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "2G (Voice/TDMA, 64 kbps) $\\to$ 3G (CDMA/WCDMA, 2 Mbps) $\\to$ 4G (All-IP/OFDMA, 100 Mbps) $\\to$ 5G (Network Slicing, eMBB/URLLC/mMTC, 10-20 Gbps)."
        },
        "exam_answer": r"""
<p>Mobile cellular communications evolved across five generations to meet surging data demands:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Generation</th>
            <th>Primary Access &amp; Core Architecture</th>
            <th>Peak Data Speed</th>
            <th>Key Technical Features &amp; Applications</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>2G</strong><br>(GSM, 1991)</td>
            <td>TDMA / FDMA.<br>Circuit-switched core (MSC, HLR, VLR).</td>
            <td>$9.6\text{ to } 64\text{ kbps}$<br>(GPRS: $171\text{ kbps}$)</td>
            <td>First digital cellular system. Introduced digital encrypted voice, SMS text messaging, and SIM cards.</td>
        </tr>
        <tr>
            <td><strong>3G</strong><br>(UMTS, 2001)</td>
            <td>W-CDMA / CDMA2000.<br>Dual-domain core (Circuit-switched voice + Packet-switched data).</td>
            <td>$2\text{ to } 42\text{ Mbps}$<br>(HSPA+)</td>
            <td>True mobile broadband; enabled mobile web browsing, video calling, mobile TV, and GPS navigation.</td>
        </tr>
        <tr>
            <td><strong>4G LTE</strong><br>(2010)</td>
            <td>OFDMA (Downlink) + SC-FDMA (Uplink).<br><strong>Flat All-IP EPC</strong> (Evolved Packet Core: MME, SGW, PGW).</td>
            <td>$100\text{ Mbps to } 1\text{ Gbps}$<br>(LTE-Advanced)</td>
            <td>Eliminated circuit switching entirely (Voice over LTE / VoLTE); enabled HD video streaming, smartphone app economy, and low latency ($< 20\text{ ms}$).</td>
        </tr>
        <tr>
            <td><strong>5G NR</strong><br>(2020)</td>
            <td>Scalable OFDMA (Sub-6 GHz &amp; mmWave).<br><strong>Service-Based Architecture (SBA)</strong> with Network Slicing and Cloud-native microservices.</td>
            <td>$10\text{ to } 20\text{ Gbps}$</td>
            <td>Three core pillars:
                <ol>
                    <li><strong>eMBB:</strong> Enhanced Mobile Broadband (ultra-fast downloads, AR/VR).</li>
                    <li><strong>URLLC:</strong> Ultra-Reliable Low-Latency Communication ($< 1\text{ ms}$, autonomous driving, remote surgery).</li>
                    <li><strong>mMTC:</strong> Massive Machine-Type Communication ($10^6 \text{ IoT devices/km}^2$).</li>
                </ol>
            </td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>The generations of mobile networks are like vehicle upgrades on a highway:</p>
<ul>
    <li><strong>2G:</strong> A telegram delivery bicycle (reliable voice and text).</li>
    <li><strong>3G:</strong> A small family hatchback car (can load web pages and simple music).</li>
    <li><strong>4G:</strong> A high-speed electric sports car (smoothly streams 4K YouTube and video calls anywhere).</li>
    <li><strong>5G:</strong> A supersonic bullet train network with dedicated private tracks: one track for ultra-fast entertainment, one dedicated hyper-safe track for driverless cars, and one track monitoring millions of smart city meters!</li>
</ul>
"""
    }
}
