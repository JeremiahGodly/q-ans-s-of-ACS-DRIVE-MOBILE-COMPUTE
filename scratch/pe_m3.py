# -*- coding: utf-8 -*-
"""
Module 3: DC-DC Converters (Choppers)
Subject: Power Electronics (EET306) - KTU 2019 Scheme S6 EEE
Questions: pe-q11 to pe-q15
"""

MODULE_3 = {
    "module_id": "pe-m3",
    "module_num": "Module 3",
    "module_title": "DC-DC Converters (Choppers)",
    "questions": [
        {
            "qid": "pe-q11",
            "marks": 10,
            "type": "Derivation & Circuit Analysis",
            "title": "Step-Down (Buck) Converter: Continuous Conduction Mode Analysis, Inductor Ripple, and Critical Filter Design",
            "yt_query": "buck converter derivation CCM volt second balance ripple current critical inductance",
            "img_path": "images/pe/buck_converter_ccm.png",
            "img_caption": "Figure 3.1: Step-Down (Buck) Converter Topology, Equivalent Sub-Circuits, and Steady-State Waveforms",
            "answer": r"""
The step-down (Buck) converter produces a regulated DC output voltage lower than its DC input voltage ($V_o \le V_s$). It consists of a controlled semiconductor switch $S$ (MOSFET or IGBT), a freewheeling diode $D$, a low-pass filter inductor $L$, and a filter capacitor $C$ feeding a load resistance $R$.

```
       + ───o───[ Switch S ]───┬───────[ Inductor L ]───┬────────o +
                               │                        │
                             ┌─┴─┐                    ┌─┴─┐
                             │ D │ Diode              │ C │ [R] Load  V_o
                             └─┬─┘                    └─┬─┘
                               │                        │
       - ───o──────────────────┴────────────────────────┴────────o -
```

### 1. Continuous Conduction Mode (CCM) Operation
In continuous conduction mode, the inductor current $i_L(t)$ flows continuously without reaching zero at any instant during the switching period $T_s = 1/f_s$.

- **Mode 1: Switch $S$ is ON ($0 < t \le D T_s$):**
  The switch conducts for duration $t_{on} = D T_s$, where $D = t_{on}/T_s$ is the duty ratio ($0 \le D \le 1$). Diode $D$ is reverse-biased with cathode at $V_s$.
  The voltage across inductor $L$ is:
  $$v_L(t) = V_s - V_o$$
  The inductor current rises linearly from its minimum value $I_1$ to its maximum value $I_2$:
  $$\frac{di_L}{dt} = \frac{V_s - V_o}{L} \implies \Delta I_L = I_2 - I_1 = \frac{V_s - V_o}{L} D T_s$$

- **Mode 2: Switch $S$ is OFF ($D T_s < t \le T_s$):**
  The switch is opened for duration $t_{off} = (1 - D)T_s$. The collapsing magnetic field in $L$ forces diode $D$ into forward conduction (freewheeling action).
  The voltage across inductor $L$ is clamped to:
  $$v_L(t) = -V_o$$
  The inductor current decays linearly from $I_2$ back to $I_1$:
  $$\frac{di_L}{dt} = -\frac{V_o}{L} \implies \Delta I_L = \frac{V_o}{L}(1 - D)T_s$$

### 2. Inductor Volt-Second Balance and Voltage Transfer Ratio
In periodic steady-state operation, the net change in inductor current over a complete switching cycle must be identically zero:
$$\Delta i_L = \frac{1}{L}\int_0^{T_s} v_L(t)\,dt = 0 \implies \int_0^{T_s} v_L(t)\,dt = 0$$

Substituting the piecewise inductor voltages:
$$(V_s - V_o) D T_s + (-V_o)(1 - D) T_s = 0$$
$$(V_s - V_o) D - V_o(1 - D) = 0$$
$$V_s D - V_o D - V_o + V_o D = 0 \implies V_o = D V_s$$

The DC voltage conversion ratio is:
$$M = \frac{V_o}{V_s} = D$$
Since $0 < D < 1$, the output voltage is always less than the input voltage ($V_o < V_s$).

### 3. Inductor Peak-to-Peak Ripple Current ($\Delta I_L$)
Substituting $V_o = D V_s$ and $T_s = 1/f_s$:
$$\Delta I_L = \frac{(V_s - V_o) D}{f_s L} = \frac{V_s(1 - D) D}{f_s L}$$
The maximum ripple current occurs at a duty ratio of $D = 0.5$:
$$\Delta I_{L,\max} = \frac{V_s}{4 f_s L}$$

### 4. Output Peak-to-Peak Ripple Voltage ($\Delta V_c$)
The capacitor current is $i_c(t) = i_L(t) - I_o$. Since the average capacitor current in steady state is zero, the DC load current is supplied entirely by the average inductor current ($I_L = I_o$).
The AC triangular ripple current flows through the filter capacitor. The total charge $\Delta Q$ accumulated on the capacitor during the positive half of the triangular ripple cycle is the area of the upper triangular region (base $T_s / 2$ and height $\Delta I_L / 2$):
$$\Delta Q = \frac{1}{2} \left(\frac{T_s}{2}\right) \left(\frac{\Delta I_L}{2}\right) = \frac{T_s \Delta I_L}{8} = \frac{\Delta I_L}{8 f_s}$$

The resulting output ripple voltage is:
$$\Delta V_c = \frac{\Delta Q}{C} = \frac{\Delta I_L}{8 f_s C} = \frac{V_s D(1 - D)}{8 f_s^2 L C}$$
Expressing as a normalized voltage ripple fraction:
$$\frac{\Delta V_o}{V_o} = \frac{1 - D}{8 f_s^2 L C}$$

### 5. Critical Inductance ($L_c$) and Critical Capacitance ($C_c$)
At the boundary between Continuous Conduction Mode (CCM) and Discontinuous Conduction Mode (DCM), the minimum inductor current just touches zero ($I_{1} = 0$):
$$I_{L\min} = I_L - \frac{\Delta I_L}{2} = 0 \implies I_L = \frac{\Delta I_L}{2}$$

Since $I_L = I_o = \frac{V_o}{R} = \frac{D V_s}{R}$:
$$\frac{D V_s}{R} = \frac{V_s D(1 - D)}{2 f_s L_c}$$
Solving for the critical inductance $L_c$:
$$L_c = \frac{(1 - D) R}{2 f_s}$$
To ensure continuous conduction under all duty cycle conditions down to minimum load, the filter inductance must satisfy:
$$L \ge L_{c,\max} = \frac{R_{\max}}{2 f_s} \quad (\text{as } D \to 0)$$

The critical filter capacitance required to maintain ripple voltage below a target specification $\frac{\Delta V_o}{V_o}$ is:
$$C_c = \frac{1 - D}{8 f_s^2 L \left(\frac{\Delta V_o}{V_o}\right)}$$
"""
        },
        {
            "qid": "pe-q12",
            "marks": 10,
            "type": "Derivation & Analytical",
            "title": "Step-Up (Boost) Converter: Operation, Volt-Second Balance, Ripple Calculations, and Critical Parameters",
            "yt_query": "boost converter derivation CCM ripple current voltage volt second balance",
            "img_path": "images/pe/boost_converter_ccm.png",
            "img_caption": "Figure 3.2: Step-Up (Boost) Converter Circuit Diagram, Operational Modes, and Inductor Current/Capacitor Voltage Waveforms",
            "answer": r"""
The step-up (Boost) converter converts a lower DC input voltage $V_s$ to a higher stabilized DC output voltage $V_o$ ($V_o \ge V_s$). It is widely utilized in photovoltaic maximum power point trackers, power factor correction (PFC) pre-regulators, and electric vehicle battery boost stages.

```
       + ───o───[ Inductor L ]───┬───►| Diode D ───┬────────o +
                                 │                 │
                           ┌─────┴─────┐         ┌─┴─┐
                           │ Switch S  │         │ C │ [R] Load  V_o
                           └─────┬─────┘         └─┬─┘
                                 │                 │
       - ───o────────────────────┴─────────────────┴────────o -
```

### 1. Operating Modes in Continuous Conduction Mode (CCM)
- **Mode 1: Switch $S$ is ON ($0 < t \le D T_s$):**
  Switch $S$ is closed for duration $D T_s$. The diode $D$ is reverse-biased because its cathode is held at output voltage $V_o$ while anode is at ground potential ($v_D = -V_o$).
  The inductor is placed directly across the DC source:
  $$v_L(t) = V_s$$
  Inductor current increases linearly from $I_1$ to $I_2$:
  $$\frac{di_L}{dt} = \frac{V_s}{L} \implies \Delta I_L = \frac{V_s}{L} D T_s$$
  During this interval, the load resistance $R$ is isolated from the source and is powered solely by the discharging output capacitor $C$.

- **Mode 2: Switch $S$ is OFF ($D T_s < t \le T_s$):**
  Switch $S$ is opened for duration $(1 - D)T_s$. The collapsing magnetic field induces a positive voltage across the inductor ($v_L = L \frac{di}{dt}$), which adds in series with the input voltage, forward-biasing diode $D$.
  The inductor voltage is:
  $$v_L(t) = V_s - V_o$$
  Since $V_o > V_s$, $v_L(t)$ is negative, and the inductor current decreases linearly from $I_2$ to $I_1$:
  $$\frac{di_L}{dt} = \frac{V_s - V_o}{L} \implies \Delta I_L = \frac{V_o - V_s}{L}(1 - D)T_s$$
  During this mode, energy is transferred simultaneously from both the DC source and the discharging inductor into capacitor $C$ and load $R$.

### 2. Inductor Volt-Second Balance and Voltage Transfer Ratio
Under steady-state periodic operation, the average voltage across the inductor over one full switching period must be zero:
$$\int_0^{T_s} v_L(t)\,dt = 0$$

$$V_s (D T_s) + (V_s - V_o)(1 - D) T_s = 0$$
$$V_s D + V_s - V_o - V_s D + V_o D = 0$$
$$V_s - V_o(1 - D) = 0 \implies V_o = \frac{V_s}{1 - D}$$

The voltage gain is:
$$M = \frac{V_o}{V_s} = \frac{1}{1 - D}$$
Since $0 \le D < 1$, the denominator $(1 - D) \le 1$, meaning $V_o \ge V_s$ under all operating conditions (Step-Up Converter).

### 3. Ripple Formulations

#### A. Inductor Peak-to-Peak Ripple Current ($\Delta I_L$)
$$\Delta I_L = \frac{V_s D T_s}{L} = \frac{V_s D}{f_s L}$$

#### B. Output Peak-to-Peak Ripple Voltage ($\Delta V_c$)
Unlike the buck converter where inductor current directly feeds the capacitor, in a boost converter the diode current is discontinuous (pulsating).
During Mode 1 ($0 < t \le D T_s$), the diode is off and the capacitor must supply the entire continuous DC load current $I_o = V_o / R$.
The total charge lost by the capacitor during this switch-on interval is:
$$\Delta Q = I_o \cdot t_{on} = I_o (D T_s) = \frac{V_o D}{R f_s}$$

The peak-to-peak output voltage ripple is therefore:
$$\Delta V_c = \frac{\Delta Q}{C} = \frac{V_o D}{R f_s C}$$
Expressed as a fractional ripple:
$$\frac{\Delta V_o}{V_o} = \frac{D}{R f_s C}$$

### 4. Critical Inductance ($L_c$) for Continuous Conduction
At the boundary between CCM and DCM:
$$I_L = \frac{\Delta I_L}{2}$$

Assuming an ideal lossless converter ($P_{in} = P_{out} \implies V_s I_L = V_o I_o$):
$$I_L = \frac{V_o}{V_s} I_o = \frac{1}{1 - D} I_o = \frac{V_o}{R(1 - D)} = \frac{V_s}{R(1 - D)^2}$$

Equating average inductor current to half the ripple current:
$$\frac{V_s}{R(1 - D)^2} = \frac{V_s D}{2 f_s L_c}$$
Solving for critical inductance $L_c$:
$$L_c = \frac{D(1 - D)^2 R}{2 f_s}$$

To find the worst-case maximum value of $L_c$, differentiate with respect to $D$:
$$\frac{d}{dD}\left[ D(1 - D)^2 \right] = (1 - D)^2 - 2D(1 - D) = (1 - D)(1 - 3D) = 0 \implies D = \frac{1}{3}$$
$$L_{c,\max} = \frac{\left(\frac{1}{3}\right)\left(\frac{2}{3}\right)^2 R}{2 f_s} = \frac{4 R}{54 f_s} = \frac{2 R}{27 f_s}$$

### 5. Effect of Parasitic Internal Resistance on Maximum Practical Gain
In a real inductor with winding resistance $r_L$, the actual voltage transfer ratio is:
$$\frac{V_o}{V_s} = \frac{1}{1 - D} \left[ \frac{1}{1 + \frac{r_L}{R(1 - D)^2}} \right]$$
As $D \to 1$, the term $\frac{r_L}{R(1 - D)^2}$ grows astronomically, causing the actual gain to plummet toward zero instead of rising toward infinity. Practical boost converters are limited to duty cycles $D \le 0.85$ and voltage gains of $M \le 4\text{ to }5$.
"""
        },
        {
            "qid": "pe-q13",
            "marks": 10,
            "type": "Derivation & Analysis",
            "title": "Buck-Boost Converter: Inverting Voltage Ratio, Ripple Formulations, and Boundary Conduction Mode",
            "yt_query": "buck boost converter derivation inverting voltage ratio CCM DCM critical inductance",
            "img_path": "images/pe/buck_boost_converter.png",
            "img_caption": "Figure 3.3: Inverting Buck-Boost Converter Circuit Topology, Energy Storage Cycles, and Steady-State Waveforms",
            "answer": r"""
The Buck-Boost converter is a DC-DC converter topology capable of producing a regulated DC output voltage whose magnitude can be either greater than, equal to, or less than the DC input voltage magnitude. The output voltage exhibits an inherent polarity inversion relative to the input.

```
       + ───o───[ Switch S ]───┬───|◄── Diode D ───┬────────o -
                               │                   │
                             ┌─┴─┐               ┌─┴─┐
                             │ L │ Inductor      │ C │ [R] Load  V_o
                             └─┬─┘               └─┬─┘
                               │                   │
       - ───o──────────────────┴───────────────────┴────────o +
```

### 1. Operational Modes in Continuous Conduction Mode (CCM)

- **Mode 1: Switch $S$ is ON ($0 < t \le D T_s$):**
  Switch $S$ is closed. The diode $D$ is reverse-biased because its cathode is held at $+V_s$ while its anode is at the negative load potential ($v_D = -(V_s + |V_o|)$).
  The input source is connected directly across inductor $L$:
  $$v_L(t) = V_s$$
  Inductor current increases linearly from $I_1$ to $I_2$:
  $$\frac{di_L}{dt} = \frac{V_s}{L} \implies \Delta I_L = \frac{V_s}{L} D T_s$$
  Energy is absorbed from the DC source and stored in the magnetic field of inductor $L$. The load is isolated and sustained entirely by capacitor $C$.

- **Mode 2: Switch $S$ is OFF ($D T_s < t \le T_s$):**
  Switch $S$ is opened. The inductor current cannot stop instantaneously. The collapsing magnetic field reverses the polarity of the voltage induced across inductor $L$ (terminal at diode becomes positive relative to ground), forward-biasing diode $D$.
  The inductor discharges its stored energy directly into the parallel combination of capacitor $C$ and load $R$:
  $$v_L(t) = -V_o$$
  Inductor current decays linearly from $I_2$ back to $I_1$:
  $$\frac{di_L}{dt} = -\frac{V_o}{L} \implies \Delta I_L = \frac{V_o}{L}(1 - D)T_s$$

### 2. Inductor Volt-Second Balance and Voltage Transfer Ratio
Applying Faraday's law of induction over one complete switching period in steady state:
$$\int_0^{T_s} v_L(t)\,dt = 0$$

$$V_s (D T_s) + (-V_o)(1 - D) T_s = 0$$
$$V_s D - V_o(1 - D) = 0 \implies V_o = \frac{D}{1 - D} V_s$$

Accounting for the opposite reference polarity (negative with respect to common ground):
$$V_o = -\frac{D}{1 - D} V_s$$

- **Operational Regions:**
  1. **Buck Region ($0 < D < 0.5$):**
     $$\frac{D}{1 - D} < 1 \implies |V_o| < V_s$$
  2. **Boost Region ($0.5 < D < 1$):**
     $$\frac{D}{1 - D} > 1 \implies |V_o| > V_s$$
  3. **Unity Gain ($D = 0.5$):**
     $$\frac{D}{1 - D} = 1 \implies |V_o| = V_s$$

### 3. Ripple Current and Ripple Voltage Formulations

#### A. Inductor Peak-to-Peak Ripple Current ($\Delta I_L$)
$$\Delta I_L = \frac{V_s D}{f_s L}$$

#### B. Output Peak-to-Peak Ripple Voltage ($\Delta V_c$)
During Mode 1 ($0 < t \le D T_s$), the diode is reverse-biased, and capacitor $C$ supplies the entire load current $I_o = V_o / R$.
The total charge extracted from the capacitor is:
$$\Delta Q = I_o (D T_s) = \frac{V_o D}{R f_s}$$
The resulting output voltage ripple is:
$$\Delta V_c = \frac{\Delta Q}{C} = \frac{V_o D}{R f_s C} \implies \frac{\Delta V_o}{V_o} = \frac{D}{R f_s C}$$

### 4. Critical Boundary Inductance ($L_c$) for CCM
At the CCM/DCM boundary condition:
$$I_L = \frac{\Delta I_L}{2}$$

From power balance ($P_{in} = P_{out} \implies V_s I_{in} = V_o I_o$):
The average input current is $I_{in} = D I_L$, and average diode current is $I_D = (1 - D)I_L = I_o$.
Therefore, the average inductor current is:
$$I_L = \frac{I_o}{1 - D} = \frac{V_o}{R(1 - D)}$$

Substituting $V_o = \frac{D}{1 - D} V_s$:
$$I_L = \frac{\frac{D}{1 - D} V_s}{R(1 - D)} = \frac{D V_s}{R(1 - D)^2}$$

Equating to half the ripple current:
$$\frac{D V_s}{R(1 - D)^2} = \frac{V_s D}{2 f_s L_c}$$
Cancelling $D V_s$ from both sides:
$$L_c = \frac{(1 - D)^2 R}{2 f_s}$$

To ensure CCM across all operating duty cycles up to $D \to 0$:
$$L \ge L_{c,\max} = \frac{R_{\max}}{2 f_s}$$
"""
        },
        {
            "qid": "pe-q14",
            "marks": 10,
            "type": "Topology Analysis & Derivation",
            "title": "Cuk Converter: Circuit Topology, Capacitive Energy Transfer, and Continuous Input/Output Currents",
            "yt_query": "Cuk converter derivation circuit operation capacitive energy transfer ripple current",
            "img_path": "images/pe/cuk_converter_topology.png",
            "img_caption": "Figure 3.4: Cuk Converter Circuit with Dual Inductors and Intermediate Coupling Capacitor",
            "answer": r"""
The Ćuk converter, developed by Slobodan Ćuk at Caltech, is an advanced DC-DC converter topology capable of both step-down and step-up voltage conversion with inverting output polarity.

Unlike the conventional Buck, Boost, and Buck-Boost converters that store and transfer energy inductively via magnetic flux in an inductor, the Ćuk converter utilizes an intermediate coupling capacitor ($C_1$) as the primary energy storage and transfer element.

```
       + ──[ L_1 ]───┬───────[ C_1 ]───────┬───[ L_2 ]───┬────────o -
                     │                     │             │
               ┌─────┴─────┐             ┌─┴─┐         ┌─┴─┐
               │ Switch S  │             │ D │ Diode   │ C_2│ [R] Load V_o
               └─────┬─────┘             └─┬─┘         └─┬─┘
                     │                     │             │
       - ────────────┴─────────────────────┴─────────────┴────────o +
```

### 1. Outstanding Advantages over Conventional Converters
1. **Continuous Input Current:** Inductor $L_1$ is in series with the input DC source, preventing pulsating current spikes.
2. **Continuous Output Current:** Inductor $L_2$ is in series with the output load, resulting in virtually ripple-free output current.
3. **Low EMI Signature:** Pulsating currents are eliminated at both input and output terminals, drastically downsizing external electromagnetic interference (EMI) filtering requirements.

### 2. Operating Modes in Continuous Conduction Mode (CCM)

- **Mode 1: Switch $S$ is ON ($0 < t \le D T_s$):**
  Switch $S$ is closed. The diode $D$ is reverse-biased by the positive charge on coupling capacitor $C_1$ ($v_D = -V_{C1}$).
  1. Inductor $L_1$ is connected directly across the DC source:
     $$v_{L1}(t) = V_s \implies \frac{di_{L1}}{dt} = \frac{V_s}{L_1}$$
  2. Coupling capacitor $C_1$ discharges its energy into the output circuit through switch $S$, feeding inductor $L_2$, output capacitor $C_2$, and load $R$:
     $$v_{L2}(t) = -(V_{C1} + V_o) \implies \frac{di_{L2}}{dt} = -\frac{V_{C1} + V_o}{L_2}$$

- **Mode 2: Switch $S$ is OFF ($D T_s < t \le T_s$):**
  Switch $S$ is opened. Inductor currents $i_{L1}$ and $i_{L2}$ force diode $D$ into forward conduction.
  1. Inductor $L_1$ charges coupling capacitor $C_1$ through diode $D$:
     $$v_{L1}(t) = V_s - V_{C1} \implies \frac{di_{L1}}{dt} = \frac{V_s - V_{C1}}{L_1}$$
  2. Inductor $L_2$ discharges its stored magnetic energy through diode $D$ into the output stage:
     $$v_{L2}(t) = -V_o \implies \frac{di_{L2}}{dt} = -\frac{V_o}{L_2}$$

### 3. Inductor Volt-Second Balance and Derivation of Voltage Gain
Applying volt-second balance across input inductor $L_1$:
$$\int_0^{T_s} v_{L1}(t)\,dt = 0 \implies V_s (D T_s) + (V_s - V_{C1})(1 - D) T_s = 0$$
$$V_s D + V_s - V_{C1} - V_s D + V_{C1} D = 0 \implies V_{C1}(1 - D) = V_s$$
$$V_{C1} = \frac{V_s}{1 - D}$$

Applying volt-second balance across output inductor $L_2$:
$$\int_0^{T_s} v_{L2}(t)\,dt = 0 \implies -(V_{C1} + V_o) D T_s + (-V_o)(1 - D) T_s = 0$$
$$-V_{C1} D - V_o D - V_o + V_o D = 0 \implies V_o = -D V_{C1}$$

Substituting the expression for $V_{C1}$:
$$V_o = -D \left(\frac{V_s}{1 - D}\right) = -\frac{D}{1 - D} V_s$$

The magnitude relationship is identical to the Buck-Boost converter:
- $|V_o| < V_s$ for $D < 0.5$ (Step-down)
- $|V_o| > V_s$ for $D > 0.5$ (Step-up)
- Output voltage is inverted in polarity.

### 4. Ripple Formulations
- **Input Inductor Ripple Current ($\Delta I_{L1}$):**
  $$\Delta I_{L1} = \frac{V_s D}{f_s L_1}$$
- **Output Inductor Ripple Current ($\Delta I_{L2}$):**
  $$\Delta I_{L2} = \frac{V_s D}{f_s L_2}$$
- **Coupling Capacitor Ripple Voltage ($\Delta V_{C1}$):**
  During switch OFF, capacitor $C_1$ is charged by current $I_{s}$:
  $$\Delta V_{C1} = \frac{I_s (1 - D) T_s}{C_1} = \frac{I_s (1 - D)}{f_s C_1} = \frac{I_o D}{f_s C_1}$$
- **Output Capacitor Ripple Voltage ($\Delta V_{C2}$):**
  Since $L_2$ provides continuous current, output ripple voltage follows the second-order filter formulation of the buck converter:
  $$\Delta V_{C2} = \frac{\Delta I_{L2}}{8 f_s C_2} = \frac{V_s D}{8 f_s^2 L_2 C_2}$$
"""
        },
        {
            "qid": "pe-q15",
            "marks": 10,
            "type": "Classification & Quadrant Analysis",
            "title": "Classification of Choppers: Class A, B, C, D, and E (Quadrant Operation, Circuits, and Applications)",
            "yt_query": "classification of choppers class A B C D E four quadrant chopper operation",
            "img_path": "images/pe/chopper_classification_quadrants.png",
            "img_caption": "Figure 3.5: Quadrant Operation of DC Choppers: Class A, B, C, D, and E H-Bridge Configurations",
            "answer": r"""
DC choppers (DC-DC electronic converters) are classified into five distinct categories based on the direction of output voltage $V_o$ and output current $I_o$ on the Cartesian $(V_o, I_o)$ plane.

```
                         V_o (Output Voltage)
                                  ▲
                                  │
         Quadrant II              │         Quadrant I
     Forward Regeneration         │      Forward Motoring
         (Class B)                │      (Class A, C, E)
       V_o > 0, I_o < 0           │      V_o > 0, I_o > 0
                                  │
   ───────────────────────────────┼───────────────────────────────► I_o (Current)
                                  │
         Quadrant III             │         Quadrant IV
       Reverse Motoring           │     Reverse Regeneration
          (Class E)               │        (Class D, E)
       V_o < 0, I_o < 0           │      V_o < 0, I_o > 0
                                  │
                                  ▼
```

### 1. Class A Chopper (First-Quadrant Chopper)
- **Circuit:** A single active switch $S_1$ connected in series with the positive DC rail, and a freewheeling diode $D_1$ connected in parallel across the inductive load.
- **Operation:**
  - When $S_1$ is ON: $v_o = V_s$ and $i_o$ flows from source to load ($V_o > 0, I_o > 0$).
  - When $S_1$ is OFF: $v_o = 0$ and $i_o$ freewheels through diode $D_1$.
- **Operating Plane:** Exclusively Quadrant I ($V_o > 0, I_o > 0$).
- **Power Flow:** Strictly unidirectional from source to load.
- **Application:** Forward speed control of DC motors, step-down power supplies.

### 2. Class B Chopper (Second-Quadrant Chopper)
- **Circuit:** Active switch $S_1$ connected in parallel across the load, and diode $D_1$ connected in series with the supply. The load must contain an active DC electromotive force $E$ (such as a battery or back EMF of a rotating machine).
- **Operation:**
  - When $S_1$ is ON: Load inductor stores energy from EMF $E$ ($i_o$ flows into switch, which is negative with respect to reference direction).
  - When $S_1$ is OFF: The collapsing inductor voltage ($L \frac{di}{dt}$) adds to $E$, elevating node voltage above $V_s$ ($E + L \frac{di}{dt} > V_s$). Diode $D_1$ is forced into conduction, returning energy into source $V_s$.
- **Operating Plane:** Exclusively Quadrant II ($V_o > 0, I_o < 0$).
- **Power Flow:** Power flows from load back into DC source.
- **Application:** Regenerative braking of DC motors.

### 3. Class C Chopper (Two-Quadrant Type-A Chopper)
- **Circuit:** Formed by connecting a Class A chopper and a Class B chopper in parallel across a common load. Consists of two switches ($S_1, S_2$) and two antiparallel diodes ($D_1, D_2$).
- **Operation:**
  - $S_1$ and $S_2$ are operated complementarily; they are never turned on simultaneously to prevent DC bus short circuit (shoot-through).
  - When $S_1$ conducts: $v_o = V_s, i_o > 0$ (Quadrant I).
  - When $S_1$ is turned off, $i_o$ freewheels through $D_2$: $v_o = 0, i_o > 0$ (Quadrant I).
  - When $S_2$ is turned on: $v_o = 0, i_o < 0$ (energy stored from load EMF).
  - When $S_2$ is turned off, current feeds back through $D_1$ into source: $v_o = V_s, i_o < 0$ (Quadrant II).
- **Operating Plane:** Quadrants I and II ($V_o > 0, I_o \gtrless 0$).
- **Application:** Reversible DC motor drives with regenerative braking capabilities.

### 4. Class D Chopper (Two-Quadrant Type-B Chopper)
- **Circuit:** Consists of two switches ($S_1, S_2$) and two diodes ($D_1, D_2$). Switch $S_1$ is on positive rail, switch $S_2$ is on negative rail; diodes $D_1$ and $D_2$ are placed diagonally.
- **Operation:**
  - Both switches $S_1$ and $S_2$ are turned ON simultaneously: $v_o = +V_s$ and current $i_o > 0$ flows from source to load (Quadrant I).
  - Both switches $S_1$ and $S_2$ are turned OFF simultaneously: Inductive load current cannot stop, forcing both diodes $D_1$ and $D_2$ into conduction. The load terminals are clamped across the DC source in reverse: $v_o = -V_s$ while $i_o$ continues in positive direction ($i_o > 0$) (Quadrant IV).
- **Average Voltage:**
  $$V_o = D V_s + (-V_s)(1 - D) = (2D - 1) V_s$$
  - $V_o > 0$ for $D > 0.5$ (Quadrant I)
  - $V_o < 0$ for $D < 0.5$ (Quadrant IV)
- **Operating Plane:** Quadrants I and IV ($V_o \gtrless 0, I_o > 0$).
- **Application:** Fast de-energization of highly inductive magnetic coils, DC motor field winding reversal.

### 5. Class E Chopper (Four-Quadrant Chopper / Full H-Bridge)
- **Circuit:** Full bridge topology comprising four switches ($S_1, S_2, S_3, S_4$) and four antiparallel diodes ($D_1, D_2, D_3, D_4$).

```
       + ────────┬───────────────────┬────────o +
                 │                   │
               ┌─┴─┐               ┌─┴─┐
               │S1 │               │S3 │
               └─┬─┘               └─┬─┘
                 ├───[ D1 ]          ├───[ D3 ]
                 │                   │
                 o──────[ Load ]─────o
                 │                   │
                 ├───[ D2 ]          ├───[ D4 ]
               ┌─┴─┐               ┌─┴─┐
               │S2 │               │S4 │
               └─┬─┘               └─┬─┘
                 │                   │
       - ────────┴───────────────────┴────────o -
```

- **Switching Combinations across all Four Quadrants:**
  1. **Quadrant I (Forward Motoring: $V_o > 0, I_o > 0$):**
     $S_4$ remains closed continuously while $S_1$ is chopped at frequency $f_s$. When $S_1$ is ON, $v_o = V_s, i_o > 0$. When $S_1$ is OFF, current freewheels through $S_4$ and $D_2$.
  2. **Quadrant II (Forward Regeneration: $V_o > 0, I_o < 0$):**
     $S_2$ is chopped while other switches remain open. When $S_2$ is ON, reverse current builds up in inductor. When $S_2$ turns off, current feeds back through $D_1$ and $D_4$ into source $V_s$.
  3. **Quadrant III (Reverse Motoring: $V_o < 0, I_o < 0$):**
     $S_2$ remains closed continuously while $S_3$ is chopped. When $S_3$ is ON, $v_o = -V_s, i_o < 0$. When $S_3$ turns off, current freewheels through $S_2$ and $D_4$.
  4. **Quadrant IV (Reverse Regeneration: $V_o < 0, I_o > 0$):**
     $S_4$ is chopped while other switches are open. Inductor current builds through $S_4$, then discharges back into DC supply through $D_2$ and $D_3$.
- **Application:** Complete four-quadrant bidirectional industrial servo drives, electric vehicle powertrains, robotics manipulators.
"""
        }
    ]
}
