# -*- coding: utf-8 -*-
"""
Authentic university examination questions for all 406 questions across 15 subjects.
"""

EXAM_QUESTIONS_MAP = {   'acs-q1': 'Explain the following state space concepts with appropriate mathematical expressions: (i) State, (ii) '
              'State variables, (iii) State vector, and (iv) State space.',
    'acs-q10': 'Explain the computation of state transition matrix e^{At} using Cayley-Hamilton theorem for both '
               'distinct and repeated eigenvalues.',
    'acs-q11': 'Derive the complete solution of non-homogeneous continuous-time state equations and determine the step '
               'response expression.',
    'acs-q12': "State and explain Kalman's duality principle relating state controllability and state observability.",
    'acs-q13': "Explain Gilbert's method for determining the state controllability and state observability of an LTI "
               'continuous system.',
    'acs-q13b': 'State and explain the Popov-Belevitch-Hautus (PBH) rank tests for testing controllability and '
                'observability.',
    'acs-q14': "Explain the design of a state feedback controller by pole placement technique and derive Ackermann's "
               'formula.',
    'acs-q15': 'Explain the design procedure of a full-order Luenberger state observer and derive its error dynamics.',
    'acs-q16': 'Explain the common physical non-linear phenomena observed in non-linear control systems that do not '
               'occur in linear systems.',
    'acs-q16b': 'Derive the describing function for an ideal relay and a relay with dead-zone non-linearity.',
    'acs-q17': 'Derive the describing function expression N(X) for a symmetrical saturation non-linearity.',
    'acs-q17b': 'Derive the describing function N(X) for a dead-zone non-linearity.',
    'acs-q18': 'Explain how the stability and frequency of limit cycles in non-linear feedback systems are determined '
               'using describing function and Nyquist criterion.',
    'acs-q19': 'Explain phase plane analysis, phase trajectory construction, and classification of singular points in '
               'second-order autonomous systems.',
    'acs-q2': 'What are phase variables? Formulate the continuous-time state-space representation of an n-th order '
              'differential equation using phase variables.',
    'acs-q20': "State Sylvester's criterion for testing the positive definiteness of quadratic scalar functions V(x) = "
               'x^T P x.',
    'acs-q20b': "Explain Krasovskii's method and variable gradient method for the construction of Lyapunov functions.",
    'acs-q21': 'Construct the phase portrait and determine the singular points of a non-linear second-order system '
               'using the method of isoclines.',
    'acs-q22': "State and prove Lyapunov's direct method stability theorems for continuous-time autonomous LTI systems "
               'using the matrix equation A^T P + P A = -Q.',
    'acs-q3': 'Draw and explain the general block diagram representation of a continuous-time LTI system described by '
              'state and output equations.',
    'acs-q4': 'Show that the state space representation of a dynamic system is not unique using similarity '
              'transformations. Prove that eigenvalues remain invariant.',
    'acs-q4b': 'Derive the transfer function matrix G(s) of a continuous-time LTI system from its state-space model.',
    'acs-q5': 'Derive the state-space model of a series RLC circuit excited by an input voltage source, selecting the '
              'inductor current and capacitor voltage as state variables.',
    'acs-q6': 'Derive the electromechanical state-space model of an armature-controlled DC servomotor with necessary '
              'differential equations and block diagram.',
    'acs-q7': 'Derive the controllable canonical form and diagonal (Jordan) canonical form from a given system '
              'transfer function.',
    'acs-q7b': 'Derive the state space equations for a field-controlled DC motor and obtain its overall transfer '
               'function.',
    'acs-q8': 'Derive the solution of homogeneous (autonomous) continuous-time state equations using the Laplace '
              'transform method.',
    'acs-q9': 'Define state transition matrix. State and prove any four important properties of the state transition '
              'matrix.',
    'acs-q9b': 'Derive the pulse transfer function and discrete state transition solution for a discrete-time LTI '
               'state model with Zero-Order Hold (ZOH).',
    'beee-q1': "State and explain Kirchhoff's Current Law (KCL) and Kirchhoff's Voltage Law (KVL) with algebraic sign "
               'conventions. Explain how they form the basis of mesh and nodal analysis.',
    'beee-q10': 'Define MMF, magnetic flux, reluctance, permeance, and flux density. Compare electric and magnetic '
                'circuits in detail. Explain the B-H curve and solve a series magnetic circuit with an air gap.',
    'beee-q11': 'Explain the construction and working principle of a single-phase transformer. Derive the EMF equation '
                'and the condition for maximum efficiency.',
    'beee-q12': 'Explain the constructional details of a DC machine with a neat sketch. Explain the operating '
                'principle of a DC generator and derive the generator EMF equation.',
    'beee-q13': 'Explain the working principle of a DC motor and the physical significance of Back-EMF. Derive the DC '
                'motor armature torque equation and speed relationship.',
    'beee-q14': 'Derive the relationship between line and phase voltages and currents in balanced 3-phase Star (Y) and '
                'Delta (Δ) connected systems. Derive the expression for total 3-phase active power.',
    'beee-q15': 'Draw the schematic layout of a residential distribution board. Explain the two-way control of a lamp '
                '(staircase wiring). Explain pipe earthing and compare Fuse, MCB, and ELCB/RCCB.',
    'beee-q16': 'Distinguish between intrinsic and extrinsic semiconductors. Explain the formation of a PN junction, '
                'depletion layer, and barrier potential. Explain forward and reverse bias V-I characteristics.',
    'beee-q17': 'Explain the working of half-wave and full-wave bridge rectifiers with circuit diagrams and waveforms. '
                'Derive expressions for V_dc, V_rms, rectification efficiency, and ripple factor. Explain the role of '
                'capacitor filter.',
    'beee-q18': 'Explain the breakdown mechanisms in a PN junction: Avalanche breakdown versus Zener breakdown. '
                'Explain the operation of a Zener diode as a shunt voltage regulator with circuit diagram and design '
                'equations.',
    'beee-q19': 'Describe the physical structure and operation of an NPN Bipolar Junction Transistor. Plot and explain '
                'the Common Emitter (CE) input and output characteristics, identifying all operating regions. Derive '
                'the relationship between α and β.',
    'beee-q2': 'Explain Nodal Voltage Analysis. Explain the supernode concept when an ideal independent voltage source '
               'is connected between two non-reference nodes, and solve a numerical problem.',
    'beee-q20': 'Explain the operation of a BJT as a digital switch with operating conditions. Draw the circuit '
                'diagram of a single-stage Common Emitter (CE) voltage amplifier with voltage-divider biasing and '
                'explain its operation and 180° phase inversion.',
    'beee-q21': 'Explain the internal architectural block diagram of an operational amplifier and pinout of IC 741. '
                'List ideal op-amp characteristics and explain the concepts of Virtual Ground and Virtual Short.',
    'beee-q22': 'Derive the closed-loop voltage gain expressions for Inverting and Non-Inverting op-amp '
                'configurations. Explain the Voltage Follower (Buffer) circuit and its practical application.',
    'beee-q23': 'Explain the circuit operations and derive the output voltage expressions for an op-amp Summing '
                'Amplifier, Difference Amplifier, Integrator, and Differentiator.',
    'beee-q24': 'Explain decimal, binary, octal, and hexadecimal number systems with radix conversion examples. '
                "Explain 1's and 2's complement representations and perform binary subtraction using 2's complement "
                'with overflow rules.',
    'beee-q25': 'Explain basic and universal logic gates with symbols, Boolean expressions, and truth tables. Show how '
                "AND, OR, NOT gates are realized using only NAND gates and only NOR gates. State and prove De Morgan's "
                'laws.',
    'beee-q26': 'Design a Half Adder and a Full Adder circuit. Write their truth tables, obtain minimized Boolean '
                'expressions using K-maps, and implement a Full Adder using two Half Adders and an OR gate.',
    'beee-q3': 'State Superposition Theorem. Explain its conditions of applicability and limitations. Find the current '
               'through the load resistor in a multi-source DC network with independent voltage and current sources.',
    'beee-q4': "State Thevenin's and Norton's Theorems and derive their dual relationship. Find the Thevenin and "
               'Norton equivalent circuits across the detector terminals of an unbalanced bridge network.',
    'beee-q5': 'State and prove Maximum Power Transfer Theorem for a DC network. Derive the expression for maximum '
               'power and show that the transmission efficiency at maximum power is 50%.',
    'beee-q6': 'Explain the generation of sinusoidal alternating voltage by a coil rotating in a uniform magnetic '
               'field. Define instantaneous value, amplitude, time period, frequency, and phasor representation.',
    'beee-q7': 'Derive the mathematical expressions for the RMS value, Average value, Form Factor, and Peak Factor of '
               'a pure sinusoidal alternating voltage waveform.',
    'beee-q8': 'Derive the expressions for impedance, current, phase angle, and power in a series R-L and series R-C '
               'circuit excited by sinusoidal AC. Explain the impedance and power triangles with a numerical problem.',
    'beee-q9': 'Derive the condition and expression for resonant frequency in a series R-L-C circuit. Derive the '
               'expressions for Quality factor (Q) and half-power bandwidth (BW).',
    'comp-q1': "State and prove Thévenin's, Norton's, and the Maximum Power Transfer theorems for DC and AC circuits. "
               'Derive the complex load condition for maximum active power transfer.',
    'comp-q10': 'Explain the determination of voltage regulation of an alternator by EMF and MMF methods. Describe '
                "Blondel's two-reaction theory for salient-pole synchronous machines and derive the power-angle "
                'equation.',
    'comp-q11': 'Explain transmission line ABCD parameters and per-unit representation. Analyze symmetrical and '
                'unsymmetrical faults using symmetrical components, and derive the swing equation and equal area '
                'criterion.',
    'comp-q12': 'Define transfer function and explain mechanical-electrical analogies. State the block diagram '
                "reduction rules and Mason's gain formula with an illustrative signal flow graph example.",
    'comp-q13': 'Derive the step response of an underdamped second-order control system and formulate the time-domain '
                'specifications: rise time, peak time, peak overshoot, and settling time. Discuss steady-state error.',
    'comp-q14': 'Explain the Routh-Hurwitz stability criterion including its special cases. Formulate the '
                'comprehensive construction rules for the Root Locus technique.',
    'comp-q15': 'Explain the construction of Bode plots and the determination of gain margin and phase margin. Explain '
                "the Nyquist stability criterion using Cauchy's principle of the argument.",
    'comp-q16': "Explain state-space representation, state transition matrix, and Kalman's criteria for "
                'controllability and observability. Describe AC bridges (Maxwell-Wien, Schering) and instrument '
                'transformers.',
    'comp-q17': 'Explain the operation and performance metrics (ripple factor, efficiency, PIV) of half-wave and '
                'full-wave rectifiers with capacitor filters. Describe the design of a Zener diode voltage regulator.',
    'comp-q18': 'Explain BJT input and output characteristics in CE configuration. Derive the stability factor for a '
                'voltage divider bias circuit and conduct small-signal low-frequency amplifier analysis.',
    'comp-q19': 'List the ideal characteristics of an Op-Amp. Derive the voltage gain for inverting, non-inverting, '
                'practical integrator, and three-Op-Amp instrumentation amplifier circuits.',
    'comp-q2': 'Derive the transient current and voltage responses for series RL, RC, and series RLC circuits excited '
               'by a DC step input. Discuss overdamped, critically damped, and underdamped conditions.',
    'comp-q20': 'Draw the internal block diagram of IC 555 timer. Explain its operation as an astable and monostable '
                'multivibrator, deriving the formulas for frequency, duty cycle, and pulse duration.',
    'comp-q21': "State De Morgan's laws and K-map minimization rules. Design a Full Adder and explain multiplexers. "
                'Explain the race-around condition in JK flip-flops and design a 3-bit synchronous binary counter.',
    'comp-q22': 'Explain the static V-I characteristics and two-transistor analogy of an SCR. Compare the structure, '
                'characteristics, and switching performance of SCR, Power MOSFET, and IGBT.',
    'comp-q23': 'Derive the average DC output voltage and RMS voltage for single-phase and three-phase '
                'fully-controlled bridge rectifiers with R and RL loads. Explain inversion mode and freewheeling diode '
                'action.',
    'comp-q24': 'Explain the continuous conduction mode (CCM) operation of Buck, Boost, and Buck-Boost DC-DC '
                'converters using inductor volt-second and capacitor charge balance, deriving voltage conversion '
                'ratios.',
    'comp-q25': 'Describe single-phase and three-phase voltage source inverters operating in 180° and 120° conduction '
                'modes with phase and line waveforms. Explain Sinusoidal PWM and its harmonic benefits.',
    'comp-q26': 'Explain four-quadrant operation of electric drives. Describe converter speed control of DC motors, '
                'constant V/f speed control of induction motors, and electrical braking methods.',
    'comp-q3': 'Derive the resonant frequency, half-power bandwidth, and Quality factor for a series RLC circuit. '
               'Explain parallel resonance in a practical tank circuit and derive its dynamic impedance.',
    'comp-q4': 'Derive the relationships between line and phase voltages and currents in balanced Star and Delta AC '
               'systems. Explain the two-wattmeter method of 3-phase power measurement and derive the power factor '
               'formula.',
    'comp-q5': "State and explain Maxwell's four equations in differential and integral forms. Derive the "
               "electromagnetic wave equation in a lossless medium and state Poynting's theorem.",
    'comp-q6': 'Derive the generated EMF and torque equations of a DC machine. Explain armature reaction, commutation, '
               'methods of improving commutation, and speed control techniques for DC motors.',
    'comp-q7': "Explain the testing of DC machines using Swinburne's test and Hopkinson's regenerative test. Derive "
               'the equations for predetermining motor and generator efficiency.',
    'comp-q8': 'Draw the exact and approximate equivalent circuits of a single-phase transformer. Derive the voltage '
               'regulation expression and explain OC/SC tests and autotransformer copper saving.',
    'comp-q9': 'Prove mathematically that a balanced 3-phase stator winding produces a rotating magnetic field of '
               'constant magnitude. Derive the torque-slip equation and discuss starting methods of induction motors.',
    'cprog-q1': 'Explain the fundamental structure of a C program. Describe the multi-stage compilation and execution '
                'process from source code to executable binary.',
    'cprog-q10': 'Explain two-dimensional character arrays (array of strings). Write a complete C program to sort a '
                 'list of student names alphabetically using bubble sort.',
    'cprog-q11': 'Explain modular programming in C. Differentiate between Call by Value and Call by Reference '
                 'parameter passing with memory stack diagrams and swapping examples.',
    'cprog-q12': 'Explain recursion in C. Detail the role of base conditions and call stack frames. Provide a '
                 'recursive solution and call tree for the Tower of Hanoi problem.',
    'cprog-q13': 'Explain storage classes in C: auto, register, static, and extern. Compare them in terms of storage '
                 'area, default initial value, scope, and lifetime.',
    'cprog-q14': 'Explain the concept of pointers in C. Discuss pointer arithmetic, array-pointer equivalence, void '
                 'pointers, and dangling pointers with illustrative examples.',
    'cprog-q15': 'Explain dynamic memory allocation in C. Differentiate between malloc, calloc, realloc, and free, and '
                 'write a program demonstrating dynamic array creation and resizing.',
    'cprog-q16': 'Define structures in C. Explain memory allocation for structures and mathematically derive structure '
                 'padding and word alignment on 32-bit and 64-bit architectures.',
    'cprog-q17': 'Explain arrays of structures and nested structures. Discuss passing structure pointers to functions '
                 'and the use of the arrow operator (->).',
    'cprog-q18': 'What is a self-referential structure? Explain how self-referential structures are utilized in linked '
                 'lists, and write a program to insert and traverse nodes.',
    'cprog-q19': 'Compare structures and unions in terms of memory allocation and size calculation. Explain the '
                 'concept of bit-fields in structures for compact memory packing.',
    'cprog-q2': 'Explain the primitive data types in C with size, range, and format specifiers. Discuss type '
                'modifiers, type qualifiers, and implicit vs explicit type conversion.',
    'cprog-q20': 'Explain typedef and enumerations (enum). Describe C preprocessor directives including #define '
                 'macros, file inclusion, and conditional compilation with header guards.',
    'cprog-q21': 'Explain file handling basics in C. Discuss the FILE pointer, fopen(), fclose(), standard file access '
                 'modes (r, w, a, r+, w+, a+), and text vs binary files.',
    'cprog-q22': 'Explain character, line, and formatted file I/O functions. Write a complete C program to copy a text '
                 'file and count the total characters, words, and lines.',
    'cprog-q23': 'Explain block-level binary file I/O using fread() and fwrite(). Write a C program to store and read '
                 'an array of employee structure records to/from a binary disk file.',
    'cprog-q24': 'Explain random access in files using fseek(), ftell(), and rewind(). Discuss SEEK_SET, SEEK_CUR, and '
                 'SEEK_END, and show how to determine file size.',
    'cprog-q25': 'Explain error handling in file operations in C. Discuss feof(), ferror(), clearerr(), perror(), and '
                 'strerror() with a diagnostic code example.',
    'cprog-q26': 'Explain command line arguments in C with argc and argv. Write a complete C program implementing a '
                 'command-line file copy utility.',
    'cprog-q3': 'Classify operators in C. Explain arithmetic, relational, logical, and bitwise operators with operator '
                'precedence and associativity rules.',
    'cprog-q4': 'Explain formatted input and output functions printf() and scanf() with format specifiers, field '
                'width, precision, and escape sequences.',
    'cprog-q5': 'Discuss decision-making and looping structures in C. Compare while and do-while loops, and write a '
                'menu-driven program for prime number checking and factorial calculation.',
    'cprog-q6': 'Explain one-dimensional arrays and memory address allocation. Implement and compare linear search and '
                'binary search algorithms with step-by-step traces.',
    'cprog-q7': 'Derive the row-major memory address formula for a two-dimensional array. Write a complete C program '
                'to perform matrix multiplication with dimensional verification.',
    'cprog-q8': 'Explain how strings are represented in C. Differentiate between character arrays and string literals, '
                'and discuss string I/O using scanf, gets, and fgets.',
    'cprog-q9': 'Explain standard library string manipulation functions in <string.h>. Provide manual C '
                'implementations of strlen, strcpy, strcat, and strcmp without library routines.',
    'drive-q1': 'Draw the block diagram of a modern electric drive system and explain the functions of each '
                'constituent component.',
    'drive-q10': 'Explain the operation of a two-quadrant Class-C chopper fed DC motor drive for motoring and '
                 'regenerative braking modes.',
    'drive-q10b': 'Explain the four-quadrant operation of a DC motor drive using a Class-E H-bridge chopper.',
    'drive-q11': 'Draw and explain the closed-loop speed control scheme of a DC motor drive with inner current control '
                 'loop and anti-windup controller.',
    'drive-q12': 'Discuss the limitations and practical application boundaries of stator voltage control method in '
                 'three-phase induction motor drives.',
    'drive-q12b': 'Compare Voltage Source Inverter (VSI) and Current Source Inverter (CSI) fed induction motor drives.',
    'drive-q13': 'Explain the principle and complete mathematical theory of constant V/f speed control of a '
                 'three-phase induction motor drive.',
    'drive-q14': 'Explain static rotor resistance control of a wound-rotor induction motor using a diode bridge '
                 'rectifier and chopper.',
    'drive-q14b': 'Explain the working principle of slip power recovery schemes. Compare Static Kramer drive with '
                  'Static Scherbius drive.',
    'drive-q15': 'Distinguish between true synchronous mode and self-controlled mode of inverter-fed synchronous motor '
                 'drives.',
    'drive-q15b': 'Explain the operation of a Load-Commutated Inverter (LCI) fed synchronous motor drive at leading '
                  'power factor.',
    'drive-q16': 'Derive Clarke and Park coordinate reference frame transformations from three-phase stationary '
                 '(a-b-c) to rotating (d-q) reference frame.',
    'drive-q17': 'Explain the principle of Space Vector Pulse Width Modulation (SVPWM). Derive sector dwell times and '
                 'explain switching sequence.',
    'drive-q18': 'Explain the principle of Field-Oriented Control (Vector Control) of a three-phase induction motor '
                 'drive with block diagram.',
    'drive-q2': 'State and explain the major advantages of electric drives over conventional mechanical and thermal '
                'drive systems in industrial motion control.',
    'drive-q3': 'Classify industrial load torques with suitable mathematical expressions and torque-speed '
                'characteristics.',
    'drive-q3b': 'Explain the concept of critical speed and torsional resonance in electric drive shaft couplings.',
    'drive-q4': 'Derive the fundamental dynamic torque equation governing the rotational motion of an electric motor '
                'driving a mechanical load.',
    'drive-q5': 'Explain with neat torque-speed diagrams the four-quadrant operation of an electric motor driving a '
                'hoist load.',
    'drive-q6': 'Derive the mathematical condition for the steady-state stability of an electric drive operating '
                'point.',
    'drive-q6b': 'Explain the thermal heating and cooling dynamics of an electric motor and discuss the determination '
                 'of motor power rating for continuous and intermittent loads.',
    'drive-q7': 'Compare armature voltage control and field weakening speed control methods of a DC separately excited '
                'motor drive with torque-power capabilities.',
    'drive-q7b': 'Explain the operation of a three-phase semi-converter fed DC motor drive. Why is regenerative '
                 'braking not possible in semi-converter drives?',
    'drive-q8': 'Explain the operation of a single-phase fully controlled rectifier fed separately excited DC motor '
                'drive and derive the speed-torque relationship for continuous conduction.',
    'drive-q8b': 'Explain the operation of a three-phase full converter fed DC drive and compare its performance with '
                 'a single-phase converter drive.',
    'drive-q9': 'Explain the speed control of a separately excited DC motor using a Class-A step-down chopper with '
                'neat circuit and waveform diagrams.',
    'drive-q9b': 'Explain the regenerative braking control of a DC motor using a Class-B step-up chopper with circuit '
                 'and waveform analysis.',
    'lac-q1': 'State the conditions for consistency of a non-homogeneous system of linear equations AX = B in terms of '
              'ranks of the coefficient matrix and the augmented matrix using the Rouché-Capelli theorem. Explain when '
              'the system has a unique solution, infinitely many solutions, and no solution.',
    'lac-q10': 'Orthogonally diagonalise the symmetric matrix A = [[6, -2, 2], [-2, 3, -1], [2, -1, 3]]. Hence reduce '
               'the quadratic form Q = 6x^2 + 3y^2 + 3z^2 - 4xy + 4xz - 2yz into canonical form and determine its '
               'rank, index, signature, and nature.',
    'lac-q11': "Evaluate the limit lim_{x->0} (x - sin x) / x^3 using L'Hopital's rule, and verify the result using "
               'Maclaurin series expansion.',
    'lac-q12': 'Determine the intervals of concavity, convexity, and points of inflection for the function f(x) = x^4 '
               '- 4x^3 + 10.',
    'lac-q13': 'Evaluate the indeterminate forms: (i) lim_{x->0+} (cot x)^(sin x) (form infinity^0), and (ii) '
               'lim_{x->0} (1/x^2 - cot x / x) (form infinity - infinity).',
    'lac-q14': 'Find the Taylor series expansion of f(x) = ln(cos x) about x = 0 up to the term containing x^4 and '
               'deduce an approximation for ln(cos 0.1).',
    'lac-q15': 'Find the Maclaurin series expansion of f(x) = e^x cos x up to the term in x^4. Hence determine '
               'f^(4)(0) and calculate an approximate value for e^(0.1) cos(0.1).',
    'lac-q16': "State Euler's theorem on homogeneous functions. If u = sin^(-1)((x^2 + y^2)/(x + y)), prove that x "
               'du/dx + y du/dy = tan u.',
    'lac-q17': 'If z = f(x, y) where x = r cos theta and y = r sin theta, show that (dz/dx)^2 + (dz/dy)^2 = (dz/dr)^2 '
               '+ (1/r^2)(dz/d theta)^2.',
    'lac-q18': 'If u = tan^(-1)((x^3 + y^3)/(x - y)), prove that: (i) x du/dx + y du/dy = sin 2u, and (ii) x^2 '
               'd^2u/dx^2 + 2xy d^2u/dxdy + y^2 d^2u/dy^2 = 2 cos 3u sin u.',
    'lac-q19': 'Find all local maxima, local minima, and saddle points of the multivariable function f(x, y) = x^3 + '
               '3xy^2 - 15x^2 - 15y^2 + 72x.',
    'lac-q2': 'Define row echelon form of a matrix. Reduce the matrix A = [[1, 2, -1, 3], [2, 4, 1, -2], [3, 6, 3, '
              '-7]] to row echelon form and determine its rank.',
    'lac-q20': 'Find the maximum volume of a rectangular parallelepiped inscribed in the ellipsoid x^2/a^2 + y^2/b^2 + '
               "z^2/c^2 = 1 using Lagrange's method of undetermined multipliers.",
    'lac-q21': 'Evaluate the double integral int_0^1 int_0^(sqrt(1-x^2)) (x^2 + y^2) dy dx by transforming into polar '
               'coordinates.',
    'lac-q22': 'Change the order of integration in int_0^1 int_x^(sqrt(x)) f(x, y) dy dx.',
    'lac-q23': 'Evaluate the improper double integral int_0^infinity int_0^infinity e^(-(x^2 + y^2)) dx dy by '
               'transforming into polar coordinates, and hence deduce the value of the Gaussian integral '
               'int_0^infinity e^(-x^2) dx = sqrt(pi)/2.',
    'lac-q24': 'Change the order of integration and evaluate: int_0^a int_y^a x / (x^2 + y^2) dx dy.',
    'lac-q25': 'Find the area bounded by the parabolas y^2 = 4ax and x^2 = 4ay using double integration.',
    'lac-q26': 'Find the volume of the solid bounded by the cylinder x^2 + y^2 = 4 and the planes y + z = 4 and z = 0 '
               'using triple integration.',
    'lac-q3': 'Investigate for what values of lambda and mu the system of equations x + y + z = 6, x + 2y + 3z = 10, x '
              '+ 2y + lambda*z = mu has: (i) no solution, (ii) a unique solution, and (iii) infinitely many solutions. '
              'Also find the solutions when lambda = 4, mu = 13 and when lambda = 3, mu = 10.',
    'lac-q4': 'Test for consistency and solve the system of linear equations using Gauss elimination: x1 - 2x2 + x3 - '
              '4x4 = 1, x1 + 3x2 + 7x3 + 2x4 = 2, x1 - 12x2 - 11x3 - 16x4 = -1.',
    'lac-q5': 'Find the non-trivial solutions of the homogeneous system of equations: x + 2y + 3z = 0, 3x + 4y + 4z = '
              '0, 7x + 10y + 12z = 0. Determine the basis and dimension (nullity) of the solution space.',
    'lac-q6': 'State Cayley-Hamilton theorem. Use it to find A^(-1) and A^3 for the matrix A = [[1, 2], [3, 4]].',
    'lac-q7': 'Find the eigenvalues and eigenvectors of the matrix A = [[3, 1], [1, 3]] and verify that the '
              'eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.',
    'lac-q8': 'Find the eigenvalues and eigenvectors of the 3x3 matrix A = [[2, 2, 1], [1, 3, 1], [1, 2, 2]]. Verify '
              'that the sum of the eigenvalues equals the trace of A and the product of the eigenvalues equals the '
              'determinant of A.',
    'lac-q9': 'Verify Cayley-Hamilton theorem for the matrix A = [[1, 0, 3], [2, 1, -1], [1, -1, 1]] and hence compute '
              'A^(-1) and A^4.',
    'lcs-q1': 'Compare open loop and closed loop control systems. Derive the expressions for the sensitivity of '
              'closed-loop system transfer function with respect to forward path gain G(s) and feedback path gain '
              'H(s).',
    'lcs-q10': 'Explain the characteristics and operating principles of P, PI, PD, and PID controllers. Discuss their '
               'effects on steady-state error, damping, stability, and transient response.',
    'lcs-q11': 'Explain the concept of BIBO stability in linear systems. State the necessary and sufficient condition '
               'for stability based on impulse response and discuss the relation between s-plane pole locations and '
               'stability.',
    'lcs-q12': 'State the Routh-Hurwitz stability criterion. Explain how Special Case 1 (first element in a row is '
               'zero while others are non-zero) is resolved using the epsilon method with a complete worked example.',
    'lcs-q13': 'Explain Special Case 2 of the Routh array when an entire row becomes zero. Describe the construction '
               'of the auxiliary polynomial and determine the range of gain K and frequency of sustained oscillations '
               'for a fourth-order system.',
    'lcs-q14': 'Explain the angle and magnitude conditions of the Root Locus technique. State and explain the eight '
               'essential procedural rules for the construction of a complete root locus diagram.',
    'lcs-q15': 'Sketch the root locus for a unity feedback control system with open loop transfer function G(s) = K / '
               '[s(s+2)(s+4)]. Calculate centroid, asymptotes, breakaway points, imaginary axis crossings, and range '
               'of K for stability.',
    'lcs-q16': 'Define the frequency domain specifications: resonant peak (Mr), resonant frequency (wr), and bandwidth '
               '(wb) for a second-order system. Derive their expressions and correlate them with time-domain '
               'specifications.',
    'lcs-q17': 'Explain the construction of Bode magnitude and phase plots. Describe the asymptotic magnitude slopes '
               'and corner frequency characteristics for standard transfer function factors.',
    'lcs-q18': 'Define Gain Crossover Frequency, Phase Crossover Frequency, Gain Margin, and Phase Margin from Bode '
               'plots. State the criteria for closed-loop stability and solve a complete numerical problem.',
    'lcs-q19': 'Explain the construction of polar plots for Type 0, Type 1, and Type 2 systems. Discuss how the '
               'addition of open-loop poles and zeros affects the shape and stability of the polar plot locus.',
    'lcs-q2': 'Explain Force-Voltage and Force-Current analogies for translational mechanical systems. Formulate the '
              'governing differential equations and provide the comprehensive analogy conversion table.',
    'lcs-q20': "State and prove the Nyquist stability criterion using Cauchy's principle of the argument. Explain the "
               'mapping of the Nyquist contour and analyze the closed-loop stability of an open-loop unstable system.',
    'lcs-q21': 'Explain the circuits, transfer functions, and pole-zero patterns of phase lead, phase lag, and '
               'lead-lag compensator networks. Derive the maximum phase lead angle phi_m and frequency omega_m for a '
               'lead network.',
    'lcs-q22': 'Explain the step-by-step design procedure of a Phase Lead Compensator using frequency response (Bode '
               'plot) to satisfy specified phase margin and velocity error constant specifications.',
    'lcs-q23': 'Explain the step-by-step design procedure of a Phase Lag Compensator using Bode plots to improve '
               'steady-state error performance without degrading existing phase margin.',
    'lcs-q24': 'Explain the state-space representation of continuous-time LTI systems. Define state, state variables, '
               'state vector, and state equations, and state the major advantages of state space analysis over '
               'transfer functions.',
    'lcs-q25': 'Derive the closed-loop transfer function matrix G(s) = C(sI - A)^{-1}B + D from state space equations. '
               'Prove that the poles of G(s) are the eigenvalues of state matrix A and solve a numerical problem.',
    'lcs-q26': 'Define the state transition matrix Phi(t) = e^{At}. State and prove four important properties of the '
               'state transition matrix and calculate e^{At} for a given 2x2 system matrix using the Laplace transform '
               'method.',
    'lcs-q3': 'Derive the mathematical model and the transfer functions X1(s)/F(s) and X2(s)/F(s) for a two-mass '
              'translational mechanical system with springs, dampers, and an external driving force applied to mass '
              'M1.',
    'lcs-q4': 'State the fundamental rules of block diagram algebra. Step-by-step, reduce a multi-loop control system '
              'block diagram with multiple feedback paths to obtain its overall closed-loop transfer function '
              'C(s)/R(s).',
    'lcs-q5': "Define the terms related to Signal Flow Graphs and state Mason's Gain Formula. Using Mason's formula, "
              'determine the overall transfer function C(s)/R(s) of a given multi-loop control system.',
    'lcs-q6': 'Define standard test signals used in control system analysis with their mathematical expressions. '
              'Derive the response of a first-order system to a unit step input and explain the significance of time '
              'constant.',
    'lcs-q7': 'Derive the mathematical expression for the unit step response of an underdamped second-order control '
              'system in the time domain.',
    'lcs-q8': 'Derive the mathematical formulas for time domain specifications of a second-order underdamped system: '
              'delay time (td), rise time (tr), peak time (tp), maximum percent overshoot (Mp), and settling time '
              '(ts).',
    'lcs-q9': 'Define steady-state error and derive its expression using the final value theorem. Define static error '
              'constants (Kp, Kv, Ka) and tabulate steady-state errors for Type 0, Type 1, and Type 2 systems.',
    'mech-q1': 'State the Parallelogram Law of Forces and the Principle of Transmissibility of Forces. Explain the '
               'analytical method of resolving a system of coplanar concurrent forces to find the resultant and state '
               'the conditions of static equilibrium.',
    'mech-q10': 'State the assumptions in the analysis of pin-jointed trusses. State the conditions for a truss to be '
                'perfect, deficient, or redundant. State the rules for identifying zero-force members by inspection '
                'and explain the Method of Joints and Method of Sections.',
    'mech-q11': 'Define the first moment of area and centroid of a composite plane area. Derive the centroid formulas '
                'and determine the centroid coordinates of an unsymmetrical T-section.',
    'mech-q12': 'State and prove Pappus-Guldinus Theorem 1 (Surface Area of Revolution) and Theorem 2 (Volume of '
                'Revolution). Use these theorems to calculate the surface area and volume of a sphere and a right '
                'circular cone.',
    'mech-q13': 'Define area moment of inertia, polar moment of inertia, and radius of gyration. State and prove the '
                "Parallel Axis Theorem (Steiner's Theorem) and the Perpendicular Axis Theorem for area moment of "
                'inertia.',
    'mech-q14': 'Determine the centroidal moments of inertia Ixx and Iyy and the radii of gyration kxx and kyy for an '
                'unsymmetrical I-section with given flange and web dimensions.',
    'mech-q15': 'Define mass moment of inertia and radius of gyration. Derive the mass moment of inertia of a uniform '
                'slender rod of mass m and length L about its centroidal transverse axis and one end, and of a thin '
                'circular disc about its polar and diameter axes.',
    'mech-q16': 'Formulate the kinematic equations for rectilinear motion with variable acceleration. Solve the '
                'equation of motion for a particle subjected to a resisting drag force proportional to velocity (a = '
                '-kv) and determine the velocity, displacement, and total distance traveled.',
    'mech-q17': 'Derive the parabolic trajectory equation for an unresisted projectile launched with initial velocity '
                'u at angle theta. Derive expressions for the time of flight, maximum vertical height, and horizontal '
                'range, and obtain the condition for maximum range.',
    'mech-q18': 'Derive the expressions for the normal and tangential components of acceleration for a particle '
                'executing curvilinear planar motion. Explain the physical significance of each component.',
    'mech-q19': "State Newton's Second Law of Motion and D'Alembert's Principle of dynamic equilibrium. Apply "
                "D'Alembert's principle to analyze the apparent weight in an accelerating elevator and determine the "
                'acceleration and cord tension in an Atwood machine.',
    'mech-q2': "State and prove Lami's Theorem using the sine rule on a force triangle. Apply Lami's theorem to find "
               'the cord tension and wall reaction for a smooth sphere of weight W suspended against a vertical wall.',
    'mech-q20': 'Formulate the equations of dynamic motion for two connected bodies where one body moves along a rough '
                'inclined plane and is connected by a cord over a pulley to a hanging body. Derive expressions for the '
                'common acceleration and cord tension.',
    'mech-q21': 'Define work done by a force and derive expressions for work done by gravity and spring forces. Derive '
                'the Work-Energy Theorem for a particle moving under a variable force.',
    'mech-q22': 'Define a conservative force and state its criteria. Define potential energy and prove the Law of '
                'Conservation of Mechanical Energy. Apply it to find the velocity of an oscillating simple pendulum.',
    'mech-q23': "State and derive the Linear Impulse-Momentum Principle from Newton's second law. Explain impulsive "
                'forces and derive the dynamic force exerted by a high-velocity fluid jet striking a curved vane.',
    'mech-q24': 'State and prove the Principle of Conservation of Linear Momentum for a system of interacting '
                'particles. Apply the principle to determine the recoil velocity of an artillery gun firing a shell.',
    'mech-q25': 'Define direct central impact and coefficient of restitution. Derive expressions for the '
                'post-collision velocities v1 and v2 of two colliding bodies in terms of their masses, initial '
                'velocities, and coefficient of restitution.',
    'mech-q26': 'Derive the complete mathematical expression for the loss of kinetic energy during direct central '
                'inelastic impact of two bodies: Delta E = (m1*m2)/(2*(m1+m2)) * (1 - e^2) * (u1 - u2)^2. Discuss '
                'perfectly elastic, inelastic, and plastic collisions.',
    'mech-q3': 'What is a Free Body Diagram (FBD)? Explain the steps to construct an FBD. Two smooth identical '
               'cylinders of weight W and radius R rest in a rectangular channel of width L. Determine all contact '
               'reactions.',
    'mech-q4': "State and prove Varignon's Theorem of Moments for a system of coplanar concurrent forces. Define a "
               'couple, list its characteristics, and explain how a force can be replaced by an equivalent '
               'force-couple system.',
    'mech-q5': 'State the equations of static equilibrium of a rigid body in two dimensions. Classify common '
               'structural supports and determine the support reactions for a simply supported beam carrying a UDL, '
               'inclined point load, and concentrated couple.',
    'mech-q6': "State Coulomb's laws of dry friction. Define the terms: static friction, limiting friction, kinetic "
               'friction, angle of friction, angle of repose, and cone of friction. Prove that the angle of repose is '
               'equal to the angle of friction.',
    'mech-q7': 'A uniform ladder of length L and weight W rests against a rough vertical wall and a rough horizontal '
               'floor. Formulate the equilibrium equations, derive the expression for the minimum inclination angle to '
               'prevent slipping, and determine the maximum distance a person can climb.',
    'mech-q8': 'Explain the working principle of a wedge for raising heavy loads. Draw the free body diagrams of the '
               'block and wedge system and derive the formula for the minimum horizontal driving force P required to '
               'raise the load.',
    'mech-q9': 'Derive the formula for the ratio of belt tensions T1/T2 = e^(mu*theta) for a flat belt passing over a '
               'fixed cylindrical pulley. Obtain the expression for the power transmitted by the belt and discuss the '
               'effect of centrifugal tension.',
    'mgt-q1': 'Explain the principles and techniques of Scientific Management propounded by F.W. Taylor. What is meant '
              'by mental revolution?',
    'mgt-q10': 'Explain the procedure of stopwatch time study. Derive the relationship between Observed Time, Normal '
               'Time, Allowances, and Standard Time with a numerical example.',
    'mgt-q11': "Define Economic Order Quantity (EOQ). Mathematically derive Wilson's lot size formula from the total "
               'annual inventory cost equation and sketch the cost curves.',
    'mgt-q12': "Explain selective inventory control techniques: ABC analysis based on Pareto's 80/20 rule, VED "
               'analysis, FSN analysis, and SDE analysis.',
    'mgt-q13': "Explain the Just-In-Time (JIT) manufacturing philosophy, Taiichi Ohno's seven wastes (Muda), the "
               'dual-card Kanban pull mechanism, and compare JIT with traditional MRP.',
    'mgt-q14': "Explain Total Quality Management (TQM), Deming's 14 points, and the PDCA cycle. Describe the Six Sigma "
               'DMAIC methodology and ISO 9001 standards.',
    'mgt-q15': 'Explain Statistical Quality Control (SQC). Distinguish between variable control charts (X-bar & R) and '
               'attribute control charts (p & c). Derive Process Capability indices Cp and Cpk.',
    'mgt-q16': 'Explain the core concepts of marketing management, the 4 Ps and 7 Ps marketing mix, and the STP '
               '(Segmentation, Targeting, Positioning) strategic framework.',
    'mgt-q17': 'Explain the Product Life Cycle (PLC) concept. Describe the sales, profit, competition, and marketing '
               'strategy characteristics across all four stages.',
    'mgt-q18': 'Explain the functions of Human Resource Management (HRM): Human resource planning, internal vs '
               'external recruitment, scientific selection funnel, and training methods.',
    'mgt-q19': 'Distinguish between Job Description and Job Specification. Explain contemporary performance appraisal '
               'methods: 360-Degree Feedback and Management by Objectives (MBO).',
    'mgt-q2': "State and explain Henri Fayol's 14 principles of administrative management. Explain the concept of the "
              'Scalar Chain and Gangplank.',
    'mgt-q20': "Compare the motivation theories in engineering management: Maslow's Hierarchy of Needs, Herzberg's "
               "Two-Factor Theory, and McGregor's Theory X and Theory Y.",
    'mgt-q21': 'Explain the scope of financial management. Compare profit maximization and wealth maximization. '
               'Describe sources of long-term and short-term capital and financial statements.',
    'mgt-q22': 'Derive the mathematical expressions for Break-Even Point (BEP in units and revenue), P/V Ratio, and '
               'Margin of Safety. Illustrate with a break-even chart and numerical example.',
    'mgt-q23': 'Explain capital budgeting evaluation techniques: Payback Period, ARR, NPV, IRR, and Profitability '
               'Index. Compare two mutually exclusive projects using a step-by-step numerical.',
    'mgt-q24': 'Explain project network construction rules in CPM. Detail the forward pass, backward pass, float '
               'calculations (total, free, independent), and identification of the critical path.',
    'mgt-q25': 'Explain the PERT technique. Derive the expected activity duration and variance using the Beta '
               'distribution, and determine the probability of project completion within target date.',
    'mgt-q26': 'Explain the concept of project crashing and time-cost trade-offs. Derive the cost slope formula and '
               'outline the step-by-step algorithm to optimize total project cost.',
    'mgt-q3': 'Explain the universal functions of management (POSDCORB). Describe the steps involved in a rational '
              'managerial decision-making process under certainty, risk, and uncertainty.',
    'mgt-q4': 'Compare Line, Functional, Line & Staff, and Matrix organizational structures with neat organizational '
              'charts, highlighting advantages and limitations.',
    'mgt-q5': "Explain Corporate Social Responsibility (CSR) with reference to Archie Carroll's pyramid of CSR. "
              'Discuss core engineering ethics principles and whistleblowing.',
    'mgt-q6': 'Discuss the primary and secondary factors influencing plant location decisions. Explain the Factor '
              "Rating method and Weber's Industrial Location Theory.",
    'mgt-q7': 'Classify plant layouts into Product, Process, Fixed-Position, and Cellular layouts. Compare their '
              'characteristics, material handling requirements, and suitability.',
    'mgt-q8': 'Define Work Study. Explain the relationship between Method Study and Work Measurement, and detail the '
              'systematic steps in conducting a method study.',
    'mgt-q9': 'Describe the recording techniques used in method study: Operation Process Chart, Flow Process Chart, '
              'String Diagram, Multiple Activity Chart, and SIMO Chart with Therbligs.',
    'mobile-q1': 'Explain the functions of middleware components and gateways in mobile computing systems.',
    'mobile-q10': 'Provide a comparative analysis of GEO, LEO, and MEO satellite systems in mobile communications.',
    'mobile-q11': 'Explain the significance and format of mobile station identifiers: IMEI, IMSI, MSISDN, and TMSI.',
    'mobile-q12': 'Explain call progress indication mechanisms and signaling protocols in cellular telephony.',
    'mobile-q13': 'Explain multiple access techniques: FDMA, TDMA, CDMA, and SDMA with mathematical principles and '
                  'comparative characteristics.',
    'mobile-q14': 'Draw and explain the comprehensive architecture of the Global System for Mobile Communications '
                  '(GSM) and its network databases.',
    'mobile-q15': 'Explain Mobile Terminated Call (MTC) and Mobile Originated Call (MOC) routing in GSM. Distinguish '
                  'between handover and roaming.',
    'mobile-q16': 'Draw and explain the Interactive Voice Response (IVR) architecture and call flow for a telephone '
                  'banking or theatre ticket booking system.',
    'mobile-q17': 'Explain GSM security architecture. Describe the mathematical operations of authentication algorithm '
                  'A3, cipher key generation A8, and encryption algorithm A5.',
    'mobile-q18': 'Explain the architectural distinctiveness and technical strengths of Short Message Service (SMS) '
                  'over cellular signaling channels.',
    'mobile-q19': 'Discuss the architectural limitations and throughput bottlenecks of General Packet Radio Service '
                  '(GPRS).',
    'mobile-q2': 'Explain the role of the Internet as the ubiquitous backbone network in mobile computing and discuss '
                 'Mobile IP tunneling.',
    'mobile-q20': 'Explain the billing and charging mechanisms in GPRS based on data volume, duration, QoS, and '
                  'Charging Data Records (CDRs).',
    'mobile-q21': 'Explain the end-to-end architecture and message delivery mechanism of SMS (SM-MT and SM-MO) and '
                  'discuss location-based SMS services.',
    'mobile-q22': 'Explain the comprehensive architecture, protocol stack, and packet routing operations of GPRS '
                  'including SGSN, GGSN, and PDP context activation.',
    'mobile-q23': 'Explain the Quality of Service (QoS) parameters, classes, and profiles defined in GPRS and packet '
                  'data networks.',
    'mobile-q24': 'Compare IEEE 802.11 WLAN Infrastructure Basic Service Set (BSS) mode with Independent Basic Service '
                  'Set (IBSS / Ad-hoc) mode.',
    'mobile-q25': 'Explain the four Interframe Spaces (IFS) in IEEE 802.11 MAC: SIFS, PIFS, DIFS, and EIFS, and their '
                  'role in medium access priority.',
    'mobile-q26': 'Provide a comprehensive comparative technical analysis between Wi-Fi (IEEE 802.11) and 3G/Cellular '
                  'wireless networks.',
    'mobile-q27': 'Explain the hidden terminal and exposed terminal problems in wireless networks. How does RTS/CTS '
                  'handshaking resolve the hidden terminal issue?',
    'mobile-q28': 'Draw and explain the comprehensive architecture and operational advantages of Wireless Local Loop '
                  '(WLL).',
    'mobile-q29': 'Trace the security evolution in IEEE 802.11 WLANs: discuss WEP vulnerabilities, WPA (TKIP), WPA2 '
                  '(AES-CCMP), and 802.1X authentication.',
    'mobile-q3': 'Explain network segmentation in mobile communication architectures: access network, edge network, '
                 'and core network.',
    'mobile-q30': 'Explain HIPERLAN communication models. Compare HIPERLAN/1 (EY-NPMA) with HIPERLAN/2 (centralized '
                  'TDMA/TDD).',
    'mobile-q31': 'Explain the foundational pillars of information security: extended CIA triad, authenticity, '
                  'non-repudiation, and authorization in mobile systems.',
    'mobile-q32': 'Classify and explain security attacks in mobile computing into static and dynamic attacks on mobile '
                  'assets.',
    'mobile-q33': 'Explain SSL/TLS protocol architecture and discuss its adaptation in mobile networks including WTLS '
                  'and Mobile VPNs.',
    'mobile-q34': 'Explain the RSA public-key cryptosystem. Solve a complete step-by-step numerical problem for key '
                  'generation, encryption, and decryption.',
    'mobile-q35': 'Derive the Diffie-Hellman key exchange algorithm. Explain the discrete logarithm problem and '
                  'discuss vulnerability to Man-in-the-Middle attack.',
    'mobile-q36': 'Explain the mathematical principle of Orthogonal Frequency Division Multiplexing (OFDM). Discuss '
                  'subcarrier orthogonality and Cyclic Prefix (CP).',
    'mobile-q37': 'Explain Multimedia Broadcast and Multicast Services (MBMS) in cellular networks and discuss MPLS '
                  'label switching in mobile core backbones.',
    'mobile-q38': 'Compare the architectural and functional evolution of cellular mobile communication networks from '
                  '2G to 5G.',
    'mobile-q4': 'Discuss the intrinsic physical and technical limitations of mobile computing environments.',
    'mobile-q5': 'Explain the comprehensive three-tier architecture of mobile computing systems with a neat '
                 'architectural diagram.',
    'mobile-q6': 'Discuss the key architectural and software design considerations for developing mobile computing '
                 'systems.',
    'mobile-q7': 'Explain context-aware system management in mobile computing covering client context, policy, '
                 'security, and adaptability managers.',
    'mobile-q8': 'What is content adaptation? Classify and explain syntactic, structural, and semantic transcoding in '
                 'mobile systems.',
    'mobile-q9': 'What is seamless communication? Discuss the essential facets that must be maintained during seamless '
                 'mobile roaming and handoff.',
    'pe-q1': 'Explain the physical construction and static V-I characteristics of a Silicon Controlled Rectifier '
             '(SCR). Derive the mathematical expression for anode current using the two-transistor analogy.',
    'pe-q10': 'Explain the effect of AC source inductance on the performance of single-phase and three-phase full '
              'converters. Derive expressions for overlap angle (mu) and average voltage drop.',
    'pe-q11': 'Analyze the step-down (Buck) converter in continuous conduction mode. Derive the voltage transfer '
              'ratio, peak-to-peak inductor ripple current, output ripple voltage, and critical inductance.',
    'pe-q12': 'Explain the operation of a step-up (Boost) converter in continuous conduction mode. Derive the voltage '
              'gain using inductor volt-second balance, and calculate the critical inductance for CCM.',
    'pe-q13': 'Derive the voltage transfer ratio of an inverting Buck-Boost converter in continuous conduction mode. '
              'Derive expressions for inductor ripple current and critical boundary inductance.',
    'pe-q14': 'Explain the circuit topology and working principle of a Cuk converter. Derive the voltage ratio and '
              'explain why both input and output currents are continuous.',
    'pe-q15': 'Classify DC choppers into Class A, B, C, D, and E based on their quadrant of operation. Draw the '
              'circuit diagram and explain the four-quadrant operation of a full H-bridge chopper.',
    'pe-q16': 'Explain the operation of single-phase half-bridge and full-bridge Voltage Source Inverters (VSI) with R '
              'and RL loads. Derive the Fourier series expression for output voltage and discuss feedback diodes.',
    'pe-q17': 'Explain the 180-degree conduction mode of a three-phase Voltage Source Inverter with a star-connected '
              'balanced load. Derive expressions for line and phase voltages and show Fourier harmonic elimination.',
    'pe-q18': 'Analyze the 120-degree conduction mode of a three-phase Voltage Source Inverter. Derive expressions for '
              'RMS line and phase voltages and compare performance with the 180-degree conduction mode.',
    'pe-q19': 'Explain Pulse Width Modulation (PWM) techniques used in inverters: Single-Pulse, Multi-Pulse, and '
              'Sinusoidal PWM (SPWM). Define modulation index (ma) and frequency ratio (mf) with harmonic spectra.',
    'pe-q2': 'Describe the various turn-on methods for an SCR. Explain the gate characteristics, safe triggering area, '
             'and design of pulse transformer isolation gate drive circuits.',
    'pe-q20': 'Compare the operating principles, circuit topologies, and performance of Voltage Source Inverters (VSI) '
              'and Current Source Inverters (CSI). Explain the ASCI commutation mechanism.',
    'pe-q21': 'Explain the operation of a single-phase AC voltage controller with resistive load using Integral Cycle '
              'Control and Phase Angle Control. Derive expressions for RMS output voltage and power factor.',
    'pe-q22': 'Analyze the single-phase AC voltage controller with an inductive (RL) load. Discuss the three operating '
              'cases based on firing angle alpha and load angle phi, and derive the RMS output voltage.',
    'pe-q23': 'Explain the working principle of single-phase to single-phase cycloconverters in mid-point and bridge '
              'configurations. Compare circulating and non-circulating current modes.',
    'pe-q24': 'Explain the limitations of hard switching in high-frequency converters. Describe the principles and '
              'circuit topologies of Zero-Current Switching (ZCS) and Zero-Voltage Switching (ZVS) resonant '
              'converters.',
    'pe-q25': 'Describe the circuit operation of isolated Switched-Mode Power Supply (SMPS) topologies: Flyback, '
              'Forward, Push-Pull, Half-bridge, and Full-bridge converters with comparative evaluation.',
    'pe-q26': 'Explain the architectures of Uninterruptible Power Supplies (UPS): Offline, Line-Interactive, and '
              'Online Double-Conversion. Discuss the role of the static bypass switch and compare performance metrics.',
    'pe-q3': 'Explain the dynamic switching characteristics of an SCR during turn-on and turn-off processes. Define '
             'reverse recovery time, gate recovery time, and circuit turn-off time with neat waveforms.',
    'pe-q4': 'Explain the need for di/dt and dv/dt protection for an SCR. Derive the design equations for a series '
             'inductor and an RC snubber circuit with a step-by-step numerical example.',
    'pe-q5': 'Compare the operating principles, switching speeds, conduction losses, and Safe Operating Areas (SOA) of '
             'TRIAC, GTO, Power MOSFET, and IGBT.',
    'pe-q6': 'Explain the operation of a single-phase half-wave controlled rectifier with R and RL loads. Derive '
             'expressions for average and RMS output voltages, and explain the effect of a freewheeling diode.',
    'pe-q7': 'Derive the expression for average and RMS output voltages of a single-phase fully controlled bridge '
             'rectifier feeding an RLE load. Distinguish between continuous and discontinuous conduction modes.',
    'pe-q8': 'Define and derive the performance parameters of phase-controlled converters: Displacement Factor (DF), '
             'Harmonic Factor (HF/THD), and Input Power Factor (PF). Compare semi-converter and full converter.',
    'pe-q9': 'Describe the working of a three-phase fully controlled bridge converter (6-pulse) with RL load. Derive '
             'the expression for average DC output voltage and plot the line-to-line output waveforms.',
    'phy-q1': 'Derive the differential equation of damped harmonic oscillations. Obtain the general solution and '
              'discuss the three cases of damping: overdamped, critically damped, and underdamped.',
    'phy-q10': 'State and prove the plane transmission diffraction grating equation. Derive expressions for the '
               'maximum observable order of spectra, dispersive power, and resolving power of the grating based on '
               "Rayleigh's criterion.",
    'phy-q11': 'State de Broglie hypothesis and derive expressions for de Broglie wavelength for a particle of energy '
               "E and an electron accelerated through potential V. State Heisenberg's uncertainty principle and prove "
               'that free electrons cannot exist inside an atomic nucleus.',
    'phy-q12': "Explain the physical significance of the wave function psi. Discuss Born's statistical interpretation, "
               'the normalization condition, and the necessary mathematical criteria for an acceptable wave function.',
    'phy-q13': 'Derive both the one-dimensional Time-Dependent and Time-Independent Schrödinger wave equations for a '
               'particle moving in a conservative potential field.',
    'phy-q14': 'Solve the one-dimensional time-independent Schrödinger equation for a particle trapped in an infinite '
               'potential well of width L. Derive expressions for the quantized energy eigenvalues, zero-point energy, '
               'and normalized wave functions.',
    'phy-q15': 'Explain the quantum confinement effect in nanomaterials. Classify nanomaterials as 0D, 1D, and 2D with '
               'examples. Describe the synthesis of nanomaterials using the Sol-Gel technique and Chemical Vapor '
               'Deposition (CVD).',
    'phy-q16': 'Explain the piezoelectric method of generating ultrasonic waves with a neat circuit diagram. State the '
               'converse piezoelectric effect and derive the formula for the resonant frequency of a vibrating quartz '
               'crystal plate.',
    'phy-q17': 'Explain the principle, circuit diagram, and working of a magnetostriction ultrasonic generator. Derive '
               'the expression for the resonant frequency of the ferromagnetic rod and state its operating frequency '
               'limits.',
    'phy-q18': 'Explain the principle and working of Ultrasonic Non-Destructive Testing (NDT) using the pulse-echo '
               'method. Draw a typical A-scan display and derive the formula for determining the depth of an internal '
               'flaw.',
    'phy-q19': "Define reverberation and reverberation time. State and derive Sabine's formula for the reverberation "
               'time of an auditorium based on the growth and decay of acoustic energy density.',
    'phy-q2': 'Derive the differential equation for forced harmonic oscillations. Obtain the expressions for the '
              'steady-state amplitude and phase difference, and discuss their variation with driving frequency.',
    'phy-q20': 'Discuss the essential architectural acoustic requirements of an auditorium. Explain common acoustic '
               'defects such as echoes, flutter echoes, sound focusing, and resonance, along with their engineering '
               'remedies.',
    'phy-q21': "Explain the three radiation-matter interaction processes. Derive the relations between Einstein's A "
               'and B coefficients, and explain why population inversion is necessary for laser action.',
    'phy-q22': 'Describe the construction and working of a Ruby laser with a neat schematic and three-level energy '
               'band diagram. Explain why ruby lasers operate in pulsed mode.',
    'phy-q23': 'Explain the construction and four-level working of a Helium-Neon (He-Ne) gas laser with an energy '
               'level diagram. Explain the mechanism of resonant collision energy transfer and continuous-wave '
               'emission at 632.8 nm.',
    'phy-q24': 'Explain the working principle of a semiconductor diode laser (GaAs). Explain how population inversion '
               'is achieved across a degenerately doped p-n junction under forward bias and how the optical cavity is '
               'formed.',
    'phy-q25': 'Explain the principle of light propagation in an optical fiber by total internal reflection. Derive '
               'expressions for the acceptance angle and Numerical Aperture of a step-index optical fiber.',
    'phy-q26': 'Classify optical fibers based on refractive index profile and mode of propagation. Explain the '
               'fundamental attenuation mechanisms in optical fibers: absorption, Rayleigh scattering, and bending '
               'losses.',
    'phy-q3': 'Explain the phenomenon of amplitude resonance in forced oscillations. Derive expressions for resonant '
              'frequency, sharpness of resonance, Quality factor, and logarithmic decrement.',
    'phy-q4': 'Derive the one-dimensional differential wave equation for the propagation of transverse waves on a '
              'stretched flexible string from fundamental principles.',
    'phy-q5': 'Apply rigid boundary conditions to obtain the standing wave modes and quantized natural frequencies of '
              "transverse vibrations on a stretched string fixed at both ends. State Mersenne's laws.",
    'phy-q6': 'Derive the expression for the optical path difference between reflected rays in a thin parallel '
              'transparent film. Deduce the conditions for constructive and destructive interference, and explain why '
              'an extremely thin film appears dark.',
    'phy-q7': 'Explain the formation of interference fringes in an air wedge. Derive the expression for fringe width '
              'and explain how the diameter of a thin wire is measured experimentally.',
    'phy-q8': "Explain the theory of Newton's rings in reflected light. Derive expressions for the diameters of dark "
              'and bright rings, and explain how the wavelength of sodium light and the refractive index of a liquid '
              'are determined.',
    'phy-q9': 'Derive the expression for the intensity distribution in Fraunhofer diffraction at a single slit. Obtain '
              'the conditions for central maximum, secondary maxima, and diffraction minima, and deduce the angular '
              'width of the central maximum.',
    'ps2-q1': 'Derive the mathematical expression for the instantaneous short-circuit current on a transmission line '
              'modeled as an RL circuit. Explain the DC offset component and the doubling effect.',
    'ps2-q10': 'Derive the expressions for sequence currents, sequence voltages, and ground fault current for a Double '
               "Line-to-Ground (LLG) fault on phases 'b' and 'c'. Draw the sequence network interconnection.",
    'ps2-q11': 'Classify the buses in a power system for load flow studies. State the known and unknown variables for '
               'each bus type and explain the formulation of Bus Admittance Matrix (Y_bus) by inspection.',
    'ps2-q12': 'Derive the static real and reactive power flow equations of an n-bus power system in polar coordinates '
               'from first principles using complex power injection relations.',
    'ps2-q13': 'Explain the Gauss-Seidel method for power flow solution. Derive the iterative bus voltage equation, '
               'discuss the role of acceleration factor, and explain the handling of PV buses with reactive power '
               'limits.',
    'ps2-q14': 'Formulate the Newton-Raphson load flow algorithm in polar coordinates. Derive the explicit '
               'mathematical expressions for the diagonal and off-diagonal elements of the Jacobian matrix sub-blocks.',
    'ps2-q15': 'State the physical assumptions underlying the Fast Decoupled Load Flow (FDLF) method. Derive the '
               "decoupled matrix equations involving B' and B'' and discuss its computational advantages.",
    'ps2-q16': 'Derive the swing equation governing the rotor dynamics of a synchronous machine during transients. '
               'Define inertia constant H and angular momentum M, and express the equation in electrical radians and '
               'degrees.',
    'ps2-q17': 'Derive the power-angle equation Pe = Pmax sin(delta) for a synchronous machine connected to an '
               'infinite bus. Define synchronizing power coefficient and determine the steady-state stability limit.',
    'ps2-q18': 'State and prove the Equal Area Criterion (EAC) for the transient stability of a synchronous machine. '
               'Apply EAC to determine the maximum swing angle for a sudden step increase in mechanical power input.',
    'ps2-q19': 'Apply the Equal Area Criterion to derive the expression for the Critical Clearing Angle (delta_cr) for '
               'a three-phase fault on a double-circuit transmission line. Obtain the critical clearing time formula.',
    'ps2-q2': 'Explain the physical phenomena occurring during a symmetrical 3-phase fault at the terminals of an '
              'unloaded synchronous generator. Define subtransient, transient, and steady-state reactances with neat '
              'oscillogram.',
    'ps2-q20': 'Explain the various practical methods employed in modern power systems to improve transient and '
               'dynamic stability, including fast fault clearing, auto-reclosing, dynamic braking, and FACTS devices.',
    'ps2-q21': 'Develop the transfer function block diagram of an isolated single-area power system for Load Frequency '
               'Control (LFC). Derive the expression for steady-state frequency deviation following a step load '
               'change.',
    'ps2-q22': 'Explain secondary frequency control and the dynamics of a two-area interconnected power system. Derive '
               'the tie-line power flow equation and define the Area Control Error (ACE) for each control area.',
    'ps2-q23': 'Draw the functional block diagram of an Automatic Voltage Regulator (AVR) for a synchronous generator. '
               'State the transfer functions of each constituent component and discuss stability compensation.',
    'ps2-q24': 'Formulate the economic load dispatch problem for thermal generating units neglecting transmission line '
               'losses. Using Lagrange multipliers, derive the criterion of equal incremental fuel costs.',
    'ps2-q25': "Formulate the economic dispatch problem including transmission network losses using Kron's loss "
               'formula. Derive the coordination equations and explain the physical significance of the Penalty Factor '
               'Li.',
    'ps2-q26': 'Two thermal generating units have fuel cost functions C1 = 0.05 P1^2 + 20 P1 + 800 Rs/h and C2 = 0.06 '
               'P2^2 + 15 P2 + 1000 Rs/h with limits 20 <= Pi <= 120 MW. For a total load of 180 MW, find optimal '
               'generation schedule, lambda, and calculate hourly cost savings compared to equal load sharing.',
    'ps2-q3': 'Define Short Circuit MVA. Explain the selection criteria for circuit breaker ratings, differentiating '
              'between rated symmetrical interrupting current and rated momentary making current.',
    'ps2-q4': 'Explain the step-by-step algorithm for the formation of the Bus Impedance Matrix (Z_bus). Derive the '
              'mathematical formulas for the four types of branch additions and Kron reduction.',
    'ps2-q5': 'Calculate the fault current in kA and fault MVA for a 3-phase symmetrical fault on an interconnected '
              'power system with two generators, step-up transformers, and transmission line on a 100 MVA base.',
    'ps2-q6': "State Fortescue's theorem and explain the symmetrical components transformation. Define the complex "
              "operator 'a', state its mathematical properties, and prove the invariance of complex power.",
    'ps2-q7': 'Draw and explain the positive, negative, and zero sequence equivalent circuits of synchronous '
              'generators, three-phase transformers (with various winding and grounding connections), and transmission '
              'lines.',
    'ps2-q8': 'Derive the expressions for sequence currents and fault current for a Single Line-to-Ground (LG) fault '
              "on phase 'a' through a fault impedance Zf. Draw the sequence network interconnection.",
    'ps2-q9': 'Derive the expressions for sequence currents and fault current for a Line-to-Line (LL) fault between '
              "phases 'b' and 'c' through fault impedance Zf. Draw the sequence network interconnection.",
    'res-q1': 'Explain the terms extraterrestrial and terrestrial solar radiation. Define solar constant and air mass '
              'ratio with standard values.',
    'res-q10': 'Compare grid-tied and stand-alone solar PV systems with functional block diagrams, balance of system '
               '(BOS) components, and inverter configurations.',
    'res-q11': 'Derive the expression for total power in an unconstrained wind stream. Derive the Betz limit for '
               'maximum theoretical power extraction using actuator disc theory.',
    'res-q12': 'Compare Horizontal Axis Wind Turbines (HAWT) and Vertical Axis Wind Turbines (VAWT) in terms of '
               'aerodynamic principles, lift vs drag, tip-speed ratio, and efficiency.',
    'res-q13': 'Draw a neat cutaway diagram of a utility-scale HAWT nacelle and explain the functions of the drive '
               'train, gearbox, yaw mechanism, and pitch control.',
    'res-q14': 'Compare the operation, converter sizing, and characteristics of Doubly Fed Induction Generators (DFIG) '
               'and Permanent Magnet Synchronous Generators (PMSG) for wind turbines.',
    'res-q15': 'Explain the wind turbine power curve across operating Regions 1 to 4. Compare pitch control, passive '
               'stall, and active stall aerodynamic power regulation.',
    'res-q16': 'Explain the thermochemical conversion pathways of biomass: Direct Combustion, Gasification (chemical '
               'reactions and gasifier types), and Pyrolysis.',
    'res-q17': 'Explain the biochemical process of biogas production through anaerobic digestion detailing the four '
               'stages: Hydrolysis, Acidogenesis, Acetogenesis, and Methanogenesis.',
    'res-q18': 'Compare the construction, operational gas pressure, capital cost, and maintenance of Floating Drum '
               '(KVIC) and Fixed Dome (Deenabandhu) biogas plants.',
    'res-q19': 'Explain the thermodynamic principle of Ocean Thermal Energy Conversion (OTEC). Compare Open-Cycle '
               '(Claude) and Closed-Cycle (Rankine) OTEC systems with Carnot limits.',
    'res-q2': 'Define the following solar angles with neat sketches: (i) Declination angle, (ii) Hour angle, (iii) '
              'Solar altitude angle, (iv) Zenith angle, and (v) Solar azimuth angle.',
    'res-q20': 'Derive the theoretical potential energy stored in a tidal barrage basin per tidal cycle. Explain the '
               'working of an Oscillating Water Column (OWC) with a Wells turbine.',
    'res-q21': 'Explain the working principle of a hydrogen-oxygen fuel cell. Derive the theoretical thermodynamic '
               'efficiency and describe the V-I polarization curve overpotentials.',
    'res-q22': 'Compare Proton Exchange Membrane Fuel Cells (PEMFC) and Solid Oxide Fuel Cells (SOFC) in terms of '
               'electrolyte, operating temperature, catalysts, and applications.',
    'res-q23': 'Describe Battery Energy Storage Systems (BESS). Define State of Charge (SoC), Depth of Discharge '
               '(DoD), C-rate, round-trip efficiency, and degradation mechanisms.',
    'res-q24': 'Explain the architecture of a Hybrid Renewable Energy System (HRES). Compare DC-coupled and AC-coupled '
               'topologies, and describe the energy dispatch strategy.',
    'res-q25': 'Explain AC and DC microgrid architectures. Discuss grid-connected and islanded modes, and derive the '
               'decentralized P-f and Q-V droop control equations.',
    'res-q26': 'Discuss the major grid integration challenges of high-penetration renewables: Duck curve, loss of '
               'rotational inertia, power quality harmonics, and Low-Voltage Fault Ride-Through (LVRT).',
    'res-q3': 'Explain with neat sketches the construction and working principles of a Pyranometer and a Pyrheliometer '
              'for measuring solar radiation.',
    'res-q4': 'Derive the single-diode equivalent circuit model and the governing I-V characteristic equation of a '
              'practical solar photovoltaic cell.',
    'res-q5': 'Define Open-Circuit Voltage, Short-Circuit Current, Maximum Power Point, Fill Factor, and Conversion '
              'Efficiency of a PV cell with step-by-step numerical calculation.',
    'res-q6': 'Explain the construction and working of a liquid flat-plate solar collector. Derive the '
              'Hottel-Whillier-Bliss useful energy balance equation and efficiency.',
    'res-q7': 'Classify concentrating solar thermal collectors. Compare Parabolic Trough, Linear Fresnel, Solar Power '
              'Tower, and Parabolic Dish systems.',
    'res-q8': 'Explain the effects of partial shading on PV module I-V and P-V characteristics. Discuss hot-spot '
              'formation and the protective role of bypass and blocking diodes.',
    'res-q9': 'Explain the Maximum Power Point Tracking (MPPT) principle. Derive the mathematical formulation of '
              'Perturb & Observe (P&O) and Incremental Conductance algorithms.',
    'vcdet-q1': "Solve Bernoulli's differential equation dy/dx + y = y^2 (cos x - sin x).",
    'vcdet-q10': 'If r = x i + y j + z k and r = |r|, prove that: (i) grad(r^n) = n r^(n-2) r, (ii) div(r^n r) = '
                 '(n+3)r^n, and (iii) Laplacian(r^n) = n(n+1)r^(n-2). Hence show that 1/r is harmonic for r != 0.',
    'vcdet-q11': "Using Green's theorem, evaluate the line integral oint_C [(x - y) dx + (x + y) dy] where C is the "
                 'closed curve bounded by y = x^2 and y^2 = x traversed counter-clockwise.',
    'vcdet-q12': 'State Gauss divergence theorem and explain its physical significance in electrostatics and fluid '
                 'mechanics.',
    'vcdet-q13': "Verify Green's theorem in the plane for oint_C [(xy + y^2) dx + x^2 dy] where C is the closed curve "
                 'bounded by y = x and y = x^2.',
    'vcdet-q14': 'Verify Gauss divergence theorem for F = 4xz i - y^2 j + yz k over the cube bounded by x = 0, x = 1, '
                 'y = 0, y = 1, z = 0, z = 1.',
    'vcdet-q15': "Verify Stokes' theorem for F = (2x - y)i - yz^2 j - y^2 z k over the upper hemisphere S: x^2 + y^2 + "
                 'z^2 = 1, z >= 0 bounded by the circle C: x^2 + y^2 = 1 in the xy-plane.',
    'vcdet-q16': "State Dirichlet's conditions for the existence of Fourier series of a function f(x) in an interval "
                 '(c, c + 2L). What does the Fourier series converge to at a point of finite discontinuity?',
    'vcdet-q17': 'Find the half-range Fourier sine series expansion for f(x) = k (constant) in the interval 0 < x < '
                 'pi.',
    'vcdet-q18': 'Find the Fourier series of f(x) = x^2 in the interval -pi <= x <= pi. Hence deduce that: (i) '
                 'sum_{n=1}^infinity (-1)^(n-1)/n^2 = pi^2/12, and (ii) sum_{n=1}^infinity 1/n^2 = pi^2/6.',
    'vcdet-q19': 'Find the Fourier series of the periodic square wave: f(x) = -k for -pi < x < 0 and k for 0 < x < pi '
                 'with period 2pi. Hence deduce the Gregory-Leibniz series for pi: 1 - 1/3 + 1/5 - 1/7 + ... = pi/4.',
    'vcdet-q2': 'Solve the second order differential equation (D^2 - 4D + 4)y = 8e^(2x) + sin 2x.',
    'vcdet-q20': 'Find the Fourier cosine and sine transforms of f(x) = e^(-ax) (a > 0). Hence evaluate the integral '
                 'int_0^infinity cos(omega*x) / (a^2 + omega^2) d(omega).',
    'vcdet-q21': 'Find the Laplace transform of f(t) = t^2 e^(-3t) sin 2t.',
    'vcdet-q22': 'State the Convolution Theorem for Laplace transforms. Use it to find L^(-1){1 / (s(s^2 + 1))}.',
    'vcdet-q23': 'Evaluate L{(cos at - cos bt) / t} and hence compute the improper integral int_0^infinity (cos t - '
                 'cos 2t) / t dt.',
    'vcdet-q24': 'Using the Convolution Theorem, find the inverse Laplace transform of F(s) = 1 / (s^2 + a^2)^2.',
    'vcdet-q25': 'Solve the initial value problem using Laplace transform: d^2y/dt^2 + 4 dy/dt + 4y = 6 e^(-2t) '
                 "subject to y(0) = -2 and y'(0) = 8.",
    'vcdet-q26': 'Solve the system of simultaneous ordinary differential equations using Laplace transform: dx/dt + y '
                 '= sin t, dy/dt + x = cos t subject to x(0) = 1 and y(0) = 0.',
    'vcdet-q3': 'Solve the differential equation d^2y/dx^2 + y = sec x tan x using the method of variation of '
                'parameters.',
    'vcdet-q4': 'Solve the Cauchy-Euler differential equation: x^2 d^2y/dx^2 - 3x dy/dx + 4y = 2x^2 using the '
                'transformation x = e^z.',
    'vcdet-q5': 'Solve the non-homogeneous higher order linear differential equation: (D^2 - 2D + 1)y = x e^x sin x '
                'using the exponential shift operator.',
    'vcdet-q6': 'Find the directional derivative of phi(x, y, z) = x^2 y z + 4 x z^2 at the point (1, -2, -1) in the '
                'direction of the vector a = 2i - j - 2k.',
    'vcdet-q7': 'Find the unit normal vector to the surface x^2 + y^2 + 2z^2 = 4 at the point (1, 1, 1), and find the '
                'equation of the tangent plane.',
    'vcdet-q8': 'Show that the vector field F = (2xy + z^3)i + x^2 j + 3xz^2 k is conservative and irrotational. Find '
                'its scalar potential phi(x, y, z) such that F = grad phi. Hence evaluate the work done in moving a '
                'particle from (1, -2, 1) to (3, 1, 4).',
    'vcdet-q9': 'Find constants a, b, c such that the vector field F = (x + 2y + az)i + (bx - 3y - z)j + (4x + cy + '
                '2z)k is irrotational. Also show that F is solenoidal for all values of a, b, c.'}
