# -*- coding: utf-8 -*-
"""
Content generator for Subject 3: Introduction to Mobile Computing (CST415)
Includes complete KTU CST415 Syllabus breakdown and all 38 university questions.
All answers are elaborated in paragraph format without bullet points.
Constructed with raw strings to eliminate any control character corruption.
"""

from mobile_m1 import MODULE_1
from mobile_m2 import MODULE_2
from mobile_m3 import MODULE_3
from mobile_m4 import MODULE_4
from mobile_m5 import MODULE_5

MOBILE_SYLLABUS = {
    "course_code": "CST415",
    "course_name": "INTRODUCTION TO MOBILE COMPUTING",
    "scheme": "2019 Scheme (APJ Abdul Kalam Technological University)",
    "credits": "3 Credits (L-T-P: 2-1-0)",
    "preamble": """
The primary purpose of this course is to prepare learners to comprehend the foundational functionalities, architectural paradigms, communication mechanisms, and engineering design considerations of modern mobile computing systems. The curriculum spans mobile computing architecture, three-tier enterprise design, cellular and satellite communication technologies, short messaging and packet radio services, wireless local area networks, mobile information security, and next-generation networks including OFDM, 4G LTE, and 5G.
""",
    "modules": [
        {
            "num": "Module 1",
            "title": "Mobile Computing Architecture",
            "contents": "Introduction to mobile computing – Functions, Devices, Middleware and gateways, Applications and services, Limitations. Mobile computing architecture – Internet: The ubiquitous network, Three-tier architecture, Design considerations for mobile computing. Context-aware computing, Client context manager, Policy manager, Security manager, Adaptability manager, Content adaptation and classifications of transcoding, Seamless communication and roaming."
        },
        {
            "num": "Module 2",
            "title": "Communication Systems & Cellular Networks",
            "contents": "Mobile computing through telephony – Evolution of telephony (1G, 2G, 2.5G, 3G, 4G, 5G). Multiple access procedures – Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA), Code Division Multiple Access (CDMA), Space Division Multiple Access (SDMA). Satellite communication systems – Basics, Applications, Geostationary Earth Orbit (GEO), Low Earth Orbit (LEO), Medium Earth Orbit (MEO), Satellite phones. Call progress indication mechanisms in cellular telephony. Mobile computing through telephone – Interactive Voice Response (IVR) architecture, Overview of voice software, Developing an IVR application. Global System for Mobile Communication (GSM) – Introduction, Architecture, Entities, Call routing (MTC, MOC), Mobility management, Handover vs roaming, Frequency allocation, Authentication and security (A3, A5, A8 algorithms)."
        },
        {
            "num": "Module 3",
            "title": "Short Messaging Service (SMS) & General Packet Radio Service (GPRS)",
            "contents": "Short Message Service (SMS) – Strengths, Architecture, Value added services, Accessing the SMS bearer (SM-MO, SM-MT, SMPP), Location-based applications using SMS. General Packet Radio Service (GPRS) – Architecture, SGSN, GGSN, PCU, Network operations, GPRS attach, PDP context activation, Data services, Applications, Limitations, Quality of Service (QoS) parameters, Billing and charging mechanisms."
        },
        {
            "num": "Module 4",
            "title": "Wireless Local Area Networks (WLAN)",
            "contents": "Wireless Local Area Network (WLAN) – Advantages, Evolution, Applications. IEEE 802.11 Architecture – Basic Service Set (BSS), Extended Service Set (ESS), Access Point (AP), Distribution System (DS), Ad-hoc vs Infrastructure mode. MAC Sublayer – CSMA/CA, Hidden terminal problem, Exposed terminal problem, Virtual carrier sensing via RTS/CTS, Interframe spaces (SIFS, PIFS, DIFS, EIFS), Fragmentation and reassembly. Mobility management in WLAN. High Performance Radio LAN (HIPERLAN 1 & 2). Wi-Fi vs 3G/Cellular. Wireless Local Loop (WLL) Architecture. WLAN Security – WEP vulnerabilities, WPA, WPA2 (802.11i), WPA3."
        },
        {
            "num": "Module 5",
            "title": "Mobile Security and Next Generation Networks",
            "contents": "Information security components – Extended CIA triad, Authenticity, Non-repudiation, Authorization. Attack classifications – Static vs Dynamic attacks on assets. Security protocols – Transport Layer Security (TLS), Secure Sockets Layer (SSL), Mobile VPN. Cryptography – Public key cryptography principles, Diffie-Hellman key exchange algorithm, RSA cryptosystem with numerical calculations. Next-generation networks – WATM, Mobile IP, WAP, XML, UMTS, Orthogonal Frequency Division Multiplexing (OFDM), Multiprotocol Label Switching (MPLS), Multimedia Broadcast and Multicast Services (MBMS), Network evolution (2G to 5G)."
        }
    ]
}

MOBILE_MODULES = [
    MODULE_1,
    MODULE_2,
    MODULE_3,
    MODULE_4,
    MODULE_5
]
