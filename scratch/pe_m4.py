# -*- coding: utf-8 -*-
"""
Module 4: Inverters (DC to AC Converters)
Subject: Power Electronics (EET306) - KTU 2019 Scheme S6 EEE
Questions: pe-q16 to pe-q20
"""

MODULE_4 = {
    "module_id": "pe-m4",
    "module_num": "Module 4",
    "module_title": "Inverters (DC to AC Converters)",
    "questions": [
        {
            "qid": "pe-q16",
            "marks": 10,
            "type": "Derivation & Waveform Analysis",
            "title": "Single-Phase Half-Bridge and Full-Bridge Voltage Source Inverters (VSI) with R and RL Loads",
            "yt_query": "single phase half bridge full bridge inverter VSI R RL load fourier series derivation",
            "img_path": "images/pe/1ph_vsi_bridge_inverter.png",
            "img_caption": "Figure 4.1: Circuit Topologies, Feedback Diode Conduction, and Output Voltage/Current Waveforms of 1-Phase VSIs",
            "answer": r"""
A Voltage Source Inverter (VSI) converts a stiff DC input voltage into an AC output voltage of controllable magnitude and frequency.

### 1. Single-Phase Half-Bridge VSI
The single-phase half-bridge VSI employs a 3-wire DC source with two identical split capacitors ($C_1 = C_2$) providing a virtual center-tap neutral point ($O$). It utilizes two controllable switches ($S_1, S_2$) and two antiparallel feedback diodes ($D_1, D_2$).

```
       + ───┬──────────────[ Switch S1 ]───┬───────────o A
            │                              │
          ┌─┴─┐                          ┌─┴─┐
          │C1 │                          │D1 │ Feedback Diode
          └─┬─┘                          └─┬─┘
            │                              │
       O ───┼──────────────────────────────┼───────────o B (Load between A and O)
            │                              │
          ┌─┴─┐                          ┌─┴─┐
          │C2 │                          │D2 │
          └─┬─┘                          └─┬─┘
            │                              │
       - ───┴──────────────[ Switch S2 ]───┴───────────o
```

- **Square-Wave Operation:**
  - For $0 < t \le T/2$: Switch $S_1$ conducts, connecting load terminal $A$ to the positive rail:
    $$v_o(t) = +\frac{V_{dc}}{2}$$
  - For $T/2 < t \le T$: Switch $S_2$ conducts, connecting load terminal $A$ to the negative rail:
    $$v_o(t) = -\frac{V_{dc}}{2}$$

- **RMS Output Voltage:**
  $$V_{o,rms} = \sqrt{\frac{1}{T}\left[ \int_0^{T/2} \left(\frac{V_{dc}}{2}\right)^2 dt + \int_{T/2}^T \left(-\frac{V_{dc}}{2}\right)^2 dt \right]} = \frac{V_{dc}}{2}$$

- **Fourier Series of Output Voltage:**
  Because the waveform possesses odd quarter-wave symmetry, even harmonics are zero ($a_n = 0, b_n = 0 \text{ for even } n$):
  $$b_n = \frac{4}{T}\int_0^{T/2} \left(\frac{V_{dc}}{2}\right) \sin(n \omega t)\,dt = \frac{2 V_{dc}}{n \pi} [-\cos(n\omega t)]_0^{\pi} = \frac{2 V_{dc}}{n \pi} [1 - \cos(n\pi)] = \frac{4 V_{dc}}{n \pi} \quad (n = 1, 3, 5\dots)$$
  $$v_o(t) = \sum_{n=1,3,5\dots}^\infty \frac{2 V_{dc}}{n \pi} \sin(n \omega t)$$

- **Fundamental RMS Voltage:**
  $$V_{o1,rms} = \frac{2 V_{dc}}{\sqrt{2} \pi} = \frac{\sqrt{2} V_{dc}}{\pi} \approx 0.450 V_{dc}$$

### 2. Single-Phase Full-Bridge VSI
The full-bridge configuration comprises four switches ($S_1, S_2, S_3, S_4$) and four antiparallel diodes ($D_1, D_2, D_3, D_4$).

```
       + ───┬──────────────┬───────────────o +
            │              │
          ┌─┴─┐          ┌─┴─┐
          │S1 │          │S3 │
          └─┬─┘          └─┬─┘
            ├───[ D1 ]     ├───[ D3 ]
            │              │
            o────[ Load ]──o
            │              │
            ├───[ D2 ]     ├───[ D4 ]
          ┌─┴─┐          ┌─┴─┐
          │S2 │          │S4 │
          └─┬─┘          └─┬─┘
            │              │
       - ───┴──────────────┴───────────────o -
```

- **Square-Wave Operation:**
  - For $0 < t \le T/2$: Diagonal switches $S_1$ and $S_2$ conduct:
    $$v_o(t) = +V_{dc}$$
  - For $T/2 < t \le T$: Diagonal switches $S_3$ and $S_4$ conduct:
    $$v_o(t) = -V_{dc}$$

- **RMS Output Voltage:**
  $$V_{o,rms} = \sqrt{\frac{1}{T}\int_0^T V_{dc}^2\,dt} = V_{dc}$$

- **Fourier Series Expansion:**
  $$v_o(t) = \sum_{n=1,3,5\dots}^\infty \frac{4 V_{dc}}{n \pi} \sin(n \omega t)$$
  The fundamental RMS output voltage is:
  $$V_{o1,rms} = \frac{4 V_{dc}}{\sqrt{2}\pi} = \frac{2\sqrt{2} V_{dc}}{\pi} \approx 0.90 V_{dc}$$
  The full-bridge inverter delivers **twice** the fundamental output voltage and **four times** the output power of a half-bridge inverter for the same DC link voltage.

### 3. Operation with Inductive ($R-L$) Load and Role of Feedback Diodes
With an inductive load, the output current $i_o(t)$ lags the output voltage $v_o(t)$ by phase angle $\phi_n = \tan^{-1}\left(\frac{n\omega L}{R}\right)$.
- When $S_1$ and $S_2$ are gated off at $t = T/2$, the inductor magnetic energy prevents the current from collapsing instantaneously. The current forces feedback diodes $D_3$ and $D_4$ into conduction.
- During this diode conduction interval:
  1. Terminal voltage is clamped to $-V_{dc}$.
  2. Load current remains positive ($i_o > 0$).
  3. Power is negative ($p(t) = v_o \cdot i_o < 0$), returning stored magnetic reactive energy from the load back into the DC source.
- Once $i_o(t)$ reaches zero, diodes $D_3$ and $D_4$ turn off naturally, and switches $S_3$ and $S_4$ begin conducting current in the negative direction ($v_o < 0, i_o < 0 \implies p(t) > 0$).
- **Rule of Thumb:**
  - Switches conduct when energy is delivered to the load ($v_o \cdot i_o > 0$).
  - Feedback diodes conduct when reactive energy is returned to the DC link ($v_o \cdot i_o < 0$).

### 4. Quasi-Square Wave Inverter (Single-Pulse Control)
By introducing a controllable zero-voltage deadband of width $\beta = \pi - 2d$ into the output voltage waveform, the inverter outputs $+V_{dc}$ for duration $2d$, $0\text{ V}$ for duration $(\pi - 2d)$, and $-V_{dc}$ for duration $2d$.
The Fourier series fundamental voltage is:
$$V_{o1,rms} = \frac{2\sqrt{2} V_{dc}}{\pi} \sin d$$
By modulating pulse half-width $d$, the fundamental voltage magnitude can be regulated continuously from $0$ to $0.9 V_{dc}$ while eliminating specific harmonic orders (e.g. setting $2d = 120^\circ$ completely eliminates the 3rd harmonic).
"""
        },
        {
            "qid": "pe-q17",
            "marks": 10,
            "type": "Derivation & Waveform Analysis",
            "title": "Three-Phase Voltage Source Inverter: 180-Degree Conduction Mode Analysis",
            "yt_query": "three phase inverter 180 conduction mode phase line voltage fourier series derivation",
            "img_path": "images/pe/3ph_vsi_180_conduction.png",
            "img_caption": "Figure 4.2: 3-Phase VSI Bridge, 180° Gating Sequence, Equivalent Circuits, and Step Waveforms",
            "answer": r"""
A three-phase voltage source inverter employs six controllable semiconductor switches ($S_1$ to $S_6$) and six antiparallel freewheeling diodes ($D_1$ to $D_6$) connected in a bridge configuration across a stiff DC link $V_{dc}$, feeding a balanced star-connected load with isolated neutral point $n$.

```
                  ┌─────────┬─────────┬─────────┐
                  │ S1      │ S3      │ S5      │
             ┌────o─┤       ├─o─┤     ├─o─┤     │
      + ─────┤    │ ├──[D1] │ │ ├──[D3] │ ├──[D5]
      V_dc   │    └─┼───────┘ └─┼───────┘ └─┼───┘
             │      │ a         │ b         │ c
      - ─────┼──────┼───────────┼───────────┤
             │    ┌─┴───────┐ ┌─┴───────┐ ┌─┴───┐
             └────┤ S4      │ │ S6      │ │ S2  │
                  └─o─┤     │ └─o─┤     │ └─o─┤ │
                      ├──[D4]     ├──[D6]   ├──[D2]
                      └─────────┴─────────┴─────┘
```

### 1. 180-Degree Gating Sequence
- Each switch conducts for an electrical angle of $180^\circ$ ($\pi$ rad).
- The gating signals to the upper and lower switches of the same leg are complementary: $(S_1, S_4)$, $(S_3, S_6)$, and $(S_5, S_2)$.
- Firing pulses are applied sequentially at intervals of $60^\circ$ ($\pi/3$ rad) in the order:
$$S_1 \to S_2 \to S_3 \to S_4 \to S_5 \to S_6 \to S_1$$
- At any given instant, exactly three switches are ON simultaneously: either two from the upper group and one from the lower group, or one from the upper group and two from the lower group.

### 2. Six Switching Intervals and Phase Voltage Derivations
Consider a balanced star load with phase impedances $Z_a = Z_b = Z_c = Z$.

- **Interval I ($0^\circ \le \omega t < 60^\circ$): Switches $S_5, S_6, S_1$ are ON.**
  - Phase $a$ and phase $c$ are connected to the positive DC bus ($+V_{dc}$).
  - Phase $b$ is connected to the negative DC bus ($0\text{ V}$).
  - Parallel combination of $Z_a$ and $Z_c$ is in series with $Z_b$.
  - Equivalent impedance:
    $$Z_{eq} = \frac{Z}{2} + Z = \frac{3}{2}Z$$
  - Neutral-to-negative bus voltage:
    $$V_{n0} = \frac{Z}{Z_{eq}} V_{dc} = \frac{Z}{\frac{3}{2}Z} V_{dc} = \frac{2}{3} V_{dc}$$
  - The resulting phase voltages ($v_{kn} = V_{k0} - V_{n0}$) are:
    $$v_{an} = V_{dc} - \frac{2}{3}V_{dc} = +\frac{1}{3}V_{dc}$$
    $$v_{bn} = 0 - \frac{2}{3}V_{dc} = -\frac{2}{3}V_{dc}$$
    $$v_{cn} = V_{dc} - \frac{2}{3}V_{dc} = +\frac{1}{3}V_{dc}$$

- **Interval II ($60^\circ \le \omega t < 120^\circ$): Switches $S_6, S_1, S_2$ are ON.**
  - Phase $a$ connected to $+V_{dc}$; phases $b$ and $c$ connected to $0\text{ V}$.
  - $V_{n0} = \frac{Z/2}{\frac{3}{2}Z} V_{dc} = \frac{1}{3} V_{dc}$.
  - Phase voltages:
    $$v_{an} = V_{dc} - \frac{1}{3}V_{dc} = +\frac{2}{3}V_{dc}$$
    $$v_{bn} = 0 - \frac{1}{3}V_{dc} = -\frac{1}{3}V_{dc}$$
    $$v_{cn} = 0 - \frac{1}{3}V_{dc} = -\frac{1}{3}V_{dc}$$

The phase-to-neutral voltage is a six-step staircase waveform taking discrete values:
$$v_{an} \in \left\{ +\frac{1}{3}V_{dc},\, +\frac{2}{3}V_{dc},\, +\frac{1}{3}V_{dc},\, -\frac{1}{3}V_{dc},\, -\frac{2}{3}V_{dc},\, -\frac{1}{3}V_{dc} \right\}$$

### 3. Line-to-Line Voltage Waveforms
Line voltages are obtained from phase differences:
$$v_{ab} = v_{an} - v_{bn}, \quad v_{bc} = v_{bn} - v_{cn}, \quad v_{ca} = v_{cn} - v_{an}$$
- During Interval I: $v_{ab} = \frac{1}{3}V_{dc} - \left(-\frac{2}{3}V_{dc}\right) = +V_{dc}$
- During Interval II: $v_{ab} = \frac{2}{3}V_{dc} - \left(-\frac{1}{3}V_{dc}\right) = +V_{dc}$
- During Interval III: $v_{ab} = 0$
- During Interval IV: $v_{ab} = -V_{dc}$
Line voltage $v_{ab}(t)$ is a quasi-square waveform that is non-zero for $120^\circ$ and zero for $60^\circ$ in each half cycle.

### 4. RMS Voltage Calculations

#### A. RMS Line-to-Line Voltage ($V_{L,rms}$)
$$V_{L,rms} = \sqrt{\frac{1}{\pi} \int_0^{2\pi/3} V_{dc}^2\,d(\omega t)} = V_{dc}\sqrt{\frac{2}{3}} \approx 0.8165 V_{dc}$$

#### B. RMS Phase Voltage ($V_{ph,rms}$)
$$V_{ph,rms} = \sqrt{\frac{1}{\pi} \left[ \int_0^{\pi/3} \left(\frac{V_{dc}}{3}\right)^2 d\omega t + \int_{\pi/3}^{2\pi/3} \left(\frac{2V_{dc}}{3}\right)^2 d\omega t + \int_{2\pi/3}^{\pi} \left(\frac{V_{dc}}{3}\right)^2 d\omega t \right]}$$
$$V_{ph,rms} = \sqrt{\frac{V_{dc}^2}{\pi} \left[ \frac{\pi}{3} \cdot \frac{1}{9} + \frac{\pi}{3} \cdot \frac{4}{9} + \frac{\pi}{3} \cdot \frac{1}{9} \right]} = \sqrt{\frac{V_{dc}^2}{3} \cdot \frac{6}{9}} = \frac{\sqrt{2}}{3} V_{dc} \approx 0.4714 V_{dc}$$

Notice the relationship:
$$V_{L,rms} = \sqrt{3} V_{ph,rms} = \sqrt{3} \times \frac{\sqrt{2}}{3} V_{dc} = \sqrt{\frac{2}{3}} V_{dc}$$

### 5. Fourier Analysis and Elimination of Triplen Harmonics
The Fourier series of line voltage $v_{ab}(t)$ is:
$$v_{ab}(t) = \sum_{n=1,3,5\dots}^\infty \frac{4 V_{dc}}{n \pi} \cos\left(\frac{n\pi}{6}\right) \sin\left[n\left(\omega t + \frac{\pi}{6}\right)\right]$$

For triplen harmonics ($n = 3, 9, 15\dots$):
$$\cos\left(\frac{3\pi}{6}\right) = \cos\left(\frac{\pi}{2}\right) = 0$$
All triplen harmonics ($3rd, 9th, 15th\dots$) are inherently eliminated from the line-to-line output voltages.

The fundamental peak line voltage ($n = 1$) is:
$$V_{L1\max} = \frac{4 V_{dc}}{\pi}\cos\frac{\pi}{6} = \frac{2\sqrt{3}}{\pi} V_{dc} \approx 1.1026 V_{dc}$$
The fundamental RMS line voltage is:
$$V_{L1,rms} = \frac{V_{L1\max}}{\sqrt{2}} = \frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc}$$
"""
        },
        {
            "qid": "pe-q18",
            "marks": 10,
            "type": "Derivation & Waveform Analysis",
            "title": "Three-Phase Voltage Source Inverter: 120-Degree Conduction Mode Analysis",
            "yt_query": "three phase inverter 120 conduction mode derivation line phase voltage comparison",
            "img_path": "images/pe/3ph_vsi_120_conduction.png",
            "img_caption": "Figure 4.3: 3-Phase VSI 120° Conduction Mode Firing Scheme, Equivalent Circuits, and Waveforms",
            "answer": r"""
In the $120^\circ$ conduction mode of a 3-phase Voltage Source Inverter, each semiconductor switch conducts for an electrical angle of $120^\circ$ ($\frac{2\pi}{3}$ rad). This is followed by an idle interval of $60^\circ$ ($\frac{\pi}{3}$ rad) during which neither switch in that phase leg conducts.

### 1. Gating Sequence and Commutation Characteristics
- Gating signals are applied to the six switches in sequence ($S_1 \to S_2 \to S_3 \to S_4 \to S_5 \to S_6$) at intervals of $60^\circ$.
- Each switch conducts for $120^\circ$ and stays off for $240^\circ$.
- **Natural Shoot-Through Immunity:** Because each upper switch turns off $60^\circ$ before the lower switch in the same leg is fired, a built-in deadband of $60^\circ$ exists. This naturally prevents shoot-through short circuits without requiring dead-time delay circuits.
- At any operating instant, exactly two switches are ON simultaneously: one from the upper positive group and one from the lower negative group. The third phase leg remains open-circuited (floating).

### 2. Phase-by-Phase Voltage Derivations
Consider a balanced star load with phase impedances $Z_a = Z_b = Z_c = Z$.

- **Interval I ($0^\circ \le \omega t < 60^\circ$): Switches $S_1$ and $S_6$ are ON.**
  - Switch $S_1$ connects load phase $a$ to $+V_{dc}$.
  - Switch $S_6$ connects load phase $b$ to negative rail ($0\text{ V}$).
  - Phase $c$ is completely open-circuited ($i_c = 0$).
  - Phases $a$ and $b$ are connected in series across $V_{dc}$. The neutral point $n$ sits at half the DC bus voltage:
    $$V_{n0} = \frac{V_{dc}}{2}$$
  - The resulting phase voltages are:
    $$v_{an} = V_{dc} - \frac{V_{dc}}{2} = +\frac{V_{dc}}{2}$$
    $$v_{bn} = 0 - \frac{V_{dc}}{2} = -\frac{V_{dc}}{2}$$
    $$v_{cn} = 0 \quad (\text{since phase } c \text{ is disconnected})$$

- **Interval II ($60^\circ \le \omega t < 120^\circ$): Switches $S_1$ and $S_2$ are ON.**
  - Switch $S_1$ connects phase $a$ to $+V_{dc}$; switch $S_2$ connects phase $c$ to $0\text{ V}$. Phase $b$ is open.
  - Phase voltages:
    $$v_{an} = +\frac{V_{dc}}{2}, \quad v_{bn} = 0, \quad v_{cn} = -\frac{V_{dc}}{2}$$

Over a full cycle, phase-to-neutral voltage $v_{an}(t)$ is a six-step waveform taking values:
$$v_{an} \in \left\{ +\frac{V_{dc}}{2},\, +\frac{V_{dc}}{2},\, 0,\, -\frac{V_{dc}}{2},\, -\frac{V_{dc}}{2},\, 0 \right\}$$

### 3. Line-to-Line Output Voltage Waveforms
Line voltages are computed as $v_{ab} = v_{an} - v_{bn}$, $v_{bc} = v_{bn} - v_{cn}$, and $v_{ca} = v_{cn} - v_{an}$.
- During Interval I: $v_{ab} = +\frac{V_{dc}}{2} - \left(-\frac{V_{dc}}{2}\right) = +V_{dc}$
- During Interval II: $v_{ab} = +\frac{V_{dc}}{2} - 0 = +\frac{V_{dc}}{2}$
- During Interval III: $v_{ab} = 0 - \left(+\frac{V_{dc}}{2}\right) = -\frac{V_{dc}}{2}$
- During Interval IV: $v_{ab} = -\frac{V_{dc}}{2} - \left(+\frac{V_{dc}}{2}\right) = -V_{dc}$

The line voltage waveform has five discrete levels: $+V_{dc}, +\frac{V_{dc}}{2}, 0, -\frac{V_{dc}}{2}, -V_{dc}$.

### 4. RMS Voltage Calculations

#### A. RMS Phase Voltage ($V_{ph,rms}$)
$$V_{ph,rms} = \sqrt{\frac{1}{\pi} \int_0^{2\pi/3} \left(\frac{V_{dc}}{2}\right)^2 d(\omega t)} = \frac{V_{dc}}{2}\sqrt{\frac{2}{3}} = \frac{V_{dc}}{\sqrt{6}} \approx 0.4082 V_{dc}$$

#### B. RMS Line Voltage ($V_{L,rms}$)
$$V_{L,rms} = \sqrt{\frac{1}{\pi} \left[ \int_0^{\pi/3}\left(\frac{V_{dc}}{2}\right)^2 d\omega t + \int_{\pi/3}^{2\pi/3} V_{dc}^2\,d\omega t + \int_{2\pi/3}^\pi \left(\frac{V_{dc}}{2}\right)^2 d\omega t \right]}$$
$$V_{L,rms} = \sqrt{\frac{V_{dc}^2}{\pi}\left[ \frac{\pi}{12} + \frac{\pi}{3} + \frac{\pi}{12} \right]} = \sqrt{V_{dc}^2 \left(\frac{1}{6} + \frac{1}{3}\right)} = \sqrt{\frac{V_{dc}^2}{2}} = \frac{V_{dc}}{\sqrt{2}} \approx 0.7071 V_{dc}$$

### 5. Detailed Comparative Evaluation: 180° vs 120° Conduction Modes

| Performance Metric | 180° Conduction Mode | 120° Conduction Mode |
| :--- | :--- | :--- |
| **Switch Conduction Angle** | $180^\circ$ ($\pi$ rad) | $120^\circ$ ($2\pi/3$ rad) |
| **Switches Conducting Simultaneously** | Exactly 3 switches | Exactly 2 switches |
| **RMS Line Voltage ($V_{L,rms}$)** | $\sqrt{\frac{2}{3}} V_{dc} \approx 0.8165 V_{dc}$ | $\frac{V_{dc}}{\sqrt{2}} \approx 0.7071 V_{dc}$ |
| **RMS Phase Voltage ($V_{ph,rms}$)**| $\frac{\sqrt{2}}{3} V_{dc} \approx 0.4714 V_{dc}$ | $\frac{V_{dc}}{\sqrt{6}} \approx 0.4082 V_{dc}$ |
| **Fundamental RMS Line Voltage** | $\frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc}$ | $\frac{3}{\sqrt{2}\pi} V_{dc} \approx 0.6752 V_{dc}$ |
| **DC Bus Utilization** | Higher ($15.5\%$ higher output) | Lower ($86.6\%$ of $180^\circ$ mode) |
| **Shoot-Through Risk** | High (Requires blanking deadtime) | None (Inherent $60^\circ$ deadband) |
| **Switch Thermal Duty** | Higher current duty ($50\%$) | Lower conduction duty ($33.3\%$) |
"""
        },
        {
            "qid": "pe-q19",
            "marks": 10,
            "type": "Comparative Analysis & Mathematical Derivation",
            "title": "Pulse Width Modulation (PWM) Techniques: Single-Pulse, Multi-Pulse, and Sinusoidal PWM (SPWM)",
            "yt_query": "PWM inverter techniques single pulse multiple pulse sinusoidal PWM SPWM derivation",
            "img_path": "images/pe/pwm_modulation_techniques.png",
            "img_caption": "Figure 4.4: Carrier-Based Modulation Schemes: Single-Pulse, Multi-Pulse, and Sinusoidal PWM Generation with Harmonic Spectra",
            "answer": r"""
Pulse Width Modulation (PWM) techniques are implemented in inverters to achieve two simultaneous objectives:
1. Precise regulation of the output AC voltage magnitude and frequency without altering the input DC bus.
2. Attenuation and shifting of harmonic components toward higher frequencies, vastly shrinking the physical size of harmonic output filters.

### 1. Single-Pulse Width Modulation
In single-pulse modulation, the inverter produces one rectangular pulse of width $2d$ symmetrical about the center of each half-cycle ($\pi/2$ and $3\pi/2$).

- **Fourier Analysis of Output Voltage:**
  $$v_o(t) = \sum_{n=1,3,5\dots}^\infty \left[ \frac{4 V_{dc}}{n \pi} \sin(n d) \right] \sin(n \omega t)$$
- **Fundamental Peak and RMS Output Voltage:**
  $$V_{o1\max} = \frac{4 V_{dc}}{\pi} \sin d \implies V_{o1,rms} = \frac{2\sqrt{2} V_{dc}}{\pi} \sin d$$
- **Harmonic Elimination:**
  The amplitude of the $n$-th harmonic is proportional to $\sin(n d)$. To eliminate the $n$-th harmonic:
  $$\sin(n d) = 0 \implies n d = \pi \implies 2d = \frac{2\pi}{n}$$
  For instance, to completely eliminate the dominant 3rd harmonic ($n = 3$):
  $$2d = \frac{2 \times 180^\circ}{3} = 120^\circ$$

### 2. Multiple Pulse Width Modulation (MPWM)
Instead of a single pulse per half-cycle, multiple pulses of uniform width $\gamma$ are distributed across each half-cycle.
- If there are $p$ pulses per half-cycle, the pulse repetition frequency is $2 p f_m$.
- The dominant lower-order harmonics present in single-pulse modulation are shifted into high-frequency sidebands clustered around the chopping frequency:
$$f_h = 2 p f_m \pm 1$$
Because these harmonics reside at high frequencies, they are heavily attenuated by load inductance with minimal filter bulk.

### 3. Sinusoidal Pulse Width Modulation (SPWM)
Sinusoidal PWM is the industry standard modulation method. It generates gating pulses by comparing a high-frequency triangular carrier wave $v_c(t)$ with a low-frequency sinusoidal reference modulating wave $v_r(t)$.

```
      Voltage
         ▲     Carrier Wave v_c (Freq f_c, Peak A_c)
     A_c ┼     /\  /\  /\  /\  /\  /\  /\  /\  /\  /\
         │    /  \/  \/  \/  \/  \/  \/  \/  \/  \/  \
     A_r ┼───/───.────.───/───.───/───.───.───.───\─── Modulating Wave v_r (Freq f_m, Peak A_r)
         │  /     \  / \ /     \ /     \ / \ /     \
         └─/───────\/───X───────X───────X───X───────\──────► Time (t)
   Gating│
   Pulse ┼─┐  ┌──┐  ┌────┐  ┌──────┐  ┌────┐  ┌──┐  ┌─
         │ │  │  │  │    │  │      │  │    │  │  │  │
       0 ┴─┴──┴──┴──┴────┴──┴──────┴──┴────┴──┴──┴──┴──────►
```

#### A. Key Modulation Parameters
1. **Amplitude Modulation Index ($m_a$):**
   The ratio of the peak amplitude of the modulating sinusoidal reference wave ($A_r$) to the peak amplitude of the triangular carrier wave ($A_c$):
   $$m_a = \frac{A_r}{A_c}$$
2. **Frequency Modulation Ratio ($m_f$):**
   The ratio of the carrier frequency ($f_c$) to the reference fundamental frequency ($f_m$):
   $$m_f = \frac{f_c}{f_m}$$
   To eliminate even harmonics and DC offsets, $m_f$ must be chosen as an odd integer. In 3-phase inverters, selecting $m_f$ as an odd multiple of 3 eliminates triplen carrier harmonics from line-to-line voltages.

#### B. Operating Modulation Regimes
1. **Linear Modulation Region ($0 \le m_a \le 1$):**
   The peak of the reference sine wave never exceeds the peak of the triangular carrier wave. The fundamental peak output voltage is strictly linearly proportional to $m_a$:
   $$V_{o1\max} = m_a V_{dc} \implies V_{o1,rms} = \frac{m_a V_{dc}}{\sqrt{2}} \quad (\text{for full-bridge})$$
   In this linear zone, output voltage control is perfectly linear, and no low-frequency baseband subharmonics are produced.
2. **Overmodulation Region ($1 < m_a \le 3.24$):**
   The reference wave exceeds the carrier amplitude near the peaks, causing the pulses near the center of each half-cycle to merge into a single wide pulse (pulse dropping). Output voltage continues to increase but becomes non-linear with $m_a$, and lower-order harmonics ($5th, 7th$) reappear in the spectrum.
3. **Square-Wave Mode ($m_a > 3.24$):**
   The reference wave completely engulfs the carrier, collapsing modulation into pure square-wave switching. The fundamental peak output reaches its theoretical ceiling:
   $$V_{o1\max} = \frac{4 V_{dc}}{\pi} \approx 1.273 V_{dc}$$

#### C. Harmonic Spectrum of SPWM
In SPWM, harmonics are pushed outward into high-frequency sidebands clustered around integer multiples of the carrier frequency:
$$f_h = (j \cdot m_f \pm k) f_m$$
where $j = 1, 2, 3\dots$ and $k = 1, 3, 5\dots$.
For $j = 1$, the first significant harmonic cluster appears at:
$$f_{h1} = (m_f \pm 2) f_m$$
Since industrial converters operate with high carrier frequencies ($f_c \approx 5\text{ to }20\text{ kHz}$), the first significant harmonic appears far above the fundamental grid frequency ($50\text{ Hz}$), enabling nearly pure sinusoidal load currents using compact, inexpensive inductors.
"""
        },
        {
            "qid": "pe-q20",
            "marks": 10,
            "type": "Comparative Analysis & Circuit Principles",
            "title": "Current Source Inverter (CSI) vs Voltage Source Inverter (VSI): Principles and Detailed Comparison",
            "yt_query": "current source inverter vs voltage source inverter CSI VSI comparison ASCI circuit",
            "img_path": "images/pe/csi_vs_vsi_comparison.png",
            "img_caption": "Figure 4.5: Topologies of Voltage Source Inverter (VSI) and Auto-Sequential Commutated Current Source Inverter (ASCI)",
            "answer": r"""
Inverters are classified based on the nature of their input DC supply into Voltage Source Inverters (VSI) and Current Source Inverters (CSI).

### 1. Fundamental Operating Principles

#### A. Voltage Source Inverter (VSI)
- **Input Source:** Fed by a stiff DC voltage source with negligible internal impedance, typically realized by a large electrolytic capacitor bank ($C_{dc}$) across the DC bus.
- **Output Characteristics:** The output terminal voltage is a rigid square or PWM pulse train whose waveform is completely independent of the load impedance. The load current waveform and phase angle are determined entirely by the nature of the load (e.g. lagging current for inductive motor load).
- **Feedback Diodes:** Antiparallel freewheeling diodes across each switch are mandatory to provide a bidirectional current path for reactive load current returning to the DC link.

#### B. Current Source Inverter (CSI)
- **Input Source:** Fed by a stiff DC current source with very high internal impedance, synthesized by a phase-controlled rectifier in series with a massive DC link inductor ($L_{dc}$).
- **Output Characteristics:** The output AC current is an alternating square wave whose amplitude and waveform are governed strictly by the inverter switching sequence, independent of the load. The output voltage waveform and harmonic distortion depend directly on the load impedance.
- **Reverse Blocking:** Antiparallel diodes cannot be used because they would short the DC current source. Switches must possess bidirectional voltage-blocking capability.

### 2. Auto-Sequential Commutated Inverter (ASCI)
The Auto-Sequential Commutated Inverter is the standard thyristor-based CSI topology for medium-voltage induction motor drives.

```
       + ──[ L_dc ]──┬─────────┬─────────┬─────────┐
                     │ T1      │ T3      │ T5      │
                ┌────o─►|─┐  ┌─o─►|─┐  ┌─o─►|─┐    │
                │    │    │  │ │    │  │ │    │    │
                │   [ D1 ]│  │[ D3 ]│  │[ D5 ]│    │
                │    │    │  │ │    │  │ │    │    │
                │    ├──[C1]─┼─┤──[C3]─┼─┤──[C5]───┘
                │    │       │ │       │ │
                │    o───────┼─o───────┼─o──► To 3-Phase Load
                │    │       │ │       │ │
                │    ├──[C4]─┼─┤──[C6]─┼─┤──[C2]───┐
                │    │    │  │ │    │  │ │    │    │
                │   [ D4 ]│  │[ D6 ]│  │[ D2 ]│    │
                │    │    │  │ │    │  │ │    │    │
                └────┤ T4  │ │ │ T6  │ │ │ T2  │   │
                     └─►|─o──┘ └─►|─o──┘ └─►|─o────┘
                          │         │         │
       - ─────────────────┴─────────┴─────────┴────o -
```

- **Components:** Six thyristors ($T_1$ to $T_6$), six series blocking diodes ($D_1$ to $D_6$), and six commutating capacitors ($C_1$ to $C_6$).
- **Commutation Mechanism:** When incoming thyristor $T_3$ is fired, the pre-charged commutating capacitor $C_1$ discharges across outgoing thyristor $T_1$, applying reverse bias to turn it off. Diodes $D_1-D_6$ isolate the commutating capacitors from the load during normal conduction, preventing capacitor discharge into the motor windings.
- **Commutation Capacitor Sizing Derivation:**
  During the linear capacitor discharge phase, constant link current $I_{dc}$ charges/discharges the commutation capacitor $C$. The available circuit turn-off time $t_c$ provided to the extinguishing thyristor is:
  $$t_c = \frac{C \cdot \Delta V}{I_{dc}} = \frac{C \cdot \sqrt{3} V_{ml}}{I_{dc}}$$
  where $V_{ml} = \sqrt{2} V_L$ is the peak AC line voltage.
  To prevent commutation failure, $t_c$ must exceed device turn-off time $t_q$ ($t_c > t_q$), requiring a minimum capacitance:
  $$C \ge \frac{I_{dc} \cdot t_q}{\sqrt{3} V_{ml}}$$
- **DC Link Inductor Sizing:**
  To maintain a stiff current source with peak-to-peak ripple below $\Delta I_{dc}$:
  $$L_{dc} \ge \frac{V_{dc}}{6 \omega \cdot \Delta I_{dc}}$$
- **Power Flow and Four-Quadrant Regeneration:**
  Instantaneous DC link power is:
  $$P_{dc} = V_{dc} \cdot I_{dc}$$
  Because current direction is unalterable ($I_{dc} > 0$), instantaneous power reversal is achieved purely by shifting the front-end converter firing angle into the inverter region ($\alpha > 90^\circ \implies V_{dc} < 0$).

### 3. Comprehensive Comparative Matrix: VSI vs CSI

| Technical Parameter | Voltage Source Inverter (VSI) | Current Source Inverter (CSI) |
| :--- | :--- | :--- |
| **DC Link Filter** | Large shunt capacitor ($C_{dc}$) | Massive series inductor ($L_{dc}$) |
| **Controlled Variable**| Output voltage is rigid; current floats | Output current is rigid; voltage floats |
| **Switch Devices** | Fast IGBTs/MOSFETs with internal diode | Symmetrical GTOs / Thyristors with reverse blocking |
| **Feedback Diodes** | Mandatory (Antiparallel across switches) | Strictly prohibited (Series diodes used instead) |
| **Shoot-Through Fault**| Fatal: Two switches in same leg short DC bus | Inherent immunity: Large inductor limits $di/dt$ |
| **Open-Circuit Fault** | Safe: Load open circuit causes no damage | Fatal: Inductor produces catastrophic overvoltage spike |
| **Regenerative Braking**| Requires dual converter or Active Front End | Inherent: Instantaneous reversal of DC link voltage $V_{dc}$ |
| **Dynamic Response** | Very fast ($10\text{ to }50\text{ kHz}$ PWM switching) | Slower due to large DC link inductor time constant |
| **Output Waveforms** | PWM pulsed voltage, smooth sinusoidal current| Six-step current, spiked/distorted terminal voltage |
| **Primary Applications**| EVs, Solar PV, UPS, Industrial AC drives | Megawatt pumps, fans, gas turbine starter drives |

**Key Takeaway:** VSI has become the overwhelmingly dominant inverter technology in modern power electronics due to high-speed IGBTs, simple control, and compact size. CSI remains reserved for ultra-high-power medium-voltage motor drives where four-quadrant regenerative operation and short-circuit immunity are critical.
"""
        }
    ]
}
