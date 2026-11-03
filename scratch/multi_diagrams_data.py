# -*- coding: utf-8 -*-
"""
multi_diagrams_data.py
======================
Comprehensive catalog of secondary / supplementary technical diagrams
providing dual-figure and multi-figure coverage for university engineering exam questions.
"""

EXTRA_DIAGRAMS_MAP = {
    # =========================================================================
    # 1. ELECTRIC DRIVES (EET413)
    # =========================================================================
    "drive-q5": [
        {
            "img_path": "images/drive/four_quadrant_hoist_mechanics.png",
            "img_caption": "Figure 1.5B: Physical Hoist Mechanical Assembly showing Cable Drum, Counterweight Wc, Loaded Cage WL, and Gravitational Torque Balance",
            "badge": "Figure B • Mechanical Force Dynamics"
        }
    ],
    "drive-q8": [
        {
            "img_path": "images/drive/single_phase_full_converter_firing_waveforms.png",
            "img_caption": "Figure 2.2B: Supply Voltage vs, Firing Angle α, Output Voltage vo(t), and Continuous Armature Current ia(t) Waveforms",
            "badge": "Figure B • Conduction Waveforms"
        }
    ],
    "drive-q8b": [
        {
            "img_path": "images/drive/three_phase_full_converter_waveforms.png",
            "img_caption": "Figure 2.2C: Six-Pulse Conduction Waveforms, Interlocking Line Voltages, and Thyristor Firing Sequence (T1-T6)",
            "badge": "Figure B • 6-Pulse Commutation Waveforms"
        }
    ],
    "drive-q10": [
        {
            "img_path": "images/drive/class_c_chopper_waveforms.png",
            "img_caption": "Figure 3.2B: Two-Quadrant Class-C Chopper Waveforms for Mode 1 (Motoring: CH1, D2) and Mode 2 (Regenerative Braking: CH2, D1)",
            "badge": "Figure B • Operating Mode Waveforms"
        }
    ],
    "drive-q10b": [
        {
            "img_path": "images/drive/class_e_chopper_modes.png",
            "img_caption": "Figure 3.2C: Four-Quadrant Class-E H-Bridge Chopper Conduction Loops across Motoring and Regenerative Braking Modes",
            "badge": "Figure B • 4-Quadrant Conduction Paths"
        }
    ],
    "drive-q11": [
        {
            "img_path": "images/drive/inner_current_control_loop.png",
            "img_caption": "Figure 3.3B: Fast Subordinate Inner Current Control Loop with Current Limiter Clamp (±Ia,max) and Anti-Windup PI Regulator",
            "badge": "Figure B • Inner Current Loop Detail"
        }
    ],
    "drive-q13": [
        {
            "img_path": "images/drive/v_f_closed_loop_schematic.png",
            "img_caption": "Figure 4.2B: Closed-Loop Constant V/f Induction Motor Drive Architecture with Slip Speed Regulation (ωsl*) and Inverter Control",
            "badge": "Figure B • Closed-Loop Architecture"
        }
    ],
    "drive-q14b": [
        {
            "img_path": "images/drive/kramer_vs_scherbius_characteristics.png",
            "img_caption": "Figure 4.3C: Comparative Slip Power Recovery Topologies: Static Kramer (Sub-synchronous only) vs Static Scherbius (Sub & Super-synchronous)",
            "badge": "Figure B • Power Flow & Operating Zones"
        }
    ],
    "drive-q18": [
        {
            "img_path": "images/drive/clarke_park_transformation_geometry.png",
            "img_caption": "Figure 5.4B: Geometric Vector Transformations from 3-Phase abc Frame to Orthogonal αβ Frame and Synchronous Rotor-Flux dq Frame",
            "badge": "Figure B • Vector Decomposition Geometry"
        }
    ],

    # =========================================================================
    # 2. ADVANCED CONTROL SYSTEMS (EET401)
    # =========================================================================
    "acs-q5": [
        {
            "img_path": "images/acs/series_rlc_state_diagram.png",
            "img_caption": "Figure 1.5B: Analog Simulation State Block Diagram of Series RLC Circuit with Integrators for x1=iL and x2=vC",
            "badge": "Figure B • State Simulation Diagram"
        }
    ],
    "acs-q6": [
        {
            "img_path": "images/acs/armature_dc_motor_block_diagram.png",
            "img_caption": "Figure 1.6B: Comprehensive Electromechanical Transfer Function Block Diagram with Armature Admittance, Torque Constant Kt, and Back-EMF Feedback Kb",
            "badge": "Figure B • Transfer Function Block Diagram"
        }
    ],
    "acs-q7": [
        {
            "img_path": "images/acs/controllable_canonical_form.png",
            "img_caption": "Figure 1.7B: Controllable Canonical Form (CCF) Phase Variable Analog Simulation Diagram with Successive Integrator Chains",
            "badge": "Figure B • Controllable Canonical Realization"
        }
    ],
    "acs-q14": [
        {
            "img_path": "images/acs/pole_placement_s_plane.png",
            "img_caption": "Figure 3.3B: Complex S-Plane Root Migration Diagram showing Open-Loop vs Desired Closed-Loop Pole Relocations within Damping Cone (ζ, ωn)",
            "badge": "Figure B • S-Plane Pole Migration"
        }
    ],
    "acs-q15": [
        {
            "img_path": "images/acs/observer_error_dynamics.png",
            "img_caption": "Figure 3.4B: Full-Order Luenberger Observer Error Dynamics and Asymptotic Convergence e(t) -> 0 governed by Eigenvalues of (A - LC)",
            "badge": "Figure B • Error Dynamics & Convergence"
        }
    ],
    "acs-q16b": [
        {
            "img_path": "images/acs/relay_waveforms_fourier.png",
            "img_caption": "Figure 4.1C: Ideal Relay Input Sinusoid x(t)=X·sin(ωt), Output Square Wave y(t)=±M, and Fundamental Fourier Harmonic Y1(t)",
            "badge": "Figure B • Input-Output Waveforms & Fourier"
        }
    ],
    "acs-q17": [
        {
            "img_path": "images/acs/saturation_waveforms_fourier.png",
            "img_caption": "Figure 4.2B: Symmetrical Saturation Clipped Waveform with Transition Angle θ1 = sin⁻¹(S/X) and Conduction Intervals",
            "badge": "Figure B • Clipped Output Waveform"
        }
    ],
    "acs-q18": [
        {
            "img_path": "images/acs/limit_cycle_stability_criterion.png",
            "img_caption": "Figure 4.3B: Polar Nyquist Plot of Plant G(jω) intersecting Non-Linear Locus -1/N(X) with Loeb's Directional Amplitude Stability Analysis",
            "badge": "Figure B • Perturbation Stability Analysis"
        }
    ],
    "acs-q21": [
        {
            "img_path": "images/acs/isocline_method_construction.png",
            "img_caption": "Figure 5.3B: Method of Isoclines Step-by-Step Construction with Constant Slope Lines M = dx2/dx1 and Directional Slope Tangents",
            "badge": "Figure B • Isocline Construction Method"
        }
    ],

    # =========================================================================
    # 3. MOBILE COMPUTING (CST415)
    # =========================================================================
    "mobile-q10": [
        {
            "img_path": "images/mobile_compute/satellite_footprint_geometry.png",
            "img_caption": "Figure 2.1B: Satellite Geometric Coverage Footprint, Earth Horizon, Slant Range Distance, and Minimum Elevation Angle (θmin >= 10°)",
            "badge": "Figure B • Footprint Geometry & Coverage"
        }
    ],
    "mobile-q14": [
        {
            "img_path": "images/mobile_compute/gsm_channel_hierarchy.png",
            "img_caption": "Figure 2.5B: GSM Logical and Physical Channel Architecture: Traffic Channels (TCH) and Control Channels (BCH, CCCH, DCCH)",
            "badge": "Figure B • Channel Hierarchy & Multiplexing"
        }
    ],
    "mobile-q15": [
        {
            "img_path": "images/mobile_compute/gsm_handover_sequence.png",
            "img_caption": "Figure 2.6B: Inter-BSS Mobile-Assisted Handover (MAHO) Signaling Protocol Ladder between MS, Old BTS, New BTS, BSC, and MSC",
            "badge": "Figure B • Handover Signaling Ladder"
        }
    ],
    "mobile-q17": [
        {
            "img_path": "images/mobile_compute/gsm_auth_cipher_timeline.png",
            "img_caption": "Figure 2.8B: GSM Security Signaling Protocol Timeline: SIM Authentication Challenge-Response (A3) and A5 Stream Cipher Activation",
            "badge": "Figure B • Authentication Protocol Timeline"
        }
    ],
    "mobile-q21": [
        {
            "img_path": "images/mobile_compute/sms_pdu_signaling_flow.png",
            "img_caption": "Figure 3.4B: End-to-End Signaling Sequence Diagrams for Mobile-Originated (SM-MO) and Mobile-Terminated (SM-MT) Message Delivery",
            "badge": "Figure B • SM-MO and SM-MT Signaling Flow"
        }
    ],
    "mobile-q22": [
        {
            "img_path": "images/mobile_compute/gprs_pdp_context_activation.png",
            "img_caption": "Figure 3.5B: Complete PDP Context Activation Signaling Procedure establishing Packet Data Protocol Tunnel from MS to APN / Internet",
            "badge": "Figure B • PDP Context Signaling Procedure"
        }
    ],
    "mobile-q25": [
        {
            "img_path": "images/mobile_compute/csma_ca_backoff_timeline.png",
            "img_caption": "Figure 4.2B: IEEE 802.11 CSMA/CA Exponential Backoff Timing with DIFS Listening, Slot Countdown, and Counter Freezing Mechanism",
            "badge": "Figure B • CSMA/CA Backoff Timeline"
        }
    ],
    "mobile-q27": [
        {
            "img_path": "images/mobile_compute/rts_cts_nav_timing.png",
            "img_caption": "Figure 4.4B: IEEE 802.11 Virtual Carrier Sensing: RTS/CTS Frame Handshake and Network Allocation Vector (NAV) Reservation Timeline",
            "badge": "Figure B • RTS/CTS Virtual Carrier Sensing"
        }
    ],
    "mobile-q34": [
        {
            "img_path": "images/mobile_compute/rsa_encryption_pipeline.png",
            "img_caption": "Figure 5.4B: Complete RSA Public Key Numerical Processing Pipeline with Key Generation (e=3, d=7), Encryption (C=8), and Decryption (M=2)",
            "badge": "Figure B • Step-by-Step Processing Pipeline"
        }
    ],
    "mobile-q35": [
        {
            "img_path": "images/mobile_compute/diffie_hellman_color_mixing_math.png",
            "img_caption": "Figure 5.5B: Diffie-Hellman Key Exchange Discrete Logarithm Math Flow & Color-Mixing Analogy for Asymmetric Shared Key Agreement",
            "badge": "Figure B • Color Mixing & Modulo Math Flow"
        }
    ],
}
