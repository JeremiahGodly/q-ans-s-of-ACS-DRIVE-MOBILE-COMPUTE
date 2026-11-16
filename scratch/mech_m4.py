# -*- coding: utf-8 -*-
"""
Module 4: Kinematics and Kinetics of Particles (mech-q16 to mech-q20)
KTU 2019 Scheme Engineering Mechanics (EST100)
"""

MODULE_4 = {
    "module_id": "mech-m4",
    "module_num": "Module 4",
    "module_title": "Kinematics and Kinetics of Particles, D'Alembert's Principle",
    "questions": [
        {
            "qid": "mech-q16",
            "marks": 7,
            "type": "Derivation & Analytical",
            "title": "Rectilinear Motion with Variable Acceleration: Calculus Formulation and Resisted Motion",
            "yt_query": "rectilinear motion variable acceleration integration resisted motion engineering mechanics",
            "img_path": "images/mechanics/variable_acceleration.png",
            "img_caption": "Figure 4.1: Kinematic Position, Velocity, and Acceleration Profiles for Resisted Rectilinear Motion",
            "answer": r"""
Rectilinear motion describes the one-dimensional translation of a particle along a straight line path. When acceleration is constant, motion is governed by standard algebraic kinematic equations ($v = u + at, s = ut + \frac{1}{2}at^2, v^2 = u^2 + 2as$). However, in most engineering situations—such as aerodynamic drag, vehicle braking, fluid viscosity resistance, or spring-mass dynamics—acceleration varies continuously as a function of time $t$, velocity $v$, or displacement $s$.

Fundamental Differential Kinematic Equations:
The position coordinate of a particle along a straight line is $s(t)$.
The instantaneous velocity $v$ is the first time derivative of displacement:
$$v = \frac{ds}{dt} \implies ds = v \, dt$$
The instantaneous acceleration $a$ is the time derivative of velocity:
$$a = \frac{dv}{dt} = \frac{d^2 s}{dt^2} \implies dv = a \, dt$$
By applying the chain rule of differentiation, time $t$ can be eliminated to link acceleration directly to displacement:
$$a = \frac{dv}{dt} = \frac{dv}{ds} \cdot \frac{ds}{dt} = v \frac{dv}{ds} \implies v \, dv = a \, ds$$

Analytical Solutions for Specific Functional Forms of Acceleration:
1. Case 1: Acceleration as a Function of Time, $a = f(t)$:
Separating variables in $dv = a \, dt$:
$$\int_{v_0}^v dv = \int_0^t f(t) \, dt \implies v(t) = v_0 + \int_0^t f(t) \, dt$$
Once $v(t)$ is obtained, displacement is integrated:
$$\int_{s_0}^s ds = \int_0^t v(t) \, dt \implies s(t) = s_0 + \int_0^t v(t) \, dt$$

2. Case 2: Acceleration as a Function of Displacement, $a = f(s)$:
Separating variables in $v \, dv = a \, ds$:
$$\int_{v_0}^v v \, dv = \int_{s_0}^s f(s) \, ds \implies \frac{v^2 - v_0^2}{2} = \int_{s_0}^s f(s) \, ds \implies v(s) = \sqrt{v_0^2 + 2\int_{s_0}^s f(s) \, ds}$$
Time is then obtained by integrating $dt = \frac{ds}{v(s)}$:
$$t = \int_{s_0}^s \frac{ds}{v(s)}$$

3. Case 3: Acceleration as a Function of Velocity (Resisted Fluid Motion), $a = -k v$:
Consider a particle launched into a viscous fluid with initial velocity $v_0$ at $t = 0, s = 0$. The fluid exerts a resisting drag force proportional to velocity, resulting in deceleration:
$$a = \frac{dv}{dt} = -k v$$
where $k$ is a positive constant of drag per unit mass ($s^{-1}$).
- Velocity as a Function of Time:
Separating variables:
$$\frac{dv}{v} = -k \, dt$$
Integrating from initial velocity $v_0$ at $t = 0$ to velocity $v$ at time $t$:
$$\int_{v_0}^v \frac{dv}{v} = -k \int_0^t dt \implies \left[ \ln v \right]_{v_0}^v = -k t \implies \ln\left(\frac{v}{v_0}\right) = -k t$$
Exponentiating both sides:
$$v(t) = v_0 e^{-k t}$$
The velocity decays exponentially with time, approaching zero asymptotically as $t \to \infty$.

- Displacement as a Function of Time:
Substituting $v = \frac{ds}{dt}$:
$$\frac{ds}{dt} = v_0 e^{-k t} \implies ds = v_0 e^{-k t} \, dt$$
Integrating with initial condition $s(0) = 0$:
$$\int_0^s ds = v_0 \int_0^t e^{-k t} \, dt \implies s(t) = v_0 \left[ \frac{e^{-k t}}{-k} \right]_0^t = \frac{v_0}{k} \left(1 - e^{-k t}\right)$$
- Maximum Distance Traveled Before Coming to Rest:
As time approaches infinity ($t \to \infty$), $e^{-k t} \to 0$. The total stopping distance $s_{max}$ is finite:
$$s_{max} = \lim_{t \to \infty} \frac{v_0}{k}\left(1 - e^{-k t}\right) = \frac{v_0}{k}$$
Alternatively, using $a = v \frac{dv}{ds} = -kv \implies dv = -k \, ds$. Integrating from $v_0$ to $0$ gives $0 - v_0 = -k s_{max} \implies s_{max} = \frac{v_0}{k}$. This demonstrates the consistency of the differential approach.
"""
        },
        {
            "qid": "mech-q17",
            "marks": 7,
            "type": "Derivation",
            "title": "Projectile Motion: Trajectory Equation, Time of Flight, Maximum Height, and Range",
            "yt_query": "projectile motion derivation trajectory equation time of flight maximum height horizontal range",
            "img_path": "images/mechanics/projectile_motion.png",
            "img_caption": "Figure 4.2: Parabolic Trajectory of a Projectile Showing Velocity Vectors and Range",
            "answer": r"""
A projectile is any object projected into the atmosphere with an initial velocity that continues in motion under the sole influence of gravity (assuming air resistance is negligible). Because gravity acts purely in the vertical downward direction, the horizontal and vertical motions are independent.

Kinematic Formulation and Coordinate Setup:
Let a particle be projected from origin $O(0,0)$ with an initial velocity $u$ at an angle of projection $\theta$ with the horizontal $x$-axis.
Resolving initial velocity $u$ into Cartesian components:
- Initial horizontal velocity: $u_x = u \cos\theta$
- Initial vertical velocity: $u_y = u \sin\theta$

Governing Equations of Motion:
1. Horizontal Motion: Zero horizontal acceleration ($a_x = 0$):
The horizontal velocity remains constant throughout the flight:
$$v_x(t) = u_x = u \cos\theta$$
The horizontal displacement at any time $t$ is:
$$x(t) = (u \cos\theta) t \implies t = \frac{x}{u \cos\theta} \quad \text{--- (Equation 1)}$$
2. Vertical Motion: Downward gravitational acceleration ($a_y = -g$):
The vertical velocity at any time $t$ is:
$$v_y(t) = u \sin\theta - g t$$
The vertical displacement at time $t$ is:
$$y(t) = (u \sin\theta) t - \frac{1}{2} g t^2 \quad \text{--- (Equation 2)}$$

1. Derivation of the Equation of the Path (Trajectory):
To determine the geometric path, we eliminate time parameter $t$ by substituting Equation 1 into Equation 2:
$$y = (u \sin\theta) \left( \frac{x}{u \cos\theta} \right) - \frac{1}{2} g \left( \frac{x}{u \cos\theta} \right)^2$$
$$y = x \left(\frac{\sin\theta}{\cos\theta}\right) - \frac{g x^2}{2 u^2 \cos^2\theta} \implies y = x \tan\theta - \frac{g x^2}{2 u^2 \cos^2\theta}$$
This equation is of the standard quadratic form $y = A x - B x^2$ (where $A = \tan\theta$ and $B = \frac{g}{2u^2 \cos^2\theta}$ are constants). This proves that the trajectory of an unresisted projectile is a parabola with its vertex pointing upward.

2. Derivation of Time of Flight ($T$):
The total time of flight $T$ is the total elapsed time from projection until the projectile strikes the horizontal ground plane again ($y = 0$).
Setting $y = 0$ in the vertical displacement equation:
$$0 = (u \sin\theta) T - \frac{1}{2} g T^2 \implies T \left( u \sin\theta - \frac{1}{2} g T \right) = 0$$
Since $T \neq 0$ (which corresponds to launch):
$$u \sin\theta - \frac{1}{2} g T = 0 \implies \frac{1}{2} g T = u \sin\theta$$
$$T = \frac{2 u \sin\theta}{g}$$
The time to reach the maximum height $t_h$ (where vertical velocity vanishes, $v_y = 0 \implies u \sin\theta - g t_h = 0$) is exactly half the total time of flight:
$$t_h = \frac{u \sin\theta}{g} = \frac{T}{2}$$

3. Derivation of Maximum Vertical Height ($H$):
At the peak apex of the trajectory ($t = t_h = \frac{u \sin\theta}{g}$), the vertical displacement reaches its maximum value $H$.
Using the kinematic relation $v_y^2 = u_y^2 - 2g H$ with $v_y = 0$:
$$0 = (u \sin\theta)^2 - 2g H \implies 2g H = u^2 \sin^2\theta$$
$$H = \frac{u^2 \sin^2\theta}{2g}$$

4. Derivation of Horizontal Range ($R$) and Condition for Maximum Range:
The horizontal range $R$ is the horizontal distance covered during the entire time of flight $T$:
$$R = x(T) = (u \cos\theta) \cdot T = (u \cos\theta) \left( \frac{2 u \sin\theta}{g} \right) = \frac{u^2 (2 \sin\theta \cos\theta)}{g}$$
Using the trigonometric identity $2 \sin\theta \cos\theta = \sin(2\theta)$:
$$R = \frac{u^2 \sin(2\theta)}{g}$$

Condition for Maximum Horizontal Range ($R_{max}$):
For a given launch velocity $u$, the range $R$ depends solely on the launch angle $\theta$. To find the angle that maximizes $R$:
$$\frac{dR}{d\theta} = \frac{u^2}{g} \frac{d}{d\theta}[\sin(2\theta)] = \frac{u^2}{g} [2 \cos(2\theta)] = 0$$
$$\cos(2\theta) = 0 \implies 2\theta = 90^\circ \implies \theta = 45^\circ$$
The maximum horizontal range is achieved at a projection angle of $45^\circ$:
$$R_{max} = \frac{u^2 \sin(90^\circ)}{g} = \frac{u^2}{g}$$
For any range $R < R_{max}$, two complementary launch angles ($\theta$ and $90^\circ - \theta$) produce the exact same horizontal range, since $\sin[2(90^\circ - \theta)] = \sin(180^\circ - 2\theta) = \sin(2\theta)$.
"""
        },
        {
            "qid": "mech-q18",
            "marks": 7,
            "type": "Derivation",
            "title": "Normal and Tangential Acceleration in Curvilinear Motion",
            "yt_query": "normal and tangential acceleration derivation curvilinear motion engineering mechanics",
            "img_path": "images/mechanics/normal_tangential_acceleration.png",
            "img_caption": "Figure 4.3: Intrinsic Coordinate System Showing Tangential and Normal Acceleration Vectors",
            "answer": r"""
When a particle moves along a general curved path in a two-dimensional plane, its velocity vector changes continuously in both magnitude (speed) and spatial direction. While Cartesian coordinates $(x,y)$ are often convenient, describing motion using the intrinsic coordinate system defined by Tangential ($\hat{\mathbf{e}}_t$) and Normal ($\hat{\mathbf{e}}_n$) unit vectors provides direct physical insight into the dynamics of curved motion.

Intrinsic Coordinate System Formulation:
Let a particle move along a planar curve described by path arc length $s(t)$. At any point $P$ along the trajectory:
- Tangential Unit Vector $\hat{\mathbf{e}}_t$: Directed tangent to the path curve pointing in the direction of increasing arc length $s$ (direction of motion).
- Principal Normal Unit Vector $\hat{\mathbf{e}}_n$: Directed perpendicular to the tangent, pointing inwards toward the instantaneous center of curvature $C$ of the path.
By fundamental definition, the velocity vector $\mathbf{v}$ is always directed along the instantaneous tangent:
$$\mathbf{v} = v \, \hat{\mathbf{e}}_t = \left(\frac{ds}{dt}\right) \hat{\mathbf{e}}_t$$
where $v = \frac{ds}{dt}$ is the scalar speed of the particle.

Derivation of the Acceleration Vector:
The acceleration vector $\mathbf{a}$ is the total time derivative of the velocity vector:
$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}\left( v \, \hat{\mathbf{e}}_t \right)$$
Applying the product rule of differentiation:
$$\mathbf{a} = \frac{dv}{dt} \hat{\mathbf{e}}_t + v \frac{d\hat{\mathbf{e}}_t}{dt} \quad \text{--- (Equation 1)}$$

To evaluate the time derivative of the unit tangent vector $\frac{d\hat{\mathbf{e}}_t}{dt}$:
Let the particle move a differential distance $ds$ from point $P$ to a neighboring point $P'$ along the curve in time $dt$.
At point $P$, the tangent is inclined at angle $\theta$ to a fixed reference direction.
At point $P'$, the tangent is inclined at angle $\theta + d\theta$.
The change in the unit tangent vector is $d\hat{\mathbf{e}}_t = \hat{\mathbf{e}}_t(P') - \hat{\mathbf{e}}_t(P)$.
Because $\hat{\mathbf{e}}_t$ has constant unit magnitude ($|\hat{\mathbf{e}}_t| = 1$), the vector triangle formed by $\hat{\mathbf{e}}_t$, $\hat{\mathbf{e}}_t + d\hat{\mathbf{e}}_t$, and $d\hat{\mathbf{e}}_t$ is an isosceles triangle with vertex angle $d\theta$.
For an infinitesimal angle $d\theta$:
$$|d\hat{\mathbf{e}}_t| \approx 1 \cdot d\theta = d\theta$$
As $dt \to 0$, the vector $d\hat{\mathbf{e}}_t$ becomes perpendicular to $\hat{\mathbf{e}}_t$ and points toward the inside of the curve (in the direction of the normal unit vector $\hat{\mathbf{e}}_n$).
Therefore, in vector form:
$$d\hat{\mathbf{e}}_t = d\theta \, \hat{\mathbf{e}}_n$$
Dividing by differential time $dt$:
$$\frac{d\hat{\mathbf{e}}_t}{dt} = \frac{d\theta}{dt} \hat{\mathbf{e}}_n = \left(\frac{d\theta}{ds} \cdot \frac{ds}{dt}\right) \hat{\mathbf{e}}_n$$
From differential geometry, the curvature of a plane curve is $\kappa = \frac{d\theta}{ds} = \frac{1}{\rho}$, where $\rho$ is the instantaneous Radius of Curvature.
Since $\frac{ds}{dt} = v$:
$$\frac{d\hat{\mathbf{e}}_t}{dt} = \left(\frac{1}{\rho} \cdot v\right) \hat{\mathbf{e}}_n = \frac{v}{\rho} \hat{\mathbf{e}}_n \quad \text{--- (Equation 2)}$$

Substituting Equation 2 back into Equation 1 yields the complete acceleration vector:
$$\mathbf{a} = \frac{dv}{dt} \hat{\mathbf{e}}_t + \frac{v^2}{\rho} \hat{\mathbf{e}}_n = a_t \hat{\mathbf{e}}_t + a_n \hat{\mathbf{e}}_n$$

Physical Interpretation of Acceleration Components:
1. Tangential Acceleration Component ($a_t$):
$$a_t = \frac{dv}{dt} = \dot{v} = v \frac{dv}{ds} = \frac{d^2 s}{dt^2}$$
$a_t$ measures the time rate of change of the magnitude of velocity (speed).
- If the particle speeds up, $a_t > 0$ (points in the direction of motion, $+\hat{\mathbf{e}}_t$).
- If the particle slows down (brakes), $a_t < 0$ (opposes motion, $-\hat{\mathbf{e}}_t$).
- In uniform circular motion (constant speed), $a_t = 0$.
2. Normal (Centripetal) Acceleration Component ($a_n$):
$$a_n = \frac{v^2}{\rho}$$
$a_n$ measures the time rate of change of the direction of the velocity vector.
- It is always directed perpendicular to the path inward toward the center of curvature ($+\hat{\mathbf{e}}_n$).
- $a_n$ can never be negative, and is zero only if the path is a straight line ($\rho \to \infty$).

Resultant Acceleration Magnitude and Direction:
Because the tangential and normal unit vectors are mutually orthogonal ($\hat{\mathbf{e}}_t \cdot \hat{\mathbf{e}}_n = 0$), the total acceleration magnitude is:
$$a = \sqrt{a_t^2 + a_n^2} = \sqrt{\left(\frac{dv}{dt}\right)^2 + \left(\frac{v^2}{\rho}\right)^2}$$
The angle $\phi$ between total acceleration $\mathbf{a}$ and the tangential direction of motion is:
$$\tan\phi = \frac{a_n}{a_t} = \frac{v^2 / \rho}{dv / dt} \implies \phi = \tan^{-1}\left(\frac{a_n}{a_t}\right)$$
"""
        },
        {
            "qid": "mech-q19",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Newton's Second Law and D'Alembert's Principle: Dynamic Equilibrium of Connected Bodies",
            "yt_query": "dalemberts principle dynamic equilibrium connected bodies atwood machine mechanics",
            "img_path": "images/mechanics/dalembert_principle.png",
            "img_caption": "Figure 4.4: Dynamic Equilibrium of Accelerating Elevator and Connected Pulley System Using Inertia Forces",
            "answer": r"""
Sir Isaac Newton's Second Law of Motion forms the foundation of classical particle kinetics: the net external force $\Sigma \mathbf{F}$ acting on a particle of constant mass $m$ produces an acceleration $\mathbf{a}$ directly proportional to the force and in the same direction:
$$\Sigma \mathbf{F} = m \mathbf{a}$$
While Newton's formulation describes a dynamic non-equilibrium state, in 1743 French mathematician Jean le Rond d'Alembert proposed a principle that transforms dynamic problems into equivalent static equilibrium problems.

D'Alembert's Principle of Dynamic Equilibrium:
D'Alembert's principle states that a system of particles or a rigid body undergoing accelerated motion can be brought into a state of dynamic equilibrium by adding an imaginary force called the Inertia Force (or reverse-effective force) to the system of actual external forces.
The Inertia Force $\mathbf{F}_i$ is defined mathematically as the negative product of mass and acceleration:
$$\mathbf{F}_i = -m \mathbf{a}$$
Adding the inertia force to Newton's second law:
$$\Sigma \mathbf{F} + (-m \mathbf{a}) = 0 \implies \Sigma \mathbf{F} + \mathbf{F}_i = 0$$
Statement of the Principle:
The vector sum of all external physical forces acting on a body and the fictitious inertia force is identically equal to zero.
This formulation allows engineers to analyze complex dynamic mechanisms using the familiar methods of statics:
$$\Sigma F_x = 0, \quad \Sigma F_y = 0, \quad \Sigma M_O = 0$$

Application 1: Apparent Weight in an Accelerating Elevator:
Consider a passenger of mass $m$ standing on a weighing scale inside an elevator cab undergoing vertical acceleration $a$.
Forces acting on the passenger:
- Real external forces: Downward weight $W = mg$ ($\downarrow$), Upward normal reaction $N$ from scale ($\uparrow$).
- Fictitious inertia force: $\mathbf{F}_i = -m\mathbf{a}$.
1. Elevator Accelerating Upward ($+a \uparrow$):
The inertia force acts downward: $F_i = ma$ ($\downarrow$).
Applying dynamic equilibrium ($\Sigma F_y = 0$):
$$N - mg - ma = 0 \implies N = m(g + a)$$
The weighing scale reads an increased apparent weight ($N > mg$).
2. Elevator Accelerating Downward ($-a \downarrow$):
The inertia force acts upward: $F_i = ma$ ($\uparrow$).
Applying dynamic equilibrium:
$$N + ma - mg = 0 \implies N = m(g - a)$$
The apparent weight decreases ($N < mg$).
3. Free Fall ($a = g \downarrow$):
$$N = m(g - g) = 0$$
The passenger experiences apparent weightlessness.

Application 2: Atwood's Machine (Connected Bodies Over a Smooth Pulley):
Problem Statement: Two bodies of unequal masses $m_1$ and $m_2$ ($m_1 > m_2$) are suspended from the ends of a light, flexible, inextensible cord passing over a frictionless, massless pulley. Determine the common acceleration $a$ of the system and the tension $T$ in the cord using D'Alembert's principle.

Analytical Solution Using Dynamic Equilibrium:
Because the cord is inextensible, mass $m_1$ accelerates downward with acceleration $a$ ($\downarrow$), while mass $m_2$ accelerates upward with the identical acceleration $a$ ($\uparrow$).
1. Dynamic Equilibrium of Mass $m_1$:
Real forces: Downward weight $m_1 g$ ($\downarrow$), Upward cable tension $T$ ($\uparrow$).
Since acceleration is downward, the inertia force acts upward: $F_{i1} = m_1 a$ ($\uparrow$).
Applying static equilibrium condition ($\Sigma F_y = 0$):
$$T + m_1 a - m_1 g = 0 \implies T = m_1(g - a) \quad \text{--- (Equation 1)}$$

2. Dynamic Equilibrium of Mass $m_2$:
Real forces: Downward weight $m_2 g$ ($\downarrow$), Upward cable tension $T$ ($\uparrow$).
Since acceleration is upward, the inertia force acts downward: $F_{i2} = m_2 a$ ($\downarrow$).
Applying static equilibrium condition ($\Sigma F_y = 0$):
$$T - m_2 g - m_2 a = 0 \implies T = m_2(g + a) \quad \text{--- (Equation 2)}$$

3. Solving for Common Acceleration $a$:
Equating Equations 1 and 2:
$$m_1(g - a) = m_2(g + a)$$
$$m_1 g - m_1 a = m_2 g + m_2 a$$
Rearranging terms:
$$(m_1 + m_2) a = (m_1 - m_2) g$$
$$a = \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g$$

4. Solving for Cord Tension $T$:
Substituting $a$ into Equation 2:
$$T = m_2 \left[ g + \left(\frac{m_1 - m_2}{m_1 + m_2}\right) g \right] = m_2 g \left[ 1 + \frac{m_1 - m_2}{m_1 + m_2} \right] = m_2 g \left[ \frac{m_1 + m_2 + m_1 - m_2}{m_1 + m_2} \right]$$
$$T = \left(\frac{2 m_1 m_2}{m_1 + m_2}\right) g$$
This demonstrates how D'Alembert's principle transforms dynamic systems into straightforward static force balance equations.
"""
        },
        {
            "qid": "mech-q20",
            "marks": 7,
            "type": "Theory & Application",
            "title": "Connected Bodies on Rough Inclined Planes: Complete Equations of Motion and Tension",
            "yt_query": "connected bodies rough inclined plane friction pulley acceleration tension mechanics",
            "img_path": "images/mechanics/inclined_plane_connected.png",
            "img_caption": "Figure 4.5: Free Body Diagrams for Block on Rough Incline Connected to Hanging Weight via Pulley",
            "answer": r"""
A fundamental problem in engineering mechanics involves the dynamic motion of interconnected bodies where one mass slides along a rough inclined plane while connected by a flexible cord over a pulley to a second hanging mass. This configuration models hoist haulage systems, inclined conveyor lines, and mine shaft cars.

System Description and Free Body Formulation:
Consider a body $A$ of mass $m_1$ resting on a rough plane inclined at angle $\alpha$ to the horizontal. The coefficient of kinetic friction between body $A$ and the plane is $\mu$. A light, flexible, inextensible cord attached to body $A$ passes over a smooth, frictionless, massless pulley fixed at the apex of the incline, supporting a hanging body $B$ of mass $m_2$ at its opposite end.
Assume mass $m_2$ is sufficiently heavy to pull mass $m_1$ up the inclined plane with an acceleration $a$.
- Mass $m_1$ moves up the incline with acceleration $a$ directed parallel to the slope ($\nearrow$).
- Mass $m_2$ moves vertically downward with acceleration $a$ ($\downarrow$).
Both bodies share the same acceleration magnitude $a$ due to cord inextensibility, and the tension $T$ is uniform throughout the cord.

1. Analysis of Body $A$ on the Rough Incline (Moving Upward):
Set up a tilted Cartesian coordinate system with the $x$-axis parallel to the incline pointing upward ($\nearrow$) and the $y$-axis perpendicular to the incline pointing outward ($\nwarrow$).
Forces acting on mass $m_1$:
- Weight $W_1 = m_1 g$ acting vertically downward ($\downarrow$).
  Resolving into components:
  - Perpendicular to incline: $m_1 g \cos\alpha$ ($-\hat{\mathbf{j}}$)
  - Parallel to incline acting down the slope: $m_1 g \sin\alpha$ ($-\hat{\mathbf{i}}$)
- Normal reaction $N$ exerted by the incline on $m_1$ ($+\hat{\mathbf{j}}$).
- Cable tension $T$ pulling up the incline ($+\hat{\mathbf{i}}$).
- Kinetic friction force $F_k = \mu N$. Because the block moves up the slope, friction acts down the slope ($-\hat{\mathbf{i}}$) opposing motion.

Applying equilibrium perpendicular to the incline ($\Sigma F_y = 0$):
$$N - m_1 g \cos\alpha = 0 \implies N = m_1 g \cos\alpha$$
The kinetic friction force is therefore:
$$F_k = \mu N = \mu m_1 g \cos\alpha$$
Applying Newton's second law / D'Alembert's dynamic equilibrium along the incline ($\Sigma F_x = m_1 a$):
$$T - m_1 g \sin\alpha - F_k = m_1 a$$
Substituting $F_k$:
$$T - m_1 g \sin\alpha - \mu m_1 g \cos\alpha = m_1 a \quad \text{--- (Equation 1)}$$
Solving for tension $T$:
$$T = m_1 a + m_1 g (\sin\alpha + \mu \cos\alpha)$$

2. Analysis of Hanging Body $B$ (Moving Downward):
Forces acting on hanging mass $m_2$:
- Downward gravitational weight: $m_2 g$ ($\downarrow$).
- Upward cable tension: $T$ ($\uparrow$).
Applying Newton's second law in the downward direction ($\Sigma F_y = m_2 a$):
$$m_2 g - T = m_2 a \quad \text{--- (Equation 2)}$$
Solving for tension $T$:
$$T = m_2 (g - a)$$

3. Derivation of Common System Acceleration ($a$):
Adding Equation 1 and Equation 2 eliminates the internal cord tension $T$:
$$(T - m_1 g \sin\alpha - \mu m_1 g \cos\alpha) + (m_2 g - T) = m_1 a + m_2 a$$
$$m_2 g - m_1 g (\sin\alpha + \mu \cos\alpha) = (m_1 + m_2) a$$
Factoring out $g$:
$$g \left[ m_2 - m_1(\sin\alpha + \mu \cos\alpha) \right] = (m_1 + m_2) a$$
Dividing by total system mass $(m_1 + m_2)$ gives the acceleration:
$$a = \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g$$

Condition for Motion to Occur:
For mass $m_1$ to accelerate up the incline ($a > 0$), the numerator must be strictly positive:
$$m_2 > m_1(\sin\alpha + \mu \cos\alpha)$$
If $m_2 < m_1(\sin\alpha - \mu \cos\alpha)$, the block will accelerate down the incline (reversing the sign of friction).
If $m_2$ falls between these two limits, the system remains in static equilibrium at rest ($a = 0$).

4. Derivation of Cable Tension ($T$):
Substituting the acceleration expression $a$ back into Equation 2:
$$T = m_2 (g - a) = m_2 \left[ g - \frac{m_2 - m_1(\sin\alpha + \mu \cos\alpha)}{m_1 + m_2} g \right]$$
$$T = \frac{m_2 g}{m_1 + m_2} \left[ (m_1 + m_2) - m_2 + m_1(\sin\alpha + \mu \cos\alpha) \right]$$
$$T = \frac{m_1 m_2 g}{m_1 + m_2} \left[ 1 + \sin\alpha + \mu \cos\alpha \right]$$
This closed-form solution yields both the motion acceleration and internal cable tension for the connected system.
"""
        }
    ]
}
