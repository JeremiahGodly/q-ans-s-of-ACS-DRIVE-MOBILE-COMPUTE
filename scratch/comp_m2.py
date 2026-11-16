# -*- coding: utf-8 -*-
"""
Module 2: Electrical Machines and Power Systems
Questions comp-q6 to comp-q11 for Comprehensive Course Work (EET308).
"""

M2_QUESTIONS = [
    {
        "qid": "comp-q6",
        "marks": 7,
        "type": "Analytical",
        "title": "DC Machines: EMF & Torque Equations, Armature Reaction, Commutation, and Speed Control",
        "yt_query": "dc machine emf torque equation armature reaction commutation speed control",
        "img_path": "images/comp/dc_machine_characteristics.png",
        "img_caption": "Figure 2.1: DC Machine Armature Reaction Flux Distortion and Speed-Torque Characteristics Under Various Control Methods",
        "answer": r"""
Direct Current (DC) machines operate on the fundamental principles of electromagnetic induction (Faraday's law) and electromagnetic Lorentz force ($d\mathbf{F} = I\,d\mathbf{l} \times \mathbf{B}$).

1. Derivation of Generated EMF Equation:
Let:
- $P$ = Number of field poles
- $\Phi$ = Useful magnetic flux per pole in Webers ($\text{Wb}$)
- $Z$ = Total number of active armature conductors
- $N$ = Armature rotational speed in revolutions per minute ($\text{rpm}$)
- $A$ = Number of parallel armature paths ($A = 2$ for wave winding; $A = P$ for lap winding)

In one complete revolution ($1 \text{ rev}$), each conductor cuts the flux of all $P$ poles:
$$\Delta\Phi = P \cdot \Phi \quad \text{Webers}$$
The time taken for one complete revolution is:
$$\Delta t = \frac{60}{N} \quad \text{seconds}$$
According to Faraday's law of electromagnetic induction, the average electromotive force (EMF) induced in a single conductor is:
$$e_{avg} = \frac{\Delta\Phi}{\Delta t} = \frac{P \Phi}{60 / N} = \frac{P \Phi N}{60} \quad \text{Volts}$$
Since the total $Z$ conductors are divided equally into $A$ parallel paths, the number of conductors connected in series per path is $Z / A$.
The total generated EMF (or back EMF $E_b$ in a motor) is the sum of EMFs across conductors in one parallel path:
$$E = \left( \frac{Z}{A} \right) e_{avg} = \frac{P \Phi Z N}{60 A} \quad \text{Volts}$$
Alternatively, in terms of angular mechanical velocity $\omega_m = \frac{2\pi N}{60} \text{ rad/s}$:
$$E = \left( \frac{P Z}{2\pi A} \right) \Phi \omega_m = K_a \Phi \omega_m \quad \text{where } K_a = \frac{P Z}{2\pi A}$$

2. Derivation of Electromagnetic Torque Equation:
The gross electromagnetic power developed in the armature is equal to the mechanical power converted:
$$P_{em} = E_b I_a = T_e \omega_m$$
where $I_a$ is total armature current and $T_e$ is developed electromagnetic torque ($\text{N}\cdot\text{m}$).
Substituting $E_b = K_a \Phi \omega_m$:
$$(K_a \Phi \omega_m) I_a = T_e \omega_m \implies T_e = K_a \Phi I_a$$
$$T_e = \frac{1}{2\pi} \left( \frac{P Z}{A} \right) \Phi I_a = 0.159 \left( \frac{P Z}{A} \right) \Phi I_a \quad \text{N}\cdot\text{m}$$
Torque is directly proportional to both air-gap flux per pole $\Phi$ and armature current $I_a$.

3. Armature Reaction:
Armature reaction is the magnetic effect produced by the armature MMF on the main field magnetic flux distribution in the machine air-gap.
- On No-Load: Only the main field MMF exists, directed along the direct axis ($d$-axis). The flux is symmetrically distributed, and the Magnetic Neutral Axis (MNA)—where no EMF is induced in conductors—coincides exactly with the Geometrical Neutral Axis (GNA).
- On Load: Armature current establishes a cross-magnetizing MMF along the quadrature axis ($q$-axis), perpendicular to the main field.
- Resultant Effects:
  1. Distortion of Air-Gap Flux: The resultant flux is shifted in the direction of rotation for a generator, and against rotation for a motor. The MNA shifts by a mechanical angle $\theta_m$.
  2. Demagnetizing Effect: Due to magnetic saturation in the trailing pole tips (generator) or leading pole tips (motor), the flux increase in the saturated tip is less than the flux decrease in the weakened tip, leading to a net reduction in useful pole flux $\Phi$ ($1-5\%$), reducing generated voltage or increasing motor speed.

Analytical Expressions for Ampere-Turns:
Let $I_c = I_a / A$ be the current per conductor. For an MNA brush lead of $\theta_m$ mechanical degrees:
- Demagnetizing Ampere-Turns per Pole:
$$AT_d = Z I_c \left( \frac{2 \theta_m}{360^\circ} \right) = \frac{Z I_a}{A} \left( \frac{\theta_m}{180^\circ} \right) \quad \implies \quad AT_d = \frac{Z I_a}{2 A P} \left( \frac{2\theta_e}{180^\circ} \right)$$
- Cross-Magnetizing Ampere-Turns per Pole:
$$AT_c = \frac{Z I_a}{2 A P} \left( 1 - \frac{2\theta_e}{180^\circ} \right)$$

4. Commutation and Mitigation:
Commutation is the process by which current in an armature coil is reversed from $+I_c$ to $-I_c$ as the commutator segments connected to the coil pass under a brush during commutation time $T_c$.
Because the coil possesses self-inductance $L_c$, the rapid current reversal induces a self-induced Reactance Voltage:
$$e_r = L_c \frac{di}{dt} \approx 2 L_c \frac{I_c}{T_c}$$
According to Lenz's law, $e_r$ opposes current reversal, resulting in delayed (under-) commutation, which produces destructive sparking at the trailing edge of the brush.
Methods to Ensure Sparkless Commutation:
- Interpoles (Compoles): Small narrow auxiliary poles placed on the GNA between main poles, wound with heavy conductors carrying full armature current $I_a$. They induce a commutating EMF $e_c$ equal and opposite to the reactance voltage ($e_c = -e_r$), neutralizing cross-magnetizing MMF at the neutral zone.
- Compensating Windings: Conductors embedded in axial slots in the main pole faces carrying current in the reverse direction of adjacent armature conductors, neutralizing cross-magnetizing armature MMF directly beneath pole shoes.

5. Speed Control Methods of DC Motors:
From the fundamental voltage equation $V = E_b + I_a R_a = K_a \Phi \omega_m + I_a R_a$:
$$N = \frac{V - I_a R_a}{K' \Phi}$$
- Armature Resistance Control (Rheostatic Control): Adding variable resistance $R_{ext}$ in series with the armature drops voltage, lowering speed below base speed. Disadvantage: high $I_a^2 R_{ext}$ power dissipation, poor efficiency, and poor speed regulation.
- Field Flux Control: Inserting variable resistance in the shunt field circuit reduces field current $I_f$, decreasing $\Phi$ and increasing speed above base speed (constant power drive).
- Armature Voltage Control (Ward-Leonard System): Feeding the DC motor armature from a dedicated motor-generator set or controlled thyristor rectifier allows continuous adjustment of $V_a$ from 0 to rated voltage, providing smooth speed control from zero to base speed in both directions (four-quadrant operation) with high efficiency.
"""
    },
    {
        "qid": "comp-q7",
        "marks": 7,
        "type": "Analytical",
        "title": "Testing of DC Machines: Swinburne's Test and Hopkinson's Regenerative Test",
        "yt_query": "swinburnes test hopkinsons test dc machine efficiency derivation",
        "img_path": "images/comp/dc_testing_hopkinson.png",
        "img_caption": "Figure 2.2: Circuit Connections for (a) Swinburne's No-Load Test and (b) Hopkinson's Regenerative Back-to-Back Test",
        "answer": r"""
Testing of DC machines is necessary to verify performance guarantees, compute losses, predetermine efficiency across operating load cycles, and assess thermal temperature rise. Tests are classified into indirect no-load methods (Swinburne's test) and regenerative back-to-back load methods (Hopkinson's test).

1. Swinburne's Test (No-Load Indirect Method):
Swinburne's test is an indirect method conducted on a DC shunt machine operated as an unloaded motor at rated voltage and rated speed.

Test Procedure & Loss Determination:
The machine is connected to rated supply voltage $V$. The no-load line current $I_{0}$ and shunt field current $I_{sh}$ are recorded.
Armature no-load current is:
$$I_{a0} = I_0 - I_{sh}$$
No-load total power drawn from supply is:
$$P_{in,0} = V I_0$$
This input power supplies the no-load armature copper loss, the shunt field copper loss, and all rotational losses (iron loss and mechanical friction/windage loss):
$$V I_0 = I_{a0}^2 R_a + V I_{sh} + W_{rotational}$$
The Constant Losses $W_c$ of the machine (combining core iron losses, friction, windage, and shunt field copper loss $V I_{sh}$) are:
$$W_c = V I_0 - I_{a0}^2 R_a$$
Since core flux $\Phi$ and speed $N$ remain substantially constant from no-load to full-load in a DC shunt machine, $W_c$ is treated as constant at all loads.

Predetermination of Efficiency at any Arbitrary Load Current $I$:
Let $I$ be the line current at which efficiency is to be evaluated.
Armature resistance $R_a$ is measured and hot-corrected to $75^\circ\text{C}$ ($R_{a,hot} \approx 1.2 R_{a,dc}$).

Case A: Machine Operating as a Motor:
- Armature current: $I_a = I - I_{sh}$
- Armature copper loss: $P_{cu,a} = I_a^2 R_a$
- Total losses: $W_{total} = W_c + I_a^2 R_a$
- Electrical input power: $P_{in} = V I$
- Mechanical output power: $P_{out} = P_{in} - W_{total} = V I - (W_c + I_a^2 R_a)$
- Efficiency as a motor:
$$\eta_m = \frac{P_{out}}{P_{in}} \times 100\% = \frac{V I - W_c - (I - I_{sh})^2 R_a}{V I} \times 100\%$$

Case B: Machine Operating as a Generator:
- Armature current: $I_a = I + I_{sh}$
- Armature copper loss: $P_{cu,a} = I_a^2 R_a$
- Total losses: $W_{total} = W_c + I_a^2 R_a$
- Electrical output power: $P_{out} = V I$
- Mechanical input power: $P_{in} = P_{out} + W_{total} = V I + W_c + (I + I_{sh})^2 R_a$
- Efficiency as a generator:
$$\eta_g = \frac{P_{out}}{P_{in}} \times 100\% = \frac{V I}{V I + W_c + (I + I_{sh})^2 R_a} \times 100\%$$

Advantages and Disadvantages of Swinburne's Test:
- Advantages: Extremely economical; power consumed is only the no-load losses ($< 5\%$ of rated power); efficiency can be predetermined for any load fraction without physical loading.
- Disadvantages: Cannot be applied to DC series motors (which run dangerously overspeed at no-load); iron loss is assumed constant, ignoring armature reaction flux distortion; does not verify commutation quality under load or assess full-load temperature rise.

2. Hopkinson's Test (Regenerative / Back-to-Back Test):
Hopkinson's test overcomes the limitations of Swinburne's test by loading two identical DC shunt machines to full load while drawing only the net losses from the DC supply mains.

Circuit Arrangement and Operating Principle:
Two identical DC shunt machines are mechanically coupled through a shaft and electrically paralleled across the DC mains.
- Starting: Machine 1 is started as a DC shunt motor from supply mains $V$. Machine 2 runs coupled as an unloaded generator.
- Paralleling (Synchronization): The field rheostat of Machine 2 is adjusted until its open-circuit armature voltage $E_2$ equals the supply mains voltage $V$, verified by a zero reading on a voltmeter bridged across the paralleling switch $S$. Switch $S$ is then closed.
- Loading by Field Control: The field excitation of Machine 2 is increased, raising its induced EMF $E_2 > V$. Machine 2 begins delivering current into the common bus, acting as a generator. Simultaneously, the field excitation of Machine 1 is slightly weakened ($E_1 < V$), causing it to draw higher current from the bus and act as a motor driving Generator 2.

Mathematical Formulation of Losses and Separate Efficiencies:
Let:
- $V$ = Supply mains voltage
- $I_1$ = Current supplied by mains
- $I_2$ = Current delivered by Generator 2 to the common bus
- $I_{m} = I_1 + I_2$ = Total armature current drawn by Motor 1
- $I_{f1}, I_{f2}$ = Shunt field currents of Motor 1 and Generator 2
- $R_a$ = Armature resistance of each machine

Power drawn from mains supplies the net total losses of both machines:
$$P_{in,mains} = V I_1 = \text{Total Losses of Both Machines}$$
Field copper losses:
$$P_{f1} = V I_{f1}, \quad P_{f2} = V I_{f2}$$
Armature copper losses:
$$P_{cu,m} = I_m^2 R_a = (I_1 + I_2)^2 R_a$$
$$P_{cu,g} = I_2^2 R_a$$
The combined stray rotational losses (iron, friction, windage) of both machines are:
$$W_{stray,total} = V I_1 - \left[ (I_1 + I_2)^2 R_a + I_2^2 R_a + V I_{f1} + V I_{f2} \right]$$
Assuming identical mechanical and magnetic construction, the stray loss per machine is:
$$W_{stray} = \frac{W_{stray,total}}{2}$$

Efficiency Calculation:
1. Generator Efficiency ($\eta_g$):
- Electrical output: $P_{out,g} = V I_2$
- Generator total losses: $W_{loss,g} = I_2^2 R_a + V I_{f2} + W_{stray}$
$$\eta_g = \frac{V I_2}{V I_2 + I_2^2 R_a + V I_{f2} + W_{stray}} \times 100\%$$

2. Motor Efficiency ($\eta_m$):
- Electrical input: $P_{in,m} = V (I_m + I_{f1}) = V (I_1 + I_2 + I_{f1})$
- Motor total losses: $W_{loss,m} = (I_1 + I_2)^2 R_a + V I_{f1} + W_{stray}$
$$\eta_m = \frac{P_{in,m} - W_{loss,m}}{P_{in,m}} \times 100\% = 1 - \frac{(I_1 + I_2)^2 R_a + V I_{f1} + W_{stray}}{V (I_1 + I_2 + I_{f1})}$$

Advantages of Hopkinson's Test:
- Both machines run under actual full-load electrical, magnetic, and thermal conditions.
- Commutation spark behavior and temperature rise can be accurately monitored over prolonged runs.
- Power drawn from the grid is strictly equal to the machine losses ($< 10-15\%$ of machine rating), making full-load testing of massive megawatt-scale DC machines feasible in industrial testbeds.
"""
    },
    {
        "qid": "comp-q8",
        "marks": 7,
        "type": "Derivation",
        "title": "Transformers: Equivalent Circuit, Regulation, OC/SC Tests, and Autotransformer Copper Saving",
        "yt_query": "transformer equivalent circuit voltage regulation oc sc test autotransformer copper saving",
        "img_path": "images/comp/transformer_equivalent_circuit.png",
        "img_caption": "Figure 2.3: Transformer Exact Equivalent Circuit Referred to Primary and Phasor Diagram for Lagging Power Factor",
        "answer": r"""
The practical transformer differs from an ideal transformer due to finite winding resistances ($R_1, R_2$), leakage magnetic flux giving rise to leakage reactances ($X_1, X_2$), finite core permeability requiring magnetizing current ($I_m$), and core hysteresis/eddy-current losses modeled by core-loss resistance ($R_c$).

1. Exact and Approximate Equivalent Circuits:
Referred to primary winding:
- Transformation ratio: $k = \frac{V_2}{V_1} = \frac{N_2}{N_1} = \frac{I_1'}{I_2}$
- Secondary winding resistance referred to primary: $R_2' = \frac{R_2}{k^2}$
- Secondary leakage reactance referred to primary: $X_2' = \frac{X_2}{k^2}$
- Equivalent total resistance referred to primary: $R_{01} = R_1 + R_2' = R_1 + \frac{R_2}{k^2}$
- Equivalent total leakage reactance referred to primary: $X_{01} = X_1 + X_2' = X_1 + \frac{X_2}{k^2}$
- Excitation shunt branch: Core resistance $R_c$ (accounting for eddy and hysteresis losses) in parallel with magnetizing reactance $X_m$ (accounting for sinusoidal core flux production), connected across primary voltage $V_1$:
$$\mathbf{I}_0 = \mathbf{I}_c + \mathbf{I}_m, \quad I_c = I_0 \cos\phi_0, \quad I_m = I_0 \sin\phi_0$$
$$R_c = \frac{V_1}{I_c} = \frac{V_1}{I_0 \cos\phi_0}, \quad X_m = \frac{V_1}{I_m} = \frac{V_1}{I_0 \sin\phi_0}$$

2. Open-Circuit (OC) and Short-Circuit (SC) Tests:
- Open-Circuit (OC) Test (determines shunt core parameters $R_c, X_m$ and iron loss $P_i$):
  - Conducted on the Low Voltage (LV) side with the High Voltage (HV) side left open-circuited.
  - Rated voltage $V_1$ at rated frequency is applied. Instruments measure $V_0, I_0, W_0$.
  - Since secondary is open, $I_0 \approx 2-5\%$ of full-load current; series winding copper losses ($I_0^2 R_1$) are negligible.
  - Core loss: $P_i = W_0$.
  - No-load power factor: $\cos\phi_0 = \frac{W_0}{V_0 I_0}$.
  - Shunt parameters: $I_c = I_0 \cos\phi_0$, $I_m = I_0 \sin\phi_0 = \sqrt{I_0^2 - I_c^2}$, $R_c = \frac{V_0}{I_c}$, $X_m = \frac{V_0}{I_m}$.
- Short-Circuit (SC) Test (determines series parameters $R_{01}, X_{01}, Z_{01}$ and full-load copper loss $P_{cu}$):
  - Conducted on the High Voltage (HV) side with the Low Voltage (LV) terminals solidly short-circuited.
  - A reduced voltage $V_{sc}$ ($5-10\%$ of rated voltage) is applied to circulate rated full-load current $I_{sc} = I_{1,fl}$.
  - Since applied voltage is very low, core flux $\Phi \propto V_{sc}$ is small, making iron losses completely negligible.
  - Full-load copper loss: $P_{cu,fl} = W_{sc}$.
  - Equivalent parameters referred to HV side:
  $$Z_{01} = \frac{V_{sc}}{I_{sc}}, \quad R_{01} = \frac{W_{sc}}{I_{sc}^2}, \quad X_{01} = \sqrt{Z_{01}^2 - R_{01}^2}$$

3. Voltage Regulation Derivation:
Voltage regulation is the fractional change in secondary terminal voltage from no-load to full-load at a given power factor:
$$\%VR = \frac{V_2^{NL} - V_2^{FL}}{V_2^{FL}} \times 100\% = \frac{E_2 - V_2}{V_2} \times 100\%$$
Referring all quantities to secondary winding:
$$\mathbf{E}_2 = \mathbf{V}_2 + \mathbf{I}_2 (R_{02} + jX_{02}) = V_2 \angle 0^\circ + (I_2 \cos\phi_2 \mp j I_2 \sin\phi_2)(R_{02} + jX_{02})$$
Expanding and taking real and imaginary projections:
$$E_2 \approx V_2 + I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2$$
where $(+)$ is for lagging power factor and $(-)$ is for leading power factor.
$$\%VR \approx \frac{I_2 R_{02} \cos\phi_2 \pm I_2 X_{02} \sin\phi_2}{V_2} \times 100\%$$
- Condition for Zero Voltage Regulation:
$$I_2 R_{02} \cos\phi_2 - I_2 X_{02} \sin\phi_2 = 0 \implies \tan\phi_2 = \frac{R_{02}}{X_{02}} \quad (\text{Leading PF})$$
- Condition for Maximum Voltage Regulation:
$$\frac{d(VR)}{d\phi_2} = 0 \implies -R_{02}\sin\phi_2 + X_{02}\cos\phi_2 = 0 \implies \tan\phi_2 = \frac{X_{02}}{R_{02}} \quad (\text{Lagging PF})$$

4. Efficiency and Condition for Maximum Efficiency:
At fractional load $x$ ($x = I_2 / I_{2,fl}$):
$$\eta = \frac{x S \cos\phi_2}{x S \cos\phi_2 + P_i + x^2 P_{cu,fl}}$$
Differentiating $\eta$ with respect to load current (or fraction $x$) and setting to zero:
$$\frac{d\eta}{dx} = 0 \implies P_i = x^2 P_{cu,fl} \quad \implies \quad \text{Variable Copper Loss} = \text{Constant Iron Loss}$$
The fractional load corresponding to maximum efficiency is:
$$x_{\eta,\max} = \sqrt{\frac{P_i}{P_{cu,fl}}}$$

5. Autotransformers: Operating Principle & Copper Saving Derivation:
An autotransformer uses a single continuous tapped winding common to both primary and secondary circuits.
Power Transfer Mechanism:
Total apparent power transferred consists of two distinct components:
- Inductively transferred power: $S_{ind} = V_1 (I_1 - I_2) = (1 - k) S_{total}$
- Conductively transferred power: $S_{cond} = k S_{total}$

Derivation of Copper Saving:
The weight (volume) of copper in any winding is proportional to the product of number of turns and current rating ($W_{cu} \propto N \cdot I$):
For a Two-Winding Transformer:
$$W_{2-wdg} \propto N_1 I_1 + N_2 I_2$$
Since $N_1 I_1 \approx N_2 I_2$:
$$W_{2-wdg} \propto 2 N_1 I_1$$

For an Autotransformer (Step-Down, $V_1 > V_2, k = V_2/V_1 < 1$):
- Section $AB$ (uncommon part) has $(N_1 - N_2)$ turns carrying current $I_1$.
- Section $BC$ (common part) has $N_2$ turns carrying current $(I_2 - I_1)$.
$$W_{auto} \propto (N_1 - N_2) I_1 + N_2 (I_2 - I_1)$$
$$W_{auto} \propto N_1 I_1 - N_2 I_1 + N_2 I_2 - N_2 I_1 = N_1 I_1 + N_2 I_2 - 2 N_2 I_1$$
Substituting $N_2 I_2 = N_1 I_1$ and $N_2 = k N_1$:
$$W_{auto} \propto 2 N_1 I_1 - 2 (k N_1) I_1 = 2 N_1 I_1 (1 - k)$$
Dividing $W_{auto}$ by $W_{2-wdg}$:
$$\frac{W_{auto}}{W_{2-wdg}} = \frac{2 N_1 I_1 (1 - k)}{2 N_1 I_1} = 1 - k$$
Copper saved by using an autotransformer:
$$\text{Copper Saved} = W_{2-wdg} - W_{auto} = k \cdot W_{2-wdg}$$
When $k \approx 1$ (e.g., $k = 0.9$ for a 220V/200V autotransformer), $90\%$ of the copper is saved, yielding dramatically lower losses, higher efficiency, and compact volume.
"""
    },
    {
        "qid": "comp-q9",
        "marks": 7,
        "type": "Derivation",
        "title": "Three-Phase Induction Motor: Rotating Field, Torque-Slip Equation, and Starting Methods",
        "yt_query": "three phase induction motor rotating magnetic field torque slip characteristics starting methods",
        "img_path": "images/comp/induction_motor_torque_slip.png",
        "img_caption": "Figure 2.4: Three-Phase Induction Motor Torque-Slip Curve Highlighting Operating Modes and Breakdown Torque",
        "answer": r"""
The three-phase induction motor, often called the workhorse of industrial automation, is a singly excited asynchronous machine wherein rotor currents are established entirely via electromagnetic induction from the stator rotating magnetic field.

1. Proof of Rotating Magnetic Field (RMF):
Consider a symmetrical three-phase stator winding with phase coils spatially displaced from each other by $120^\circ$ electrical around the stator bore. Energizing these windings with balanced sinusoidal three-phase currents:
$$i_R(t) = I_m \sin(\omega t)$$
$$i_Y(t) = I_m \sin(\omega t - 120^\circ)$$
$$i_B(t) = I_m \sin(\omega t - 240^\circ) = I_m \sin(\omega t + 120^\circ)$$
Each phase current establishes an alternating spatial flux along its respective magnetic axis:
$$\Phi_R = \Phi_m \sin(\omega t)$$
$$\Phi_Y = \Phi_m \sin(\omega t - 120^\circ)$$
$$\Phi_B = \Phi_m \sin(\omega t + 120^\circ)$$

Evaluating the resultant flux $\mathbf{\Phi}_r$ at different electrical time instants:
- Instant 1: $\omega t = 0$:
  $\Phi_R = 0$
  $\Phi_Y = \Phi_m \sin(-120^\circ) = -\frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_B = \Phi_m \sin(+120^\circ) = +\frac{\sqrt{3}}{2}\Phi_m$
  Resolving along horizontal and vertical axes:
  $$\Phi_{rx} = \Phi_R - \Phi_Y \cos 60^\circ - \Phi_B \cos 60^\circ = 0 - \left(-\frac{\sqrt{3}}{2}\Phi_m\right)\frac{1}{2} - \left(\frac{\sqrt{3}}{2}\Phi_m\right)\frac{1}{2} = 0$$
  $$\Phi_{ry} = 0 - \Phi_Y \sin 60^\circ + \Phi_B \sin 60^\circ = -\left(-\frac{\sqrt{3}}{2}\Phi_m\right)\frac{\sqrt{3}}{2} + \left(\frac{\sqrt{3}}{2}\Phi_m\right)\frac{\sqrt{3}}{2} = \frac{3}{4}\Phi_m + \frac{3}{4}\Phi_m = \frac{3}{2}\Phi_m$$
  Resultant magnitude:
  $$\Phi_r = \sqrt{\Phi_{rx}^2 + \Phi_{ry}^2} = \frac{3}{2}\Phi_m = 1.5 \Phi_m \quad \text{directed at } 90^\circ$$

- Instant 2: $\omega t = 60^\circ$:
  $\Phi_R = \Phi_m \sin 60^\circ = \frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_Y = \Phi_m \sin(-60^\circ) = -\frac{\sqrt{3}}{2}\Phi_m$
  $\Phi_B = \Phi_m \sin(180^\circ) = 0$
  Computing the resultant:
  $$\Phi_r = 2 \left( \frac{\sqrt{3}}{2}\Phi_m \right) \cos 30^\circ = 2 \left( \frac{\sqrt{3}}{2}\Phi_m \right)\frac{\sqrt{3}}{2} = \frac{3}{2}\Phi_m = 1.5 \Phi_m \quad \text{rotated by } 60^\circ$$

General Mathematical Proof:
Using trigonometric identities for any arbitrary $\omega t$:
$$\Phi_r(\theta, t) = \Phi_m \sin\omega t \cos\theta + \Phi_m \sin(\omega t - 120^\circ)\cos(\theta - 120^\circ) + \Phi_m \sin(\omega t + 120^\circ)\cos(\theta + 120^\circ)$$
Using the product-to-sum identity $\sin A \cos B = \frac{1}{2}[\sin(A - B) + \sin(A + B)]$:
$$\Phi_r(\theta, t) = \frac{3}{2}\Phi_m \sin(\omega t - \theta)$$
This represents a traveling magnetic wave of constant magnitude $1.5 \Phi_m$ revolving uniformly around the air-gap at Synchronous Speed:
$$N_s = \frac{120 f}{P} \quad \text{rpm} \quad \text{or} \quad \omega_s = \frac{4\pi f}{P} \quad \text{rad/s}$$

2. Slip and Rotor Electrical Parameters:
Slip $s$ is the fractional difference between synchronous speed and rotor speed $N$:
$$s = \frac{N_s - N}{N_s} \implies N = N_s (1 - s)$$
- Rotor induced frequency: $f_r = s f$
- Rotor induced EMF at slip $s$: $E_{2s} = s E_2$
- Rotor standstill leakage reactance: $X_2 = 2\pi f L_2$
- Rotor running leakage reactance: $X_{2s} = 2\pi f_r L_2 = s X_2$
- Rotor current per phase:
$$I_2 = \frac{E_{2s}}{\sqrt{R_2^2 + X_{2s}^2}} = \frac{s E_2}{\sqrt{R_2^2 + (s X_2)^2}} = \frac{E_2}{\sqrt{(R_2/s)^2 + X_2^2}}$$
- Rotor power factor: $\cos\phi_2 = \frac{R_2}{\sqrt{R_2^2 + (s X_2)^2}} = \frac{R_2/s}{\sqrt{(R_2/s)^2 + X_2^2}}$

3. Derivation of Electromagnetic Torque Equation:
The total mechanical air-gap power transferred across the stator-rotor boundary for a 3-phase motor is:
$$P_g = 3 I_2^2 \left(\frac{R_2}{s}\right) = 3 \left( \frac{s^2 E_2^2}{R_2^2 + s^2 X_2^2} \right) \frac{R_2}{s} = \frac{3 s E_2^2 R_2}{R_2^2 + s^2 X_2^2}$$
Rotor copper loss: $P_{cu,rotor} = 3 I_2^2 R_2 = s P_g$.
Gross mechanical power developed: $P_{mech} = P_g - P_{cu,rotor} = (1 - s) P_g$.
Electromagnetic torque $T_e$ is air-gap power divided by synchronous mechanical speed:
$$T_e = \frac{P_{mech}}{\omega_m} = \frac{(1 - s) P_g}{(1 - s)\omega_s} = \frac{P_g}{\omega_s}$$
$$T_e = \frac{3}{\omega_s} \cdot \frac{s E_2^2 R_2}{R_2^2 + (s X_2)^2} \quad \text{N}\cdot\text{m}$$

Analysis of Torque-Slip Characteristics:
- Low-Slip Region (Normal Operation, $s \ll 1$):
  Here $(s X_2)^2 \ll R_2^2$, so the reactance term is negligible:
  $$T_e \approx \frac{3}{\omega_s} \frac{s E_2^2}{R_2} \implies T_e \propto s$$
  Torque varies linearly with slip; the motor operates stably with high efficiency.
- High-Slip Region ($s \to 1$, Starting Condition):
  Here $(s X_2)^2 \gg R_2^2$, so resistance is negligible:
  $$T_e \approx \frac{3}{\omega_s} \frac{s E_2^2 R_2}{s^2 X_2^2} = \frac{3 E_2^2 R_2}{\omega_s X_2^2} \cdot \frac{1}{s} \implies T_e \propto \frac{1}{s}$$
  Torque is inversely proportional to slip (unstable region).

Condition for Maximum (Breakdown) Torque ($T_{max}$):
Differentiating $T_e$ with respect to slip $s$ and setting $\frac{dT_e}{ds} = 0$:
$$\frac{d}{ds}\left[ \frac{s}{R_2^2 + s^2 X_2^2} \right] = \frac{(R_2^2 + s^2 X_2^2)\cdot 1 - s(2s X_2^2)}{(R_2^2 + s^2 X_2^2)^2} = 0$$
$$R_2^2 - s^2 X_2^2 = 0 \implies s_{\max} = \frac{R_2}{X_2}$$
Maximum torque occurs at a slip equal to the ratio of rotor resistance to standstill reactance.
Substituting $s_{\max} = R_2 / X_2$ into the torque equation:
$$T_{\max} = \frac{3}{\omega_s} \frac{(R_2 / X_2) E_2^2 R_2}{R_2^2 + (R_2 / X_2)^2 X_2^2} = \frac{3}{\omega_s} \frac{(R_2^2 / X_2) E_2^2}{2 R_2^2}$$
$$T_{\max} = \frac{3}{2 \omega_s} \frac{E_2^2}{X_2}$$
Key Insight: Maximum breakdown torque is completely independent of rotor resistance $R_2$. Adding external resistance to a wound-rotor induction motor shifts the point of maximum torque toward standstill ($s = 1$), enabling maximum torque at starting ($s_{max} = 1$ when $R_2 = X_2$) without diminishing $T_{max}$.

4. Starting Methods of Three-Phase Induction Motors:
Direct-On-Line (DOL) starting draws $5-7$ times rated full-load current ($I_{st} = 5 \text{ to } 7 I_{fl}$), causing unacceptable network voltage sags.
- Star-Delta ($\text{Y}-\Delta$) Starter:
  Windings are connected in Star during starting, then switched to Delta after acceleration ($> 80\% N_s$).
  - Starting phase voltage: $V_{ph,Y} = V_L / \sqrt{3}$
  - Starting line current: $I_{st,Y} = \frac{V_L / \sqrt{3}}{Z_{st}} = \frac{1}{3} \left( \frac{\sqrt{3} V_L}{Z_{st}} \right) = \frac{1}{3} I_{st,\Delta}$
  - Starting torque: $T_{st,Y} = \frac{1}{3} T_{st,\Delta}$
  Both starting current and starting torque are reduced to exactly one-third ($33.3\%$) of their DOL values.
- Auto-Transformer Starter:
  Tappings on an autotransformer supply a fraction $x$ ($x = 0.5, 0.65, 0.8$) of line voltage to the stator:
  - Motor terminal voltage: $V_{st} = x V_L$
  - Motor starting current: $I_{motor} = x I_{sc}$
  - Line starting current drawn from mains: $I_{line} = x \cdot I_{motor} = x^2 I_{sc}$
  - Starting torque: $T_{st} = x^2 T_{sc} = x^2 \left( \frac{I_{sc}}{I_{fl}} \right)^2 s_{fl} T_{fl}$
"""
    },
    {
        "qid": "comp-q10",
        "marks": 7,
        "type": "Derivation",
        "title": "Synchronous Machines: Regulation Methods (EMF/MMF) & Two-Reaction Theory",
        "yt_query": "synchronous machine voltage regulation emf mmf method two reaction theory",
        "img_path": "images/comp/synchronous_machine_phasor.png",
        "img_caption": "Figure 2.5: Blondel Two-Reaction Phasor Diagram for Salient Pole Alternator and Power-Angle Curve",
        "answer": r"""
Synchronous machines are doubly excited AC machines operating strictly at synchronous speed $N_s = 120 f / P$. Their voltage regulation under changing load power factor is a critical stability parameter.

1. Generated EMF Equation & Winding Factors:
For a 3-phase alternator with flux per pole $\Phi$ ($\text{Wb}$), frequency $f$ ($\text{Hz}$), and series turns per phase $T_{ph}$:
$$E_{ph} = 4.44 k_p k_d f \Phi T_{ph} \quad \text{Volts}$$
- Pitch Factor (Chording Factor) $k_p$: Accounts for short-pitching coils by chording angle $\alpha$:
$$k_p = \cos\left( \frac{\alpha}{2} \right)$$
Short pitching eliminates specific harmonic orders (e.g., setting $\alpha = 180^\circ / n$ eliminates the $n$-th harmonic) and reduces end-turn copper volume.
- Distribution (Breadth) Factor $k_d$: Accounts for distributing coils over $m$ slots per pole per phase with slot pitch angle $\beta = 180^\circ / (\text{slots/pole})$:
$$k_d = \frac{\sin(m\beta / 2)}{m \sin(\beta / 2)}$$

2. Voltage Regulation Determination:
Voltage regulation is defined as:
$$\%VR = \frac{|E_{0}| - |V|}{V} \times 100\%$$
where $E_0$ is the no-load open-circuit terminal voltage for the same excitation field current $I_f$ that yields rated terminal voltage $V$ at rated load.

Method A: Synchronous Impedance (EMF) Method:
1. Conduct Open-Circuit Test to obtain the Open-Circuit Characteristic (OCC: $V_{oc}$ vs $I_f$).
2. Conduct Short-Circuit Test to obtain the Short-Circuit Characteristic (SCC: $I_{sc}$ vs $I_f$).
3. For a specific field current $I_f$:
$$Z_s = \left. \frac{V_{oc,ph}}{I_{sc,ph}} \right|_{I_f = \text{const}}$$
4. Measure DC armature resistance and correct for skin effect: $R_a \approx 1.25 R_{dc}$.
5. Calculate Synchronous Reactance: $X_s = \sqrt{Z_s^2 - R_a^2}$.
6. Determine No-Load EMF $E_0$ from phasor analysis:
$$\mathbf{E}_0 = \mathbf{V} + \mathbf{I}_a (R_a + jX_s) = (V\cos\phi + I_a R_a) + j(V\sin\phi \pm I_a X_s)$$
$$E_0 = \sqrt{(V\cos\phi + I_a R_a)^2 + (V\sin\phi \pm I_a X_s)^2}$$
where $(+)$ is used for lagging PF and $(-)$ for leading PF.
Critique: The EMF method assumes magnetic linearity and uses unsaturated $Z_s$. Because saturation lowers the actual reactance, the EMF method yields an $E_0$ larger than the real value, predicting higher regulation. Hence, it is known as the Pessimistic Method.

Method B: MMF (Ampere-Turn / Rothert's) Method:
The MMF method treats armature reaction as an MMF rather than a fictitious reactance drop:
1. Determine $F_{f1}$: Field current required to generate rated terminal voltage $V$ on OCC plus armature resistance drop.
2. Determine $F_{ar}$: Field current required to circulate rated armature current on SCC against armature reaction and leakage reactance.
3. Combine field MMF vectors at an angle of $(90^\circ \pm \phi)$:
$$F_R = \sqrt{F_{f1}^2 + F_{ar}^2 - 2 F_{f1} F_{ar} \cos(90^\circ + \phi)} = \sqrt{F_{f1}^2 + F_{ar}^2 + 2 F_{f1} F_{ar} \sin\phi}$$
4. From the OCC curve, read $E_0$ corresponding to resultant field current $F_R$.
Critique: Because it understates saturation, the MMF method yields an $E_0$ smaller than the actual value. Hence, it is known as the Optimistic Method.

3. Blondel's Two-Reaction Theory for Salient Pole Alternators:
In salient pole machines, the air-gap is non-uniform: it is minimal along the direct axis ($d$-axis, center of pole) and maximal along the quadrature axis ($q$-axis, interpolar space). Consequently, the reluctance along the $q$-axis is much higher than along the $d$-axis:
$$\mathcal{R}_q \gg \mathcal{R}_d \implies X_d > X_q$$
where $X_d$ is direct-axis synchronous reactance and $X_q$ is quadrature-axis synchronous reactance.

Armature Current Resolution:
Armature current $\mathbf{I}_a$ is resolved into two orthogonal components:
- Direct-axis current $I_d = I_a \sin(\delta + \phi)$ (produces flux purely along $d$-axis).
- Quadrature-axis current $I_q = I_a \cos(\delta + \phi)$ (produces flux purely along $q$-axis).
where $\delta$ is the power (rotor) angle and $\phi$ is the load power factor angle.

Terminal Voltage Phasor Equation:
$$\mathbf{E}_0 = \mathbf{V} + I_a R_a + j I_d X_d + j I_q X_q$$
Projecting along the $d$ and $q$ axes (neglecting $R_a$):
$$V\sin\delta = I_q X_q \implies I_q = \frac{V\sin\delta}{X_q}$$
$$E_0 = V\cos\delta + I_d X_d \implies I_d = \frac{E_0 - V\cos\delta}{X_d}$$

Determination of Power Angle $\delta$:
From the geometry of the phasor diagram:
$$\tan\delta = \frac{I_a X_q \cos\phi \pm I_a R_a \sin\phi}{V + I_a X_q \sin\phi \mp I_a R_a \cos\phi}$$
Once $\delta$ is calculated, $I_d$ and $I_q$ are determined, and excitation EMF is:
$$E_0 = V\cos\delta + I_d X_d + I_q R_a$$

Power-Angle Equation & Reluctance Torque:
Total electrical power delivered per phase is:
$$P = V I_a \cos\phi = V (I_q \cos\delta + I_d \sin\delta)$$
Substituting $I_d$ and $I_q$:
$$P = V \left( \frac{V\sin\delta}{X_q} \cos\delta + \frac{E_0 - V\cos\delta}{X_d} \sin\delta \right) = \frac{E_0 V}{X_d}\sin\delta + V^2 \sin\delta\cos\delta \left( \frac{1}{X_q} - \frac{1}{X_d} \right)$$
Using $\sin\delta\cos\delta = \frac{1}{2}\sin 2\delta$:
$$P = \frac{E_0 V}{X_d}\sin\delta + \frac{V^2}{2}\left( \frac{X_d - X_q}{X_d X_q} \right)\sin 2\delta$$
Physical Interpretation:
- First Term $\frac{E_0 V}{X_d}\sin\delta$: Fundamental Electromagnetic Excitation Power, arising from interaction between rotor field excitation and stator field.
- Second Term $\frac{V^2}{2}\left( \frac{X_d - X_q}{X_d X_q} \right)\sin 2\delta$: Reluctance Power, independent of field excitation $E_0$. It arises entirely from the saliency of the rotor ($X_d \neq X_q$), which causes the rotor to align with the minimum-reluctance position of the air-gap rotating field. Even if field excitation is completely lost ($E_0 = 0$), a salient-pole alternator can still deliver stable reluctance power up to $\delta = 45^\circ$.
"""
    },
    {
        "qid": "comp-q11",
        "marks": 7,
        "type": "Analytical",
        "title": "Power Systems Analysis: Modeling, Fault Analysis, and Transient Stability",
        "yt_query": "power systems symmetrical components unsymmetrical fault swing equation equal area criterion",
        "img_path": "images/comp/power_system_stability_eac.png",
        "img_caption": "Figure 2.6: Symmetrical Component Interconnections for Asymmetrical Faults and Equal Area Criterion Stability Plot",
        "answer": r"""
Modern electrical power systems demand rigorous analytical modeling to ensure continuous stability under dynamic electromechanical disturbances and fault contingencies.

1. Transmission Line ABCD Parameters:
Transmission lines are represented as two-port four-terminal networks relating sending-end voltage/current to receiving-end quantities:
$$\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix}$$
Properties of passive linear reciprocal transmission lines:
- Reciprocity: $A D - B C = 1$
- Symmetry: $A = D$ (for identical bilateral lines)

Line Classifications:
- Short Line ($L < 80\text{ km}$, shunt capacitance neglected):
  $$A = D = 1, \quad B = Z = R + j\omega L, \quad C = 0$$
- Medium Line ($80\text{ km} \le L \le 250\text{ km}$):
  - Nominal-$\pi$ Model (total admittance $Y$ split equally at ends $Y/2$):
  $$A = D = 1 + \frac{Y Z}{2}, \quad B = Z, \quad C = Y\left(1 + \frac{Y Z}{4}\right)$$
  - Nominal-T Model (total impedance $Z$ split equally $Z/2$):
  $$A = D = 1 + \frac{Y Z}{2}, \quad B = Z\left(1 + \frac{Y Z}{4}\right), \quad C = Y$$

2. Per-Unit (pu) Representation:
The per-unit value simplifies computational analysis across multiple voltage levels:
$$\text{Value}_{pu} = \frac{\text{Actual Value}}{\text{Base Value}}$$
Base impedance: $Z_{base} = \frac{(V_{base,LL})^2}{S_{base,3\phi}} \ \Omega$.
Base change formula:
$$Z_{pu}^{new} = Z_{pu}^{old} \times \left( \frac{V_{base}^{old}}{V_{base}^{new}} \right)^2 \times \left( \frac{S_{base}^{new}}{S_{base}^{old}} \right)$$

3. Symmetrical and Unsymmetrical Fault Analysis:
Symmetrical (Three-Phase) Fault:
All three phases short simultaneously. The system remains balanced; per-phase analysis using Thévenin equivalent impedance $Z_{th} = Z_1$ suffices:
$$I_f = \frac{V_f}{Z_1 + Z_f}, \quad \text{Short-Circuit MVA} = \sqrt{3} V_L I_f = \frac{\text{Base MVA}}{Z_{pu}}$$

Unsymmetrical Fault Analysis via Symmetrical Components:
Fortescue's Theorem resolves any unbalanced set of 3-phase vectors into three symmetrical components:
$$\begin{bmatrix} \mathbf{I}_a \\ \mathbf{I}_b \\ \mathbf{I}_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} \mathbf{I}_{a0} \\ \mathbf{I}_{a1} \\ \mathbf{I}_{a2} \end{bmatrix}$$
where $a = 1 \angle 120^\circ = -0.5 + j0.866$, and $a^2 = 1 \angle 240^\circ$.

Sequence Network Connections for Shunt Faults:
1. Single Line-to-Ground (SLG) Fault (Phase 'a' to ground):
   - Boundary conditions: $I_b = 0, I_c = 0, V_a = I_a Z_f$.
   - Symmetrical components: $I_{a0} = I_{a1} = I_{a2} = \frac{1}{3}I_a$.
   - Network Interconnection: Positive, Negative, and Zero sequence networks connected in series:
   $$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$
   $$I_f = I_a = 3 I_{a1} = \frac{3 E_a}{Z_1 + Z_2 + Z_0 + 3 Z_f}$$
2. Line-to-Line (LL) Fault (Between Phase 'b' and Phase 'c'):
   - Boundary conditions: $I_a = 0, I_b = -I_c, V_b - V_c = I_b Z_f$.
   - Sequence components: $I_{a0} = 0, I_{a2} = -I_{a1}$.
   - Network Interconnection: Positive and Negative sequence networks connected in parallel opposing:
   $$I_{a1} = \frac{E_a}{Z_1 + Z_2 + Z_f}$$
   $$I_f = I_b = -j\sqrt{3} I_{a1}$$
3. Double Line-to-Ground (DLG) Fault (Phases 'b' and 'c' to ground):
   - Boundary conditions: $I_a = 0, V_b = V_c = (I_b + I_c)Z_f$.
   - Network Interconnection: Positive, Negative, and Zero sequence networks connected in parallel:
   $$I_{a1} = \frac{E_a}{Z_1 + \frac{Z_2 (Z_0 + 3 Z_f)}{Z_2 + Z_0 + 3 Z_f}}$$

4. Rotor Dynamics & The Swing Equation:
The electromechanical equation governing rotor angular motion of a synchronous generator is derived from Newton's second law:
$$J \frac{d^2\theta_m}{dt^2} = T_m - T_e = T_a$$
where $J$ is moment of inertia ($\text{kg}\cdot\text{m}^2$), $\theta_m$ is mechanical rotor position, $T_m$ is shaft mechanical torque, $T_e$ is electromagnetic torque, and $T_a$ is accelerating torque.
Expressing angular position relative to synchronously rotating reference frame: $\theta_m = \omega_{sm} t + \delta_m$.
Differentiating twice: $\frac{d^2\theta_m}{dt^2} = \frac{d^2\delta_m}{dt^2}$.
Multiplying both sides by synchronous speed $\omega_{sm}$:
$$J \omega_{sm} \frac{d^2\delta_m}{dt^2} = P_m - P_e$$
Defining the Angular Momentum $M = J \omega_{sm}$ and Inertia Constant $H$:
$$H = \frac{\text{Stored Kinetic Energy at Synchronous Speed}}{\text{Machine Rating } S_n} = \frac{\frac{1}{2} J \omega_{sm}^2}{S_n} \ \frac{\text{MJ}}{\text{MVA}}$$
$$M = \frac{2 H S_n}{\omega_s} \quad \implies \quad M \frac{d^2\delta}{dt^2} = P_m - P_e$$
In per-unit form:
$$\frac{2 H}{\omega_s} \frac{d^2\delta}{dt^2} = P_{m,pu} - P_{e,pu}$$
where $\omega_s = 2\pi f$ ($\text{rad/s}$) and $P_e = P_{max} \sin\delta$. This non-linear second-order differential equation is the Swing Equation.

5. Transient Stability & The Equal Area Criterion:
For a single machine connected to an infinite bus (SMIB), stability following a disturbance can be assessed without numerically solving the non-linear swing equation by applying the Equal Area Criterion.
Multiplying the swing equation by $2 \frac{d\delta}{dt}$:
$$2 \frac{d\delta}{dt} \frac{d^2\delta}{dt^2} = \frac{\omega_s}{M}(P_m - P_e)\frac{d\delta}{dt} \implies \frac{d}{dt}\left[ \left(\frac{d\delta}{dt}\right)^2 \right] = \frac{2\omega_s}{M}(P_m - P_e)\frac{d\delta}{dt}$$
Integrating from initial angle $\delta_0$ to maximum swing angle $\delta_{max}$:
$$\left( \frac{d\delta}{dt} \right)^2 = \frac{2\omega_s}{M} \int_{\delta_0}^{\delta_{max}} (P_m - P_e) d\delta$$
For the system to remain stable, the rotor speed deviation $\frac{d\delta}{dt}$ must return to zero at some maximum angle $\delta_{max}$, meaning:
$$\int_{\delta_0}^{\delta_{max}} (P_m - P_e) d\delta = 0$$
Dividing into accelerating ($A_1$) and decelerating ($A_2$) energy areas:
$$A_1 = \int_{\delta_0}^{\delta_{cr}} (P_m - P_e^{fault}) d\delta = A_2 = \int_{\delta_{cr}}^{\delta_{max}} (P_e^{post} - P_m) d\delta$$
- Critical Clearing Angle ($\delta_{cr}$): The maximum allowable angle at which circuit breakers can isolate the fault such that $A_1 = A_2$.
For a fault cleared on an unmodified system with $P_e^{fault} = 0$:
$$P_m (\delta_{cr} - \delta_0) = \int_{\delta_{cr}}^{\delta_{max}} (P_{max}\sin\delta - P_m) d\delta$$
$$\cos\delta_{cr} = \frac{P_m}{P_{max}}(\delta_{max} - \delta_0) + \cos\delta_{max}$$
where $\delta_{max} = \pi - \delta_0$. If the fault is cleared before $\delta$ reaches $\delta_{cr}$, the system successfully decelerates and remains transiently stable.
"""
    }
]
