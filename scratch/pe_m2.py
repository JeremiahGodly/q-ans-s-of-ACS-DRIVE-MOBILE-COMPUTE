# -*- coding: utf-8 -*-
"""
Module 2: Controlled Rectifiers (Phase Controlled Converters)
Subject: Power Electronics (EET306) - KTU 2019 Scheme S6 EEE
Questions: pe-q6 to pe-q10
"""

MODULE_2 = {
    "module_id": "pe-m2",
    "module_num": "Module 2",
    "module_title": "Controlled Rectifiers (Phase Controlled Converters)",
    "questions": [
        {
            "qid": "pe-q6",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Single-Phase Half-Wave Controlled Rectifier with R, RL, and RL Load with Freewheeling Diode",
            "yt_query": "single phase half wave controlled rectifier R RL load freewheeling diode derivation",
            "img_path": "images/pe/1ph_halfwave_rectifier.png",
            "img_caption": "Figure 2.1: Circuit Diagrams and Voltage/Current Waveforms for 1-Phase Half-Wave Converter with R, RL, and RL Load with Freewheeling Diode",
            "answer": r"""
The single-phase half-wave controlled converter represents the most fundamental phase-controlled topology, employing a single thyristor in series with an AC voltage source $v_s(t) = V_m \sin\omega t$ and a load.

### 1. Resistive (R) Load
When the load is purely resistive, the thyristor is forward-biased during the positive half-cycle ($0 \le \omega t \le \pi$). When a gate trigger pulse is applied at firing angle $\omega t = \alpha$, the SCR turns on instantly. Conduction ceases naturally at $\omega t = \pi$ when the supply voltage drops to zero and reverses (natural or line commutation).

- **Average Output Voltage ($V_{dc}$):**
$$V_{dc} = \frac{1}{2\pi} \int_\alpha^\pi V_m \sin\omega t\,d(\omega t) = \frac{V_m}{2\pi} [-\cos\omega t]_\alpha^\pi = \frac{V_m}{2\pi} [-\cos\pi - (-\cos\alpha)] = \frac{V_m}{2\pi} (1 + \cos\alpha)$$

- **RMS Output Voltage ($V_{rms}$):**
$$V_{rms} = \sqrt{\frac{1}{2\pi} \int_\alpha^\pi V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{2\pi}} \sqrt{\int_\alpha^\pi \frac{1 - \cos 2\omega t}{2}\,d(\omega t)}$$
$$V_{rms} = \frac{V_m}{2\sqrt{\pi}} \sqrt{\left[ \omega t - \frac{\sin 2\omega t}{2} \right]_\alpha^\pi} = \frac{V_m}{2\sqrt{\pi}} \sqrt{(\pi - \alpha) + \frac{1}{2}\sin 2\alpha}$$

### 2. Inductive ($R-L$) Load without Freewheeling Diode
With an inductive load, when the thyristor is triggered at $\omega t = \alpha$, load current $i_o(t)$ begins to rise. Energy is stored in the magnetic field of the inductor ($E_L = \frac{1}{2} L i^2$).

```
       v_s = V_m sin(wt) ───[ SCR ]───┬────────o +
                                       │
                                      [R]
                                       │       v_o(t)
                                      [L]
                                       │
                         ──────────────┴────────o -
```

The governing differential equation during conduction ($\alpha \le \omega t \le \beta$) is:
$$L \frac{di_o}{dt} + R i_o = V_m \sin\omega t$$

Solving this linear non-homogeneous differential equation, the total current consists of steady-state and transient components:
$$i_o(\omega t) = \frac{V_m}{Z}\sin(\omega t - \phi) + A e^{-\frac{R}{\omega L}\omega t}$$
where $Z = \sqrt{R^2 + (\omega L)^2}$ and $\phi = \tan^{-1}\left(\frac{\omega L}{R}\right)$.

Applying initial boundary condition $i_o(\alpha) = 0$:
$$0 = \frac{V_m}{Z}\sin(\alpha - \phi) + A e^{-\frac{R}{\omega L}\alpha} \implies A = -\frac{V_m}{Z}\sin(\alpha - \phi) e^{\frac{R}{\omega L}\alpha}$$

Substituting constant $A$ back into the current equation:
$$i_o(\omega t) = \frac{V_m}{Z}\left[ \sin(\omega t - \phi) - \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\omega t - \alpha)} \right]$$

- **Extinction Angle ($\beta$):**
At $\omega t = \pi$, the supply voltage reverses, but the current cannot drop instantaneously to zero due to inductive opposition. The collapsing magnetic field self-induces an opposing electromotive force ($v_L = -L \frac{di}{dt}$), maintaining the anode positive relative to the cathode. Conduction continues into the negative half-cycle until all stored magnetic energy is completely dissipated at $\omega t = \beta$ ($\beta > \pi$), termed the **extinction angle**.
At $\omega t = \beta$, $i_o(\beta) = 0$:
$$\sin(\beta - \phi) = \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\beta - \alpha)}$$

- **Average Output Voltage ($V_{dc}$):**
$$V_{dc} = \frac{1}{2\pi} \int_\alpha^\beta V_m \sin\omega t\,d(\omega t) = \frac{V_m}{2\pi} [-\cos\omega t]_\alpha^\beta = \frac{V_m}{2\pi}(\cos\alpha - \cos\beta)$$
Because $\beta > \pi$, the negative voltage excursion between $\pi$ and $\beta$ substantially degrades the net DC average voltage.

### 3. $R-L$ Load with Freewheeling Diode (FD)
To eliminate the undesirable negative voltage loop, a freewheeling diode ($D_{fw}$) is connected in inverse parallel across the $R-L$ load.

```
       v_s ───[ SCR ]───┬───────────────o +
                        │       │
                      ┌─┴─┐    [R]
                      │FD │     │       v_o(t)
                      └─┬─┘    [L]
                        │       │
           ─────────────┴───────┴───────o -
```

- **Operation:**
  1. From $\omega t = \alpha$ to $\pi$: The thyristor conducts, $v_o = v_s$, and the diode is reverse-biased ($v_{FD} = -v_s$).
  2. At $\omega t = \pi$: Supply voltage crosses zero and turns negative. This forward-biases the freewheeling diode, which turns on automatically.
  3. The load voltage is clamped to zero:
  $$v_o(t) = 0 \quad (\pi \le \omega t \le \beta)$$
  4. The thyristor cathode potential becomes higher than its anode, forcing the SCR to turn off by line commutation at $\omega t = \pi$.
  5. The load current now recirculates (freewheels) entirely through the diode and load resistance, governed by:
  $$L \frac{di}{dt} + R i = 0 \implies i_o(t) = I_0 e^{-\frac{R}{L}t}$$

- **Average Output Voltage:**
Since output voltage is positive from $\alpha$ to $\pi$ and identically zero from $\pi$ to $2\pi$:
$$V_{dc} = \frac{1}{2\pi} \int_\alpha^\pi V_m \sin\omega t\,d(\omega t) = \frac{V_m}{2\pi}(1 + \cos\alpha)$$

- **Key Advantages of Freewheeling Diode:**
  1. Prevents negative voltage excursion, substantially increasing average output voltage $V_{dc}$.
  2. Provides an alternate discharge path for inductive energy, smoothing load current and reducing ripple factor.
  3. Relieves the thyristor of reverse-voltage stress during carrier sweep-out.
  4. Improves the input displacement factor and overall power factor of the converter.
"""
        },
        {
            "qid": "pe-q7",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Single-Phase Fully Controlled Bridge Rectifier with RLE Load: Continuous and Discontinuous Conduction Modes",
            "yt_query": "single phase full converter RLE load continuous discontinuous conduction derivation",
            "img_path": "images/pe/1ph_full_converter_rle.png",
            "img_caption": "Figure 2.2: 1-Phase Fully Controlled Converter with RLE Load showing Two-Quadrant (Vdc-Idc) Operation and Inversion",
            "answer": r"""
The single-phase fully controlled bridge rectifier (full converter) consists of four thyristors ($T_1, T_2, T_3, T_4$) in a Graetz bridge configuration feeding an active $R-L-E$ load, representing the armature circuit of a DC motor with back EMF $E$.

```
           ┌──────────┬──────────┐
           │ T1       │ T3       │
      ┌────o─►|─┐   ┌─o─►|─┐     │
      │    │    │   │ │    │     │
   v_s(t)  └────┼───┘ └────┼─────┘
      │         │          │
      └─────────┼──────────┤
           ┌────┴────┐┌────┴────┐
           │ T4      ││ T2      │
           └─►|─o────┘└─►|─o────┘
                │          │
                └────┬─────┘
                     │
                  ┌──┴──┐
                  │ [R] │
                  │ [L] │ v_o(t), i_o(t)
                  │ (E) │
                  └──┬──┘
                     │
```

### 1. Continuous Conduction Mode (CCM) Operation
Under continuous conduction, load inductance $L$ is sufficiently large that load current $i_o(t)$ never decays to zero.
- **Positive Half-Cycle ($\alpha \le \omega t \le \pi + \alpha$):**
  Thyristors $T_1$ and $T_2$ are triggered at $\omega t = \alpha$. They conduct simultaneously, applying AC supply voltage directly to the load:
  $$v_o(t) = v_s(t) = V_m \sin\omega t$$
- **Negative Half-Cycle ($\pi + \alpha \le \omega t \le 2\pi + \alpha$):**
  At $\omega t = \pi + \alpha$, gate firing pulses are applied to $T_3$ and $T_4$. Because supply voltage is negative ($v_s < 0$), firing $T_3$ and $T_4$ applies a reverse anode-to-cathode voltage across $T_1$ and $T_2$, commutating them off by line commutation. Now $T_3$ and $T_4$ connect the negative supply line to the load:
  $$v_o(t) = -v_s(t) = -V_m \sin\omega t$$

### 2. Mathematical Derivation of Average and RMS Output Voltages
Since the output voltage waveform repeats every $\pi$ radians ($180^\circ$ symmetry):
- **Average Output Voltage ($V_{dc}$):**
$$V_{dc} = \frac{1}{\pi} \int_\alpha^{\pi+\alpha} V_m \sin\omega t\,d(\omega t) = \frac{V_m}{\pi} [-\cos\omega t]_\alpha^{\pi+\alpha}$$
$$V_{dc} = \frac{V_m}{\pi} \left[ -\cos(\pi+\alpha) - (-\cos\alpha) \right] = \frac{V_m}{\pi} [\cos\alpha + \cos\alpha] = \frac{2 V_m}{\pi}\cos\alpha$$

- **RMS Output Voltage ($V_{rms}$):**
$$V_{rms} = \sqrt{\frac{1}{\pi} \int_\alpha^{\pi+\alpha} V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{\pi}} \sqrt{\int_\alpha^{\pi+\alpha} \frac{1 - \cos 2\omega t}{2}\,d(\omega t)}$$
$$V_{rms} = \frac{V_m}{\sqrt{2\pi}} \sqrt{\left[ \omega t - \frac{\sin 2\omega t}{2} \right]_\alpha^{\pi+\alpha}} = \frac{V_m}{\sqrt{2\pi}} \sqrt{\pi} = \frac{V_m}{\sqrt{2}} = V_s$$
The RMS output voltage is independent of firing angle $\alpha$ and exactly equals the RMS AC supply voltage $V_s$.

- **Average Load Current ($I_{dc}$):**
Applying KVL to the DC loop:
$$V_{dc} = R I_{dc} + E \implies I_{dc} = \frac{V_{dc} - E}{R} = \frac{\frac{2 V_m}{\pi}\cos\alpha - E}{R}$$

### 3. Two-Quadrant Operation (Rectification vs Inversion)
The full converter operates in two quadrants on the $V_{dc}-I_{dc}$ plane:
1. **Quadrant I (Rectifier Mode, $0 \le \alpha < 90^\circ$):**
   $\cos\alpha > 0 \implies V_{dc} > 0$. Since thyristors only conduct current unidirectionally, $I_{dc} > 0$. Net power $P_{dc} = V_{dc} I_{dc} > 0$. Power flows from AC supply to DC motor (motoring drive).
2. **Quadrant IV (Inverter Mode, $90^\circ < \alpha < 180^\circ$):**
   $\cos\alpha < 0 \implies V_{dc} < 0$. Current cannot reverse ($I_{dc} > 0$). If the polarity of the DC source EMF $E$ is reversed (by reversing motor armature terminals during regenerative braking) such that $|E| > |V_{dc}|$, net power becomes negative:
   $$P_{dc} = V_{dc} I_{dc} < 0$$
   Power flows from the DC machine back into the AC utility grid. This is termed a **line-commutated inverter**.

```
             V_dc (Average Voltage)
                   ▲
                   │ Quadrant I: Rectification (Motoring)
                   │ P_dc > 0, 0 <= alpha < 90 deg
                   │
    ───────────────┼───────────────► I_dc (Current unidirectional)
                   │
                   │ Quadrant IV: Inversion (Regeneration)
                   │ P_dc < 0, 90 deg < alpha < 180 deg
                   ▼
```

### 4. Discontinuous Conduction Mode (DCM)
When load current is low, or at high values of back EMF $E$, the load current drops to zero at extinction angle $\beta < \pi + \alpha$.
During the idle interval $\beta \le \omega t \le \pi + \alpha$, all four thyristors are off ($i_o = 0$), and the output voltage floats at the battery back EMF:
$$v_o(t) = E \quad (\beta \le \omega t \le \pi + \alpha)$$

- **Average Voltage in DCM:**
$$V_{dc} = \frac{1}{\pi} \left[ \int_\alpha^\beta V_m \sin\omega t\,d(\omega t) + \int_\beta^{\pi+\alpha} E\,d(\omega t) \right]$$
$$V_{dc} = \frac{V_m}{\pi}(\cos\alpha - \cos\beta) + \frac{E}{\pi}(\pi + \alpha - \beta)$$
- **Minimum Firing Angle ($\alpha_{\min}$):**
To initiate conduction, the peak instantaneous AC supply voltage must exceed back EMF $E$:
$$\alpha_{\min} = \sin^{-1}\left(\frac{E}{V_m}\right)$$
"""
        },
        {
            "qid": "pe-q8",
            "marks": 10,
            "type": "Derivation & Performance Evaluation",
            "title": "Performance Parameters of Phase-Controlled Converters: DF, HF, THD, RF, and Comparative Analysis",
            "yt_query": "performance parameters phase controlled converters DF HF THD RF derivation",
            "img_path": "images/pe/converter_performance_parameters.png",
            "img_caption": "Figure 2.3: Input Current Harmonic Decomposition, Displacement Angle, and Performance Comparison of Semi vs Full Converters",
            "answer": r"""
To evaluate the power quality, grid distortion, and rectification efficiency of phase-controlled converters, standardized performance parameters are established.

### 1. Fundamental Definitions and Mathematical Formulations

#### A. Input Displacement Factor (DF)
The Displacement Factor is the cosine of the phase displacement angle $\phi_1$ between the fundamental component of AC input current $i_{s1}(t)$ and the sinusoidal AC input voltage $v_s(t)$:
$$\text{DF} = \cos\phi_1$$
For a single-phase fully controlled converter with ripple-free DC load current $I_{dc}$, the fundamental current lags the supply voltage by the firing angle $\alpha$:
$$\phi_1 = \alpha \implies \text{DF} = \cos\alpha$$

#### B. Harmonic Factor (HF) / Total Harmonic Distortion (THD)
The Harmonic Factor measures the harmonic content present in the input supply current relative to the fundamental component:
$$\text{THD} = \text{HF} = \frac{\sqrt{I_s^2 - I_{s1}^2}}{I_{s1}} = \sqrt{\left(\frac{I_s}{I_{s1}}\right)^2 - 1}$$
where $I_s$ is the total RMS supply current and $I_{s1}$ is the RMS value of the fundamental current.

For a 1-phase full converter with ripple-free DC load current $I_{dc}$:
- Supply current is a square wave of amplitude $\pm I_{dc}$:
$$I_s = \sqrt{\frac{1}{\pi}\int_0^\pi I_{dc}^2\,d(\omega t)} = I_{dc}$$
- Fourier series expansion of supply current $i_s(t)$:
$$i_s(t) = \sum_{n=1,3,5\dots}^\infty \frac{4 I_{dc}}{n \pi} \sin\left[n(\omega t - \alpha)\right]$$
- Fundamental RMS current ($n = 1$):
$$I_{s1} = \frac{4 I_{dc}}{\pi \sqrt{2}} = \frac{2\sqrt{2}}{\pi} I_{dc} \approx 0.9003 I_{dc}$$

Substituting $I_s$ and $I_{s1}$ into the THD formulation:
$$\text{THD} = \sqrt{\left(\frac{I_{dc}}{\frac{2\sqrt{2}}{\pi}I_{dc}}\right)^2 - 1} = \sqrt{\left(\frac{\pi}{2\sqrt{2}}\right)^2 - 1} = \sqrt{\frac{\pi^2}{8} - 1} \approx \sqrt{1.2337 - 1} = \sqrt{0.2337} \approx 0.4834 \ (48.34\%)$$

#### C. Input Power Factor (PF)
The overall power factor is the ratio of real active input power to total apparent volt-amperes:
$$\text{PF} = \frac{P_{in}}{S_{in}} = \frac{V_s I_{s1} \cos\phi_1}{V_s I_s} = \left(\frac{I_{s1}}{I_s}\right) \cos\phi_1 = g \cdot \text{DF}$$
where $g = I_{s1} / I_s$ is defined as the **Current Distortion Factor**.
For the 1-phase full converter:
$$g = \frac{2\sqrt{2}}{\pi} \approx 0.9003 \implies \text{PF} = \frac{2\sqrt{2}}{\pi}\cos\alpha \approx 0.9 \cos\alpha$$

#### D. Form Factor (FF) and Voltage Ripple Factor (RF)
- **Form Factor (FF):** Ratio of RMS output voltage to average DC output voltage:
$$\text{FF} = \frac{V_{rms}}{V_{dc}} = \frac{V_m/\sqrt{2}}{\frac{2 V_m}{\pi}\cos\alpha} = \frac{\pi}{2\sqrt{2}\cos\alpha}$$
- **Ripple Factor (RF):** Measure of residual AC ripple voltage on the DC output:
$$\text{RF} = \frac{V_{ac}}{V_{dc}} = \frac{\sqrt{V_{rms}^2 - V_{dc}^2}}{V_{dc}} = \sqrt{\left(\frac{V_{rms}}{V_{dc}}\right)^2 - 1} = \sqrt{\text{FF}^2 - 1}$$

### 2. Comprehensive Comparison: Semi-Converter vs Full-Converter

| Metric / Parameter | 1-Phase Semi-Converter | 1-Phase Full-Converter |
| :--- | :--- | :--- |
| **Topology** | 2 SCRs + 2 Diodes (or FD) | 4 SCRs (Fully controlled) |
| **Quadrants** | 1 Quadrant ($V_{dc} \ge 0, I_{dc} \ge 0$) | 2 Quadrants ($V_{dc} \gtrless 0, I_{dc} \ge 0$) |
| **Average Output Voltage** | $V_{dc} = \frac{V_m}{\pi}(1 + \cos\alpha)$ | $V_{dc} = \frac{2 V_m}{\pi}\cos\alpha$ |
| **RMS Output Voltage** | $V_s \sqrt{\frac{1}{\pi}[(\pi-\alpha) + \frac{1}{2}\sin 2\alpha]}$ | $V_{rms} = V_s$ (Constant) |
| **Inversion Capability** | No (Cannot regenerate) | Yes (Regeneration for $\alpha > 90^\circ$) |
| **Input Current Waveform** | Quasi-square with zero gaps | Pure square wave ($I_{dc}$ to $-I_{dc}$) |
| **Displacement Factor (DF)**| $\cos(\alpha/2)$ | $\cos\alpha$ |
| **Input Power Factor (PF)** | $\frac{\sqrt{2}(1 + \cos\alpha)}{\sqrt{\pi(\pi - \alpha)}}$ | $\frac{2\sqrt{2}}{\pi}\cos\alpha$ |
| **Reactive Power Demand** | Much lower (Freewheeling diode) | High, especially near $\alpha \approx 90^\circ$ |
| **Circuit Cost & Control** | Cheaper (2 gate drivers only) | Higher (4 isolated gate drivers) |

**Key Takeaway:** At any firing angle $\alpha > 0$, the semi-converter exhibits a significantly superior power factor and lower reactive power consumption because freewheeling action bypasses the AC source during $(0 \le \omega t \le \alpha)$, eliminating reactive circulating current.
"""
        },
        {
            "qid": "pe-q9",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Three-Phase Fully Controlled Bridge Converter (6-Pulse) with Highly Inductive Load",
            "yt_query": "three phase full converter bridge 6 pulse derivation waveforms",
            "img_path": "images/pe/3ph_full_converter_bridge.png",
            "img_caption": "Figure 2.4: 3-Phase Fully Controlled Bridge Rectifier Circuit, Firing Sequence, and Output Line-to-Line Conduction Waveforms",
            "answer": r"""
The three-phase fully controlled bridge converter (6-pulse converter) is the standard workhorse topology for high-power DC drives, electrochemical refining plants, and HVDC converter terminals.

### 1. Circuit Configuration and Conduction Sequence
The circuit consists of 6 thyristors connected across a balanced 3-phase AC supply ($v_a, v_b, v_c$):
- **Positive Group (Upper SCRs):** $T_1$ (phase $a$), $T_3$ (phase $b$), $T_5$ (phase $c$). The thyristor with the most positive instantaneous anode voltage conducts.
- **Negative Group (Lower SCRs):** $T_4$ (phase $a$), $T_6$ (phase $b$), $T_2$ (phase $c$). The thyristor with the most negative cathode voltage conducts.

```
                  ┌─────────┬─────────┬─────────┐
                  │ T1      │ T3      │ T5      │
             ┌────o─►|─┐  ┌─o─►|─┐  ┌─o─►|─┐    │
      Va ────┤    │    │  │ │    │  │ │    │    │
             │    └────┼──┘ └────┼──┘ └────┼────┘
      Vb ────┼─────────┼─────────┤         │
             │         │         │         │
      Vc ────┼─────────┼─────────┼─────────┤
             │    ┌────┴───┐┌────┴───┐┌────┴───┐
             └────┤ T4     ││ T6     ││ T2     │
                  └─►|─o───┘└─►|─o───┘└─►|─o───┘
                       │         │         │
                       └─────────┴────┬────┘
                                      │
                                   [ Load ]
                                      │
```

- **Triggering Sequence:** Thyristors are fired in numerical index order at uniform intervals of $60^\circ$ ($\pi/3$ rad):
$$T_1 \to T_2 \to T_3 \to T_4 \to T_5 \to T_6 \to T_1$$
- **Conduction Angle:** Each thyristor conducts for $120^\circ$ ($2\pi/3$ rad).
- At any operating instant, exactly two thyristors conduct simultaneously: one from the upper group and one from the lower group. The load is connected directly across the corresponding line-to-line voltage.
- **Conduction Pairs:**
  - $60^\circ + \alpha \text{ to } 120^\circ + \alpha$: $T_1$ and $T_6$ conduct ($v_o = v_{ab}$)
  - $120^\circ + \alpha \text{ to } 180^\circ + \alpha$: $T_1$ and $T_2$ conduct ($v_o = v_{ac}$)
  - $180^\circ + \alpha \text{ to } 240^\circ + \alpha$: $T_3$ and $T_2$ conduct ($v_o = v_{bc}$)
  - $240^\circ + \alpha \text{ to } 300^\circ + \alpha$: $T_3$ and $T_4$ conduct ($v_o = v_{ba}$)
  - $300^\circ + \alpha \text{ to } 360^\circ + \alpha$: $T_5$ and $T_4$ conduct ($v_o = v_{ca}$)
  - $0^\circ + \alpha \text{ to } 60^\circ + \alpha$: $T_5$ and $T_6$ conduct ($v_o = v_{cb}$)

### 2. Mathematical Derivation of Average Output Voltage ($V_{dc}$)
Because the output voltage waveform repeats every $60^\circ$ ($\pi/3$ rad), the average voltage is evaluated over one $60^\circ$ conduction period.
Let the line-to-line voltage $v_{ab}(t)$ be defined with reference to the peak line voltage $V_{ml} = \sqrt{2} V_L$:
$$v_{ab}(\omega t) = V_{ml} \cos\omega t$$
The natural commutation point occurs at $\omega t = -30^\circ$ ($-\pi/6$). When fired with a delay angle $\alpha$, the conduction interval for line pair $v_{ab}$ spans from $-\pi/6 + \alpha$ to $+\pi/6 + \alpha$.

Evaluating the average DC voltage:
$$V_{dc} = \frac{1}{\pi/3} \int_{-\pi/6 + \alpha}^{\pi/6 + \alpha} V_{ml} \cos\omega t\,d(\omega t) = \frac{3 V_{ml}}{\pi} [\sin\omega t]_{-\pi/6 + \alpha}^{\pi/6 + \alpha}$$
$$V_{dc} = \frac{3 V_{ml}}{\pi} \left[ \sin\left(\frac{\pi}{6} + \alpha\right) - \sin\left(-\frac{\pi}{6} + \alpha\right) \right]$$

Applying the trigonometric identity $\sin(A + B) - \sin(B - A) = 2 \sin A \cos B$:
$$V_{dc} = \frac{3 V_{ml}}{\pi} \left[ 2 \sin\frac{\pi}{6} \cos\alpha \right] = \frac{3 V_{ml}}{\pi} \left[ 2 \times \frac{1}{2} \cos\alpha \right] = \frac{3 V_{ml}}{\pi}\cos\alpha$$

Expressing in terms of RMS line voltage ($V_{ml} = \sqrt{2} V_L$):
$$V_{dc} = \frac{3 \sqrt{2} V_L}{\pi}\cos\alpha \approx 1.35 V_L \cos\alpha$$

Expressing in terms of RMS phase voltage ($V_L = \sqrt{3} V_{ph}$):
$$V_{dc} = \frac{3 \sqrt{6} V_{ph}}{\pi}\cos\alpha \approx 2.34 V_{ph} \cos\alpha$$

### 3. RMS Output Voltage Derivation
$$V_{rms} = \sqrt{\frac{3}{\pi} \int_{-\pi/6 + \alpha}^{\pi/6 + \alpha} V_{ml}^2 \cos^2\omega t\,d(\omega t)} = V_{ml} \sqrt{\frac{3}{\pi} \int_{-\pi/6 + \alpha}^{\pi/6 + \alpha} \frac{1 + \cos 2\omega t}{2}\,d(\omega t)}$$
$$V_{rms} = V_{ml} \sqrt{\frac{1}{2} + \frac{3\sqrt{3}}{4\pi}\cos 2\alpha}$$
At $\alpha = 0^\circ$:
$$V_{rms} = V_{ml} \sqrt{\frac{1}{2} + \frac{3\sqrt{3}}{4\pi}} = \sqrt{2} V_L \times 0.9558 = 1.655 V_{ph}$$

### 4. Rectifier Mode vs Inverter Mode
- For $0 \le \alpha < 90^\circ$: $\cos\alpha > 0 \implies V_{dc} > 0$. Real power flows from AC line to DC load (motoring).
- At $\alpha = 90^\circ$: $V_{dc} = 0$.
- For $90^\circ < \alpha < 180^\circ$: $\cos\alpha < 0 \implies V_{dc} < 0$. With reversed DC source EMF ($E > |V_{dc}|$), the converter operates as a line-commutated inverter, feeding active power from DC side into the 3-phase grid.
"""
        },
        {
            "qid": "pe-q10",
            "marks": 10,
            "type": "Derivation & Problem Solving",
            "title": "Effect of Source Inductance (Ls) on Commutation Angle and Output Voltage in Controlled Rectifiers",
            "yt_query": "effect of source inductance commutation overlap angle derivation 1ph 3ph converter",
            "img_path": "images/pe/source_inductance_overlap.png",
            "img_caption": "Figure 2.5: Commutation Overlap Phenomenon (mu) and Source Current Transfer due to AC Source Inductance",
            "answer": r"""
In ideal rectifier analysis, the AC supply is assumed to be an ideal voltage source with zero internal impedance. However, in physical systems, utility distribution lines and transformer windings possess significant leakage inductance, termed **Source Inductance ($L_s$)**.

### 1. Commutation Overlap Phenomenon
Because the current through an inductor cannot change discontinuously ($di/dt \ne \infty$), the current transfer from the outgoing thyristor pair to the incoming thyristor pair cannot happen instantaneously.
- **Commutation Overlap Interval ($\mu$):** The finite angular duration during which both outgoing and incoming thyristors conduct simultaneously.
- During overlap:
  1. The AC source is momentarily short-circuited through the conducting thyristors.
  2. The output terminal voltage drops to zero (in 1-phase bridge) or the mean of the commutating phase voltages (in 3-phase bridge).
  3. The average DC terminal voltage is reduced by an overlap voltage drop $\Delta V_d$.

```
AC Source (v_s) ──[ L_s ]──┬────► Outgoing SCR (Current decaying from I_dc to 0)
                           │
                           └────► Incoming SCR (Current rising from 0 to I_dc)
                                   Over interval: alpha to alpha + mu
```

### 2. Derivation of Overlap Angle ($\mu$) and Voltage Drop for 1-Phase Full Converter
Consider the commutation from thyristors $T_1, T_2$ to $T_3, T_4$ occurring at $\omega t = \alpha$.
During the overlap interval ($\alpha \le \omega t \le \alpha + \mu$):
- All four thyristors ($T_1, T_2, T_3, T_4$) are simultaneously conducting.
- The output terminal voltage is shorted: $v_o(t) = 0$.
- The source current $i_s(\omega t)$ transitions from $-I_{dc}$ to $+I_{dc}$.

Applying KVL to the AC loop:
$$v_s(t) = V_m \sin\omega t = L_s \frac{di_s}{dt} = \omega L_s \frac{di_s}{d(\omega t)}$$

Rearranging and integrating from $\omega t = \alpha$ ($i_s = -I_{dc}$) to $\omega t = \alpha + \mu$ ($i_s = +I_{dc}$):
$$\int_\alpha^{\alpha + \mu} V_m \sin\omega t\,d(\omega t) = \omega L_s \int_{-I_{dc}}^{+I_{dc}} di_s$$
$$V_m [-\cos\omega t]_\alpha^{\alpha + \mu} = \omega L_s [I_{dc} - (-I_{dc})]$$
$$V_m [\cos\alpha - \cos(\alpha + \mu)] = 2 \omega L_s I_{dc}$$

Solving for $\cos(\alpha + \mu)$:
$$\cos(\alpha + \mu) = \cos\alpha - \frac{2 \omega L_s I_{dc}}{V_m}$$

The reduction in average DC output voltage due to the loss of volt-second area during overlap is:
$$\Delta V_d = \frac{1}{\pi} \int_\alpha^{\alpha + \mu} V_m \sin\omega t\,d(\omega t) = \frac{V_m}{\pi} [\cos\alpha - \cos(\alpha + \mu)]$$
Substituting $V_m [\cos\alpha - \cos(\alpha + \mu)] = 2 \omega L_s I_{dc}$:
$$\Delta V_d = \frac{2 \omega L_s}{\pi} I_{dc} = 4 f L_s I_{dc}$$

The net average DC output voltage is:
$$V_{dc} = \frac{2 V_m}{\pi}\cos\alpha - \Delta V_d = \frac{2 V_m}{\pi}\cos\alpha - \frac{2 \omega L_s}{\pi} I_{dc}$$
Alternatively written as:
$$V_{dc} = \frac{V_m}{\pi} [\cos\alpha + \cos(\alpha + \mu)]$$

### 3. Extension to Three-Phase Fully Controlled Converter
In a 3-phase full bridge converter, commutation occurs between thyristors in the same group every $60^\circ$ ($6$ commutations per supply cycle):
$$\cos(\alpha + \mu) = \cos\alpha - \frac{2 \omega L_s I_{dc}}{\sqrt{3} V_{ml}}$$
where $V_{ml} = \sqrt{2} V_L$ is the peak line-to-line voltage.

Average voltage drop per commutation is $\frac{1}{\pi/3}\int \dots$, yielding:
$$\Delta V_d = \frac{3 \omega L_s}{\pi} I_{dc} = 6 f L_s I_{dc}$$

The net average DC output voltage of the 3-phase converter becomes:
$$V_{dc} = \frac{3 V_{ml}}{\pi}\cos\alpha - \frac{3 \omega L_s}{\pi} I_{dc} = \frac{3 V_{ml}}{2\pi}[\cos\alpha + \cos(\alpha + \mu)]$$

### 4. Commutation Failure in Inverter Mode
When operating in line-commutated inverter mode ($90^\circ < \alpha < 180^\circ$), the extinction angle is defined as:
$$\gamma = 180^\circ - (\alpha + \mu)$$
To prevent commutation failure, the circuit turn-off time $t_c = \gamma / \omega$ must be strictly greater than the device turn-off time $t_q$ ($t_c > t_q \implies \gamma > \omega t_q$).
If load current $I_{dc}$ increases or line voltage dips, overlap angle $\mu$ increases. If $\alpha + \mu$ approaches $180^\circ$, the thyristor is subjected to forward voltage before inner junction $J_2$ has recovered, resulting in catastrophic **inverter commutation failure** and AC short circuit.
"""
        }
    ]
}
