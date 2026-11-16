# -*- coding: utf-8 -*-
"""
Module 5: AC Voltage Controllers, Cycloconverters & Resonant Converters
Subject: Power Electronics (EET306) - KTU 2019 Scheme S6 EEE
Questions: pe-q21 to pe-q26
"""

MODULE_5 = {
    "module_id": "pe-m5",
    "module_num": "Module 5",
    "module_title": "AC Voltage Controllers, Cycloconverters & Resonant Converters",
    "questions": [
        {
            "qid": "pe-q21",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Single-Phase AC Voltage Controller with Resistive Load: Integral Cycle Control and Phase Angle Control",
            "yt_query": "single phase AC voltage controller R load integral cycle phase control RMS voltage derivation",
            "img_path": "images/pe/1ph_ac_voltage_controller_r.png",
            "img_caption": "Figure 5.1: 1-Phase AC Voltage Controller Topologies and Output Waveforms for Integral Cycle and Phase Angle Control",
            "answer": r"""
AC voltage controllers (AC regulators) convert a fixed-voltage, fixed-frequency AC supply directly into a variable-voltage AC output at the same frequency without an intermediate DC link.

The basic single-phase power circuit consists of two thyristors ($T_1, T_2$) connected in antiparallel (inverse parallel) between the AC source $v_s(t) = V_m \sin\omega t$ and a resistive load $R$.

```
       v_s(t) ───┬───►| T1 ───┬──────────────o +
                 │            │
                 └─── |◄ T2 ──┘
                                      [R] Load   v_o(t)
                                      │
              ────────────────────────┴────────o -
```

### 1. Integral Cycle Control (ON-OFF Control)
In integral cycle control, the thyristor switch connects the load to the AC source for an integral number of cycles $n$, and disconnects it for an integral number of cycles $m$.
- Total control repeating period:
  $$T_o = (n + m) T_s$$
- Duty ratio ($k$):
  $$k = \frac{n}{n + m}$$

#### A. Derivation of RMS Output Voltage ($V_{o,rms}$)
The total energy delivered to the load over one repeating period $(n + m) T_s$ is the energy of $n$ complete sinusoidal AC cycles:
$$V_{o,rms} = \sqrt{\frac{1}{(n + m) T_s} \int_0^{n T_s} V_m^2 \sin^2\omega t\,dt}$$
Since the RMS value of a full sine wave over $n$ complete cycles is $V_s = V_m / \sqrt{2}$:
$$V_{o,rms} = \sqrt{\frac{n T_s}{(n + m) T_s} \left(\frac{V_m}{\sqrt{2}}\right)^2} = V_s \sqrt{\frac{n}{n + m}} = V_s \sqrt{k}$$

#### B. Input Power Factor (PF)
The active power delivered to the load is:
$$P = \frac{V_{o,rms}^2}{R} = \frac{k V_s^2}{R}$$
The apparent power supplied by the AC line is:
$$S = V_s I_{s,rms} = V_s \left(\frac{V_{o,rms}}{R}\right) = \frac{V_s^2 \sqrt{k}}{R}$$
The input power factor is:
$$\text{PF} = \frac{P}{S} = \frac{\frac{k V_s^2}{R}}{\frac{\sqrt{k} V_s^2}{R}} = \sqrt{k} = \sqrt{\frac{n}{n + m}}$$
- **Features:** Thyristors switch at natural zero-crossings, resulting in negligible switching power loss and virtually zero radio-frequency interference (RFI). However, the periodic on-off bursting generates sub-harmonic line flickering, restricting this method to high-inertia heating loads and temperature control systems.

### 2. Phase Angle Control
In phase angle control, thyristor $T_1$ is triggered at delay angle $\omega t = \alpha$ during the positive half-cycle, and thyristor $T_2$ is triggered at $\omega t = \pi + \alpha$ during the negative half-cycle. Each thyristor turns off naturally at the end of its respective half-cycle ($\pi$ and $2\pi$).

#### A. Derivation of RMS Output Voltage ($V_{o,rms}$)
Because the output voltage waveform possesses half-wave symmetry:
$$V_{o,rms} = \sqrt{\frac{1}{\pi} \int_\alpha^\pi V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{\pi}} \sqrt{\int_\alpha^\pi \frac{1 - \cos 2\omega t}{2}\,d(\omega t)}$$
$$V_{o,rms} = \frac{V_m}{\sqrt{2\pi}} \sqrt{\left[ \omega t - \frac{\sin 2\omega t}{2} \right]_\alpha^\pi} = \frac{V_m}{\sqrt{2\pi}} \sqrt{(\pi - \alpha) - \left(-\frac{\sin 2\alpha}{2}\right)}$$
$$V_{o,rms} = \frac{V_m}{\sqrt{2}} \sqrt{\frac{1}{\pi}\left[ (\pi - \alpha) + \frac{1}{2}\sin 2\alpha \right]} = V_s \sqrt{\frac{1}{\pi}\left[ (\pi - \alpha) + \frac{1}{2}\sin 2\alpha \right]}$$

#### B. Input Power Factor
Since the load is purely resistive, the RMS load current is $I_{o,rms} = V_{o,rms} / R$.
Active power is:
$$P = \frac{V_{o,rms}^2}{R}$$
Apparent power is:
$$S = V_s I_{s,rms} = V_s \left(\frac{V_{o,rms}}{R}\right)$$
The overall power factor is:
$$\text{PF} = \frac{P}{S} = \frac{V_{o,rms}}{V_s} = \sqrt{\frac{1}{\pi}\left[ (\pi - \alpha) + \frac{1}{2}\sin 2\alpha \right]}$$

- **Control Range:**
  - At $\alpha = 0^\circ$: $V_{o,rms} = V_s$ and $\text{PF} = 1.0$ (Full conduction).
  - At $\alpha = 90^\circ$: $V_{o,rms} = V_s / \sqrt{2} \approx 0.707 V_s$ and $\text{PF} = 0.707$.
  - At $\alpha = 180^\circ$: $V_{o,rms} = 0\text{ V}$ and $\text{PF} = 0$.
"""
        },
        {
            "qid": "pe-q22",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Single-Phase AC Voltage Controller with Inductive (RL) Load: Modes of Operation and Conduction Limits",
            "yt_query": "single phase AC voltage controller RL load derivation extinction angle conduction modes",
            "img_path": "images/pe/1ph_ac_voltage_controller_rl.png",
            "img_caption": "Figure 5.2: 1-Phase AC Regulator with RL Load showing Waveforms for α > φ, α = φ, and α < φ",
            "answer": r"""
When a single-phase AC voltage controller feeds a series inductive load ($R-L$), the load impedance is $Z = \sqrt{R^2 + (\omega L)^2}$ and the load impedance phase angle is defined as:
$$\phi = \tan^{-1}\left(\frac{\omega L}{R}\right)$$

### 1. Mathematical Analysis of Load Current
Thyristor $T_1$ is triggered at $\omega t = \alpha$. The circuit differential equation during conduction is:
$$L \frac{di_o}{dt} + R i_o = V_m \sin\omega t$$

The complete general solution consists of the steady-state sinusoidal component and a transient exponential component:
$$i_o(\omega t) = \frac{V_m}{Z}\sin(\omega t - \phi) + A e^{-\frac{R}{\omega L}\omega t}$$

Applying initial boundary condition $i_o(\alpha) = 0$:
$$0 = \frac{V_m}{Z}\sin(\alpha - \phi) + A e^{-\frac{R}{\omega L}\alpha} \implies A = -\frac{V_m}{Z}\sin(\alpha - \phi) e^{\frac{R}{\omega L}\alpha}$$

Substituting $A$ back into the current expression:
$$i_o(\omega t) = \frac{V_m}{Z}\left[ \sin(\omega t - \phi) - \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\omega t - \alpha)} \right] \quad (\alpha \le \omega t \le \beta)$$

### 2. Extinction Angle ($\beta$) and Conduction Angle ($\gamma$)
At $\omega t = \beta$, the load current extinguishes ($i_o(\beta) = 0$):
$$\sin(\beta - \phi) = \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\beta - \alpha)}$$
The conduction angle of the thyristor is:
$$\gamma = \beta - \alpha$$

### 3. Three Operating Modes based on Firing Angle $\alpha$

#### A. Case 1: Firing Angle Greater than Load Angle ($\alpha > \phi$)
- Conduction angle is less than $\pi$ radians ($\gamma < \pi \implies \beta < \pi + \alpha$).
- The current extinguishes at $\beta$ before the gate pulse is applied to the incoming reverse thyristor $T_2$ at $\pi + \alpha$.
- A zero-current deadband of width $(\pi + \alpha - \beta)$ exists.
- The output RMS voltage is fully controllable by varying $\alpha$ in the range $\phi \le \alpha \le \pi$.

#### B. Case 2: Firing Angle Equals Load Angle ($\alpha = \phi$)
- At $\alpha = \phi$, the transient exponential coefficient vanishes:
  $$\sin(\alpha - \phi) = \sin(0) = 0$$
- The load current reduces to a pure steady-state sinusoid:
  $$i_o(\omega t) = \frac{V_m}{Z}\sin(\omega t - \phi)$$
- The extinction angle occurs at:
  $$\beta = \pi + \phi = \pi + \alpha \implies \gamma = \beta - \alpha = \pi$$
- Each thyristor conducts for exactly $180^\circ$ ($\pi$ rad). As soon as $T_1$ turns off, $T_2$ is immediately triggered.
- The output voltage is a full continuous sine wave identical to the supply voltage ($V_{o,rms} = V_s$).

#### C. Case 3: Firing Angle Less than Load Angle ($\alpha < \phi$)
- If $\alpha < \phi$, the theoretical conduction angle exceeds $\pi$ ($\gamma > \pi$).
- At the instant $\omega t = \pi + \alpha$ when a firing pulse is delivered to incoming thyristor $T_2$, thyristor $T_1$ is still conducting ($i_o > 0$).
- Consequently, $T_2$ is reverse-biased by the forward voltage drop of $T_1$ and **fails to turn on**.
- If a narrow gate pulse is used, $T_2$ misses its firing opportunity entirely, resulting in single-phase half-wave rectification with massive DC saturation of supply transformers.
- **Rule:** The minimum permissible firing angle for an inductive load is:
$$\alpha_{\min} = \phi$$
Firing angles below $\phi$ provide no voltage control.

### 4. Derivation of RMS Output Voltage with Extinction Angle $\beta$
$$V_{o,rms} = \sqrt{\frac{1}{\pi} \int_\alpha^\beta V_m^2 \sin^2\omega t\,d(\omega t)} = \frac{V_m}{\sqrt{2\pi}} \sqrt{\int_\alpha^\beta (1 - \cos 2\omega t)\,d(\omega t)}$$
$$V_{o,rms} = \frac{V_m}{\sqrt{2}} \sqrt{\frac{1}{\pi} \left[ (\beta - \alpha) - \frac{\sin 2\beta - \sin 2\alpha}{2} \right]}$$
$$V_{o,rms} = V_s \sqrt{\frac{1}{\pi} \left[ \gamma - \frac{\sin 2\beta - \sin 2\alpha}{2} \right]}$$

### 5. Gating Pulse Requirements: Short Pulses vs High-Frequency Pulse Trains
With an inductive load, the rate of current rise ($di/dt$) is constrained by $L$. A short gate pulse ($10\text{ to }50\ \mu\text{s}$) may end before the anode current rises to the latching current $I_L$, causing firing failure. Furthermore, if $\alpha < \phi$, the incoming thyristor cannot turn on during the pulse.
To overcome this:
1. **Continuous Gate Signals:** Kept high for the entire conduction half-cycle $(\pi - \alpha)$; however, this creates excessive gate power dissipation.
2. **High-Frequency Pulse Train (Pulse Modulation):** A high-frequency pulse train ($f_p \approx 10\text{ to }20\text{ kHz}$) is applied for the full duration of $(\pi - \alpha)$. This ensures that as soon as the opposing thyristor commutates off and forward voltage appears, the incoming thyristor immediately latches into conduction, while gate drive power dissipation is drastically minimized.
"""
        },
        {
            "qid": "pe-q23",
            "marks": 10,
            "type": "Operating Principle & Topology Comparison",
            "title": "Single-Phase to Single-Phase Cycloconverters: Mid-Point and Bridge Configurations",
            "yt_query": "cycloconverter midpoint bridge step down step up circulating non circulating derivation",
            "img_path": "images/pe/cycloconverter_topologies.png",
            "img_caption": "Figure 5.3: 1-Phase Mid-Point and Bridge Cycloconverter Topologies and Synthesized Low-Frequency Waveforms",
            "answer": r"""
A cycloconverter is a direct AC-to-AC frequency changer that converts an input AC supply of fixed frequency and fixed voltage into an output AC supply of adjustable frequency and adjustable voltage without an intermediate DC energy storage link.

### 1. Classification by Frequency
1. **Step-Down Cycloconverter ($f_o < f_s$):**
   The output frequency is lower than the input line frequency (typically $f_o \le \frac{1}{3} f_s$ to maintain low harmonic distortion). Thyristors are commutated naturally by the AC supply line voltages (natural/line commutation).
2. **Step-Up Cycloconverter ($f_o > f_s$):**
   The output frequency is higher than the input frequency. Because line voltage does not reverse at the required switching instants, forced commutation circuitry is mandatory.

### 2. Single-Phase to Single-Phase Mid-Point Cycloconverter
The mid-point cycloconverter employs a center-tapped input transformer and four thyristors arranged into two converter groups:
- **Positive Group ($P_1, P_2$):** Produces positive load current ($i_o > 0$).
- **Negative Group ($N_1, N_2$):** Produces negative load current ($i_o < 0$).

```
                     ┌───►| P1 ───┐
      AC Supply      │            ├───┐
      ┌───[ ]───┐    ├─── |◄ N1 ──┘   │
      │         ├───o                 │
      │         │    O (Mid-point)    ├───o +
      │         ├───o                 │     [ Load ]
      └───[ ]───┘    ├───►| P2 ───┐   │
                     │            ├───┘
                     └─── |◄ N2 ──┘
```

- **Operation for $f_o = \frac{1}{3} f_s$ ($16.67\text{ Hz}$ from $50\text{ Hz}$):**
  - During the first $1.5$ cycles of input supply ($540^\circ$), thyristors $P_1$ and $P_2$ are triggered alternately in successive half-cycles to synthesize the positive half-cycle of the low-frequency output voltage.
  - During the next $1.5$ input cycles, thyristors $N_1$ and $N_2$ are triggered alternately to synthesize the negative half-cycle of the low-frequency output voltage.
  - The synthesized output wave has a fundamental period $T_o = 3 T_s \implies f_o = f_s / 3$.

### 3. Single-Phase to Single-Phase Bridge Cycloconverter
The bridge topology employs two fully controlled 1-phase bridge converters connected back-to-back in antiparallel across the load:
- **Positive Bridge ($P$-Converter):** Consists of 4 thyristors ($P_1, P_2, P_3, P_4$).
- **Negative Bridge ($N$-Converter):** Consists of 4 thyristors ($N_1, N_2, N_3, N_4$).
- **Advantage:** Eliminates the need for a heavy, expensive center-tapped transformer and doubles the output voltage rating for the same thyristor voltage class.

### 4. Circulating Current Mode vs Non-Circulating Current Mode

#### A. Non-Circulating Current Mode (Blocking Mode)
- In this scheme, only one converter group is enabled at any instant:
  - When load current is positive ($i_o > 0$), only the $P$-converter is fired, while gate pulses to the $N$-converter are completely suppressed.
  - When load current reverses ($i_o < 0$), firing pulses to the $P$-converter are inhibited, and after an intentional deadband delay ($1\text{ to }2\text{ ms}$) to ensure complete carrier recombination in outgoing thyristors, the $N$-converter is fired.
- **Advantage:** No circulating current flows between converters; efficiency is high; no intergroup reactor is needed.
- **Disadvantage:** The deadband around current zero crossings introduces output waveform distortion and harmonic degradation.

#### B. Circulating Current Mode
- Both $P$ and $N$ converter groups are operated simultaneously.
- To match their average DC terminal voltages, their firing angles are interlocked:
$$\alpha_P + \alpha_N = 180^\circ \implies \cos\alpha_N = -\cos\alpha_P$$
- Although average voltages match, instantaneous output voltages differ, creating an instantaneous AC voltage difference that would cause catastrophic short-circuit currents.
- **Intergroup Reactor (IGR):** A center-tapped current-limiting inductor is connected between the output terminals of the $P$ and $N$ converters to restrict this circulating ripple current.
- **Advantage:** Eliminates the zero-crossing deadband, producing clean, continuous, low-distortion sinusoidal current waveforms.

### 5. Industrial Applications
1. Gearless low-speed AC motor drives for cement kilns, ball mills, and mine winders ($>1\text{ MW}$, $0\text{ to }20\text{ Hz}$).
2. Variable-Speed Constant-Frequency (VSCF) aircraft generation systems ($400\text{ Hz}$ generation from variable engine shaft speed).
3. Heavy electric traction drives (converting $50\text{ Hz}$ three-phase grid power to $16\frac{2}{3}\text{ Hz}$ single-phase power for rail networks).
"""
        },
        {
            "qid": "pe-q24",
            "marks": 10,
            "type": "Principle & State-Plane Analysis",
            "title": "Resonant Converters: Zero-Voltage Switching (ZVS) and Zero-Current Switching (ZCS) Topologies",
            "yt_query": "resonant converters ZVS ZCS zero voltage zero current switching soft switching",
            "img_path": "images/pe/resonant_converters_zvs_zcs.png",
            "img_caption": "Figure 5.4: Hard vs Soft Switching Trajectories, ZCS Quasi-Resonant Switch, and ZVS Quasi-Resonant Switch",
            "answer": r"""
Conventional switched-mode power converters operate on the principle of **hard switching**, where power switches are forced to interrupt full load current under high terminal voltage.

### 1. Inherent Limitations of Hard Switching
1. **High Switching Losses:** During turn-on and turn-off transients, voltage and current cross over simultaneously over rise time $t_r$ and fall time $t_f$. The resulting switching power dissipation is proportional to switching frequency:
   $$P_{sw} = \frac{1}{2} V_s I_o (t_r + t_f) f_s$$
   As $f_s$ exceeds $100\text{ kHz}$, switching losses exceed conduction losses, dramatically lowering conversion efficiency.
2. **Capacitive Turn-on Loss:** The energy stored in the internal output capacitance of a MOSFET ($C_{oss}$) is dissipated internally as heat every time the switch turns on:
   $$P_{cap} = \frac{1}{2} C_{oss} V_{ds}^2 f_s$$
3. **Severe Electromagnetic Interference (EMI):** Abrupt voltage steps ($dv/dt > 10\text{ kV}/\mu\text{s}$) and current spikes ($di/dt > 1000\text{ A}/\mu\text{s}$) radiate high-frequency electromagnetic noise, polluting the power grid and nearby control circuitry.

### 2. Soft-Switching Principle
Soft-switching converters incorporate an auxiliary $L_r-C_r$ resonant tank that shapes the switch voltage or current into quasi-sinusoidal waveforms. Switching transitions are timed to occur exclusively when either switch current or switch voltage is identically zero.

```
   Hard Switching                  Zero-Current Switching (ZCS)    Zero-Voltage Switching (ZVS)
      v_sw, i_sw                      v_sw, i_sw                      v_sw, i_sw
        ▲                               ▲                               ▲
   v_sw ┼───┐                      v_sw ┼───┐                      v_sw ┼   /───\
        │   │\                          │   │                           │  /     \
   i_sw ┼   │ \                    i_sw ┼  /─\                     i_sw ┼─/───────\─
        └───┴──\───► Time               └──┴───┴───► Time               └──┴───────┴──► Time
            |  |                            Turn-off at i=0                 Turn-on at v=0
            Overlap Loss!                   Zero Turn-off Loss              Zero Turn-on Loss
```

### 3. Zero-Current Switching (ZCS) Quasi-Resonant Converter
- **Circuit Configuration:** A resonant inductor $L_r$ is placed in series with the switch, and a resonant capacitor $C_r$ is placed in parallel.
- **Operating Mechanism:**
  1. When the switch is turned on, the series inductor $L_r$ prevents instantaneous current rise ($di/dt = V_s / L_r$).
  2. The resonant tank ($L_r, C_r$) causes the switch current to oscillate sinusoidally:
     $$i_{sw}(t) = I_o + \frac{V_s}{Z_0}\sin\omega_0 t$$
     where characteristic impedance $Z_0 = \sqrt{L_r / C_r}$ and resonant frequency $\omega_0 = 1/\sqrt{L_r C_r}$.
  3. The switch current naturally rings down and crosses zero. The gate drive turns the switch off while current is zero ($i_{sw} = 0$).
- **Device Suitability:** Primarily utilized with **IGBTs and BJT switches**, because zero-current turn-off completely eliminates the collector tail-current switching loss.
- **Limitation:** At turn-on, $C_r$ discharges into the switch, dissipating capacitive energy. Switch current stress is elevated ($I_{sw,\max} = I_o + V_s / Z_0$).

### 4. Zero-Voltage Switching (ZVS) Quasi-Resonant Converter
- **Circuit Configuration:** A resonant capacitor $C_r$ is placed in direct parallel with the switch (absorbing the MOSFET's parasitic $C_{oss}$), and a resonant inductor $L_r$ is connected in series with the input line.
- **Operating Mechanism:**
  1. When the switch is opened, the parallel capacitor $C_r$ absorbs the current, limiting the rate of voltage rise ($dv/dt = I_o / C_r$) and eliminating turn-off overlap loss.
  2. The tank voltage oscillates through a sinusoidal pulse:
     $$v_{sw}(t) = V_s + I_o Z_0 \sin\omega_0 t$$
  3. When $v_{sw}(t)$ rings back down to zero, the antiparallel diode across the switch clamps the voltage to zero.
  4. The switch is turned on while the terminal voltage is zero ($v_{sw} = 0$).
- **Device Suitability:** Ideally suited for **Power MOSFETs**, because zero-voltage turn-on completely eliminates the $\frac{1}{2} C_{oss} V_{ds}^2 f_s$ capacitive discharge loss.
- **Operating Frequency:** Enables power converters to operate efficiently at frequencies from $500\text{ kHz}$ to well over $2\text{ MHz}$.
- **Limitation:** Voltage stress across the switch is high ($V_{sw,\max} = V_s + I_o Z_0 \approx 3\text{ to }4 \times V_s$).

### 5. Summary Comparison: ZCS vs ZVS

| Feature | Zero-Current Switching (ZCS) | Zero-Voltage Switching (ZVS) |
| :--- | :--- | :--- |
| **Switching Condition** | Turn-off at zero current ($i_{sw} = 0$) | Turn-on at zero voltage ($v_{sw} = 0$) |
| **Auxiliary Components**| Resonant $L_r$ in series with switch | Resonant $C_r$ in parallel with switch |
| **Eliminated Loss** | Turn-off tail loss & diode recovery | Capacitive turn-on discharge ($\frac{1}{2}CV^2$) |
| **Optimal Power Switch**| IGBT, BJT, GTO | Power MOSFET, GaN HEMT, SiC MOSFET |
| **Peak Device Stress** | High current stress ($I_{sw} > 2 I_o$) | High voltage stress ($V_{sw} > 3 V_s$) |
| **Switching Frequency** | Up to $200\text{ kHz}$ | High: $500\text{ kHz} - 5\text{ MHz}$ |
"""
        },
        {
            "qid": "pe-q25",
            "marks": 10,
            "type": "Topology Derivation & Comparison",
            "title": "Switched-Mode Power Supplies (SMPS): Isolated Topologies (Flyback, Forward, Push-Pull, Half-Bridge, and Full-Bridge)",
            "yt_query": "SMPS isolated topologies flyback forward push pull half bridge full bridge comparison",
            "img_path": "images/pe/smps_isolated_topologies.png",
            "img_caption": "Figure 5.5: Circuit Topologies of Isolated SMPS: Flyback, Forward, Push-Pull, and Half-Bridge Converters",
            "answer": r"""
Switched-Mode Power Supplies (SMPS) utilize high-frequency switching to achieve compact size, light weight, and high conversion efficiency. In utility-connected and safety-critical applications, galvanic electrical isolation between input and output is mandated, provided by high-frequency ferrite transformers.

### 1. Flyback Converter
The Flyback converter is derived from the buck-boost converter by replacing the inductor with a two-winding coupled inductor (flyback transformer with a gapped magnetic core).

```
       + ───o───[ Primary N_p ]───┬──────────────o +
                                  │
                                ┌─┴─┐ Switch S
                                │   │
                                └─┬─┘
       - ───o─────────────────────┴──────────────o -
                     : :
                     : :  Secondary N_s
              ┌──────: :──────►| Diode D ───┬────────o +
              │                             │
            [===]                         ┌─┴─┐
              │                           │ C │ [R] Load  V_o
              └───────────────────────────┴─┬─┘
                                            │
                                            o -
```

- **Operating Principle:**
  - **Switch ON ($0 < t \le D T_s$):** Diode $D$ is reverse-biased due to reversed winding dot convention. Input energy is stored purely in the air gap of the transformer core ($E = \frac{1}{2} L_m I_p^2$).
  - **Switch OFF ($D T_s < t \le T_s$):** Switch opens. Secondary winding voltage reverses polarity, forward-biasing diode $D$. Stored magnetic energy is transferred to output capacitor and load.
- **Voltage Transfer Ratio:**
  $$V_o = \frac{N_s}{N_p} \left(\frac{D}{1 - D}\right) V_s$$
- **Power Range:** Low power ($<150\text{ W}$, mobile phone chargers, auxiliary electronics).

### 2. Forward Converter
Derived from the buck converter, the Forward converter transfers energy directly to the load while the active switch is conducting (true transformer action).

- **Tertiary Demagnetizing Winding ($N_d$):**
  Because the transformer operates in one quadrant ($B > 0$), magnetizing current builds up during switch ON. A tertiary reset winding with a series diode returns this magnetizing energy back to the input DC bus during switch OFF, resetting core flux $\Phi$ to zero before the next cycle.
- **Maximum Duty Ratio Limit:**
  To guarantee complete core reset ($V_s D T_s = V_s \frac{N_p}{N_d} t_{reset}$):
  $$D_{\max} = \frac{1}{1 + \frac{N_d}{N_p}}$$
  For standard $N_d = N_p$, $D_{\max} = 0.5$ ($50\%$).
- **Voltage Transfer Ratio:**
  $$V_o = \frac{N_s}{N_p} D V_s$$
- **Power Range:** Medium power ($100\text{ to }300\text{ W}$, desktop computer power supplies).

### 3. Push-Pull Converter
- **Circuit:** Center-tapped primary and secondary windings with two switches ($S_1, S_2$) switching alternately in opposite half-cycles for duty cycle $D \le 0.5$.
- **Magnetic Operation:** The core is excited symmetrically in two quadrants ($+B_m$ and $-B_m$), doubling magnetic core utilization.
- **Susceptibility:** If switch conduction times differ by even fractions of a microsecond, a net DC magnetizing bias develops, pushing the transformer core into catastrophic magnetic saturation (**flux walking**). Requires current-mode control.
- **Voltage Transfer Ratio:**
  $$V_o = 2 \left(\frac{N_s}{N_p}\right) D V_s$$
- **Power Range:** $250\text{ W to }1000\text{ W}$ (automotive audio amplifiers, $12\text{ V}$ battery inverters).

### 4. Half-Bridge and Full-Bridge Converters
- **Half-Bridge Converter:**
  - Employs two series capacitors splitting the DC bus, applying $\pm V_s / 2$ across the primary.
  - A series DC blocking capacitor eliminates DC flux imbalance, completely preventing transformer core saturation.
  - Voltage transfer ratio:
    $$V_o = \left(\frac{N_s}{N_p}\right) D V_s$$
  - Power range: $500\text{ W to }2\text{ kW}$.
- **Full-Bridge Converter:**
  - Employs four switches in an H-bridge configuration.
  - Full DC bus voltage $V_s$ is applied across the primary, doubling power delivery for the same switch current rating.
  - Voltage transfer ratio:
    $$V_o = 2 \left(\frac{N_s}{N_p}\right) D V_s$$
  - Power range: High power ($>2\text{ kW to }50\text{ kW}$, EV charging stations, server power racks).

### 5. Comprehensive Comparative Matrix of Isolated SMPS Topologies

| Feature / Metric | Flyback | Forward | Push-Pull | Half-Bridge | Full-Bridge |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Power Capability** | $<150\text{ W}$ | $100 - 300\text{ W}$ | $250 - 1000\text{ W}$| $500 - 2000\text{ W}$| $>2000\text{ W}$ |
| **Number of Switches**| 1 | 1 | 2 (Low side) | 2 (Totem pole) | 4 (H-bridge) |
| **Voltage Stress ($V_{sw}$)**| $V_s + \frac{N_p}{N_s}V_o$ | $2 V_s$ | $2 V_s$ | $V_s$ | $V_s$ |
| **Core Utilization** | 1 Quadrant ($B > 0$) | 1 Quadrant ($B > 0$)| 2 Quadrants ($\pm B_m$) | 2 Quadrants ($\pm B_m$)| 2 Quadrants ($\pm B_m$) |
| **Output Filter Inductor**| Not required | Required | Required | Required | Required |
| **Core Reset Method** | Output diode | Tertiary winding | Symmetrical drive | Self-balancing cap | Symmetrical drive |
| **Cost & Complexity** | Lowest | Moderate | Moderate | High | Highest |
"""
        },
        {
            "qid": "pe-q26",
            "marks": 10,
            "type": "System Architecture & Performance Analysis",
            "title": "Uninterruptible Power Supplies (UPS): Architectures, Static Bypass Switch, and Performance Comparison",
            "yt_query": "uninterruptible power supplies UPS offline standby online double conversion line interactive comparison",
            "img_path": "images/pe/ups_architectures_comparison.png",
            "img_caption": "Figure 5.6: Functional Block Schematics of Offline (Standby), Line-Interactive, and Online Double-Conversion UPS",
            "answer": r"""
An Uninterruptible Power Supply (UPS) is an autonomous power conditioning and backup system engineered to maintain high-quality, uninterrupted electrical power to mission-critical loads (data centers, medical life support, telecommunication switches, industrial process controls) during utility grid failures and power disturbances.

### 1. Classification of UPS Architectures

#### A. Offline (Standby) UPS
- **Normal Operation:** Mains utility power feeds the critical load directly through a surge suppressor, an EMI filter, and a high-speed Static Transfer Switch (STS). A small battery charger maintains the battery bank in a fully charged float state. The inverter remains idle (OFF).
- **Outage Operation:** When mains voltage collapses or exceeds tolerable thresholds, the STS transfers the load from mains to the battery-powered inverter.
- **Transfer Time:** $4 \text{ to } 10\text{ ms}$.
- **Evaluation:** High operating efficiency ($>95\%$) and lowest cost; however, provides zero voltage regulation during normal operation, and the transfer delay can reboot sensitive electronic servers.

#### B. Line-Interactive UPS
- **Normal Operation:** Incorporates an Automatic Voltage Regulator (AVR) buck/boost tap-changing autotransformer. The AVR stabilizes grid voltage variations ($\pm 15\%$) without discharging the battery. The inverter is bidirectional: it operates in reverse as a battery charger during normal conditions.
- **Outage Operation:** The STS disconnects the utility grid, and the bidirectional inverter immediately reverses to supply power from the battery to the load.
- **Transfer Time:** $2 \text{ to } 4\text{ ms}$.
- **Evaluation:** Moderate cost, good voltage conditioning, widely deployed for commercial office workstations and branch servers.

#### C. Online Double-Conversion UPS
- **Architecture:** Consists of a rectifier/power factor correction (PFC) stage, a DC link battery bank, a continuous PWM inverter, and an antiparallel thyristor Static Bypass Switch.
- **Normal Operation:** Mains AC power is continuously converted to DC by the rectifier. The DC bus simultaneously charges the battery and powers the inverter. The inverter continuously synthesizes a pure sinusoidal AC voltage for the critical load:
$$\text{AC Mains} \longrightarrow \text{Rectifier (AC to DC)} \longrightarrow \text{Inverter (DC to AC)} \longrightarrow \text{Critical Load}$$
- **Outage Operation:** When mains power fails, the DC link is instantly sustained by the battery bank through a blocking diode. Because the inverter is already powering the load continuously:
$$\text{Transfer Time} = 0\text{ ms} \quad (\text{Zero Interruption})$$
- **Power Quality:** Complete galvanic and electronic isolation between AC grid and load. Immune to voltage sags, swells, brownouts, frequency variations, and harmonic distortion.

```
       AC Input ───►[ Rectifier / PFC ]───┬───►[ PWM Inverter ]───┬───► Critical Load
                                           │                       │
                                      [ Battery ]                  │ (Transfer < 1 ms)
                                                                   ▲
       Bypass AC Line ──────────────────[ Static Bypass Switch ]───┘
```

### 2. Static Bypass Switch Operation
The Static Bypass Switch consists of high-speed back-to-back thyristors (SCRs) connected in parallel between the raw AC utility line and the critical load.
- **Function:** Transfers the load to mains in less than $1\text{ ms}$ under three critical fault conditions:
  1. Internal failure or trip of the inverter.
  2. Severe output load short circuit (allowing utility fault clearing without damaging inverter IGBTs).
  3. Sustained load current overload (e.g. motor inrush currents exceeding $150\%$ of inverter rating).
- Once the fault is cleared, the static switch seamlessly commutates the load back to the online inverter.

### 3. Comprehensive Performance Comparison of UPS Types

| Technical Metric | Offline (Standby) | Line-Interactive | Online Double-Conversion |
| :--- | :--- | :--- | :--- |
| **Transfer Time** | $4 - 10\text{ ms}$ | $2 - 4\text{ ms}$ | **$0\text{ ms}$ (Zero)** |
| **Output Waveform** | Quasi-square / Stepped | Pure / Modified Sine | **Pure Sinusoid ($<2\%$ THD)** |
| **Voltage Conditioning**| None | Good (AVR Tap steps) | **Excellent ($\pm 1\%$ Regulated)** |
| **Frequency Regulation**| Tracks mains frequency | Tracks mains frequency | **Independent ($50.0 \pm 0.1\text{ Hz}$)** |
| **Harmonic Isolation** | Poor | Moderate | **Total (AC-DC-AC barrier)** |
| **Normal Efficiency** | $95 - 98\%$ | $93 - 97\%$ | $88 - 94\%$ (Eco mode: $97\%$) |
| **Component Stress** | Low (Inverter idle) | Moderate | Continuous (Inverter 100% duty)|
| **Capital Cost** | Lowest | Medium | High |
| **Target Application** | Desktop PCs, POS terminals| Small office networks | **Data Centers, ICUs, Airports** |
"""
        }
    ]
}
