# scratch/drive_lecturer_bank.py
# Complete KTU Exam-Ready Answers for Subject 2: Electric Drives (EET411 / EE402)
# Written in simple, direct local English with rich core content, clear bullet points,
# step-by-step mathematical derivations, comparison tables, and intuitive everyday engineering analogies.

DRIVE_ANSWERS = {
    # =========================================================================
    # MODULE 1: Drive Dynamics, Fundamental Torque Equations & Four-Quadrant
    # =========================================================================
    'drive-q1': {
        "title": "Elements and Block Diagram of Modern Electric Drive Systems",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Power Source $\\to$ Power Modulator (Converter) $\\to$ Motor $\\to$ Load; regulated via Sensing Unit $\\to$ Control Unit."
        },
        "exam_answer": r"""
<p><strong>1. Definition:</strong><br>
An electric drive is an electromechanical system designed to convert electrical energy into precisely controlled mechanical motion for industrial machinery.</p>

<p><strong>2. Core Functional Blocks &amp; Their Roles:</strong></p>
<ol>
    <li><strong>Electrical Power Source:</strong> Provides raw electrical energy. It can be 1-phase or 3-phase AC from the utility grid ($50\text{ Hz}, 415\text{ V}$) or DC from a battery/DC bus.</li>
    <li><strong>Power Modulator (Converter):</strong> Converts power from the source into the exact voltage, current, and frequency required by the motor.
        <ul>
            <li>Controls speed and torque smoothly during starting, steady-state, and braking.</li>
            <li>Restricts motor starting current to safe limits.</li>
            <li>Types: Controlled rectifiers (AC to DC), inverters (DC to AC), choppers (DC to DC), cycloconverters (AC to AC).</li>
        </ul>
    </li>
    <li><strong>Electric Motor:</strong> Converts modulated electrical energy into rotational mechanical torque. (DC shunt/series motors, 3-phase induction motors, BLDC, PMSM, or stepper motors).</li>
    <li><strong>Mechanical Load:</strong> The industrial machine performing useful work (e.g., pumps, fans, cranes, hoists, electric trains, rolling mills).</li>
    <li><strong>Sensing Unit:</strong> Measures actual system parameters—motor speed ($\omega$), shaft torque ($T$), rotor position ($\theta$), and motor phase currents ($I$).</li>
    <li><strong>Control Unit:</strong> Compares measured feedback signals with user reference setpoints (desired speed/torque) and generates firing pulses (PWM) to control the power modulator switches.</li>
</ol>
""",
        "understand_simply": r"""
<p>An electric drive is like an electric car's powertrain:</p>
<ul>
    <li>The battery is the <strong>Power Source</strong>.</li>
    <li>The inverter is the <strong>Power Modulator</strong> (adjusting how much power flows).</li>
    <li>The electric motor turns the wheels (the <strong>Load</strong>).</li>
    <li>The accelerator pedal and speedometer act as the <strong>Control and Sensing Units</strong> telling the motor exactly how fast to spin.</li>
</ul>
"""
    },

    'drive-q2': {
        "title": "Advantages of Electric Drives in Industrial Motion Control",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "High efficiency (>90%), zero point-of-use emissions, instant start/acceleration, flexible 4-quadrant control, regenerative braking."
        },
        "exam_answer": r"""
<p>Electric drives have replaced traditional mechanical, steam, and diesel drives in modern industries due to five major technical advantages:</p>
<ol>
    <li><strong>High Efficiency &amp; Low Operating Cost:</strong> Electric motors achieve $85\%\text{ to } 96\%$ energy conversion efficiency, compared to only $25\%\text{ to } 40\%$ for internal combustion (diesel/petrol) engines. No fuel is wasted during idle periods.</li>
    <li><strong>Smooth Speed Control &amp; Wide Range:</strong> Speed can be adjusted smoothly from zero to several times rated base speed in both forward and reverse directions without mechanical gears.</li>
    <li><strong>Instant Starting and High Starting Torque:</strong> Electric motors can develop rated or peak torque immediately at standstill, enabling rapid acceleration under heavy loads (e.g., electric trains, traction).</li>
    <li><strong>Regenerative Braking Capability:</strong> When stopping or lowering loads, mechanical kinetic energy is converted back into electrical power and returned to the supply grid, saving substantial electricity.</li>
    <li><strong>Clean, Compact &amp; Safe Operation:</strong> Produces zero smoke or exhaust fumes at point of use, operates with low noise, requires minimal maintenance, and can operate safely in hazardous, submerged, or explosive environments (mining, cleanrooms).</li>
</ol>
""",
        "understand_simply": r"""
<p>Compare an electric metro train with an old diesel train: the electric train accelerates quietly and quickly, uses no fuel while waiting at stations, pumps power back into the grid every time it brakes, and leaves zero smoke inside underground tunnels!</p>
"""
    },

    'drive-q3': {
        "title": "Classification and Nature of Industrial Load Torques",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Active torques (gravity) retain direction upon speed reversal; Passive torques (friction, fan $\\propto \\omega^2$) always oppose motion."
        },
        "exam_answer": r"""
<p><strong>1. Basis of Classification:</strong><br>
Industrial load torques are classified into two broad categories based on whether their directional sign depends on the direction of motor rotation:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Feature</th>
            <th>Active Load Torques</th>
            <th>Passive Load Torques</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Physical Origin</strong></td>
            <td>Gravitational potential energy, elastic deformation of springs, tension in suspended cables.</td>
            <td>Friction (dry, viscous, fluid), mechanical cutting, fluid drag, material deformation.</td>
        </tr>
        <tr>
            <td><strong>Directional Behavior</strong></td>
            <td><strong>Retains its directional sign</strong> regardless of whether the motor rotates in forward or reverse direction.</td>
            <td><strong>Always opposes the direction of rotation.</strong> Its sign automatically reverses when motor rotation reverses.</td>
        </tr>
        <tr>
            <td><strong>Action as Prime Mover</strong></td>
            <td>Capable of driving the motor shaft independently (can act as a prime mover, e.g., falling hoist load).</td>
            <td>Cannot drive the motor shaft by itself; only absorbs and dissipates mechanical energy.</td>
        </tr>
        <tr>
            <td><strong>Torque Equations &amp; Examples</strong></td>
            <td>Constant torque: $T_L = \text{const}$<br><em>Examples:</em> Hoist gravitational load, elevator counterweight, coiled spring.</td>
            <td>Coloumb friction: $T_L \propto \operatorname{sign}(\omega)$<br>Fan/Pump load: $T_L \propto \omega^2$<br>Lathe cutting tool: $T_L \propto 1/\omega$.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Think about a cart on a hilly road:</p>
<ul>
    <li><strong>Active Load:</strong> Gravity pulling the cart downhill is an active load. Whether you push the cart uphill or roll it downhill, gravity always pulls in the exact same downward direction.</li>
    <li><strong>Passive Load:</strong> Wheel friction is a passive load. If you push the cart forward, friction pushes backward. If you pull the cart backward, friction pushes forward. Friction always resists motion!</li>
</ul>
"""
    },

    'drive-q3b': {
        "title": "Critical Speed and Torsional Resonance in Electric Drives",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\omega_{cr} = \sqrt{\frac{K_{sh}}{J_{eq}}}, \quad \omega_{\text{operating}} \ne \omega_{cr}$$",
            "text": "Critical speed occurs when rotational speed matches the natural torsional resonant frequency of the motor-load shaft."
        },
        "exam_answer": r"""
<p><strong>1. Physical Concept:</strong></p>
<ul>
    <li>Any real mechanical shaft connecting a motor to an industrial load acts like a torsional spring with finite stiffness $K_{sh}$ ($\text{N}\cdot\text{m/rad}$) and inertia $J$.</li>
    <li>The shaft has a natural torsional resonant frequency:
    $$\omega_{n} = \sqrt{\frac{K_{sh}}{J_{eq}}}$$</li>
    <li>When the motor rotational speed (or torque ripple harmonic frequency from inverter switching) matches this natural frequency, <strong>torsional resonance</strong> occurs.</li>
</ul>

<p><strong>2. Effects of Operating at Critical Speed:</strong></p>
<ul>
    <li>Severe mechanical vibrations and violent angular oscillations.</li>
    <li>Excessive shaft shear stress leading to fatigue failure and shaft breakage.</li>
    <li>Rapid bearing wear, gear tooth pitting, and acoustic noise.</li>
</ul>

<p><strong>3. Mitigation &amp; Design Remedies:</strong></p>
<ul>
    <li><strong>Skip Frequencies (Band Avoidance):</strong> Drive inverters are programmed with "skip frequency bands" so the motor accelerates rapidly through the critical speed without dwelling there.</li>
    <li><strong>Flexible Couplings:</strong> Installing elastomeric or fluid couplings to add mechanical damping.</li>
    <li><strong>Active Vibration Damping:</strong> Using notch filters or state feedback control in the drive firmware to cancel resonance.</li>
</ul>
""",
        "understand_simply": r"""
<p>Have you ever noticed an old ceiling fan or washing machine that shakes violently at one particular medium speed, but runs smoothly when you click it to full speed? That violent shaking speed is the <strong>critical speed</strong>. The spin frequency matches the natural vibration of the machine, causing resonance.</p>
"""
    },

    'drive-q4': {
        "title": "Mathematical Derivation of the Fundamental Dynamic Torque Equation",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$T - T_L = J \frac{d\omega_m}{dt} + \omega_m \frac{dJ}{dt} \implies T - T_L = J \frac{d\omega_m}{dt}$$",
            "text": r"Net accelerating torque $(T - T_L)$ accelerates rotor inertia $J$. $T > T_L \implies$ Acceleration; $T < T_L \implies$ Deceleration."
        },
        "exam_answer": r"""
<p><strong>1. Fundamental Physical Principle:</strong><br>
According to Newton's second law for rotational motion, the net resultant torque acting on a motor-load combination equals the time rate of change of angular momentum:</p>
$$T_{\text{net}} = \frac{d}{dt}\left( J \omega_m \right)$$
where:
<ul>
    <li>$T = \text{Motor developed electromagnetic torque (N}\cdot\text{m)}$</li>
    <li>$T_L = \text{Total resisting load torque referred to the motor shaft (N}\cdot\text{m)}$</li>
    <li>$J = \text{Combined polar moment of inertia of motor and load (kg}\cdot\text{m}^2)$</li>
    <li>$\omega_m = \text{Rotor angular velocity (rad/s)}$</li>
</ul>

<p><strong>2. Step-by-Step Derivation:</strong></p>
<p>Expanding the derivative of the product $(J \omega_m)$ using the chain rule:
$$T - T_L = J \frac{d\omega_m}{dt} + \omega_m \frac{dJ}{dt} \quad \text{--- (1)}$$</p>
<p>For most industrial electric drives, the moment of inertia is constant over time ($\frac{dJ}{dt} = 0$).<br>
Equation (1) simplifies to the <strong>Fundamental Dynamic Torque Equation</strong>:
$$T - T_L = J \frac{d\omega_m}{dt} \quad \text{--- (2)}$$
where $J \frac{d\omega_m}{dt}$ represents the dynamic inertia torque ($T_{\text{dyn}}$).</p>

<p><strong>3. Operating States of the Electric Drive:</strong></p>
<ol>
    <li><strong>Steady-State Running ($\frac{d\omega_m}{dt} = 0$):</strong><br>
    $$T = T_L$$
    The motor developed torque exactly balances the load torque; the motor runs at constant operating speed.</li>
    <li><strong>Acceleration ($\frac{d\omega_m}{dt} > 0$):</strong><br>
    $$T > T_L$$
    Motor torque exceeds load torque. The surplus torque $(T - T_L)$ accelerates the rotating parts.</li>
    <li><strong>Deceleration ($\frac{d\omega_m}{dt} < 0$):</strong><br>
    $$T < T_L$$
    Motor torque is less than load torque (or motor develops negative braking torque). Rotating parts slow down.</li>
</ol>
<p><strong>Note for Variable Inertia Loads:</strong> In applications like mine winders or industrial robots, inertia varies with position ($J = J(\theta)$). Then the term $\omega_m \frac{dJ}{dt} = \omega_m^2 \frac{dJ}{d\theta}$ must be retained.</p>
""",
        "understand_simply": r"""
<p>This is simply Newton's $F = ma$ written for rotating machines! $T$ is the engine pushing forward, $T_L$ is the friction and hill pushing backward, and $J \frac{d\omega}{dt}$ is the mass being accelerated. If engine push is greater than resistance ($T > T_L$), you speed up. If resistance is greater ($T < T_L$), you slow down.</p>
"""
    },

    'drive-q5': {
        "title": "Comprehensive Four-Quadrant Operation of an Electric Motor Driving a Hoist Load",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": r"$$P_m = T \cdot \omega \quad (P_m > 0 \implies \text{Motoring}, \quad P_m < 0 \implies \text{Braking})$$",
            "text": "Quadrant I: Upward lifting; Quadrant IV: Controlled downward lowering with regenerative braking."
        },
        "exam_answer": r"""
<p><strong>1. Definition &amp; Convention:</strong></p>
<ul>
    <li>An electric drive operates in four quadrants on the Torque-Speed plane based on the signs of speed ($\omega$) and developed torque ($T$).</li>
    <li>Mechanical power is: $P_m = T \cdot \omega$.
        <ul>
            <li>When $T$ and $\omega$ have the <strong>same sign</strong> ($P_m > 0$), the machine converts electrical power to mechanical power $\implies$ <strong>Motoring</strong>.</li>
            <li>When $T$ and $\omega$ have <strong>opposite signs</strong> ($P_m < 0$), mechanical power is converted back to electrical power $\implies$ <strong>Braking / Generating</strong>.</li>
        </ul>
    </li>
    <li><strong>Hoist Convention:</strong> Upward motion is taken as positive speed ($\omega > 0$). Downward motion is negative speed ($\omega < 0$). Gravity always pulls downward with active load torque $T_L$.</li>
</ul>

<p><strong>2. Quadrant-by-Quadrant Analysis:</strong></p>
<table class="exam-table">
    <thead>
        <tr>
            <th>Quadrant</th>
            <th>Speed ($\omega$)</th>
            <th>Torque ($T$)</th>
            <th>Power ($P_m$)</th>
            <th>Mode</th>
            <th>Hoist Physical Operation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Quadrant I</strong><br>(Forward Motoring)</td>
            <td>$\omega > 0$<br>(Upward)</td>
            <td>$T > 0$<br>(Upward)</td>
            <td>$P_m > 0$<br>(Electrical $\to$ Mech)</td>
            <td>Motoring</td>
            <td><strong>Lifting loaded cage:</strong> Motor develops upward torque in the direction of upward motion to overcome gravity. Energy drawn from supply.</td>
        </tr>
        <tr>
            <td><strong>Quadrant II</strong><br>(Forward Braking)</td>
            <td>$\omega > 0$<br>(Upward)</td>
            <td>$T < 0$<br>(Downward)</td>
            <td>$P_m < 0$<br>(Mech $\to$ Electrical)</td>
            <td>Braking</td>
            <td><strong>Stopping light/empty cage moving upward:</strong> An empty cage moving upward has upward momentum. Motor produces downward braking torque to bring it to a controlled stop.</td>
        </tr>
        <tr>
            <td><strong>Quadrant III</strong><br>(Reverse Motoring)</td>
            <td>$\omega < 0$<br>(Downward)</td>
            <td>$T < 0$<br>(Downward)</td>
            <td>$P_m > 0$<br>(Electrical $\to$ Mech)</td>
            <td>Motoring</td>
            <td><strong>Driving down an empty cage:</strong> If the empty cage has a heavy counterweight or high guide friction, gravity alone cannot pull it down. The motor drives downward in the direction of motion.</td>
        </tr>
        <tr>
            <td><strong>Quadrant IV</strong><br>(Reverse Braking)</td>
            <td>$\omega < 0$<br>(Downward)</td>
            <td>$T > 0$<br>(Upward)</td>
            <td>$P_m < 0$<br>(Mech $\to$ Electrical)</td>
            <td>Regenerative Braking</td>
            <td><strong>Lowering a loaded cage safely:</strong> Heavy weight pulls the cage downward ($\omega < 0$). Motor develops upward holding torque ($T > 0$) to prevent free-fall crash, regenerating power back to supply.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>An elevator hoist is the perfect example:</p>
<ul>
    <li><strong>Quadrant 1 (Lifting):</strong> Motor pulls UP, elevator moves UP. Electricity is consumed to lift the load.</li>
    <li><strong>Quadrant 4 (Lowering heavy cargo):</strong> Elevator is moving DOWN, but gravity wants to drop it like a rock! The motor must pull UP to brake and hold the car at a safe speed. Because movement is down and motor pull is up, the motor acts like an electric generator, sending power back to the grid.</li>
</ul>
"""
    },

    'drive-q6': {
        "title": "Mathematical Derivation of the Condition for Steady-State Stability",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m} > 0 \implies \frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m}$$",
            "text": "For steady-state stability, the slope of load torque must be strictly greater than the slope of motor torque at the operating point."
        },
        "exam_answer": r"""
<p><strong>1. Steady-State Equilibrium Point:</strong><br>
Let a motor-load drive system operate at an equilibrium speed $\omega_{m0}$. At this operating point:
$$T_0 = T_{L0} \quad \text{and} \quad \frac{d\omega_{m0}}{dt} = 0$$</p>

<p><strong>2. Small Perturbation Analysis:</strong><br>
Introduce a small speed disturbance $\Delta\omega_m$ around the operating point:
$$\omega_m = \omega_{m0} + \Delta\omega_m$$
The motor torque and load torque become:
$$T = T_0 + \Delta T, \quad T_L = T_{L0} + \Delta T_L$$
Linearizing $\Delta T$ and $\Delta T_L$ using first-order Taylor series expansions around $\omega_{m0}$:
$$\Delta T = \left(\frac{dT}{d\omega_m}\right)_0 \Delta\omega_m, \quad \Delta T_L = \left(\frac{dT_L}{d\omega_m}\right)_0 \Delta\omega_m$$

<p><strong>3. Substitute into Fundamental Dynamic Equation:</strong><br>
$$T - T_L = J \frac{d\omega_m}{dt}$$
$$(T_0 + \Delta T) - (T_{L0} + \Delta T_L) = J \frac{d(\omega_{m0} + \Delta\omega_m)}{dt}$$
Since $T_0 = T_{L0}$ and $\frac{d\omega_{m0}}{dt} = 0$:
$$\Delta T - \Delta T_L = J \frac{d(\Delta\omega_m)}{dt}$$
$$\left[\left(\frac{dT}{d\omega_m}\right)_0 - \left(\frac{dT_L}{d\omega_m}\right)_0\right] \Delta\omega_m = J \frac{d(\Delta\omega_m)}{dt}$$

<p><strong>4. Differential Equation for Speed Disturbance:</strong><br>
Rearranging into standard first-order differential form:
$$\frac{d(\Delta\omega_m)}{dt} + \frac{1}{J}\left[ \left(\frac{dT_L}{d\omega_m}\right)_0 - \left(\frac{dT}{d\omega_m}\right)_0 \right] \Delta\omega_m = 0$$
The general solution is:
$$\Delta\omega_m(t) = \Delta\omega_m(0) \cdot e^{-\frac{t}{\tau}}, \quad \text{where } \frac{1}{\tau} = \frac{1}{J}\left[ \frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m} \right]$$

<p><strong>5. Stability Condition:</strong><br>
For the system to be stable, the disturbance must decay to zero over time ($\Delta\omega_m(t) \to 0$ as $t \to \infty$). This requires the exponent to be strictly negative:
$$\frac{1}{\tau} > 0 \implies \frac{dT_L}{d\omega_m} - \frac{dT}{d\omega_m} > 0$$
$$\frac{dT_L}{d\omega_m} > \frac{dT}{d\omega_m}$$
<strong>Physical Meaning:</strong> If a disturbance increases speed ($\Delta\omega > 0$), load torque must become larger than motor torque ($T_L > T$), producing a net decelerating torque that naturally restores the motor back to $\omega_{m0}$.</p>
""",
        "understand_simply": r"""
<p>Think about driving a car with cruise control set at 60 km/h. If a sudden downhill gust speeds the car up to 62 km/h, road resistance must rise faster than the engine output (or the engine must back off), slowing the car back to 60 km/h. If instead the engine pushed <em>harder</em> whenever speed rose, the car would accelerate out of control! Stability means load slope must be steeper than motor slope.</p>
"""
    },

    'drive-q6b': {
        "title": "Thermal Heating and Cooling Dynamics of Electric Motors and Rating Selection",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\theta(t) = \theta_{ss}\left(1 - e^{-t/\tau_h}\right) \quad \text{[Heating]}, \quad \theta(t) = \theta_0 e^{-t/\tau_c} \quad \text{[Cooling]}$$",
            "text": "Thermal time constant $\\tau = C/D$; cooling time constant $\\tau_c > \\tau_h$ because ventilation fan stops when motor is turned off."
        },
        "exam_answer": r"""
<p><strong>1. Heat Balance Equation:</strong><br>
In an electric motor operating under load, internal electrical and magnetic losses ($P_{\text{loss}}$ in Watts) are converted to heat. In a small time interval $dt$:</p>
$$\text{Heat Generated} = \text{Heat Stored in Motor Mass} + \text{Heat Dissipated to Ambient}$$
$$P_{\text{loss}} \, dt = C \, d\theta + D \, \theta \, dt$$
where:
<ul>
    <li>$C = \text{Thermal capacity of motor (Joules/}^\circ\text{C)}$</li>
    <li>$D = \text{Heat dissipation coefficient (Watts/}^\circ\text{C)}$</li>
    <li>$\theta = \text{Temperature rise above ambient (}^\circ\text{C)}$</li>
</ul>

<p><strong>2. Heating Curve Derivation:</strong><br>
Rearranging the differential equation:
$$\frac{d\theta}{dt} + \frac{D}{C}\theta = \frac{P_{\text{loss}}}{C}$$
Solving with initial condition $\theta(0) = 0$ (starting cold from ambient):
$$\theta(t) = \theta_{ss} \left( 1 - e^{-t / \tau_h} \right)$$
where $\theta_{ss} = \frac{P_{\text{loss}}}{D}$ is the steady-state maximum temperature rise, and $\tau_h = \frac{C}{D}$ is the <strong>heating time constant</strong> (typically 30–60 minutes).</p>

<p><strong>3. Cooling Curve Derivation:</strong><br>
When the motor is shut down or load is removed ($P_{\text{loss}} \approx 0$), heat is dissipated:
$$\theta(t) = \theta_0 e^{-t / \tau_c}$$
where $\theta_0$ is initial temperature at shutdown, and $\tau_c = \frac{C}{D'}$ is the <strong>cooling time constant</strong>.<br>
<em>Important Note:</em> In self-cooled motors, the cooling fan stops when the motor stops, so $D' < D \implies \tau_c > \tau_h$ (cooling is much slower than heating!).</p>

<p><strong>4. Motor Power Rating Selection for Continuous Duty:</strong></p>
<ul>
    <li>The selected motor rated power $P_{\text{rated}}$ must be chosen such that its steady-state temperature rise does not exceed the permissible temperature limit of the stator insulation class:
    $$\theta_{ss} \le \theta_{\text{permissible}}$$</li>
    <li>Standard Insulation Classes: Class B ($130^\circ\text{C}$), Class F ($155^\circ\text{C}$), Class H ($180^\circ\text{C}$).</li>
</ul>
""",
        "understand_simply": r"""
<p>An electric motor is like an electric kettle. When you turn it on, heat builds up rapidly until the heat escaping into the room equals the heat being generated inside (steady state). If you overload the motor, it gets hotter than the plastic insulation on the copper wires can handle, causing the wires to melt and short-circuit!</p>
"""
    },

    # =========================================================================
    # MODULE 2: Phase-Controlled DC Motor Drives
    # =========================================================================
    'drive-q7': {
        "title": "Armature Voltage Control vs Field Weakening Speed Control of DC Motors",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": r"$$\omega \approx \frac{V_a - I_a R_a}{K \Phi} \quad (\text{Below Base Speed: Constant Torque; Above: Constant Power})$$",
            "text": r"Armature control: $0 \to \omega_{\text{base}}$ by varying $V_a$ (constant torque); Field control: $\omega_{\text{base}} \to \omega_{\text{max}}$ by reducing $\Phi$ (constant power)."
        },
        "exam_answer": r"""
<p>The speed equation of a separately excited DC motor is $\omega = \frac{V_a - I_a R_a}{K \Phi}$. The two control zones are compared below:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Armature Voltage Control</th>
            <th>Field Weakening Control</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Operating Speed Range</strong></td>
            <td>Sub-base speeds: from $0$ up to rated base speed ($\omega \le \omega_{\text{base}}$).</td>
            <td>Super-base speeds: from $\omega_{\text{base}}$ up to maximum speed ($\omega > \omega_{\text{base}}$).</td>
        </tr>
        <tr>
            <td><strong>Method of Control</strong></td>
            <td>Armature voltage $V_a$ is varied from $0 \to V_{\text{rated}}$; field flux $\Phi$ is kept constant at rated.</td>
            <td>Armature voltage $V_a$ is fixed at rated; field current $I_f$ is reduced, weakening flux $\Phi$.</td>
        </tr>
        <tr>
            <td><strong>Torque Capability</strong></td>
            <td><strong>Constant Torque:</strong> $T = K \Phi I_a = \text{constant}$ because flux $\Phi$ and rated current $I_a$ are both constant.</td>
            <td><strong>Decreasing Torque:</strong> Torque capability drops inversely with speed ($T \propto \frac{1}{\omega}$) as flux weakens.</td>
        </tr>
        <tr>
            <td><strong>Power Capability</strong></td>
            <td>Power increases linearly with speed ($P = T \cdot \omega \propto \omega$) up to rated power.</td>
            <td><strong>Constant Power:</strong> Power remains fixed at rated power ($P = V_{\text{rated}} I_{\text{rated}} = \text{const}$).</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>Think of bicycle gears: In 1st gear (Armature Control), you push hard with maximum torque to climb hills from a dead stop up to moderate speed. Once you hit top cruising speed (Base speed), you shift into high gear (Field Weakening): you produce less turning torque, but your pedals spin much faster at the same muscle power!</p>
"""
    },

    'drive-q7b': {
        "title": "Three-Phase Semi-Converter Fed DC Motor Drive: Features and Voltage Expression",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = \frac{3\sqrt{3}V_{m}}{\pi} \left( \frac{1 + \cos\alpha}{2} \right) = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha)$$",
            "text": "Semi-converter uses 3 thyristors + 3 diodes (half-controlled); operates strictly in Quadrant I (one-quadrant motoring)."
        },
        "exam_answer": r"""
<p><strong>1. Circuit Topology:</strong><br>
A 3-phase semi-converter (half-controlled bridge) uses 3 thyristors in the top group and 3 uncontrolled diodes in the bottom group, plus a freewheeling diode across the DC motor armature.</p>

<p><strong>2. Average Output Voltage Equation:</strong><br>
For continuous armature current with line-to-neutral peak voltage $V_m$:
$$V_a = \frac{3\sqrt{3}V_m}{2\pi}(1 + \cos\alpha) = \frac{3V_{ml}}{2\pi}(1 + \cos\alpha)$$
where $V_{ml} = \sqrt{3}V_m$ is the peak line-to-line voltage, and $\alpha$ is the firing delay angle ($0 \le \alpha \le 180^\circ$).</p>

<p><strong>3. Key Features &amp; Limitations:</strong></p>
<ul>
    <li><strong>One-Quadrant Operation:</strong> Since $(1 + \cos\alpha) \ge 0$, the armature voltage $V_a$ is always positive. Current $I_a$ is unidirectional. Therefore, it can only operate in <strong>Quadrant I (Motoring)</strong>; regenerative braking is impossible.</li>
    <li><strong>Higher Power Factor:</strong> Better input displacement power factor and lower harmonic content than a fully controlled converter because the freewheeling diode prevents negative voltage loops.</li>
    <li><strong>Cost-Effective:</strong> Diodes require no gate firing circuits, reducing drive hardware cost significantly.</li>
</ul>
""",
        "understand_simply": r"""
<p>A semi-converter is like a budget, one-way speed controller. Half the switches are smart (thyristors) and half are cheap automatic one-way valves (diodes). It is cheaper and cleaner for running a motor forward, but it cannot run in reverse or perform regenerative braking.</p>
"""
    },

    'drive-q8': {
        "title": "Single-Phase Fully Controlled Rectifier Fed Separately Excited DC Motor",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = \frac{2V_m}{\pi}\cos\alpha, \quad \omega_m = \frac{\frac{2V_m}{\pi}\cos\alpha - I_a R_a}{K_b \Phi}$$",
            "text": r"Firing angle $0^\circ \le \alpha \le 90^\circ \implies$ Motoring ($V_a > 0$); $90^\circ < \alpha \le 180^\circ \implies$ Inversion ($V_a < 0$, regenerative braking)."
        },
        "exam_answer": r"""
<div class="interactive-practice-pill" style="margin: 0.5rem 0 1.25rem 0; padding: 0.75rem 1rem; border-radius: 10px; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.3); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.6rem;">
    <div style="display: flex; align-items: center; gap: 0.6rem;">
        <span style="font-size: 1.35rem;">✏️</span>
        <div>
            <strong style="color: #38bdf8; font-size: 0.88rem;">Interactive Muscle Memory Canvas</strong>
            <p style="font-size: 0.76rem; color: var(--text-muted); margin: 0;">Trace and draw this exact circuit diagram with magnetic stroke-snapping.</p>
        </div>
    </div>
    <a href="draw.html" class="tool-btn primary" style="text-decoration: none; padding: 0.4rem 0.9rem; font-size: 0.8rem; font-weight: 700; border-radius: 8px; display: inline-flex; align-items: center; gap: 0.4rem; background: #0284c7; color: white; border: 1px solid #38bdf8;">
        <span>🎯 Practice Drawing Now</span>
    </a>
</div>

<p><strong>1. Circuit Topology &amp; Operation:</strong><br>
A single-phase fully controlled converter uses four thyristors ($T_1, T_2, T_3, T_4$) in a full-bridge arrangement to supply the armature of a separately excited DC motor from an AC source $v_s(t) = V_m \sin\omega t$.</p>
<ul>
    <li>During positive half-cycle ($\omega t = \alpha$ to $\pi + \alpha$): Thyristors $T_1$ and $T_2$ are fired, applying source voltage to the armature.</li>
    <li>During negative half-cycle ($\omega t = \pi + \alpha$ to $2\pi + \alpha$): Thyristors $T_3$ and $T_4$ are fired, applying reversed AC voltage to the armature.</li>
</ul>

<p><strong>2. Average Armature Voltage Derivation:</strong><br>
Assuming continuous conduction due to large armature inductance:
$$V_a = \frac{1}{\pi} \int_{\alpha}^{\pi + \alpha} V_m \sin(\omega t) \, d(\omega t) = \frac{V_m}{\pi} [-\cos(\omega t)]_{\alpha}^{\pi + \alpha} = \frac{2V_m}{\pi}\cos\alpha$$</p>

<p><strong>3. Speed-Torque Characteristic Equation:</strong><br>
The motor steady-state equations are:
$$V_a = E_b + I_a R_a, \quad E_b = K_b \Phi \omega_m, \quad T = K_t \Phi I_a \implies I_a = \frac{T}{K_t \Phi}$$
Substituting $V_a$ and $I_a$ into the back-EMF equation:
$$\frac{2V_m}{\pi}\cos\alpha = K_b \Phi \omega_m + \left(\frac{T}{K_t \Phi}\right) R_a$$
$$\omega_m = \frac{\frac{2V_m}{\pi}\cos\alpha}{K_b \Phi} - \frac{R_a}{(K_b \Phi)(K_t \Phi)} T$$
For continuous conduction, the speed-torque curves form a family of parallel drooping lines shifted downward as firing angle $\alpha$ increases from $0^\circ$ to $90^\circ$.</p>

<p><strong>4. Two-Quadrant Operating Capability:</strong><br>
Because current $I_a$ can only flow in one direction through the thyristors ($I_a > 0$), but voltage $V_a$ can become negative when $\alpha > 90^\circ$, this drive operates in Quadrant I (Forward Motoring, $V_a > 0, I_a > 0$) and Quadrant IV (Regenerative Inversion, $V_a < 0, I_a > 0$ when motor back-EMF is reversed).</p>
""",
        "understand_simply": r"""
<p>A thyristor is an electronic valve with a trigger. If you trigger it early in the AC wave ($\alpha = 0^\circ$), full voltage rushes through to spin the motor fast. If you delay the trigger ($\alpha \to 90^\circ$), less voltage passes through and the motor slows down. If you delay past $90^\circ$, the average voltage flips negative, allowing spinning kinetic energy to turn into electricity and push current back into the power lines!</p>
"""
    },

    'drive-q8b': {
        "title": "Three-Phase Full Converter Fed Separately Excited DC Motor Drive",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = \frac{3V_{ml}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_m}{\pi}\cos\alpha$$",
            "text": "Uses 6 thyristors; 6-pulse output ripple frequency ($300\\text{ Hz}$) drastically reduces armature current ripple and eliminates discontinuous conduction."
        },
        "exam_answer": r"""
<p><strong>1. Circuit Configuration:</strong><br>
A 3-phase full converter consists of a 6-pulse bridge with six thyristors ($T_1 \dots T_6$) connected to a 3-phase AC supply ($415\text{ V}, 50\text{ Hz}$) feeding a high-power separately excited DC motor.</p>

<p><strong>2. Average Armature Voltage Derivation:</strong><br>
The output voltage repeats every $60^\circ$ ($\frac{\pi}{3}$ radians), yielding a 6-pulse ripple of frequency $6f = 300\text{ Hz}$.<br>
Integrating the line-to-line voltage over one $60^\circ$ conduction interval:
$$V_a = \frac{3}{\pi} \int_{\frac{\pi}{6} + \alpha}^{\frac{\pi}{2} + \alpha} V_{ml} \sin\left(\omega t + \frac{\pi}{6}\right) \, d(\omega t) = \frac{3V_{ml}}{\pi}\cos\alpha = \frac{3\sqrt{3}V_m}{\pi}\cos\alpha$$
where $V_{ml}$ is the peak line-to-line supply voltage.</p>

<p><strong>3. Speed-Torque Equation:</strong><br>
$$\omega_m = \frac{\frac{3V_{ml}}{\pi}\cos\alpha}{K_b \Phi} - \frac{R_a}{(K_b \Phi)(K_t \Phi)} T$$</p>

<p><strong>4. Major Advantages over 1-Phase Drives:</strong></p>
<ul>
    <li><strong>6-Pulse Low Ripple:</strong> Output ripple frequency is $300\text{ Hz}$ compared to $100\text{ Hz}$ in 1-phase converters. Armature current is practically continuous and ripple-free, eliminating the need for large smoothing filter inductors.</li>
    <li><strong>Discontinuous Conduction Eliminated:</strong> Discontinuous conduction occurs only at extremely light loads, preventing erratic speed regulation.</li>
    <li><strong>Higher Power Capability:</strong> Suitable for heavy industrial ratings (from tens of kW up to several MW in rolling mills and mine hoists).</li>
</ul>
""",
        "understand_simply": r"""
<p>A single-phase converter is like a two-cylinder car engine—it pushes power twice per cycle with big gaps in between. A 3-phase full converter is like a smooth 6-cylinder engine—it delivers continuous overlapping power pulses, so the motor spins smoothly without jerky vibrations or current ripples.</p>
"""
    },

    # =========================================================================
    # MODULE 3: Chopper-Controlled DC Motor Drives & Closed Loop Control
    # =========================================================================
    'drive-q9': {
        "title": "Motoring Control of DC Separately Excited Motor using Class-A Chopper",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = \delta \cdot V_{\text{dc}}, \quad \omega_m = \frac{\delta V_{\text{dc}} - I_a R_a}{K_b \Phi} \quad (\delta = \frac{t_{\text{on}}}{T})$$",
            "text": "Class-A chopper operates in Quadrant I (Step-Down / Buck); average voltage $V_a$ is controlled via duty ratio $\\delta$."
        },
        "exam_answer": r"""
<p><strong>1. Circuit Topology &amp; Operation:</strong><br>
A Class-A chopper (step-down/buck converter) connects a DC supply $V_{\text{dc}}$ to the armature of a separately excited DC motor using a power semiconductor switch (IGBT/MOSFET) $CH_1$ and a parallel freewheeling diode $D_1$.</p>
<ul>
    <li><strong>ON Period ($0 < t \le t_{\text{on}}$):</strong> Switch $CH_1$ is ON. Supply voltage $V_{\text{dc}}$ is applied to the armature. Armature current $i_a$ rises, storing energy in the armature inductance.</li>
    <li><strong>OFF Period ($t_{\text{on}} < t \le T$):</strong> Switch $CH_1$ is turned OFF. Inductive energy forces current $i_a$ to freewheel through diode $D_1$. Voltage across armature drops to zero ($V_a = 0$).</li>
</ul>

<p><strong>2. Average Voltage &amp; Speed Equations:</strong><br>
$$V_a = \frac{t_{\text{on}}}{T} V_{\text{dc}} = \delta \cdot V_{\text{dc}} \quad (0 \le \delta \le 1)$$
where $\delta = \frac{t_{\text{on}}}{T}$ is the duty cycle.<br>
Speed equation:
$$\omega_m = \frac{\delta V_{\text{dc}} - I_a R_a}{K_b \Phi}$$</p>

<p><strong>3. Operating Quadrant:</strong><br>
Both average voltage $V_a \ge 0$ and current $I_a \ge 0$ are strictly positive. The drive operates exclusively in <strong>Quadrant I (Forward Motoring)</strong>.</p>
""",
        "understand_simply": r"""
<p>A Class-A chopper is like rapidly flicking a light switch on and off. If you keep the switch ON for $70\%$ of the time and OFF for $30\%$, the motor sees an average of $70\%$ of the battery voltage. By changing the ON-time ratio ($\delta$), you smoothly adjust the motor speed from zero to full.</p>
"""
    },

    'drive-q9b': {
        "title": "Regenerative Braking Control of DC Motor using Class-B Step-Up Chopper",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_{\text{dc}} = \frac{E_b}{1 - \delta} \implies E_b < V_{\text{dc}} \text{ can pump energy back into higher supply } V_{\text{dc}}$$*",
            "text": "Class-B chopper operates in Quadrant II (Step-Up / Boost); pumps electrical power from motor back into supply."
        },
        "exam_answer": r"""
<p><strong>1. Operating Principle:</strong><br>
A Class-B chopper operates as a boost converter to transfer energy from a decelerating DC motor (where back-EMF $E_b$ is lower than supply $V_{\text{dc}}$) back into the higher-voltage DC supply.</p>

<p><strong>2. Circuit Operation:</strong></p>
<ul>
    <li>The circuit uses a chopper switch $CH_2$ connected across the armature and a series blocking diode $D_2$ pointing toward the supply $+V_{\text{dc}}$.</li>
    <li><strong>Interval 1 ($CH_2$ ON):</strong> Switch $CH_2$ closes. Motor back-EMF $E_b$ drives current through the armature inductance $L_a$ and $CH_2$. The motor acts as a generator, storing kinetic energy in the magnetic field of inductor $L_a$.</li>
    <li><strong>Interval 2 ($CH_2$ OFF):</strong> Switch $CH_2$ opens. The inductor $L_a$ opposes current collapse and develops a high induced voltage $L_a \frac{di_a}{dt}$. The combined voltage $(E_b + L_a \frac{di_a}{dt})$ exceeds the DC bus voltage $V_{\text{dc}}$, forcing diode $D_2$ to conduct and feeding energy into the supply.</li>
</ul>

<p><strong>3. Average Voltage &amp; Quadrant:</strong><br>
Average voltage across chopper: $V_a = (1 - \delta) V_{\text{dc}}$.<br>
Because current flows out of the motor ($I_a < 0$) while motor voltage remains positive ($V_a > 0$), power $P_m = V_a I_a < 0$. The drive operates in <strong>Quadrant II (Forward Regenerative Braking)</strong>.</p>
""",
        "understand_simply": r"""
<p>How do you pump water from a low bucket up into a high tank? You use a hand pump to build up pressure! A Class-B chopper does the exact same thing electrically: it shorts the motor through an inductor to build up magnetic pressure, then opens the switch so the combined kick shoots energy up into the high-voltage battery.</p>
"""
    },

    'drive-q10': {
        "title": "Two-Quadrant Class-C Chopper Fed DC Motor Drive",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = \delta_1 V_{\text{dc}} \quad (\text{Quadrant I: Motoring via } CH_1/D_1; \quad \text{Quadrant II: Braking via } CH_2/D_2)$$",
            "text": "Class-C combines Class-A and Class-B; allows seamless transition between motoring and regenerative braking without mechanical switches."
        },
        "exam_answer": r"""
<p><strong>1. Circuit Topology:</strong><br>
A Class-C chopper combines a Class-A chopper ($CH_1, D_1$) and a Class-B chopper ($CH_2, D_2$) across a common DC supply $V_{\text{dc}}$ feeding a DC motor. The two switches are operated complementarily (when $CH_1$ is ON, $CH_2$ is OFF, and vice-versa) to prevent a shoot-through dead short across the DC bus.</p>

<p><strong>2. Two Modes of Operation:</strong></p>
<p><strong>Mode 1: Quadrant I (Forward Motoring):</strong></p>
<ul>
    <li>Switch $CH_1$ is gated. When $CH_1$ conducts, power flows from $V_{\text{dc}}$ into the motor, building up armature current $I_a > 0$.</li>
    <li>When $CH_1$ turns off, current freewheels through diode $D_1$.</li>
    <li>Average armature voltage $V_a = \delta_1 V_{\text{dc}} > 0$ and current $I_a > 0$. Electrical power is converted into mechanical work.</li>
</ul>

<p><strong>Mode 2: Quadrant II (Forward Regenerative Braking):</strong></p>
<ul>
    <li>When braking is commanded, $CH_1$ is disabled and $CH_2$ is gated.</li>
    <li>During $CH_2$ ON period, motor back-EMF $E_b$ charges the armature inductor through $CH_2$.</li>
    <li>When $CH_2$ turns off, the inductive kick forces current out through feedback diode $D_2$ into the supply $V_{\text{dc}}$.</li>
    <li>Armature current reverses ($I_a < 0$) while voltage remains positive ($V_a > 0$). Mechanical kinetic energy is pumped back into the DC source.</li>
</ul>

<p><strong>3. Practical Application:</strong><br>
Class-C chopper drives are standard in battery-powered electric vehicles (EVs), urban electric buses, and battery locomotives where instant transition between acceleration (Quadrant I) and regenerative braking (Quadrant II) is required.</p>
""",
        "understand_simply": r"""
<p>A Class-C chopper is like a smart reversible pump. Press the accelerator pedal, and valve 1 opens to feed electricity into the motor to drive the wheels forward. Press the brake pedal, and valve 2 takes over, letting the spinning wheels drive the motor backwards like a dynamo to recharge the vehicle battery.</p>
"""
    },

    'drive-q10b': {
        "title": "Four-Quadrant Class-E Chopper Fed DC Motor Drive (H-Bridge)",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$V_a = (2\delta - 1)V_{\text{dc}} \quad (-V_{\text{dc}} \le V_a \le +V_{\text{dc}})$$",
            "text": "Full H-Bridge (4 switches + 4 anti-parallel diodes) provides complete four-quadrant speed and torque reversal."
        },
        "exam_answer": r"""
<p><strong>1. Circuit Topology:</strong><br>
A Class-E chopper consists of four semiconductor switches ($CH_1, CH_2, CH_3, CH_4$) and four anti-parallel feedback diodes ($D_1, D_2, D_3, D_4$) connected in a full H-bridge bridge configuration across a DC voltage source $V_{\text{dc}}$.</p>

<p><strong>2. Operation across the Four Quadrants:</strong></p>
<ol>
    <li><strong>Quadrant I (Forward Motoring, $V_a > 0, I_a > 0$):</strong><br>
    $CH_4$ is kept continuously ON, and $CH_1$ is chopped at duty ratio $\delta$. When $CH_1$ is ON, current flows $V_{\text{dc}} \to CH_1 \to \text{Motor} \to CH_4 \to \text{Ground}$. When $CH_1$ turns off, current freewheels through $CH_4$ and diode $D_2$.</li>
    <li><strong>Quadrant II (Forward Braking, $V_a > 0, I_a < 0$):</strong><br>
    $CH_1, CH_4$ are off. Switch $CH_2$ is chopped. When $CH_2$ is ON, current builds through motor back-EMF and $CH_2$. When $CH_2$ turns off, current feeds back through $D_1$ and $D_4$ into $+V_{\text{dc}}$, regenerating power.</li>
    <li><strong>Quadrant III (Reverse Motoring, $V_a < 0, I_a < 0$):</strong><br>
    $CH_2$ is kept continuously ON, and $CH_3$ is chopped. Motor terminal voltage is reversed, and motor spins in reverse direction. Freewheeling occurs through $CH_2$ and $D_4$.</li>
    <li><strong>Quadrant IV (Reverse Braking, $V_a < 0, I_a > 0$):</strong><br>
    $CH_2, CH_3$ are off. Switch $CH_4$ is chopped. Inductive energy feeds back into supply through diodes $D_2$ and $D_3$, providing regenerative braking in the reverse direction.</li>
</ol>
<p><strong>Application:</strong> Industrial robotic manipulators, steel rolling mills, CNC machine tools, and electric traction requiring rapid bidirectional reversal.</p>
""",
        "understand_simply": r"""
<p>An H-Bridge is like an electrical railway cross-track. By flipping the 4 switches in pairs, you can connect the battery forward across the motor (spins clockwise), connect it backward (spins counter-clockwise), or let the motor push power back into the battery in either direction!</p>
"""
    },

    'drive-q11': {
        "title": "Closed-Loop Speed Control Architecture of DC Motor Drives with Inner Current Loop",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\text{Outer Loop (Speed Error } \to \text{ PI Controller } \to I_a^* \text{ Limiter}) \implies \text{Inner Loop (Current Error } \to \text{ Controller } \to \text{ Converter Firing)}$$",
            "text": "Two-loop cascaded control: Inner current loop protects power switches and ensures fast torque response; Outer loop ensures zero steady-state speed error."
        },
        "exam_answer": r"""
<p><strong>1. Architectural Need for Cascaded Control:</strong></p>
<ul>
    <li>Directly controlling speed with a single control loop is dangerous: any sudden speed error command causes huge armature current surges ($I_a \approx \frac{V_a - E_b}{R_a}$), which can destroy power semiconductor switches and cause commutator flashover.</li>
    <li>The industry-standard solution is <strong>cascaded two-loop control</strong>: an outer speed loop containing an inner current-limiting control loop.</li>
</ul>

<p><strong>2. Detailed Description of Control Blocks:</strong></p>
<ol>
    <li><strong>Outer Speed Control Loop:</strong>
        <ul>
            <li>Speed sensor (optical encoder/tachometer) measures actual rotor speed $\omega_m$.</li>
            <li>Error detector compares reference speed $\omega^*$ with actual speed $\omega_m$: $e_\omega = \omega^* - \omega_m$.</li>
            <li>Speed controller (PI controller) processes $e_\omega$ to generate the reference armature current command $I_a^*$.</li>
            <li><strong>Current Limiter Block:</strong> Clamps $I_a^*$ strictly between $\pm I_{a,\text{max}}$ (typically $1.5\text{ to } 2.0 \times$ rated current). This guarantees absolute overcurrent protection under all starting, stall, and shock-load conditions!</li>
        </ul>
    </li>
    <li><strong>Inner Current Control Loop:</strong>
        <ul>
            <li>Current sensor (Hall-effect CT) measures actual armature current $I_a$.</li>
            <li>Error detector compares $I_a^*$ with $I_a$: $e_i = I_a^* - I_a$.</li>
            <li>Current controller (fast PI controller) processes $e_i$ to generate the converter control voltage $v_c$.</li>
            <li>PWM / Firing pulse generator converts $v_c$ into trigger pulses (firing angle $\alpha$ or duty cycle $\delta$) for the power converter.</li>
        </ul>
    </li>
</ol>

<p><strong>3. Key Operational Advantages:</strong></p>
<ul>
    <li><strong>Inherent Overcurrent Protection:</strong> Current never exceeds $I_{a,\text{max}}$ even if the motor shaft is completely jammed at standstill.</li>
    <li><strong>Decoupled Dynamics:</strong> Inner current loop has very small electrical time constant ($\tau_a = L_a/R_a \approx 10\text{ ms}$), responding $5\text{ to } 10\times$ faster than the mechanical speed loop ($\tau_m = J/B \approx 100\text{--}500\text{ ms}$).</li>
    <li><strong>Fast Disturbance Rejection:</strong> Supply voltage fluctuations are immediately corrected by the inner loop before they can affect motor speed.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of cruise control in a modern sports car. You set the cruise control to 80 km/h (the <strong>outer speed loop</strong>). If you suddenly command 120 km/h, a dumb system might flood the engine and blow the pistons! But the smart car uses an <strong>inner torque-limiter loop</strong>: it pushes maximum safe acceleration current, holds it exactly at the safe redline limit, and then smoothly glides to 120 km/h without burning anything up.</p>
"""
    },

    # =========================================================================
    # MODULE 4: Induction Motor Drives
    # =========================================================================
    'drive-q12': {
        "title": "Limitations and Application Boundaries of Stator Voltage Control in Induction Motors",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$T \propto V^2 \implies \text{Torque drops drastically with voltage; stable speed control range is limited to } s \le s_m$$",
            "text": "Restricted to fan/pump loads ($T_L \\propto \\omega^2$); causes excessive rotor copper losses ($P_{rc} = s P_g$) and motor heating at high slip."
        },
        "exam_answer": r"""
<p><strong>1. Operating Principle:</strong><br>
The electromagnetic torque of an induction motor is proportional to the square of stator terminal voltage: $T \propto V^2$. By reducing $V$ using an AC voltage controller (TRIAC/back-to-back thyristors) at fixed supply frequency, speed can be varied.</p>

<p><strong>2. Three Major Technical Limitations:</strong></p>
<ol>
    <li><strong>Severely Restricted Stable Speed Range:</strong> The breakdown torque drops with $V^2$. For constant-torque loads, stable operation is restricted only between synchronous speed and maximum torque slip ($0 \le s \le s_m$). At lower voltages, the motor stalls.</li>
    <li><strong>Excessive Rotor Heating &amp; Poor Efficiency at Low Speeds:</strong> Rotor copper loss is proportional to slip: $P_{rc} = s \cdot P_{\text{airgap}}$. Operating at high slip to achieve low speed turns most of the input power directly into heat in the rotor, leading to motor burnout unless heavily derated.</li>
    <li><strong>High Harmonic Distortion &amp; Low Power Factor:</strong> Firing angle control introduces high stator current harmonics and poor displacement power factor.</li>
</ol>

<p><strong>3. Practical Application Boundaries:</strong><br>
Strictly restricted to low-power centrifugal fan, blower, and water pump drives where load torque drops quadratically ($T_L \propto \omega^2$). Because load torque is tiny at low speeds, the motor does not overheat.</p>
""",
        "understand_simply": r"""
<p>Stator voltage control is like an ordinary domestic ceiling fan regulator. It works fine for a ceiling fan because air resistance is small at low speeds. But if you tried using a fan regulator on a heavy loaded conveyor belt or crane, the motor would stall, hum loudly, and burn its copper windings within minutes!</p>
"""
    },

    'drive-q12b': {
        "title": "Comparison between Voltage Source Inverter (VSI) and Current Source Inverter (CSI) Drives",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "VSI uses large DC bus capacitor (constant voltage); CSI uses large DC link inductor (constant current, inherent regenerative braking)."
        },
        "exam_answer": r"""
<p>Voltage Source Inverter (VSI) and Current Source Inverter (CSI) drives are compared below:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Feature</th>
            <th>Voltage Source Inverter (VSI) Drive</th>
            <th>Current Source Inverter (CSI) Drive</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>DC Link Intermediate Element</strong></td>
            <td>Large <strong>electrolytic capacitor ($C$)</strong> connected in parallel; maintains a stiff, ripple-free DC bus voltage.</td>
            <td>Large <strong>smoothing inductor ($L$)</strong> connected in series; maintains a stiff, ripple-free DC link current.</td>
        </tr>
        <tr>
            <td><strong>Output Waveforms to Motor</strong></td>
            <td>Output voltage is a square wave or PWM pulse train; motor current is approximately sinusoidal.</td>
            <td>Output current is a 6-step square wave; motor terminal voltage is approximately sinusoidal.</td>
        </tr>
        <tr>
            <td><strong>Regenerative Braking Capability</strong></td>
            <td>Requires an extra anti-parallel feedback converter or dynamic braking chopper + resistor to absorb regenerative energy.</td>
            <td><strong>Inherent 4-quadrant regeneration:</strong> Power reversal occurs naturally by simply reversing the DC link voltage polarity without adding extra switches.</td>
        </tr>
        <tr>
            <td><strong>Short-Circuit Protection</strong></td>
            <td>Vulnerable to DC shoot-through fault (if both upper and lower switches fire simultaneously, capacitor discharges with violent current spike).</td>
            <td>Inherently short-circuit proof; the large series inductor limits the rate of rise of fault current ($di/dt$).</td>
        </tr>
        <tr>
            <td><strong>Industrial Prevalence</strong></td>
            <td>Dominates $95\%$ of modern industrial AC drives (PWM-VSI with IGBTs).</td>
            <td>Restricted to very large multi-megawatt fan/pump/compressor drives and high-power synchronous motors.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>VSI is like maintaining constant water pressure in your pipes using a pressure tank—you open and close taps to let water spurt through. CSI is like keeping a constant high-speed stream of water circulating through a thick loop pipe, and diverting that stream into different motor windings using valves.</p>
"""
    },

    'drive-q13': {
        "title": "Comprehensive Theory and Derivation of Constant V/f Speed Control of Induction Motors",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\Phi_m \propto \frac{V}{f} = \text{constant}, \quad T_{\text{max}} = \frac{3}{2 \omega_s} \frac{V^2}{2 X_s} \approx \text{constant}$$",
            "text": "Keeping $V/f$ constant avoids magnetic core saturation and maintains constant maximum breakdown torque across the speed range."
        },
        "exam_answer": r"""
<p><strong>1. Theoretical Principle:</strong><br>
The induced stator EMF per phase of a 3-phase induction motor is governed by Faraday's law:
$$E_1 = 4.44 \cdot f \cdot N_1 \cdot K_{w1} \cdot \Phi_m \implies \Phi_m \approx \frac{V}{f}$$
If supply frequency $f$ is reduced to lower motor speed while voltage $V$ is kept constant, the air-gap flux $\Phi_m \propto \frac{V}{f}$ increases drastically, saturating the stator magnetic iron core. Core saturation causes severe magnetizing current spikes, high core losses, and motor overheating.<br>
To maintain rated air-gap flux $\Phi_m$ without saturation, supply voltage $V$ must be varied in direct proportion to frequency $f$, keeping the ratio $\frac{V}{f}$ constant.</p>

<p><strong>2. Maximum Breakdown Torque Analysis:</strong><br>
The maximum torque (breakdown torque) developed by an induction motor is:
$$T_{\text{max}} \approx \frac{3}{2 \omega_s} \frac{V^2}{2 X_1} = \frac{3}{2 \left(\frac{4\pi f}{P}\right)} \frac{V^2}{2 (2\pi f L_1)} \propto \left(\frac{V}{f}\right)^2$$
Since $\frac{V}{f}$ is held constant, the maximum breakdown torque $T_{\text{max}}$ remains nearly constant at all operating frequencies.</p>

<p><strong>3. Operating Zones:</strong></p>
<ul>
    <li><strong>Low-Frequency Voltage Boost:</strong> At very low frequencies ($f < 10\text{ Hz}$), the stator resistive drop $I_1 R_1$ becomes significant compared to induced voltage $E_1$. An extra voltage boost is added to maintain rated air-gap flux and prevent torque droop.</li>
    <li><strong>Sub-Base Speed Region ($f \le f_{\text{rated}}$):</strong> $V$ is increased linearly with $f$, providing a <strong>Constant Torque</strong> capability.</li>
    <li><strong>Super-Base Speed Region ($f > f_{\text{rated}}$):</strong> Voltage cannot exceed rated stator insulation voltage ($V = V_{\text{rated}} = \text{const}$). Further increase in $f$ causes flux to weaken ($\Phi \propto 1/f$), providing a <strong>Constant Power</strong> capability with reduced torque.</li>
</ul>
""",
        "understand_simply": r"""
<p>Think of an induction motor like a magnetic sponge. Frequency $f$ controls how fast the magnetic field spins, while voltage $V$ controls how much magnetism is poured into the iron sponge. If you slow down the spin without lowering the voltage, you over-soak the sponge—the iron saturates and draws dangerous overheating currents. By scaling voltage and frequency together ($V/f = \text{const}$), the motor always stays at peak magnetic strength and produces maximum pulling torque at any speed.</p>
"""
    },

    'drive-q14': {
        "title": "Static Rotor Resistance Speed Control of Wound-Rotor Induction Motor",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$R_{\text{eff}} = R_2 + 0.5 \cdot R_{\text{ext}}(1 - \delta), \quad \omega_m = \omega_s(1 - s)$$",
            "text": "Uses 3-phase diode rectifier + DC chopper + external resistor $R_{\\text{ext}}$; duty ratio $\\delta$ provides smooth, stepless resistance variation."
        },
        "exam_answer": r"""
<p><strong>1. Working Principle:</strong><br>
In a slip-ring (wound-rotor) induction motor, speed can be controlled below synchronous speed by adding external resistance into the rotor circuit. Traditional stepped contactor-switched resistors cause jerky torque transitions.<br>
A <strong>Static Rotor Resistance Controller</strong> replaces mechanical contactors with a 3-phase diode bridge rectifier, a DC filter choke, a power transistor chopper ($CH$), and a single external power resistor $R_{\text{ext}}$.</p>

<p><strong>2. Circuit Operation:</strong></p>
<ul>
    <li>Three-phase slip-frequency AC rotor voltages are rectified into DC by the diode bridge.</li>
    <li>The DC chopper switch is switched ON and OFF with time period $T$ and duty cycle $\delta = \frac{t_{\text{on}}}{T}$.</li>
    <li><strong>When Chopper is ON ($0 < t \le t_{\text{on}}$):</strong> Resistor $R_{\text{ext}}$ is short-circuited. Equivalent resistance across DC terminals is zero.</li>
    <li><strong>When Chopper is OFF ($t_{\text{on}} < t \le T$):</strong> Current is forced through resistor $R_{\text{ext}}$, dissipating slip energy.</li>
</ul>

<p><strong>3. Equivalent Effective Rotor Resistance Derivation:</strong><br>
The average resistance seen across the DC chopper terminals is:
$$R_{\text{dc}} = R_{\text{ext}} \left( \frac{T - t_{\text{on}}}{T} \right) = R_{\text{ext}}(1 - \delta)$$
Referred back to the 3-phase AC rotor circuit:
$$R_{\text{eff}} = R_2 + 0.5 \cdot R_{\text{ext}}(1 - \delta)$$
where $R_2$ is the internal rotor winding resistance per phase.</p>

<p><strong>4. Major Operational Advantages:</strong></p>
<ul>
    <li><strong>Smooth, Stepless Speed Control:</strong> Varying duty cycle $\delta$ continuously from $0 \to 1$ varies effective rotor resistance smoothly without mechanical steps.</li>
    <li><strong>Balanced Three-Phase Currents:</strong> Uses a single chopper and a single DC resistor, completely avoiding phase unbalance.</li>
    <li><strong>High Starting Torque with Low Starting Current:</strong> Setting $\delta = 0$ inserts full $R_{\text{ext}}$ at startup for maximum torque ($s_m \approx 1$), then $\delta \to 1$ as the motor reaches operating speed.</li>
</ul>
""",
        "understand_simply": r"""
<p>Instead of manually unplugging and plugging heavy ceramic resistors into the rotor circuit, a static rotor resistance drive uses an ultra-fast electronic switch. By flipping the switch thousands of times a second, the resistor is connected for only a fraction of each cycle. It fools the motor into seeing any smooth resistance value you choose!</p>
"""
    },

    'drive-q14b': {
        "title": "Slip Power Recovery Schemes: Static Kramer vs Static Scherbius Systems",
        "marks": 7,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "Static Kramer: Diode bridge + Inverter (sub-synchronous speed only); Static Scherbius: Cycloconverter / Dual Inverter (bi-directional sub/super-synchronous speed)."
        },
        "exam_answer": r"""
<p><strong>1. Problem with Rotor Resistance Control:</strong><br>
In conventional rotor resistance control, slip power $P_{\text{slip}} = s \cdot P_{\text{airgap}}$ is wasted as heat in resistors, causing terrible efficiency at low speeds. <strong>Slip Power Recovery Schemes</strong> capture this rotor slip power and return it to the AC power grid, dramatically improving drive efficiency.</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Static Kramer Drive System</th>
            <th>Static Scherbius Drive System</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Rotor Converter Topology</strong></td>
            <td>Uncontrolled 3-phase <strong>diode bridge rectifier</strong> connected to line-commutated thyristor inverter.</td>
            <td>Bidirectional converter: <strong>Cycloconverter</strong> or back-to-back PWM inverter (dual IGBT converters).</td>
        </tr>
        <tr>
            <td><strong>Direction of Power Flow</strong></td>
            <td><strong>Unidirectional only:</strong> Slip power can only flow OUT of the rotor and back into the AC grid.</td>
            <td><strong>Bidirectional:</strong> Power can flow from rotor to grid (sub-synchronous) OR from grid into rotor (super-synchronous).</td>
        </tr>
        <tr>
            <td><strong>Speed Range</strong></td>
            <td><strong>Sub-synchronous only:</strong> Operates strictly from standstill up to synchronous speed ($\omega < \omega_s$).</td>
            <td><strong>Sub- and Super-synchronous:</strong> Operates both below synchronous speed ($\omega < \omega_s$) and above synchronous speed ($\omega > \omega_s$).</td>
        </tr>
        <tr>
            <td><strong>Converter Power Rating</strong></td>
            <td>Converter size depends only on maximum slip: $P_{\text{converter}} = s_{\text{max}} \cdot P_{\text{motor}}$ (typically only $20\text{--}30\%$ of motor rating).</td>
            <td>Converter rating is also fractional ($s_{\text{max}} \cdot P_{\text{motor}}$), but requires more complex bidirectional gating.</td>
        </tr>
        <tr>
            <td><strong>Industrial Applications</strong></td>
            <td>Large water pumping stations, boiler feed pumps, mine ventilators, cement kiln fans.</td>
            <td>Doubly-Fed Induction Generators (DFIG) in wind turbines, pumped storage hydro plants, high-speed compressor drives.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p>When an induction motor slows down, the extra energy in the rotor normally turns into useless heat in a resistor. A Slip Power Recovery drive acts like an electrical siphon: it captures that wasted rotor energy, cleans it up, and feeds it straight back into the main building's electrical wiring. You get slow speed without paying an enormous electricity bill!</p>
"""
    },

    # =========================================================================
    # MODULE 5: Synchronous Motor Drives, SVPWM, Transforms & FOC
    # =========================================================================
    'drive-q15': {
        "title": "True Synchronous Mode vs Self-Controlled Mode in Synchronous Motor Drives",
        "marks": 3,
        "remember_this": {
            "title": "Remember This",
            "eq": None,
            "text": "True Synchronous: Open-loop inverter frequency, prone to hunting/pull-out; Self-Controlled: Closed-loop rotor position sensor (brushless DC), never pulls out of synchronism."
        },
        "exam_answer": r"""
<p>Synchronous motor drives are classified into two distinct operating modes based on how inverter frequency is generated:</p>

<table class="exam-table">
    <thead>
        <tr>
            <th>Characteristic</th>
            <th>True Synchronous Mode (Separate Control)</th>
            <th>Self-Controlled Mode (Self-Synchronous)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Frequency Generation</strong></td>
            <td>Inverter frequency is set independently by an <strong>external oscillator / signal generator</strong> (open-loop control).</td>
            <td>Inverter firing pulses are triggered directly by a <strong>rotor position sensor (RPS / Hall sensors / encoder)</strong> mounted on the motor shaft.</td>
        </tr>
        <tr>
            <td><strong>Stability &amp; Hunting</strong></td>
            <td>Prone to hunting oscillations and motor stalling ("pull-out") under sudden shock loads if the torque angle $\delta > 90^\circ$.</td>
            <td><strong>Cannot pull out of synchronism!</strong> The stator field rotates at the exact speed of the rotor, maintaining optimal torque angle $\delta = 90^\circ$ at all times.</td>
        </tr>
        <tr>
            <td><strong>Starting Behavior</strong></td>
            <td>Cannot start on its own; requires amortisseur (damper) winding starting as an induction motor or low-frequency ramping.</td>
            <td>Self-starting from zero speed with smooth, high starting torque (operates electronically like a DC motor $\implies$ <em>Brushless DC Motor</em>).</td>
        </tr>
        <tr>
            <td><strong>Applications</strong></td>
            <td>Multi-motor drives requiring precise lockstep speed synchronization (e.g., synthetic fiber manufacturing, textile mills).</td>
            <td>High-performance servo drives, electric vehicles, robotics, variable-speed industrial pumps.</td>
        </tr>
    </tbody>
</table>
""",
        "understand_simply": r"""
<p><strong>True Synchronous:</strong> Like a marching military band. The drummer sets a rigid tempo. If one soldier trips, the band marches on without him and he falls behind (pulls out of synchronism).</p>
<p><strong>Self-Controlled:</strong> Like a horse and rider. The rider kicks the horse, but the horse's own galloping footsteps dictate the rhythm. The motor controls its own inverter firing, so it can never trip or fall out of step!</p>
"""
    },

    'drive-q15b': {
        "title": "Load-Commutated Inverter (LCI) Fed Synchronous Motor Drives",
        "marks": 3,
        "remember_this": {
            "title": "Key Equation",
            "eq": None,
            "text": "Operates at leading power factor; motor over-excited back-EMF naturally turns off (commutates) thyristors without forced commutation circuits."
        },
        "exam_answer": r"""
<p><strong>1. Working Principle:</strong><br>
A Load-Commutated Inverter (LCI) drive powers a wound-field synchronous motor using standard, low-cost line-commutated thyristor bridges on both the source and load sides:</p>
<ul>
    <li><strong>Line-Side Converter:</strong> 3-phase fully controlled thyristor rectifier connected to utility grid; acts as a regulated DC current source through a large DC link inductor.</li>
    <li><strong>Load-Side Inverter:</strong> 6-thyristor bridge feeding the synchronous motor stator windings.</li>
</ul>

<p><strong>2. Load Commutation Mechanism:</strong></p>
<ul>
    <li>The synchronous motor is deliberately operated in an <strong>over-excited condition</strong> (leading power factor).</li>
    <li>The leading motor counter-EMF ($E_b$) provides reverse bias voltage across outgoing thyristors, naturally turning them off (commutating them) without requiring expensive forced-commutation capacitors or inductors.</li>
</ul>

<p><strong>3. Starting Limitation &amp; Solution:</strong></p>
<ul>
    <li>At very low speeds ($0\text{ to } 10\%$ rated speed), the motor back-EMF is too small to commutate the thyristors.</li>
    <li><strong>Pulsed DC Link Starting:</strong> The line-side converter is momentarily phased back to zero current to extinguish thyristor conduction before firing the next phase pair. Once speed reaches $>10\%$, natural load commutation takes over.</li>
</ul>
<p><strong>Industrial Application:</strong> Mega-watt power ratings (5 MW to 100 MW) in gas pipeline compressors, blast furnace blowers, and pumped-storage hydro generators.</p>
""",
        "understand_simply": r"""
<p>Turning off heavy thyristor switches normally requires complicated shut-off circuits. But if you over-excite a synchronous motor, the motor's own spinning voltage acts like an electronic vacuum that pulls the current to zero and shuts off the switches naturally! It allows massive industrial motors (10,000+ horsepower) to use simple, rugged electronics.</p>
"""
    },

    'drive-q16': {
        "title": "Mathematical Derivation of Clarke and Park Coordinate Reference Frame Transformations",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\text{Clarke: } [a, b, c] \to [\alpha, \beta, 0] \quad (\text{Stationary}), \quad \text{Park: } [\alpha, \beta] \to [d, q] \quad (\text{Rotating at } \omega_e)$$",
            "text": "Transforms coupled 3-phase AC sinusoidal quantities into constant DC-like quantities ($d$-axis flux, $q$-axis torque) for independent control."
        },
        "exam_answer": r"""
<p><strong>1. Purpose of Coordinate Transformations:</strong><br>
In 3-phase AC machines, stator currents ($i_a, i_b, i_c$) are time-varying sinusoids physically displaced by $120^\circ$ in space. Their magnetic couplings vary continuously with rotor angle $\theta$.<br>
Clarke and Park transformations convert these complex, coupled 3-phase AC equations into decoupled 2-axis DC quantities ($d$-$q$ frame) rotating synchronously with the rotor flux.</p>

<p><strong>2. Clarke Transformation ($abc \to \alpha\beta0$ Stationary Frame):</strong><br>
Projects 3-phase stationary axes ($a, b, c$) onto a 2-axis orthogonal stationary reference frame ($\alpha, \beta$):</p>
$$\begin{bmatrix} i_\alpha \\ i_\beta \\ i_0 \end{bmatrix} = \frac{2}{3} \begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$
For balanced 3-phase systems without neutral connection ($i_a + i_b + i_c = 0$), the zero-sequence component $i_0 = 0$:
$$i_\alpha = i_a, \quad i_\beta = \frac{1}{\sqrt{3}}(i_b - i_c)$$

<p><strong>3. Park Transformation ($\alpha\beta \to dq$ Synchronously Rotating Frame):</strong><br>
Rotates the stationary orthogonal axes ($\alpha, \beta$) by electrical rotor flux angle $\theta_e = \int \omega_e dt$ into a synchronously rotating reference frame ($d, q$):</p>
$$\begin{bmatrix} i_d \\ i_q \end{bmatrix} = \begin{bmatrix} \cos\theta_e & \sin\theta_e \\ -\sin\theta_e & \cos\theta_e \end{bmatrix} \begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix}$$

<p><strong>4. Combined Direct Transformation ($abc \to dq0$):</strong><br>
$$\begin{bmatrix} i_d \\ i_q \\ i_0 \end{bmatrix} = \frac{2}{3} \begin{bmatrix} \cos\theta_e & \cos(\theta_e - \frac{2\pi}{3}) & \cos(\theta_e + \frac{2\pi}{3}) \\ -\sin\theta_e & -\sin(\theta_e - \frac{2\pi}{3}) & -\sin(\theta_e + \frac{2\pi}{3}) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$
<strong>Engineering Result:</strong> In the $d$-$q$ frame, steady-state currents become <strong>pure DC quantities</strong>:
<ul>
    <li>$i_d$ controls only the rotor magnetic flux (like field current $I_f$ in a DC motor).</li>
    <li>$i_q$ controls only the electromagnetic torque (like armature current $I_a$ in a DC motor).</li>
</ul>
This complete decoupling is the foundation of Vector Control (FOC).</p>
""",
        "understand_simply": r"""
<p>Imagine riding on a carousel (merry-go-round) while people on the ground wave their hands up and down (3-phase AC sinusoids). From the ground, everything looks like a confusing swirl. But if you jump onto the carousel and spin at the exact same speed (Park transform), the horses around you appear completely motionless (constant DC)! That makes controlling the motor as easy as adjusting a simple DC circuit.</p>
"""
    },

    'drive-q17': {
        "title": "Space Vector Pulse Width Modulation (SVPWM): Principles, Sectors, and Dwell Times",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$T_1 = \frac{\sqrt{3} T_s V_{\text{ref}}}{V_{\text{dc}}} \sin(60^\circ - \theta), \quad T_2 = \frac{\sqrt{3} T_s V_{\text{ref}}}{V_{\text{dc}}} \sin\theta, \quad T_0 = T_s - (T_1 + T_2)$$",
            "text": r"SVPWM yields $15.5\%$ higher DC bus voltage utilization ($V_{1,\text{max}} = V_{\text{dc}}/\sqrt{3} = 0.577 V_{\text{dc}}$) than Sine PWM."
        },
        "exam_answer": r"""
<p><strong>1. Space Vector Concept:</strong><br>
A 3-phase Voltage Source Inverter (VSI) has six switches with 8 possible switching states $(S_a, S_b, S_c)$. These generate 6 active non-zero voltage space vectors ($V_1 \dots V_6$) of magnitude $\frac{2}{3} V_{\text{dc}}$ spaced $60^\circ$ apart, and 2 zero vectors ($V_0(000)$ and $V_7(111)$) located at the origin of the complex plane.</p>
<p>The 6 active vectors divide the circular space into <strong>6 equal sectors ($60^\circ$ each)</strong>.</p>

<p><strong>2. Reference Voltage Vector Synthesis:</strong><br>
To produce a sinusoidal balanced 3-phase voltage, a reference voltage vector $V_{\text{ref}}$ of constant magnitude rotates smoothly at angular frequency $\omega$.<br>
In any sector (say Sector 1, where $0 \le \theta \le 60^\circ$), $V_{\text{ref}}$ is synthesized over a switching sub-cycle $T_s$ by modulating the two adjacent active vectors ($V_1, V_2$) and the zero vectors ($V_0, V_7$):</p>
$$V_{\text{ref}} T_s = V_1 T_1 + V_2 T_2 + V_0 T_0$$
where $T_1, T_2$ are active dwell times, and $T_0$ is the total zero-vector dwell time ($T_0 = T_s - T_1 - T_2$).</p>

<p><strong>3. Dwell Time Equations (Sector 1):</strong><br>
Resolving along orthogonal axes:
$$T_1 = \frac{\sqrt{3} T_s V_{\text{ref}}}{V_{\text{dc}}} \sin\left(\frac{\pi}{3} - \theta\right)$$
$$T_2 = \frac{\sqrt{3} T_s V_{\text{ref}}}{V_{\text{dc}}} \sin(\theta)$$
$$T_0 = T_s - (T_1 + T_2)$$
The zero time $T_0$ is divided equally between $V_0(000)$ and $V_7(111)$ using a symmetrical 7-segment switching sequence ($V_0 \to V_1 \to V_2 \to V_7 \to V_2 \to V_1 \to V_0$) to minimize inverter switching losses.</p>

<p><strong>4. Major Advantages over Sinusoidal PWM (SPWM):</strong></p>
<ul>
    <li><strong>15.5% Higher DC Bus Utilization:</strong> Maximum fundamental peak line-to-neutral voltage without overmodulation is $V_{\text{peak}} = \frac{V_{\text{dc}}}{\sqrt{3}} \approx 0.577 V_{\text{dc}}$, compared to $0.5 V_{\text{dc}}$ for standard SPWM.</li>
    <li><strong>Lower Current Harmonic Distortion (THD):</strong> Symmetrical zero-vector placement reduces motor ripple current and acoustic noise.</li>
    <li><strong>Ideal for Digital Implementation:</strong> Directly programmed in modern DSP / FPGA motor controllers using timer counters.</li>
</ul>
""",
        "understand_simply": r"""
<p>Imagine pushing a boat in a smooth circle, but you only have two friends pushing in fixed directions $60^\circ$ apart. To move in any angle between them, Friend 1 pushes for 3 seconds, Friend 2 pushes for 2 seconds, and both rest for 1 second. By constantly adjusting how long each friend pushes during each 6-second window, the boat glides in a perfect circle!</p>
"""
    },

    'drive-q18': {
        "title": "Field-Oriented Control (Vector Control) of Three-Phase Induction Motors",
        "marks": 7,
        "remember_this": {
            "title": "Key Equation",
            "eq": r"$$\psi_{rq} = 0, \quad \psi_{rd} = \psi_r \implies T_e = \frac{3}{2}\frac{P}{2}\frac{L_m}{L_r}\psi_{rd} i_{sq}$$",
            "text": "Aligns $d$-axis with rotor flux vector $\\psi_r$; completely decouples flux control ($i_{sd}$) from torque control ($i_{sq}$), giving DC-motor performance."
        },
        "exam_answer": r"""
<p><strong>1. Problem with Scalar (V/f) Control:</strong><br>
In scalar V/f control, stator voltage and frequency are adjusted, but flux and torque are coupled dynamically. Changing torque inherently perturbs flux, causing sluggish transient response (settling time $100\text{--}500\text{ ms}$).</p>

<p><strong>2. Field-Oriented Control (FOC) Principle:</strong><br>
Field-Oriented Control transforms the induction motor control into that of a separately excited DC motor by aligning the $d$-axis of the synchronously rotating reference frame with the <strong>Rotor Flux Vector $\boldsymbol{\psi}_r$</strong>:</p>
$$\psi_{rd} = \psi_r \quad \text{and} \quad \psi_{rq} = 0$$

<p><strong>3. Decoupled Flux and Torque Equations:</strong><br>
Under this field-alignment condition:
<ul>
    <li><strong>Rotor Flux Equation:</strong>
    $$\tau_r \frac{d\psi_r}{dt} + \psi_r = L_m i_{sd}$$
    In steady state, $\psi_r = L_m i_{sd}$. The rotor flux magnitude is controlled <em>exclusively</em> by the direct-axis stator current component $i_{sd}$ (analogous to DC motor field current $I_f$).</li>
    <li><strong>Electromagnetic Torque Equation:</strong>
    $$T_e = \frac{3}{2} \left(\frac{P}{2}\right) \frac{L_m}{L_r} \psi_{rd} i_{sq} = K_t \cdot \psi_r \cdot i_{sq}$$
    When flux $\psi_r$ is held constant, torque is directly and linearly proportional to the quadrature-axis stator current component $i_{sq}$ (analogous to DC motor armature current $I_a$).</li>
</ul>

<p><strong>4. Rotor Flux Position Estimation (Indirect FOC):</strong><br>
The rotor flux angle $\theta_e$ needed for Park transformation is computed by adding rotor mechanical angle $\theta_r$ and slip angle $\theta_{sl}$:
$$\theta_e = \theta_r + \int \omega_{sl} dt, \quad \text{where slip speed is } \omega_{sl} = \frac{L_m}{\tau_r \psi_r} i_{sq}$$</p>

<p><strong>5. Performance Superiority:</strong><br>
FOC provides instantaneous torque response (under $5\text{ ms}$), full torque capability at zero speed, and high dynamic precision required in electric vehicles, wind turbines, rolling mills, and elevators.</p>
""",
        "understand_simply": r"""
<p>In a standard induction motor, changing the throttle changes both the magnetic field and the pulling torque at the same time—like trying to steer and accelerate with a single combined joystick. Vector Control cleanly splits them apart: you get one independent dial for magnetic strength ($i_{sd}$) and another independent dial for instant pulling torque ($i_{sq}$). It makes an AC motor behave just like a DC motor!</p>
"""
    }
}
