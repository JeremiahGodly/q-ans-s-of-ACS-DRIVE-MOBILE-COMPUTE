# -*- coding: utf-8 -*-
"""
Batch vector diagram generator for missing Mobile Computing (CST415) questions.
Renders 26 high-resolution 960x460 engineering schematics to PNG using sips.
"""
import os, subprocess, re

os.makedirs("images/mobile_compute", exist_ok=True)

def render_svg_to_png(svg_content, png_path):
    if os.path.exists(png_path) and os.path.getsize(png_path) > 1000:
        return
    svg_content = re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_content)
    svg_path = png_path.replace(".png", ".svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    res = subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], 
                         capture_output=True, text=True)
    if os.path.exists(svg_path):
        os.remove(svg_path)
    if os.path.exists(png_path):
        print(f"Rendered -> {png_path} ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"Error rendering {png_path}: {res.stderr}")

def create_card_diagram(png_path, title, subtitle, accent_color, badge_text, elements_xml, footer_text=""):
    title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    subtitle = subtitle.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    footer_text = footer_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    badge_text = badge_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="460" viewBox="0 0 960 460">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1220"/>
      <stop offset="100%" stop-color="#151d30"/>
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{accent_color}"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#10b981"/>
    </marker>
  </defs>
  <rect width="960" height="460" fill="url(#bgGrad)" rx="16"/>
  <rect x="20" y="20" width="920" height="420" fill="none" stroke="#223049" stroke-width="1.5" rx="12"/>
  
  <rect x="40" y="35" width="140" height="26" fill="{accent_color}22" stroke="{accent_color}" stroke-width="1" rx="5"/>
  <text x="110" y="52" fill="{accent_color}" font-family="-apple-system, sans-serif" font-size="12" font-weight="700" text-anchor="middle">{badge_text}</text>
  <text x="500" y="55" fill="#f1f5f9" font-family="-apple-system, sans-serif" font-size="18" font-weight="700" text-anchor="middle">{title}</text>
  <text x="500" y="80" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="13" text-anchor="middle">{subtitle}</text>
  {elements_xml}
  {f'''<rect x="40" y="405" width="880" height="24" fill="#0b111e" stroke="#223049" stroke-width="1" rx="4"/>
  <text x="480" y="421" fill="#94a3b8" font-family="-apple-system, sans-serif" font-size="11" font-weight="600" text-anchor="middle">{footer_text}</text>''' if footer_text else ''}
</svg>"""
    render_svg_to_png(svg, png_path)

print("Starting generation of missing Mobile Computing diagrams...")

# 1. mobile-q1: middleware_architecture.png
create_card_diagram(
    "images/mobile_compute/middleware_architecture.png",
    "Mobile Middleware and Gateway Architecture",
    "Protocol Bridging, Data Compression, Security Mediation, and State Synchronization between Clients and Enterprise Backends",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- Tier 1: Mobile Clients -->
    <rect x="60" y="120" width="220" height="250" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="170" y="150" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">Tier 1: Mobile Clients</text>
    <rect x="80" y="170" width="180" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="170" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Smartphones / Tablets</text>
    <rect x="80" y="225" width="180" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="170" y="250" fill="#f1f5f9" font-size="12" text-anchor="middle">IoT / Edge Devices</text>
    <text x="170" y="300" fill="#cbd5e1" font-size="11" text-anchor="middle">Constraint: Battery, CPU,</text>
    <text x="170" y="320" fill="#cbd5e1" font-size="11" text-anchor="middle">Intermittent Connectivity</text>
    <text x="170" y="345" fill="#fbbf24" font-size="11" text-anchor="middle">Lightweight Protocols</text>

    <!-- Communication arrows -->
    <path d="M 280 230 L 350 230" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <path d="M 350 260 L 280 260" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="315" y="220" fill="#34d399" font-size="10" text-anchor="middle">Wireless</text>

    <!-- Tier 2: Middleware & Gateways -->
    <rect x="360" y="120" width="260" height="250" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="490" y="150" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">Tier 2: Mobile Middleware</text>
    <rect x="380" y="170" width="220" height="35" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="490" y="193" fill="#34d399" font-size="12" font-weight="600" text-anchor="middle">Protocol Conversion &amp; Proxy</text>
    <rect x="380" y="215" width="220" height="35" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="490" y="238" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">Data Compression &amp; Transcoding</text>
    <rect x="380" y="260" width="220" height="35" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="490" y="283" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">Offline Cache &amp; Sync Engine</text>
    <rect x="380" y="305" width="220" height="35" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="490" y="328" fill="#c084fc" font-size="12" font-weight="600" text-anchor="middle">Security &amp; Token Authentication</text>

    <!-- Communication arrows -->
    <path d="M 620 230 L 690 230" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <path d="M 690 260 L 620 260" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="655" y="220" fill="#34d399" font-size="10" text-anchor="middle">High-Speed</text>

    <!-- Tier 3: Enterprise Backend -->
    <rect x="700" y="120" width="210" height="250" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="805" y="150" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">Tier 3: Enterprise Cloud</text>
    <rect x="715" y="170" width="180" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="805" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Database Clusters (SQL/NoSQL)</text>
    <rect x="715" y="225" width="180" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="805" y="250" fill="#f1f5f9" font-size="12" text-anchor="middle">Legacy ERP / Core APIs</text>
    <text x="805" y="300" fill="#cbd5e1" font-size="11" text-anchor="middle">High-Bandwidth</text>
    <text x="805" y="320" fill="#cbd5e1" font-size="11" text-anchor="middle">Heavy Computational Engines</text>
    <text x="805" y="345" fill="#34d399" font-size="11" text-anchor="middle">Always-On Availability</text>
    """,
    "Middleware abstracts physical network heterogeneity, converts heavy enterprise formats (SOAP/XML) to lightweight mobile payloads (JSON/Protobuf)"
)

# 2. mobile-q2: ubiquitous_internet.png
create_card_diagram(
    "images/mobile_compute/ubiquitous_internet.png",
    "The Internet as the Ubiquitous Backbone of Mobile Computing",
    "Seamless Convergence of Heterogeneous Networks: 4G/5G Cellular, Wi-Fi, Satellite, and IP Packet Routing",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- Central IP Core -->
    <circle cx="480" cy="245" r="75" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2.5"/>
    <text x="480" y="235" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Global IP</text>
    <text x="480" y="255" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Backbone</text>
    <text x="480" y="275" fill="#cbd5e1" font-size="11" text-anchor="middle">(IPv4 / IPv6, BGP)</text>

    <!-- Satellite Orbit -->
    <rect x="80" y="125" width="160" height="70" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="160" y="152" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">LEO / GEO Satellite</text>
    <text x="160" y="175" fill="#cbd5e1" font-size="11" text-anchor="middle">Global Coverage</text>
    <path d="M 240 170 L 415 215" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Cellular Network (5G/4G) -->
    <rect x="720" y="125" width="160" height="70" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="800" y="152" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">4G LTE / 5G Core</text>
    <text x="800" y="175" fill="#cbd5e1" font-size="11" text-anchor="middle">High Mobility &amp; QoE</text>
    <path d="M 720 170 L 545 215" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Public Wi-Fi / Hotspots -->
    <rect x="80" y="295" width="160" height="70" fill="url(#boxGrad)" stroke="#a855f7" rx="6"/>
    <text x="160" y="322" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">Wi-Fi 6 / 7 (802.11)</text>
    <text x="160" y="345" fill="#cbd5e1" font-size="11" text-anchor="middle">Local High Throughput</text>
    <path d="M 240 320 L 415 275" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Edge Clouds & CDNs -->
    <rect x="720" y="295" width="160" height="70" fill="url(#boxGrad)" stroke="#10b981" rx="6"/>
    <text x="800" y="322" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Edge Compute &amp; CDN</text>
    <text x="800" y="345" fill="#cbd5e1" font-size="11" text-anchor="middle">Low Latency Caching</text>
    <path d="M 720 320 L 545 275" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>

    <text x="480" y="380" fill="#f1f5f9" font-size="12" text-anchor="middle">Unified IP layer hides differences in physical transmission mediums to provide pervasive anytime/anywhere connectivity</text>
    """,
    "Ubiquitous Computing Ideal: Mobile IP, TCP extensions, and DNS enable seamless handover across Wi-Fi and Cellular networks"
)

# 3. mobile-q3: network_segmentation.png
create_card_diagram(
    "images/mobile_compute/network_segmentation.png",
    "Mobile Network Segmentation: Core, Edge, and Access Networks",
    "Hierarchical Distribution of Data Processing, Routing, and Wireless Transmission Across Mobile Infrastructures",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- Segment 1: Access Network -->
    <rect x="50" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="180" y="145" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">1. Access Network (RAN)</text>
    <rect x="70" y="170" width="220" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="180" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Base Stations (gNB / eNodeB)</text>
    <rect x="70" y="220" width="220" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="180" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">Wi-Fi APs / Small Cells</text>
    <text x="180" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">Role: Radio frequency modulation,</text>
    <text x="180" y="310" fill="#cbd5e1" font-size="11" text-anchor="middle">air-interface scheduling, MIMO beamforming</text>
    <text x="180" y="345" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Last-Hop Wireless Connection</text>

    <!-- Arrow -->
    <path d="M 315 245 L 345 245" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Segment 2: Edge Network -->
    <rect x="350" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="480" y="145" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">2. Edge Network (MEC)</text>
    <rect x="370" y="170" width="220" height="40" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="480" y="195" fill="#34d399" font-size="12" font-weight="600" text-anchor="middle">Multi-Access Edge Computing</text>
    <rect x="370" y="220" width="220" height="40" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="480" y="245" fill="#fbbf24" font-size="12" text-anchor="middle">Local UPF (User Plane Function)</text>
    <text x="480" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">Role: Sub-10ms ultra-low latency,</text>
    <text x="480" y="310" fill="#cbd5e1" font-size="11" text-anchor="middle">local caching, AR/VR and V2X processing</text>
    <text x="480" y="345" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">Distributed Edge Cloud</text>

    <!-- Arrow -->
    <path d="M 615 245 L 645 245" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Segment 3: Core Network -->
    <rect x="650" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="780" y="145" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">3. Core Network (5GC/EPC)</text>
    <rect x="670" y="170" width="220" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="780" y="195" fill="#f1f5f9" font-size="12" text-anchor="middle">Control Plane (AMF, SMF, UDM)</text>
    <rect x="670" y="220" width="220" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="780" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">Charging &amp; Policy (PCF, CHF)</text>
    <text x="780" y="290" fill="#cbd5e1" font-size="11" text-anchor="middle">Role: Subscriber authentication,</text>
    <text x="780" y="310" fill="#cbd5e1" font-size="11" text-anchor="middle">mobility management, global IP routing</text>
    <text x="780" y="345" fill="#c084fc" font-size="11" font-weight="600" text-anchor="middle">Centralized High-Capacity Backbone</text>
    """,
    "Network Slicing: Core and Edge networks dynamically partition physical hardware into isolated logical slices (eMBB, URLLC, mMTC)"
)

# 4. mobile-q4: mobile_limitations.png
create_card_diagram(
    "images/mobile_compute/mobile_limitations.png",
    "Intrinsic Physical Limitations of Mobile Computing",
    "Engineering Challenges: Resource Scarcity, Wireless Channel Dynamics, Physical Hostility, and Security Vulnerabilities",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- Quadrant 1: Battery & Resource Constraints -->
    <rect x="50" y="115" width="410" height="120" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="80" y="142" fill="#f87171" font-size="14" font-weight="700">1. Battery &amp; Energy Scarcity</text>
    <text x="80" y="168" fill="#cbd5e1" font-size="12">• Electrochemical batteries improve only 5-8% annually</text>
    <text x="80" y="190" fill="#cbd5e1" font-size="12">• Radios consume high transmission power (TX/RX energy drain)</text>
    <text x="80" y="212" fill="#f1f5f9" font-size="11">Mitigation: Dynamic Voltage Scaling (DVS) &amp; Sleep Scheduling</text>

    <!-- Quadrant 2: Wireless Dynamics -->
    <rect x="500" y="115" width="410" height="120" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="530" y="142" fill="#fbbf24" font-size="14" font-weight="700">2. Wireless Communication Variability</text>
    <text x="530" y="168" fill="#cbd5e1" font-size="12">• Multipath fading, Doppler shift, shadowing, interference</text>
    <text x="530" y="190" fill="#cbd5e1" font-size="12">• Bandwidth varies dynamically; frequent burst packet loss</text>
    <text x="530" y="212" fill="#f1f5f9" font-size="11">Mitigation: Adaptive Modulation and Coding (AMC) &amp; FEC</text>

    <!-- Quadrant 3: Mobility & Disconnection -->
    <rect x="50" y="255" width="410" height="120" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="80" y="282" fill="#38bdf8" font-size="14" font-weight="700">3. Mobility &amp; Intermittent Disconnection</text>
    <text x="80" y="308" fill="#cbd5e1" font-size="12">• Involuntary handovers between cells, dead zones in tunnels</text>
    <text x="80" y="330" fill="#cbd5e1" font-size="12">• TCP misinterprets wireless loss as congestion, throttling speeds</text>
    <text x="80" y="352" fill="#f1f5f9" font-size="11">Mitigation: Hoarding, pre-fetching, and Mobile IP fast handovers</text>

    <!-- Quadrant 4: Physical & Security Vulnerabilities -->
    <rect x="500" y="255" width="410" height="120" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="530" y="282" fill="#c084fc" font-size="14" font-weight="700">4. Physical Hostility &amp; Security Risks</text>
    <text x="530" y="308" fill="#cbd5e1" font-size="12">• Susceptible to physical loss, device theft, and environmental wear</text>
    <text x="530" y="330" fill="#cbd5e1" font-size="12">• Open broadcast medium permits passive eavesdropping &amp; spoofing</text>
    <text x="530" y="352" fill="#f1f5f9" font-size="11">Mitigation: Hardware keystores, biometric auth &amp; remote wipe</text>
    """,
    "Engineering Trade-off: Mobile design requires asymmetric computing where heavy computations are offloaded to edge/cloud servers"
)

# 5. mobile-q6: design_considerations.png
create_card_diagram(
    "images/mobile_compute/design_considerations.png",
    "Comprehensive Design Considerations for Mobile Computing Systems",
    "Multi-Disciplinary Design Pillars: Energy Efficiency, Context-Awareness, Reliability, and UI Adaptability",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- 4 Pillar Cards -->
    <rect x="50" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="150" y="145" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">1. Energy Design</text>
    <text x="150" y="180" fill="#cbd5e1" font-size="11" text-anchor="middle">Power-aware algorithms</text>
    <text x="150" y="205" fill="#cbd5e1" font-size="11" text-anchor="middle">Radio sleep scheduling</text>
    <text x="150" y="230" fill="#cbd5e1" font-size="11" text-anchor="middle">Computation offloading</text>
    <text x="150" y="255" fill="#cbd5e1" font-size="11" text-anchor="middle">Dark mode UI savings</text>
    <text x="150" y="295" fill="#fbbf24" font-size="11" text-anchor="middle">Maximize battery runtime</text>
    <text x="150" y="335" fill="#34d399" font-size="10" text-anchor="middle">Low idle current drain</text>

    <rect x="270" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="370" y="145" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">2. Context Awareness</text>
    <text x="370" y="180" fill="#cbd5e1" font-size="11" text-anchor="middle">Location (GPS/Cell/Wi-Fi)</text>
    <text x="370" y="205" fill="#cbd5e1" font-size="11" text-anchor="middle">Network quality sensing</text>
    <text x="370" y="230" fill="#cbd5e1" font-size="11" text-anchor="middle">User activity &amp; posture</text>
    <text x="370" y="255" fill="#cbd5e1" font-size="11" text-anchor="middle">Ambient light sensors</text>
    <text x="370" y="295" fill="#fbbf24" font-size="11" text-anchor="middle">Dynamic self-adaptation</text>
    <text x="370" y="335" fill="#38bdf8" font-size="10" text-anchor="middle">Context-driven services</text>

    <rect x="490" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="590" y="145" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">3. Disconnection &amp; Data</text>
    <text x="590" y="180" fill="#cbd5e1" font-size="11" text-anchor="middle">Local SQLite caching</text>
    <text x="590" y="205" fill="#cbd5e1" font-size="11" text-anchor="middle">Optimistic transactions</text>
    <text x="590" y="230" fill="#cbd5e1" font-size="11" text-anchor="middle">Delta synchronization</text>
    <text x="590" y="255" fill="#cbd5e1" font-size="11" text-anchor="middle">Conflict resolution rules</text>
    <text x="590" y="295" fill="#fbbf24" font-size="11" text-anchor="middle">Graceful degradation</text>
    <text x="590" y="335" fill="#fbbf24" font-size="10" text-anchor="middle">Offline-first resilience</text>

    <rect x="710" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="810" y="145" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">4. Security &amp; UI</text>
    <text x="810" y="180" fill="#cbd5e1" font-size="11" text-anchor="middle">Hardware keystores</text>
    <text x="810" y="205" fill="#cbd5e1" font-size="11" text-anchor="middle">End-to-end TLS / mTLS</text>
    <text x="810" y="230" fill="#cbd5e1" font-size="11" text-anchor="middle">Biometric auth (Touch/Face)</text>
    <text x="810" y="255" fill="#cbd5e1" font-size="11" text-anchor="middle">Responsive viewport</text>
    <text x="810" y="295" fill="#fbbf24" font-size="11" text-anchor="middle">Zero-trust mobile defense</text>
    <text x="810" y="335" fill="#c084fc" font-size="10" text-anchor="middle">Intuitive touchscreen touch</text>
    """,
    "Mobile Design Axiom: Build for intermittent, low-bandwidth, battery-constrained devices while providing fluid user experiences"
)

# 6. mobile-q7: context_aware_managers.png
create_card_diagram(
    "images/mobile_compute/context_aware_managers.png",
    "Context-Aware System Management Architecture",
    "Coordination of Client Context, Policy, Security, and Adaptability Managers for Dynamic Environmental Tuning",
    "#10b981", "MOBILE • MOD 1",
    """
    <!-- Sensor Inputs -->
    <rect x="50" y="140" width="130" height="210" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="115" y="165" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Context Inputs</text>
    <text x="115" y="195" fill="#cbd5e1" font-size="11" text-anchor="middle">GPS / Location</text>
    <text x="115" y="220" fill="#cbd5e1" font-size="11" text-anchor="middle">Battery Level (%)</text>
    <text x="115" y="245" fill="#cbd5e1" font-size="11" text-anchor="middle">Network RTT &amp; BW</text>
    <text x="115" y="270" fill="#cbd5e1" font-size="11" text-anchor="middle">User Status (Work/Car)</text>
    <text x="115" y="295" fill="#cbd5e1" font-size="11" text-anchor="middle">Ambient Light</text>
    <text x="115" y="325" fill="#fbbf24" font-size="11" text-anchor="middle">Device Posture</text>

    <path d="M 180 245 L 230 245" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- Central Manager Hub -->
    <rect x="240" y="125" width="460" height="240" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="10"/>
    <text x="470" y="155" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Context-Aware Management Framework</text>

    <!-- Manager 1: Client Context -->
    <rect x="260" y="175" width="200" height="70" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="360" y="200" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">1. Client Context Manager</text>
    <text x="360" y="225" fill="#cbd5e1" font-size="11" text-anchor="middle">Aggregates &amp; models raw context</text>

    <!-- Manager 2: Policy Manager -->
    <rect x="480" y="175" width="200" height="70" fill="#0b111e" stroke="#fbbf24" stroke-width="1.5" rx="6"/>
    <text x="580" y="200" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">2. Policy Manager</text>
    <text x="580" y="225" fill="#cbd5e1" font-size="11" text-anchor="middle">Evaluates rules &amp; SLA constraints</text>

    <!-- Manager 3: Security Manager -->
    <rect x="260" y="265" width="200" height="70" fill="#0b111e" stroke="#ef4444" stroke-width="1.5" rx="6"/>
    <text x="360" y="290" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">3. Security Manager</text>
    <text x="360" y="315" fill="#cbd5e1" font-size="11" text-anchor="middle">Risk-based access &amp; encryption</text>

    <!-- Manager 4: Adaptability Manager -->
    <rect x="480" y="265" width="200" height="70" fill="#0b111e" stroke="#a855f7" stroke-width="1.5" rx="6"/>
    <text x="580" y="290" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">4. Adaptability Manager</text>
    <text x="580" y="315" fill="#cbd5e1" font-size="11" text-anchor="middle">Executes content &amp; UI adaptations</text>

    <path d="M 700 245 L 750 245" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Action Outputs -->
    <rect x="760" y="140" width="150" height="210" fill="url(#boxGrad)" stroke="#10b981" rx="8"/>
    <text x="835" y="165" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">System Action</text>
    <text x="835" y="200" fill="#cbd5e1" font-size="11" text-anchor="middle">Transcode Video</text>
    <text x="835" y="225" fill="#cbd5e1" font-size="11" text-anchor="middle">Throttle Background Sync</text>
    <text x="835" y="250" fill="#cbd5e1" font-size="11" text-anchor="middle">Trigger Biometric Prompt</text>
    <text x="835" y="275" fill="#cbd5e1" font-size="11" text-anchor="middle">Switch to Offline Mode</text>
    <text x="835" y="305" fill="#fbbf24" font-size="11" text-anchor="middle">Adjust Display Brightness</text>
    """,
    "Adaptive Loop: Sense (Context Manager) → Decide (Policy &amp; Security Managers) → Act (Adaptability Manager)"
)

# 7. mobile-q8: content_adaptation_transcoding.png
create_card_diagram(
    "images/mobile_compute/content_adaptation_transcoding.png",
    "Content Adaptation Attributes and Transcoding Classifications",
    "Syntactic (Format Re-encoding), Structural (Layout Transformation), and Semantic (Summarization/Extraction) Transcoding",
    "#10b981", "MOBILE • MOD 1",
    """
    <rect x="50" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="180" y="145" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">1. Syntactic Transcoding</text>
    <rect x="70" y="170" width="220" height="50" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="180" y="195" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">Format &amp; Codec Conversion</text>
    <text x="180" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">BMP/PNG → WebP/JPEG, WAV → AAC</text>
    <text x="180" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">Preserves original content schema</text>
    <text x="180" y="275" fill="#cbd5e1" font-size="11" text-anchor="middle">Modifies data encoding &amp; compression</text>
    <text x="180" y="305" fill="#34d399" font-size="11" text-anchor="middle">Resolution downscaling (4K → 720p)</text>
    <text x="180" y="340" fill="#fbbf24" font-size="11" text-anchor="middle">Reduces network bit-rate drastically</text>

    <rect x="350" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#fbbf24" stroke-width="1.5" rx="8"/>
    <text x="480" y="145" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">2. Structural Transcoding</text>
    <rect x="370" y="170" width="220" height="50" fill="#0b111e" stroke="#fbbf24" rx="4"/>
    <text x="480" y="195" fill="#fbbf24" font-size="12" font-weight="600" text-anchor="middle">DOM &amp; Presentation Restructuring</text>
    <text x="480" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">Multi-column HTML → Single column</text>
    <text x="480" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">Modifies spatial relationships</text>
    <text x="480" y="275" fill="#cbd5e1" font-size="11" text-anchor="middle">Pagination of long web documents</text>
    <text x="480" y="305" fill="#38bdf8" font-size="11" text-anchor="middle">Converts large tables to card lists</text>
    <text x="480" y="340" fill="#fbbf24" font-size="11" text-anchor="middle">Optimizes for small smartphone screens</text>

    <rect x="650" y="115" width="260" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="780" y="145" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">3. Semantic Transcoding</text>
    <rect x="670" y="170" width="220" height="50" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="780" y="195" fill="#34d399" font-size="12" font-weight="600" text-anchor="middle">Content Abstraction &amp; Extraction</text>
    <text x="780" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">Text-to-Speech, Video Keyframe Summaries</text>
    <text x="780" y="245" fill="#f1f5f9" font-size="12" text-anchor="middle">Changes information meaning/depth</text>
    <text x="780" y="275" fill="#cbd5e1" font-size="11" text-anchor="middle">Replaces heavy images with alt-text</text>
    <text x="780" y="305" fill="#c084fc" font-size="11" text-anchor="middle">Extracts executive summaries of news</text>
    <text x="780" y="340" fill="#fbbf24" font-size="11" text-anchor="middle">Extreme bandwidth conservation (&gt;90%)</text>
    """,
    "Transcoding Pipeline: Proxy inspects User-Agent &amp; Network RTT to select optimal combination of syntactic, structural, and semantic filters"
)

# 8. mobile-q9: seamless_communication_roaming.png
create_card_diagram(
    "images/mobile_compute/seamless_communication_roaming.png",
    "Seamless Communication and Roaming Architecture",
    "State Preservation During Handover: TCP Connection Continuity, Session State Persistence, and Sub-50ms Packet Loss Prevention",
    "#10b981", "MOBILE • MOD 1",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Seamless Handover Execution</text>
    
    <!-- Base Station 1 & 2 -->
    <rect x="80" y="175" width="140" height="60" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="150" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Source Cell (BS 1)</text>
    <text x="150" y="222" fill="#cbd5e1" font-size="11" text-anchor="middle">Current Radio Link</text>

    <rect x="280" y="175" width="140" height="60" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="350" y="202" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Target Cell (BS 2)</text>
    <text x="350" y="222" fill="#cbd5e1" font-size="11" text-anchor="middle">New Radio Link</text>

    <!-- X2 / Direct Forwarding Link -->
    <path d="M 220 205 L 280 205" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="3,3" marker-end="url(#arrow)"/>
    <text x="250" y="195" fill="#fbbf24" font-size="10" text-anchor="middle">X2 Forwarding</text>

    <rect x="80" y="270" width="340" height="85" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="250" y="295" fill="#f1f5f9" font-size="12" font-weight="700" text-anchor="middle">Make-Before-Break Principle</text>
    <text x="250" y="318" fill="#cbd5e1" font-size="11" text-anchor="middle">Packets in transit are buffered and forwarded via X2 interface</text>
    <text x="250" y="338" fill="#34d399" font-size="11" text-anchor="middle">Prevents TCP packet drop and congestion collapse</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Four Facets of Seamless Roaming</text>
    
    <text x="530" y="185" fill="#38bdf8" font-size="13" font-weight="700">1. Network Layer Transparency:</text>
    <text x="530" y="205" fill="#cbd5e1" font-size="12">Mobile IP keeps IP address invariant (Home Agent / Care-of Address)</text>

    <text x="530" y="235" fill="#34d399" font-size="13" font-weight="700">2. Transport Session Continuity:</text>
    <text x="530" y="255" fill="#cbd5e1" font-size="12">TCP socket stays alive without reset (SYN/ACK sequence preserved)</text>

    <text x="530" y="285" fill="#fbbf24" font-size="13" font-weight="700">3. Application State Persistence:</text>
    <text x="530" y="305" fill="#cbd5e1" font-size="12">Active video streams and database transactions remain intact</text>

    <text x="530" y="335" fill="#a855f7" font-size="13" font-weight="700">4. Quality of Service (QoS) Parity:</text>
    <text x="530" y="355" fill="#cbd5e1" font-size="12">Resource reservation (RSVP) guarantees bandwidth in target cell</text>
    """,
    "Seamless Roaming Metric: Handover latency must remain below 50 ms for human voice and VoIP without perceptible audio stutter"
)

# 9. mobile-q11: mobile_identifiers.png
create_card_diagram(
    "images/mobile_compute/mobile_identifiers.png",
    "Mobile Station Identifiers: IMEI, IMSI, MSISDN, and TMSI",
    "Hardware Identity, SIM Subscription Identity, Telephone Directory Number, and Air-Interface Temporary Identity",
    "#10b981", "MOBILE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="120" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="80" y="142" fill="#38bdf8" font-size="14" font-weight="700">IMEI (International Mobile Equipment Identity)</text>
    <text x="80" y="165" fill="#cbd5e1" font-size="12">• 15-digit unique hardware serial number burned into mobile equipment</text>
    <text x="80" y="185" fill="#cbd5e1" font-size="12">• Structure: TAC (8 digits) + SNR (6 digits) + Check Digit (1 digit)</text>
    <text x="80" y="208" fill="#fbbf24" font-size="11">Checked against EIR (White, Gray, Black lists) to block stolen phones</text>

    <rect x="500" y="115" width="410" height="120" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="530" y="142" fill="#34d399" font-size="14" font-weight="700">IMSI (International Mobile Subscriber Identity)</text>
    <text x="530" y="165" fill="#cbd5e1" font-size="12">• Up to 15-digit internal subscription identity stored securely on SIM</text>
    <text x="530" y="185" fill="#cbd5e1" font-size="12">• Structure: MCC (3 digits) + MNC (2-3 digits) + MSIN (9-10 digits)</text>
    <text x="530" y="208" fill="#34d399" font-size="11">Identifies subscriber uniquely across all worldwide cellular networks</text>

    <rect x="50" y="255" width="410" height="120" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="80" y="282" fill="#fbbf24" font-size="14" font-weight="700">MSISDN (Mobile Station ISDN Number)</text>
    <text x="80" y="305" fill="#cbd5e1" font-size="12">• The public telephone phone number dialed by humans to reach mobile</text>
    <text x="80" y="325" fill="#cbd5e1" font-size="12">• Structure: CC (Country Code) + NDC (National Code) + SN (Subscriber)</text>
    <text x="80" y="348" fill="#cbd5e1" font-size="11">Mapped to IMSI inside the HLR; subscriber can change SIM keeping MSISDN</text>

    <rect x="500" y="255" width="410" height="120" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="530" y="282" fill="#c084fc" font-size="14" font-weight="700">TMSI (Temporary Mobile Subscriber Identity)</text>
    <text x="530" y="305" fill="#cbd5e1" font-size="12">• Random 32-bit temporary number assigned by VLR during location update</text>
    <text x="530" y="325" fill="#cbd5e1" font-size="12">• Transmitted over the unencrypted radio air interface instead of IMSI</text>
    <text x="530" y="348" fill="#f87171" font-size="11">Crucial for privacy: Prevents eavesdroppers from tracking subscriber location</text>
    """,
    "Identifier Hierarchy: User dials MSISDN → HLR translates MSISDN to IMSI → VLR generates temporary TMSI for air interface"
)

# 10. mobile-q12: call_progress_indication.png
create_card_diagram(
    "images/mobile_compute/call_progress_indication.png",
    "Call Progress Indication Mechanisms in Cellular Telephony",
    "Signaling Tone Sequences: Dial Tone, Ringback Tone, Busy Tone, Congestion, and Call Waiting Alerts",
    "#10b981", "MOBILE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Audible Call Progress Tones</text>
    
    <text x="70" y="180" fill="#38bdf8" font-size="13" font-weight="700">1. Dial Tone:</text>
    <text x="200" y="180" fill="#cbd5e1" font-size="12">Continuous 350+440 Hz (Ready for digit entry)</text>

    <text x="70" y="215" fill="#34d399" font-size="13" font-weight="700">2. Ringback Tone:</text>
    <text x="200" y="215" fill="#cbd5e1" font-size="12">440+480 Hz cadence (2s ON / 4s OFF - Alerting called party)</text>

    <text x="70" y="250" fill="#fbbf24" font-size="13" font-weight="700">3. Busy Tone:</text>
    <text x="200" y="250" fill="#cbd5e1" font-size="12">480+620 Hz fast cadence (0.5s ON / 0.5s OFF - Called busy)</text>

    <text x="70" y="285" fill="#f87171" font-size="13" font-weight="700">4. Congestion Tone:</text>
    <text x="200" y="285" fill="#cbd5e1" font-size="12">Fast re-order tone (0.25s ON / 0.25s OFF - Network trunk blocked)</text>

    <text x="70" y="320" fill="#c084fc" font-size="13" font-weight="700">5. Call Waiting Tone:</text>
    <text x="200" y="320" fill="#cbd5e1" font-size="12">Short beep injected into active voice call (New incoming call)</text>

    <text x="255" y="355" fill="#94a3b8" font-size="11" text-anchor="middle">Standardized by ITU-T Recommendation E.180</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Digital ISDN / SS7 Signaling Messages</text>
    
    <rect x="525" y="170" width="360" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="705" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">CALL PROCEEDING (Channel Allocated)</text>

    <rect x="525" y="220" width="360" height="40" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="705" y="245" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">ALERTING (Remote B-Party Phone Ringing)</text>

    <rect x="525" y="270" width="360" height="40" fill="#0b111e" stroke="#fbbf24" rx="4"/>
    <text x="705" y="295" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">CONNECT (Call Answered / Audio Path Cut-Through)</text>

    <rect x="525" y="320" width="360" height="40" fill="#0b111e" stroke="#ef4444" rx="4"/>
    <text x="705" y="345" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">DISCONNECT / RELEASE (Call Cleared / Reason Cause)</text>
    """,
    "Signaling vs In-Band: Modern digital cellular networks send out-of-band signaling messages; audible tones are generated locally by MS"
)

# 11. mobile-q15: gsm_call_routing_handover_roaming.png
create_card_diagram(
    "images/mobile_compute/gsm_call_routing_handover_roaming.png",
    "GSM Mobile Terminating Call (MTC) Routing and Handover vs Roaming",
    "Gateway MSC (GMSC) Query to HLR for MSRN, Routing to Visited MSC (VMSC), and BSS Paging Sequence",
    "#10b981", "MOBILE • MOD 2",
    """
    <!-- MTC Flow Steps -->
    <rect x="50" y="115" width="560" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="330" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">Mobile Terminating Call (MTC) Routing Flow</text>
    
    <!-- PSTN Calling Party -->
    <rect x="70" y="170" width="80" height="45" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="110" y="197" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">PSTN Caller</text>
    <path d="M 150 192 L 185 192" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- GMSC -->
    <rect x="190" y="170" width="80" height="45" fill="#0b111e" stroke="#34d399" rx="4"/>
    <text x="230" y="197" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">GMSC</text>

    <!-- Query to HLR -->
    <path d="M 230 170 L 230 145 L 360 145 L 360 170" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="295" y="140" fill="#fbbf24" font-size="10" text-anchor="middle">1. Send Routing Info (MSISDN)</text>

    <!-- HLR -->
    <rect x="330" y="170" width="80" height="45" fill="#0b111e" stroke="#fbbf24" rx="4"/>
    <text x="370" y="197" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">HLR</text>

    <!-- Query to VLR -->
    <path d="M 410 192 L 445 192" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="430" y="180" fill="#fbbf24" font-size="10" text-anchor="middle">2. Provide MSRN</text>

    <!-- VMSC / VLR -->
    <rect x="450" y="170" width="130" height="45" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="515" y="197" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">VMSC / VLR</text>

    <!-- Trunk to VMSC -->
    <path d="M 230 215 L 230 250 L 515 250 L 515 215" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="370" y="245" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">3. IAM Call Trunk Forwarded using MSRN</text>

    <!-- BSS & MS Paging -->
    <path d="M 515 215 L 515 280 L 370 280 L 370 310" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="300" y="310" width="140" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="370" y="335" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">4. BSC/BTS Paging MS</text>

    <!-- Handover vs Roaming Comparison -->
    <rect x="630" y="115" width="280" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="770" y="145" fill="#fbbf24" font-size="15" font-weight="700" text-anchor="middle">Handover vs Roaming</text>
    
    <text x="645" y="180" fill="#38bdf8" font-size="12" font-weight="700">Handover:</text>
    <text x="645" y="200" fill="#cbd5e1" font-size="11">• In-call dynamic channel switch</text>
    <text x="645" y="218" fill="#cbd5e1" font-size="11">• Duration: &lt; 50 ms</text>
    <text x="645" y="236" fill="#cbd5e1" font-size="11">• Trigger: Low RSSI / C/I ratio</text>

    <text x="645" y="270" fill="#fbbf24" font-size="12" font-weight="700">Roaming:</text>
    <text x="645" y="290" fill="#cbd5e1" font-size="11">• Inter-PLMN network switching</text>
    <text x="645" y="308" fill="#cbd5e1" font-size="11">• Idle mode location updating</text>
    <text x="645" y="326" fill="#cbd5e1" font-size="11">• Trigger: Visited network entry</text>
    <text x="645" y="348" fill="#34d399" font-size="11">• Handled via VLR/HLR bilateral SLA</text>
    """,
    "Mobile Station Roaming Number (MSRN): Temporary E.164 number allocated by VLR to route incoming trunks to the correct serving VMSC"
)

# 12. mobile-q16: ivr_theatre_booking_callflow.png
create_card_diagram(
    "images/mobile_compute/ivr_theatre_booking_callflow.png",
    "Interactive Voice Response (IVR) Architecture: Theatre Ticket Booking",
    "DTMF Tone Recognition, Text-to-Speech (TTS), Database Querying, and SMS Confirmation Sequence",
    "#10b981", "MOBILE • MOD 2",
    """
    <!-- Caller -->
    <rect x="60" y="130" width="130" height="230" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="125" y="160" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Caller (MS)</text>
    <text x="125" y="200" fill="#cbd5e1" font-size="11" text-anchor="middle">1. Dials IVR Number</text>
    <text x="125" y="235" fill="#fbbf24" font-size="11" text-anchor="middle">2. DTMF Keypresses</text>
    <text x="125" y="255" fill="#94a3b8" font-size="10" text-anchor="middle">"1" Movie, "2" Show</text>
    <text x="125" y="295" fill="#34d399" font-size="11" text-anchor="middle">3. Hears TTS Audio</text>
    <text x="125" y="330" fill="#a855f7" font-size="11" text-anchor="middle">4. Gets SMS Ticket</text>

    <path d="M 190 220 L 260 220" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <path d="M 260 250 L 190 250" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- IVR Server Engine -->
    <rect x="270" y="120" width="380" height="250" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="10"/>
    <text x="460" y="150" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">IVR Telephony Server</text>
    
    <rect x="290" y="170" width="160" height="50" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="370" y="195" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">DTMF Decoder / ASR</text>
    <text x="370" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">Detects Dual-Tone Freqs</text>

    <rect x="470" y="170" width="160" height="50" fill="#0b111e" stroke="#34d399" rx="6"/>
    <text x="550" y="195" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">TTS Audio Generator</text>
    <text x="550" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">Plays Menu Prompts</text>

    <rect x="290" y="235" width="340" height="55" fill="#0b111e" stroke="#fbbf24" rx="6"/>
    <text x="460" y="260" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">VoiceXML / Dialogue Flow Controller</text>
    <text x="460" y="278" fill="#cbd5e1" font-size="11" text-anchor="middle">Manages multi-level menu navigation &amp; timeout retries</text>

    <rect x="290" y="305" width="340" height="45" fill="#0b111e" stroke="#a855f7" rx="6"/>
    <text x="460" y="333" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">SMS Gateway Connector (SMPP Protocol)</text>

    <path d="M 650 240 L 720 240" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <path d="M 720 270 L 650 270" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- Database & Payment Backend -->
    <rect x="730" y="130" width="180" height="230" fill="url(#boxGrad)" stroke="#a855f7" rx="8"/>
    <text x="820" y="160" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">Booking Backend</text>
    <rect x="745" y="180" width="150" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="820" y="205" fill="#f1f5f9" font-size="11" text-anchor="middle">Seat Inventory DB</text>
    <rect x="745" y="235" width="150" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="820" y="260" fill="#f1f5f9" font-size="11" text-anchor="middle">Payment Gateway API</text>
    <rect x="745" y="290" width="150" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="820" y="315" fill="#34d399" font-size="11" text-anchor="middle">SMSC Service Center</text>
    """,
    "Dual-Tone Multi-Frequency (DTMF): Uses pairs of audible frequencies (e.g., 697 Hz + 1209 Hz for '1') to signal digits reliably over voice channels"
)

# 13. mobile-q18: sms_strengths.png
create_card_diagram(
    "images/mobile_compute/sms_strengths.png",
    "Architectural Distinctiveness and Strengths of SMS",
    "Store-and-Forward Delivery via Signaling Channels (SS7 SDCCH/SACCH) with Zero IP/Data Plan Dependency",
    "#10b981", "MOBILE • MOD 2",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Key Architectural Strengths</text>
    
    <text x="70" y="185" fill="#34d399" font-size="13" font-weight="700">1. Out-of-Band Signaling Transport:</text>
    <text x="70" y="205" fill="#cbd5e1" font-size="12">Transmitted over SS7 control channels (SDCCH / SACCH)</text>
    <text x="70" y="222" fill="#94a3b8" font-size="11">Can transmit during active phone calls without collisions</text>

    <text x="70" y="250" fill="#fbbf24" font-size="13" font-weight="700">2. Store-and-Forward Resilience:</text>
    <text x="70" y="270" fill="#cbd5e1" font-size="12">SMSC stores message if recipient is offline or out of coverage</text>
    <text x="70" y="287" fill="#94a3b8" font-size="11">Retries automatically when mobile becomes reachable</text>

    <text x="70" y="315" fill="#38bdf8" font-size="13" font-weight="700">3. Universal Device Compatibility:</text>
    <text x="70" y="335" fill="#cbd5e1" font-size="12">Works on 100% of GSM/LTE phones without apps or internet</text>
    <text x="70" y="352" fill="#34d399" font-size="11">Standard for 2FA OTPs, banking alerts, and emergency broadcast</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">SMS Protocol Architecture &amp; Delivery</text>
    
    <!-- Flow: MS_A -> BTS -> MSC -> SMSC -> MSC -> BTS -> MS_B -->
    <rect x="525" y="175" width="80" height="45" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="565" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MS-MO</text>
    <path d="M 605 197 L 640 197" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <rect x="645" y="175" width="120" height="45" fill="#0b111e" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="705" y="202" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">SMSC Core</text>
    <path d="M 765 197 L 800 197" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>

    <rect x="805" y="175" width="80" height="45" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="845" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MS-MT</text>

    <rect x="525" y="245" width="360" height="60" fill="#0b111e" stroke="#fbbf24" rx="6"/>
    <text x="705" y="270" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">140-Byte Signaling Payload Limit</text>
    <text x="705" y="292" fill="#cbd5e1" font-size="12" text-anchor="middle">160 characters (7-bit GSM) | 70 characters (16-bit UCS2)</text>

    <text x="705" y="340" fill="#cbd5e1" font-size="12" text-anchor="middle">Delivery Reports: MS confirms receipt to SMSC via SM-MT ACK</text>
    <text x="705" y="360" fill="#94a3b8" font-size="11" text-anchor="middle">Over-The-Air (OTA) SIM updates utilize silent SMS Class-2</text>
    """,
    "Zero Overhead on Voice: By riding on control channels, SMS creates immediate monetization without consuming voice traffic slots"
)

# 14. mobile-q19: gprs_limitations.png
create_card_diagram(
    "images/mobile_compute/gprs_limitations.png",
    "Technical Bottlenecks and Limitations of GPRS (2.5G)",
    "Air Interface Constraints: CS-1 to CS-4 Speeds (&lt;171.2 kbps), High Latency (&gt;600 ms), and Voice Preemption",
    "#10b981", "MOBILE • MOD 3",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#f87171" font-size="16" font-weight="700" text-anchor="middle">Core Bottlenecks of GPRS</text>
    
    <text x="70" y="180" fill="#f87171" font-size="13" font-weight="700">1. Voice Preemption (Circuit Priority):</text>
    <text x="70" y="200" fill="#cbd5e1" font-size="12">GSM circuit-switched voice calls take absolute priority over GPRS data</text>
    <text x="70" y="217" fill="#94a3b8" font-size="11">Data packets are abruptly dropped during high cell voice traffic</text>

    <text x="70" y="245" fill="#fbbf24" font-size="13" font-weight="700">2. Severe Sub-200 kbps Throughput:</text>
    <text x="70" y="265" fill="#cbd5e1" font-size="12">Theoretical max: 171.2 kbps (8 timeslots × CS-4 at 21.4 kbps)</text>
    <text x="70" y="282" fill="#94a3b8" font-size="11">Real-world speed: 30-50 kbps (Multislot class 4+1 with CS-2)</text>

    <text x="70" y="310" fill="#38bdf8" font-size="13" font-weight="700">3. High Latency (&gt; 600 - 1000 ms):</text>
    <text x="70" y="330" fill="#cbd5e1" font-size="12">Round-trip delays make interactive web &amp; online gaming impossible</text>
    <text x="70" y="352" fill="#cbd5e1" font-size="11">GMSK modulation lacks spectral efficiency (paved way for EDGE)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Coding Scheme (CS) Trade-offs</text>
    
    <rect x="525" y="170" width="360" height="40" fill="#0b111e" stroke="#38bdf8" rx="4"/>
    <text x="705" y="195" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">CS-1: 9.05 kbps/slot (Highest FEC protection, cell edge)</text>

    <rect x="525" y="215" width="360" height="40" fill="#0b111e" stroke="#10b981" rx="4"/>
    <text x="705" y="240" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">CS-2: 13.4 kbps/slot (Standard robust commercial profile)</text>

    <rect x="525" y="260" width="360" height="40" fill="#0b111e" stroke="#fbbf24" rx="4"/>
    <text x="705" y="285" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">CS-3: 15.6 kbps/slot (Reduced error correction code)</text>

    <rect x="525" y="305" width="360" height="40" fill="#0b111e" stroke="#ef4444" rx="4"/>
    <text x="705" y="330" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle">CS-4: 21.4 kbps/slot (Zero error protection, only near base station)</text>
    <text x="705" y="360" fill="#94a3b8" font-size="11" text-anchor="middle">EDGE (8-PSK) was later introduced to overcome GMSK limitations</text>
    """,
    "GPRS Milestone: Despite bottlenecks, GPRS established the permanent 'Always-On' packet paradigm replacing dial-up CSD"
)

# 15. mobile-q20: gprs_billing_charging.png
create_card_diagram(
    "images/mobile_compute/gprs_billing_charging.png",
    "GPRS Billing and Charging Architecture via Charging Gateway Function (CGF)",
    "Generation of S-CDRs (SGSN) and G-CDRs (GGSN) Based on Volume (Bytes), Duration, and QoS Profiles",
    "#10b981", "MOBILE • MOD 3",
    """
    <!-- SGSN & GGSN Boxes -->
    <rect x="60" y="140" width="160" height="90" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="2" rx="8"/>
    <text x="140" y="170" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle">SGSN</text>
    <text x="140" y="195" fill="#cbd5e1" font-size="12" text-anchor="middle">Generates S-CDRs</text>
    <text x="140" y="215" fill="#94a3b8" font-size="10" text-anchor="middle">(Radio &amp; Location Usage)</text>

    <rect x="60" y="260" width="160" height="90" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="140" y="290" fill="#34d399" font-size="15" font-weight="700" text-anchor="middle">GGSN</text>
    <text x="140" y="315" fill="#cbd5e1" font-size="12" text-anchor="middle">Generates G-CDRs</text>
    <text x="140" y="335" fill="#94a3b8" font-size="10" text-anchor="middle">(External IP Data Volume)</text>

    <!-- Arrows to CGF -->
    <path d="M 220 185 L 340 225" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <path d="M 220 305 L 340 265" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <text x="280" y="200" fill="#38bdf8" font-size="10">Ga Protocol</text>
    <text x="280" y="290" fill="#34d399" font-size="10">Ga Protocol</text>

    <!-- CGF Box -->
    <rect x="350" y="160" width="230" height="160" fill="url(#boxGrad)" stroke="#fbbf24" stroke-width="2" rx="10"/>
    <text x="465" y="195" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">Charging Gateway (CGF)</text>
    <text x="465" y="225" fill="#f1f5f9" font-size="12" text-anchor="middle">• CDR Aggregation &amp; Filtering</text>
    <text x="465" y="250" fill="#f1f5f9" font-size="12" text-anchor="middle">• Duplicate CDR Elimination</text>
    <text x="465" y="275" fill="#f1f5f9" font-size="12" text-anchor="middle">• Format Validation &amp; Buffering</text>
    <text x="465" y="300" fill="#34d399" font-size="11" text-anchor="middle">Secure GTP' / FTAM Transfer</text>

    <!-- Arrow to Billing System -->
    <path d="M 580 240 L 660 240" stroke="#fbbf24" stroke-width="3" marker-end="url(#arrow)"/>
    <text x="620" y="230" fill="#fbbf24" font-size="11">Bx Interface</text>

    <!-- Billing System -->
    <rect x="670" y="140" width="240" height="210" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="790" y="170" fill="#c084fc" font-size="15" font-weight="700" text-anchor="middle">Billing &amp; Mediation System</text>
    <rect x="690" y="190" width="200" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="790" y="215" fill="#f1f5f9" font-size="11" text-anchor="middle">Prepaid Rating (Online / CAMEL)</text>
    <rect x="690" y="240" width="200" height="40" fill="#0b111e" stroke="#a855f7" rx="4"/>
    <text x="790" y="265" fill="#f1f5f9" font-size="11" text-anchor="middle">Postpaid Invoicing (Offline)</text>
    <text x="790" y="310" fill="#cbd5e1" font-size="11" text-anchor="middle">Charging Parameters:</text>
    <text x="790" y="330" fill="#34d399" font-size="11" text-anchor="middle">Volume (MB) + Duration + APN + QoS</text>
    """,
    "Charging Differentiation: Volume-based charging revolutionized data pricing by charging users only for bytes transferred, not connection time"
)

# 16. mobile-q21: sms_architecture_delivery.png
create_card_diagram(
    "images/mobile_compute/sms_architecture_delivery.png",
    "Comprehensive SMS Network Architecture and Delivery (SM-MT &amp; SM-MO)",
    "Short Message Service Center (SMSC), SMS-Gateway MSC (SMS-GMSC), SMPP Protocol, and Location-Based SMS",
    "#10b981", "MOBILE • MOD 2",
    """
    <!-- ESME / App Server -->
    <rect x="50" y="175" width="120" height="70" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="110" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">External App</text>
    <text x="110" y="222" fill="#cbd5e1" font-size="10" text-anchor="middle">(Bank/OTP Server)</text>
    <path d="M 170 210 L 230 210" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="200" y="200" fill="#38bdf8" font-size="10">SMPP</text>

    <!-- SMSC -->
    <rect x="240" y="155" width="130" height="110" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="305" y="185" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">SMSC</text>
    <text x="305" y="208" fill="#f1f5f9" font-size="11" text-anchor="middle">Store &amp; Forward</text>
    <text x="305" y="230" fill="#fbbf24" font-size="10" text-anchor="middle">Validity Period Timer</text>
    <text x="305" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">Message Buffer</text>

    <!-- SMS-GMSC -->
    <path d="M 370 210 L 430 210" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>
    <rect x="440" y="175" width="120" height="70" fill="url(#boxGrad)" stroke="#fbbf24" rx="6"/>
    <text x="500" y="202" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">SMS-GMSC</text>
    <text x="500" y="222" fill="#cbd5e1" font-size="10" text-anchor="middle">Interrogates HLR</text>

    <!-- HLR Query -->
    <path d="M 500 175 L 500 135 L 610 135" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#arrow)"/>
    <rect x="620" y="115" width="100" height="40" fill="#0b111e" stroke="#fbbf24" rx="4"/>
    <text x="670" y="140" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">HLR</text>

    <!-- MSC / VLR -->
    <path d="M 560 210 L 620 210" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)"/>
    <rect x="630" y="175" width="110" height="70" fill="url(#boxGrad)" stroke="#a855f7" rx="6"/>
    <text x="685" y="202" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle">Serving MSC</text>
    <text x="685" y="222" fill="#cbd5e1" font-size="10" text-anchor="middle">&amp; VLR</text>

    <!-- Target MS -->
    <path d="M 740 210 L 800 210" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>
    <rect x="810" y="175" width="100" height="70" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="860" y="202" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Mobile (MS)</text>
    <text x="860" y="222" fill="#34d399" font-size="10" text-anchor="middle">SM-MT ACK</text>

    <!-- Bottom LBS panel -->
    <rect x="50" y="295" width="860" height="85" fill="#0b111e" stroke="#10b981" rx="8"/>
    <text x="480" y="320" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Location-Based Applications via SMS (LBS)</text>
    <text x="480" y="342" fill="#cbd5e1" font-size="11" text-anchor="middle">Serving Cell-ID and Timing Advance (TA) provide instantaneous location without GPS; SMSC triggers local alerts</text>
    <text x="480" y="362" fill="#fbbf24" font-size="11" text-anchor="middle">Applications: Emergency disaster broadcast, fleet telematics tracking, geo-targeted localized retail marketing</text>
    """,
    "Short Message Peer-to-Peer (SMPP): Standard TCP/IP protocol enabling external application servers (ESME) to inject bulk SMS directly into SMSC"
)

# 17. mobile-q23: gprs_qos_parameters.png
create_card_diagram(
    "images/mobile_compute/gprs_qos_parameters.png",
    "Quality of Service (QoS) Profile Parameters in GPRS",
    "Standardized 3GPP QoS Classes: Precedence, Reliability, Delay, Peak Throughput, and Mean Throughput",
    "#10b981", "MOBILE • MOD 3",
    """
    <rect x="50" y="115" width="165" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="132" y="145" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">1. Precedence</text>
    <text x="132" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">Priority in Congestion</text>
    <text x="132" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">• High Priority</text>
    <text x="132" y="240" fill="#cbd5e1" font-size="10" text-anchor="middle">• Normal Priority</text>
    <text x="132" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle">• Low Priority</text>
    <text x="132" y="310" fill="#f87171" font-size="10" text-anchor="middle">Low precedence packets</text>
    <text x="132" y="330" fill="#f87171" font-size="10" text-anchor="middle">are dropped first</text>

    <rect x="225" y="115" width="165" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="307" y="145" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">2. Reliability</text>
    <text x="307" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">Residual Error Rate</text>
    <text x="307" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 1 (GTP, LLC,</text>
    <text x="307" y="235" fill="#cbd5e1" font-size="10" text-anchor="middle">RLC all ACK mode)</text>
    <text x="307" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 2 (RLC ACK)</text>
    <text x="307" y="295" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 3 (Unack data)</text>
    <text x="307" y="335" fill="#38bdf8" font-size="10" text-anchor="middle">Critical for billing</text>

    <rect x="400" y="115" width="165" height="260" fill="url(#boxGrad)" stroke="#fbbf24" stroke-width="1.5" rx="8"/>
    <text x="482" y="145" fill="#fbbf24" font-size="13" font-weight="700" text-anchor="middle">3. Delay Class</text>
    <text x="482" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">End-to-End Latency</text>
    <text x="482" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 1: &lt; 0.5 s (128B)</text>
    <text x="482" y="240" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 2: &lt; 5 s</text>
    <text x="482" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 3: &lt; 50 s</text>
    <text x="482" y="290" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 4: Best Effort</text>
    <text x="482" y="335" fill="#fbbf24" font-size="10" text-anchor="middle">Voice vs Background</text>

    <rect x="575" y="115" width="165" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="657" y="145" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">4. Peak Rate</text>
    <text x="657" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">Max Data Burst Speed</text>
    <text x="657" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 1: Up to 8 kbps</text>
    <text x="657" y="240" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 4: Up to 64 kbps</text>
    <text x="657" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 9: Up to 2 Mbps</text>
    <text x="657" y="310" fill="#34d399" font-size="10" text-anchor="middle">Protects radio link</text>
    <text x="657" y="330" fill="#34d399" font-size="10" text-anchor="middle">from buffer overflow</text>

    <rect x="750" y="115" width="160" height="260" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="830" y="145" fill="#c084fc" font-size="13" font-weight="700" text-anchor="middle">5. Mean Rate</text>
    <text x="830" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">Average Throughput</text>
    <text x="830" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">• 19 discrete steps</text>
    <text x="830" y="240" fill="#cbd5e1" font-size="10" text-anchor="middle">• 0.22 bps to 111 kB/h</text>
    <text x="830" y="265" fill="#cbd5e1" font-size="10" text-anchor="middle">• Class 31: Best Effort</text>
    <text x="830" y="310" fill="#c084fc" font-size="10" text-anchor="middle">Used for SLA contracts</text>
    <text x="830" y="330" fill="#c084fc" font-size="10" text-anchor="middle">&amp; long-term billing</text>
    """,
    "PDP Context Activation: Mobile requests desired QoS profile; SGSN/GGSN negotiate and grant subscribed QoS based on network load"
)

# 18. mobile-q24: wlan_infrastructure_adhoc.png
create_card_diagram(
    "images/mobile_compute/wlan_infrastructure_adhoc.png",
    "IEEE 802.11 WLAN Architecture: Infrastructure BSS vs Ad-Hoc IBSS",
    "Centralized Access Point Distribution System (DS) vs Peer-to-Peer Decentralized Ad-Hoc Independent BSS",
    "#10b981", "MOBILE • MOD 4",
    """
    <!-- Infrastructure Mode BSS -->
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Infrastructure Mode (BSS / ESS)</text>
    
    <!-- Central Access Point -->
    <rect x="205" y="170" width="100" height="50" fill="#0b111e" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="255" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Access Point</text>
    <text x="255" y="210" fill="#cbd5e1" font-size="10" text-anchor="middle">(AP / Router)</text>

    <!-- Distribution System to Ethernet -->
    <path d="M 255 170 L 255 145" stroke="#38bdf8" stroke-width="2"/>
    <text x="255" y="138" fill="#94a3b8" font-size="10" text-anchor="middle">Distribution System (DS)</text>

    <!-- Mobile Stations -->
    <circle cx="120" cy="280" r="22" fill="#0b111e" stroke="#10b981" stroke-width="2"/>
    <text x="120" y="285" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">STA 1</text>

    <circle cx="255" cy="290" r="22" fill="#0b111e" stroke="#10b981" stroke-width="2"/>
    <text x="255" y="295" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">STA 2</text>

    <circle cx="390" cy="280" r="22" fill="#0b111e" stroke="#10b981" stroke-width="2"/>
    <text x="390" y="285" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">STA 3</text>

    <!-- Star Topology Links -->
    <path d="M 135 265 L 210 215" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 255 268 L 255 220" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 375 265 L 300 215" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="255" y="340" fill="#cbd5e1" font-size="11" text-anchor="middle">All traffic relays through AP; client-to-client direct TX blocked</text>
    <text x="255" y="360" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">Seamless bridging to corporate LAN &amp; Internet</text>

    <!-- Ad-Hoc Mode IBSS -->
    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#fbbf24" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#fbbf24" font-size="16" font-weight="700" text-anchor="middle">2. Ad-Hoc Mode (IBSS Peer-to-Peer)</text>
    
    <!-- 3 Peer Stations in Mesh -->
    <circle cx="580" cy="210" r="24" fill="#0b111e" stroke="#fbbf24" stroke-width="2"/>
    <text x="580" y="215" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Node A</text>

    <circle cx="830" cy="210" r="24" fill="#0b111e" stroke="#fbbf24" stroke-width="2"/>
    <text x="830" y="215" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Node B</text>

    <circle cx="705" cy="300" r="24" fill="#0b111e" stroke="#fbbf24" stroke-width="2"/>
    <text x="705" y="305" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Node C</text>

    <!-- Direct Mesh Links -->
    <path d="M 605 210 L 805 210" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 595 230 L 685 285" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 815 230 L 725 285" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>

    <text x="705" y="180" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Zero Central Infrastructure</text>
    <text x="705" y="340" fill="#cbd5e1" font-size="11" text-anchor="middle">Direct station-to-station communication without Access Point</text>
    <text x="705" y="360" fill="#fbbf24" font-size="11" font-weight="600" text-anchor="middle">Quick temporary setups, disaster recovery &amp; Wi-Fi Direct</text>
    """,
    "Extended Service Set (ESS): Multiple APs connected via Distribution System (DS) share same SSID to allow seamless campus-wide Wi-Fi roaming"
)

# 19. mobile-q26: wifi_vs_3g.png
create_card_diagram(
    "images/mobile_compute/wifi_vs_3g.png",
    "Comparative Technical Analysis: Wi-Fi (802.11) vs 3G / Cellular Networks",
    "Coverage Radius, Licensed vs Unlicensed Spectrum, Data Throughput, Mobility Handling, and Cost Structures",
    "#10b981", "MOBILE • MOD 4",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">Wi-Fi (IEEE 802.11 a/b/g/n/ac/ax)</text>
    
    <text x="70" y="180" fill="#38bdf8" font-size="12" font-weight="700">• Spectrum:</text>
    <text x="160" y="180" fill="#cbd5e1" font-size="12">Unlicensed ISM bands (2.4 GHz, 5 GHz, 6 GHz)</text>

    <text x="70" y="210" fill="#38bdf8" font-size="12" font-weight="700">• Coverage:</text>
    <text x="160" y="210" fill="#cbd5e1" font-size="12">Short range: 30 to 100 meters (Indoor hotspot)</text>

    <text x="70" y="240" fill="#38bdf8" font-size="12" font-weight="700">• Throughput:</text>
    <text x="160" y="240" fill="#34d399" font-size="12" font-weight="700">Very High (54 Mbps to 9.6 Gbps)</text>

    <text x="70" y="270" fill="#38bdf8" font-size="12" font-weight="700">• Mobility:</text>
    <text x="160" y="270" fill="#f87171" font-size="12">Low (Pedestrian speeds &lt; 10 km/h)</text>

    <text x="70" y="300" fill="#38bdf8" font-size="12" font-weight="700">• MAC Protocol:</text>
    <text x="175" y="300" fill="#cbd5e1" font-size="12">CSMA/CA (Contention-based collision avoidance)</text>

    <text x="70" y="330" fill="#38bdf8" font-size="12" font-weight="700">• Deployment:</text>
    <text x="175" y="330" fill="#fbbf24" font-size="12">Inexpensive commercial off-the-shelf APs</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">3G / Cellular (UMTS / WCDMA)</text>
    
    <text x="520" y="180" fill="#34d399" font-size="12" font-weight="700">• Spectrum:</text>
    <text x="610" y="180" fill="#cbd5e1" font-size="12">Licensed telecom bands (900, 1800, 2100 MHz)</text>

    <text x="520" y="210" fill="#34d399" font-size="12" font-weight="700">• Coverage:</text>
    <text x="610" y="210" fill="#cbd5e1" font-size="12">Wide area: 2 to 15 km cell radius</text>

    <text x="520" y="240" fill="#34d399" font-size="12" font-weight="700">• Throughput:</text>
    <text x="610" y="240" fill="#fbbf24" font-size="12">Moderate (384 kbps to 42 Mbps with HSPA+)</text>

    <text x="520" y="270" fill="#34d399" font-size="12" font-weight="700">• Mobility:</text>
    <text x="610" y="270" fill="#34d399" font-size="12" font-weight="700">High (Full support up to 250+ km/h in cars/trains)</text>

    <text x="520" y="300" fill="#34d399" font-size="12" font-weight="700">• MAC Protocol:</text>
    <text x="625" y="300" fill="#cbd5e1" font-size="12">CDMA / WCDMA (Orthogonal spreading codes)</text>

    <text x="520" y="330" fill="#34d399" font-size="12" font-weight="700">• Deployment:</text>
    <text x="625" y="330" fill="#cbd5e1" font-size="12">Billion-dollar licensed telecom infrastructure</text>
    """,
    "Complementary Coexistence: Modern smartphones use Wi-Fi Offloading to relieve cellular network congestion in home and office environments"
)

# 20. mobile-q29: wlan_security_evolution.png
create_card_diagram(
    "images/mobile_compute/wlan_security_evolution.png",
    "Evolution of WLAN Security: WEP Vulnerabilities to WPA3 SAE",
    "Cryptographic Progression: WEP (RC4+24b IV) → WPA (TKIP) → WPA2 (802.11i AES-CCMP) → WPA3 (Simultaneous Authentication of Equals)",
    "#10b981", "MOBILE • MOD 4",
    """
    <rect x="50" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="150" y="145" fill="#f87171" font-size="14" font-weight="700" text-anchor="middle">1. WEP (1997)</text>
    <text x="150" y="175" fill="#f87171" font-size="11" font-weight="600" text-anchor="middle">BROKEN &amp; OBSOLETE</text>
    <text x="150" y="205" fill="#cbd5e1" font-size="10" text-anchor="middle">RC4 stream cipher</text>
    <text x="150" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">Short 24-bit IV reuse</text>
    <text x="150" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">Weak CRC-32 integrity</text>
    <text x="150" y="280" fill="#ef4444" font-size="11" text-anchor="middle">FMS &amp; KoreK attacks</text>
    <text x="150" y="300" fill="#ef4444" font-size="11" text-anchor="middle">Crackable in &lt;60 seconds</text>
    <text x="150" y="340" fill="#94a3b8" font-size="10" text-anchor="middle">Shared static key</text>

    <rect x="270" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="370" y="145" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">2. WPA (2003)</text>
    <text x="370" y="175" fill="#fbbf24" font-size="11" font-weight="600" text-anchor="middle">INTERIM TRANSITION</text>
    <text x="370" y="205" fill="#cbd5e1" font-size="10" text-anchor="middle">TKIP wrapper on RC4</text>
    <text x="370" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">Extended 48-bit IV</text>
    <text x="370" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">Per-packet key mixing</text>
    <text x="370" y="275" fill="#cbd5e1" font-size="10" text-anchor="middle">Michael MIC integrity</text>
    <text x="370" y="305" fill="#fbbf24" font-size="11" text-anchor="middle">Fixes WEP IV collision</text>
    <text x="370" y="340" fill="#94a3b8" font-size="10" text-anchor="middle">Vulnerable to Beck-Tews</text>

    <rect x="490" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="590" y="145" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">3. WPA2 (2004)</text>
    <text x="590" y="175" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">IEEE 802.11i ROBUST</text>
    <text x="590" y="205" fill="#cbd5e1" font-size="10" text-anchor="middle">AES-128 bit block cipher</text>
    <text x="590" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">CCMP mode encryption</text>
    <text x="590" y="250" fill="#cbd5e1" font-size="10" text-anchor="middle">CBC-MAC message integrity</text>
    <text x="590" y="275" fill="#34d399" font-size="11" text-anchor="middle">Enterprise 802.1X/EAP</text>
    <text x="590" y="305" fill="#cbd5e1" font-size="10" text-anchor="middle">4-way handshake</text>
    <text x="590" y="340" fill="#fbbf24" font-size="10" text-anchor="middle">Vulnerable to KRACK attack</text>

    <rect x="710" y="115" width="200" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="810" y="145" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">4. WPA3 (2018)</text>
    <text x="810" y="175" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">STATE-OF-THE-ART</text>
    <text x="810" y="205" fill="#cbd5e1" font-size="10" text-anchor="middle">SAE (Dragonfly handshake)</text>
    <text x="810" y="225" fill="#34d399" font-size="11" text-anchor="middle">Zero offline dictionary</text>
    <text x="810" y="245" fill="#34d399" font-size="11" text-anchor="middle">Forward secrecy</text>
    <text x="810" y="275" fill="#cbd5e1" font-size="10" text-anchor="middle">Protected Mgmt Frames</text>
    <text x="810" y="305" fill="#34d399" font-size="11" text-anchor="middle">192-bit CNSA security</text>
    <text x="810" y="340" fill="#34d399" font-size="10" text-anchor="middle">Opportunistic Wireless (OWE)</text>
    """,
    "Simultaneous Authentication of Equals (SAE): Eliminates password dictionary cracking by enforcing Diffie-Hellman zero-knowledge handshake"
)

# 21. mobile-q30: hiperlan_architecture.png
create_card_diagram(
    "images/mobile_compute/hiperlan_architecture.png",
    "HIPERLAN Communication Models and MAC: HIPERLAN 1 vs HIPERLAN 2",
    "ETSI European Standards: EY-NPMA Contention MAC (HIPERLAN 1) vs Dynamic TDMA/TDD Scheduled Framing (HIPERLAN 2)",
    "#10b981", "MOBILE • MOD 4",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">HIPERLAN Type 1 (Ad-Hoc Focus)</text>
    
    <rect x="80" y="170" width="350" height="50" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="255" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">MAC: EY-NPMA Protocol</text>
    <text x="255" y="212" fill="#cbd5e1" font-size="11" text-anchor="middle">(Elimination-Yield Non-Preemptive Priority)</text>

    <text x="70" y="245" fill="#cbd5e1" font-size="12">✔ 5 GHz band, up to 23.5 Mbps raw data rate</text>
    <text x="70" y="270" fill="#cbd5e1" font-size="12">✔ Prioritized channel access: 5 distinct priority levels</text>
    <text x="70" y="295" fill="#cbd5e1" font-size="12">✔ Elimination phase uses active radio bursts to eliminate peers</text>
    <text x="70" y="320" fill="#cbd5e1" font-size="12">✔ Supports multi-hop routing and ad-hoc mesh topologies</text>
    <text x="70" y="348" fill="#fbbf24" font-size="11">Connectionless best-effort with QoS prioritization</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">HIPERLAN Type 2 (Cellular-Like AP)</text>
    
    <rect x="530" y="170" width="350" height="50" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">MAC: Centralized Dynamic TDMA / TDD</text>
    <text x="705" y="212" fill="#cbd5e1" font-size="11" text-anchor="middle">(Fixed 2 ms MAC Frame with Dedicated Time Slots)</text>

    <text x="520" y="245" fill="#cbd5e1" font-size="12">✔ 5 GHz band, up to 54 Mbps using OFDM (like 802.11a)</text>
    <text x="520" y="270" fill="#cbd5e1" font-size="12">✔ Connection-oriented: AP assigns uplink/downlink time slots</text>
    <text x="520" y="295" fill="#cbd5e1" font-size="12">✔ Strict ATM-like QoS guarantees for real-time voice &amp; video</text>
    <text x="520" y="320" fill="#cbd5e1" font-size="12">✔ Dynamic frequency selection (DFS) &amp; transmit power control</text>
    <text x="520" y="348" fill="#34d399" font-size="11">Designed as high-speed wireless extension for ATM and 3G cores</text>
    """,
    "EY-NPMA Mechanics: Prioritization Phase → Contention (Elimination Burst + Yield Listening) → Transmission Phase"
)

# 22. mobile-q31: information_security_components.png
create_card_diagram(
    "images/mobile_compute/information_security_components.png",
    "Foundational Components of Information Security in Mobile Computing",
    "The Extended Security Hexad: Confidentiality, Integrity, Availability, Authenticity, Non-Repudiation, and Authorization",
    "#10b981", "MOBILE • MOD 5",
    """
    <!-- 6 Hexad Cards -->
    <rect x="50" y="115" width="260" height="115" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="8"/>
    <text x="75" y="142" fill="#38bdf8" font-size="14" font-weight="700">1. Confidentiality</text>
    <text x="75" y="168" fill="#cbd5e1" font-size="11">• Protects data from eavesdropping</text>
    <text x="75" y="188" fill="#cbd5e1" font-size="11">• Symmetric encryption (AES-256)</text>
    <text x="75" y="212" fill="#34d399" font-size="11">Air interface scrambling (A5/1, CCMP)</text>

    <rect x="350" y="115" width="260" height="115" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="8"/>
    <text x="375" y="142" fill="#34d399" font-size="14" font-weight="700">2. Integrity</text>
    <text x="375" y="168" fill="#cbd5e1" font-size="11">• Prevents undetected tampering</text>
    <text x="375" y="188" fill="#cbd5e1" font-size="11">• Cryptographic hashes (SHA-256)</text>
    <text x="375" y="212" fill="#38bdf8" font-size="11">HMAC signatures &amp; CRC check</text>

    <rect x="650" y="115" width="260" height="115" fill="url(#boxGrad)" stroke="#fbbf24" stroke-width="1.5" rx="8"/>
    <text x="675" y="142" fill="#fbbf24" font-size="14" font-weight="700">3. Availability</text>
    <text x="675" y="168" fill="#cbd5e1" font-size="11">• Ensures services remain operational</text>
    <text x="675" y="188" fill="#cbd5e1" font-size="11">• Mitigates Jamming &amp; DDoS</text>
    <text x="675" y="212" fill="#fbbf24" font-size="11">Redundant cell carriers &amp; CDNs</text>

    <rect x="50" y="255" width="260" height="115" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="1.5" rx="8"/>
    <text x="75" y="282" fill="#c084fc" font-size="14" font-weight="700">4. Authenticity</text>
    <text x="75" y="308" fill="#cbd5e1" font-size="11">• Verifies identity of communicating parties</text>
    <text x="75" y="328" fill="#cbd5e1" font-size="11">• Mutual authentication (AKA in 3G/4G/5G)</text>
    <text x="75" y="352" fill="#c084fc" font-size="11">Digital X.509 certificates</text>

    <rect x="350" y="255" width="260" height="115" fill="url(#boxGrad)" stroke="#f59e0b" stroke-width="1.5" rx="8"/>
    <text x="375" y="282" fill="#fbbf24" font-size="14" font-weight="700">5. Non-Repudiation</text>
    <text x="375" y="308" fill="#cbd5e1" font-size="11">• Prevents sender from denying action</text>
    <text x="375" y="328" fill="#cbd5e1" font-size="11">• Asymmetric digital signatures (RSA/ECDSA)</text>
    <text x="375" y="352" fill="#34d399" font-size="11">Immutable cryptographic audit trail</text>

    <rect x="650" y="255" width="260" height="115" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="8"/>
    <text x="675" y="282" fill="#f87171" font-size="14" font-weight="700">6. Authorization</text>
    <text x="675" y="308" fill="#cbd5e1" font-size="11">• Granular permission enforcement</text>
    <text x="675" y="328" fill="#cbd5e1" font-size="11">• OAuth 2.0 tokens &amp; RBAC policies</text>
    <text x="675" y="352" fill="#f87171" font-size="11">Principle of least privilege</text>
    """,
    "Defense-in-Depth: Mobile security binds cryptographic primitives at physical, link, network, transport, and application layers"
)

# 23. mobile-q32: static_vs_dynamic_attacks.png
create_card_diagram(
    "images/mobile_compute/static_vs_dynamic_attacks.png",
    "Classification of Security Attacks in Mobile Computing: Static vs Dynamic",
    "Passive Data Interception (Eavesdropping, Traffic Analysis) vs Active System Mutation (Spoofing, Replay, Man-in-the-Middle)",
    "#10b981", "MOBILE • MOD 5",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Static (Passive) Security Attacks</text>
    
    <rect x="80" y="170" width="350" height="40" fill="#0b111e" stroke="#38bdf8" rx="6"/>
    <text x="255" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Air-Interface Eavesdropping (Sniffing)</text>

    <text x="70" y="235" fill="#cbd5e1" font-size="12">• Objective: Intercept and inspect confidential information</text>
    <text x="70" y="260" fill="#cbd5e1" font-size="12">• System state is UNMODIFIED (attacker remains silent/invisible)</text>
    <text x="70" y="285" fill="#cbd5e1" font-size="12">• Traffic Analysis: Inspects packet timing, bursts, and IP headers</text>
    <text x="70" y="310" fill="#cbd5e1" font-size="12">• Location Tracking: Intercepting IMSI or cell identity over radio</text>
    <text x="255" y="348" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Defense: Strong End-to-End Encryption (AES/TLS)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#ef4444" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#f87171" font-size="16" font-weight="700" text-anchor="middle">2. Dynamic (Active) Security Attacks</text>
    
    <rect x="530" y="170" width="350" height="40" fill="#0b111e" stroke="#ef4444" rx="6"/>
    <text x="705" y="195" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle">Man-in-the-Middle (MITM) &amp; Modification</text>

    <text x="520" y="235" fill="#cbd5e1" font-size="12">• Objective: Alter, inject, delay, or destroy network traffic</text>
    <text x="520" y="260" fill="#cbd5e1" font-size="12">• Rogue BTS / IMSI Catchers: Impersonating legitimate cell tower</text>
    <text x="520" y="285" fill="#cbd5e1" font-size="12">• Message Replay Attacks: Re-transmitting authenticated tokens</text>
    <text x="520" y="310" fill="#cbd5e1" font-size="12">• Radio Jamming: Flooding 2.4/5GHz spectrum with RF noise (DoS)</text>
    <text x="705" y="348" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Defense: Mutual Auth, HMACs, Nonces &amp; Spread Spectrum</text>
    """,
    "Fundamental Distinction: Static attacks violate Confidentiality without detection; Dynamic attacks violate Integrity and Availability"
)

# 24. mobile-q33: ssl_tls_mobile_vpn.png
create_card_diagram(
    "images/mobile_compute/ssl_tls_mobile_vpn.png",
    "Security Protocols in Mobile Networks: TLS Handshake and Mobile VPN",
    "TLS 1.3 Asymmetric Key Exchange &amp; Record Layer vs Mobile VPN (IPsec IKEv2 / MOBIKE IP Invariance)",
    "#10b981", "MOBILE • MOD 5",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. TLS 1.3 Transport Security Handshake</text>
    
    <path d="M 90 185 L 390 185" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
    <text x="240" y="175" fill="#38bdf8" font-size="11">ClientHello (Supported Ciphers, KeyShare ECDHE)</text>

    <path d="M 390 225 L 90 225" stroke="#10b981" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="240" y="215" fill="#34d399" font-size="11">ServerHello, Certificate, Finished (1-RTT Key)</text>

    <rect x="80" y="255" width="350" height="50" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="255" y="278" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">Encrypted Application Data Flow</text>
    <text x="255" y="295" fill="#cbd5e1" font-size="11" text-anchor="middle">AES-GCM-256 Symmetric Stream with Zero-RTT resumption</text>

    <text x="255" y="340" fill="#cbd5e1" font-size="11" text-anchor="middle">Operates at Transport/Session Layer (Secures HTTP/HTTPS)</text>
    <text x="255" y="360" fill="#fbbf24" font-size="11" text-anchor="middle">Does not survive client IP changes (Socket breaks on handover)</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Mobile Virtual Private Network (MOBIKE)</text>
    
    <rect x="530" y="170" width="350" height="50" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="705" y="195" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle">IPsec Tunnel Mode + IKEv2 / MOBIKE</text>
    <text x="705" y="212" fill="#cbd5e1" font-size="11" text-anchor="middle">(RFC 4555 IKEv2 Mobility and Multihoming)</text>

    <text x="520" y="245" fill="#cbd5e1" font-size="12">✔ Encapsulates entire IP packet (ESP Header + Payload)</text>
    <text x="520" y="270" fill="#34d399" font-size="12" font-weight="600">✔ IP Invariance: Outer IP changes, Inner tunnel IP persists</text>
    <text x="520" y="295" fill="#cbd5e1" font-size="12">✔ Seamless Wi-Fi to 5G Cellular handovers without dropped VPN</text>
    <text x="520" y="320" fill="#cbd5e1" font-size="12">✔ Enterprise intranet assets remain transparently accessible</text>
    <text x="705" y="355" fill="#fbbf24" font-size="11" text-anchor="middle">Ideal for enterprise security, remote access, and medical telemetry</text>
    """,
    "MOBIKE Protocol: Allows mobile client to inform IPsec VPN gateway of its new IP address without re-establishing Security Associations (SA)"
)

# 25. mobile-q34: rsa_cryptosystem_derivation.png
create_card_diagram(
    "images/mobile_compute/rsa_cryptosystem_derivation.png",
    "Public Key Cryptography: Step-by-Step Numerical RSA Cryptosystem",
    "Complete Calculation: Primes (p=11, q=13), Modulus n=143, φ(n)=120, Keys (e=7, d=103), Encryption &amp; Decryption of M=9",
    "#10b981", "MOBILE • MOD 5",
    """
    <rect x="50" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#38bdf8" stroke-width="1.5" rx="10"/>
    <text x="255" y="145" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle">1. Key Generation Procedure</text>
    
    <text x="70" y="180" fill="#f1f5f9" font-size="12">1. Choose Primes:</text>
    <text x="210" y="180" fill="#38bdf8" font-size="12" font-weight="700">p = 11,  q = 13</text>

    <text x="70" y="210" fill="#f1f5f9" font-size="12">2. Compute Modulus:</text>
    <text x="210" y="210" fill="#34d399" font-size="12" font-weight="700">n = p · q = 11 × 13 = 143</text>

    <text x="70" y="240" fill="#f1f5f9" font-size="12">3. Euler Totient φ(n):</text>
    <text x="210" y="240" fill="#fbbf24" font-size="12" font-weight="700">φ(n) = (11 - 1) × (13 - 1) = 120</text>

    <text x="70" y="270" fill="#f1f5f9" font-size="12">4. Public Exponent e:</text>
    <text x="210" y="270" fill="#38bdf8" font-size="12" font-weight="700">e = 7  (gcd(7, 120) = 1)</text>

    <text x="70" y="300" fill="#f1f5f9" font-size="12">5. Private Key d:</text>
    <text x="210" y="300" fill="#c084fc" font-size="12" font-weight="700">d ≡ e⁻¹ (mod φ(n)) = 103</text>
    <text x="210" y="320" fill="#94a3b8" font-size="10">(Since 7 × 103 = 721 = 6 × 120 + 1)</text>

    <rect x="70" y="335" width="370" height="30" fill="#0b111e" stroke="#34d399" rx="4"/>
    <text x="255" y="355" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Public: {e=7, n=143} | Private: {d=103, n=143}</text>

    <rect x="500" y="115" width="410" height="260" fill="url(#boxGrad)" stroke="#10b981" stroke-width="1.5" rx="10"/>
    <text x="705" y="145" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle">2. Encryption &amp; Decryption Proof</text>
    
    <rect x="525" y="170" width="360" height="75" fill="#0b111e" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
    <text x="705" y="195" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">Encryption (Plaintext M = 9):</text>
    <text x="705" y="217" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">C = M^e mod n = 9⁷ mod 143 = 48</text>
    <text x="705" y="235" fill="#cbd5e1" font-size="11" text-anchor="middle">(9⁷ = 4,782,969; 4,782,969 = 33,447 × 143 + 48)</text>

    <rect x="525" y="260" width="360" height="75" fill="#0b111e" stroke="#10b981" stroke-width="1.5" rx="6"/>
    <text x="705" y="285" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">Decryption (Ciphertext C = 48):</text>
    <text x="705" y="307" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="middle">M = C^d mod n = 48¹⁰³ mod 143 = 9</text>
    <text x="705" y="325" fill="#cbd5e1" font-size="11" text-anchor="middle">Verified via Square-and-Multiply: Recovers original M = 9</text>

    <text x="705" y="360" fill="#cbd5e1" font-size="11" text-anchor="middle">Security Assumption: Factoring large semi-prime n into p × q is computationally intractable</text>
    """,
    "Modular Exponentiation: C ≡ M^e (mod n) and M ≡ C^d (mod n) relies on Euler's Totient Theorem: M^(φ(n)) ≡ 1 (mod n)"
)

# 26. mobile-q37: mbms_mpls_architecture.png
create_card_diagram(
    "images/mobile_compute/mbms_mpls_architecture.png",
    "Multimedia Broadcast Multicast Service (MBMS) &amp; MPLS in Cellular",
    "Single-Frequency Network Point-to-Multipoint (PTM) Radio Transmission Combined with MPLS Label Switching",
    "#10b981", "MOBILE • MOD 5",
    """
    <!-- Content Source -->
    <rect x="50" y="165" width="130" height="90" fill="url(#boxGrad)" stroke="#38bdf8" rx="8"/>
    <text x="115" y="195" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Content Provider</text>
    <text x="115" y="215" fill="#cbd5e1" font-size="11" text-anchor="middle">Live HD Broadcast</text>
    <text x="115" y="235" fill="#34d399" font-size="10" text-anchor="middle">Single Stream</text>

    <path d="M 180 210 L 240 210" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow)"/>

    <!-- BM-SC & MBMS Gateway -->
    <rect x="250" y="150" width="160" height="120" fill="url(#boxGrad)" stroke="#10b981" stroke-width="2" rx="8"/>
    <text x="330" y="180" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle">BM-SC &amp; MBMS-GW</text>
    <text x="330" y="205" fill="#f1f5f9" font-size="11" text-anchor="middle">Broadcast Multicast</text>
    <text x="330" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">Service Center Core</text>
    <text x="330" y="250" fill="#fbbf24" font-size="10" text-anchor="middle">IP Multicast (M-IP)</text>

    <!-- MPLS Core Network -->
    <path d="M 410 210 L 470 210" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    
    <rect x="480" y="150" width="160" height="120" fill="url(#boxGrad)" stroke="#a855f7" stroke-width="2" rx="8"/>
    <text x="560" y="180" fill="#c084fc" font-size="14" font-weight="700" text-anchor="middle">MPLS Core Transport</text>
    <text x="560" y="205" fill="#f1f5f9" font-size="11" text-anchor="middle">Label Switched Paths</text>
    <text x="560" y="225" fill="#cbd5e1" font-size="10" text-anchor="middle">(LSP 20-bit Header)</text>
    <text x="560" y="250" fill="#34d399" font-size="10" text-anchor="middle">Strict QoS Bandwidth</text>

    <!-- Point to Multipoint Fan-out -->
    <path d="M 640 190 L 710 160" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <path d="M 640 210 L 710 210" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>
    <path d="M 640 230 L 710 260" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>

    <!-- eNodeB / gNB Cells -->
    <rect x="720" y="130" width="180" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="810" y="152" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MBSFN Area (Cell 1)</text>
    <text x="810" y="168" fill="#34d399" font-size="10" text-anchor="middle">Single Radio Carrier (PTM)</text>

    <rect x="720" y="190" width="180" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="810" y="212" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MBSFN Area (Cell 2)</text>
    <text x="810" y="228" fill="#34d399" font-size="10" text-anchor="middle">Thousands of Concurrent Users</text>

    <rect x="720" y="250" width="180" height="50" fill="url(#boxGrad)" stroke="#38bdf8" rx="6"/>
    <text x="810" y="272" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">MBSFN Area (Cell 3)</text>
    <text x="810" y="288" fill="#34d399" font-size="10" text-anchor="middle">Zero Uplink Radio Feedback</text>

    <rect x="50" y="310" width="850" height="65" fill="#0b111e" stroke="#10b981" rx="6"/>
    <text x="475" y="333" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle">Radio Spectral Efficiency: Point-to-Multipoint (PTM) vs Unicast</text>
    <text x="475" y="355" fill="#cbd5e1" font-size="11" text-anchor="middle">Instead of transmitting N separate unicast streams to N users, 1 broadcast stream serves all users in the cell simultaneously</text>
    """,
    "MBSFN Synchronization: Base stations transmit time-synchronized identical waveforms; receiver treats multi-cell signals as multipath"
)

print("Finished generating Mobile Computing diagrams.")
