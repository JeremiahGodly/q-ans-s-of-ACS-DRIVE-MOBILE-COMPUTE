# -*- coding: utf-8 -*-
"""
Content generator for Subject 9: Management for Engineers (HUT300)
KTU 2019 Scheme Comprehensive Question Bank.
All answers are written from the perspective of an experienced engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r\"\"\"...\"\"\") to prevent LaTeX backslash corruption.
"""

MANAGEMENT_MODULES = [
    {
        "module_id": "mgt-m1",
        "module_num": "Module 1",
        "module_title": "Principles & Functions of Management, Organizational Structures, Ethics",
        "questions": [
            {
                "qid": "mgt-q1",
                "marks": 7,
                "type": "Descriptive",
                "title": "Scientific Management by F.W. Taylor: Principles, Techniques, and Mental Revolution",
                "yt_query": "scientific management taylor principles techniques time motion study",
                "img_path": "images/mgt/scientific_management_framework.png",
                "img_caption": "Figure 1.1: Taylor's Scientific Management Framework and Functional Foremanship Architecture",
                "answer": r"""
Frederick Winslow Taylor (1856-1915), recognized as the Father of Scientific Management, introduced a systematic, empirical approach to industrial shop-floor management at the Midvale and Bethlehem Steel companies. Confronted with widespread worker 'soldiering' (deliberate restriction of output) and arbitrary management rule-of-thumb traditions, Taylor sought to replace intuition and guesswork with precise scientific investigation, measurement, and standardization.

1. Foundational Principles of Scientific Management:
- Science, Not Rule of Thumb: Every element of a workman's task must be subjected to rigorous scientific study (investigating tool geometry, feed rates, physical postures, and operational sequencing) to establish the single 'one best way' of performing the work, discarding arbitrary rules-of-thumb.
- Harmony, Not Discord: Taylor insisted on complete psychological alignment between management and labor. Instead of fighting over the division of existing enterprise surplus, both groups must collaborate to expand total productivity, creating a larger surplus that yields higher wages for workers and higher profits for the enterprise.
- Cooperation, Not Individualism: Mutual trust and joint responsibility must govern workplace relations. Management assumes the responsibility of planning, scheduling, and standardizing working conditions, leaving the physical execution to workers, thereby eliminating adversarial friction.
- Development of Each Person to Greatest Efficiency and Prosperity: Workers must be scientifically selected according to physical and mental suitability, systematically trained in standardized work methods, and assigned tasks aligned with their maximum potential.
- Equal Division of Work and Responsibility: Management takes over all work for which it is better fitted (planning, design, process control, and method development), whereas previously almost all responsibility was thrust onto the shop-floor worker.

2. Core Techniques of Scientific Management:
- Time Study: The measurement of the time required by an average skilled operator working under normal conditions to complete a standardized task, utilizing a stopwatch to establish standard task times.
- Motion Study: Pioneered with Frank and Lillian Gilbreth, this involves the close observation and elimination of unnecessary, wasteful, and awkward physical movements during work execution, optimizing the kinetic trajectory of the human body.
- Standardization of Tools, Equipment, and Working Conditions: Establishing precise technical standards for machine speeds, cutting tools, bench heights, ambient lighting, and raw material specifications to guarantee uniform production cycles.
- Functional Foremanship: Taylor rejected the traditional military-style single foreman command. He proposed eight specialized functional foremen divided between the Planning Department and the Shop Floor:
  1. Planning Department Foremen: Route Clerk (determines production sequence), Instruction Card Clerk (issues step-by-step operating instructions), Time and Cost Clerk (records time taken and computes labor costs), and Shop Disciplinarian (handles grievances, attendance, and discipline).
  2. Shop Floor (Execution) Foremen: Gang Boss (prepares machines, tools, and materials before work starts), Speed Boss (ensures cutting machines run at scientifically designated speeds), Repair Boss (maintains and repairs machinery), and Inspector (checks product dimensional accuracy and quality standards).
- Differential Piece Rate System: An aggressive incentive wage system designed to reward high performers and penalize underperformance. Taylor established two distinct wage rates: a high piece rate for workers who reach or exceed the standard daily output, and a low piece rate (e.g., $20\% \text{ to } 30\%$ lower) for those who fail to achieve the standard quota.

3. The Concept of Mental Revolution:
Taylor emphasized that the techniques of scientific management are worthless without a complete 'Mental Revolution' on the part of both management and workers. Workers must stop viewing management as exploiters and realize that maximizing efficiency secures higher earning power. Concurrently, management must stop treating labor as cheap commodities and share the economic fruits of increased productivity through generous incentive compensation.
"""
            },
            {
                "qid": "mgt-q2",
                "marks": 7,
                "type": "Descriptive",
                "title": "Henri Fayol's 14 Principles of Administrative Management",
                "yt_query": "henri fayol 14 principles of management administrative theory",
                "img_path": "images/mgt/fayol_14_principles.png",
                "img_caption": "Figure 1.2: Henri Fayol's Administrative Management Architecture and Scalar Chain Gangplank",
                "answer": r"""
Henri Fayol (1841-1925), a French mining engineer and senior executive, is regarded as the Father of Modern Operational Management Theory. Unlike Taylor, who focused on shop-floor technical efficiency, Fayol addressed the universal administrative functions of top-level enterprise management. In his 1916 treatise *Administration Industrielle et Générale*, Fayol articulated 14 universal principles of management:

1. Division of Work: Specialization of labor increases output by making workers more efficient, reducing cognitive and physical switching costs across engineering, manufacturing, and commercial tasks.
2. Authority and Responsibility: Authority is the official right to issue orders and the personal power to exact obedience. Responsibility is the natural corollary of authority. Fayol stressed that authority and responsibility must be commensurate: delegating authority without corresponding responsibility invites abuse, while holding a manager responsible without granting commensurate authority paralyzes decision-making.
3. Discipline: Obedience, application, energy, and outward marks of respect observed in accordance with standing agreements between the firm and its employees. Requires good superiors at all levels, clear and fair agreements, and judicious application of penalties.
4. Unity of Command: An employee must receive orders from one, and only one, direct superior. Fayol warned that if an employee reports to two superiors, authority is undermined, discipline is imperiled, order is disturbed, and stability is threatened.
5. Unity of Direction: One head and one plan for a group of organizational activities having the same objective ($One Head, One Plan$). This ensures coordination and focusing of corporate effort.
6. Subordination of Individual Interest to General Interest: The interests of an individual employee or group of employees must not prevail over the overarching goals, survival, and prosperity of the enterprise.
7. Remuneration of Personnel: Compensation paid to employees must be fair, equitable, and afford maximum possible satisfaction to both employees and the employer, incorporating both financial (bonuses, piece rates) and non-financial incentives.
8. Centralization: The degree to which decision-making authority is concentrated at top management versus dispersed to lower operational levels. Fayol argued that centralization is not inherently good or bad; the optimal balance must vary according to enterprise size, organizational maturity, and subordinate competence.
9. Scalar Chain (Line of Authority) and Gangplank: The uninterrupted chain of superiors ranging from the ultimate authority (CEO) down to the lowest ranks. Communications normally follow this formal scalar line. However, to prevent bureaucratic delays in urgent situations, Fayol introduced the Gangplank (cross-communication bridge): two colleagues at the same hierarchical level in different departments may communicate directly, provided their respective immediate superiors have authorized the bridge and are kept informed of the outcome.
10. Order: A place for everything (everyone) and everything (everyone) in its place ($Material Order$ ensures tools and materials are readily accessible; $Social Order$ ensures right person in the right job through scientific placement).
11. Equity: A combination of fairness, justice, and friendliness on the part of managers toward subordinates, fostering loyalty and devotion.
12. Stability of Tenure of Personnel: High employee turnover is both a cause and consequence of poor management. An employee requires substantial time to adapt to a new function and perform effectively; tenure stability must be preserved through job security.
13. Initiative: The freedom to conceive, formulate, and execute a plan. Fayol urged managers to encourage subordinate initiative, as it represents a powerful source of organizational vitality.
14. Esprit de Corps: Promoting team spirit, harmony, and unity within the workforce. Fayol warned against two major dangers: dividing personnel into warring factions and abusing written communication when direct oral communication can resolve misunderstandings.
"""
            },
            {
                "qid": "mgt-q3",
                "marks": 7,
                "type": "Descriptive",
                "title": "Functions of Management (POSDCORB) and the Managerial Decision-Making Process",
                "yt_query": "POSDCORB functions of management decision making process risk uncertainty",
                "img_path": "images/mgt/posdcorb_decision_making.png",
                "img_caption": "Figure 1.3: The POSDCORB Management Cycle and Structured Rational Decision-Making Flowchart",
                "answer": r"""
Management is fundamentally defined as the dynamic process of planning, organizing, actuating, and controlling enterprise resources (human, financial, physical, and informational) to achieve organizational goals efficiently and effectively.

1. Universal Functions of Management (POSDCORB):
Synthesizing Fayol's functional breakdown, Luther Gulick coined the classical acronym POSDCORB to summarize the primary administrative duties of management:
- Planning ($P$): The foundational function of deciding in advance what to do, how to do it, when to do it, and who is to do it. It bridges the gap from where an organization currently stands to where it desires to be. Planning involves environmental forecasting, formulating missions and long-term strategic objectives, and establishing policies, procedures, and operating budgets.
- Organizing ($O$): The formal structuring of enterprise activities. Involves identifying and grouping required tasks, assigning these task clusters to specific departments or work teams, delegating requisite authority, and defining clear reporting relationships to prevent duplication and conflict.
- Staffing ($S$): The human resource function of maintaining qualified personnel in the organization. Encompasses manpower planning, recruitment, selection, job placement, orientation, training, career development, performance appraisal, and compensation.
- Directing ($D$): The continuous task of guiding, instructing, and supervising employees. It encompasses four vital sub-functions: Leadership (guiding subordinates toward objectives), Motivation (energizing positive work behaviors), Communication (transmitting unambiguous information), and Supervision (overseeing day-to-day execution).
- Coordinating ($CO$): Harmonizing all individual efforts, departmental processes, and functional divisions to ensure unified action toward common enterprise goals. It prevents inter-departmental friction and sub-optimization.
- Reporting ($R$): Keeping executive management, board directors, shareholders, and regulatory authorities informed through systematic records, operational research, quality audits, and financial statements.
- Budgeting ($B$): Translating organizational plans into quantitative financial terms. Encompasses fiscal planning, capital allocation, revenue forecasting, cost accounting, and budgetary variance control.

2. Rational Decision-Making Process:
Decision-making is the conscious cognitive process of selecting a single course of action from among two or more mutually exclusive alternatives. The rational decision-making model follows seven systematic phases:
1. Identification and Definition of the Problem: Diagnosing root causes rather than surface symptoms (e.g., distinguishing between declining machine output and motor overheating).
2. Establishing Decision Criteria and Weights: Defining performance benchmarks (e.g., cost, safety, payback period, technical reliability) and assigning relative importance weights.
3. Development of Alternative Solutions: Brainstorming and engineering design synthesis to generate a robust set of potential strategies.
4. Evaluation of Alternatives: Assessing each generated alternative against the established criteria, risks, resource constraints, and feasibility limits.
5. Selection of the Best Alternative: Choosing the option that maximizes net utility or expected monetary value ($EMV$).
6. Implementation of the Decision: Mobilizing physical, financial, and human resources, communicating directives to affected stakeholders, and executing the chosen solution.
7. Monitoring and Follow-Up: Establishing feedback control loops to track actual operational results against planned performance, taking corrective action if variances arise.

3. Decision-Making Environments:
- Certainty: Complete knowledge exists; the outcome of every alternative is known with $100\%$ deterministic accuracy (e.g., standard linear programming problems).
- Risk: Future states of nature cannot be predicted with certainty, but objective historical probabilities can be assigned to each possible outcome (evaluated using Expected Value: $EMV = \sum p_i X_i$).
- Uncertainty: Future outcomes are unknown, and no reliable objective probability distribution exists (evaluated using decision rules like Maximax, Maximin, Laplace, or Hurwicz criteria).
"""
            },
            {
                "qid": "mgt-q4",
                "marks": 7,
                "type": "Descriptive",
                "title": "Organizational Structures: Line, Functional, Line and Staff, and Matrix Organizations",
                "yt_query": "organizational structures line functional line and staff matrix organization charts",
                "img_path": "images/mgt/organizational_structures.png",
                "img_caption": "Figure 1.4: Comparative Organizational Charts of Line, Functional, Line & Staff, and Matrix Structures",
                "answer": r"""
An organizational structure defines the formal framework of task allocation, coordination, authority distribution, and reporting relationships within an enterprise. The choice of structural design directly influences operational flexibility, decision speed, and employee productivity.

1. Line Organization (Military / Scalar Organization):
- Architecture: The oldest and simplest organizational design. Authority flows strictly vertically downward in an unbroken scalar chain from top management to shop-floor operatives, while accountability flows strictly upward. Every individual has a single, unambiguous superior.
- Advantages: Absolute simplicity; unity of command is rigidly preserved; rapid decision-making without committee consensus; clear fixing of individual responsibility.
- Limitations: Lack of specialized technical expertise; key line executives are overloaded with administrative and technical duties; autocratic tendencies; rigid and inflexible.
- Suitability: Small enterprises, automated continuous process plants, or military units with routine operations.

2. Functional Organization:
- Architecture: Proposed by F.W. Taylor to overcome the lack of technical specialization in pure line systems. Work is divided according to managerial functions (e.g., Production, Quality, Design, Maintenance, Finance). Each functional specialist exercises direct command authority over workers within their functional domain.
- Advantages: Maximum exploitation of technical specialization; relieves shop-floor supervisors of planning burdens; promotes high operational efficiency and technical mastery.
- Limitations: Destroys Unity of Command (workers receive simultaneous orders from multiple functional bosses); creates inter-departmental conflicts and boundary disputes; difficulty in fixing overall project accountability; slow coordination across functions.
- Suitability: Medium-to-large single-product manufacturing plants requiring deep specialized skills.

3. Line and Staff Organization:
- Architecture: A hybrid structure that combines the executive authority of line managers with the advisory support of specialized staff experts.
  - Line Managers: Possess executive decision-making and operational command authority (the authority to command action).
  - Staff Specialists: Possess advisory authority (the authority to counsel, investigate, research, and recommend, e.g., Legal Counsel, R&D, Industrial Engineering, Safety Officers). Staff personnel have no direct right to issue orders to line subordinates.
- Advantages: Combines expert specialized counsel with unambiguous operational command; maintains unity of command for operating workers; relieves line executives of technical research burdens.
- Limitations: Friction between line and staff personnel (line managers perceive staff as impractical theorists; staff specialists feel their expert recommendations are ignored); high administrative overhead costs.
- Suitability: Large industrial enterprises, aerospace corporations, and public utility corporations.

4. Matrix Organization (Project-Functional Hybrid):
- Architecture: A multidimensional grid structure where horizontal project or product management teams are superimposed across traditional vertical functional departments. Employees have two direct bosses simultaneously: a permanent Functional Manager (who manages career progression, professional standards, and technical training) and a temporary Project Manager (who manages project deliverables, schedules, and budgets).
- Advantages: Exceptional flexibility; optimal sharing of scarce, specialized engineering talent across concurrent projects; rapid responsiveness to shifting customer requirements; excellent inter-disciplinary collaboration.
- Limitations: Direct violation of Fayol's Unity of Command creates dual-boss role ambiguity and psychological stress; power struggles between functional and project heads; high communication overhead and meeting times.
- Suitability: High-technology engineering projects, defense aerospace contracting, large civil infrastructure, and software systems integration.
"""
            },
            {
                "qid": "mgt-q5",
                "marks": 7,
                "type": "Descriptive",
                "title": "Corporate Social Responsibility (CSR), Carroll's Pyramid, and Professional Engineering Ethics",
                "yt_query": "corporate social responsibility carroll pyramid engineering ethics whistleblowing",
                "img_path": "images/mgt/csr_carroll_pyramid.png",
                "img_caption": "Figure 1.5: Carroll's Four-Part Pyramid of Corporate Social Responsibility and Ethical Decision Framework",
                "answer": r"""
Modern engineering enterprises do not operate in a social vacuum; they exist within a societal matrix where technological innovation and profit generation must balance ecological integrity, public welfare, and moral responsibility.

1. Corporate Social Responsibility (CSR):
CSR is the ongoing commitment by business enterprises to behave ethically and contribute to sustainable economic development while improving the quality of life of the workforce, their families, the local community, and society at large.
In India, the Companies Act of 2013 (Section 135) made India the first nation to legally mandate corporate social responsibility. Under this law, companies meeting designated financial thresholds (net worth $\ge \text{INR } 500\text{ crore}$, turnover $\ge \text{INR } 1000\text{ crore}$, or net profit $\ge \text{INR } 5\text{ crore}$) must establish a CSR Committee and spend at least $2\%$ of their average net profits made during the preceding three financial years on qualifying social initiatives (eradicating poverty, education, healthcare, environmental sustainability, and rural infrastructure).

2. Archie Carroll's Four-Part Pyramid of CSR:
Archie B. Carroll structured corporate social responsibility into a hierarchical four-tier pyramid:
1. Economic Responsibilities (Base of Pyramid - Required): The foundational duty to be profitable, provide meaningful employment, manufacture goods demanded by consumers, and generate returns for investors. Without economic viability, the enterprise cannot fulfill higher-level responsibilities ($Be profitable$).
2. Legal Responsibilities (Second Tier - Required): The obligation to obey the laws, environmental regulations, labor standards, and consumer protection statutes enacted by local, state, and central governments. Law represents codified social ethics ($Obey the law$).
3. Ethical Responsibilities (Third Tier - Expected): The obligation to do what is right, fair, and just, even when not explicitly codified into written law. Involves respecting community norms, preventing environmental degradation, avoiding deceptive marketing, and treating suppliers fairly ($Be ethical$).
4. Philanthropic Responsibilities (Apex of Pyramid - Desired): Discretionary corporate citizenship activities aimed at actively contributing to the welfare of the broader community through charitable donations, educational sponsorships, and community enrichment programs ($Be a good corporate citizen$).

3. Professional Engineering Ethics:
Engineering ethics is the field of applied philosophy and system of moral principles governing the practice of engineering design, safety, and operational conduct.
- Fundamental Canons of Engineering Ethics (e.g., IEEE / NSPE / IEI Codes):
  1. Engineers shall hold paramount the safety, health, and welfare of the public in the performance of their professional duties.
  2. Engineers shall perform services only in areas of their verified technical competence.
  3. Engineers shall issue public statements only in an objective and truthful manner.
  4. Engineers shall act in professional matters for each employer or client as faithful agents or trustees, scrupulously avoiding conflicts of interest.
  5. Engineers shall build their professional reputation on the merit of their services and shall not compete unfairly.

- Critical Ethical Dilemmas in Engineering:
  - Whistleblowing: The act by an employee of reporting organizational misconduct, safety violations, illegal practices, or imminent public dangers to external regulatory bodies or the public when internal channels have failed to resolve the threat (e.g., the Challenger Space Shuttle O-ring failure warnings). Whistleblowers require clear legal protections against retaliatory termination.
  - Conflict of Interest: A professional situation where an engineer's personal, financial, or familial interests could compromise, or appear to compromise, their impartial judgment in discharging engineering duties (e.g., an engineer recommending a vendor firm in which they hold personal shares). Full disclosure is mandatory.
  - Intellectual Property and Trade Secrets: Respecting nondisclosure agreements (NDAs) and patent rights when transitioning between competing technological firms.
"""
            }
        ]
    },
    {
        "module_id": "mgt-m2",
        "module_num": "Module 2",
        "module_title": "Plant Location, Layout, Work Study & Ergonomics",
        "questions": [
            {
                "qid": "mgt-q6",
                "marks": 7,
                "type": "Descriptive",
                "title": "Plant Location: Factors Influencing Facility Location Decisions and Location Evaluation Models",
                "yt_query": "plant location factors facility selection center of gravity factor rating method",
                "img_path": "images/mgt/plant_location_models.png",
                "img_caption": "Figure 2.1: Primary vs Secondary Location Determinants and Center of Gravity Coordinate Geometry",
                "answer": r"""
Plant location is a strategic long-term capital decision that determines the geographic site for establishing an industrial facility. Selecting an optimal location minimizes the sum of procurement, manufacturing, and distribution costs while maximizing operational responsiveness and customer satisfaction. Once established, relocating a large engineering plant involves catastrophic capital losses.

1. Factors Influencing Plant Location:
- Primary (Direct Cost) Factors:
  1. Proximity to Raw Materials: Essential when raw materials are perishable, bulky, or weight-losing during processing (e.g., steel plants near iron ore and coking coal mines, or sugar mills near sugarcane plantations).
  2. Proximity to Markets: Crucial when the finished product is fragile, perishable, or heavier/bulkier than raw inputs (e.g., beverage bottling, large transformer manufacturing), or when rapid customer service and low distribution freight costs are paramount.
  3. Availability of Reliable Infrastructure and Power: Continuous, un-interrupted high-voltage electrical power, industrial process water, natural gas pipelines, and waste treatment facilities.
  4. Transportation Facilities: Multi-modal connectivity via highways, railway freight corridors, deep-water seaports, and cargo airports.
  5. Availability of Skilled and Unskilled Labor: Sourcing technicians, machinists, and electrical engineers with competitive wage structures and stable industrial relations.
- Secondary (Institutional & Environmental) Factors:
  1. Government Policies and Fiscal Subsidies: Tax holidays, special economic zones (SEZ benefits), capital investment subsidies, and industrial corridor incentives (e.g., Make in India initiatives).
  2. Climate and Topography: Stable seismic zones, absence of flood risks, suitable soil load-bearing capacity for heavy foundations, and favorable ambient temperatures.
  3. Waste Disposal and Environmental Regulations: Stringent pollution control board guidelines for toxic effluent and airborne emissions.
  4. Community and Civic Amenities: Housing, healthcare, technical educational institutions, and public safety.

2. Quantitative Location Evaluation Techniques:
- Factor Rating Method:
A versatile multi-criteria decision tool that incorporates both qualitative and quantitative parameters. The analytical procedure involves:
1. Identifying critical location criteria ($n$ factors, e.g., labor availability, power reliability, transport costs).
2. Assigning a relative importance weight $w_i$ to each factor such that $\sum_{i=1}^n w_i = 1.0$ (or $100\%$).
3. Scoring each candidate site $j$ on a standardized scale (e.g., 1 to 100 points) to yield score $S_{ij}$.
4. Computing the composite Weighted Score ($WS_j$) for each candidate location:
$$WS_j = \sum_{i=1}^n w_i \cdot S_{ij}$$
The site achieving the highest composite score is selected.

- Center of Gravity (Centroid) Method:
Used primarily for locating central distribution warehouses or intermediate processing facilities feeding multiple geographically dispersed supplier sources and retail destination markets.
Let $(x_i, y_i)$ be the geographic coordinates of existing location $i$ (suppliers and markets), and let $W_i$ represent the volume of goods or tonnage transported per year to or from facility $i$.
The optimal coordinates $(X^*, Y^*)$ for the central facility that minimize total transportation tonne-kilometers are determined by the weighted centroids:
$$X^* = \frac{\sum_{i=1}^n x_i \cdot W_i}{\sum_{i=1}^n W_i}, \quad Y^* = \frac{\sum_{i=1}^n y_i \cdot W_i}{\sum_{i=1}^n W_i}$$

- Alfred Weber's Industrial Location Theory:
Weber formulated the Material Index ($MI$):
$$MI = \frac{\text{Weight of Localized Raw Materials Consumed}}{\text{Weight of Finished Product Output}}$$
- If $MI > 1$: The raw materials lose substantial weight during manufacturing (Weight-Losing / Gross Materials). The optimal plant location is pulled strictly toward the Raw Material Source.
- If $MI < 1$: The product gains weight during processing (Weight-Gaining / Ubiquitous Materials like water). The plant is pulled toward the Consumer Market.
- If $MI = 1$: Pure materials; location is indifferent to material or market, governed instead by labor pools or agglomeration economies.
"""
            },
            {
                "qid": "mgt-q7",
                "marks": 7,
                "type": "Descriptive",
                "title": "Plant Layout Types: Product, Process, Fixed-Position, and Cellular (Group Technology) Layouts",
                "yt_query": "plant layout types product process fixed position cellular group technology",
                "img_path": "images/mgt/plant_layout_types.png",
                "img_caption": "Figure 2.2: Physical Floor Plans of Product, Process, Fixed-Position, and Cellular Manufacturing Layouts",
                "answer": r"""
Plant layout is the physical arrangement of industrial machinery, processing equipment, work stations, material storage bays, and service areas within a manufacturing facility. An optimal layout minimizes material handling costs, eliminates processing bottlenecks, shortens total manufacturing throughput time, and ensures safety for operating personnel.

1. Product Layout (Line Layout):
- Architecture: Machines and work stations are arranged strictly along the sequential technological processing path of the product. Raw material enters at one end of the line, moves progressively through dedicated stations (lathe $\to$ milling $\to$ drilling $\to$ grinding $\to$ inspection), and emerges as a finished product at the other end.
- Suitability: High-volume, highly standardized products with steady, continuous demand (e.g., automotive assembly lines, electrical appliance manufacturing, bottling plants).
- Advantages: Extremely low work-in-process (WIP) inventory; smooth, continuous material flow with automated conveyors; minimal material handling distance; short production cycle time; simple production scheduling and inventory control.
- Limitations: Complete lack of operational flexibility (a breakdown of a single machine stops the entire production line); high capital investment in dedicated machinery; monotonous, repetitive tasks for operators.

2. Process Layout (Functional Layout):
- Architecture: Machines of similar technical capability or process function are grouped together into dedicated departments (e.g., all lathes in a turning shop, all milling machines in a milling shop, all welding gear in a welding bay). Products move between functional departments in intermittent batches according to custom routings.
- Suitability: Low-to-medium volume, high variety of non-standardized products manufactured against custom job orders (e.g., custom machine building, tool-and-die shops, aircraft repair facilities).
- Advantages: High flexibility to handle diverse product designs and volume fluctuations; a breakdown of one machine does not halt production (work is redirected to adjacent parallel machines); lower capital investment through general-purpose machines; high job variety for skilled operators.
- Limitations: High material handling cost and complex flow paths; high work-in-process (WIP) inventories waiting in department queues; long manufacturing lead times; difficult production scheduling and tracking.

3. Fixed-Position Layout (Project Layout):
- Architecture: The physical product remains stationary in a fixed geographical dock because of its immense physical size, weight, or fragile nature. Human labor, specialized machine tools, scaffolding, welding equipment, and raw subassemblies are brought to the product site.
- Suitability: Megascale, low-volume engineering projects (e.g., shipbuilding, commercial aircraft construction, steam turbine assembly, civil bridge construction).
- Advantages: Eliminates transportation costs of moving massive completed structures; high product customization; simple organizational structure for a dedicated project team.
- Limitations: Requires extensive open yard space; complex coordination and scheduling of traveling specialized equipment and subcontractors; high material handling of temporary tooling; low equipment utilization.

4. Cellular Layout (Group Technology Layout):
- Architecture: A modern hybrid design combining the high flexibility of a process layout with the high efficiency of a product layout. Parts are analyzed and grouped into Part Families based on geometric design similarities and manufacturing process sequences. Dedicated clusters of dissimilar machines, organized into U-shaped manufacturing cells, are assigned exclusively to produce a specific part family.
- Advantages: Drastically reduces setup times through standardized group tooling; cuts work-in-process (WIP) by $60\% \text{ to } 80\%$; shortens material travel distances; promotes cross-trained autonomous work teams; facilitates Just-In-Time (JIT) workflow.
- Limitations: Requires extensive upfront classification and coding analysis (Group Technology); possible duplication of equipment across multiple parallel cells; reduced machine utilization if product demand fluctuates.
"""
            },
            {
                "qid": "mgt-q8",
                "marks": 7,
                "type": "Descriptive",
                "title": "Work Study: Objectives, Interrelationship between Method Study and Work Measurement, and Method Study Procedure",
                "yt_query": "work study method study work measurement procedure select record examine develop",
                "img_path": "images/mgt/work_study_framework.png",
                "img_caption": "Figure 2.3: Work Study Framework Interlinking Method Study and Work Measurement (Time Study)",
                "answer": r"""
Work Study is a fundamental branch of industrial engineering defined by the International Labour Organization (ILO) as the systematic examination of methods of carrying out activities so as to improve the effective use of resources and to set up standards of performance for the activities being carried out. It aims to eliminate unproductive time, streamline physical workflows, and establish accurate time standards without requiring heavy capital expenditure.

1. Interrelationship between Method Study and Work Measurement:
Work study comprises two interdependent and complementary techniques:
$$\text{Work Study} = \text{Method Study} + \text{Work Measurement}$$
- Method Study (Motion Study): Focuses on the systematic recording and critical examination of existing and proposed ways of doing work, with the aim of developing easier, more effective, and ergonomically superior methods. Its goal is to eliminate unnecessary motions, reduce handling, and optimize workflow. Method study answers: *'How should the work be done?'*
- Work Measurement (Time Study): Focuses on the application of techniques designed to establish the time for a qualified worker to carry out a specified job at a defined level of performance. Work measurement answers: *'How long should the work take?'*

Sequential Relationship:
Method Study must always precede Work Measurement. It is futile and wasteful to establish precise time standards for a job using stopwatches if the underlying operational method is inherently defective, inefficient, or loaded with redundant motions. Once the single best method has been designed and standardized via Method Study, Work Measurement is conducted to establish the Standard Time. This standard time then serves as the scientific foundation for production scheduling, machine capacity planning, labor cost estimation, and incentive wage schemes.

2. Systematic Method Study Procedure:
The execution of a standard method study project follows a disciplined seven-step cycle:
1. SELECT: Choose the job, operation, or process to be studied. Selection is guided by three considerations:
   - Economic: Bottleneck operations with high costs, long delays, or excessive scrap.
   - Technical: Operations undergoing technological obsolescence or frequent machine breakdowns.
   - Human: Heavy physical strain, hazardous conditions, or worker fatigue.
2. RECORD: Record all relevant facts relating to the existing method using standardized process charting techniques (Operation Process Charts, Flow Process Charts, Flow Diagrams, String Diagrams, SIMO Charts). Accurate recording is essential for objective critique.
3. EXAMINE: Critically examine the recorded facts using the structured Questioning Technique:
   - The Purpose: *What is actually done? Why is it done? What else could be done? What should be done?*
   - The Place: *Where is it done? Why there? Where else could it be done? Where should it be done?*
   - The Sequence: *When is it done? Why then? When could it be done? When should it be done?*
   - The Person: *Who does it? Why that person? Who else could do it? Who should do it?*
   - The Means: *How is it done? Why that way? How else could it be done? How should it be done?*
4. DEVELOP: Formulate the new, improved method based on the answers obtained during critical examination. Combine compatible operations, eliminate redundant handling, re-sequence tasks logically, design ergonomic fixtures, and optimize layout.
5. DEFINE: Formulate a detailed Standard Operating Procedure (SOP) documenting the new method, specifying tools, machine settings, materials, workplace layout, and operator movements.
6. INSTALL: Implement the new method as standard practice. Train operating workers and supervisors, and resolve initial transitional glitches.
7. MAINTAIN: Maintain the new standard through routine shop-floor audits to ensure workers do not slip back into outdated, inefficient habits.
"""
            },
            {
                "qid": "mgt-q9",
                "marks": 7,
                "type": "Descriptive",
                "title": "Method Study Recording Techniques: Process Charts, String Diagrams, Multiple Activity Charts, and SIMO Charts",
                "yt_query": "method study process charts flow process chart string diagram SIMO chart therbligs",
                "img_path": "images/mgt/method_study_charts.png",
                "img_caption": "Figure 2.4: ASME Standard Process Charting Symbols and SIMO Chart Format with Therbligs",
                "answer": r"""
To objectively analyze physical workflows, industrial engineers employ standardized graphic recording tools developed under ASME and ILO conventions. Standard process charting uses five fundamental activity symbols:
1. Circle ($\bigcirc$): Operation (intentional modification of physical/chemical properties or addition of information).
2. Arrow ($\Rightarrow$): Transport (movement of workers, materials, or equipment across distances).
3. Square ($\square$): Inspection (verification of quality, dimensions, or quantity against specifications).
4. Capital Letter D ($D$): Delay / Temporary Storage (unplanned waiting or queue in a process).
5. Inverted Triangle ($\nabla$): Permanent Storage (controlled retention in a stockroom requiring authorization to withdraw).
6. Concentric Circle and Square ($\bigodot \! \square$): Combined Activity (operation and inspection performed simultaneously).

1. Operation Process Chart (Outline Process Chart - OPC):
- Characteristics: Provides a high-level bird's-eye view of the entire manufacturing process.
- Content: Records only the major Operations ($\bigcirc$) and Inspections ($\square$) in chronological sequence as raw materials and subassemblies enter the main assembly line. Transports, delays, and storages are excluded.
- Application: Visualizing overall manufacturing logic, comparing structural design alternatives, and planning plant layout expansion.

2. Flow Process Chart (FPC):
- Characteristics: A detailed, step-by-step sequential record of all events occurring during an operation, utilizing all five process chart symbols ($\bigcirc, \Rightarrow, \square, D, \nabla$).
- Three Standard Variations:
  1. Man-Type Flow Process Chart: Records the physical movements and actions of the human operator.
  2. Material-Type Flow Process Chart: Records what happens to the physical raw material as it is processed, handled, and stored.
  3. Equipment-Type Flow Process Chart: Records the operational status, utilization, and idle periods of machinery.
- Summary Block: A standard tabular summary at the bottom of the chart detailing the total count of operations, transports, inspections, delays, and storages, along with total transport distance moved in meters and total process time in minutes. Comparing summaries between the 'Present Method' and 'Proposed Method' demonstrates achieved savings.

3. Flow Diagram and String Diagram:
- Flow Diagram: A scaled floor plan of the manufacturing area showing the exact spatial locations of machines and storage areas, onto which the path of travel of men or materials is drawn using lines and direction arrows. It reveals spatial bottlenecks, backtracking, and traffic cross-overs.
- String Diagram: A scale layout model mounted on a wooden board where miniature pins are driven into machine workstations. A continuous thread or string of known length is wound along the sequential movement path of the worker or material during a full shift. Unwinding and measuring the string gives the exact total physical distance traveled. It is particularly effective for studying multi-machine operators with non-linear, complex movement paths.

4. Multiple Activity Chart (Man-Machine Chart):
- Characteristics: A synchronized multi-column time chart where the concurrent activities of one or more operators and one or more machines are plotted against a common vertical time scale.
- Application: Investigating machine idle time and operator idle time. Identifies opportunities to assign multiple machines to a single operator or to reallocate tasks so that machine setup occurs while the machine is running, thereby maximizing overall equipment effectiveness (OEE).

5. SIMO Chart (Simultaneous Motion Cycle Chart) and Therbligs:
- Characteristics: An ultra-fine micro-motion study chart based on high-speed filming of rapid, repetitive manual operations. It plots the simultaneous activities of the operator's left hand and right hand on a common time scale graduated in winks ($1 \text{ wink} = 1/2000 \text{ minute} = 0.03 \text{ seconds}$).
- Therbligs: Frank Gilbreth divided all manual work into 17 fundamental elemental motions termed Therbligs (Gilbreth spelled backward with 'th' transposed), each assigned a unique name, mnemonic symbol, and color code:
  - Effective Therbligs (value-adding): Reach ($RE$), Grasp ($G$), Move ($M$), Position ($P$), Assemble ($A$), Disassemble ($DA$), Use ($U$), Release Load ($RL$).
  - Ineffective Therbligs (wasteful, to be eliminated): Search ($Sh$), Select ($St$), Hold ($H$), Inspect ($I$), Pre-position ($PP$), Unavoidable Delay ($UD$), Avoidable Delay ($AD$), Plan ($Pn$), Rest for overcoming fatigue ($R$).
- Application: Optimizing high-volume manual assembly tasks (e.g., electronic circuit board component insertion).
"""
            },
            {
                "qid": "mgt-q10",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Work Measurement / Time Study: Observed Time, Performance Rating, Allowances, and Derivation of Standard Time",
                "yt_query": "time study derivation standard time normal time performance rating allowances numerical",
                "img_path": "images/mgt/time_study_derivation.png",
                "img_caption": "Figure 2.5: Chronological Buildup from Observed Time to Normal Time and Final Standard Time",
                "answer": r"""
Work Measurement (specifically Stopwatch Time Study) is the industrial engineering discipline of establishing the standard time required by a qualified, well-trained operator working at a standard pace under specified workplace conditions to complete a unit of production.

1. Chronological Steps in Conducting a Time Study:
1. Decomposing Job into Distinct Work Elements: The total operational cycle is broken down into small, measurable, homogeneous work elements with clearly identifiable visual and audible start and end breakpoints.
2. Timing the Elements: A trained observer times each element over a statistically valid number of cycles ($N$ observations) using continuous or snapback stopwatch timing, calculating the mean Observed Time ($OT$).
3. Performance Rating ($PR$): The observer evaluates the operator's actual working pace relative to a conceptual Standard Pace ($100\%$ on standard scale) based on speed, rhythm, and dexterity.
4. Computation of Normal Time ($NT$): Normalizing the observed time by the performance rating factor.
5. Determination of Allowances: Allocating percentage additions for relaxation, personal hygiene, unavoidable delays, and fatigue.
6. Computation of Standard Time ($ST$): Adding allowances to the normal time.

2. Mathematical Formulation and Derivation of Standard Time:
- Observed Time ($OT$):
For an elemental task observed over $n$ representative cycles, let $t_i$ be the observed clock time for cycle $i$. The arithmetic average Observed Time is:
$$OT = \bar{t} = \frac{1}{n} \sum_{i=1}^n t_i$$

- Normal Time ($NT$ or Basic Time):
Because operating workers may work faster or slower than a standard pace, Observed Time cannot serve as the production standard. Performance Rating Factor ($RF$) is applied. On the standard $100\%$ scale (Westinghouse or ILO rating):
$$NT = OT \times \left( \frac{\text{Observed Performance Rating } (PR)}{100} \right)$$
- If an operator works faster than standard ($PR = 120\% = 1.20$), their normal time is longer than observed time ($NT = 1.20 \times OT$).
- If an operator works slower ($PR = 80\% = 0.80$), their normal time is shorter ($NT = 0.80 \times OT$).

- Total Normal Time for a Multi-Element Job:
For a job comprising $m$ distinct work elements:
$$NT_{total} = \sum_{j=1}^m NT_j = \sum_{j=1}^m \left[ OT_j \times \left(\frac{PR_j}{100}\right) \right]$$

- Allowances ($A$):
No human operator can maintain a continuous standard pace for eight hours without experiencing physical fatigue or personal interruption. Allowances are allocated as a percentage ($A\%$) of Normal Time:
1. Personal Needs Allowance ($5\%$ for males, $7\%$ for females: drinking water, restroom).
2. Basic Fatigue Allowance ($4\%$ for basic psychological and physical recovery).
3. Variable Fatigue Allowance (posture stress, extreme heat, heavy muscular load, visual strain).
4. Contingency Allowance ($< 5\%$ for occasional tool adjustments, machine oiling).
5. Policy / Interference Allowance (waiting for materials or crane service).

- Derivation of Standard Time ($ST$):
Standard Time is defined as the total allowable time allocated to complete a unit of work. Adding total percentage allowances ($A = \sum a_k\%$) to the total Normal Time yields:
$$ST = NT_{total} + \text{Allowances} = NT_{total} + (NT_{total} \times A)$$
$$\mathbf{ST = NT_{total} \times (1 + A)}$$
where $A$ is expressed as a decimal fraction of Normal Time (e.g., $15\% \implies A = 0.15$).

---
NUMERICAL PROBLEM (KTU Examination Model):
An industrial engineer conducts a stopwatch time study on an electric motor rotor assembly workstation. The operation comprises four repetitive elements. The observed times and performance ratings recorded over 50 cycles, together with negotiated factory allowances, are tabulated below:

| Element | Description | Observed Time ($OT$, min) | Performance Rating ($PR$) |
|---|---|---|---|
| 1 | Pick rotor and mount on jig | $0.45$ | $110\%$ |
| 2 | Wind copper wire bundle | $1.20$ | $105\%$ |
| 3 | Solder terminal lead connections | $0.60$ | $90\%$ |
| 4 | Dismount and place in bin | $0.25$ | $100\%$ |

Company policy allocates the following allowances expressed as percentages of Normal Time:
- Personal and Basic Fatigue allowance: $9\%$
- Muscular load and heat stress allowance: $4\%$
- Unavoidable tool maintenance contingency: $3\%$
Calculate:
(a) The Normal Time ($NT$) for each element and the total Normal Time ($NT_{total}$).
(b) The total percentage allowance ($A\%$) and the final Standard Time ($ST$) for the assembly operation in minutes.
(c) The standard hourly production rate (units per hour).

SOLUTION STEP-BY-STEP:
Step 1: Calculate Normal Time ($NT$) for each elemental task:
$$NT_1 = 0.45 \times \frac{110}{100} = 0.45 \times 1.10 = 0.495\text{ minutes}$$
$$NT_2 = 1.20 \times \frac{105}{100} = 1.20 \times 1.05 = 1.260\text{ minutes}$$
$$NT_3 = 0.60 \times \frac{90}{100} = 0.60 \times 0.90 = 0.540\text{ minutes}$$
$$NT_4 = 0.25 \times \frac{100}{100} = 0.25 \times 1.00 = 0.250\text{ minutes}$$

Step 2: Sum elemental normal times to obtain total Normal Time:
$$NT_{total} = 0.495 + 1.260 + 0.540 + 0.250 = 2.545\text{ minutes}$$

Step 3: Calculate total allowances:
$$A = 9\% + 4\% + 3\% = 16\% = 0.16$$
Allowance time in minutes:
$$\text{Allowance Time} = NT_{total} \times A = 2.545 \times 0.16 = 0.4072\text{ minutes}$$

Step 4: Compute Standard Time ($ST$):
$$ST = NT_{total} \times (1 + A) = 2.545 \times (1 + 0.16) = 2.545 \times 1.16 \approx 2.9522\text{ minutes}$$

Step 5: Compute standard hourly production quota:
$$\text{Production Rate} = \frac{60\text{ minutes per hour}}{ST} = \frac{60}{2.9522} \approx 20.32 \approx 20 \text{ assembled rotors per hour}$$

Final highlighted results:
$$\mathbf{NT_{total} = 2.545\text{ min}}, \quad \mathbf{ST = 2.952\text{ min}}, \quad \mathbf{\text{Standard Output} = 20.32\text{ units/hour}}$$
"""
            }
        ]
    },
    {
        "module_id": "mgt-m3",
        "module_num": "Module 3",
        "module_title": "Materials Management, Inventory Control & Quality Engineering",
        "questions": [
            {
                "qid": "mgt-q11",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Economic Order Quantity (EOQ): Mathematical Derivation of Wilson's Lot Size Formula and Total Cost Curves",
                "yt_query": "economic order quantity EOQ derivation total cost curve inventory formula",
                "img_path": "images/mgt/eoq_cost_curves.png",
                "img_caption": "Figure 3.1: Annual Inventory Cost Curves Showing Minimization of Total Cost at EOQ",
                "answer": r"""
Materials management is a core engineering management function responsible for planning, procuring, storing, and controlling direct material flows to support uninterrupted manufacturing schedules while minimizing capital tied up in inventory.

1. Concept of Economic Order Quantity (EOQ):
Invented by Ford Whitman Harris in 1913 and popularized by R.H. Wilson, the Economic Order Quantity (EOQ) is the optimal replenishment order batch size ($Q^*$) that minimizes the Total Annual Inventory Cost ($TIC$) by balancing two opposing cost curves:
1. Annual Ordering (or Setup) Cost: Decreases monotonically as order quantity $Q$ increases, because fewer total replenishment orders are placed during the year.
2. Annual Inventory Holding (or Carrying) Cost: Increases linearly with order quantity $Q$, because larger batch sizes result in higher average physical inventory in the warehouse.

2. Assumptions of Classical Wilson EOQ Model:
1. Annual demand rate $D$ is constant, uniform, and known with deterministic certainty.
2. Replenishment lead time $L$ is zero or constant (instantaneous delivery without shortages).
3. Unit purchase price $C$ is constant regardless of order quantity (no quantity discounts).
4. Ordering cost per order $S$ is constant and independent of the order quantity.
5. Holding cost per unit per year $H$ is constant ($H = C \times i$, where $i$ is the annual carrying cost fraction).
6. Stockouts, backorders, and shortages are not permitted.

3. Mathematical Formulation and Derivation:
Let:
- $D$ = Total annual demand for the item (units/year),
- $Q$ = Replenishment order quantity per batch (units/order),
- $S$ = Ordering cost per order ($\text{INR}$/order) or setup cost per production run,
- $H$ = Inventory holding cost per unit per year ($\text{INR}$/unit/year),
- $C$ = Unit purchase price of the item ($\text{INR}$/unit).

Step 1: Annual Ordering Cost ($AOC$):
The total number of replenishment purchase orders placed per year is:
$$N = \frac{D}{Q}$$
Multiplying by the fixed cost per order $S$:
$$AOC = \left(\frac{D}{Q}\right) \cdot S = \frac{D S}{Q}$$

Step 2: Annual Carrying / Holding Cost ($AHC$):
Under uniform consumption and instantaneous replenishment, the inventory level follows a classical sawtooth profile, dropping linearly from a peak of $Q$ down to $0$. The average inventory level held in stock throughout the year is:
$$\bar{I} = \frac{Q + 0}{2} = \frac{Q}{2}$$
Multiplying by the holding cost per unit per year $H$:
$$AHC = \left(\frac{Q}{2}\right) \cdot H = \frac{Q H}{2}$$

Step 3: Total Annual Inventory Cost ($TIC$):
Total variable annual cost is the sum of annual ordering cost and annual holding cost:
$$TIC(Q) = AOC + AHC = \frac{D S}{Q} + \frac{Q H}{2}$$

Step 4: Optimization using First-Order Calculus:
To find the order quantity $Q$ that minimizes total cost, we differentiate $TIC(Q)$ with respect to $Q$ and equate the derivative to zero:
$$\frac{d(TIC)}{dQ} = \frac{d}{dQ} \left( D S Q^{-1} + \frac{H}{2} Q \right) = -D S Q^{-2} + \frac{H}{2} = -\frac{D S}{Q^2} + \frac{H}{2} = 0$$
Rearranging the equality:
$$\frac{H}{2} = \frac{D S}{Q^2}$$
Note: This equality proves that at the optimal economic order quantity, the Annual Holding Cost exactly equals the Annual Ordering Cost:
$$AHC = AOC$$
Solving explicitly for the optimal order quantity $Q^*$:
$$Q^2 = \frac{2 D S}{H} \implies Q^* = \sqrt{\frac{2 D S}{H}}$$
This is the celebrated Wilson Economic Order Quantity Formula:
$$\mathbf{EOQ = Q^* = \sqrt{\frac{2 D S}{H}}}$$

Step 5: Verification of Second-Order Condition (Sufficiency):
Differentiating a second time with respect to $Q$:
$$\frac{d^2(TIC)}{dQ^2} = \frac{d}{dQ} \left( -D S Q^{-2} + \frac{H}{2} \right) = +2 D S Q^{-3} = \frac{2 D S}{Q^3}$$
Because demand $D > 0$, order cost $S > 0$, and order size $Q > 0$, the second derivative is strictly positive:
$$\frac{d^2(TIC)}{dQ^2} > 0 \quad (\forall Q > 0)$$
This proves mathematically that $Q^*$ strictly minimizes total annual inventory cost.

Step 6: Minimum Total Variable Inventory Cost ($TIC^*$):
Substituting $Q^* = \sqrt{\frac{2DS}{H}}$ into the $TIC$ expression:
$$TIC^* = \frac{D S}{\sqrt{\frac{2DS}{H}}} + \frac{H}{2} \sqrt{\frac{2DS}{H}} = \sqrt{\frac{D^2 S^2 H}{2 D S}} + \sqrt{\frac{H^2 \cdot 2 D S}{4 H}} = \sqrt{\frac{D S H}{2}} + \sqrt{\frac{D S H}{2}} = 2 \sqrt{\frac{D S H}{2}}$$
$$\mathbf{TIC^* = \sqrt{2 D S H}}$$
Total Annual Cost including direct purchase material cost ($D \times C$) is:
$$TC_{total} = (D \cdot C) + \sqrt{2 D S H}$$
"""
            },
            {
                "qid": "mgt-q12",
                "marks": 7,
                "type": "Descriptive",
                "title": "Selective Inventory Control Techniques: ABC Analysis (Pareto Principle), VED, FSN, and SDE Analyses",
                "yt_query": "ABC analysis inventory control pareto 80 20 rule VED FSN SDE analysis",
                "img_path": "images/mgt/abc_inventory_curve.png",
                "img_caption": "Figure 3.2: ABC Inventory Classification Curve Based on Pareto's Law of Cumulative Annual Consumption",
                "answer": r"""
In an industrial manufacturing enterprise stocking tens of thousands of individual spare parts, raw materials, and assemblies, it is operationally impossible and economically irrational to exercise the same degree of stringent inventory control over every single item. Selective Inventory Control classifies inventory items into discrete categories based on distinct operational criteria, applying appropriate management rigor to each category.

1. ABC Analysis (Always Better Control):
- Theoretical Foundation: Based on the Pareto Principle (the 80/20 Rule) formulated by Italian economist Vilfredo Pareto. In materials management, the rule states that a small percentage of inventory items account for the vast majority of total annual monetary consumption.
- Classification Parameter: Annual Consumption Value ($ACV$), computed for each item $i$ as:
$$ACV_i = \text{Annual Demand } (D_i) \times \text{Unit Cost } (C_i)$$
- Category Definitions:
  1. Category A Items (High Value, Low Volume): Represent only approximately $10\% \text{ to } 20\%$ of total inventory item counts, but account for a staggering $70\% \text{ to } 80\%$ of total cumulative annual consumption value.
  2. Category B Items (Moderate Value, Moderate Volume): Represent approximately $20\% \text{ to } 30\%$ of total item counts, and account for $15\% \text{ to } 25\%$ of annual consumption value.
  3. Category C Items (Low Value, High Volume): Represent the vast bulk of physical items ($50\% \text{ to } 70\%$ of item counts, such as standard washers, bolts, nuts, cotter pins), but account for merely $5\% \text{ to } 10\%$ of annual expenditure.

- Management Control Policies across ABC Categories:
| Management Parameter | Category A Items | Category B Items | Category C Items |
|---|---|---|---|
| Control Rigor | Extremely tight, high managerial oversight | Moderate, periodic review | Simple, visual rule-of-thumb control |
| Ordering System | Frequent small orders (JIT / MRP) | Periodic replenishment orders | Bulk ordering (Two-bin system, 6-month supply) |
| Safety Stock | Kept strictly minimal to avoid locked capital | Moderate safety stock | Generous safety stock to eliminate stockouts |
| Stock Verification | Continuous / weekly perpetual audits | Monthly cycle counting | Annual physical stock verification |
| Authority Level | Senior Purchase / Plant Manager | Assistant Purchase Officer | Storekeeper / Purchase Assistant |

2. VED Analysis (Vital, Essential, Desirable):
- Classification Parameter: Criticality of the item to continuous plant production and maintenance operations (specifically applied to maintenance, repair, and operating - MRO spare parts).
- Categories:
  - Vital ($V$): Spares whose absence causes immediate, total plant shutdown or grave safety hazards (e.g., main turbine bearings, high-voltage transformer bushings). No lead-time delay is acceptable; generous safety stocks are maintained regardless of cost.
  - Essential ($E$): Spares whose absence causes serious production slowdown or minor system degradation, but where temporary bypasses or substitutes can be arranged for a few hours/days.
  - Desirable ($D$): Spares whose absence does not disrupt production in the short run; non-availability causes minor inconvenience only.

3. FSN Analysis (Fast-moving, Slow-moving, Non-moving):
- Classification Parameter: Rate of stock movement and inventory turnover ratio across a given financial year.
- Categories:
  - Fast-Moving ($F$): Items frequently requisitioned and consumed in rapid cycles; stock turnover is high. Requires continuous replenishment tracking.
  - Slow-Moving ($S$): Items consumed irregularly over long intervals. Stocks are strictly controlled to prevent capital locking.
  - Non-Moving ($N$): Dead stock that has experienced zero requisitions over the past 12 to 24 months. Subject to obsolescence review and liquidative disposal.

4. SDE Analysis (Scarce, Difficult, Easy):
- Classification Parameter: Procurement lead time and geographical market availability.
- Categories:
  - Scarce ($S$): Imported components, government-rationed canalized raw materials, or items with global supply shortages; requires long-term forward purchasing and buffer reserves.
  - Difficult ($D$): Items available only from specialized domestic manufacturers located far from the plant with lead times of several weeks.
  - Easy ($E$): Readily available off-the-shelf items from local suppliers with same-day or next-day delivery.
"""
            },
            {
                "qid": "mgt-q13",
                "marks": 7,
                "type": "Descriptive",
                "title": "Just-In-Time (JIT) Manufacturing, Seven Wastes (Muda), Kanban Pull System, and JIT vs MRP Comparison",
                "yt_query": "just in time JIT toyota production system seven wastes muda kanban push vs pull MRP",
                "img_path": "images/mgt/jit_kanban_system.png",
                "img_caption": "Figure 3.3: The Toyota Kanban Dual-Card Pull Loop and River Analogy of Waste Elimination",
                "answer": r"""
Just-In-Time (JIT) is an integrated operations management philosophy developed by Taiichi Ohno and Shigeo Shingo at Toyota Motor Corporation (known broadly as the Toyota Production System - TPS). JIT is defined as an operational strategy dedicated to producing only what is needed, at the exact time it is needed, and in the exact quantity needed, with zero waste and zero defect tolerance.

1. The River Analogy and Elimination of Seven Wastes (Muda):
In traditional manufacturing, high levels of inventory are deliberately maintained like water in a deep river to hide underlying submerged operational rocks (machine breakdowns, quality defects, long setup times, unreliable vendors, and worker absenteeism). JIT lowers the water level (reduces inventory toward zero) to expose the rocks so they can be permanently removed through root-cause engineering solutions.
Taiichi Ohno classified industrial waste ($Muda$ - any enterprise activity that consumes time and resources without adding value from the customer's perspective) into Seven Cardinal Categories:
1. Waste of Overproduction: Producing items before they are ordered or producing in excess of current customer demand. Considered by Ohno to be the root of all other wastes because it locks up capital and necessitates extra warehousing, handling, and defect hiding.
2. Waste of Waiting: Machine idle time, operator delays awaiting raw materials, inspection delays, or waiting for upstream station processing.
3. Waste of Transportation: Unnecessary physical transit, handling, and relocalizing of raw materials and assemblies between departments and warehouses.
4. Waste of Over-Processing: Performing unnecessary, non-value-adding precision steps or cosmetic finishes beyond the functional specifications required by the customer.
5. Waste of Inventory: Excess raw materials, excessive work-in-process (WIP) stacked between workstations, and excess finished goods tied up in storage.
6. Waste of Motion: Unnecessary, awkward, or non-ergonomic operator movements (bending, stretching, reaching, searching for tools).
7. Waste of Defects: Producing scrapped parts or defective components requiring expensive rework, salvage, customer warranty replacements, and inspection.

2. The Kanban System (The Pull Mechanism):
Traditional manufacturing operates on a Push System (MRP): central computers schedule production based on long-range forecasts, pushing work onto the next downstream department regardless of whether that station is ready.
JIT operates on a Pull System: downstream stations withdraw parts from upstream stations only as they are consumed by actual customer demand. The physical signaling mechanism that coordinates this pull workflow is the Kanban (a Japanese term meaning *'visual sign' or 'signal card'*).

Operation of Dual-Card Kanban System:
The system uses two dedicated cards:
1. Production Kanban (P-Kanban): Authorizes an upstream workstation to manufacture a standard container of specified parts.
2. Withdrawal / Conveyance Kanban (C-Kanban): Authorizes the material handler to transport a standard container of parts from the upstream output store to the downstream workstation.

Execution Cycle:
When an operator at Downstream Station $B$ consumes the first part from a standardized container, the attached C-Kanban is detached and placed in a withdrawal post. A material handler collects the C-Kanban, travels to the Upstream Station $A$ output storage rack, attaches the C-Kanban to a full container of finished parts, and detaches the existing P-Kanban from that container. The detached P-Kanban is left at Station $A$, serving as the direct visual production authorization order for Station $A$ to manufacture another single container of parts. Without an active P-Kanban, Station $A$ is forbidden to produce any parts. Thus, overproduction is structurally impossible.
The required number of Kanban containers $k$ circulating in the loop is calculated from:
$$k = \frac{D \cdot L (1 + \alpha)}{C}$$
where $D$ is consumption rate, $L$ is lead time, $\alpha$ is safety factor, and $C$ is standard container capacity.

3. JIT (Pull) vs Traditional MRP (Push) Systems:
| Feature | Traditional MRP System (Push) | Just-In-Time System (Pull) |
|---|---|---|
| Production Trigger | Long-range master forecast | Actual downstream customer demand |
| Inventory Philosophy | High safety stock ('Just-in-Case') | Zero inventory ('Just-in-Time') |
| Lot Sizing | Large economic batch sizes | Single-piece flow / small lot sizes |
| Machine Setup Time | Long setups accepted as inevitable | Rapid setups (SMED: Single Minute Exchange of Die) |
| Quality Philosophy | Acceptable Quality Level (AQL) | Zero Defects (Poka-Yoke / Jidoka automatic stop) |
| Supplier Relationships | Multiple adversarial bidding vendors | Few long-term trusted partner suppliers |
"""
            },
            {
                "qid": "mgt-q14",
                "marks": 7,
                "type": "Descriptive",
                "title": "Total Quality Management (TQM), Deming's 14 Points, PDCA Cycle, Six Sigma (DMAIC), and ISO 9001 Standards",
                "yt_query": "total quality management TQM deming 14 points PDCA six sigma DMAIC ISO 9001",
                "img_path": "images/mgt/tqm_six_sigma_dmaic.png",
                "img_caption": "Figure 3.4: The Deming PDCA Improvement Cycle and the Five Sequential Phases of Six Sigma DMAIC",
                "answer": r"""
Quality is defined in engineering management as fitness for intended purpose, conformance to design specifications, and freedom from variation. Modern quality engineering evolved from end-of-line post-production inspection to holistic, company-wide Total Quality Management (TQM) and data-driven Six Sigma architectures.

1. Total Quality Management (TQM) & Core Principles:
TQM is an organization-wide management philosophy dedicated to continuous improvement across all business processes, products, and services through the active involvement of all employees at all levels to achieve complete customer satisfaction.
Core Pillars of TQM:
- Customer Focus: The internal or external customer is the ultimate arbiter of quality.
- Continuous Process Improvement ($Kaizen$): Small, incremental, continuous enhancements to eliminate process waste.
- Total Employee Empowerment: Training shop-floor workers in quality circles to identify and solve operational defects.
- Fact-Based Decision Making: Utilizing statistical data rather than intuition to drive process modifications.

2. W. Edwards Deming's Contributions:
W. Edwards Deming, an American statistician who transformed post-war Japanese industry, formulated the classical 14 Points for Management, including:
- Create constancy of purpose toward improvement of product and service.
- Cease dependence on mass inspection; build quality into the product in the first place.
- End the practice of awarding business on the basis of price tag alone; move toward single trusted suppliers.
- Drive out fear so that everyone may work effectively for the company.
- Break down barriers between departments; work as cross-functional teams.
- Eliminate numerical quotas and management by arbitrary numeric objectives.

The Deming Wheel / PDCA Cycle:
A continuous four-phase quality improvement loop:
1. PLAN ($P$): Identify a problem, gather baseline data, analyze root causes using Ishikawa Cause-and-Effect diagrams, and formulate an improvement plan.
2. DO ($D$): Implement the proposed solution on a small experimental pilot scale.
3. CHECK ($C$): Measure the results of the pilot change; evaluate if process performance improved.
4. ACT ($A$): If successful, standardize the new procedure enterprise-wide; if unsuccessful, revise the plan and begin the cycle anew.

3. Six Sigma Methodology:
Pioneered by Bill Smith at Motorola in 1986 and popularized by Jack Welch at General Electric, Six Sigma is a disciplined, data-driven statistical methodology aimed at reducing process variation and eliminating defects.
Statistical Definition:
A process operating at Six Sigma capability produces a process distribution where the nearest customer specification limit (USL or LSL) is six standard deviations ($6\sigma$) away from the process mean ($\mu$). Even under a standard long-term mean shift of $\pm 1.5\sigma$, a Six Sigma process achieves a defect rate of:
$$\text{Defect Rate} = 3.4 \text{ Defects Per Million Opportunities (DPMO)}$$
This corresponds to a $99.99966\%$ success rate (virtually zero defect manufacturing).

The DMAIC Improvement Framework:
For existing underperforming processes, Six Sigma executes the 5-phase DMAIC methodology:
1. DEFINE: Define the business problem, critical-to-quality (CTQ) customer requirements, project charter, and process boundaries.
2. MEASURE: Map the process in detail, validate the measurement system (Gage R&R study), and gather accurate baseline defect data to establish current process capability ($C_p, C_{pk}$).
3. ANALYZE: Conduct statistical analysis (ANOVA, Regression, Hypothesis Testing, Pareto Analysis) to isolate root causes of variation.
4. IMPROVE: Design, test, and implement robust solutions to eliminate root causes; optimize settings using Design of Experiments (DOE).
5. CONTROL: Establish standard operating procedures, mistake-proofing fixtures ($Poka-Yoke$), and Statistical Process Control (SPC) control charts to sustain gains over time.

4. ISO 9001 Quality Management System (QMS):
ISO 9001, published by the International Organization for Standardization, is the premier international standard setting out requirements for a certified Quality Management System. It is built upon seven quality management principles: Customer focus, Leadership, Engagement of people, Process approach, Continuous improvement, Evidence-based decision-making, and Relationship management. ISO 9001 certification audits verify that an organization documents its processes, consistently adheres to documented standards, and maintains rigorous corrective and preventive action (CAPA) systems.
"""
            },
            {
                "qid": "mgt-q15",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Statistical Quality Control (SQC): Control Charts for Variables (X-bar & R) and Attributes, Process Capability (Cp & Cpk)",
                "yt_query": "statistical quality control control charts X bar R chart p chart process capability Cp Cpk derivation",
                "img_path": "images/mgt/sqc_control_charts.png",
                "img_caption": "Figure 3.5: Statistical Control Chart Boundaries (UCL, CL, LCL) and Normal Curve Process Capability",
                "answer": r"""
Statistical Quality Control (SQC) is the application of statistical methods to monitor, control, and improve the quality of manufacturing operations. Pioneered by Walter A. Shewhart at Bell Telephone Laboratories in 1924, Statistical Process Control (SPC) distinguishes between two sources of process variation:
1. Chance (Common) Causes of Variation: Inherent, random, unavoidable background noise in the process (e.g., minute micro-vibrations, minor ambient temperature fluctuations). When only common causes are present, the process is in a state of Statistical Control.
2. Assignable (Special) Causes of Variation: Specific, identifiable, and rectifiable disruptive factors (e.g., machine tool wear, incorrect operator setup, batch-to-batch raw material defect). When assignable causes arise, the process is Out of Control and requires immediate diagnostic intervention.

1. Shewhart Control Chart Architecture:
A control chart consists of three horizontal reference lines derived from statistical normal distribution theory:
- Upper Control Limit ($UCL$): Set at $\mu + 3\sigma$,
- Center Line ($CL$): Set at process mean $\mu$,
- Lower Control Limit ($LCL$): Set at $\mu - 3\sigma$.
By the properties of the Gaussian normal distribution, $99.73\%$ of all sample statistics will fall within these $\pm 3\sigma$ control limits if the process is operating under chance causes alone. Any sample point plotting outside the limits indicates an assignable cause ($p < 0.0027$).

2. Control Charts for Variables: $\bar{X}$ and $R$ Charts:
Used when quality characteristics are continuous physical measurements (e.g., shaft diameter in millimeters, electrical resistance in ohms). Samples of size $n$ (typically $n = 4 \text{ to } 6$) are drawn across $m$ successive subgroups.
- Range Chart ($R$-Chart): Monitors process dispersion (variability):
For each subgroup $j$, sample range is $R_j = X_{\max} - X_{\min}$.
Mean range is:
$$\bar{R} = \frac{1}{m} \sum_{j=1}^m R_j$$
Control limits for $R$-chart (using standard Shewhart factors $D_3$ and $D_4$):
$$UCL_R = D_4 \bar{R}, \quad CL_R = \bar{R}, \quad LCL_R = D_3 \bar{R}$$

- Mean Chart ($\bar{X}$-Chart): Monitors process central tendency:
For each subgroup $j$, sample mean is $\bar{X}_j = \frac{1}{n} \sum_{i=1}^n X_{ij}$.
Grand mean is:
$$\bar{\bar{X}} = \frac{1}{m} \sum_{j=1}^m \bar{X}_j$$
Control limits for $\bar{X}$-chart (using Shewhart factor $A_2$):
$$UCL_{\bar{X}} = \bar{\bar{X}} + A_2 \bar{R}, \quad CL_{\bar{X}} = \bar{\bar{X}}, \quad LCL_{\bar{X}} = \bar{\bar{X}} - A_2 \bar{R}$$

3. Control Charts for Attributes:
Used when items are classified discretely as conforming/non-conforming (good/bad) or by counting defect instances:
- $p$-Chart: Fraction non-conforming (defective) for varying or constant sample sizes:
$$\bar{p} = \frac{\text{Total defective units across all samples}}{\text{Total units inspected}}$$
$$UCL_p = \bar{p} + 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}, \quad CL_p = \bar{p}, \quad LCL_p = \max\left\{0, \, \bar{p} - 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}\right\}$$
- $c$-Chart: Total count of defects per single complex inspection unit (Poisson model with mean count $\bar{c}$):
$$UCL_c = \bar{c} + 3\sqrt{\bar{c}}, \quad CL_c = \bar{c}, \quad LCL_c = \max\left\{0, \, \bar{c} - 3\sqrt{\bar{c}}\right\}$$

4. Process Capability Analysis ($C_p$ and $C_{pk}$):
Process capability measures the intrinsic ability of a stable manufacturing process (free of assignable causes) to produce output strictly within external customer specification limits: Upper Specification Limit ($USL$) and Lower Specification Limit ($LSL$).
The Natural Tolerance Spread of a process is $6\sigma$, where $\sigma \approx \frac{\bar{R}}{d_2}$.
- Process Capability Ratio ($C_p$):
Measures potential capability assuming the process is centered exactly between specification limits:
$$C_p = \frac{\text{Allowable Specification Spread}}{\text{Actual Process Spread}} = \frac{USL - LSL}{6\sigma}$$
- If $C_p > 1.33$: The process is fully capable.
- If $C_p = 1.0$: Marginal capability (specification spread equals natural spread).
- If $C_p < 1.0$: Process is incapable; defects are generated even if centered.

- Process Capability Index ($C_{pk}$):
Accounts for actual off-center shifts of the process mean $\mu$:
$$C_{pk} = \min\left[ C_{pu}, \, C_{pl} \right] = \min\left[ \frac{USL - \mu}{3\sigma}, \, \frac{\mu - LSL}{3\sigma} \right]$$
A process is truly capable only if $C_{pk} \ge 1.33$. If a process is centered, $C_{pk} = C_p$; if shifted off-center, $C_{pk} < C_p$.
"""
            }
        ]
    },
    {
        "module_id": "mgt-m4",
        "module_num": "Module 4",
        "module_title": "Marketing Management & Human Resource Management",
        "questions": [
            {
                "qid": "mgt-q16",
                "marks": 7,
                "type": "Descriptive",
                "title": "Marketing Management: Core Concepts, the Marketing Mix (4 Ps & 7 Ps), and the STP Strategic Framework",
                "yt_query": "marketing management marketing mix 4 Ps 7 Ps STP segmentation targeting positioning",
                "img_path": "images/mgt/marketing_mix_stp.png",
                "img_caption": "Figure 4.1: The STP Strategic Marketing Funnel and the Expanded 7 Ps Marketing Mix Model",
                "answer": r"""
Marketing management is the art and science of choosing target markets and getting, keeping, and growing customers through creating, delivering, and communicating superior customer value. Unlike selling (which focuses on pushing manufactured factory products to convert inventory into cash), modern marketing focuses on identifying unmet consumer needs and designing products to satisfy those needs profitably.

1. The Classical Marketing Mix (The 4 Ps of Product Marketing):
Formulated by E. Jerome McCarthy and popularized by Philip Kotler, the Marketing Mix represents the set of controllable tactical marketing tools that the firm blends to produce the response it wants in the target market:
1. Product: The physical good or intangible service offered to the market, incorporating functional design, technical features, quality levels, brand naming, packaging, warranties, and after-sales service policies.
2. Price: The monetary amount customers must pay to obtain the product. Pricing strategies include:
   - Cost-Plus Pricing (adding a standard markup over production cost),
   - Penetration Pricing (setting a low initial price to rapidly capture market share),
   - Price Skimming (setting a high initial price to skim maximum revenue from early adopters before competitors enter).
3. Place (Distribution): The institutional distribution channels and logistics systems through which the product moves from manufacturer to consumer. Encompasses channel design (direct sales, wholesalers, distributors, retail dealerships), warehouse locations, inventory management, and transport logistics.
4. Promotion: The integrated marketing communications (IMC) suite used to inform, persuade, and remind buyers about the product. Includes Advertising, Personal Selling, Public Relations (PR), Direct Digital Marketing, and Sales Promotions (rebates, discounts).

2. Expanded Marketing Mix for Services (The 7 Ps):
Because services are intangible, inseparable, variable, and perishable, Booms and Bitner expanded the traditional 4 Ps framework by adding three additional elements:
5. People: All human actors who play a role in service delivery and thus influence the buyer's perceptions (e.g., technical support engineers, customer care representatives, sales personnel).
6. Process: The actual operational procedures, mechanisms, and flow of activities by which the service is delivered (e.g., seamless online checkout, rapid technical trouble-ticketing workflows).
7. Physical Evidence: The physical environment in which the service is delivered, along with tangible artifacts that facilitate or communicate the quality of the service (e.g., modern corporate offices, clean service stations, branded documentation).

3. The STP Strategic Marketing Framework:
The STP framework constitutes the cornerstone of modern strategic marketing:
1. Segmentation ($S$): Dividing a heterogeneous mass market into distinct, homogeneous subsets of consumers possessing similar needs, characteristics, or behavioral patterns. Segmentation bases include:
   - Geographic (country, state, urban/rural climate),
   - Demographic (age, income, occupation, education, family size),
   - Psychographic (lifestyle, social class, personality values),
   - Behavioral (usage rate, brand loyalty, purchase occasion, benefits sought).
2. Targeting ($T$): Evaluating the commercial attractiveness of each identified market segment (market size, growth rate, structural profitability, competitive rivalry) and selecting one or more target segments to enter. Target strategies include Undifferentiated (mass marketing), Differentiated (distinct offerings for separate segments), or Concentrated (niche marketing).
3. Positioning ($P$): The act of designing the company's offering and brand image to occupy a distinctive, desirable place in the mind of the target consumer relative to competing offerings (e.g., Volvo positioned as 'Safety', Apple as 'Premium Design & Innovation'). Formulated via Positioning Maps (Perceptual Maps).
"""
            },
            {
                "qid": "mgt-q17",
                "marks": 7,
                "type": "Descriptive",
                "title": "Product Life Cycle (PLC): Stages, Characteristics, Sales-Profit Curves, and Strategic Responses",
                "yt_query": "product life cycle PLC stages introduction growth maturity decline marketing strategy",
                "img_path": "images/mgt/product_life_cycle_curves.png",
                "img_caption": "Figure 4.2: Product Life Cycle (PLC) Sales and Profit Trajectories Across Four Distinct Stages",
                "answer": r"""
The Product Life Cycle (PLC) concept asserts that commercial products, like biological organisms, pass through a sequence of identifiable phases from initial market introduction to eventual obsolescence and withdrawal. Tracking a product's position along the PLC enables engineering and marketing managers to anticipate market dynamics, reallocate capital investments, and modify product design and pricing strategies.

1. Stages of the Product Life Cycle:
A typical PLC trajectory exhibits an S-shaped sales revenue curve paired with an inverted U-shaped net profit curve, spanning four distinct phases:

1. Introduction Stage:
- Market Characteristics: The product is launched into the commercial market for the first time. Sales growth is slow because consumer awareness is low and distribution channels are being established.
- Financial Dynamics: High unit manufacturing costs due to low production volumes; heavy promotional expenses to educate prospective buyers. Profits are negative (net financial loss) due to high initial R&D amortization and marketing expenditures.
- Competition: Negligible or zero direct competition.
- Strategic Response: Focus on creating primary demand (product awareness); establish selective distribution; employ Price Skimming to recover high R&D investments or Penetration Pricing to deter prospective competitors; maintain agile engineering teams to resolve early field bugs.

2. Growth Stage:
- Market Characteristics: Rapid consumer adoption and surging sales revenues ('climbing the exponential curve'). The product achieves mainstream acceptance.
- Financial Dynamics: Economies of scale in manufacturing lower unit production costs; sales revenues rise faster than marketing expenses, driving profit margins to their absolute peak.
- Competition: Competitors enter the market attracted by high profitability, introducing competing models with alternative features.
- Strategic Response: Expand market share; enhance product quality and add new features; open intensive distribution channels; shift promotion from brand awareness to brand preference; begin lowering prices moderately to tap price-sensitive buyer segments.

3. Maturity Stage:
- Market Characteristics: Sales growth decelerates, levels off, and reaches a peak plateau. The market is saturated; almost all prospective customers own the product.
- Financial Dynamics: Total sales revenue reaches its maximum, but profit margins begin a steady downward decline. Overcapacity in the industry triggers aggressive price cutting and high promotional spending (loyalty discounts) to defend market share.
- Competition: Intense, fierce rivalry among entrenched competitors; marginal firms exit the industry.
- Strategic Response: Market modification (discovering new user segments or alternative applications); Product modification (styling refreshes, engineering redesign, improved energy efficiency); Cost rationalization through value engineering to protect margins.

4. Decline Stage:
- Market Characteristics: Sales experience a persistent, irreversible downward trend driven by technological obsolescence, shifting consumer tastes, or superior substitute products (e.g., smartphones displacing standalone compact digital cameras).
- Financial Dynamics: Sales plunge; profits shrink toward zero or turn into losses; excess manufacturing capacity burdens the enterprise.
- Competition: Number of competitors shrinks as firms divest or shut down operations.
- Strategic Response: Harvesting (drastically cutting all R&D and promotional expenditures to extract remaining cash flows); Divestment (selling the product line to niche operators); or Phased discontinuation with customer spare-part support commitments.

Summary Comparison Table:
| Stage Parameter | Introduction | Growth | Maturity | Decline |
|---|---|---|---|---|
| Sales Volume | Low | Rapidly rising | Peak / Plateau | Falling |
| Profits | Negative (Loss) | Rising to Peak | High but declining | Low or zero |
| Customers | Innovators | Early Adopters | Mass Market | Laggards |
| Competitors | Few | Increasing | Intense / Stable | Declining |
| Strategic Focus | Create Awareness | Maximize Share | Defend Position | Harvest / Divest |
| Pricing | Skimming / Penetration | Competitive | Price wars / Discounting | Deep discounting |
"""
            },
            {
                "qid": "mgt-q18",
                "marks": 7,
                "type": "Descriptive",
                "title": "Human Resource Management (HRM): Planning, Recruitment, Scientific Selection, Induction, and Training Methods",
                "yt_query": "human resource management HRM recruitment selection training on the job off the job",
                "img_path": "images/mgt/hrm_selection_training_funnel.png",
                "img_caption": "Figure 4.3: Scientific Multi-Stage Selection Funnel and Training Methods Classification",
                "answer": r"""
Human Resource Management (HRM) is the strategic, coherent approach to the employment, development, and well-being of the people working in an enterprise. In knowledge-intensive engineering corporations, human capital constitutes the primary source of competitive advantage.

1. Human Resource Planning (HRP):
HRP is the systematic process by which an enterprise ensures that it has the right number and right kind of people, at the right places, at the right time, doing things for which they are economically most useful. Involves forecasting human resource demand based on business growth projections and analyzing internal labor supply (skills inventory, succession planning) to bridge manpower deficits.

2. Recruitment (Attracting Talent):
Recruitment is the positive process of discovering, encouraging, and stimulating prospective job candidates to apply for existing or anticipated vacancies within an enterprise.
- Internal Sources of Recruitment:
  - Channels: Transfers (horizontal relocation), Promotions (vertical mobility), and re-employment of former employees.
  - Advantages: High employee morale and loyalty; lower recruitment and training costs; candidate's verified capabilities are already known to management.
  - Disadvantages: Limits inbreeding of fresh ideas and innovative perspectives; internal politics; limited talent pool.
- External Sources of Recruitment:
  - Channels: Campus placements at premier engineering institutes, direct employment advertisements, online job portals, professional recruitment headhunters, and walk-in interviews.
  - Advantages: Infusion of new blood, diverse perspectives, and cutting-edge technical skills; wide competitive talent choice.
  - Disadvantages: Expensive and time-consuming; risk of hiring candidates who fail to adapt to enterprise culture; lowers morale of internal staff passed over for promotion.

3. Scientific Selection Procedure:
Unlike recruitment (which is a positive, inclusive process), selection is a negative, exclusionary process of screening and choosing the most qualified candidates from the applicant pool. A comprehensive scientific selection funnel comprises seven sequential stages:
1. Preliminary Screening / Scrutiny of Applications: Eliminating unqualified applicants who fail minimum educational degrees, grades, or experience requirements.
2. Written Technical and Aptitude Tests: Administering psychometric tests evaluating cognitive ability, numerical reasoning, specialized engineering domain knowledge, and personality profiles.
3. Technical Employment Interview: In-depth face-to-face or panel interview assessing technical problem-solving capabilities, project experience, and analytical mindset.
4. Comprehensive HR Interview: Evaluating cultural alignment, communication skills, emotional intelligence, career ambitions, and compensation expectations.
5. Reference and Background Verification: Contacting previous employers, academic advisors, and professional referees to verify candidate integrity, past performance, and criminal background checks.
6. Pre-Employment Medical Examination: Ensuring the candidate is physically and medically fit for the physical and environmental demands of the job.
7. Final Job Offer and Appointment Letter: Formal issuance of employment contract outlining job designation, salary structure, probation period, and reporting date.

4. Induction and Training:
- Induction (Orientation): Welcoming and integrating the newly appointed employee into the enterprise. Familiarizes the new hire with corporate culture, company policies, safety protocols, facility layout, and colleagues, reducing entry anxiety.
- Training Methods:
  - On-the-Job Training (OJT): The employee learns the job while actually performing it at the regular workstation under the guidance of a senior mentor:
    1. Job Instruction Training (JIT) / Apprenticeship: Step-by-step mentoring where the trainer explains, demonstrates, and supervises practice.
    2. Job Rotation: Systematically shifting the trainee across diverse engineering departments (design, manufacturing, quality, testing) to develop a holistic understanding of enterprise operations.
    3. Mentoring / Coaching: Day-to-day guidance provided by an experienced senior engineer.
  - Off-the-Job Training: Training conducted away from the physical production shop-floor, insulating learners from production pressures:
    1. Vestibule Training: Training conducted in a separate learning facility equipped with identical machinery, tools, and materials mimicking actual factory floor conditions. Enables trainees to gain technical proficiency without risking production downtime or machine damage.
    2. Classrooms, Lectures, and Case Studies: Theoretical instruction in engineering principles, safety regulations, and project management standards.
    3. Computer-Based Simulation: Flight simulators, virtual reality (VR) maintenance environments, and power plant digital twin simulators.
"""
            },
            {
                "qid": "mgt-q19",
                "marks": 7,
                "type": "Descriptive",
                "title": "Performance Appraisal and Job Analysis: Job Description, Job Specification, 360-Degree Feedback, and MBO",
                "yt_query": "performance appraisal job analysis job description job specification 360 degree feedback MBO",
                "img_path": "images/mgt/job_analysis_appraisal.png",
                "img_caption": "Figure 4.4: Job Analysis Hierarchy and the 360-Degree Performance Feedback Matrix",
                "answer": r"""
Performance appraisal and job analysis provide the structural and evaluative foundation for objective compensation structuring, promotions, training need identification, and organizational human capital optimization.

1. Job Analysis and Its Dual Components:
Job Analysis is the formal, systematic process of collecting, evaluating, and recording all relevant data regarding the tasks, responsibilities, working environment, and human requirements of a specific job. Job analysis synthesizes into two distinct functional documents:
$$\text{Job Analysis} = \text{Job Description (JD)} + \text{Job Specification (JS)}$$
- Job Description (JD) - Focuses on the Job:
A written factual statement detailing the duties, responsibilities, reporting relationships, working conditions, and equipment utilized in a specific position.
Typical Contents: Job Title, Job Summary, Department, Reporting Superior, Key Performance Responsibilities, Machine Tools and Software Operated, Hazards and Environmental Working Conditions.
- Job Specification (JS) - Focuses on the Person:
A written statement specifying the minimum acceptable human qualities, qualifications, skills, and personal attributes necessary for a worker to perform the job satisfactorily.
Typical Contents: Minimum Educational Qualifications, Technical Certifications, Years of Relevant Professional Experience, Specialized Analytical/Manual Skills, Physical Fitness Standards, and Emotional/Leadership Attributes.

2. Performance Appraisal Systems:
Performance appraisal is the systematic, periodic evaluation of an employee's job performance and contribution relative to established organizational standards.
Objectives: Provide feedback, establish merit-based salary increments and bonuses, identify training deficits, and make equitable promotion and transfer decisions.

3. Contemporary Performance Appraisal Techniques:
- 360-Degree Performance Appraisal:
  - Architecture: A multi-source evaluative feedback system that eliminates single-rater supervisory bias. Performance data is gathered anonymously from all stakeholders who interact professionally with the employee:
    1. Immediate Superior / Manager (evaluates target achievement and technical execution),
    2. Subordinates (evaluate leadership, empathy, and delegation),
    3. Peers / Colleagues (evaluate teamwork, collaboration, and communication),
    4. Internal / External Customers (evaluate responsiveness, quality, and service orientation),
    5. Self-Appraisal (the employee evaluates their own performance, identifying personal strengths and development needs).
  - Advantages: Exceptionally comprehensive, balanced, and objective; reduces personal favoritism; fosters cross-functional collaboration and leadership self-awareness.
  - Limitations: Highly complex to administer; potential collusion or retaliatory scoring if strict anonymity is compromised.

- Management by Objectives (MBO):
  - Architecture: Formulated by Peter Drucker in 1954 in *The Practice of Management*. MBO is a participative goal-setting process where superiors and subordinates jointly define specific, measurable, mutually agreed-upon performance goals for a designated operating period.
  - The MBO Cycle:
    1. Joint Goal Setting: Manager and subordinate jointly formulate SMART Objectives ($Specific, Measurable, Achievable, Relevant, Time-bound$), such as *'Reduce assembly line scrap rate from 4.5% to 2.0% by December 31'*.
    2. Action Planning: Formulating operational strategies and identifying resources required to attain the agreed targets.
    3. Periodic Progress Reviews: Conducting scheduled milestone reviews to assess progress and adjust resources.
    4. Final Evaluation: Objectively comparing actual achieved results against established targets; rewards and promotions are linked directly to target fulfillment.
  - Advantages: Eliminates subjective personality bias; enhances subordinate motivation and commitment through direct participation; clarifies organizational goals.
  - Limitations: Excessive focus on short-term quantifiable metrics at the expense of qualitative long-term objectives; heavy documentation overhead.

- Behaviorally Anchored Rating Scales (BARS):
Combines quantitative rating scales with specific critical incident narrative examples of effective and ineffective job behaviors, establishing concrete, observable performance anchors across rating points (e.g., 1 to 7).
"""
            },
            {
                "qid": "mgt-q20",
                "marks": 7,
                "type": "Descriptive",
                "title": "Theories of Motivation in Engineering Management: Maslow's Hierarchy, Herzberg's Two-Factor, and McGregor's X & Y",
                "yt_query": "theories of motivation maslow hierarchy herzberg two factor mcgregor theory X theory Y",
                "img_path": "images/mgt/motivation_theories_comparison.png",
                "img_caption": "Figure 4.5: Comparative Alignment of Maslow's Hierarchy and Herzberg's Motivator-Hygiene Factors",
                "answer": r"""
Motivation is the psychological process that initiates, energizes, directs, and sustains goal-oriented human behavior in an organization. For engineering managers, understanding motivation is essential to unlocking technical talent, reducing turnover, and maximizing research and manufacturing productivity.

1. Abraham Maslow's Hierarchy of Needs:
Formulated in 1943, Maslow asserted that human needs are arranged in a hierarchical order of prepotency, structured across five ascending levels:
1. Physiological Needs (Base): Fundamental survival needs: food, water, clothing, shelter, sleep. In an industrial context: competitive base salary, clean drinking water, climate-controlled working conditions.
2. Safety and Security Needs: Protection from physical danger, financial insecurity, emotional harm, and arbitrary managerial actions. In an industry context: job security, medical health insurance, pension plans, workplace safety equipment.
3. Social / Belongingness Needs: The desire for affection, friendship, acceptance, and positive interpersonal association. In an industry context: collaborative engineering teams, professional associations, company sports and cultural clubs.
4. Esteem Needs: Divided into internal esteem (self-respect, autonomy, competence) and external esteem (status, recognition, prestige, managerial appreciation). In an industry context: job titles, merit awards, promotion to lead engineer, private office space.
5. Self-Actualization Needs (Apex): The drive to become everything that one is capable of becoming; realizing personal potential and self-fulfillment. In an industry context: challenging R&D projects, freedom to innovate, patent filing, technical excellence.

Core Maslow Tenets:
- Deficit Principle: A satisfied need ceases to motivate behavior; only unmet needs act as behavioral motivators.
- Progression Principle: Needs are satisfied sequentially from lower to higher; an individual will not focus on esteem needs until physiological and safety needs are substantially gratified.

2. Frederick Herzberg's Two-Factor (Motivator-Hygiene) Theory:
Based on empirical studies of 200 engineers and accountants, Herzberg (1959) discovered that job satisfaction and job dissatisfaction are not polar opposites on a single continuum; they are two entirely independent psychological dimensions governed by two distinct sets of factors:
1. Hygiene (Extrinsic / Maintenance) Factors:
- Relate to the Job Context (the environment in which work is performed): Company policies, quality of supervision, interpersonal relations, working conditions, base salary, and job security.
- Impact: Hygiene factors do not motivate employees toward superior performance. If hygiene factors are inadequate or absent, employees experience severe dissatisfaction. However, when hygiene factors are fully satisfied, they merely eliminate dissatisfaction, producing a neutral state of *'No Dissatisfaction'* without inducing proactive motivation.
2. Motivators (Intrinsic Factors):
- Relate to the Job Content (the work itself): Challenging work, achievement, recognition, increased responsibility, personal growth, and advancement.
- Impact: Motivators actively inspire employees to achieve superior, discretionary performance. True, lasting job satisfaction can only be cultivated through motivators.

Managerial Implication:
Herzberg emphasized that managers must not rely solely on pay increases and comfortable working conditions (hygiene factors) to inspire technical teams. Instead, they must implement Job Enrichment—redesigning engineering roles to give engineers greater autonomy, accountability, and technical challenge.

3. Douglas McGregor's Theory X and Theory Y:
In *The Human Side of Enterprise* (1960), Douglas McGregor argued that managerial leadership behavior is shaped by fundamental implicit assumptions held regarding human nature:
- Theory X (Traditional / Authoritarian View):
  - Assumptions: The average human being possesses an inherent dislike of work and will avoid it if possible; workers lack ambition, avoid responsibility, and prefer to be directed; workers are self-centered, resistant to change, and gullible; workers must be coerced, controlled, threatened with punishment, and closely monitored to achieve organizational objectives.
  - Managerial Style: Autocratic supervision, strict scalar hierarchy, rigid rules, micro-management, and punitive discipline.
- Theory Y (Modern / Humanistic View):
  - Assumptions: The expenditure of physical and mental effort in work is as natural as play or rest; external control and threat of punishment are not the only means of motivating effort; employees will exercise self-direction and self-control in the service of objectives to which they are committed; commitment to objectives is a function of the rewards associated with their achievement (especially self-esteem and self-actualization); under proper conditions, the average person learns not only to accept but to actively seek responsibility; the capacity to exercise imagination, ingenuity, and creativity in solving enterprise problems is widely distributed in the population.
  - Managerial Style: Participative management, delegation of authority, open communication, decentralization, management by objectives (MBO), and employee empowerment.
"""
            }
        ]
    },
    {
        "module_id": "mgt-m5",
        "module_num": "Module 5",
        "module_title": "Financial Management, Capital Budgeting & Project Management (CPM/PERT)",
        "questions": [
            {
                "qid": "mgt-q21",
                "marks": 7,
                "type": "Descriptive",
                "title": "Financial Management: Scope, Profit vs Wealth Maximization, Sources of Capital, and Financial Statements",
                "yt_query": "financial management profit vs wealth maximization sources of capital equity debt balance sheet",
                "img_path": "images/mgt/financial_management_overview.png",
                "img_caption": "Figure 5.1: Scope of Corporate Financial Management and Core Financial Statement Relationships",
                "answer": r"""
Financial management is the managerial activity concerned with the planning, procurement, allocation, and control of an enterprise's financial resources to maximize the economic value of the firm.

1. Primary Objectives: Profit Maximization vs Wealth Maximization:
- Profit Maximization:
  - Principle: The traditional economic objective asserting that the primary goal of business decisions is to maximize accounting net profit.
  - Limitations: Ignores the Time Value of Money ($INR 100$ earned today is worth more than $INR 100$ earned five years hence); ignores Business and Financial Risk (incentivizes high-risk, volatile projects that report high nominal profits); relies on accounting profit which is vulnerable to manipulation; overlooks dividend policies and long-term sustainability.
- Wealth Maximization (Value Maximization):
  - Principle: The modern, universally accepted objective asserting that the fundamental goal of the firm is to maximize the Net Present Worth of the enterprise, measured through the market value (stock price) of its equity shares:
$$W = \sum_{t=1}^n \frac{CF_t}{(1 + k)^t} - I_0$$
where $CF_t$ is cash flow in year $t$, $k$ is discount rate (cost of capital), and $I_0$ is initial capital investment.
  - Superiority: Explicitly incorporates the Time Value of Money through discounted cash flows; fully accounts for project risk and uncertainty; considers the timing and sustainability of cash flows; aligns the interests of management with shareholders.

2. Long-Term and Short-Term Sources of Capital:
- Long-Term Capital Sources:
  1. Equity Shares (Common Stock): Represents permanent ownership capital. Equity holders possess voting rights and receive dividends from residual profits. Incurs zero mandatory fixed interest burden, but dilutes ownership and carries the highest cost of capital ($k_e$).
  2. Preference Shares: Hybrid security holding preferential rights over equity shareholders regarding fixed annual dividend payout and asset distribution during liquidation, but typically without voting rights.
  3. Debentures / Corporate Bonds: Long-term debt instruments carrying a legally binding fixed interest rate ($k_d$). Interest payments are tax-deductible expenses ($k_d(1 - T)$), lowering the effective cost of debt. However, excessive debt increases financial leverage risk and default risk.
  4. Retained Earnings: Internal financing achieved by ploughing back enterprise net profits into expansion projects rather than distributing them as dividends. Eliminates flotation and underwriting costs.
  5. Term Loans from Financial Institutions: Medium-to-long term secured debt provided by banks (IDBI, ICICI, SBI) with structured amortization schedules.
  6. Venture Capital and Private Equity: Equity investments provided to early-stage, high-growth technology startups in exchange for significant equity ownership and board representation.
- Short-Term Capital (Working Capital Sources):
  Commercial bank overdrafts, cash credit, trade credit from suppliers, factoring of accounts receivable, and short-term commercial paper.

3. Fundamental Financial Statements:
- The Balance Sheet:
A snapshot financial statement presenting the financial position of the enterprise at a specific point in time (e.g., as of March 31). It is strictly governed by the Fundamental Accounting Equation:
$$\mathbf{\text{Total Assets} = \text{Total Liabilities} + \text{Shareholders' Equity}}$$
  - Assets: Resources owned by the firm (Fixed Assets: plant, machinery; Current Assets: cash, inventory, accounts receivable).
  - Liabilities: Obligations owed to external creditors (Long-Term Debt, Current Liabilities: accounts payable, accrued expenses).
  - Equity: Residual interest belonging to owners (Paid-up share capital + Reserves and Surplus).
- Profit and Loss Statement (Income Statement):
A period financial statement summarizing operational revenues earned and expenses incurred over an accounting interval (e.g., April 1 to March 31):
$$\text{Net Sales Revenue} - \text{Cost of Goods Sold (COGS)} = \text{Gross Profit}$$
$$\text{Gross Profit} - \text{Operating Expenses (Selling, Admin, R\&D)} = \text{EBIT (Operating Profit)}$$
$$\text{EBIT} - \text{Interest Expense} = \text{EBT (Earnings Before Taxes)}$$
$$\text{EBT} - \text{Corporate Taxes} = \text{EAT (Net Profit After Tax)}$$
"""
            },
            {
                "qid": "mgt-q22",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Break-Even Analysis (Cost-Volume-Profit): Derivation of BEP, P/V Ratio, Margin of Safety, and Break-Even Chart",
                "yt_query": "break even analysis BEP derivation PV ratio margin of safety break even chart numerical",
                "img_path": "images/mgt/break_even_chart.png",
                "img_caption": "Figure 5.2: Cost-Volume-Profit Break-Even Chart Illustrating Fixed Costs, Variable Costs, and Margin of Safety",
                "answer": r"""
Break-Even Analysis (Cost-Volume-Profit or CVP Analysis) is an essential financial modeling tool used by engineering managers to determine the minimum sales volume and capacity utilization required for an enterprise to operate without financial loss.

1. Cost Classification in CVP Analysis:
- Total Fixed Cost ($FC$): Expenses that remain constant in total amount regardless of production volume within the relevant range (e.g., factory rent, executive salaries, depreciation of plant, property insurance).
- Variable Cost per Unit ($v$): Expenses that vary in direct, linear proportion to production volume (e.g., direct raw material, direct shop-floor labor, machine electricity consumption). Total Variable Cost is $TVC = v \cdot Q$.
- Selling Price per Unit ($P$): Revenue earned per unit sold. Total Sales Revenue is $TR = P \cdot Q$.
- Contribution Margin per Unit ($C$): The surplus revenue generated by each unit sold after recovering its direct variable cost, which contributes toward covering fixed overheads and generating operating profit:
$$C = P - v$$

2. Mathematical Derivation of Break-Even Point:
Total Cost ($TC$) of producing $Q$ units is:
$$TC = FC + TVC = FC + v \cdot Q$$
Total Revenue ($TR$) from selling $Q$ units is:
$$TR = P \cdot Q$$
Total Operating Profit ($\Pi$) is the difference between total revenue and total cost:
$$\Pi = TR - TC = (P \cdot Q) - (FC + v \cdot Q) = (P - v)Q - FC$$

By fundamental definition, the Break-Even Point ($BEP$) is the unique level of production and sales volume at which total revenue equals total cost, resulting in exactly Zero Net Profit ($\Pi = 0$):
$$(P - v) Q_{BEP} - FC = 0 \implies (P - v) Q_{BEP} = FC$$
Solving for physical sales volume in units:
$$\mathbf{Q_{BEP} = \frac{FC}{P - v} = \frac{FC}{\text{Unit Contribution Margin } (C)}} \quad \text{units}$$

To determine the Break-Even Sales Revenue ($S_{BEP}$ in monetary currency):
$$S_{BEP} = Q_{BEP} \cdot P = \left( \frac{FC}{P - v} \right) P = \frac{FC}{\frac{P - v}{P}}$$
The denominator term $\frac{P - v}{P}$ is defined as the Profit-Volume Ratio ($P/V$ Ratio or Contribution-to-Sales Ratio):
$$P/V \text{ Ratio} = \frac{P - v}{P} = \frac{\text{Contribution Margin}}{\text{Sales Price}} = \frac{\Delta \text{Profit}}{\Delta \text{Sales}}$$
Thus:
$$\mathbf{S_{BEP} = \frac{FC}{P/V \text{ Ratio}}} \quad \text{INR}$$

3. Margin of Safety ($MoS$):
The Margin of Safety represents the buffer or cushion by which actual or budgeted sales exceed the break-even sales volume. It indicates how much sales can fall before the company incurs an operating loss:
$$MoS_{\text{units}} = Q_{\text{actual}} - Q_{BEP}$$
$$MoS_{\text{revenue}} = S_{\text{actual}} - S_{BEP}$$
Expressed as a percentage ratio:
$$\mathbf{MoS \% = \frac{S_{\text{actual}} - S_{BEP}}{S_{\text{actual}}} \times 100\% = \frac{\text{Operating Profit}}{\text{Total Contribution Margin}} \times 100\%}$$

---
NUMERICAL PROBLEM (KTU Examination Model):
An electrical appliance manufacturer produces miniature circuit breakers (MCBs). The cost accounting department provides the following financial figures for the upcoming financial year:
- Annual Total Fixed Overhead Costs ($FC$) = $\text{INR } 18,00,000$
- Direct raw material cost per MCB = $\text{INR } 45$
- Direct manufacturing labor cost per MCB = $\text{INR } 25$
- Variable sales commission and packaging per MCB = $\text{INR } 10$
- Selling price per unit ($P$) = $\text{INR } 160$
- Budgeted production and sales for the year = $30,000\text{ units}$
Calculate:
(a) The unit variable cost ($v$), unit contribution margin ($C$), and the $P/V$ Ratio.
(b) The Break-Even Point in physical units ($Q_{BEP}$) and sales turnover ($S_{BEP}$).
(c) The Margin of Safety in sales revenue and as a percentage of budgeted sales.
(d) The net profit earned at the budgeted volume of $30,000\text{ units}$.
(e) The required sales volume to earn a target net profit of $\text{INR } 9,00,000$.

SOLUTION STEP-BY-STEP:
Step 1: Compute unit variable cost and unit contribution margin:
$$v = 45 + 25 + 10 = \text{INR } 80\text{ per unit}$$
$$C = P - v = 160 - 80 = \text{INR } 80\text{ per unit}$$
$$P/V \text{ Ratio} = \frac{C}{P} = \frac{80}{160} = 0.50 \implies 50\%$$

Step 2: Calculate Break-Even Point:
$$Q_{BEP} = \frac{FC}{C} = \frac{18,00,000}{80} = 22,500\text{ units}$$
$$S_{BEP} = Q_{BEP} \times P = 22,500 \times 160 = \text{INR } 36,00,000$$
(Alternatively: $S_{BEP} = \frac{FC}{P/V} = \frac{18,00,000}{0.50} = \text{INR } 36,00,000$).

Step 3: Calculate Margin of Safety at budgeted volume ($Q = 30,000$):
Actual Budgeted Sales Turnover:
$$S_{actual} = 30,000 \times 160 = \text{INR } 48,00,000$$
$$MoS_{\text{revenue}} = 48,00,000 - 36,00,000 = \text{INR } 12,00,000$$
$$MoS \% = \frac{12,00,000}{48,00,000} \times 100\% = 25.0\%$$

Step 4: Compute Net Profit at budgeted volume:
$$\Pi = (Q \cdot C) - FC = (30,000 \times 80) - 18,00,000 = 24,00,000 - 18,00,000 = \text{INR } 6,00,000$$

Step 5: Compute required sales volume for target profit ($\Pi_{target} = \text{INR } 9,00,000$):
$$Q_{target} = \frac{FC + \Pi_{target}}{C} = \frac{18,00,000 + 9,00,000}{80} = \frac{27,00,000}{80} = 33,750\text{ units}$$

Final highlighted results:
$$\mathbf{Q_{BEP} = 22,500\text{ units}}, \quad \mathbf{S_{BEP} = \text{INR } 36,00,000}, \quad \mathbf{MoS = 25\%}, \quad \mathbf{\Pi = \text{INR } 6,00,000}$$
"""
            },
            {
                "qid": "mgt-q23",
                "marks": 7,
                "type": "Numerical Problem",
                "title": "Capital Budgeting Evaluation Techniques: Payback Period, ARR, NPV, IRR, and Comparative Numerical Evaluation",
                "yt_query": "capital budgeting techniques payback period ARR NPV IRR profitability index example",
                "img_path": "images/mgt/capital_budgeting_techniques.png",
                "img_caption": "Figure 5.3: Decision Trees for Capital Budgeting Methods and NPV Profile vs Discount Rate",
                "answer": r"""
Capital budgeting is the corporate decision-making process for evaluating, selecting, and allocating capital funds to major long-term engineering investment projects (such as plant expansions, new automated lines, or robotic automation) whose cash flows extend beyond one year.

1. Classical Evaluation Methods:
- Traditional (Non-Discounted) Techniques:
  1. Payback Period ($PBP$): The exact time required for the cumulative cash inflows from an investment project to fully recover the initial capital outlay ($I_0$). Ignores cash flows occurring after the payback cutoff and ignores the time value of money.
  2. Accounting Rate of Return ($ARR$):
$$ARR = \frac{\text{Average Annual Accounting Net Profit After Taxes}}{\text{Average Investment}} \times 100\% = \frac{\bar{\Pi}_{net}}{(I_0 + S)/2} \times 100\%$$
where $S$ is scrap/salvage value. Uses accounting profits rather than cash flows and ignores discounting.

- Modern Discounted Cash Flow (DCF) Techniques:
  1. Net Present Value ($NPV$): The gold-standard criterion. Evaluates the difference between the present value of all future operating cash inflows discounted at the firm's cost of capital ($k$) and the initial investment outlay:
$$\mathbf{NPV = \sum_{t=1}^n \frac{CF_t}{(1 + k)^t} - I_0}$$
Decision Rule: Accept project if $NPV > 0$; reject if $NPV < 0$. Between mutually exclusive projects, select the project with the highest positive $NPV$.
  2. Internal Rate of Return ($IRR$): The intrinsic discount rate ($r$) that equates the present value of expected future cash inflows exactly to the initial investment outlay, rendering $NPV = 0$:
$$\sum_{t=1}^n \frac{CF_t}{(1 + IRR)^t} - I_0 = 0$$
Decision Rule: Accept if $IRR > k$ (hurdle cost of capital); reject if $IRR < k$.
  3. Profitability Index ($PI$ / Benefit-Cost Ratio):
$$PI = \frac{\sum_{t=1}^n \frac{CF_t}{(1 + k)^t}}{I_0}$$
Accept if $PI > 1.0$.

---
NUMERICAL PROBLEM (KTU Examination Model):
An electrical switchgear manufacturing company is evaluating two mutually exclusive automated CNC machinery proposals: Project A and Project B. Both require an initial capital outlay of $\text{INR } 5,00,000$. The company's cost of capital (discount rate) is $10\%$. Cash inflows are after tax but before depreciation. Estimated cash flows are:

| Year | Cash Inflow Project A ($\text{INR}$) | Cash Inflow Project B ($\text{INR}$) | Present Value Factor ($PVF$ at $10\%$) |
|---|---|---|---|
| 1 | $2,00,000$ | $1,00,000$ | $0.909$ |
| 2 | $2,00,000$ | $1,50,000$ | $0.826$ |
| 3 | $1,50,000$ | $2,00,000$ | $0.751$ |
| 4 | $1,00,000$ | $2,50,000$ | $0.683$ |
| 5 | $50,000$ | $1,00,000$ | $0.621$ |

Evaluate both proposals using:
(a) Payback Period ($PBP$).
(b) Net Present Value ($NPV$) at $10\%$.
(c) Profitability Index ($PI$).
Recommend which project management should select, stating justifications.

SOLUTION STEP-BY-STEP:
Part (a): Payback Period ($PBP$):
- For Project A ($I_0 = 5,00,000$):
  - Year 1: Cumulative cash flow = $\text{INR } 2,00,000$
  - Year 2: Cumulative cash flow = $2,00,000 + 2,00,000 = \text{INR } 4,00,000$
  - Year 3 inflow is $1,50,000$. Unrecovered balance after Year 2 = $5,00,000 - 4,00,000 = 1,00,000$.
  - Fraction of Year 3 required = $\frac{1,00,000}{1,50,000} = 0.67\text{ years}$.
  - $PBP_A = 2 + 0.67 = \mathbf{2.67\text{ years}}$ (2 years, 8 months).

- For Project B ($I_0 = 5,00,000$):
  - Year 1: $\text{INR } 1,00,000$
  - Year 2: $1,00,000 + 1,50,000 = \text{INR } 2,50,000$
  - Year 3: $2,50,000 + 2,00,000 = \text{INR } 4,50,000$
  - Year 4 inflow is $2,50,000$. Unrecovered balance after Year 3 = $5,00,000 - 4,50,000 = 50,000$.
  - Fraction of Year 4 required = $\frac{50,000}{2,50,000} = 0.20\text{ years}$.
  - $PBP_B = 3 + 0.20 = \mathbf{3.20\text{ years}}$ (3 years, 2.4 months).

Part (b): Net Present Value ($NPV$) at $10\%$:
- For Project A:
$$PV_1 = 2,00,000 \times 0.909 = 1,81,800$$
$$PV_2 = 2,00,000 \times 0.826 = 1,65,200$$
$$PV_3 = 1,50,000 \times 0.751 = 1,12,650$$
$$PV_4 = 1,00,000 \times 0.683 = 68,300$$
$$PV_5 = 50,000 \times 0.621 = 31,050$$
$$\text{Total Present Value } (PV_A) = 1,81,800 + 1,65,200 + 1,12,650 + 68,300 + 31,050 = \text{INR } 5,59,000$$
$$NPV_A = PV_A - I_0 = 5,59,000 - 5,00,000 = \mathbf{+\text{INR } 59,000}$$

- For Project B:
$$PV_1 = 1,00,000 \times 0.909 = 90,900$$
$$PV_2 = 1,50,000 \times 0.826 = 1,23,900$$
$$PV_3 = 2,00,000 \times 0.751 = 1,50,200$$
$$PV_4 = 2,50,000 \times 0.683 = 1,70,750$$
$$PV_5 = 1,00,000 \times 0.621 = 62,100$$
$$\text{Total Present Value } (PV_B) = 90,900 + 1,23,900 + 1,50,200 + 1,70,750 + 62,100 = \text{INR } 5,97,850$$
$$NPV_B = PV_B - I_0 = 5,97,850 - 5,00,000 = \mathbf{+\text{INR } 97,850}$$

Part (c): Profitability Index ($PI$):
$$PI_A = \frac{PV_A}{I_0} = \frac{5,59,000}{5,00,000} = \mathbf{1.118}$$
$$PI_B = \frac{PV_B}{I_0} = \frac{5,97,850}{5,00,000} = \mathbf{1.196}$$

RECOMMENDATION AND JUSTIFICATION:
Although Project A has a shorter Payback Period ($2.67\text{ years}$ vs $3.20\text{ years}$), Payback Period is an unreliable criterion because it completely ignores subsequent cash flows and the time value of money.
Under modern discounted cash flow principles, **Project B must be selected** because it yields a significantly higher Net Present Value ($NPV_B = \text{INR } 97,850 > NPV_A = \text{INR } 59,000$) and a superior Profitability Index ($PI_B = 1.196 > PI_A = 1.118$), thereby adding greater total net wealth to the enterprise.
"""
            },
            {
                "qid": "mgt-q24",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Project Network Analysis (CPM): Construction Rules, Forward/Backward Pass, Floats, and Critical Path",
                "yt_query": "critical path method CPM network diagram forward pass backward pass total float free float",
                "img_path": "images/mgt/cpm_network_analysis.png",
                "img_caption": "Figure 5.4: CPM Project Network Showing Event Nodes, Float Calculations, and Critical Path",
                "answer": r"""
Project management is the application of knowledge, skills, tools, and techniques to project activities to meet project requirements within defined time, cost, and quality specifications. Complex engineering projects (such as substation construction or new power plant commissioning) involve thousands of interdependent activities analyzed via Network Analysis techniques: the Critical Path Method (CPM) and the Program Evaluation and Review Technique (PERT).

1. Rules for Network Construction:
1. An activity is a distinct, time-consuming task represented by a directed arrow ($\to$).
2. An event is a point in time representing the commencement or completion of one or more activities, depicted as a circle or node ($\bigcirc$). An event consumes zero time and zero resources.
3. Every network must have exactly one starting node (initial event) and exactly one terminal node (end event).
4. Time flows unidirectionally from left to right; no looping or cyclic recurrence is permitted.
5. No two activities can share the exact same start event and same finish event. If two parallel activities have identical start and end nodes, a Dummy Activity (represented by a dashed arrow carrying zero duration and zero cost) must be inserted to preserve unique logical identification.
6. Dangling (an activity ending without connecting to the network) is strictly prohibited.
7. Fulkerson's Rule for Node Numbering: Start event is labeled 1. Cross out all arrows originating from node 1. Find all newly unentered nodes and number them 2, 3, etc., ensuring that for every activity $(i \to j)$, the start event number is strictly smaller than the finish event number ($i < j$).

2. Algorithmic Determination of the Critical Path:
- Forward Pass Computation (Determining Earliest Times):
We set the Earliest Start Time of the initial event 1 to zero: $E_1 = 0$.
Moving progressively from left to right through all nodes $j$:
$$\mathbf{E_j = \max_{i} [E_i + t_{ij}]}$$
where $t_{ij}$ is the duration of activity $(i \to j)$ and the maximum is taken over all incoming activities into node $j$.
For an activity $(i \to j)$:
- Earliest Start Time: $ES_{ij} = E_i$
- Earliest Finish Time: $EF_{ij} = ES_{ij} + t_{ij} = E_i + t_{ij}$

- Backward Pass Computation (Determining Latest Allowable Times):
Let $n$ be the terminal event node. The latest allowable completion time equals its earliest completion time: $L_n = E_n$.
Moving backward from right to left through all nodes $i$:
$$\mathbf{L_i = \min_{j} [L_j - t_{ij}]}$$
where the minimum is taken over all activities emerging from node $i$.
For an activity $(i \to j)$:
- Latest Finish Time: $LF_{ij} = L_j$
- Latest Start Time: $LS_{ij} = LF_{ij} - t_{ij} = L_j - t_{ij}$

3. Mathematical Formulation of Floats (Slacks):
Float is the measure of scheduling flexibility; it is the amount of time an activity can be delayed without extending the overall project completion date:
1. Total Float ($TF_{ij}$): The maximum time an activity can be delayed without delaying the total project completion time:
$$TF_{ij} = LS_{ij} - ES_{ij} = LF_{ij} - EF_{ij} = (L_j - E_i) - t_{ij}$$
2. Free Float ($FF_{ij}$): The portion of total float that can be utilized without delaying the earliest start time of any immediate successor activity:
$$FF_{ij} = E_j - EF_{ij} = E_j - E_i - t_{ij} = TF_{ij} - (L_j - E_j)$$
3. Independent Float ($IF_{ij}$): The time leeway available when the preceding activity finishes at its latest allowable time and the successor starts at its earliest time (guaranteed float):
$$IF_{ij} = \max[0, \, (E_j - L_i - t_{ij})] = FF_{ij} - (L_i - E_i)$$

4. The Critical Path:
The Critical Path is the continuous chain of sequential activities connecting the start event to the terminal event that possesses Zero Total Float ($TF_{ij} = 0$):
$$E_i = L_i, \quad E_j = L_j, \quad E_j - E_i = t_{ij}$$
The Critical Path represents the longest path in terms of total duration through the network. Any delay along a critical activity directly and identically delays the final completion date of the entire project.
"""
            },
            {
                "qid": "mgt-q25",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Program Evaluation and Review Technique (PERT): Three Time Estimates, Beta Distribution, and Completion Probability",
                "yt_query": "PERT three time estimates expected time variance beta distribution probability of completion Z score",
                "img_path": "images/mgt/pert_beta_distribution.png",
                "img_caption": "Figure 5.5: PERT Beta Probability Distribution and Standard Normal Bell Curve for Target Date",
                "answer": r"""
The Program Evaluation and Review Technique (PERT) was developed in 1958 by the U.S. Navy Special Projects Office with Booz Allen Hamilton for the Polaris missile project. While CPM is deterministic (applied to repetitive construction where task times are known with high certainty), PERT is probabilistic, designed specifically for non-repetitive, R&D, and aerospace projects characterized by high technological uncertainty.

1. PERT Three Time Estimates:
To account for uncertainty, PERT collects three independent time estimates for each activity $(i \to j)$:
1. Optimistic Time ($t_o$ or $a$): The minimum possible duration if everything proceeds exceptionally well, weather is ideal, and zero breakdowns occur (probability $< 1\%$).
2. Most Likely Time ($t_m$ or $m$): The modal duration occurring most frequently under normal, realistic operating conditions (the peak mode of the distribution).
3. Pessimistic Time ($t_p$ or $b$): The maximum possible duration if adverse complications occur, severe supply delays arise, or major technical hurdles emerge, excluding catastrophic acts of nature (probability $< 1\%$).

2. Derivation of Expected Duration and Variance using Beta Distribution:
PERT models activity duration as following a continuous, unimodal Beta Distribution bounded within $[t_o, t_p]$. The beta distribution is chosen because it allows for skewness (non-symmetric distributions reflecting engineering realities).
Assuming the total range $(t_p - t_o)$ represents approximately six standard deviations ($6\sigma$) of the distribution:
$$6\sigma = t_p - t_o \implies \mathbf{\sigma = \frac{t_p - t_o}{6}}$$
The variance ($\sigma^2$) of the activity duration is:
$$\mathbf{\sigma^2 = \left( \frac{t_p - t_o}{6} \right)^2}$$

The Expected Mean Duration ($t_e$ or $\mu$) of the activity is derived by taking a weighted polynomial approximation assigning a weight of 4 to the mode $t_m$ and 1 to each extreme tail ($t_o$ and $t_p$):
$$\mathbf{t_e = \frac{t_o + 4 t_m + t_p}{6}}$$

3. Project Variance and Central Limit Theorem:
Once $t_e$ is computed for all activities, standard CPM forward and backward pass algorithms identify the Critical Path.
Let $CP$ denote the set of all activities lying on the critical path.
The Expected Total Project Duration ($T_e$) is the sum of expected durations of critical activities:
$$T_e = \sum_{(i,j) \in CP} t_{e, ij}$$
By the Central Limit Theorem, although individual activity durations follow skewed Beta distributions, the total project duration distribution approaches a Gaussian Normal Distribution $\mathcal{N}(T_e, \sigma_p^2)$ because it is the sum of multiple independent random variables.
The Total Project Variance ($\sigma_p^2$) is the sum of the variances of only the critical path activities:
$$\mathbf{\sigma_p^2 = \sum_{(i,j) \in CP} \sigma_{ij}^2 = \sum_{(i,j) \in CP} \left( \frac{t_{p, ij} - t_{o, ij}}{6} \right)^2}$$
The standard deviation of project duration is:
$$\mathbf{\sigma_p = \sqrt{\sigma_p^2} = \sqrt{\sum_{(i,j) \in CP} \sigma_{ij}^2}}$$
Note: Non-critical activities do not contribute to project completion variance unless their float is small enough that high variance could create a secondary critical path.

4. Probability of Completing Project Within Target Schedule ($T_s$):
Let $T_s$ be a contractually mandated target completion date. We normalize the target date into a standard normal variable $Z$ with mean $\mu = 0$ and variance $\sigma = 1$:
$$\mathbf{Z = \frac{T_s - T_e}{\sigma_p}}$$
The probability of project completion on or before target date $T_s$ is given by the cumulative standard normal distribution function:
$$P(T \le T_s) = \Phi(Z) = \int_{-\infty}^Z \frac{1}{\sqrt{2\pi}} e^{-u^2/2} \, du$$
From standard normal probability tables:
- If $T_s = T_e \implies Z = 0 \implies P = 50\%$.
- If $Z = +1.00 \implies P = 84.13\%$.
- If $Z = +1.645 \implies P = 95.0\%$.
- If $Z = +2.00 \implies P = 97.72\%$.
- If $Z = -1.00 \implies P = 15.87\%$.
"""
            },
            {
                "qid": "mgt-q26",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Project Crashing and Time-Cost Trade-Off: Normal/Crash Costs, Cost Slope, and Total Cost Optimization",
                "yt_query": "project crashing time cost trade off cost slope formula indirect cost numerical example",
                "img_path": "images/mgt/project_crashing_cost_curves.png",
                "img_caption": "Figure 5.6: Direct Cost, Indirect Cost, and Total Project Cost Optimization Curve in Project Crashing",
                "answer": r"""
Project Crashing is a systematic network optimization technique applied when a project must be expedited to meet an aggressive deadline, avoid liquidated contractual delay penalties, or seize commercial market opportunities. Crashing involves injecting extra resources (overtime labor, additional shifts, multi-skilled subcontractors, advanced high-speed machinery) to shorten activity durations at the expense of increased direct expenditures.

1. Cost Concepts in Time-Cost Trade-Off:
- Direct Costs: Costs directly assigned to specific work activities (labor wages, overtime pay, equipment leasing, fuel). Direct costs increase as project duration is compressed (crashed).
- Indirect Costs: Overhead expenses tied to the total chronological duration of the project (site supervision salaries, trailer rentals, security, insurance, administrative overhead, and penalty liquidated damages). Indirect costs decrease linearly as project duration is shortened:
$$\text{Total Indirect Cost} = \text{Indirect Cost Rate per Day } (C_{ind}) \times \text{Total Project Duration } (T)$$
- Total Project Cost: The sum of direct and indirect costs:
$$\text{Total Project Cost} = \text{Direct Costs} + \text{Indirect Costs}$$
As project duration is compressed from its normal schedule, total direct costs rise while total indirect costs fall. The optimal project duration is the point where the Total Project Cost reaches its absolute minimum.

2. Normal and Crash Parameters:
For every activity $(i \to j)$:
- Normal Time ($NT$): Standard activity duration under normal working conditions.
- Normal Cost ($NC$): The direct cost associated with completing the task in normal time $NT$.
- Crash Time ($CT$): The absolute minimum duration into which the activity can be compressed regardless of additional resources.
- Crash Cost ($CC$): The direct cost incurred when completing the task in crash time $CT$.

3. Mathematical Formulation of Cost Slope:
Assuming a linear relationship between duration compression and cost increase between normal and crash limits, the Cost Slope represents the additional direct cost incurred per unit time saved (e.g., $\text{INR}$ per day):
$$\mathbf{\text{Cost Slope} = \frac{\Delta \text{Cost}}{\Delta \text{Time}} = \frac{\text{Crash Cost } (CC) - \text{Normal Cost } (NC)}{\text{Normal Time } (NT) - \text{Crash Time } (CT)} = \frac{CC - NC}{NT - CT}}$$
The maximum permissible crash duration for any activity is:
$$\Delta t_{\max} = NT - CT$$

4. Step-by-Step Algorithmic Procedure for Project Crashing:
1. Construct the project network under Normal Times. Determine earliest and latest event times, identify the Critical Path, and compute total normal project duration $T$ and initial Total Direct Cost ($\sum NC$).
2. Calculate the Cost Slope for all activities in the project.
3. Identify the Critical Activities: Activities lying on the critical path. Non-critical activities have positive float; crashing them increases direct costs without shortening overall project duration.
4. Select the Critical Activity with the Lowest Cost Slope: Expedite this activity first to achieve the cheapest possible duration reduction.
5. Crash the selected activity by the maximum permissible amount until:
   - Its crash limit is reached ($t = CT$), or
   - A previously non-critical path becomes parallel critical (creating multiple concurrent critical paths).
6. When Multiple Critical Paths Emerge: To shorten the project further, one must crash:
   - An activity common to all critical paths, OR
   - A combination of activities (one from each independent critical path) such that the sum of their individual cost slopes is minimized.
7. Repeat the crashing cycle step-by-step, recalculating Total Cost ($Direct + Indirect$) at each iteration, until no further crashing is technically possible or until the cost slope of the next crash exceeds the daily indirect cost savings. The iteration yielding the absolute minimum Total Project Cost represents the optimal economic schedule.
"""
            }
        ]
    }
]

MANAGEMENT_BYHEART = {
    'mgt-q1': {
        "eq": r'$$\text{Taylor: Science, not rule of thumb; Harmony, not discord; Cooperation; Development of each man.}$$',
        "text": r'F.W. Taylor pioneered Scientific Management: time and motion studies, functional foremanship (8 specialized bosses), differential piece-rate incentive wages, and the Mental Revolution aligning labor and capital.'
    },
    'mgt-q2': {
        "eq": r'$$\text{Unity of Command: 1 Employee} \to 1 \text{ Boss}; \quad \text{Gangplank: Direct Cross-Communication}$$',
        "text": r'Henri Fayol articulated 14 principles of administrative management, including Division of Work, Authority and Responsibility, Unity of Command (one boss), Unity of Direction, Scalar Chain, and the Gangplank communication bypass.'
    },
    'mgt-q3': {
        "eq": r'$$\text{POSDCORB} = \text{Planning, Organizing, Staffing, Directing, Coordinating, Reporting, Budgeting}$$',
        "text": r'Luther Gulick synthesized management functions into POSDCORB. Rational decision-making evaluates alternatives under certainty ($100\%$ known), risk (probabilistic $EMV = \sum p_i X_i$), and uncertainty.'
    },
    'mgt-q4': {
        "eq": r'$$\text{Matrix Org: Dual Authority (Functional Manager } \times \text{ Project Manager)}$$',
        "text": r'<strong>Line Org:</strong> Rigid scalar chain, pure unity of command.<br><strong>Line & Staff:</strong> Advisory specialists counsel executive line managers.<br><strong>Matrix:</strong> High-flexibility dual-reporting structure for complex technical projects.'
    },
    'mgt-q5': {
        "eq": r'$$\text{Carroll Pyramid: Philanthropic (Apex)} \to \text{Ethical} \to \text{Legal} \to \text{Economic (Base)}$$',
        "text": r'CSR mandates corporate citizenship (India Companies Act: $2\%$ net profit). Engineering ethics mandates holding public safety paramount, avoiding conflicts of interest, and protecting whistleblowers.'
    },
    'mgt-q6': {
        "eq": r'$$X^* = \frac{\sum x_i W_i}{\sum W_i}, \quad Y^* = \frac{\sum y_i W_i}{\sum W_i}, \quad MI = \frac{\text{Weight of Raw Materials}}{\text{Weight of Product}}$$',
        "text": r'<strong>Location Factors:</strong> Raw material proximity, market access, power, labor, incentives.<br><strong>Models:</strong> Factor Rating weighted score, Center of Gravity centroid $(X^*, Y^*)$, and Weber Material Index ($MI > 1$ raw material bound).'
    },
    'mgt-q7': {
        "eq": r'$$\text{Product: Line Flow (High Vol)}; \quad \text{Process: Functional Groups}; \quad \text{Cellular: Part Families}$$',
        "text": r'<strong>Product Layout:</strong> Machines arranged in sequential line for high-volume standardized goods.<br><strong>Process Layout:</strong> Similar machines grouped in departments for custom jobs.<br><strong>Cellular:</strong> U-shaped cells grouping part families via Group Technology.'
    },
    'mgt-q8': {
        "eq": r'$$\text{Work Study} = \text{Method Study (How to do)} + \text{Work Measurement (How long)}$$',
        "text": r'Work Study optimizes resource utilization without heavy capital cost. Method Study procedure: Select $\to$ Record $\to$ Examine (questioning technique) $\to$ Develop $\to$ Define $\to$ Install $\to$ Maintain.'
    },
    'mgt-q9': {
        "eq": r'$$\bigcirc \text{ (Operation)}, \ \Rightarrow \text{ (Transport)}, \ \square \text{ (Inspection)}, \ D \text{ (Delay)}, \ \nabla \text{ (Storage)}$$',
        "text": r'Method recording uses 5 ASME symbols. Tools include Operation Process Chart, Flow Process Chart (man/material/equipment), String Diagram, Multiple Activity Chart, and SIMO Chart based on 17 Therbligs.'
    },
    'mgt-q10': {
        "eq": r'$$NT = OT \times \left(\frac{PR}{100}\right), \quad ST = NT_{total} \times (1 + A) = NT_{total} + \text{Allowances}$$',
        "text": r'<strong>Time Study Derivation:</strong> Normal Time adjusts observed time by performance rating ($PR$). Adding percentage allowances ($A\%$: relaxation, personal, fatigue, contingency) yields Standard Time ($ST$).'
    },
    'mgt-q11': {
        "eq": r'$$EOQ = Q^* = \sqrt{\frac{2 D S}{H}}, \quad TIC^* = \sqrt{2 D S H}, \quad AOC = AHC \ (\text{at } EOQ)$$',
        "text": r'<strong>Wilson EOQ Derivation:</strong> Minimizes total inventory cost by equating annual ordering cost ($D S / Q$) to annual holding cost ($Q H / 2$). Second derivative is strictly positive, verifying global minimum.'
    },
    'mgt-q12': {
        "eq": r'$$\text{ABC: Pareto 80/20 Rule}; \quad \text{VED: Vital/Essential/Desirable}; \quad \text{FSN: Fast/Slow/Non-moving}$$',
        "text": r'<strong>ABC Analysis:</strong> Category A ($10-20\%$ items, $70-80\%$ value, tightest control); B ($20-30\%$ items, $20\%$ value); C ($50-70\%$ items, $10\%$ value).<br><strong>VED:</strong> Spares criticality for maintenance.'
    },
    'mgt-q13': {
        "eq": r'$$k = \frac{D \cdot L (1 + \alpha)}{C}, \quad \text{Seven Wastes: Muda of Overproduction, Waiting, Transport...}$$',
        "text": r'<strong>JIT Philosophy:</strong> Pull system eliminating 7 wastes (Muda). Dual-card Kanban (P-Kanban and C-Kanban) pulls standard containers only upon customer demand, preventing overproduction.'
    },
    'mgt-q14': {
        "eq": r'$$\text{Six Sigma: } 3.4 \text{ DPMO } (6\sigma); \quad \text{DMAIC: Define, Measure, Analyze, Improve, Control}$$',
        "text": r'<strong>TQM:</strong> Deming 14 points, PDCA cycle, customer focus, Kaizen.<br><strong>Six Sigma:</strong> Variation reduction yielding 3.4 defects per million opportunities via DMAIC.<br><strong>ISO 9001:</strong> Certified Quality Management System.'
    },
    'mgt-q15': {
        "eq": r'$$UCL/LCL = \bar{\bar{X}} \pm A_2 \bar{R}, \quad C_p = \frac{USL - LSL}{6\sigma}, \quad C_{pk} = \min\left[\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right]$$',
        "text": r'<strong>SQC:</strong> Distinguishes common from assignable causes using $\pm 3\sigma$ control limits.<br><strong>Capability:</strong> $C_p$ measures potential spread; $C_{pk} \ge 1.33$ accounts for process mean shifts.'
    },
    'mgt-q16': {
        "eq": r'$$\text{Marketing Mix: 4 Ps (Product, Price, Place, Promotion)} + \text{People, Process, Physical Evidence (7 Ps)}$$',
        "text": r'Marketing satisfies consumer needs profitably. STP framework segments heterogeneous markets, targets profitable segments, and positions the brand distinctly on perceptual maps.'
    },
    'mgt-q17': {
        "eq": r'$$\text{PLC Stages: Introduction (Loss)} \to \text{Growth (Max Margin)} \to \text{Maturity (Peak Sales)} \to \text{Decline}$$',
        "text": r'Product Life Cycle traces sales and profit curves across 4 stages, guiding strategic pricing (skimming vs penetration), advertising focus, product modifications, and harvesting/divestment.'
    },
    'mgt-q18': {
        "eq": r'$$\text{HRM: Planning} \to \text{Recruitment} \to \text{Selection} \to \text{Induction} \to \text{Training (OJT / Off-JT)}$$',
        "text": r'Recruitment attracts applicants (internal vs external); scientific selection uses tests and panel interviews to screen candidates. Training encompasses on-the-job (JIT, rotation) and off-the-job (vestibule, simulation).'
    },
    'mgt-q19': {
        "eq": r'$$\text{Job Analysis} = \text{Job Description (JD: Tasks)} + \text{Job Specification (JS: Human Specs)}$$',
        "text": r'<strong>Job Description:</strong> Duties, tools, working conditions.<br><strong>Job Specification:</strong> Required qualifications and skills.<br><strong>Appraisal:</strong> 360-degree multi-rater feedback and Drucker Management by Objectives (MBO).'
    },
    'mgt-q20': {
        "eq": r'$$\text{Maslow (Needs Hierarchy)} \leftrightarrow \text{Herzberg (Hygiene vs Motivators)} \leftrightarrow \text{McGregor (Theory X vs Y)}$$',
        "text": r'<strong>Maslow:</strong> 5-tier pyramid of needs.<br><strong>Herzberg:</strong> Hygiene factors prevent dissatisfaction; intrinsic motivators drive satisfaction.<br><strong>McGregor:</strong> Theory X (authoritarian) vs Theory Y (participative empowerment).'
    },
    'mgt-q21': {
        "eq": r'$$\text{Assets} = \text{Liabilities} + \text{Equity}, \quad W = \sum_{t=1}^n \frac{CF_t}{(1 + k)^t} - I_0$$',
        "text": r'<strong>Wealth Maximization:</strong> Superior to profit maximization by discounting cash flows.<br><strong>Capital Sources:</strong> Equity shares, debentures, retained earnings, term loans.<br><strong>Financial Statements:</strong> Balance sheet and P&L income statement.'
    },
    'mgt-q22': {
        "eq": r'$$Q_{BEP} = \frac{FC}{P - v} = \frac{FC}{C}, \quad S_{BEP} = \frac{FC}{P/V \text{ Ratio}}, \quad MoS \% = \frac{S_{actual} - S_{BEP}}{S_{actual}} \times 100\%$$',
        "text": r'<strong>Break-Even Point:</strong> Zero-profit sales volume where total revenue equals total costs ($FC + v \cdot Q$). Contribution margin $C = P - v$. Margin of Safety ($MoS$) measures cushion above BEP.'
    },
    'mgt-q23': {
        "eq": r'$$NPV = \sum_{t=1}^n \frac{CF_t}{(1 + k)^t} - I_0 > 0, \quad \sum_{t=1}^n \frac{CF_t}{(1 + IRR)^t} - I_0 = 0, \quad PI = \frac{PV}{I_0}$$',
        "text": r'Capital budgeting evaluates long-term investments. Non-discounted Payback Period ignores post-payback cash flows. Modern DCF criteria prioritize Net Present Value ($NPV$), Internal Rate of Return ($IRR$), and Profitability Index ($PI$).'
    },
    'mgt-q24': {
        "eq": r'$$E_j = \max[E_i + t_{ij}], \quad L_i = \min[L_j - t_{ij}], \quad TF = (L_j - E_i) - t_{ij} = 0 \ (\text{Critical Path})$$',
        "text": r'<strong>CPM Network Analysis:</strong> Forward pass finds earliest times ($E_j$); backward pass finds latest times ($L_i$). The Critical Path is the longest path through the network, defined by activities with Zero Total Float ($TF = 0$).'
    },
    'mgt-q25': {
        "eq": r'$$t_e = \frac{t_o + 4 t_m + t_p}{6}, \quad \sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2, \quad Z = \frac{T_s - T_e}{\sigma_p}$$',
        "text": r'<strong>PERT Probabilistic Analysis:</strong> Three time estimates ($t_o, t_m, t_p$) follow a Beta distribution. Total project variance is the sum of critical path variances. Standard normal $Z$-score gives the probability of meeting target date $T_s$.'
    },
    'mgt-q26': {
        "eq": r'$$\text{Cost Slope} = \frac{CC - NC}{NT - CT}, \quad \text{Total Cost} = \text{Direct Cost} + \text{Indirect Cost}$$',
        "text": r'<strong>Project Crashing:</strong> Expedites critical activities having the lowest cost slope. Compressing project duration increases direct costs but decreases indirect overhead costs, optimizing total project cost.'
    }
}

MANAGEMENT_EXAM_QUESTIONS = {
    "mgt-q1": "Explain the principles and techniques of Scientific Management propounded by F.W. Taylor. What is meant by mental revolution?",
    "mgt-q2": "State and explain Henri Fayol's 14 principles of administrative management. Explain the concept of the Scalar Chain and Gangplank.",
    "mgt-q3": "Explain the universal functions of management (POSDCORB). Describe the steps involved in a rational managerial decision-making process under certainty, risk, and uncertainty.",
    "mgt-q4": "Compare Line, Functional, Line & Staff, and Matrix organizational structures with neat organizational charts, highlighting advantages and limitations.",
    "mgt-q5": "Explain Corporate Social Responsibility (CSR) with reference to Archie Carroll's pyramid of CSR. Discuss core engineering ethics principles and whistleblowing.",
    "mgt-q6": "Discuss the primary and secondary factors influencing plant location decisions. Explain the Factor Rating method and Weber's Industrial Location Theory.",
    "mgt-q7": "Classify plant layouts into Product, Process, Fixed-Position, and Cellular layouts. Compare their characteristics, material handling requirements, and suitability.",
    "mgt-q8": "Define Work Study. Explain the relationship between Method Study and Work Measurement, and detail the systematic steps in conducting a method study.",
    "mgt-q9": "Describe the recording techniques used in method study: Operation Process Chart, Flow Process Chart, String Diagram, Multiple Activity Chart, and SIMO Chart with Therbligs.",
    "mgt-q10": "Explain the procedure of stopwatch time study. Derive the relationship between Observed Time, Normal Time, Allowances, and Standard Time with a numerical example.",
    "mgt-q11": "Define Economic Order Quantity (EOQ). Mathematically derive Wilson's lot size formula from the total annual inventory cost equation and sketch the cost curves.",
    "mgt-q12": "Explain selective inventory control techniques: ABC analysis based on Pareto's 80/20 rule, VED analysis, FSN analysis, and SDE analysis.",
    "mgt-q13": "Explain the Just-In-Time (JIT) manufacturing philosophy, Taiichi Ohno's seven wastes (Muda), the dual-card Kanban pull mechanism, and compare JIT with traditional MRP.",
    "mgt-q14": "Explain Total Quality Management (TQM), Deming's 14 points, and the PDCA cycle. Describe the Six Sigma DMAIC methodology and ISO 9001 standards.",
    "mgt-q15": "Explain Statistical Quality Control (SQC). Distinguish between variable control charts (X-bar & R) and attribute control charts (p & c). Derive Process Capability indices Cp and Cpk.",
    "mgt-q16": "Explain the core concepts of marketing management, the 4 Ps and 7 Ps marketing mix, and the STP (Segmentation, Targeting, Positioning) strategic framework.",
    "mgt-q17": "Explain the Product Life Cycle (PLC) concept. Describe the sales, profit, competition, and marketing strategy characteristics across all four stages.",
    "mgt-q18": "Explain the functions of Human Resource Management (HRM): Human resource planning, internal vs external recruitment, scientific selection funnel, and training methods.",
    "mgt-q19": "Distinguish between Job Description and Job Specification. Explain contemporary performance appraisal methods: 360-Degree Feedback and Management by Objectives (MBO).",
    "mgt-q20": "Compare the motivation theories in engineering management: Maslow's Hierarchy of Needs, Herzberg's Two-Factor Theory, and McGregor's Theory X and Theory Y.",
    "mgt-q21": "Explain the scope of financial management. Compare profit maximization and wealth maximization. Describe sources of long-term and short-term capital and financial statements.",
    "mgt-q22": "Derive the mathematical expressions for Break-Even Point (BEP in units and revenue), P/V Ratio, and Margin of Safety. Illustrate with a break-even chart and numerical example.",
    "mgt-q23": "Explain capital budgeting evaluation techniques: Payback Period, ARR, NPV, IRR, and Profitability Index. Compare two mutually exclusive projects using a step-by-step numerical.",
    "mgt-q24": "Explain project network construction rules in CPM. Detail the forward pass, backward pass, float calculations (total, free, independent), and identification of the critical path.",
    "mgt-q25": "Explain the PERT technique. Derive the expected activity duration and variance using the Beta distribution, and determine the probability of project completion within target date.",
    "mgt-q26": "Explain the concept of project crashing and time-cost trade-offs. Derive the cost slope formula and outline the step-by-step algorithm to optimize total project cost."
}
