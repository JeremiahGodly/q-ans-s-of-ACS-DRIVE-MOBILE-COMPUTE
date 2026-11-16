# -*- coding: utf-8 -*-
"""
Content generator for Subject 7: Power Electronics (EET306)
KTU 2019 Scheme Electrical & Electronics Engineering S6 Question Bank.
All answers are written from the perspective of an experienced engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings to prevent LaTeX backslash corruption.
Exports: PE_MODULES, PE_BYHEART, PE_EXAM_QUESTIONS
"""

PE_MODULES = [
    {
        "module_id": "pe-m1",
        "module_num": "Module 1",
        "module_title": "Power Semiconductor Devices",
        "questions": [
            {
                "qid": "pe-q1",
                "marks": 10,
                "type": "Theory & Analytical",
                "title": "Silicon Controlled Rectifier (SCR): Structure, Static V-I Characteristics, and Two-Transistor Analogy",
                "yt_query": "SCR structure static VI characteristics two transistor analogy derivation",
                "img_path": "images/pe/scr_characteristics_two_transistor.png",
                "img_caption": "Figure 1.1: Physical Structure, Static V-I Characteristics, and Two-Transistor Analogy of Silicon Controlled Rectifier (SCR)",
                "answer": r"""
The Silicon Controlled Rectifier (SCR) is a four-layer, three-junction ($p_1-n_1-p_2-n_2$) semiconductor switching device possessing three external terminals: Anode ($A$), Cathode ($K$), and Gate ($G$). It is a unidirectional, bistable switch capable of handling high voltages (up to several kilovolts) and large currents (up to several kiloamperes).

### 1. Physical Structure and Operating States
The device consists of four alternating semiconductor layers forming three distinct $p-n$ junctions denoted as $J_1$, $J_2$, and $J_3$ from anode to cathode:
- **Junction $J_1$:** Formed between outer $p_1$ layer (Anode) and lightly doped inner $n_1$ layer (drift region).
- **Junction $J_2$:** Formed between inner $n_1$ layer and moderately doped inner $p_2$ layer (Gate).
- **Junction $J_3$:** Formed between inner $p_2$ layer and heavily doped outer $n_2$ layer (Cathode).

The static $V-I$ characteristics of an SCR exhibit three distinct operating regions:
1. **Reverse Blocking Mode ($V_{AK} < 0$, $I_g = 0$):**
   When the anode is made negative with respect to the cathode, junctions $J_1$ and $J_3$ are reverse-biased while junction $J_2$ is forward-biased. The device behaves as two reverse-biased diodes in series. Only a small reverse leakage current flows until the applied voltage reaches the reverse breakdown voltage ($V_{BR}$). Beyond $V_{BR}$, avalanche breakdown occurs at $J_1$ and $J_3$, leading to destructive thermal runaway if current is not externally limited.
2. **Forward Blocking Mode ($V_{AK} > 0$, $I_g = 0$):**
   When the anode is made positive with respect to the cathode, outer junctions $J_1$ and $J_3$ are forward-biased, but the central junction $J_2$ is reverse-biased. A wide depletion region forms across $J_2$, blocking the flow of forward current except for a negligible forward leakage current. The SCR acts as an open switch. If forward voltage is increased to the forward breakover voltage ($V_{BO}$), avalanche breakdown of $J_2$ occurs, causing the device to switch into conduction.
3. **Forward Conduction Mode ($V_{AK} > 0$, $I_g > 0$):**
   When a positive gate current pulse is applied while $V_{AK} > 0$, junction $J_2$ breaks down at a forward voltage well below $V_{BO}$. All three junctions ($J_1, J_2, J_3$) become forward-biased, and the device transitions into a high-conduction state. The voltage drop across the conducting SCR collapses to a low value ($V_{on} \approx 1.0\text{ to }1.5\text{ V}$), and the forward current is governed entirely by the external load impedance.

```
                  Anode (A)
                     │
               ┌─────┴─────┐
            p1 │   Anode   │ Junction J1 (Forward biased)
               ├───────────┤
            n1 │ Drift (W) │ Junction J2 (Reverse biased in blocking)
         G ────┤   Base    │
            p2 │   Gate    │ Junction J3 (Forward biased)
               ├───────────┤
            n2 │  Cathode  │
               └─────┬─────┘
                     │
                 Cathode (K)
```

### 2. Definition of Latching Current and Holding Current
- **Latching Current ($I_L$):** The minimum anode current that the SCR must attain during the turn-on process before the gate trigger signal can be safely removed, such that the SCR remains latched in the forward conduction mode. If the anode current does not reach $I_L$, the device reverts to the forward blocking state upon removal of the gate pulse.
- **Holding Current ($I_H$):** The minimum anode current below which the SCR drops out of forward conduction and reverts back to the forward blocking state during the turn-off process.
- **Relationship:** For any given thyristor, $I_L > I_H$, typically related by:
$$I_L \approx 2 \text{ to } 3 \times I_H$$

### 3. Two-Transistor Analogy and Mathematical Derivation
The regenerative switching mechanism of an SCR is explained by slicing the four-layer structure vertically into two interconnected complementary transistors:
- A $p_1-n_1-p_2$ transistor representing a PNP transistor ($Q_1$).
- An $n_1-p_2-n_2$ transistor representing an NPN transistor ($Q_2$).

```
            Anode (I_A)
               │
            ┌──┴──┐
            │ Q1  │ (PNP)
            │     ├──┐ I_C1
            └──┬──┘  │
          I_B1 │     │
               │  ┌──▼──┐
               ├──┤ Q2  │ (NPN)
         I_g ──┴─►│     │
                  └──┬──┘
                     │
                Cathode (I_K = I_A + I_g)
```

From transistor junction theory, the collector current $I_C$ of a bipolar junction transistor is expressed as:
$$I_C = \alpha I_E + I_{CBO}$$
where $\alpha$ is the common-base current gain, $I_E$ is the emitter current, and $I_{CBO}$ is the collector-to-base leakage current with emitter open.

For transistor $Q_1$ (PNP):
- Emitter current: $I_{E1} = I_A$
- Collector current:
$$I_{C1} = \alpha_1 I_A + I_{CBO1}$$

For transistor $Q_2$ (NPN):
- Emitter current: $I_{E2} = I_K = I_A + I_g$
- Collector current:
$$I_{C2} = \alpha_2 I_K + I_{CBO2} = \alpha_2 (I_A + I_g) + I_{CBO2}$$

From Kirchhoff's Current Law applied at the central junction plane, the total anode current entering the device must equal the sum of the two collector currents:
$$I_A = I_{C1} + I_{C2}$$

Substituting the expressions for $I_{C1}$ and $I_{C2}$:
$$I_A = \left(\alpha_1 I_A + I_{CBO1}\right) + \left(\alpha_2 (I_A + I_g) + I_{CBO2}\right)$$

Expanding and collecting the terms containing $I_A$:
$$I_A = (\alpha_1 + \alpha_2) I_A + \alpha_2 I_g + I_{CBO1} + I_{CBO2}$$
$$I_A \left[1 - (\alpha_1 + \alpha_2)\right] = \alpha_2 I_g + I_{CBO1} + I_{CBO2}$$

Solving explicitly for the anode current $I_A$:
$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}$$

### 4. Regenerative Latching Mechanism
In the forward blocking state without gate current ($I_g = 0$), the current gains $\alpha_1$ and $\alpha_2$ are very small ($\alpha_1 + \alpha_2 \ll 1$) because of the low emitter currents. Consequently, $I_A$ is limited to the tiny leakage current:
$$I_A \approx \frac{I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)} \approx \text{few milliamperes}$$

When a positive gate current $I_g$ is injected into the base of $Q_2$:
1. $I_{C2}$ increases, which directly feeds into the base of $Q_1$ ($I_{B1} = I_{C2}$).
2. Transistor $Q_1$ turns on harder, increasing $I_{C1}$, which feeds back into the base of $Q_2$ ($I_{B2} = I_{C1} + I_g$).
3. The current gains $\alpha_1$ and $\alpha_2$ are strong functions of emitter current; as current rises, both $\alpha_1$ and $\alpha_2$ increase rapidly.
4. When the loop gain reaches unity:
$$\alpha_1 + \alpha_2 \to 1$$
5. The denominator $[1 - (\alpha_1 + \alpha_2)] \to 0$, causing $I_A \to \infty$ (limited only by external circuit load resistance). This represents regenerative internal positive feedback, driving both transistors into hard saturation. Once triggered, the internal loop current sustains itself, rendering the gate current $I_g$ completely redundant.
"""
            },
            {
                "qid": "pe-q2",
                "marks": 7,
                "type": "Descriptive & Analytical",
                "title": "SCR Turn-On Methods, Gate Firing Requirements, and Gate Drive Circuit Design",
                "yt_query": "SCR turn on methods gate characteristics triggering pulse transformer",
                "img_path": "images/pe/scr_gate_characteristics.png",
                "img_caption": "Figure 1.2: SCR Gate V-I Characteristics, Safe Operating Triggering Area, and Pulse Isolation Drive",
                "answer": r"""
To switch an SCR from the forward blocking state to the forward conduction state, the central reverse-biased junction $J_2$ must be caused to break down.

### 1. Classification of SCR Turn-on Methods
1. **Forward Voltage Triggering ($V_{AK} \ge V_{BO}$):**
   When the forward anode-to-cathode voltage is increased to the forward breakover voltage $V_{BO}$ with gate open ($I_g = 0$), the depletion layer at junction $J_2$ experiences avalanche breakdown. This method is generally avoided in practice because high voltage turn-on causes excessive localized power dissipation and device degradation.
2. **Thermal (Temperature) Triggering:**
   At high junction temperatures, thermally generated electron-hole pairs inside the depletion layer of $J_2$ increase exponentially. Leakage current doubles roughly every $8\text{ to }10^\circ\text{C}$. This increases $\alpha_1$ and $\alpha_2$, causing regenerative breakdown when $(\alpha_1 + \alpha_2) \to 1$.
3. **$dv/dt$ Triggering:**
   Junction $J_2$ acts as a dielectric capacitor with junction capacitance $C_{j2}$. When a rapidly rising forward voltage is applied, a displacement current flows through $J_2$:
   $$i = \frac{dq}{dt} = \frac{d(C_{j2} v)}{dt} = C_{j2} \frac{dv}{dt} + v \frac{dC_{j2}}{dt}$$
   If $\frac{dv}{dt}$ is excessively large, the displacement current $i$ acts as an internal gate current, triggering the SCR prematurely. This is an undesirable false turn-on mechanism and requires snubber protection.
4. **Light (Radiation) Triggering (LASCR):**
   Light-Activated SCRs (LASCR) contain a recessed optical window on junction $J_2$. When incident light photons with energy $h\nu \ge E_g$ strike the silicon lattice, electron-hole pairs are generated near $J_2$, initiating regenerative turn-on. It provides complete electrical isolation and is standard in High-Voltage DC (HVDC) transmission converter valves.
5. **Gate Triggering (Standard Controlled Turn-on):**
   Applying a positive voltage between gate and cathode injects carriers into the $p_2$ layer, initiating regenerative latching at low forward voltages ($V_{AK} \ll V_{BO}$).

### 2. Gate V-I Characteristics and Safe Triggering Area
Due to manufacturing tolerances between different SCR units of the same type, gate characteristics are defined by a spread bounded by maximum and minimum curves:

```
    Gate Voltage (V_g)
        ▲
        │      P_gm (Peak Gate Power Hyperbola)
  V_gmax┼───┐ . . . . . . . .
        │   │ ┌─────────┐   :
        │   │ │ Preferred│   :
        │   │ │ Trigger │   :
  V_gmin┼───┼─┴─────────┴───:─ Load Line (Slope = -R_g)
        │   │ Non-trigger   :
        └───┼───┼───────────┼──────► Gate Current (I_g)
            0  I_gmin      I_gmax
```

To ensure reliable triggering without damaging the gate junction:
- $V_{g\min}$ and $I_{g\min}$: Minimum gate voltage and current required to ensure firing of all devices of a given rating at the lowest operating temperature.
- $V_{g\max}$ and $I_{g\max}$: Maximum limits to prevent reverse breakdown or junction melting.
- $P_{gm}$ (Peak Gate Power Hyperbola): Maximum instantaneous power dissipation curve defined by:
$$P_{gm} = V_g \cdot I_g = \text{constant}$$
The operating point must lie strictly within the Preferred Triggering Zone bounded by $V_{g\min}$, $V_{g\max}$, $I_{g\min}$, $I_{g\max}$, and the $P_{gm}$ curve.

The gate circuit equation with source voltage $E_s$ and source resistance $R_g$ is:
$$E_s = V_g + R_g I_g \implies V_g = E_s - R_g I_g$$
The load line has a vertical intercept at $E_s$ and a slope of $-R_g$.

### 3. Pulse Triggering and Gate Isolation Circuit
Using continuous DC gate signals causes excessive average gate power loss ($P_{g,avg} = V_g I_g$) and thermal heating. Practical converters utilize high-frequency pulse trains ($f_p \approx 10\text{ to }50\text{ kHz}$) modulated over the firing angle window.
- **Pulse Transformer:** Provides galvanic high-voltage isolation between the low-voltage microcontroller/DSP logic ($5\text{ V}$) and the high-potential thyristor cathode ($400\text{ to }1000\text{ V}$). It passes short microsecond trigger pulses while blocking DC.
- **Optocoupler:** An infrared LED coupled with a phototransistor or phototriac provides electrical isolation exceeding $5\text{ kV}$, eliminating ground loops.
- **Diode and Resistor Protection:** A diode in series prevents reverse gate voltage breakdown, while a shunt resistor $R_{gk}$ across gate-cathode drains displacement currents caused by high $dv/dt$, preventing spurious turn-on.
"""
            },
            {
                "qid": "pe-q3",
                "marks": 10,
                "type": "Analytical & Waveform Analysis",
                "title": "Dynamic Switching Characteristics of SCR: Turn-On and Turn-Off Mechanisms with Commutation Requirements",
                "yt_query": "SCR dynamic switching turn on turn off characteristics reverse recovery time",
                "img_path": "images/pe/scr_switching_waveforms.png",
                "img_caption": "Figure 1.3: Dynamic Transient Switching Waveforms of Anode Voltage and Current During Turn-On and Turn-Off of an SCR",
                "answer": r"""
The dynamic switching characteristics of an SCR describe the transient transitions between the non-conducting (OFF) and conducting (ON) states. Because of internal junction capacitances and finite charge-carrier transit times, transitions cannot occur instantaneously.

### 1. Dynamic Turn-on Characteristics
The turn-on process begins when a gate trigger pulse is applied and is divided into three distinct time intervals:
$$t_{on} = t_d + t_r + t_p$$

1. **Delay Time ($t_d$):**
   The time interval between the instant the gate current reaches $0.1 I_g$ and the instant the anode current rises to $0.1 I_A$ (where $I_A$ is full on-state current). Simultaneously, the anode voltage drops from $V_A$ to $0.9 V_A$. During $t_d$, charge carriers are injected into the gate region, establishing conduction only in a tiny filament near the gate cathode boundary.
2. **Rise Time ($t_r$):**
   The time required for the anode current to rise from $0.1 I_A$ to $0.9 I_A$, during which the anode-to-cathode voltage falls sharply from $0.9 V_A$ to $0.1 V_A$.
   - Because high voltage and high current coexist across the device during $t_r$, the instantaneous power dissipation ($p(t) = v_A(t) \cdot i_A(t)$) reaches a tremendous peak.
   - For an inductive load, $t_r$ is longer because the rate of rise of anode current is limited by the circuit time constant ($L/R$).
3. **Spread Time ($t_p$ or $t_s$):**
   The time taken for the conduction plasma to spread laterally across the entire active cross-sectional area of the cathode junction. During this interval, the anode current increases from $0.9 I_A$ to full load value $I_A$, and the forward voltage drop falls to its steady-state on-state value:
   $$V_{on} \approx 1.0 \text{ to } 1.5\text{ V}$$

```
Anode Voltage (v_A) & Current (i_A)
     ▲
 v_A │───────┐
     │  V_A  │\
     │       │ \
     │       │  \                v_A drops to V_on
     │       │   \───────────────────────
     ├───────┼───┼───────┼───────────────► Time (t)
 i_A │       │   │  /────┼─────── I_A (Load current)
     │       │   │ /     │
     │       │  _│/      │
     └───────┴───┴───────┴───────────────►
             | t_d | t_r |  t_p  |
             |<───── t_on ──────>|
```

### 2. Dynamic Turn-off Characteristics (Commutation)
Once an SCR is turned on, reducing gate current to zero does not turn it off. Turn-off requires:
1. Reducing the anode current below the holding current ($I_A < I_H$).
2. Applying a reverse voltage across the anode-to-cathode terminals for a sufficient duration to allow trapped excess charge carriers to be removed and recombine.

The internal device turn-off time ($t_q$) consists of two phases:
$$t_q = t_{rr} + t_{gr}$$

```
Anode Current (i_A)
     ▲
 I_A ┼───────────┐
     │           │\
     │           │ \ (di/dt)
   0 ┼───────────┼──\───────────────┼────────► Time (t)
     │           │   \             /│
-I_RR┼ - - - - - ┼ - -\ - - - - - / │
     │           │     \_________/  │
     │           |<─── t_rr ────>|<─ t_gr ─>|
     │           |<─────────── t_q ────────>|
     │           |<──────────── t_c ──────────────>| (t_c > t_q)
     ▼
```

1. **Reverse Recovery Time ($t_{rr}$):**
   When the anode current falls to zero at a rate $di/dt$ determined by external circuit parameters, it continues to flow in the reverse direction due to the sweeping out of stored holes and electrons from outer junctions $J_1$ and $J_3$. The reverse current reaches a peak value $I_{RR}$ (Reverse Recovery Current) and then decays rapidly to zero. At the end of $t_{rr}$, junctions $J_1$ and $J_3$ have regained their reverse blocking capability.
   The reverse recovery charge $Q_{rr}$ is:
   $$Q_{rr} = \frac{1}{2} I_{RR} \cdot t_{rr} \implies I_{RR} = \left(\frac{di}{dt}\right) t_{rr} \implies t_{rr} = \sqrt{\frac{2 Q_{rr}}{di/dt}}$$
2. **Gate Recovery Time ($t_{gr}$):**
   Even after $J_1$ and $J_3$ recover, inner junction $J_2$ remains flooded with trapped minority carriers. These carriers cannot be swept out by external reverse voltage; they must decay solely via internal thermal carrier recombination. The time required for recombination to reduce carrier density below the critical threshold is the gate recovery time $t_{gr}$.

### 3. Circuit Turn-off Time ($t_c$) and Commutation Failure
- **Device Turn-off Time ($t_q$):** The intrinsic physical time required by the SCR to regain forward blocking capability after anode current has ceased. Standard converter-grade thyristors have $t_q \approx 50\text{ to }100\ \mu\text{s}$, while inverter-grade fast thyristors have $t_q \approx 3\text{ to }20\ \mu\text{s}$.
- **Circuit Turn-off Time ($t_c$):** The time duration for which the external power circuit actually applies a reverse bias voltage across the SCR:
$$t_c = \frac{\pi - \alpha}{\omega} \quad \text{(in line-commutated converters)}$$
- **Mandatory Commutation Condition:**
To guarantee successful commutation and prevent catastrophic short-circuits:
$$t_c > t_q$$
Typically, a safety design factor of $1.5 \text{ to } 2$ is enforced ($t_c \ge 1.5 t_q$). If forward voltage is reapplied when $t_c < t_q$, the residual trapped carriers at junction $J_2$ will immediately re-trigger the thyristor into forward conduction without any gate pulse, causing **commutation failure**.
"""
            },
            {
                "qid": "pe-q4",
                "marks": 10,
                "type": "Design & Derivation",
                "title": "SCR Protection Schemes: di/dt Inductor and dv/dt RC Snubber Circuit Design",
                "yt_query": "SCR protection di dt dv dt snubber circuit design derivation",
                "img_path": "images/pe/scr_snubber_protection.png",
                "img_caption": "Figure 1.4: Complete Protection Circuit for an SCR showing Series Inductor (Ls), Parallel RC Snubber, and Varistor",
                "answer": r"""
Power thyristors must be protected against catastrophic electrical stresses: high rates of current rise ($di/dt$), high rates of voltage rise ($dv/dt$), overvoltages, and overcurrents.

### 1. $di/dt$ Protection using Series Inductor ($L_s$)
- **Problem:** During the initial turn-on interval ($t_d$ and $t_r$), conduction begins over a tiny localized area near the gate cathode contact. If the anode current rises at an excessively high rate ($di/dt$), current density in this restricted area becomes astronomically high. Localized power dissipation creates microscopic "hot spots" where silicon temperature exceeds $300^\circ\text{C}$, causing permanent localized thermal puncture.
- **Remedy:** A small inductor $L_s$ is connected in direct series with the anode. The inductor opposes instantaneous changes in current ($v_L = L \frac{di}{dt}$), limiting the rate of rise:
$$\left(\frac{di}{dt}\right)_{\max} \le \left(\frac{di}{dt}\right)_{\text{rated}}$$
- **Design Formula:** For a supply voltage $V_s$, the minimum value of series inductance required is:
$$L_s \ge \frac{V_s}{(di/dt)_{\max}}$$

### 2. $dv/dt$ Protection using Parallel RC Snubber Circuit
- **Problem:** When an SCR is in forward blocking, junction $J_2$ acts as a capacitor with depletion capacitance $C_{j2}$. A steep step voltage or voltage transient causes a capacitive displacement current:
$$i_c = C_{j2} \frac{dv}{dt}$$
If $i_c$ exceeds the gate threshold current $I_{g\min}$, the SCR turns on unintentionally without a gate command.
- **Remedy:** A snubber circuit comprising a series combination of a non-inductive resistor $R_s$ and capacitor $C_s$ is connected in parallel with the SCR.

```
       + ─────────o───[ L_s ]───┬───────────────o +
                                │
                          ┌─────┴─────┐
                          │     │     │
                         [R_s]  │     │
                          │     ▼ SCR │ [Load]
                         [C_s]  │     │
                          │     │     │
                          └─────┬─────┘
                                │
       - ───────────────────────┴───────────────o -
```

### 3. Mathematical Derivation of RC Snubber Equations
When supply voltage $V_s$ is suddenly switched across the uncharged circuit with the SCR in OFF state, the equivalent circuit is a series $R-L-C$ circuit formed by source inductance $L_s$, snubber resistance $R_s$, and snubber capacitance $C_s$.

Applying Kirchhoff's Voltage Law:
$$V_s = L_s \frac{di}{dt} + R_s i + v_c(t)$$
Since the loop current is $i(t) = C_s \frac{dv_c}{dt}$:
$$L_s C_s \frac{d^2 v_c}{dt^2} + R_s C_s \frac{dv_c}{dt} + v_c = V_s$$

Dividing by $L_s C_s$:
$$\frac{d^2 v_c}{dt^2} + \frac{R_s}{L_s}\frac{dv_c}{dt} + \frac{1}{L_s C_s} v_c = \frac{V_s}{L_s C_s}$$

This represents a standard second-order system characterized by:
- Undamped natural frequency: $\omega_n = \frac{1}{\sqrt{L_s C_s}}$
- Damping ratio: $\zeta = \frac{R_s}{2}\sqrt{\frac{C_s}{L_s}}$

The voltage appearing across the SCR is the terminal voltage across the snubber branch:
$$v_{AK}(t) = v_c(t) + R_s i(t)$$

At the initial instant of switching ($t = 0^+$), capacitor voltage is zero ($v_c(0^+) = 0$) and current is zero ($i(0^+) = 0$). The rate of change of voltage across the SCR is maximized:
$$\left(\frac{dv}{dt}\right)_{\max} \approx \frac{V_s}{L_s} R_s = 2 \zeta \omega_n V_s$$

For an optimally damped response to avoid severe voltage overshoots ($\zeta \approx 0.65\text{ to }0.707$):
$$\left(\frac{dv}{dt}\right)_{\max} = 0.563 \omega_n V_s = 0.563 \frac{V_s}{\sqrt{L_s C_s}}$$

Squaring both sides and solving for $C_s$:
$$C_s = \frac{(0.563)^2 V_s^2}{L_s \left(\frac{dv}{dt}\right)_{\max}^2} \approx \frac{V_s^2}{L_s \left(\frac{dv}{dt}\right)_{\max}^2}$$

### 4. Snubber Resistor Sizing and Discharge Current Limit
When the SCR is triggered into conduction, the snubber capacitor $C_s$ (charged up to $V_s$) discharges locally through $R_s$ and the internal conducting channel of the SCR.
The peak discharge current at $t = 0^+$ is:
$$I_{dis,\max} = \frac{V_s}{R_s}$$

To ensure this discharge current does not exceed the maximum allowable repetitive surge current rating of the SCR ($I_{T\max}$):
$$R_s \ge \frac{V_s}{I_{T\max}}$$

Simultaneously, the rate of discharge current rise must not exceed device $(di/dt)_{\max}$:
$$\left(\frac{di}{dt}\right)_{\text{discharge}} = \frac{V_s}{R_s C_s} \le \left(\frac{di}{dt}\right)_{\max}$$

### 5. Step-by-Step Numerical Example
**Given Specifications:**
- Supply DC Voltage: $V_s = 400\text{ V}$
- Maximum allowable $(di/dt)_{\max} = 40\text{ A}/\mu\text{s} = 40 \times 10^6\text{ A/s}$
- Maximum allowable $(dv/dt)_{\max} = 200\text{ V}/\mu\text{s} = 200 \times 10^6\text{ V/s}$
- Peak allowable discharge current: $I_{T\max} = 100\text{ A}$

**Step 1: Calculate series inductance $L_s$:**
$$L_s \ge \frac{V_s}{(di/dt)_{\max}} = \frac{400}{40 \times 10^6} = 10 \times 10^{-6}\text{ H} = 10\ \mu\text{H}$$

**Step 2: Calculate snubber resistance $R_s$ from discharge limit:**
$$R_s \ge \frac{V_s}{I_{T\max}} = \frac{400}{100} = 4\ \Omega$$

**Step 3: Calculate snubber capacitance $C_s$:**
$$C_s = \frac{V_s^2}{L_s \left(\frac{dv}{dt}\right)_{\max}^2} = \frac{(400)^2}{(10 \times 10^{-6}) \times (200 \times 10^6)^2} = \frac{160000}{10^{-5} \times 4 \times 10^{16}} = \frac{160000}{4 \times 10^{11}} = 0.4\ \mu\text{F}$$

**Step 4: Verify damping ratio $\zeta$:**
$$\zeta = \frac{R_s}{2}\sqrt{\frac{C_s}{L_s}} = \frac{4}{2}\sqrt{\frac{0.4 \times 10^{-6}}{10 \times 10^{-6}}} = 2 \times \sqrt{0.04} = 2 \times 0.2 = 0.4$$
To raise $\zeta$ toward optimal $0.65$, $R_s$ is selected as $R_s = 6.5\ \Omega$, safely above the minimum $4\ \Omega$ constraint.
"""
            },
            {
                "qid": "pe-q5",
                "marks": 10,
                "type": "Comparative Analysis & Device Physics",
                "title": "Comprehensive Comparison of Modern Power Semiconductor Devices: TRIAC, GTO, Power MOSFET, and IGBT",
                "yt_query": "comparison TRIAC GTO MOSFET IGBT switching speed SOA conduction loss",
                "img_path": "images/pe/power_devices_comparison.png",
                "img_caption": "Figure 1.5: Output and Transfer Characteristics, Switching Waveforms, and Safe Operating Areas (SOA) of Power Switching Devices",
                "answer": r"""
Modern power electronic converters utilize diverse power semiconductor switches depending on the operating power level, voltage blocking requirement, switching frequency, and gate control complexity.

### 1. Device Physics and Operating Principles

#### A. TRIAC (Triode for Alternating Current)
- **Physics:** A bidirectional 5-layer thyristor equivalent to two SCRs connected in inverse-parallel with a single common gate terminal.
- **Conduction:** Conducts current in either direction between Main Terminals $MT_1$ and $MT_2$.
- **Triggering Modes:** Operates in 4 quadrants depending on polarities of $V_{MT2-MT1}$ and $V_{G-MT1}$:
  - Mode $I^+$ ($V_{MT2} > 0, V_G > 0$): Highly sensitive turn-on.
  - Mode $I^-$ ($V_{MT2} > 0, V_G < 0$): Moderate sensitivity.
  - Mode $III^-$ ($V_{MT2} < 0, V_G < 0$): Highly sensitive turn-on.
  - Mode $III^+$ ($V_{MT2} < 0, V_G > 0$): Least sensitive (avoided in practice).
- **Limitation:** Poor commutating $dv/dt$ capability ($dv/dt_c \approx 10\text{ to }20\text{ V}/\mu\text{s}$); when current falls to zero at AC zero crossing, stored charge can cause re-triggering. Limited to low-power $50\text{ Hz}$ AC line regulators (light dimmers, fan speed controllers).

#### B. GTO (Gate Turn-Off Thyristor)
- **Physics:** A 4-layer $p-n-p-n$ thyristor designed with an interdigitated multi-finger cathode-gate geometry to minimize lateral base resistance.
- **Turn-off Mechanism:** Can be turned off by extracting a large negative gate current pulse ($I_{GR}$). The negative gate pulse extracts stored carriers from the $p$-base, pinching the anode current into narrow filaments until total carrier starvation extinguishes conduction.
- **Turn-off Gain ($\beta_{off}$):**
$$\beta_{off} = \frac{I_A}{I_{GR}} \approx 3 \text{ to } 5$$
Because $\beta_{off}$ is very low, turning off an anode current of $1000\text{ A}$ requires an instantaneous reverse gate pulse of $200\text{ to }300\text{ A}$, necessitating complex, bulky gate-drive circuitry.
- **Application:** High-power traction drives and HVDC systems ($>4\text{ kV}, >3\text{ kA}$) where high conduction capability is paramount.

#### C. Power MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)
- **Physics:** A unipolar, majority-carrier, voltage-controlled device with a vertical planar (DMOS) or trench architecture.
- **Switching Speed:** Because conduction occurs exclusively via majority carriers (electrons in $n$-channel), there is zero minority-carrier storage delay. Switching times are extremely short ($10\text{ to }50\text{ ns}$), permitting switching frequencies up to several megahertz ($>1\text{ MHz}$).
- **Input Impedance:** The insulated $SiO_2$ gate provides nearly infinite input DC resistance ($>10^9\ \Omega$); gate drive requires energy only to charge and discharge gate capacitances ($C_{iss} = C_{gs} + C_{gd}$).
- **On-State Resistance ($R_{DS(on)}$):** Exhibits a positive temperature coefficient ($dR_{DS(on)}/dT > 0$), making MOSFETs naturally self-balancing when operated in parallel without thermal runaway.
- **Limitation:** On-state resistance increases steeply with breakdown voltage ($R_{DS(on)} \propto V_{BR}^{2.5}$). Hence, conduction losses become excessive at ratings above $600\text{ V}$.

#### D. IGBT (Insulated Gate Bipolar Transistor)
- **Physics:** A monolithic hybrid power device combining the high-impedance MOS gate structure of a MOSFET with the high-current bipolar output characteristic of a wide-base BJT.
- **Conductivity Modulation:** An added $p^+$ substrate injects holes into the lightly doped $n^-$ drift region during conduction. This massive injection floods the drift region with electron-hole plasma, dropping its effective resistance by orders of magnitude (conductivity modulation).
- **Conduction Voltage:** On-state saturation voltage remains low and nearly constant ($V_{CE(sat)} \approx 1.5\text{ to }2.5\text{ V}$) even for devices rated up to $6.5\text{ kV}$ and $1500\text{ A}$.
- **Turn-Off Tail Current:** During turn-off, the MOS channel opens immediately, but minority carriers stored in the wide $n^-$ drift base can only decay by recombination, causing a persistent "collector current tail" that increases turn-off switching losses.

```
       MOSFET Equivalent                  IGBT Equivalent
          D (Drain)                          C (Collector)
              │                                  │
          ┌───┴───┐                         ┌────┴────┐
          │ MOSFET│                         │   PNP   │
          │       │                         │   BJT   │
     G ───┤       │                    G ───┤         │
          └───┬───┘                         └────┬────┘
              │                             MOSFET In│
          S (Source)                         E (Emitter)
```

### 2. Comprehensive Comparative Matrix

| Parameter / Feature | TRIAC | GTO | Power MOSFET | IGBT |
| :--- | :--- | :--- | :--- | :--- |
| **Control Type** | Current controlled (Pulse) | Current controlled (Bi-directional) | Voltage controlled ($V_{GS}$) | Voltage controlled ($V_{GE}$) |
| **Carrier Type** | Bipolar (Minority) | Bipolar (Minority) | Unipolar (Majority only) | Hybrid (Majority + Minority) |
| **Voltage Rating** | Medium ($<1.2\text{ kV}$) | Very High ($>6\text{ kV}$) | Low/Medium ($<1000\text{ V}$) | High ($600\text{ V} - 6.5\text{ kV}$) |
| **Current Rating** | Low/Medium ($<100\text{ A}$) | Very High ($>3000\text{ A}$) | Medium ($<200\text{ A}$) | High ($>1500\text{ A}$) |
| **Switching Frequency** | Very Low ($<400\text{ Hz}$) | Low ($<2\text{ kHz}$) | Very High ($100\text{ kHz} - 2\text{ MHz}$) | Medium/High ($10\text{ kHz} - 100\text{ kHz}$) |
| **On-State Loss** | Low ($V_{on} \approx 1.5\text{ V}$) | Low ($V_{on} \approx 2\text{ to }3\text{ V}$) | High at high $V$ ($I^2 R_{DS(on)}$) | Low ($V_{CE(sat)} \approx 1.8\text{ to }2.5\text{ V}$) |
| **Switching Loss** | Low at $50\text{ Hz}$ | High (Turn-off tail) | Negligible (Fast edges) | Moderate (Tail current) |
| **Gate Drive Power** | Low (Short pulses) | Very High ($\beta_{off} \approx 3-5$) | Minimal (Capacitive only) | Minimal (Capacitive only) |
| **Safe Operating Area** | Limited by $dv/dt$ | Moderate (Needs snubber) | Excellent (No 2nd breakdown)| Excellent (Wide FBSOA/RBSOA) |
| **Paralleling Ease** | Poor | Poor | Excellent (Positive temp coeff)| Very Good (Modern planar) |
| **Primary Applications**| AC regulators, dimmers | Traction, heavy MW drives | SMPS, RF, EV DC-DC | EV inverters, VFD, Renewables |

### 3. Safe Operating Area (SOA) Considerations
- **Power MOSFET SOA:** Strictly bounded by thermal dissipation ($P_D = V_{DS} I_D$) and maximum pulsed drain current. Because MOSFETs have a positive temperature coefficient of resistance, hot spots do not form, rendering them immune to second breakdown.
- **IGBT SOA:**
  - **Forward-Biased Safe Operating Area (FBSOA):** Bounded by maximum collector current $I_{CM}$, maximum power dissipation $P_D$, and maximum collector-emitter voltage $V_{CES}$. Modern trench IGBTs feature a square FBSOA up to short-circuit durations of $10\ \mu\text{s}$.
  - **Reverse-Biased Safe Operating Area (RBSOA):** Governs dynamic turn-off when clamping inductive voltage spikes. With proper gate resistance $R_g$, modern IGBTs offer full square RBSOA at twice the continuous rated collector current ($2 I_C$) up to $V_{CES}$.
"""
            }
        ]
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
]

PE_BYHEART = {
    "pe-q1": {
        "eq": r"""$$I_A = \frac{\alpha_2 I_g + I_{CBO1} + I_{CBO2}}{1 - (\alpha_1 + \alpha_2)}, \quad I_L \approx (2 \text{ to } 3) I_H$$""",
        "text": r"""SCR 4-layer $p_1-n_1-p_2-n_2$ structure modeled as coupled PNP ($Q_1$) and NPN ($Q_2$) transistors. Forward latching occurs via regenerative positive feedback when loop gain $\alpha_1 + \alpha_2 \to 1$. Latching current $I_L$ is minimum turn-on holding value; $I_H$ is drop-out threshold."""
    },
    "pe-q2": {
        "eq": r"""$$P_{gm} = V_g I_g = \text{const}, \quad E_s = V_g + R_g I_g, \quad i_c = C_{j2}\frac{dv}{dt}$$""",
        "text": r"""Turn-on via gate pulse, light (LASCR), thermal, or $dv/dt$. Gate operating point must lie inside preferred triggering window bounded by $V_{g\min}, V_{g\max}, I_{g\min}, I_{g\max}$ and peak gate power hyperbola $P_{gm}$. Pulse transformer / optocoupler provides galvanic isolation."""
    },
    "pe-q3": {
        "eq": r"""$$t_{on} = t_d + t_r + t_p, \quad t_q = t_{rr} + t_{gr}, \quad t_c > t_q \ (\text{commutation})$$""",
        "text": r"""Turn-on transient comprises delay ($t_d$), rise ($t_r$), and spread ($t_p$) times. Turn-off transient requires sweeping out reverse carriers ($t_{rr}$) and thermal recombination of trapped junction charges ($t_{gr}$). Circuit turn-off time must satisfy $t_c > t_q$ to avoid commutation failure."""
    },
    "pe-q4": {
        "eq": r"""$$L_s \ge \frac{V_s}{(di/dt)_{\max}}, \quad C_s = \frac{V_s^2}{L_s (dv/dt)_{\max}^2}, \quad R_s \ge \frac{V_s}{I_{T\max}}, \quad \zeta = \frac{R_s}{2}\sqrt{\frac{C_s}{L_s}}$$""",
        "text": r"""Series inductor $L_s$ suppresses localized gate hot-spot burning from high $di/dt$. Parallel RC snubber dampens transient $dv/dt$ displacement currents across junction $J_2$. Snubber resistor $R_s$ limits discharge current when SCR fires."""
    },
    "pe-q5": {
        "eq": r"""$$\beta_{off} = \frac{I_A}{I_{GR}} \approx 3-5 \ (\text{GTO}), \quad R_{DS(on)} \propto V_{BR}^{2.5} \ (\text{MOSFET}), \quad V_{CE(sat)} \approx 1.8-2.5\text{ V} \ (\text{IGBT})$$""",
        "text": r"""<strong>TRIAC:</strong> Bidirectional AC line switch (4 quadrants).<br><strong>GTO:</strong> Turn-off via large reverse gate current.<br><strong>MOSFET:</strong> Unipolar majority-carrier switch for MHz frequencies ($<600\text{ V}$).<br><strong>IGBT:</strong> Hybrid MOS-input BJT-output with conductivity modulation for medium/high power."""
    },
    "pe-q6": {
        "eq": r"""$$V_{dc} = \frac{V_m}{2\pi}(1 + \cos\alpha), \quad V_{rms} = \frac{V_m}{2\sqrt{\pi}}\sqrt{(\pi - \alpha) + \frac{1}{2}\sin 2\alpha}, \quad i_o(\beta) = 0$$""",
        "text": r"""1-Phase Half-Wave Controlled Rectifier. Inductive RL load extends conduction into negative half-cycle to extinction angle $\beta$. Freewheeling diode clamps $v_o \ge 0$, discharges inductive energy, boosts average DC voltage, and improves power factor."""
    },
    "pe-q7": {
        "eq": r"""$$V_{dc} = \frac{2 V_m}{\pi}\cos\alpha, \quad V_{rms} = \frac{V_m}{\sqrt{2}} = V_s, \quad I_{dc} = \frac{V_{dc} - E}{R}$$""",
        "text": r"""1-Phase Full Converter with RLE load operates in Quadrant I ($0 \le \alpha < 90^\circ$, Rectification) and Quadrant IV ($90^\circ < \alpha < 180^\circ$, Inversion). Line commutation transfers current between SCR pairs. Discontinuous conduction occurs at light loads."""
    },
    "pe-q8": {
        "eq": r"""$$\text{DF} = \cos\alpha, \quad \text{THD} = \sqrt{\left(\frac{\pi}{2\sqrt{2}}\right)^2 - 1} \approx 48.34\%, \quad \text{PF} = \frac{2\sqrt{2}}{\pi}\cos\alpha$$""",
        "text": r"""Displacement Factor $\text{DF} = \cos\phi_1$. Total Harmonic Distortion measures ripple current relative to fundamental. Semi-converter exhibits higher PF ($\text{DF} = \cos(\alpha/2)$) and lower reactive power than full converter due to freewheeling action."""
    },
    "pe-q9": {
        "eq": r"""$$V_{dc} = \frac{3 V_{ml}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_{mp}}{\pi}\cos\alpha \approx 1.35 V_L \cos\alpha, \quad V_{rms} = V_{ml}\sqrt{\frac{1}{2} + \frac{3\sqrt{3}}{4\pi}\cos 2\alpha}$$""",
        "text": r"""3-Phase 6-Pulse Full Bridge Converter: 6 SCRs triggered at $60^\circ$ intervals, each conducting for $120^\circ$. Output line voltage switches between 6 line pairs. Operates as rectifier for $\alpha \le 90^\circ$ and line-commutated inverter for $\alpha > 90^\circ$."""
    },
    "pe-q10": {
        "eq": r"""$$\cos(\alpha + \mu) = \cos\alpha - \frac{2 \omega L_s I_{dc}}{V_m}, \quad \Delta V_d = \frac{2 \omega L_s}{\pi} I_{dc} \ (\text{1-ph}), \quad \Delta V_d = \frac{3 \omega L_s}{\pi} I_{dc} \ (\text{3-ph})$$""",
        "text": r"""Source inductance $L_s$ prevents instantaneous current transfer, causing commutation overlap angle $\mu$. Output voltage drops by $\Delta V_d$. In inverter mode, if $\alpha + \mu > 180^\circ - \omega t_q$, commutation failure occurs."""
    },
    "pe-q11": {
        "eq": r"""$$V_o = D V_s, \quad \Delta I_L = \frac{V_s D(1 - D)}{f_s L}, \quad \Delta V_c = \frac{V_s D(1 - D)}{8 f_s^2 L C}, \quad L_c = \frac{(1 - D) R}{2 f_s}$$""",
        "text": r"""Step-down (Buck) converter in CCM. Inductor volt-second balance yields linear gain $M = D$. Second-order LC filter delivers low output voltage ripple. Critical inductance $L_c$ guarantees continuous conduction at specified load resistance."""
    },
    "pe-q12": {
        "eq": r"""$$V_o = \frac{V_s}{1 - D}, \quad \Delta I_L = \frac{V_s D}{f_s L}, \quad \Delta V_c = \frac{V_o D}{R f_s C}, \quad L_c = \frac{D(1 - D)^2 R}{2 f_s}$$""",
        "text": r"""Step-up (Boost) converter in CCM. Energy stored during switch ON adds in series with DC source during switch OFF. Output capacitor supplies load while switch is ON. Inductor parasitic resistance limits maximum practical voltage gain."""
    },
    "pe-q13": {
        "eq": r"""$$V_o = -\frac{D}{1 - D} V_s, \quad \Delta I_L = \frac{V_s D}{f_s L}, \quad \Delta V_c = \frac{V_o D}{R f_s C}, \quad L_c = \frac{(1 - D)^2 R}{2 f_s}$$""",
        "text": r"""Inverting Buck-Boost converter provides step-down ($D < 0.5$) and step-up ($D > 0.5$) voltage translation with reversed output polarity. Inductor acts as intermediate energy reservoir between input and output ports."""
    },
    "pe-q14": {
        "eq": r"""$$V_o = -\frac{D}{1 - D} V_s, \quad V_{C1} = \frac{V_s}{1 - D}, \quad \Delta I_{L1} = \frac{V_s D}{f_s L_1}, \quad \Delta I_{L2} = \frac{V_s D}{f_s L_2}$$""",
        "text": r"""Ćuk converter transfers energy capacitively via intermediate capacitor $C_1$. Dual input and output inductors eliminate pulsating currents at both terminal ports, yielding low EMI signatures and smooth continuous waveforms."""
    },
    "pe-q15": {
        "eq": r"""$$\text{Class A: } (+V_o, +I_o), \ \text{Class B: } (+V_o, -I_o), \ \text{Class C: } (+V_o, \pm I_o), \ \text{Class D: } (\pm V_o, +I_o), \ \text{Class E: } (\pm V_o, \pm I_o)$$""",
        "text": r"""Chopper classification across $(V_o, I_o)$ plane: Class A (Motoring), Class B (Regenerative braking), Class C (Reversible drive), Class D (Coil de-energization), and Class E (Complete 4-quadrant H-bridge servo drive)."""
    },
    "pe-q16": {
        "eq": r"""$$\text{Half: } V_{o,rms} = \frac{V_{dc}}{2}, \ V_{o1} = \frac{2 V_{dc}}{\pi}; \quad \text{Full: } V_{o,rms} = V_{dc}, \ V_{o1} = \frac{4 V_{dc}}{\pi}; \quad V_{o1,\text{quasi}} = \frac{4 V_{dc}}{\pi}\sin d$$""",
        "text": r"""1-Phase VSI topologies: Full-bridge delivers twice the voltage and 4x the power of half-bridge. Feedback diodes circulate reactive load current and return energy to DC source ($v_o \cdot i_o < 0$). Quasi-square wave modulation controls fundamental and eliminates harmonics."""
    },
    "pe-q17": {
        "eq": r"""$$V_{L,rms} = \sqrt{\frac{2}{3}} V_{dc} \approx 0.8165 V_{dc}, \quad V_{ph,rms} = \frac{\sqrt{2}}{3} V_{dc} \approx 0.4714 V_{dc}, \quad V_{L1,rms} = \frac{\sqrt{6}}{\pi} V_{dc} \approx 0.7797 V_{dc}$$""",
        "text": r"""3-Phase VSI 180° conduction: Each switch conducts for 180°, with 3 switches ON simultaneously. Six-step phase voltage waveform. Triplen harmonics are inherently eliminated from line-to-line voltages."""
    },
    "pe-q18": {
        "eq": r"""$$V_{L,rms} = \frac{V_{dc}}{\sqrt{2}} \approx 0.7071 V_{dc}, \quad V_{ph,rms} = \frac{V_{dc}}{\sqrt{6}} \approx 0.4082 V_{dc}, \quad \text{Inherent } 60^\circ \text{ Deadband}$$""",
        "text": r"""3-Phase VSI 120° conduction: Each switch conducts for 120°, with 2 switches ON simultaneously. Inherent 60° deadband prevents shoot-through faults without blanking circuits. Delivers 86.6% of the line voltage of 180° mode."""
    },
    "pe-q19": {
        "eq": r"""$$m_a = \frac{A_r}{A_c}, \quad m_f = \frac{f_c}{f_m}, \quad V_{o1\max} = m_a V_{dc} \ (m_a \le 1), \quad f_h = (j \cdot m_f \pm k) f_m$$""",
        "text": r"""Sinusoidal PWM (SPWM) compares sine reference with triangular carrier. Linear modulation up to $m_a = 1$. High carrier ratio $m_f$ pushes harmonic sidebands far above line frequency, simplifying passive filter design."""
    },
    "pe-q20": {
        "eq": r"""$$\text{VSI: Stiff } C_{dc}, \text{ antiparallel diodes, shoot-through risk}; \quad \text{CSI: Stiff } L_{dc}, \text{ series diodes, open-circuit risk}$$""",
        "text": r"""VSI regulates voltage (load determines current), dominates EVs and industrial inverters. CSI regulates current via large series choke $L_{dc}$ with ASCI commutation, offering inherent short-circuit immunity and four-quadrant regeneration for MW drives."""
    },
    "pe-q21": {
        "eq": r"""$$\text{Integral: } V_{o,rms} = V_s \sqrt{\frac{n}{n + m}}, \ \text{PF} = \sqrt{\frac{n}{n + m}}; \quad \text{Phase: } V_{o,rms} = V_s \sqrt{\frac{1}{\pi}\left[(\pi - \alpha) + \frac{1}{2}\sin 2\alpha\right]}$$""",
        "text": r"""1-Phase AC Voltage Controller with R load: Integral cycle control switches at zero crossings (no RFI, heating loads); Phase angle control varies firing angle $\alpha$ from 0 to 180° to continuously regulate output RMS voltage."""
    },
    "pe-q22": {
        "eq": r"""$$i_o(\omega t) = \frac{V_m}{Z}\left[\sin(\omega t - \phi) - \sin(\alpha - \phi) e^{-\frac{R}{\omega L}(\omega t - \alpha)}\right], \quad \alpha \ge \phi \ (\text{Operating Rule})$$""",
        "text": r"""1-Phase AC Controller with RL load: Controlled discontinuous mode for $\alpha > \phi$. When $\alpha = \phi$, current is continuous sinusoid ($V_{o,rms} = V_s$). Firing at $\alpha < \phi$ causes loss of control and DC core saturation; wide gate pulses required."""
    },
    "pe-q23": {
        "eq": r"""$$f_o = \frac{f_s}{k} \ (k = 2, 3\dots), \quad \alpha_P + \alpha_N = 180^\circ \ (\text{Circulating Mode with IGR})$$""",
        "text": r"""Cycloconverters directly convert AC frequency without intermediate DC link. Step-down operation uses line commutation. Non-circulating mode requires zero-crossing deadtime; circulating mode uses Intergroup Reactor (IGR) to eliminate crossover distortion."""
    },
    "pe-q24": {
        "eq": r"""$$P_{sw} = \frac{1}{2} V_s I_o (t_r + t_f) f_s, \quad \text{ZCS: } i_{sw} = 0 \ (\text{IGBT tail loss elimination}), \quad \text{ZVS: } v_{sw} = 0 \ (\text{MOSFET } C_{oss})$$""",
        "text": r"""Soft switching eliminates hard-switching overlap power dissipation. ZCS turns switch on/off at zero current (ideal for IGBTs). ZVS turns switch on/off at zero voltage (ideal for high-frequency Power MOSFETs, eliminating $\frac{1}{2}CV^2$ losses)."""
    },
    "pe-q25": {
        "eq": r"""$$\text{Flyback: } V_o = \frac{N_s}{N_p}\left(\frac{D}{1-D}\right)V_s, \quad \text{Forward: } V_o = \frac{N_s}{N_p} D V_s \ (D < 0.5), \quad \text{Push-Pull/Full: } V_o = 2\frac{N_s}{N_p} D V_s$$""",
        "text": r"""Isolated SMPS topologies: Flyback uses coupled inductor (energy stored in gap during switch ON, $<150\text{ W}$); Forward transfers energy during switch ON (needs tertiary reset winding); Push-Pull, Half-Bridge, and Full-Bridge provide 2-quadrant core utilization for high power."""
    },
    "pe-q26": {
        "eq": r"""$$\text{Offline: } 4-10\text{ ms transfer}; \quad \text{Line-Interactive: } 2-4\text{ ms}; \quad \text{Online Double-Conversion: } 0\text{ ms (Zero)}$$""",
        "text": r"""UPS configurations: Offline provides raw mains with battery backup; Line-Interactive adds AVR voltage conditioning; Online Double-Conversion continuously converts $AC \to DC \to AC$, delivering 0 ms transfer time, perfect sine wave, and static bypass protection."""
    }
}

PE_EXAM_QUESTIONS = {
    "pe-q1": "Explain the physical construction and static V-I characteristics of a Silicon Controlled Rectifier (SCR). Derive the mathematical expression for anode current using the two-transistor analogy.",
    "pe-q2": "Describe the various turn-on methods for an SCR. Explain the gate characteristics, safe triggering area, and design of pulse transformer isolation gate drive circuits.",
    "pe-q3": "Explain the dynamic switching characteristics of an SCR during turn-on and turn-off processes. Define reverse recovery time, gate recovery time, and circuit turn-off time with neat waveforms.",
    "pe-q4": "Explain the need for di/dt and dv/dt protection for an SCR. Derive the design equations for a series inductor and an RC snubber circuit with a step-by-step numerical example.",
    "pe-q5": "Compare the operating principles, switching speeds, conduction losses, and Safe Operating Areas (SOA) of TRIAC, GTO, Power MOSFET, and IGBT.",
    "pe-q6": "Explain the operation of a single-phase half-wave controlled rectifier with R and RL loads. Derive expressions for average and RMS output voltages, and explain the effect of a freewheeling diode.",
    "pe-q7": "Derive the expression for average and RMS output voltages of a single-phase fully controlled bridge rectifier feeding an RLE load. Distinguish between continuous and discontinuous conduction modes.",
    "pe-q8": "Define and derive the performance parameters of phase-controlled converters: Displacement Factor (DF), Harmonic Factor (HF/THD), and Input Power Factor (PF). Compare semi-converter and full converter.",
    "pe-q9": "Describe the working of a three-phase fully controlled bridge converter (6-pulse) with RL load. Derive the expression for average DC output voltage and plot the line-to-line output waveforms.",
    "pe-q10": "Explain the effect of AC source inductance on the performance of single-phase and three-phase full converters. Derive expressions for overlap angle (mu) and average voltage drop.",
    "pe-q11": "Analyze the step-down (Buck) converter in continuous conduction mode. Derive the voltage transfer ratio, peak-to-peak inductor ripple current, output ripple voltage, and critical inductance.",
    "pe-q12": "Explain the operation of a step-up (Boost) converter in continuous conduction mode. Derive the voltage gain using inductor volt-second balance, and calculate the critical inductance for CCM.",
    "pe-q13": "Derive the voltage transfer ratio of an inverting Buck-Boost converter in continuous conduction mode. Derive expressions for inductor ripple current and critical boundary inductance.",
    "pe-q14": "Explain the circuit topology and working principle of a Cuk converter. Derive the voltage ratio and explain why both input and output currents are continuous.",
    "pe-q15": "Classify DC choppers into Class A, B, C, D, and E based on their quadrant of operation. Draw the circuit diagram and explain the four-quadrant operation of a full H-bridge chopper.",
    "pe-q16": "Explain the operation of single-phase half-bridge and full-bridge Voltage Source Inverters (VSI) with R and RL loads. Derive the Fourier series expression for output voltage and discuss feedback diodes.",
    "pe-q17": "Explain the 180-degree conduction mode of a three-phase Voltage Source Inverter with a star-connected balanced load. Derive expressions for line and phase voltages and show Fourier harmonic elimination.",
    "pe-q18": "Analyze the 120-degree conduction mode of a three-phase Voltage Source Inverter. Derive expressions for RMS line and phase voltages and compare performance with the 180-degree conduction mode.",
    "pe-q19": "Explain Pulse Width Modulation (PWM) techniques used in inverters: Single-Pulse, Multi-Pulse, and Sinusoidal PWM (SPWM). Define modulation index (ma) and frequency ratio (mf) with harmonic spectra.",
    "pe-q20": "Compare the operating principles, circuit topologies, and performance of Voltage Source Inverters (VSI) and Current Source Inverters (CSI). Explain the ASCI commutation mechanism.",
    "pe-q21": "Explain the operation of a single-phase AC voltage controller with resistive load using Integral Cycle Control and Phase Angle Control. Derive expressions for RMS output voltage and power factor.",
    "pe-q22": "Analyze the single-phase AC voltage controller with an inductive (RL) load. Discuss the three operating cases based on firing angle alpha and load angle phi, and derive the RMS output voltage.",
    "pe-q23": "Explain the working principle of single-phase to single-phase cycloconverters in mid-point and bridge configurations. Compare circulating and non-circulating current modes.",
    "pe-q24": "Explain the limitations of hard switching in high-frequency converters. Describe the principles and circuit topologies of Zero-Current Switching (ZCS) and Zero-Voltage Switching (ZVS) resonant converters.",
    "pe-q25": "Describe the circuit operation of isolated Switched-Mode Power Supply (SMPS) topologies: Flyback, Forward, Push-Pull, Half-bridge, and Full-bridge converters with comparative evaluation.",
    "pe-q26": "Explain the architectures of Uninterruptible Power Supplies (UPS): Offline, Line-Interactive, and Online Double-Conversion. Discuss the role of the static bypass switch and compare performance metrics."
}
