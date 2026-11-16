# scratch/build_res.py
# Builder script to generate scratch/gen_res.py for Subject 8: Renewable Energy Systems (RES)
import os

res_code = r'''# -*- coding: utf-8 -*-
"""
Content generator for Subject 8: Renewable Energy Systems (RES)
KTU 2019 Scheme Electrical & Electronics Engineering Comprehensive Question Bank.
All answers are written from the perspective of an experienced engineering professor:
clear, direct, mathematically rigorous, with step-by-step intermediate equations.
All strings are raw multiline strings (r\"\"\"...\"\"\") to prevent LaTeX backslash corruption.
"""

RES_MODULES = [
    {
        "module_id": "res-m1",
        "module_num": "Module 1",
        "module_title": "Solar Radiation Fundamentals & Solar PV Physics",
        "questions": [
            {
                "qid": "res-q1",
                "marks": 3,
                "type": "Short Answer",
                "title": "Extraterrestrial vs Terrestrial Solar Radiation, Solar Constant, and Air Mass Ratio",
                "yt_query": "extraterrestrial terrestrial solar radiation solar constant air mass ratio",
                "img_path": "images/res/solar_radiation_spectrum.png",
                "img_caption": "Figure 1.1: Spectral Distribution of Extraterrestrial (AM0) and Terrestrial (AM1.5) Solar Irradiance",
                "answer": r"""
Extraterrestrial solar radiation represents the electromagnetic energy emitted by the sun that reaches the outer boundary of the earth's atmosphere without experiencing any absorption, scattering, or attenuation. The intensity of this radiation when measured on a surface normal to the sun's rays at the mean earth-sun distance of 1 astronomical unit ($1.496 \times 10^8 \text{ km}$) is termed the Solar Constant, standardly denoted as $I_{sc}$. According to the World Radiation Center (WRC), the internationally accepted value of the solar constant is:
$$I_{sc} = 1367 \text{ W/m}^2$$
Because the earth's orbit around the sun is slightly elliptical, the actual extraterrestrial radiation flux $I_{on}$ varies by approximately $\pm 3.3\%$ throughout the year. It is mathematically determined for any day of the year $n$ ($1 \le n \le 365$) using Spencer's formula:
$$I_{on} = I_{sc} \left[ 1 + 0.033 \cos\left( \frac{360 n}{365} \right) \right]$$

Terrestrial solar radiation refers to the solar radiation that actually reaches the surface of the earth after traversing through the atmospheric blanket. As extraterrestrial rays propagate through the atmosphere, they undergo substantial attenuation due to Rayleigh scattering by air molecules, Mie scattering by suspended aerosol dust particles and water droplets, and selective spectral absorption by atmospheric gases such as ozone ($O_3$, absorbing ultraviolet rays), water vapor ($H_2 O$), and carbon dioxide ($CO_2$, absorbing infrared bands). Terrestrial radiation comprises two distinct components: Direct or Beam Radiation ($I_b$), which travels in an unscattered optical line of sight directly from the solar disc, and Diffuse Radiation ($I_d$), which arrives at the earth's surface from all directions of the sky dome after multiple scattering events. The sum of both constitutes the Global Horizontal Irradiance ($I_g = I_b \cos\theta_z + I_d$).

The Air Mass ($AM$) ratio is the path length of solar radiation through the earth's atmosphere relative to the shortest possible path length when the sun is directly overhead at the zenith ($\theta_z = 0^\circ$). Under the standard planar atmospheric approximation, Air Mass is given by:
$$AM = \frac{\text{Optical path length through atmosphere}}{\text{Path length at zenith}} = \frac{1}{\cos\theta_z} = \sec\theta_z$$
where $\theta_z$ is the solar zenith angle. In space, where no atmosphere exists, the spectrum is designated as $AM0$ ($I_{sc} = 1367 \text{ W/m}^2$), which is used for satellite and spacecraft PV testing. At sea level with the sun directly overhead, $AM = 1.0$. The standard international test condition (STC) for terrestrial solar photovoltaic modules is defined at $AM1.5$, corresponding to a zenith angle of $\theta_z \approx 48.2^\circ$, with an integrated terrestrial irradiance normalized to $1000 \text{ W/m}^2$ at a cell temperature of $25^\circ\text{C}$.
"""
            },
            {
                "qid": "res-q2",
                "marks": 3,
                "type": "Short Answer",
                "title": "Solar Geometry: Declination, Hour Angle, Altitude, Zenith, and Azimuth Angles",
                "yt_query": "solar angles declination hour angle altitude zenith azimuth angles",
                "img_path": "images/res/solar_geometry_angles.png",
                "img_caption": "Figure 1.2: Angular Coordinates Defining the Position of the Sun Relative to a Terrestrial Observer",
                "answer": r"""
To precisely design, orient, and tilt solar energy collectors, the instantaneous geometric position of the sun in the celestial sphere relative to the local horizontal plane must be uniquely determined using fundamental angular relationships.

1. Declination Angle ($\delta$): The declination is the angular position of the sun at solar noon relative to the plane of the earth's equator. Because the earth's rotational axis is tilted at an angle of $23.45^\circ$ with respect to its orbital plane around the sun, the declination angle continuously varies between $-23.45^\circ$ at the winter solstice (December 21) and $+23.45^\circ$ at the summer solstice (June 21), passing through $0^\circ$ at the vernal and autumnal equinoxes. For any day of the year $n$ ($1 \le n \le 365$), $\delta$ is determined with high accuracy by Cooper's empirical equation:
$$\delta = 23.45^\circ \sin\left[ \frac{360}{365}(284 + n) \right]$$

2. Hour Angle ($\omega$): The hour angle is the angular displacement of the sun east or west of the local celestial meridian due to the earth's rotation on its axis at $15^\circ$ per hour ($360^\circ / 24 \text{ hours}$). By international convention, $\omega = 0^\circ$ at true solar noon. The hour angle is negative in the morning and positive in the afternoon:
$$\omega = 15^\circ \times (\text{Solar Time in hours} - 12)$$
For example, at 10:00 AM solar time, $\omega = 15^\circ \times (10 - 12) = -30^\circ$, and at 2:00 PM solar time, $\omega = +30^\circ$.

3. Solar Altitude Angle ($\alpha$) and Zenith Angle ($\theta_z$): The solar altitude angle $\alpha$ is the vertical angular elevation of the sun above the horizontal plane. The solar zenith angle $\theta_z$ is the angle between the sun's rays and the local vertical (zenith direction). Because altitude and zenith are complementary angles:
$$\alpha + \theta_z = 90^\circ \implies \theta_z = 90^\circ - \alpha$$
For a location with geographic latitude $\phi$, the altitude angle is computed from the fundamental spherical trigonometry relationship:
$$\sin\alpha = \cos\theta_z = \sin\phi \sin\delta + \cos\phi \cos\delta \cos\omega$$

4. Solar Azimuth Angle ($\gamma_s$) and Surface Tilt Angle ($\beta$): The solar azimuth angle $\gamma_s$ is the angular displacement between the true south direction and the projection of the sun's rays on the horizontal plane (negative when east of south, positive when west of south). The collector tilt angle $\beta$ is the angle between the surface of the collector panel and the horizontal plane. For maximum annual solar energy harvest in the northern hemisphere, fixed solar collectors are installed facing due south ($\gamma = 0^\circ$) at a tilt angle approximately equal to the local latitude ($\beta \approx \phi$).
"""
            },
            {
                "qid": "res-q3",
                "marks": 7,
                "type": "Descriptive",
                "title": "Solar Radiation Measurement Instruments: Pyranometer and Pyrheliometer",
                "yt_query": "pyranometer pyrheliometer working principle solar radiation measurement",
                "img_path": "images/res/pyranometer_pyrheliometer.png",
                "img_caption": "Figure 1.3: Schematic Cross-Section of a Thermopile Pyranometer and a Normal Incidence Pyrheliometer",
                "answer": r"""
Accurate quantitative assessment of solar resource availability requires specialized radiometric instrumentation. The two primary instruments utilized globally in meteorological stations and commercial solar power plants are the Pyranometer and the Pyrheliometer.

1. Pyranometer:
A pyranometer is a precision radiometric device designed to measure total global solar radiation (the sum of direct beam and diffuse sky radiation) received from a full hemispherical field of view ($2\pi$ steradians) onto a flat horizontal surface over a broad spectral bandwidth ($0.3 \text{ to } 3.0 \ \mu\text{m}$).
Construction and Working Principle:
The core sensing element of a standard precision pyranometer is a high-sensitivity multijunction differential thermopile. The active hot junctions of the thermopile are coated with an optical black absorption layer (such as carbon black or black optical paint) having an absorptance exceeding $0.97$ across the entire solar spectrum. The reference cold junctions are thermally coupled to a massive, polished brass or aluminum instrument heat sink protected under a radiation shield. When sunlight impinges on the black receiver, it absorbs radiant energy, creating a sharp temperature differential $\Delta T$ between the hot and cold junctions. By the Seebeck thermoelectric effect, this temperature gradient induces a minute DC voltage proportional to the incident radiant flux:
$$V_{out} = C_{cal} \cdot I_g$$
where $C_{cal}$ is the factory calibration sensitivity coefficient (typically $5 \text{ to } 10 \ \mu\text{V} / (\text{W/m}^2)$) and $I_g$ is the global irradiance in $\text{W/m}^2$.
To isolate the thermopile sensor from convective wind cooling and ambient weather perturbations, the sensor is sealed beneath two concentric hemispherical optical glass domes made of high-purity optical grade Schott glass. The outer dome reflects long-wave thermal radiation, and the inner dome provides a stagnant air insulating barrier. A silica-gel desiccant chamber prevents internal moisture condensation.
Diffuse Radiation Measurement: A pyranometer can also measure purely diffuse solar radiation ($I_d$) by shielding the sensor disc from the direct solar beam using either an automated shadow band or an motorized sun-tracking occulting disc.

2. Pyrheliometer:
A pyrheliometer is a directional radiometric instrument designed exclusively to measure Beam or Direct Normal Irradiance (DNI), which is the solar flux coming directly from the solar disc without sky-diffuse components, received on a surface held perpendicular to the sun's rays.
Construction and Working Principle:
The sensor consists of a black thermopile detector positioned at the bottom base of an elongated collimating tube. The collimating tube has a precisely machined aperture at its entrance that limits the field of view to a narrow full acceptance angle of exactly $5.7^\circ$ (or approximately $5^\circ$ slope angle per ISO 9060 standards). The inside of the collimating tube is blackened and baffled with a succession of knife-edge circular diaphragms to suppress internal optical reflections and eliminate stray diffuse light.
Because the acceptance angle is extremely narrow, the pyrheliometer must constantly point directly at the moving sun throughout the day. It is mounted on an automated dual-axis celestial sun tracker driven by microprocessor-controlled stepper motors and sun-position ephemeris algorithms.
The thermopile generates a thermoelectric voltage directly proportional to the direct normal irradiance:
$$I_{bN} = \frac{V_{pyr}}{C_{pyr}}$$
Pyrheliometer measurements are indispensable for Concentrated Solar Power (CSP) plants, such as parabolic trough and solar tower systems, which can concentrate only parallel direct rays and cannot utilize diffuse radiation.
"""
            },
            {
                "qid": "res-q4",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Solar Photovoltaic Cell Physics: P-N Junction Effect, Single-Diode Equivalent Circuit, and Governing I-V Equation",
                "yt_query": "solar cell equivalent circuit single diode model derivation I-V equation",
                "img_path": "images/res/pv_equivalent_circuit.png",
                "img_caption": "Figure 1.4: Single-Diode Equivalent Circuit Model of a Practical Solar PV Cell with Parasitic Resistances",
                "answer": r"""
A solar photovoltaic cell is essentially a large-area semiconductor p-n junction diode optimized for the conversion of incident photon energy directly into electrical energy through the photovoltaic effect. When incident photons have an energy $E_{ph} = h\nu$ greater than or equal to the semiconductor bandgap energy $E_g$ ($E_g \approx 1.12 \text{ eV}$ for crystalline silicon at $300\text{ K}$), photons are absorbed, exciting electrons from the valence band into the conduction band, thereby generating electron-hole pairs (EHPs).

Within the built-in space-charge depletion region, an internal electric field exists directed from the donor-doped n-side to the acceptor-doped p-side. This strong electrostatic field immediately separates the generated carrier pairs before they can recombine, sweeping the minority electrons into the n-region and minority holes into the p-region. This spatial charge accumulation creates an open-circuit photovoltage across the external terminals and drives a continuous photocurrent when connected to an external load.

To analyze the electrical behavior of a real solar cell, we construct its standard single-diode equivalent circuit model. The practical equivalent circuit consists of:
1. An ideal constant current source producing light-generated photocurrent $I_{ph}$ proportional to solar irradiance.
2. A parallel semiconductor p-n junction diode modeling dark recombination currents.
3. A parallel shunt resistance $R_{sh}$ representing leakage currents across the p-n junction edges and structural crystal defects.
4. A series resistance $R_s$ representing the ohmic contact resistance of metallic grid fingers, busbars, and bulk semiconductor material.

Applying Kirchhoff's Current Law (KCL) at the top output node:
$$I = I_{ph} - I_D - I_{sh}$$
The current flowing through the parallel diode is governed by Shockley's ideal diode equation:
$$I_D = I_0 \left[ \exp\left( \frac{q V_D}{n k T} \right) - 1 \right]$$
where:
- $I_0$ is the reverse saturation (dark) current of the diode,
- $q$ is the electronic charge ($1.602 \times 10^{-19} \text{ C}$),
- $k$ is the Boltzmann constant ($1.381 \times 10^{-23} \text{ J/K}$),
- $T$ is the absolute junction temperature in Kelvin,
- $n$ is the diode ideality factor (typically $1.0 \le n \le 2.0$),
- $V_t = \frac{k T}{q}$ is the thermal voltage ($V_t \approx 0.0259 \text{ V}$ at $25^\circ\text{C} = 298.15\text{ K}$).

From the equivalent circuit loop, the voltage across the diode $V_D$ is related to terminal voltage $V$ and terminal current $I$ by:
$$V_D = V + I R_s$$
The leakage current diverted through the shunt resistance is:
$$I_{sh} = \frac{V_D}{R_{sh}} = \frac{V + I R_s}{R_{sh}}$$

Substituting the expressions for $I_D$ and $I_{sh}$ into the KCL node equation yields the celebrated transcendental characteristic equation of a practical solar cell:
$$I = I_{ph} - I_0 \left[ \exp\left( \frac{q (V + I R_s)}{n k T} \right) - 1 \right] - \frac{V + I R_s}{R_{sh}}$$

For an ideal solar cell, parasitic losses are neglected ($R_s = 0$ and $R_{sh} \to \infty$). Under these ideal conditions, the equation reduces to:
$$I = I_{ph} - I_0 \left[ \exp\left( \frac{q V}{n k T} \right) - 1 \right]$$
Setting $V = 0$ yields the short-circuit current:
$$I_{sc} \approx I_{ph}$$
Setting $I = 0$ yields the open-circuit voltage:
$$0 = I_{sc} - I_0 \left[ \exp\left( \frac{q V_{oc}}{n k T} \right) - 1 \right]$$
Since $\exp\left( \frac{q V_{oc}}{n k T} \right) \gg 1$:
$$V_{oc} = \frac{n k T}{q} \ln\left( \frac{I_{sc}}{I_0} + 1 \right) \approx V_t \cdot n \ln\left( \frac{I_{sc}}{I_0} \right)$$
This confirms that $I_{sc}$ increases linearly with incident solar irradiance, whereas $V_{oc}$ increases logarithmically with irradiance and decreases significantly with increasing cell operating temperature.
"""
            },
            {
                "qid": "res-q5",
                "marks": 7,
                "type": "Numerical Problem",
                "title": "PV Cell Characteristics: Voc, Isc, Pmp, Fill Factor (FF), and Efficiency Derivation with Step-by-Step Calculation",
                "yt_query": "solar cell fill factor efficiency calculation example numerical",
                "img_path": "images/res/pv_iv_pv_curves.png",
                "img_caption": "Figure 1.5: Current-Voltage (I-V) and Power-Voltage (P-V) Characteristic Curves of a Solar Photovoltaic Cell",
                "answer": r"""
The performance of a photovoltaic device is evaluated through its Current-Voltage ($I-V$) and Power-Voltage ($P-V$) characteristic curves. Four critical parameters define the operating limits:

1. Short-Circuit Current ($I_{sc}$): The maximum current delivered by the cell when the external load impedance is zero ($V = 0$). For an ideal cell, $I_{sc} = I_{ph}$.
2. Open-Circuit Voltage ($V_{oc}$): The maximum terminal voltage developed when the external load is open-circuited ($I = 0$).
3. Maximum Power Point ($P_{mp}$): The unique point on the $I-V$ curve where the product of terminal voltage $V$ and current $I$ attains its absolute maximum:
$$P_{mp} = V_{mp} \cdot I_{mp}$$
At this point, $\frac{dP}{dV} = 0$, which yields $\frac{d(VI)}{dV} = I + V \frac{dI}{dV} = 0 \implies \frac{dI}{dV} = -\frac{I}{V}$.
4. Fill Factor ($FF$): A dimensionless measure of the squareness of the $I-V$ curve, defined as the ratio of maximum harvestable power to the product of $V_{oc}$ and $I_{sc}$:
$$FF = \frac{P_{mp}}{V_{oc} \cdot I_{sc}} = \frac{V_{mp} \cdot I_{mp}}{V_{oc} \cdot I_{sc}}$$
For high-quality commercial silicon solar cells, $FF$ ranges between $0.75$ and $0.85$ ($75\%$ to $85\%$). Higher series resistance or lower shunt resistance severely degrades the fill factor.
5. Conversion Efficiency ($\eta$): The ratio of maximum electrical power output $P_{mp}$ to total incident solar optical power $P_{in}$ over cell surface area $A$:
$$\eta = \frac{P_{mp}}{P_{in}} \times 100\% = \frac{V_{mp} I_{mp}}{G \cdot A} \times 100\% = \frac{V_{oc} \cdot I_{sc} \cdot FF}{G \cdot A} \times 100\%$$
where $G$ is the incident solar irradiance ($\text{W/m}^2$) and $A$ is the aperture surface area of the cell ($\text{m}^2$).

---
NUMERICAL PROBLEM (KTU Model Examination):
A monocrystalline silicon solar cell of dimensions $12.5\text{ cm} \times 12.5\text{ cm}$ is subjected to standard test conditions (STC: irradiance $G = 1000\text{ W/m}^2$ at temperature $T = 25^\circ\text{C}$). Under these conditions, the cell exhibits:
- Short-circuit current $I_{sc} = 5.25\text{ A}$
- Open-circuit voltage $V_{oc} = 0.62\text{ V}$
- Voltage at maximum power $V_{mp} = 0.51\text{ V}$
- Current at maximum power $I_{mp} = 4.80\text{ A}$
Determine:
(a) The cell active surface area $A$ and incident solar power $P_{in}$.
(b) The maximum electrical power output $P_{mp}$.
(c) The Fill Factor ($FF$).
(d) The solar energy conversion efficiency ($\eta$).

SOLUTION STEP-BY-STEP:
Step 1: Calculate the cell surface area and total incident power:
$$A = 12.5\text{ cm} \times 12.5\text{ cm} = 0.125\text{ m} \times 0.125\text{ m} = 0.015625\text{ m}^2$$
The total incident radiant optical power is:
$$P_{in} = G \times A = 1000\text{ W/m}^2 \times 0.015625\text{ m}^2 = 15.625\text{ W}$$

Step 2: Calculate the maximum electrical power output:
$$P_{mp} = V_{mp} \times I_{mp} = 0.51\text{ V} \times 4.80\text{ A} = 2.448\text{ W}$$

Step 3: Calculate the Fill Factor:
The nominal product of open-circuit voltage and short-circuit current is:
$$V_{oc} \times I_{sc} = 0.62\text{ V} \times 5.25\text{ A} = 3.255\text{ W}$$
Applying the Fill Factor formula:
$$FF = \frac{P_{mp}}{V_{oc} \times I_{sc}} = \frac{2.448}{3.255} \approx 0.7521 \implies FF = 75.21\%$$

Step 4: Calculate the solar cell conversion efficiency:
$$\eta = \frac{P_{mp}}{P_{in}} \times 100\% = \frac{2.448\text{ W}}{15.625\text{ W}} \times 100\% = 15.6672\% \approx 15.67\%$$
Final highlighted results:
$$\mathbf{P_{mp} = 2.448\text{ W}}, \quad \mathbf{FF = 0.7521 \ (75.21\%)}, \quad \mathbf{\eta = 15.67\%}$$
"""
            }
        ]
    },
    {
        "module_id": "res-m2",
        "module_num": "Module 2",
        "module_title": "Solar Thermal Collectors & Solar PV Systems",
        "questions": [
            {
                "qid": "res-q6",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Liquid Flat-Plate Solar Collector: Construction, Heat Losses, and Hottel-Whillier-Bliss Energy Balance Equation",
                "yt_query": "flat plate collector hottel whillier bliss equation derivation solar thermal",
                "img_path": "images/res/flat_plate_collector.png",
                "img_caption": "Figure 2.1: Structural Components and Thermal Heat Flow Diagram of a Liquid Flat-Plate Collector",
                "answer": r"""
A liquid flat-plate solar collector (FPC) is a non-concentrating solar thermal device designed to absorb incident solar radiation and transfer the collected thermal energy to a working liquid (typically water or a water-glycol mixture) flowing through embedded tubes for domestic hot water, space heating, and low-temperature industrial processes ($50^\circ\text{C} \text{ to } 90^\circ\text{C}$).

Constructional Components:
1. Absorber Plate: A high-conductivity metallic sheet (copper or aluminum) coated with a spectrally selective surface having high solar absorptance ($\alpha \ge 0.95$) in the short-wave solar spectrum and low thermal emittance ($\varepsilon \le 0.10$) in the long-wave infrared spectrum (e.g., black chrome or titanium nitrite oxide).
2. Riser Tubes and Headers: A grid of parallel copper riser tubes brazed or laser-welded onto the absorber plate, fed by lower and upper fluid distribution headers.
3. Transparent Glazing: One or two sheets of low-iron tempered glass ($3.2 \text{ to } 4\text{ mm}$ thick) with high transmittance ($\tau \approx 0.90$) that admit shortwave solar rays while blocking long-wave thermal radiation emitted by the hot absorber plate (the greenhouse effect).
4. Thermal Insulation: Mineral wool, polyurethane foam, or fiberglass layers placed beneath the bottom and around the sidewalls to suppress conductive heat loss.
5. Protective Casing: A weatherproof aluminum or galvanized sheet steel casing that seals the assembly against wind, rain, and dust.

Derivation of Hottel-Whillier-Bliss Energy Balance Equation:
Under steady-state conditions, the incident solar energy absorbed by the collector plate of aperture area $A_c$ is:
$$q_{absorbed} = A_c \cdot S = A_c \left[ I_t (\tau\alpha) \right]$$
where $I_t$ is the total incident solar irradiance on the tilted collector aperture, and $(\tau\alpha)$ is the effective transmittance-absorptance product of the cover-plate system.

The absorber plate operates at a mean temperature $T_p$ higher than the ambient temperature $T_a$, leading to thermal losses back to the environment via radiation, convection, and conduction. These combined heat losses are expressed using an overall heat loss coefficient $U_L$:
$$q_{loss} = A_c \cdot U_L (T_p - T_a)$$
where $U_L = U_{top} + U_{bottom} + U_{edge}$.
Thus, the net useful thermal power extracted by the collector is:
$$q_u = q_{absorbed} - q_{loss} = A_c \left[ S - U_L (T_p - T_a) \right]$$

Because the actual mean plate temperature $T_p$ is difficult to measure experimentally across the entire plate surface, Hottel, Whillier, and Bliss introduced the Collector Heat Removal Factor $F_R$. $F_R$ is a dimensionless factor defined as the ratio of actual useful heat gain to the maximum possible heat gain that would occur if the entire absorber plate were at the fluid inlet temperature $T_i$:
$$q_u = F_R A_c \left[ S - U_L (T_i - T_a) \right] = F_R A_c \left[ I_t (\tau\alpha) - U_L (T_i - T_a) \right]$$
The useful heat gain can also be determined from the fluid mass flow rate $\dot{m}$, fluid specific heat capacity $C_p$, and temperature rise between inlet $T_i$ and outlet $T_o$:
$$q_u = \dot{m} C_p (T_o - T_i)$$

Equating both expressions yields the celebrated Hottel-Whillier-Bliss instantaneous collector thermal efficiency $\eta$:
$$\eta = \frac{q_u}{A_c I_t} = \frac{F_R A_c \left[ I_t (\tau\alpha) - U_L (T_i - T_a) \right]}{A_c I_t}$$
$$\eta = F_R (\tau\alpha) - F_R U_L \left( \frac{T_i - T_a}{I_t} \right)$$
Plotting $\eta$ against the reduced temperature parameter $\left( \frac{T_i - T_a}{I_t} \right)$ produces a straight line where:
- The y-intercept represents the optical efficiency $F_R (\tau\alpha)$,
- The negative slope represents the thermal loss parameter $-F_R U_L$.
"""
            },
            {
                "qid": "res-q7",
                "marks": 7,
                "type": "Descriptive",
                "title": "Concentrating Solar Power (CSP) Collectors: Parabolic Trough, Linear Fresnel, Solar Tower, and Dish Stirling",
                "yt_query": "concentrating solar power parabolic trough solar tower linear fresnel dish stirling",
                "img_path": "images/res/csp_collector_technologies.png",
                "img_caption": "Figure 2.2: Schematics of Four Major Concentrating Solar Thermal Technologies (PTC, LFR, CR, PDS)",
                "answer": r"""
Concentrating Solar Power (CSP) systems utilize optical reflectors (mirrors) to concentrate direct normal solar irradiance (DNI) from a large aperture area onto a significantly smaller absorber target. Concentrating the solar flux achieves elevated working temperatures ($300^\circ\text{C} \text{ to } 1000^\circ\text{C}+$ ), driving conventional steam or gas turbine thermal cycles at high thermodynamic efficiency.

Concentration Ratio ($C_R$):
The fundamental figure of merit is the geometric concentration ratio $C_R$, defined as:
$$C_R = \frac{\text{Aperture Area of Concentrator } (A_a)}{\text{Surface Area of Receiver Absorber } (A_r)}$$
As $C_R$ increases, the thermal loss area $A_r$ shrinks relative to the collecting aperture $A_a$, enabling much higher operating temperatures without excessive radiation heat loss.

1. Parabolic Trough Collector (PTC) - Line Focus:
- Geometry & Optics: PTC consists of long, U-shaped parabolic curved mirrors that focus direct sunlight onto a linear metallic absorber tube positioned along the focal line. It utilizes single-axis tracking (typically tracking from East to West).
- Receiver: A stainless steel pipe coated with cermet selective coating surrounded by an evacuated glass envelope to eliminate convection losses. Synthetic thermal oil or molten salt circulates through the tube.
- Operating Temperature: $350^\circ\text{C} \text{ to } 400^\circ\text{C}$; Concentration ratio $C_R \approx 15 \text{ to } 80$.
- Status: The most mature and widely deployed CSP technology globally (e.g., SEGS and Mojave plants).

2. Linear Fresnel Reflector (LFR) - Line Focus:
- Geometry & Optics: Instead of curved parabolic mirrors, LFR employs long, flat or slightly curved elastic mirror strips placed close to the ground that rotate independently to focus sunlight onto an elevated stationary linear receiver.
- Receiver: Suspended above the mirror field, containing multiple water/steam boiling tubes.
- Operating Temperature: $250^\circ\text{C} \text{ to } 380^\circ\text{C}$; Concentration ratio $C_R \approx 10 \text{ to } 40$.
- Advantages: Lower capital cost, lower wind load on ground mirrors, and higher land-use factor compared to PTC.

3. Central Receiver / Solar Power Tower (CR) - Point Focus:
- Geometry & Optics: Employs a vast circular or semi-circular field of hundreds or thousands of dual-axis tracking flat mirrors called heliostats. All heliostats continuously track the sun and reflect rays onto a single central receiver mounted atop a tall tower ($100 \text{ to } 250\text{ meters}$).
- Heat Transfer Fluid: Molten nitrate salt ($60\% \text{ NaNO}_3 + 40\% \text{ KNO}_3$) is pumped up the tower, heated to $565^\circ\text{C}$, and stored in massive insulated hot-salt tanks, enabling 10 to 15 hours of full-load thermal energy storage (TES) for dispatchable baseload generation during nighttime.
- Operating Temperature: $550^\circ\text{C} \text{ to } 800^\circ\text{C}+$; Concentration ratio $C_R \approx 500 \text{ to } 1500$.

4. Parabolic Dish Stirling System (PDS) - Point Focus:
- Geometry & Optics: A standalone dish-shaped paraboloid mirror that concentrates sunlight onto a focal point receiver mounted on the dish structure, guided by dual-axis tracking.
- Power Cycle: A compact Stirling or Brayton engine is placed directly at the focal receiver, using hydrogen or helium working gas.
- Operating Temperature: $700^\circ\text{C} \text{ to } 900^\circ\text{C}$; Concentration ratio $C_R \approx 600 \text{ to } 3000$.
- Status: Demonstrates the highest solar-to-electric conversion efficiency (over $31\%$), but lacks thermal storage integration and has higher mechanical complexity per kW.
"""
            },
            {
                "qid": "res-q8",
                "marks": 7,
                "type": "Descriptive",
                "title": "PV Module Interconnection, Partial Shading Effects, Hot-Spot Formation, Bypass and Blocking Diodes",
                "yt_query": "partial shading pv module hot spot bypass diode blocking diode",
                "img_path": "images/res/pv_shading_bypass_diodes.png",
                "img_caption": "Figure 2.3: Bypass Diodes Mitigating Hot-Spot Formation and Resulting Multi-Peak P-V Curves",
                "answer": r"""
To generate utility-level voltages and power outputs, individual photovoltaic cells (which typically produce only $\approx 0.5 \text{ to } 0.6\text{ V}$ and $5 \text{ to } 10\text{ A}$) are interconnected into solar modules, strings, and multi-string arrays.

Series and Parallel Interconnections:
- In a series string of $N_s$ cells, the total output voltage is the algebraic sum of the individual cell voltages ($V_{string} = \sum_{i=1}^{N_s} V_i$), while the current is strictly limited to the current of the weakest cell ($I_{string} = \min\{I_1, I_2, \dots, I_{N_s}\}$).
- In a parallel grouping of $N_p$ strings, the total output current is the sum of the individual string currents ($I_{array} = \sum_{j=1}^{N_p} I_j$), while the array voltage equals the string voltage ($V_{array} = V_{string}$).

Partial Shading and Mismatch Phenomena:
When a portion of a PV array is shaded by building obstructions, overhead transmission lines, tree foliage, bird droppings, or localized cloud cover, the illuminated irradiance on the shaded cells drops significantly. Because the short-circuit current of a PV cell is directly proportional to irradiance ($I_{sc} \propto G$), the shaded cell can produce only a reduced photocurrent.
However, because all cells in the series string are forced to carry the higher current generated by the fully illuminated cells, the shaded cell is driven into reverse-bias operation ($V_{cell} < 0$). Under deep reverse bias, the shaded cell stops producing power and instead behaves as a resistive sink, dissipating power internally equal to:
$$P_{dissipated} = |V_{reverse}| \times I_{string}$$
This localized electrical power dissipation is converted into intense heat. The localized temperature can exceed $150^\circ\text{C} \text{ to } 200^\circ\text{C}$, resulting in the destructive phenomenon known as Hot-Spot Formation. Hot spots cause localized EVA browning, backsheet melting, solder fatigue, glass cracking, and permanent cell burnout.

Role of Bypass Diodes:
To protect series strings against hot-spot destruction, Bypass Diodes are connected in anti-parallel (reverse polarity) across groups of series cells (typically across 18 to 24 cells in standard 60-cell or 72-cell silicon modules).
- Under normal uniform sunlight: All cells generate positive forward voltage. The bypass diode is reverse-biased and remains in an open-circuit state, consuming negligible leakage current.
- Under partial shading: As the shaded cell becomes reverse-biased, the total net voltage across that sub-string drops below zero. When this reverse voltage reaches approximately $-0.7\text{ V}$, the bypass diode turns ON (forward-biased). The excess string current safely bypasses the shaded cell group through the forward-conducting diode, clamping the reverse voltage to approximately $-0.7\text{ V}$ and eliminating destructive hot-spot power dissipation.
Consequence on P-V Characteristics: The activation of bypass diodes distorts the smooth, unimodal Power-Voltage curve, creating Multiple Local Maxima (LMPPs) and a single Global Maximum Power Point (GMPP). Conventional gradient-based MPPT algorithms fail by becoming trapped in local peaks, requiring advanced global tracking techniques.

Role of Blocking Diodes:
Blocking Diodes are connected in series with each parallel string in an array or between the PV array and a battery storage bank:
1. They prevent reverse current from flowing from fully illuminated parallel strings into lower-voltage shaded strings.
2. In off-grid battery systems, they prevent the battery from discharging backward into the PV array during nighttime when the PV terminal voltage drops to zero.
"""
            },
            {
                "qid": "res-q9",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Maximum Power Point Tracking (MPPT): Perturb and Observe (P&O) and Incremental Conductance (IncCond) Algorithms",
                "yt_query": "mppt perturb and observe incremental conductance algorithm derivation",
                "img_path": "images/res/mppt_algorithms_flowchart.png",
                "img_caption": "Figure 2.4: Flowcharts and Mathematical Derivatives for P&O and Incremental Conductance MPPT Methods",
                "answer": r"""
Because the Power-Voltage ($P-V$) characteristic of a photovoltaic array is highly non-linear and continuously varies with solar irradiance and ambient temperature, Maximum Power Point Tracking (MPPT) is incorporated into power electronic interfaces (DC-DC buck, boost, or inverter stages) to continuously operate the array at its optimal voltage $V_{mp}$ and extract the maximum available power $P_{mp}$.

1. Perturb and Observe (P&O) Algorithm:
Principle: P&O operates by periodically perturbing (incrementing or decrementing) the array operating voltage (or duty cycle $D$ of the DC-DC converter) and observing the resulting change in array output power.
Mathematical Decision Logic:
Let $V(k)$ and $I(k)$ be the measured voltage and current at iteration step $k$. The power is $P(k) = V(k) \cdot I(k)$.
The changes in voltage and power between successive samples are:
$$\Delta V = V(k) - V(k-1), \quad \Delta P = P(k) - P(k-1)$$
The control rules are:
- If $\Delta P > 0$ and $\Delta V > 0$: Power is increasing; the operating point is moving up the left side of the $P-V$ curve toward the MPP. Therefore, continue perturbing in the same direction ($\Delta V > 0$, increase $V_{ref}$).
- If $\Delta P > 0$ and $\Delta V < 0$: Power is increasing with decreasing voltage; continue perturbing downward ($\Delta V < 0$, decrease $V_{ref}$).
- If $\Delta P < 0$ and $\Delta V > 0$: Power has decreased after increasing voltage; the operating point has overshot the peak and moved onto the right side of the MPP. Therefore, reverse the perturbation direction ($\Delta V < 0$, decrease $V_{ref}$).
- If $\Delta P < 0$ and $\Delta V < 0$: Power has decreased after decreasing voltage; reverse the perturbation direction ($\Delta V > 0$, increase $V_{ref}$).

Limitations of P&O:
1. Steady-State Oscillation: Around the MPP, the operating point continuously oscillates around $V_{mp}$ in a three-point limit cycle, causing steady-state power loss.
2. Divergence during Rapid Irradiance Shifts: If solar irradiance suddenly increases between sample steps, $\Delta P > 0$ even if the voltage perturbation moved away from the MPP, causing the algorithm to track in the wrong direction.

2. Incremental Conductance (IncCond) Algorithm:
Derivation: The Incremental Conductance method eliminates the tracking errors of P&O by utilizing the exact mathematical derivative of the $P-V$ curve.
The electrical power delivered by the PV array is:
$$P = V \cdot I$$
Differentiating both sides with respect to terminal voltage $V$:
$$\frac{dP}{dV} = \frac{d(V \cdot I)}{dV} = I \frac{dV}{dV} + V \frac{dI}{dV} = I + V \frac{dI}{dV}$$
Dividing through by terminal voltage $V$ ($V > 0$):
$$\frac{1}{V} \frac{dP}{dV} = \frac{I}{V} + \frac{dI}{dV}$$
At the Maximum Power Point (MPP), the slope of the $P-V$ curve is zero:
$$\frac{dP}{dV} = 0 \implies \frac{dI}{dV} = -\frac{I}{V}$$
To the left of the MPP (where power increases with voltage):
$$\frac{dP}{dV} > 0 \implies \frac{dI}{dV} > -\frac{I}{V}$$
To the right of the MPP (where power decreases with voltage):
$$\frac{dP}{dV} < 0 \implies \frac{dI}{dV} < -\frac{I}{V}$$
Here:
- $\frac{I}{V}$ is the Instantaneous Conductance ($G$),
- $\frac{dI}{dV} \approx \frac{\Delta I}{\Delta V}$ is the Incremental Conductance ($\Delta G$).

IncCond Control Logic:
The controller measures instantaneous $V(k)$ and $I(k)$, computes $\Delta V = V(k) - V(k-1)$ and $\Delta I = I(k) - I(k-1)$:
- If $\Delta V = 0$: Check if $\Delta I = 0$. If $\Delta I = 0$, the operating point is at the MPP. If $\Delta I > 0$, irradiance has increased (increase $V_{ref}$); if $\Delta I < 0$, irradiance has decreased (decrease $V_{ref}$).
- If $\Delta V \ne 0$: Compare $\frac{\Delta I}{\Delta V}$ with $-\frac{I}{V}$:
  - If $\frac{\Delta I}{\Delta V} = -\frac{I}{V}$: The system is exactly at the MPP; no voltage adjustment is needed.
  - If $\frac{\Delta I}{\Delta V} > -\frac{I}{V}$: The operating point is to the left of the MPP; increment reference voltage ($V_{ref} \leftarrow V_{ref} + \Delta V_{step}$).
  - If $\frac{\Delta I}{\Delta V} < -\frac{I}{V}$: The operating point is to the right of the MPP; decrement reference voltage ($V_{ref} \leftarrow V_{ref} - \Delta V_{step}$).

Advantages: The IncCond algorithm can recognize when the array reaches the MPP and halt perturbations, completely eliminating steady-state limit-cycle hunting and accurately tracking dynamic atmospheric variations.
"""
            },
            {
                "qid": "res-q10",
                "marks": 7,
                "type": "Descriptive",
                "title": "Grid-Tied vs Stand-Alone Solar PV Systems: Balance of Systems, Inverter Topologies, and Charge Controllers",
                "yt_query": "grid tied vs standalone solar pv system balance of systems charge controllers inverters",
                "img_path": "images/res/grid_tied_vs_standalone.png",
                "img_caption": "Figure 2.5: Block Diagrams of Grid-Connected and Stand-Alone Photovoltaic Systems with Balance of Systems",
                "answer": r"""
Photovoltaic power generation systems are fundamentally categorized into Grid-Tied (Grid-Connected) and Stand-Alone (Off-Grid) systems depending on their operational interface with the utility electrical grid.

1. Stand-Alone (Off-Grid) Solar PV Systems:
- Architecture: Designed to operate autonomously without any electrical connection to the utility grid, commonly deployed in remote rural areas, telecommunication towers, and navigational aids.
- Core Components:
  1. PV Generator Array: Converts solar photons into DC electrical power.
  2. Solar Charge Controller: Regulates the DC power coming from the array to properly charge an electrochemical battery bank without overcharging or deep discharge. Two types exist:
     - Pulse Width Modulation (PWM) Controllers: Direct switch connection; clamps panel voltage down to battery voltage, losing potential power ($20\% \text{ to } 30\%$ optical mismatch loss).
     - MPPT Controllers: Incorporates a high-efficiency DC-DC buck/boost converter that tracks $V_{mp}$ and transforms excess voltage into charging current ($98\%$ conversion efficiency).
  3. Battery Energy Storage Bank: Typically deep-cycle Lead-Acid or Lithium-iron-phosphate (LFP) batteries sized to provide 2 to 3 days of autonomy during overcast periods.
  4. Off-Grid Inverter: Converts battery DC voltage ($12\text{ V}, 24\text{ V}, \text{ or } 48\text{ V}$) into regulated single-phase or three-phase AC voltage ($230\text{ V} / 400\text{ V}, 50\text{ Hz}$) to feed local household or industrial AC loads.
  5. Balance of System (BOS): DC disconnects, fuses, lightning surge arresters, wiring, and structural mounting racks.

2. Grid-Tied (On-Grid) Solar PV Systems:
- Architecture: Operates in direct parallel synchronization with the utility AC distribution grid. During daytime, power generated by the array supplies local loads first, and any surplus is exported directly into the grid. At night or during high peak loads, power is imported seamlessly from the grid.
- Key Characteristics:
  1. No battery storage is mandatory, significantly reducing initial capital investment, replacement costs, and maintenance complexity.
  2. Grid-Interactive Inverter: The central component that performs MPPT on the DC side, inverts DC into pure sinusoidal AC, and synchronizes its output frequency, phase angle, and voltage to the utility grid using Phase-Locked Loop (PLL) algorithms.
  3. Anti-Islanding Protection: A mandatory IEEE 1547 / IEC 62116 safety requirement. If utility grid power fails, the inverter must disconnect within $2.0 \text{ seconds}$ to prevent powering a de-energized line section (islanding), protecting utility lineworkers from lethal electrocution.
  4. Net-Metering System: A bidirectional energy meter that logs import and export kWh for financial settlement.

3. Grid-Tied Inverter Topologies:
- Central Inverter: A single large inverter ($100\text{ kW to several MW}$) connected to dozens of parallel strings. Economical for large utility-scale plants, but prone to high mismatch losses under partial shading and represents a single point of catastrophic failure.
- String Inverter: Multiple dedicated inverters ($3\text{ kW to } 50\text{ kW}$), each connected to 1 to 4 strings with independent MPPT tracking channels. High reliability and modularity.
- Micro-Inverters: A miniature inverter ($250\text{ W to } 400\text{ W}$) mounted directly on the back of each individual PV panel. Fully eliminates mismatch and partial shading losses across the array, but incurs higher initial equipment cost per installed watt.
"""
            }
        ]
    },
    {
        "module_id": "res-m3",
        "module_num": "Module 3",
        "module_title": "Wind Energy Conversion Systems",
        "questions": [
            {
                "qid": "res-q11",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Power in the Wind Equation and Derivation of the Betz Limit (Cp = 16/27 = 0.593)",
                "yt_query": "power in wind betz limit derivation actuator disc theory",
                "img_path": "images/res/betz_limit_actuator_disc.png",
                "img_caption": "Figure 3.1: One-Dimensional Actuator Disc Control Volume for Betz Limit Derivation",
                "answer": r"""
To quantify the maximum aerodynamic power that can theoretically be extracted from an unconstrained wind stream by a wind turbine, we apply Lanchester-Betz One-Dimensional Actuator Disc Theory based on the conservation laws of mass, momentum, and energy.

1. Total Kinetic Power Available in the Wind Stream:
Consider an air parcel of density $\rho$ moving with undisturbed upstream velocity $v$ through a cross-sectional area $A$. The mass of air traversing area $A$ per second (mass flow rate $\dot{m}$) is:
$$\dot{m} = \rho A v$$
The kinetic energy $E_k$ of a mass $m$ is $E_k = \frac{1}{2} m v^2$. Therefore, the total kinetic power $P_w$ passing through area $A$ without any mechanical obstruction is:
$$P_w = \frac{1}{2} \dot{m} v^2 = \frac{1}{2} (\rho A v) v^2 = \frac{1}{2} \rho A v^3$$
For a standard horizontal-axis wind turbine with rotor blade radius $R$, the swept circular area is $A = \pi R^2$. Hence:
$$P_w = \frac{1}{2} \rho \pi R^2 v^3$$
This fundamental equation demonstrates that wind power is proportional to the air density $\rho$, proportional to the square of the rotor radius ($R^2$), and critically proportional to the cube of the wind velocity ($v^3$). Doubling the wind speed increases the available kinetic power by a factor of eight ($2^3 = 8$).

2. Derivation of the Betz Limit:
A wind turbine extracts mechanical energy by decelerating the wind stream. Let:
- $v_1$ be the undisturbed upstream wind speed ahead of the turbine rotor,
- $v$ be the wind velocity directly passing through the rotor actuator disc plane,
- $v_2$ be the downstream wake velocity far behind the rotor.
By the continuity equation for steady, incompressible flow:
$$\dot{m} = \rho A_1 v_1 = \rho A v = \rho A_2 v_2$$

Applying Newton's Second Law, the total aerodynamic thrust force $T$ exerted by the wind on the rotor disc equals the rate of change of linear momentum:
$$T = \dot{m} (v_1 - v_2) = \rho A v (v_1 - v_2)$$
Simultaneously, from the application of Bernoulli's equation upstream and downstream of the actuator disc, the mechanical power extracted by the rotor disc is the thrust force multiplied by the velocity across the disc:
$$P = T \cdot v = \dot{m} (v_1 - v_2) v$$
From the conservation of energy, the rate of kinetic energy extraction from the fluid stream between the far upstream and far downstream states is:
$$P = \frac{1}{2} \dot{m} (v_1^2 - v_2^2)$$
Equating both expressions for mechanical power:
$$\dot{m} (v_1 - v_2) v = \frac{1}{2} \dot{m} (v_1^2 - v_2^2) = \frac{1}{2} \dot{m} (v_1 - v_2)(v_1 + v_2)$$
Dividing by $\dot{m} (v_1 - v_2)$ yields Froude's theorem:
$$v = \frac{v_1 + v_2}{2}$$
This proves that the wind velocity through the rotor disc is the simple arithmetic mean of the undisturbed upstream velocity $v_1$ and the downstream wake velocity $v_2$.

We define the Axial Induction Factor (or axial interference factor) $a$ as the fractional reduction in wind velocity between upstream and the rotor plane:
$$a = \frac{v_1 - v}{v_1} \implies v = v_1(1 - a)$$
Substituting $v = \frac{v_1 + v_2}{2}$ into this expression gives the wake velocity:
$$v_1(1 - a) = \frac{v_1 + v_2}{2} \implies v_2 = v_1 (1 - 2a)$$
The mass flow rate through the turbine rotor is:
$$\dot{m} = \rho A v = \rho A v_1 (1 - a)$$
The extracted mechanical power becomes:
$$P = \frac{1}{2} \dot{m} (v_1^2 - v_2^2) = \frac{1}{2} \left[ \rho A v_1 (1 - a) \right] \left[ v_1^2 - v_1^2(1 - 2a)^2 \right]$$
Expanding $(1 - 2a)^2 = 1 - 4a + 4a^2$:
$$v_1^2 - v_1^2(1 - 4a + 4a^2) = v_1^2 [1 - (1 - 4a + 4a^2)] = v_1^2 (4a - 4a^2) = 4a(1 - a) v_1^2$$
Substituting back into the power expression:
$$P = \frac{1}{2} \rho A v_1^3 \cdot 4a (1 - a)^2$$
The Power Coefficient $C_p$ is defined as the fraction of available wind power extracted by the rotor:
$$C_p = \frac{P}{P_w} = \frac{P}{\frac{1}{2} \rho A v_1^3} = 4a (1 - a)^2 = 4a (1 - 2a + a^2) = 4a - 8a^2 + 4a^3$$

To determine the maximum theoretical power coefficient, we differentiate $C_p$ with respect to the induction factor $a$ and equate to zero:
$$\frac{dC_p}{da} = 4 - 16a + 12a^2 = 0 \implies 3a^2 - 4a + 1 = 0$$
Factoring this quadratic equation:
$$(3a - 1)(a - 1) = 0$$
Physical bounds require $0 \le a \le 0.5$. Thus, the physically valid solution is:
$$a = \frac{1}{3}$$
Substituting $a = \frac{1}{3}$ into the $C_p$ expression:
$$C_{p,\max} = 4\left(\frac{1}{3}\right) \left(1 - \frac{1}{3}\right)^2 = \frac{4}{3} \times \left(\frac{2}{3}\right)^2 = \frac{4}{3} \times \frac{4}{9} = \frac{16}{27} \approx 0.5926$$
Thus, the celebrated Betz Limit states that no unconstrained wind turbine rotor can convert more than $\frac{16}{27}$ ($59.26\%$) of the kinetic energy in the wind into useful mechanical power:
$$\mathbf{C_{p,\max} = \frac{16}{27} \approx 59.26\%}$$
"""
            },
            {
                "qid": "res-q12",
                "marks": 7,
                "type": "Descriptive",
                "title": "Horizontal Axis Wind Turbine (HAWT) vs Vertical Axis Wind Turbine (VAWT): Aerodynamics, Lift vs Drag, Tip-Speed Ratio",
                "yt_query": "horizontal axis wind turbine vs vertical axis HAWT VAWT tip speed ratio lift drag",
                "img_path": "images/res/hawt_vs_vawt_aerodynamics.png",
                "img_caption": "Figure 3.2: Structural Comparison of HAWT and VAWT (Savonius & Darrieus) with Aerodynamic Lift/Drag Vectors",
                "answer": r"""
Wind energy conversion systems are classified according to the geometric orientation of their rotor axis of rotation into Horizontal Axis Wind Turbines (HAWT) and Vertical Axis Wind Turbines (VAWT).

1. Horizontal Axis Wind Turbine (HAWT):
- Configuration: The main rotor shaft and electrical generator are installed horizontally at the top of a tall tubular steel tower. The rotor planes are oriented perpendicular to the oncoming wind direction.
- Aerodynamic Principle: Exclusively lift-based machines. The rotor blades are shaped with aerodynamic airfoil cross-sections. As wind flows over the airfoil, a pressure difference develops between the upper curved suction surface and lower pressure surface, creating aerodynamic Lift ($F_L$) perpendicular to the relative wind stream and a small parasitic Drag ($F_D$) parallel to it. Modern blades operate at high lift-to-drag ratios ($C_L / C_D > 50$), generating strong rotational aerodynamic torque.
- Tip-Speed Ratio ($\lambda$): Operates at high tip-speed ratios ($\lambda \approx 7 \text{ to } 10$), where:
$$\lambda = \frac{\omega R}{v}$$
where $\omega$ is rotor angular velocity, $R$ is blade tip radius, and $v$ is wind velocity. High $\lambda$ allows slender, low-solidity blades with high power coefficients ($C_p \approx 0.45 \text{ to } 0.50$).
- Advantages: Elevated hub height captures higher-velocity, less turbulent winds ($v \propto h^\alpha$); high aerodynamic efficiency; active pitch and yaw control.
- Disadvantages: Massive nacelle and generator located atop the tower require heavy cranes; requires active yaw drive mechanism to track wind direction.

2. Vertical Axis Wind Turbine (VAWT):
- Configuration: The rotor shaft is mounted vertically, perpendicular to the ground and independent of wind direction. The generator and gearbox can be mounted at ground level.
- Classification:
  a. Savonius Rotor (Drag-based): S-shaped cross section with two overlapping semicircular cups. Operates on differential drag between the concave side ($C_D \approx 1.2$) and convex side ($C_D \approx 0.3$). Characterized by very high starting torque, low tip-speed ratio ($\lambda < 1.0$), and low efficiency ($C_p \approx 0.15 \text{ to } 0.20$). Ideal for water pumping.
  b. Darrieus Rotor (Lift-based): Egg-beater curved blades or straight vertical H-rotor blades with symmetric airfoils. As the blades rotate around the vertical axis, they experience varying angles of attack, generating net positive lift torque over each revolution. Operates at medium tip-speed ratios ($\lambda \approx 3 \text{ to } 5$) with $C_p \approx 0.30 \text{ to } 0.35$. Not self-starting; requires an auxiliary starting motor.
- Advantages: Omnidirectional operation (accepts wind from any direction without needing a yaw mechanism); generator and drive train at ground level for easy maintenance; lower tower structural costs.
- Disadvantages: Operates in slower, turbulent ground-level winds; blades experience cyclic fatigue loading every $360^\circ$ rotation; lower peak aerodynamic efficiency than modern HAWTs.

Comprehensive Comparison Table:
| Parameter | Horizontal Axis Wind Turbine (HAWT) | Vertical Axis Wind Turbine (VAWT) |
|---|---|---|
| Rotor Axis | Horizontal (parallel to ground) | Vertical (perpendicular to ground) |
| Wind Directionality | Needs active Yaw system | Omnidirectional (no yaw required) |
| Aerodynamic Mechanism | Pure aerodynamic lift | Savonius: Drag; Darrieus: Lift |
| Tip Speed Ratio ($\lambda$) | High ($\lambda = 6 - 10$) | Savonius: $\lambda < 1$; Darrieus: $\lambda = 3 - 5$ |
| Peak Power Coeff. ($C_p$) | High ($0.45 - 0.50$) | Moderate ($0.15 - 0.35$) |
| Generator Location | Atop tower inside nacelle | At ground level base |
| Starting Torque | Good (with active pitch) | Savonius: High; Darrieus: Zero (needs start aid) |
| Cyclic Blade Fatigue | Lower cyclic reversals | Severe cyclic aerodynamic fatigue |
"""
            },
            {
                "qid": "res-q13",
                "marks": 7,
                "type": "Descriptive",
                "title": "Major Electromechanical Components of a Grid-Connected Utility-Scale HAWT",
                "yt_query": "components of wind turbine nacelle drive train gearbox yaw pitch generator",
                "img_path": "images/res/hawt_components_cutaway.png",
                "img_caption": "Figure 3.3: Cutaway Engineering Diagram of a Modern Utility-Scale Horizontal Axis Wind Turbine Nacelle",
                "answer": r"""
A modern grid-connected utility-scale Horizontal Axis Wind Turbine (typically rated from $2\text{ MW to } 6\text{ MW}$) is a complex mechatronic system designed to operate reliably under extreme meteorological conditions. Its primary structural, mechanical, and electrical components include:

1. Rotor Blades and Hub:
- Blades: Modern utility turbines utilize three glass-fiber or carbon-fiber reinforced epoxy blades ($50 \text{ to } 90\text{ meters}$ in length). They feature aerodynamic airfoil cross-sections with built-in aerodynamic twist from root to tip to maintain optimal angle of attack.
- Hub: Cast ductile iron structure that mechanically joins the three blade roots to the main low-speed shaft. Contains internal pitch bearings, electric or hydraulic pitch actuators, and pitch backup batteries.

2. Drive Train and Nacelle Components:
The nacelle is the housing structure mounted atop the tower that encloses the drive train:
- Low-Speed Shaft (Main Shaft): Transmits aerodynamic rotational torque from the rotor hub into the gearbox at slow speeds (typically $8 \text{ to } 18\text{ rpm}$). Supported by massive spherical roller main bearings.
- Gearbox: A multi-stage mechanical speed increaser (combining planetary epicyclic stages and parallel helical spur stages). It steps up the low rotational speed from $\approx 15\text{ rpm}$ up to high generator speeds of $\approx 1500\text{ rpm}$ (a speed step-up ratio of approximately $1:100$). Note: Direct-drive turbines eliminate the gearbox entirely, using large-diameter multipole low-speed generators.
- Mechanical Brake: A high-capacity aerodynamic disc brake mounted on the high-speed shaft used as a secondary safety holding mechanism during maintenance or extreme emergency shut-down. Primary aerodynamic braking is achieved via blade pitch feathering.
- High-Speed Shaft: Connects the gearbox output to the electrical generator shaft, fitted with flexible elastomeric couplings to isolate torsional vibration spikes.

3. Electrical Generator and Power Converter:
- Generator: Converts mechanical rotational power into electrical energy. Most modern multi-megawatt installations employ either a Doubly Fed Induction Generator (DFIG) or a Permanent Magnet Synchronous Generator (PMSG).
- Power Electronic Converter: A four-quadrant back-to-back AC-DC-AC converter using high-power IGBT switches that decouples grid frequency ($50\text{ Hz}$) from variable mechanical rotor speed, delivering fully controlled active and reactive power.

4. Control and Auxiliary Subsystems:
- Pitch Control Mechanism: Independent electric servomotors at each blade root that rotate the blade along its longitudinal axis to regulate angle of attack, control aerodynamic power capture, and feather the blades to a complete aerodynamic stop.
- Yaw Mechanism: Large ring gear and electric yaw drive motors situated at the tower-nacelle interface. Using input from ultrasonic wind vanes on the nacelle roof, the yaw system continuously rotates the entire nacelle to keep the rotor plane facing perpendicular to oncoming wind.
- Wind Sensors (Anemometer & Wind Vane): Mounted on the rear roof of the nacelle to measure wind speed and directional misalignment.
- Tubular Steel Tower: A conical rolled-steel cylindrical structure ($80 \text{ to } 140\text{ meters}$ tall) that supports the nacelle and houses the step-up transformer ($690\text{ V} / 33\text{ kV}$), power cables, switchgear, and service elevators.
"""
            },
            {
                "qid": "res-q14",
                "marks": 7,
                "type": "Descriptive",
                "title": "Generators for Wind Turbines: Doubly-Fed Induction Generator (DFIG) vs Permanent Magnet Synchronous Generator (PMSG)",
                "yt_query": "DFIG vs PMSG wind turbine generator working operation slip power",
                "img_path": "images/res/dfig_vs_pmsg_topologies.png",
                "img_caption": "Figure 3.4: Electrical Topologies of (a) DFIG with Partial-Scale Converter and (b) PMSG with Full-Scale Converter",
                "answer": r"""
Modern utility-scale wind turbines operate at variable rotational speed to maximize aerodynamic efficiency ($C_p$) across varying wind conditions. The two dominant generator technologies employed globally are the Doubly-Fed Induction Generator (DFIG) and the Permanent Magnet Synchronous Generator (PMSG).

1. Doubly-Fed Induction Generator (DFIG):
- Construction & Topology: The DFIG is a wound-rotor induction machine whose stator three-phase windings are connected directly to the $50\text{ Hz}$ medium-voltage electrical grid via a step-up transformer. The rotor three-phase windings are connected to the grid through carbon slip rings and a bidirectional back-to-back partial-scale IGBT converter consisting of a Rotor-Side Converter (RSC) and a Grid-Side Converter (GSC) linked by a common DC bus.
- Converter Sizing: Because the partial-scale converter only needs to handle slip power ($P_{rotor} = s \cdot P_{stator}$), and operating slip is limited to approximately $\pm 30\%$ ($s = \frac{N_s - N_r}{N_s} \in [-0.30, +0.30]$), the power electronic converter rating is only approximately $25\% \text{ to } 30\%$ of the total machine nominal power rating. This drastically lowers converter capital cost and power electronic losses.
- Operational Modes:
  - Sub-synchronous Mode ($N_r < N_s$, positive slip $s > 0$): Rotor absorbs electrical slip power from the grid through the converter, while stator delivers net generated power ($P_{net} = P_{stator} - P_{rotor}$).
  - Super-synchronous Mode ($N_r > N_s$, negative slip $s < 0$): Both stator and rotor deliver power simultaneously to the utility grid ($P_{net} = P_{stator} + |P_{rotor}|$).
- Control Capabilities: Decoupled vector control (stator flux-oriented control) enables independent four-quadrant regulation of active power ($P$) and reactive power ($Q$) for grid voltage support.
- Drawbacks: Slip rings and brush gear require periodic maintenance and replacement; requires a multi-stage high-ratio gearbox; vulnerable to grid voltage dips (requires active crowbar circuits for Fault Ride Through).

2. Permanent Magnet Synchronous Generator (PMSG):
- Construction & Topology: Employs a multi-pole synchronous rotor energized by high-coercivity rare-earth permanent magnets (Neodymium-Iron-Boron, NdFeB), completely eliminating rotor excitation copper losses, DC field exciters, and slip rings. The stator is connected to the grid through a Full-Scale Converter (FSC) rated for $100\%$ of total turbine output power.
- Operational Characteristics: Often realized as a Direct-Drive (gearless) system with a very large pole count (e.g., 60 to 80 poles). The rotor is coupled directly to the wind turbine hub, rotating at slow speed ($10 \text{ to } 15\text{ rpm}$).
- Advantages: Eliminating the heavy mechanical gearbox removes the single most frequent source of mechanical failure and maintenance downtime in offshore installations; superior low-voltage fault ride-through (LVRT) performance because the full converter completely decouples the generator from grid transient disturbances; higher electrical efficiency across partial loads.
- Drawbacks: The full-scale power converter must be rated for $100\%$ machine capacity, increasing capital expenditure; direct-drive generator is physically massive in diameter ($4 \text{ to } 6\text{ meters}$) and heavy; permanent magnets are susceptible to thermal demagnetization under severe short-circuits and carry high material supply chain costs.

Comprehensive Comparison:
| Feature | Doubly-Fed Induction Generator (DFIG) | Permanent Magnet Synchronous Generator (PMSG) |
|---|---|---|
| Converter Rating | Partial-scale ($25\% - 30\%$ of rated power) | Full-scale ($100\%$ of rated power) |
| Drive Train | Requires multi-stage speed-up gearbox | Can be Direct-Drive (no gearbox) or medium-speed |
| Slip Rings & Brushes | Yes (wound rotor requires periodic maintenance) | None (brushless design) |
| Electrical Efficiency | High at rated speed; lower at low wind | Superior across wide partial-load range |
| Capital Cost | Lower initial power electronics cost | Higher converter and rare-earth magnet cost |
| Grid Fault Compliance | Requires crowbar and DC chopper protection | Excellent (full decoupling by DC link capacitor) |
"""
            },
            {
                "qid": "res-q15",
                "marks": 7,
                "type": "Descriptive",
                "title": "Wind Turbine Power Control Strategies: Pitch, Stall, Yaw Control, and Power Curve Operating Regions",
                "yt_query": "wind turbine power curve pitch control stall control yaw regions",
                "img_path": "images/res/wind_turbine_power_curve.png",
                "img_caption": "Figure 3.5: Idealized Wind Turbine Power Curve Depicting Operating Control Regions 1 through 4",
                "answer": r"""
To extract maximum energy safely without exceeding structural and electrical design thresholds across fluctuating wind speeds, wind turbines incorporate multi-level aerodynamic and electromechanical control strategies.

Wind Turbine Power Curve Operating Regions:
The operational envelope of a utility wind turbine is standardly delineated across four distinct wind speed regimes:
1. Region 1 (Below Cut-In Speed, $v < v_{cut-in}$):
Wind speed is insufficient to overcome internal bearing friction and generate net positive electrical power ($v_{cut-in} \approx 3 \text{ to } 4\text{ m/s}$). The turbine remains parked with blades pitched out of the wind.
2. Region 2 (Partial Load / MPPT Region, $v_{cut-in} \le v \le v_{rated}$):
Wind speed is between cut-in and rated velocity ($v_{rated} \approx 11 \text{ to } 13\text{ m/s}$). The control objective is Maximum Energy Capture. The blade pitch angle is held fixed at its aerodynamically optimal angle ($\beta \approx 0^\circ$), and generator electromagnetic torque is adjusted in proportion to the square of rotor speed ($T_e = k_{opt} \omega^2$) to maintain the optimal Tip-Speed Ratio ($\lambda_{opt}$), operating at maximum power coefficient ($C_{p,\max}$).
3. Region 3 (Full Load / Rated Power Region, $v_{rated} < v \le v_{cut-out}$):
Wind speed exceeds rated velocity but is below cut-out ($v_{cut-out} \approx 25\text{ m/s}$). The available wind power exceeds the structural and electrical rating of the generator and converter. The control objective is Power Limitation to constant rated capacity ($P = P_{rated}$). Active blade pitch control continuously feathers the blades to shed excess aerodynamic lift.
4. Region 4 (Above Cut-Out Speed, $v > v_{cut-out}$):
Extreme high-wind conditions ($v > 25\text{ m/s}$, gale/storm conditions). Operating the turbine risks catastrophic structural failure from excessive thrust. The turbine is tripped, blades are fully feathered ($\beta = 90^\circ$) to stall rotation, and the mechanical yaw system turns the nacelle to minimize aerodynamic drag until wind speeds subside.

Aerodynamic Power Regulation Methods:
1. Active Pitch Control:
Modern utility HAWTs feature independent electric servomotors at each blade root that rotate the blade along its longitudinal axis. In Region 3, as wind velocity rises, the controller rotates the blade leading edge into the wind (feathering, increasing $\beta$). This decreases the aerodynamic angle of attack ($\alpha = \phi - \beta$), reducing aerodynamic lift force and maintaining steady rated electrical power and thrust force. It provides smooth power control and full aerodynamic braking during shutdown.

2. Stall Control:
- Passive Stall: Blades are aerodynamically designed with fixed geometry such that when wind speed exceeds rated velocity, the angle of attack naturally increases beyond the stall margin. Flow separation occurs over the upper airfoil surface, destroying lift and dramatically increasing drag. It requires no moving pitch actuators, but power regulation is coarse and sensitive to blade surface soiling and air density.
- Active Stall (Combi Stall): Incorporates blade pitch drives that rotate the blades toward deeper stall (decreasing pitch angle into stall) rather than toward feathering. Provides tighter power control than passive stall.

3. Yaw Control:
Driven by electric gear motors located at the tower-nacelle junction. Using signals from nacelle wind vanes, the yaw mechanism continuously tracks low-frequency directional shifts in the wind, keeping the rotor swept plane oriented perpendicular to the wind vector. Yaw rotation is intentionally slow ($0.5^\circ \text{ to } 1.0^\circ \text{ per second}$) to avoid inducing destructive gyroscopic moments on the main shaft bearings.
"""
            }
        ]
    },
    {
        "module_id": "res-m4",
        "module_num": "Module 4",
        "module_title": "Biomass Energy & Ocean Energy Systems",
        "questions": [
            {
                "qid": "res-q16",
                "marks": 7,
                "type": "Descriptive",
                "title": "Biomass Energy Conversion Technologies: Direct Combustion, Gasification, and Pyrolysis",
                "yt_query": "biomass conversion gasification pyrolysis combustion syngas biochar",
                "img_path": "images/res/biomass_conversion_routes.png",
                "img_caption": "Figure 4.1: Thermochemical and Biochemical Conversion Pathways of Lignocellulosic Biomass",
                "answer": r"""
Biomass encompasses all organic matter derived from plants and animals (agricultural residues, forestry waste, animal manure, dedicated energy crops, and municipal solid wastes). Because biomass fixes atmospheric carbon dioxide through photosynthesis, it represents a dispatchable, carbon-neutral renewable energy resource. The primary thermochemical conversion technologies include Direct Combustion, Gasification, and Pyrolysis.

1. Direct Combustion:
- Principle: The complete oxidation of solid biomass fuel in the presence of excess air ($100\% \text{ to } 150\%$ excess stoichiometric oxygen) at high temperatures ($800^\circ\text{C} \text{ to } 1100^\circ\text{C}$).
$$\text{Biomass } (C_x H_y O_z) + O_2 \to CO_2 + H_2 O + \text{Ash} + \text{Heat}$$
- Equipment: Grate-fired boilers, pulverized fuel burners, and Fluidized Bed Combustion (FBC) boilers. The generated high-pressure steam expands through a Rankine cycle steam turbine-generator set to produce electricity or combined heat and power (CHP).
- Limitations: Requires low moisture content ($< 20\% - 30\%$); generates particulate fly ash and $NO_x$ emissions; lower electrical efficiency ($18\% - 25\%$) at small scales.

2. Biomass Gasification:
- Principle: The partial thermal oxidation of solid carbonaceous biomass in a substoichiometric oxygen environment (equivalence ratio $\lambda \approx 0.25 \text{ to } 0.35$) at elevated temperatures ($750^\circ\text{C} \text{ to } 1200^\circ\text{C}$) to produce a clean, combustible gaseous mixture called Producer Gas or Synthesis Gas (Syngas).
- Fundamental Chemical Reactions:
  1. Combustion (Exothermic): $C + O_2 \to CO_2 \quad (\Delta H = -393.8\text{ kJ/mol})$
  2. Boudouard Reaction (Endothermic): $C + CO_2 \rightleftharpoons 2 CO \quad (\Delta H = +172.6\text{ kJ/mol})$
  3. Water-Gas Reaction (Endothermic): $C + H_2 O \rightleftharpoons CO + H_2 \quad (\Delta H = +131.3\text{ kJ/mol})$
  4. Methanation Reaction (Exothermic): $C + 2 H_2 \rightleftharpoons CH_4 \quad (\Delta H = -74.8\text{ kJ/mol})$
  5. Water-Gas Shift Reaction: $CO + H_2 O \rightleftharpoons CO_2 + H_2 \quad (\Delta H = -41.2\text{ kJ/mol})$
The resulting producer gas consists primarily of Carbon Monoxide ($CO \approx 18-22\%$), Hydrogen ($H_2 \approx 15-20\%$), Methane ($CH_4 \approx 2-4\%$), Carbon Dioxide ($CO_2 \approx 10-12\%$), and Nitrogen ($N_2 \approx 45-50\%$ when air is used as gasifying agent), having a Lower Heating Value (LHV) of $4.5 \text{ to } 6.0\text{ MJ/Nm}^3$. It can fuel internal combustion engines or gas turbines directly.
- Gasifier Types:
  - Updraft (Counter-current): Biomass moves down, gasifying air enters from bottom. High thermal efficiency, but producer gas contains heavy tar ($50 \text{ to } 100\text{ g/Nm}^3$).
  - Downdraft (Co-current): Biomass and air move downward through a throat constriction. Tars pass through high-temperature glowing char bed and crack into light gases, producing very low tar content ($< 1\text{ g/Nm}^3$), making it ideal for engine operation.
  - Fluidized Bed Gasifiers: Bubbling and circulating fluidized beds for high-throughput multi-megawatt industrial applications.

3. Pyrolysis:
- Principle: The irreversible thermal decomposition of organic matter in the complete absence of oxygen at temperatures between $300^\circ\text{C}$ and $650^\circ\text{C}$, breaking complex lignocellulosic polymers (cellulose, hemicellulose, lignin) into solid, liquid, and gaseous fuels.
- Classification:
  - Slow Pyrolysis (Carbonization): Low heating rate ($< 10^\circ\text{C}/\text{min}$), long vapor residence time (hours), moderate temperatures ($400^\circ\text{C}$). Maximizes solid Biochar ($35\%$) and non-condensable fuel gas.
  - Fast Pyrolysis: High heating rates ($> 1000^\circ\text{C}/\text{s}$), very short vapor residence time ($< 2 \text{ seconds}$), rapid cooling/quenching, temperature $\approx 500^\circ\text{C}$. Yields up to $60\% \text{ to } 75\%$ liquid Bio-Oil (pyrolysis oil), an oxygenated synthetic crude oil that can be refined into drop-in transportation biofuels.
"""
            },
            {
                "qid": "res-q17",
                "marks": 7,
                "type": "Descriptive",
                "title": "Biogas Production through Anaerobic Digestion: Biochemical Stages and Environmental Factors",
                "yt_query": "anaerobic digestion biogas stages hydrolysis acidogenesis acetogenesis methanogenesis",
                "img_path": "images/res/anaerobic_digestion_stages.png",
                "img_caption": "Figure 4.2: Four Sequential Biochemical Stages of Anaerobic Digestion for Biogas Synthesis",
                "answer": r"""
Biogas is a clean, renewable combustible fuel gas generated through the biological decomposition of organic wastes (animal dung, food waste, sewage sludge) by specialized bacterial consortia in an airtight, oxygen-free environment. High-quality biogas consists primarily of $55\% \text{ to } 70\%$ Methane ($CH_4$), $30\% \text{ to } 40\%$ Carbon Dioxide ($CO_2$), and trace quantities of Nitrogen ($N_2$), Hydrogen ($H_2$), and Hydrogen Sulfide ($H_2 S$). It has a calorific value of approximately $20 \text{ to } 26\text{ MJ/m}^3$.

Four Sequential Biochemical Stages of Anaerobic Digestion:
Anaerobic degradation proceeds through a closely coupled microbial metabolic chain:

1. Stage 1: Hydrolysis:
Complex, high-molecular-weight insoluble organic polymers (carbohydrates, proteins, fats/lipids) are enzymatically cleaved into soluble monomers (monosaccharides, amino acids, fatty acids, glycerol) by extracellular hydrolytic enzymes (cellulases, proteases, lipases) secreted by facultative anaerobic bacteria:
$$[C_6 H_{10} O_5]_n + n H_2 O \xrightarrow{\text{hydrolytic bacteria}} n C_6 H_{12} O_6$$
Hydrolysis is generally the rate-limiting step for recalcitrant, solid lignocellulosic feedstocks.

2. Stage 2: Acidogenesis (Fermentation):
The soluble monomers are absorbed by acidogenic (fermentative) bacteria and converted into volatile fatty acids (VFAs, such as acetic, propionic, butyric, and valeric acids), lactic acid, alcohols, and gases like $CO_2$ and $H_2$:
$$C_6 H_{12} O_6 \xrightarrow{\text{acidogenic bacteria}} 2 CH_3 CH_2 COOH + 2 H_2 O$$

3. Stage 3: Acetogenesis:
Acetogenic bacteria (homoacetogens and syntrophic acetogens) metabolize the higher-order volatile fatty acids and alcohols into Acetic Acid ($CH_3 COOH$), along with additional $CO_2$ and hydrogen gas ($H_2$):
$$CH_3 CH_2 COOH + 2 H_2 O \xrightarrow{\text{acetogenic bacteria}} CH_3 COOH + CO_2 + 3 H_2$$
Acetogenic bacteria require extremely low partial pressure of hydrogen to make the reaction thermodynamically favorable ($\Delta G^\circ < 0$).

4. Stage 4: Methanogenesis:
Strictly obligate anaerobic Archaea (methanogens) convert the simple acetate, hydrogen, and carbon dioxide into methane gas via two distinct pathways:
- Acetoclastic Methanogenesis (accounts for $\approx 70\%$ of methane yield):
$$CH_3 COOH \xrightarrow{\text{acetoclastic methanogens}} CH_4 + CO_2$$
- Hydrogenotrophic Methanogenesis (accounts for $\approx 30\%$ of methane yield):
$$CO_2 + 4 H_2 \xrightarrow{\text{hydrogenotrophic methanogens}} CH_4 + 2 H_2 O$$

Critical Environmental and Operational Factors:
1. Carbon-to-Nitrogen Ratio (C/N Ratio): The optimal C/N ratio for anaerobic digestion is $25:1 \text{ to } 30:1$. A C/N ratio that is too high causes rapid nitrogen exhaustion, slowing digestion; a C/N ratio that is too low ($< 15:1$, excessive nitrogen) causes excessive ammonium accumulation, leading to ammonia toxicity that inhibits methanogens.
2. Temperature: Methanogens are highly sensitive to thermal fluctuations. Digestion occurs in two optimal zones:
   - Mesophilic Range: $35^\circ\text{C} \text{ to } 38^\circ\text{C}$ (stable, robust, commonly used).
   - Thermophilic Range: $50^\circ\text{C} \text{ to } 55^\circ\text{C}$ (faster reaction rates and pathogen destruction, but highly sensitive to temperature shocks).
3. pH and Buffering Capacity: Methanogenic Archaea thrive strictly within a narrow neutral pH range of $6.8 \text{ to } 7.5$. If acidogenesis outpaces methanogenesis, volatile fatty acids accumulate, causing the digester pH to drop below $6.2$ (digester souring), which halts methanogenesis entirely.
4. Hydraulic Retention Time (HRT): The average residence time the slurry spends inside the reactor ($30 \text{ to } 50\text{ days}$ under mesophilic conditions in tropical regions).
"""
            },
            {
                "qid": "res-q18",
                "marks": 7,
                "type": "Descriptive",
                "title": "Biogas Plant Construction & Comparison: Floating Drum (KVIC) vs Fixed Dome (Janata / Deenabandhu)",
                "yt_query": "floating drum kvic vs fixed dome deenabandhu biogas plant comparison",
                "img_path": "images/res/kvic_vs_deenabandhu.png",
                "img_caption": "Figure 4.3: Engineering Cross-Sections of (a) KVIC Floating Drum and (b) Deenabandhu Fixed Dome Biogas Plants",
                "answer": r"""
Small-to-medium scale rural and institutional biogas installations in India are dominated by two classical designs developed under national renewable energy programs: the Floating Drum type (KVIC design) and the Fixed Dome type (Janata and Deenabandhu designs).

1. Floating Drum Type (KVIC Model):
Developed by the Khadi and Village Industries Commission (KVIC), this model features an inverted floating gas holder drum.
- Construction Details:
  - Digester Pit: An underground cylindrical masonry well made of brick masonry and cement mortar, divided vertically into two chambers by a central partition wall.
  - Inlet and Outlet Pipes: Sloping cement concrete or PVC pipes positioned on opposite sides. The inlet pipe feeds fresh cow dung slurry ($1:1$ ratio with water) to the bottom of the inlet chamber, and digested slurry overflows automatically from the outlet chamber.
  - Gas Holder Drum: An inverted cylindrical drum fabricated from mild steel (MS) sheet metal or fiber-reinforced plastic (FRP). The drum is guided along a central vertical guide pipe, resting inverted over the digester slurry.
- Working Principle: As anaerobic bacteria generate biogas, gas bubbles rise and accumulate under the floating drum. The trapped gas volume causes the drum to float and rise vertically along the central guide axis. When gas is consumed at the kitchen stove or engine, the drum settles downward.
- Gas Pressure: The gas pressure remains completely constant at all times, dictated strictly by the structural weight of the metal drum ($8 \text{ to } 12\text{ cm of water column}$).

2. Fixed Dome Type (Deenabandhu Model):
Developed by Action for Food Production (AFPRO), this design eliminates all moving metallic components to maximize durability and reduce capital expenditure.
- Construction Details:
  - The entire structure is constructed underground from brick masonry in the form of two intersecting spherical dome segments.
  - Bottom Segment: A shallow curved concave masonry floor.
  - Digester Wall & Top Roof: A rigid hemispherical masonry dome plastered internally with multiple coats of cement-mortar and acrylic sealant to prevent gas permeability.
  - Slurry Inlet and Outlet Tanks: Connected by large-diameter sloping channels. The outlet tank is designed as an elevated rectangular displacement chamber.
- Working Principle: The digester is filled completely with slurry up to the base of the upper dome. As biogas is produced by fermentation, it accumulates in the upper fixed volume of the masonry dome. Because the dome volume is fixed and gas cannot escape, the gas exerts pressure downward onto the slurry surface, forcing a large volume of digested slurry upward through the outlet gate into the elevated displacement chamber. When gas is consumed, the slurry flows back into the digester.
- Gas Pressure: Gas pressure is variable, fluctuating between $0\text{ cm}$ (when empty) and $100\text{ cm of water column}$ (when fully pressurized).

Comprehensive Engineering Comparison:
| Parameter | Floating Drum (KVIC) | Fixed Dome (Deenabandhu) |
|---|---|---|
| Structural Material | Masonry well + Mild Steel / FRP drum | $100\%$ underground brick masonry and cement |
| Moving Components | Floating drum moves vertically on guide pipe | None (no moving mechanical components) |
| Gas Pressure | Strictly constant (fixed by drum weight) | Highly variable ($0 \text{ to } 100\text{ cm } H_2O$) |
| Capital Cost | High (expensive steel drum accounts for $40\%$) | Low (approximately $30-40\%$ cheaper than KVIC) |
| Corrosion & Maintenance | Steel drum prone to severe corrosion; needs painting | Virtually zero corrosion; long lifespan ($> 30\text{ years}$) |
| Construction Skill | Standard masonry + metal workshop fabrication | Requires specialized skilled masons for leak-proof dome |
| Thermal Insulation | Exposed metal drum loses heat in winter | Completely underground; excellent thermal stability |
"""
            },
            {
                "qid": "res-q19",
                "marks": 7,
                "type": "Descriptive",
                "title": "Ocean Thermal Energy Conversion (OTEC): Thermodynamic Principle, Open vs Closed Cycles, and Carnot Efficiency",
                "yt_query": "ocean thermal energy conversion OTEC open cycle closed cycle carnot efficiency",
                "img_path": "images/res/otec_open_closed_cycles.png",
                "img_caption": "Figure 4.4: Thermodynamic Flowsheets of (a) Closed Rankine OTEC and (b) Open Claude Cycle OTEC",
                "answer": r"""
Ocean Thermal Energy Conversion (OTEC) is a marine renewable energy technology that exploits the solar thermal temperature gradient between warm tropical ocean surface water ($25^\circ\text{C} \text{ to } 28^\circ\text{C}$) and cold deep ocean water ($4^\circ\text{C} \text{ to } 6^\circ\text{C}$ at depths of $800 \text{ to } 1000\text{ meters}$) to drive a low-temperature heat engine and generate base-load electricity $24/7$.

Thermodynamic Principle and Carnot Limit:
Because the ocean acts as a massive thermal solar collector, the surface layer remains warm year-round, while deep ocean currents flowing from polar regions maintain near-freezing temperatures. A minimum thermal gradient of $\Delta T \approx 20^\circ\text{C}$ is standardly required for economic feasibility.
Let $T_H$ be the warm surface source temperature ($T_H = 27^\circ\text{C} = 300.15\text{ K}$) and $T_C$ be the cold deep sink temperature ($T_C = 5^\circ\text{C} = 278.15\text{ K}$).
From the Second Law of Thermodynamics, the maximum theoretical Carnot thermal efficiency $\eta_{Carnot}$ of any heat engine operating between these limits is:
$$\eta_{Carnot} = \frac{T_H - T_C}{T_H} = \frac{300.15 - 278.15}{300.15} = \frac{22}{300.15} \approx 0.0733 \implies 7.33\%$$
When practical heat exchanger temperature drops, turbine isentropic losses, and parasitic pumping power requirements (for massive seawater pumps) are accounted for, the net real-world thermal efficiency of an OTEC power plant is only approximately $2.5\% \text{ to } 4.0\%$. Consequently, immense volumetric flow rates of seawater must be continuously circulated to generate megawatts of power.

1. Closed-Cycle OTEC (Anderson / Organic Rankine Cycle):
- Working Fluid: Utilizes a low-boiling-point working fluid, typically pure anhydrous Ammonia ($NH_3$, boiling point $-33.3^\circ\text{C}$ at atmospheric pressure) or propane.
- Cycle Operation:
  1. Warm surface seawater ($26^\circ\text{C}$) is pumped through a titanium plate-and-frame evaporator, transferring heat to liquid ammonia, which vaporizes at high pressure ($\approx 9 \text{ to } 10\text{ bar}$).
  2. The pressurized ammonia vapor expands through a specialized low-pressure axial vapor turbine coupled to an electrical generator, producing shaft work.
  3. The expanded exhaust ammonia vapor enters a condenser, where it is cooled and liquefied by cold deep seawater ($5^\circ\text{C}$) pumped up from $1000\text{ m}$ depth through a massive Cold Water Pipe (CWP).
  4. Liquid ammonia is repressurized by a feed pump and returned to the evaporator, completing a closed thermodynamic loop.

2. Open-Cycle OTEC (Claude Cycle):
- Working Fluid: Warm surface seawater itself acts as the working fluid.
- Cycle Operation:
  1. Warm surface seawater ($26^\circ\text{C}$) is pumped into an evacuated Flash Evaporation Chamber maintained at deep vacuum pressure ($P_{sat} \approx 0.03\text{ bar} = 3\text{ kPa}$).
  2. Under this deep vacuum, a fraction ($\approx 0.5\%$) of the warm seawater violently flashes into low-pressure steam, leaving behind concentrated brine.
  3. The steam expands through an ultra-low-pressure steam turbine designed with very large rotor diameters to produce electrical power.
  4. The low-pressure steam exhaust enters a surface condenser cooled by deep seawater.
  5. Byproduct Desalination: Because the evaporated steam leaves all dissolved salts behind in the flash chamber, condensing the steam produces high-purity Fresh Potable Desalinated Water as a valuable co-product (approximately $2 \text{ million liters}$ per day for a $1\text{ MW}$ plant).

Engineering Challenges:
1. Massive deep-sea Cold Water Pipes ($3 \text{ to } 5\text{ meters}$ in diameter, $1000\text{ m}$ long) subjected to intense ocean currents and hydrostatic pressure.
2. Marine biofouling of evaporator heat exchangers by micro-algae and barnacles.
3. High parasitic pumping power consumption (up to $25-30\%$ of gross generated electricity).
"""
            },
            {
                "qid": "res-q20",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Tidal and Wave Energy Systems: Tidal Barrage Energy Equation and Oscillating Water Column (OWC)",
                "yt_query": "tidal barrage energy derivation oscillating water column wells turbine wave energy",
                "img_path": "images/res/tidal_barrage_owc.png",
                "img_caption": "Figure 4.5: (a) Tidal Barrage Basin Operation and (b) Oscillating Water Column Wave Energy Converter",
                "answer": r"""
Ocean kinetic and potential energy represents a dense, highly predictable renewable resource, harnessed primarily through Tidal Energy and Wave Energy conversion systems.

1. Tidal Barrage Energy Equation Derivation:
Tidal power exploits the periodic gravitational rise and fall of coastal sea levels caused by the planetary gravitational interactions between the earth, moon, and sun. A tidal barrage consists of a dam structure with sluice gates and low-head bulb turbines built across a natural estuary or coastal bay.
In a Single-Basin One-Way (Ebb Generation) scheme:
- At high tide, sluice gates open to fill the enclosed tidal basin.
- At slack high tide, sluice gates close, trapping water inside the basin.
- During ebb tide, the sea level drops outside, establishing a hydraulic head $R$ (the tidal range). The trapped water is released through low-head Kaplan/bulb hydro-turbines to generate electricity.

Mathematical Derivation of Potential Energy:
Consider a tidal basin with surface area $A$. Let $z$ be the instantaneous water level in the basin above the low-tide sea datum, varying from $z = 0$ to $z = R$, where $R$ is the tidal range.
For a thin horizontal water layer of thickness $dz$ at elevation $z$, the volume is $dV = A \cdot dz$, and the mass of seawater in this slice is:
$$dm = \rho \cdot dV = \rho A \cdot dz$$
where $\rho$ is the density of seawater ($\approx 1025 \text{ kg/m}^3$).
The potential energy $dE$ of this mass element with respect to the low-tide datum ($z = 0$) is:
$$dE = dm \cdot g \cdot z = (\rho A dz) g z = \rho g A z dz$$
Integrating over the entire tidal range from $z = 0$ to $z = R$:
$$E = \int_0^R \rho g A z \, dz = \rho g A \left[ \frac{z^2}{2} \right]_0^R = \frac{1}{2} \rho g A R^2$$
Thus, the total theoretical potential energy stored in the basin per tidal filling and emptying cycle is:
$$\mathbf{E = \frac{1}{2} \rho g A R^2} \quad \text{Joules}$$
Since there are approximately two high tides and two low tides per solar day (a semidiurnal tidal period of $T_{tide} \approx 12.42 \text{ hours} = 44712 \text{ seconds}$), the theoretical average power generated over one full tidal cycle is:
$$P_{avg} = \frac{E}{T_{tide}} = \frac{\rho g A R^2}{2 T_{tide}}$$
This fundamental derivation reveals that tidal energy is proportional to the basin surface area $A$ and scales quadratically with the tidal range ($R^2$). Economically viable sites require a mean tidal range $R > 5\text{ meters}$.

2. Wave Energy Conversion: Oscillating Water Column (OWC):
Ocean waves are generated by wind shear blowing over extensive ocean fetches. The Oscillating Water Column (OWC) is one of the most robust shoreline and nearshore wave energy converters (e.g., the Vizhinjam OWC plant in Kerala, India).
Construction and Working Principle:
- Structure: An OWC comprises a hollow, reinforced concrete or steel caisson chamber partially submerged in the ocean with an open submerged lower aperture facing oncoming waves. The upper chamber forms an airtight plenum chamber above the internal water level, terminating in an air duct.
- Bi-Directional Air Flow:
  1. Upward Wave Motion: As an incoming ocean wave crest enters the chamber, the internal water column rises like a piston, compressing the trapped air and forcing high-velocity air outward through the top exhaust duct.
  2. Downward Wave Motion: As the wave trough arrives, the internal water level recedes downward, creating a partial vacuum that sucks atmospheric air backward into the chamber through the duct.

The Wells Turbine:
A conventional aerodynamic turbine would reverse its direction of rotation every half wave cycle as air changes flow direction. To solve this, the OWC employs a Wells Turbine—a specialized self-rectifying axial-flow air turbine invented by Prof. Alan Wells.
- Aerodynamic Principle: The rotor blades of a Wells turbine are made of symmetrical NACA airfoils oriented perpendicular to the axis of rotation ($90^\circ$ stagger angle).
- Unidirectional Rotation: Regardless of whether air flows upward (compression) or downward (suction), the relative airflow vector across the symmetrical airfoil generates an aerodynamic lift vector that consistently produces a net forward tangential driving force along the direction of rotation. Thus, the Wells turbine rotates continuously in a single direction without requiring mechanical reversing valves, driving a conventional induction or synchronous generator.
"""
            }
        ]
    },
    {
        "module_id": "res-m5",
        "module_num": "Module 5",
        "module_title": "Energy Storage, Fuel Cells & Microgrids",
        "questions": [
            {
                "qid": "res-q21",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Fuel Cells: Hydrogen-Oxygen Cell Principle, Gibbs Free Energy, Efficiency, and Polarization Overpotentials",
                "yt_query": "fuel cell working principle gibbs free energy polarization curve activation ohmic concentration",
                "img_path": "images/res/fuel_cell_polarization_curve.png",
                "img_caption": "Figure 5.1: Fuel Cell V-I Polarization Curve Illustrating Three Dominant Loss Regimes",
                "answer": r"""
A fuel cell is an electrochemical energy conversion device that converts the chemical energy of a continuously supplied fuel (hydrogen) and an oxidant (oxygen/air) directly into electrical energy and water without undergoing intermediate thermal combustion. Because it bypasses the Carnot thermodynamic limitation of heat engines, it achieves high conversion efficiency.

1. Electrochemical Operation of Hydrogen-Oxygen Fuel Cell:
The basic cell comprises an anode, a cathode, and an ion-conducting electrolyte.
- Anode Reaction (Hydrogen Oxidation Reaction - HOR): Pure hydrogen fuel is supplied to the porous anode coated with platinum catalyst, where each $H_2$ molecule is split into protons and electrons:
$$2 H_2 \to 4 H^+ + 4 e^- \quad (E^\circ = 0.00\text{ V})$$
- Electrolyte: Protons ($H^+$) migrate through the proton exchange membrane to the cathode, while electrons are blocked by the electrically insulating membrane and forced to travel through the external electrical load, producing usable DC power.
- Cathode Reaction (Oxygen Reduction Reaction - ORR): At the cathode, oxygen reacts with incoming electrons and protons to form water and heat:
$$O_2 + 4 H^+ + 4 e^- \to 2 H_2 O \quad (E^\circ = +1.229\text{ V})$$
- Overall Cell Reaction:
$$2 H_2 + O_2 \to 2 H_2 O + \text{Electrical Energy} + \text{Heat} \quad (\Delta H^\circ = -285.8\text{ kJ/mol})$$

2. Theoretical Reversible EMF and Thermodynamic Efficiency:
The maximum electrical work $W_{elec}$ that can be extracted from an isothermal, isobaric chemical reaction is given by the change in Gibbs Free Energy ($\Delta G$):
$$W_{elec} = -\Delta G$$
The relationship between Gibbs free energy and cell reversible electromotive force $E_0$ is:
$$\Delta G = -n F E_0 \implies E_0 = -\frac{\Delta G}{n F}$$
where $n$ is the number of electrons transferred per mole of fuel ($n = 2$ for $H_2$), and $F$ is Faraday's constant ($F = 96485\text{ C/mol}$).
For the liquid water formation reaction at standard conditions ($25^\circ\text{C}, 1\text{ atm}$):
$$\Delta G^\circ = -237.2\text{ kJ/mol} = -237200\text{ J/mol}$$
$$E_0 = \frac{237200}{2 \times 96485} \approx 1.229\text{ V}$$
The theoretical thermodynamic efficiency $\eta_{th}$ of a fuel cell is defined as the ratio of maximum extractable electrical energy ($\Delta G$) to total heat of combustion (enthalpy change $\Delta H$, using the Higher Heating Value HHV of $-285.8\text{ kJ/mol}$):
$$\eta_{th} = \frac{\Delta G}{\Delta H} = \frac{-237.2\text{ kJ/mol}}{-285.8\text{ kJ/mol}} \approx 0.830 \implies \mathbf{83.0\%}$$

3. V-I Polarization Curve and Overpotentials:
Under actual current load $I$, terminal voltage $V_{cell}$ drops significantly below the reversible equilibrium potential $E_0$ due to three irreversible loss mechanisms:
$$V_{cell} = E_0 - \Delta V_{act} - \Delta V_{ohm} - \Delta V_{conc}$$
- Activation Overpotential ($\Delta V_{act}$): Caused by the slow kinetics of electrochemical charge-transfer reactions on the catalyst surfaces, especially the sluggish oxygen reduction at the cathode. Dominates at low current densities. Governed by the Butler-Volmer and Tafel equations:
$$\Delta V_{act} = \frac{R T}{\alpha n F} \ln\left( \frac{i}{i_0} \right)$$
where $i_0$ is the exchange current density.
- Ohmic Overpotential ($\Delta V_{ohm}$): Caused by internal ionic resistance of the polymer electrolyte membrane and electronic resistance of the carbon bipolar plates and gas diffusion layers. Follows Ohm's law, dominating in the intermediate linear region of the polarization curve:
$$\Delta V_{ohm} = i \cdot R_{internal}$$
- Concentration (Mass Transport) Overpotential ($\Delta V_{conc}$): At high current densities, reactant hydrogen and oxygen gases cannot diffuse through the porous diffusion layer fast enough to replenish consumed molecules, or liquid water floods the cathode pores. Governed by:
$$\Delta V_{conc} = -\frac{R T}{n F} \ln\left( 1 - \frac{i}{i_L} \right)$$
where $i_L$ is the limiting current density. When current approaches $i_L$, terminal voltage plunges sharply to zero.
"""
            },
            {
                "qid": "res-q22",
                "marks": 7,
                "type": "Descriptive",
                "title": "Fuel Cell Technologies: Proton Exchange Membrane Fuel Cell (PEMFC) vs Solid Oxide Fuel Cell (SOFC)",
                "yt_query": "PEMFC vs SOFC fuel cell comparison membrane electrolyte temperature",
                "img_path": "images/res/pemfc_vs_sofc.png",
                "img_caption": "Figure 5.2: Operating Architectures of (a) Low-Temperature PEMFC and (b) High-Temperature SOFC",
                "answer": r"""
Fuel cells are classified according to the chemical nature of their electrolyte, which dictates their operating temperature, catalyst materials, fuel flexibility, and practical applications. The two leading technologies are the Proton Exchange Membrane Fuel Cell (PEMFC) and the Solid Oxide Fuel Cell (SOFC).

1. Proton Exchange Membrane Fuel Cell (PEMFC):
- Electrolyte: A solid, flexible fluoropolymer membrane with sulfonic acid functional groups, universally made of Nafion (perfluorosulfonic acid, PFSA). The membrane conducts positively charged hydrogen ions (protons, $H^+$) through water-hydrated channels.
- Operating Temperature: Low-temperature operation, typically $60^\circ\text{C} \text{ to } 80^\circ\text{C}$ (HT-PEMFC operates at $120^\circ\text{C} \text{ to } 160^\circ\text{C}$ using polybenzimidazole doped with phosphoric acid).
- Catalyst: Nanoparticle Platinum ($Pt$) or Platinum-Ruthenium ($Pt-Ru$) supported on high-surface-area carbon black.
- Fuel Requirements: Requires ultra-pure hydrogen fuel ($> 99.99\%$). Carbon monoxide ($CO$) is a severe catalyst poison at temperatures below $100^\circ\text{C}$; even $10\text{ ppm}$ of $CO$ poisons the active platinum sites, requiring expensive external fuel reforming and cleanup.
- Operational Characteristics: Rapid startup time (seconds to minutes) and high power density ($1 \text{ to } 2\text{ W/cm}^2$), making it the preeminent choice for Fuel Cell Electric Vehicles (FCEVs, e.g., Toyota Mirai, Hyundai Nexo), portable consumer power, and unmanned aerial vehicles.
- Water Management: Crucial challenge: if the membrane dries out, ionic conductivity drops and the membrane can tear; if too much water accumulates, cathode pores flood, suffocating oxygen transport.

2. Solid Oxide Fuel Cell (SOFC):
- Electrolyte: A dense, non-porous ceramic metal-oxide solid, standardly Yttria-Stabilized Zirconia (YSZ, $8\text{ mol}\% \text{ Y}_2 O_3 \text{ in } ZrO_2$). At high temperatures, oxygen ion vacancies allow oxygen ions ($O^{2-}$) to migrate through the crystal lattice from cathode to anode.
- Operating Temperature: High-temperature operation, typically $700^\circ\text{C} \text{ to } 1000^\circ\text{C}$.
- Catalyst: Inexpensive, non-precious materials. Anode is a Nickel-YSZ cermet (ceramic-metallic composite); cathode is Lanthanum Strontium Manganite (LSM).
- Fuel Flexibility: Due to extreme internal temperatures, SOFCs do not require pure hydrogen. They can internally reform common hydrocarbons (natural gas, methane, biogas, propane, ethanol) into syngas directly on the nickel anode without external reformers ($CH_4 + H_2 O \to CO + 3 H_2$). Furthermore, Carbon Monoxide ($CO$) is consumed as a primary fuel ($CO + O^{2-} \to CO_2 + 2 e^-$) rather than acting as a poison.
- Operational Characteristics: Long startup times (hours) and high thermal cycling stresses due to ceramic brittleness. However, the high-temperature exhaust heat ($> 600^\circ\text{C}$) can drive combined-cycle gas and steam turbines (SOFC-GT hybrid cycles) or provide industrial district heating, achieving combined electrical/thermal efficiencies exceeding $75\% \text{ to } 85\%$.
- Applications: Stationary utility-scale power generation, data center baseload power, and decentralized industrial microgrids.

Comparative Summary:
| Parameter | Proton Exchange Membrane (PEMFC) | Solid Oxide Fuel Cell (SOFC) |
|---|---|---|
| Electrolyte | Solid polymer (Nafion membrane) | Ceramic metal oxide (YSZ) |
| Mobile Carrier Ion | Protons ($H^+$ migrating to cathode) | Oxygen ions ($O^{2-}$ migrating to anode) |
| Operating Temp. | $60^\circ\text{C} - 80^\circ\text{C}$ (Low) | $700^\circ\text{C} - 1000^\circ\text{C}$ (High) |
| Catalyst | Precious Platinum ($Pt$) nanoparticles | Non-precious Ni-YSZ and LSM ceramics |
| Fuel Purity | Ultra-pure $H_2$ ($CO$ poisons platinum) | High flexibility ($H_2$, $CH_4$, natural gas, syngas) |
| Startup Time | Instantaneous (seconds to minutes) | Very slow (hours to reach thermal equilibrium) |
| Primary Application | Transportation (FCEVs), portable power | Stationary baseload plants, CHP systems |
"""
            },
            {
                "qid": "res-q23",
                "marks": 7,
                "type": "Descriptive",
                "title": "Battery Energy Storage Systems (BESS): Lead-Acid, Lithium-Ion, Redox Flow, Metrics (SoC, DoD, C-Rate), and Degradation",
                "yt_query": "battery energy storage systems BESS lead acid lithium ion flow battery SoC DoD C-rate",
                "img_path": "images/res/bess_technologies_metrics.png",
                "img_caption": "Figure 5.3: Schematic Operating Principles of Lithium-Ion and Vanadium Redox Flow Batteries",
                "answer": r"""
Electrochemical Battery Energy Storage Systems (BESS) are critical to modern power grids, providing load leveling, peak shaving, frequency regulation, and mitigating the intermittent generation of solar PV and wind farms.

1. BESS Technologies Comparison:
- Lead-Acid Batteries:
  - Chemistry: Lead dioxide ($PbO_2$) cathode, sponge lead ($Pb$) anode, sulfuric acid ($H_2 SO_4$) electrolyte.
  - Characteristics: Low energy density ($30 \text{ to } 40\text{ Wh/kg}$); short cycle life ($500 \text{ to } 1200\text{ cycles}$ at $50\%\text{ DoD}$); low round-trip efficiency ($70\% \text{ to } 80\%$).
  - Advantages/Applications: Very low initial capital cost, excellent surge current capability, fully established recycling supply chains. Used in automotive SLI and low-cost rural off-grid solar.
- Lithium-Ion Batteries:
  - Chemistry: Lithium intercalates into metal-oxide cathodes (Lithium Iron Phosphate - $LiFePO_4$ / LFP, or Nickel Manganese Cobalt - NMC) and graphitic carbon anodes, with organic liquid carbonate electrolytes containing $LiPF_6$ salts.
  - Characteristics: High energy density ($150 \text{ to } 250\text{ Wh/kg}$); long cycle life ($3000 \text{ to } 8000+\text{ cycles}$ for LFP); high round-trip efficiency ($90\% \text{ to } 95\%$).
  - Advantages/Applications: Compact footprint, rapid dynamic response ($< 20\text{ ms}$ for primary frequency support), dominant in commercial/utility grid-scale BESS and electric vehicles. Requires sophisticated Battery Management Systems (BMS) to prevent thermal runaway.
- Vanadium Redox Flow Batteries (VRFB):
  - Chemistry: Employs liquid electrolytes containing vanadium in four distinct oxidation states ($V^{2+} / V^{3+}$ in negative tank, $V^{4+} / V^{5+}$ in positive tank) dissolved in sulfuric acid, pumped through a central proton-exchange cell stack.
  - Unique Advantage: Independent scaling of Power and Energy. Power capacity (kW) is determined strictly by the membrane cell stack surface area, whereas Energy capacity (kWh) is determined solely by the volume of electrolyte in the external storage tanks.
  - Characteristics: Long calendar life ($> 20\text{ years}$, $15000+\text{ cycles}$ without degradation); immune to thermal runaway; lower round-trip efficiency ($70\% \text{ to } 75\%$). Ideal for multi-hour (4 to 12 hour) long-duration grid energy storage.

2. Fundamental BESS Metrics:
- State of Charge ($SoC(t)$): The instantaneous available capacity in the battery expressed as a percentage of nominal rated capacity $Q_n$:
$$SoC(t) = SoC(t_0) - \frac{1}{Q_n} \int_{t_0}^t \eta_c I(t) \, dt$$
where $I(t)$ is the current (positive for discharge, negative for charge), and $\eta_c$ is Coulombic efficiency (Coulomb Counting method).
- Depth of Discharge ($DoD$): The percentage of capacity discharged relative to nominal capacity:
$$DoD = 100\% - SoC$$
- C-Rate: A normalized measure of the charging or discharging speed relative to total battery capacity. A discharge rate of $1\text{C}$ discharges the entire rated capacity in exactly 1 hour. For a $100\text{ Ah}$ battery:
  - $1\text{C} = 100\text{ A}$ (discharges in 1 hour)
  - $0.5\text{C} = 50\text{ A}$ (discharges in 2 hours)
  - $2\text{C} = 200\text{ A}$ (discharges in 30 minutes)
- Round-Trip Efficiency ($\eta_{rt}$): The ratio of total AC electrical energy recovered during discharging to the AC electrical energy supplied during charging:
$$\eta_{rt} = \frac{E_{discharge}}{E_{charge}} \times 100\%$$

3. Battery Degradation Mechanisms:
Electrochemical cells degrade through both Calendar Aging (time and temperature degradation while idling) and Cycle Aging (stress from charge-discharge throughput):
- Solid Electrolyte Interphase (SEI) Growth: In lithium-ion cells, continuous parasitic reaction between the liquid electrolyte and negative graphite anode consumes active lithium ions, permanently increasing internal resistance.
- Lithium Plating: Charging at high C-rates or low temperatures ($< 0^\circ\text{C}$) causes metallic lithium to plate onto the anode surface rather than intercalating, forming hazardous dendrites that can pierce the separator and cause catastrophic internal short-circuits.
- Depth-of-Discharge Stress: Deep cycling ($100\%\text{ DoD}$) induces mechanical lattice strain, particle cracking, and electrode delamination. Restricting operation to $10\% - 90\%\text{ SoC}$ substantially extends battery operating life.
"""
            },
            {
                "qid": "res-q24",
                "marks": 7,
                "type": "Descriptive",
                "title": "Hybrid Renewable Energy Systems (HRES): Solar-Wind-Battery-Diesel, DC vs AC Bus Coupling, and Energy Dispatch",
                "yt_query": "hybrid renewable energy system solar wind diesel battery DC coupled AC coupled dispatch",
                "img_path": "images/res/hres_dc_ac_architectures.png",
                "img_caption": "Figure 5.4: Architectural Topologies of (a) DC-Coupled and (b) AC-Coupled Hybrid Renewable Microgrids",
                "answer": r"""
A Hybrid Renewable Energy System (HRES) integrates two or more renewable energy sources (typically solar photovoltaic arrays and wind turbines) with energy storage banks (batteries) and conventional dispatchable backup generators (diesel generator sets). Because solar and wind resources possess strong natural negative seasonal and diurnal cross-correlations (wind is often strongest at night or during stormy weather when solar irradiance is zero), combining them dramatically dampens power volatility, enhances supply reliability, and reduces the required battery capacity.

1. System Architectural Topologies:
- DC-Coupled HRES Architecture:
  - Operation: The solar PV array (via DC-DC MPPT converter), the wind turbine (via AC-DC rectifier and MPPT chopper), and the electrochemical battery storage bank (via bidirectional DC-DC charge controller) all connect to a common central DC distribution bus.
  - Delivery: A single central bidirectional inverter interfaces the DC bus to local AC loads or the utility grid.
  - Advantages: Excellent efficiency for battery charging because DC power from solar and wind charges the battery without passing through multiple AC-DC-AC conversion stages; simpler synchronization since only the central inverter needs to synchronize with the AC load.
  - Disadvantages: Less modular; failure of the central inverter halts AC power delivery entirely; requires high DC cabling ratings.
- AC-Coupled HRES Architecture:
  - Operation: The solar PV array, wind turbine, and diesel generator each connect independently to a common AC distribution bus through dedicated grid-forming or grid-tied AC inverters. The battery storage bank interfaces with the AC bus via its own bidirectional battery inverter/charger.
  - Advantages: Highly modular and scalable; standard commercial off-the-shelf grid-tied inverters can be added at any location along the AC line; power generated by solar or wind can feed AC loads directly without conversion through a central battery inverter.
  - Disadvantages: Higher conversion losses when renewable power charges the battery (DC to AC, then back from AC to DC through the charger); complex decentralized phase synchronization and frequency stability management across multiple parallel inverters.

2. Energy Management System (EMS) Operational Dispatch Strategy:
The centralized EMS microgrid controller executes real-time optimal power dispatch governed by strict hierarchical priorities:
- Priority 1 (Direct Renewable Consumption): Real-time electricity demand ($P_{load}$) is supplied preferentially by immediate solar and wind generation ($P_{ren} = P_{pv} + P_{wind}$).
- Priority 2 (Battery Storage Management):
  - Surplus Condition ($P_{ren} > P_{load}$): Excess power charges the battery bank up to its maximum limit ($SoC \le SoC_{max}$). Any remaining excess beyond battery capacity is diverted to a dump load (water heating) or curtailed by pitching wind blades / shifting PV off the MPP.
  - Deficit Condition ($P_{ren} < P_{load}$): The power shortfall ($\Delta P = P_{load} - P_{ren}$) is supplied by discharging the battery bank, provided the state of charge remains above its safe cut-off limit ($SoC \ge SoC_{min}$).
- Priority 3 (Diesel Generator Dispatch):
  - When renewable generation is insufficient and the battery reaches its lower threshold ($SoC_{min}$), the EMS sends a remote auto-start command to the backup diesel generator.
  - The diesel generator is commanded to operate at an efficient loading point ($75\% \text{ to } 85\%$ of rated capacity) to prevent low-load engine carbon fouling, simultaneously supplying net deficit load and recharging the battery bank up to a preset recovery threshold ($SoC_{rec} \approx 60\%$), at which point the diesel generator is shut down.
"""
            },
            {
                "qid": "res-q25",
                "marks": 7,
                "type": "Descriptive",
                "title": "Microgrids: AC vs DC Microgrids, Grid-Connected vs Islanded Modes, and Decentralized Droop Control",
                "yt_query": "microgrid AC DC grid connected islanded droop control P-f Q-V",
                "img_path": "images/res/microgrid_droop_control.png",
                "img_caption": "Figure 5.5: Microgrid Droop Control Characteristics: (a) P-f Active Droop and (b) Q-V Reactive Droop",
                "answer": r"""
A microgrid is a localized, discrete electrical network comprising distributed energy resources (DERs - solar PV, wind turbines, microturbines), energy storage systems (BESS), and controllable electrical loads. It acts as a single controllable electrical entity relative to the main grid and can connect and disconnect seamlessly between Grid-Connected and Islanded (Autonomous) operational modes.

1. Operational Modes and Transition:
- Grid-Connected Mode: The microgrid is tied to the utility distribution grid at the Point of Common Coupling (PCC) through a static transfer switch (STS). The utility grid acts as a stiff voltage source establishing system frequency ($50\text{ Hz}$) and voltage. Microgrid inverters operate in Grid-Following (P-Q) mode, injecting commanded active ($P$) and reactive ($Q$) power dictated by local generation economics.
- Islanded (Autonomous) Mode: When a utility grid fault, blackout, or scheduled maintenance occurs, the static switch at the PCC opens rapidly ($< 10-20\text{ ms}$) to isolate the microgrid. Within the islanded island, the distributed inverters must instantly transition to Grid-Forming mode to establish and maintain voltage and frequency without the utility grid.
- Seamless Re-synchronization: When utility grid voltage returns, a synchrocheck relay verifies that voltage amplitude, frequency, and phase angle differences across the static switch are within strict limits ($\Delta V < 3\%, \Delta f < 0.1\text{ Hz}, \Delta\theta < 5^\circ$) before commanding the static switch to close, avoiding severe transient inrush currents.

2. AC vs DC Microgrid Architecture:
- AC Microgrid: DERs and batteries connect to a common AC bus. Dominant in retrofitting existing AC infrastructure and powering standard AC industrial induction motors and appliances. Disadvantages include transformer core losses, reactive power circulation, and synchronization complexities.
- DC Microgrid: DERs, EV charging stations, modern variable-frequency drive motors, data centers, and batteries connect directly to a high-voltage DC distribution bus ($380\text{ V} \text{ or } 750\text{ V DC}$). Completely eliminates AC-DC conversion stages ($10-15\%$ higher efficiency), eliminates reactive power losses ($Q = 0$), and eliminates phase angle and frequency synchronization requirements. Disadvantages include immature DC protection switchgear and DC arc extinction challenges.

3. Decentralized Droop Control:
In an islanded microgrid containing multiple parallel grid-forming inverters, power sharing cannot rely on high-speed physical communication cables across large geographical distances due to latency, noise, and single-point communication failure vulnerabilities. Instead, Decentralized Droop Control mimics the self-regulating governor and exciter action of traditional synchronous generators.
In inductive power transmission lines ($X \gg R$), active power $P$ is predominantly coupled to voltage phase angle (and thus frequency $f$), while reactive power $Q$ is predominantly coupled to voltage magnitude $V$:
$$P \approx \frac{V_1 V_2}{X} \sin\delta, \quad Q \approx \frac{V_1 (V_1 - V_2 \cos\delta)}{X}$$
Based on this decoupling, droop equations are implemented inside each inverter's digital controller:
1. Active Power - Frequency ($P-f$) Droop:
$$f = f_0 - m_p (P - P_0)$$
where $f_0$ is the nominal reference frequency ($50\text{ Hz}$), $P_0$ is the nominal active power, $P$ is the measured output active power, and $m_p$ is the active droop slope coefficient:
$$m_p = \frac{\Delta f_{\max}}{P_{\max}}$$
If an electrical load increases, system frequency naturally drops slightly. Each parallel inverter automatically senses this frequency deviation and proportionally ramps up its active power output in inverse proportion to its droop slope ($m_p$), achieving autonomous active power sharing without any digital communications.
2. Reactive Power - Voltage ($Q-V$) Droop:
$$V = V_0 - n_q (Q - Q_0)$$
where $V_0$ is nominal voltage, $Q_0$ is nominal reactive power, $Q$ is measured reactive power, and $n_q$ is the reactive droop slope coefficient:
$$n_q = \frac{\Delta V_{\max}}{Q_{\max}}$$
If reactive load increases, terminal voltage dips slightly, and each inverter automatically increases its reactive power output ($Q$) to stabilize the voltage profile.
"""
            },
            {
                "qid": "res-q26",
                "marks": 7,
                "type": "Descriptive",
                "title": "Grid Integration Challenges of Renewables: Duck Curve, System Inertia, Harmonics, and Low-Voltage Fault Ride-Through (LVRT)",
                "yt_query": "grid integration challenges duck curve system inertia harmonics LVRT fault ride through",
                "img_path": "images/res/grid_integration_duck_curve.png",
                "img_caption": "Figure 5.6: The California ISO 'Duck Curve' and Grid Code Low-Voltage Ride-Through (LVRT) Profile",
                "answer": r"""
Large-scale integration of inverter-interfaced renewable energy sources (solar PV and wind) into traditional AC transmission networks presents complex technical and stability challenges due to their non-synchronous, intermittent, and weather-dependent nature.

1. The California ISO "Duck Curve" and Ramp-Rate Stress:
As rooftop and utility-scale solar PV penetration reaches high levels, net load (defined as Total Electrical Demand minus Variable Renewable Generation: $P_{net} = P_{load} - P_{solar}$) drops precipitously during midday hours when solar generation peaks. This creates a deep belly in the net load profile.
As the sun sets in the late afternoon, solar output drops to zero at the exact time evening residential peak electricity demand surges. This requires conventional thermal generation (gas peakers and hydro) to execute an extremely steep upward ramp ($> 13000\text{ MW}$ in 2 to 3 hours). During midday periods, excessive solar generation can push net load below the minimum operating turndown limits of baseload nuclear and coal power stations, forcing curtailment of clean solar energy or negative wholesale electricity prices.

2. Reduction of System Rotational Inertia and Frequency Instability:
Conventional thermal, hydro, and nuclear power stations employ massive synchronous generators whose physical rotating rotors ($J$) store enormous kinetic energy ($E_k = \frac{1}{2} J \omega^2$). When a sudden load step or generator trip occurs, this stored physical inertia naturally and instantaneously decelerates, providing intrinsic inertial response that dampens the initial Rate of Change of Frequency ($RoCoF$):
$$\frac{df}{dt} = \frac{f_0 (P_m - P_e)}{2 H S_n}$$
where $H$ is the inertia constant in seconds.
In contrast, solar PV has zero moving parts, and wind turbines couple through power electronic converters that physically decouple the rotating blade inertia from grid frequency. High renewable penetration displaces synchronous generators, causing low system inertia. A sudden loss of generation leads to extremely rapid $RoCoF$ spikes and deep frequency nadirs that can trip under-frequency load shedding (UFLS) relays and trigger cascading blackouts.
Solution: Modern grid codes mandate synthetic (virtual) inertia and fast frequency response (FFR) programmed into grid-forming battery inverters and wind turbine pitch controllers.

3. Power Quality, Harmonics, and Voltage Flicker:
Inverter-based resources use high-frequency Pulse Width Modulation (PWM) switching ($2 \text{ kHz to } 16\text{ kHz}$) using IGBTs. This introduces high-frequency switching harmonics and inter-harmonics into the AC grid. If not properly attenuated by tuned inductive-capacitive-inductive (LCL) grid filters, these harmonics distort grid voltage, overheat distribution transformers, and excite resonant interactions with underground cabling. Furthermore, rapid cloud transits over massive solar farms cause sharp irradiance fluctuations ($> 70\%$ drop in seconds), causing severe voltage flicker on distribution feeders.

4. Low-Voltage Fault Ride-Through (LVRT / FRT) Requirements:
In early renewable integration stages, grid codes instructed solar and wind inverters to disconnect immediately whenever grid voltage dipped below $0.85\text{ pu}$ to protect inverter power electronics. However, during high penetration, a single transmission line fault causing a momentary voltage dip would cause gigawatts of renewable generation across an entire state to disconnect simultaneously, turning a localized minor fault into a catastrophic national grid collapse.
Modern Grid Codes (such as IEEE 1547-2018 and CEA standards) strictly mandate Low-Voltage Ride-Through (LVRT):
- Ride-Through Boundary: The inverter must remain physically connected to the grid during severe faults even if terminal voltage plunges to $0.05 \text{ to } 0.15\text{ pu}$ (or even zero volts) for a duration of $150 \text{ to } 625\text{ milliseconds}$.
- Dynamic Grid Support (Reactive Current Injection): During the voltage depression, the inverter must immediately halt active power curtailment and inject maximum inductive reactive current ($I_q \ge 2\% \text{ per } 1\% \text{ voltage drop}$) to support grid voltage recovery and aid protective distance relays in clearing the fault safely.
"""
            }
        ]
    }
]

RES_BYHEART = {
    'res-q1': {
        "eq": r'$$I_{sc} = 1367 \text{ W/m}^2, \quad AM = \frac{1}{\cos\theta_z} = \sec\theta_z, \quad I_{on} = I_{sc}\left[1 + 0.033\cos\left(\frac{360n}{365}\right)\right]$$',
        "text": r'<strong>Solar Constant:</strong> $I_{sc} = 1367\text{ W/m}^2$ is the extraterrestrial solar irradiance normal to the beam at mean earth-sun distance.<br><strong>Air Mass:</strong> $AM = 1/\cos\theta_z$ defines optical atmospheric path length ($AM0$ in space, $AM1.5$ with $1000\text{ W/m}^2$ for terrestrial testing).'
    },
    'res-q2': {
        "eq": r'$$\delta = 23.45^\circ \sin\left[\frac{360}{365}(284 + n)\right], \quad \sin\alpha = \cos\theta_z = \sin\phi\sin\delta + \cos\phi\cos\delta\cos\omega$$',
        "text": r'<strong>Declination ($\delta$):</strong> Angle between sun-earth line and equatorial plane ($-23.45^\circ \le \delta \le +23.45^\circ$).<br><strong>Hour Angle ($\omega$):</strong> Earth rotation displacement ($15^\circ/\text{hr}$, $\omega=0^\circ$ at solar noon).<br><strong>Zenith ($\theta_z$) & Altitude ($\alpha$):</strong> $\alpha + \theta_z = 90^\circ$.'
    },
    'res-q3': {
        "eq": r'$$V_{out} = C_{cal} \cdot I_g, \quad I_{bN} = \frac{V_{pyr}}{C_{pyr}}$$',
        "text": r'<strong>Pyranometer:</strong> Measures total hemispherical global radiation ($I_g = I_b\cos\theta_z + I_d$) across $0.3-3.0\,\mu\text{m}$ using a black thermopile with dual glass domes.<br><strong>Pyrheliometer:</strong> Measures beam direct normal irradiance (DNI) using a narrow collimating tube ($5.7^\circ$ field of view) mounted on a 2-axis solar tracker.'
    },
    'res-q4': {
        "eq": r'$$I = I_{ph} - I_0 \left[ \exp\left( \frac{q (V + I R_s)}{n k T} \right) - 1 \right] - \frac{V + I R_s}{R_{sh}}$$',
        "text": r'Single-diode PV equivalent circuit couples light-generated current $I_{ph}$, dark diode recombination current $I_D$, series contact resistance $R_s$, and parallel shunt leakage resistance $R_{sh}$. Open-circuit voltage scales logarithmically: $V_{oc} \approx V_t \cdot n \ln(I_{sc}/I_0)$.'
    },
    'res-q5': {
        "eq": r'$$FF = \frac{P_{mp}}{V_{oc} I_{sc}} = \frac{V_{mp} I_{mp}}{V_{oc} I_{sc}}, \quad \eta = \frac{P_{mp}}{G \cdot A} \times 100\% = \frac{V_{oc} I_{sc} FF}{G \cdot A} \times 100\%$$',
        "text": r'<strong>Fill Factor ($FF$):</strong> Measures the squareness of the I-V curve (typically $0.75 - 0.85$).<br><strong>Conversion Efficiency ($\eta$):</strong> Ratio of maximum electrical power $P_{mp}$ to total incident solar optical power $P_{in} = G \cdot A$.'
    },
    'res-q6': {
        "eq": r'$$q_u = F_R A_c [I_t (\tau\alpha) - U_L (T_i - T_a)], \quad \eta = F_R (\tau\alpha) - F_R U_L \left(\frac{T_i - T_a}{I_t}\right)$$',
        "text": r'<strong>Hottel-Whillier-Bliss Equation:</strong> Quantifies useful thermal gain $q_u$ of a flat-plate collector using heat removal factor $F_R$, optical transmittance-absorptance product $(\tau\alpha)$, and overall heat loss coefficient $U_L$.'
    },
    'res-q7': {
        "eq": r'$$C_R = \frac{A_a}{A_r}, \quad PTC: C_R \approx 15-80, \quad CR (\text{Tower}): C_R \approx 500-1500$$',
        "text": r'Concentrating Solar Power (CSP) reduces heat loss area $A_r$ relative to aperture $A_a$ to achieve high operating temperatures.<br><strong>Line Focus:</strong> Parabolic Trough ($400^\circ\text{C}$) & Linear Fresnel ($350^\circ\text{C}$).<br><strong>Point Focus:</strong> Solar Power Tower ($550-800^\circ\text{C}$) with molten salt storage.'
    },
    'res-q8': {
        "eq": r'$$P_{dissipated} = |V_{reverse}| \times I_{string}, \quad V_{bypass} \approx -0.7\text{ V}$$',
        "text": r'<strong>Hot-Spot Phenomenon:</strong> Shaded cell in series carries illuminated string current, forced into reverse bias and dissipating power as concentrated heat.<br><strong>Bypass Diodes:</strong> Placed anti-parallel across cell groups to conduct string current when reverse-biased, protecting cells from burn-out.'
    },
    'res-q9': {
        "eq": r'$$\frac{dP}{dV} = 0 \implies \frac{dI}{dV} = -\frac{I}{V} \quad (\text{at MPP}), \quad \frac{dI}{dV} > -\frac{I}{V} \ (\text{Left}), \quad \frac{dI}{dV} < -\frac{I}{V} \ (\text{Right})$$',
        "text": r'<strong>P&O MPPT:</strong> Perturbs voltage and observes power change; hunts in 3-point cycle.<br><strong>Incremental Conductance:</strong> Tracks derivative $\frac{dI}{dV} + \frac{I}{V} = 0$, halting perturbations at exact peak and eliminating steady-state oscillation.'
    },
    'res-q10': {
        "eq": r'$$P_{import} = P_{load} - P_{pv}, \quad t_{islanding} \le 2.0\text{ s}$$',
        "text": r'<strong>Stand-Alone PV:</strong> Battery storage bank, MPPT charge controller, and off-grid inverter operate autonomously.<br><strong>Grid-Tied PV:</strong> Grid-interactive inverter synchronizes via PLL; mandatory IEEE 1547 anti-islanding shuts down within 2 seconds of grid loss.'
    },
    'res-q11': {
        "eq": r'$$P_w = \frac{1}{2}\rho A v^3, \quad C_p = 4a(1-a)^2, \quad C_{p,\max} = \frac{16}{27} \approx 0.5926 \quad (\text{at } a = 1/3)$$',
        "text": r'<strong>Wind Power:</strong> Proportional to cube of wind speed ($v^3$).<br><strong>Betz Limit:</strong> By 1D actuator disc theory, optimal axial induction factor is $a = 1/3$, establishing maximum aerodynamic power coefficient $C_{p,\max} = 16/27 \approx 59.3\%$.'
    },
    'res-q12': {
        "eq": r'$$\lambda = \frac{\omega R}{v}, \quad HAWT: \lambda \approx 7-10 \ (C_p \approx 0.48), \quad VAWT: \lambda \approx 1-4$$',
        "text": r'<strong>HAWT:</strong> Lift-based airfoil blades with high tip-speed ratio ($\lambda$) and high efficiency ($C_p \approx 0.48$); requires active yaw tracking.<br><strong>VAWT:</strong> Savonius (drag) and Darrieus (lift) operate omnidirectionally with ground-level drive train, but lower efficiency and high cyclic fatigue.'
    },
    'res-q13': {
        "eq": r'$$n_{generator} = G_{ratio} \times n_{rotor} \implies 1500\text{ rpm} = 100 \times 15\text{ rpm}$$',
        "text": r'Nacelle houses low-speed shaft ($15\text{ rpm}$), planetary/helical gearbox ($1:100$ speed increase), high-speed shaft with mechanical disc brake, generator, independent blade pitch actuators, yaw ring drive, and anemometer sensors.'
    },
    'res-q14': {
        "eq": r'$$P_{rotor} = s \cdot P_{stator}, \quad s = \frac{N_s - N_r}{N_s} \in [-0.3, +0.3], \quad P_{net} = P_{stator} + |P_{rotor}|$$',
        "text": r'<strong>DFIG:</strong> Stator connects directly to grid; rotor connects via slip rings and partial-scale converter ($25-30\%$ rating) handling slip power.<br><strong>PMSG:</strong> Direct-drive multi-pole synchronous machine with permanent magnets; connected via $100\%$ full-scale converter, eliminating gearbox.'
    },
    'res-q15': {
        "eq": r'$$T_e = k_{opt}\omega^2 \ (\text{Region 2 MPPT}), \quad P = P_{rated} = \text{const} \ (\text{Region 3 Pitch Regulation})$$',
        "text": r'<strong>Region 1:</strong> Below cut-in ($<3\text{ m/s}$).<br><strong>Region 2:</strong> MPPT ($3-12\text{ m/s}$) tracking optimal tip-speed ratio ($\lambda_{opt}$).<br><strong>Region 3:</strong> Rated power ($12-25\text{ m/s}$) where pitch actuators feather blades.<br><strong>Region 4:</strong> Cut-out ($>25\text{ m/s}$) shutdown.'
    },
    'res-q16': {
        "eq": r'$$C + CO_2 \rightleftharpoons 2 CO, \quad C + H_2 O \rightleftharpoons CO + H_2, \quad \text{LHV} \approx 4.5-6.0\text{ MJ/Nm}^3$$',
        "text": r'<strong>Direct Combustion:</strong> Full oxidation with excess air ($800-1100^\circ\text{C}$).<br><strong>Gasification:</strong> Partial oxidation ($\lambda = 0.3$) producing syngas/producer gas ($CO + H_2$).<br><strong>Pyrolysis:</strong> Oxygen-free thermal cracking at $500^\circ\text{C}$ yielding liquid bio-oil.'
    },
    'res-q17': {
        "eq": r'$$\text{Hydrolysis} \to \text{Acidogenesis (VFAs)} \to \text{Acetogenesis (Acetic Acid)} \to \text{Methanogenesis (CH}_4\text{)}$$',
        "text": r'Anaerobic digestion degrades organic matter in four steps. Methanogens convert acetic acid and $H_2 + CO_2$ to methane ($55-70\% \text{ CH}_4$). Optimum parameters: $C/N = 25-30:1$, mesophilic temp $35-38^\circ\text{C}$, neutral pH $6.8-7.5$.'
    },
    'res-q18': {
        "eq": r'$$P_{KVIC} = \text{Constant } (8-12\text{ cm } H_2O), \quad P_{Deenabandhu} = \text{Variable } (0-100\text{ cm } H_2O)$$',
        "text": r'<strong>Floating Drum (KVIC):</strong> Inverted mild steel drum maintains constant gas pressure; higher cost and corrosion.<br><strong>Fixed Dome (Deenabandhu):</strong> Underground brick masonry dome with slurry displacement chamber; lower cost, zero moving parts, long lifespan.'
    },
    'res-q19': {
        "eq": r'$$\eta_{Carnot} = \frac{T_H - T_C}{T_H} \approx \frac{300.15 - 278.15}{300.15} \approx 7.33\%, \quad \eta_{net} \approx 2.5-4.0\%$$',
        "text": r'OTEC exploits thermal gradient ($\Delta T \approx 20^\circ\text{C}$) between surface warm water ($26^\circ\text{C}$) and deep water ($5^\circ\text{C}$). Closed Rankine cycle uses ammonia; Open Claude cycle flash-evaporates seawater into low-pressure steam, co-producing desalinated water.'
    },
    'res-q20': {
        "eq": r'$$E = \frac{1}{2} \rho g A R^2, \quad P_{avg} = \frac{\rho g A R^2}{2 T_{tide}}, \quad \text{Wells Turbine Lift: } F_{tan} > 0 \ (\forall \text{ flow})$$',
        "text": r'<strong>Tidal Barrage:</strong> Potential energy is proportional to basin area $A$ and square of tidal range ($R^2$).<br><strong>Oscillating Water Column (OWC):</strong> Waves compress/expand air column driving a Wells turbine whose symmetrical blades rotate unidirectionally.'
    },
    'res-q21': {
        "eq": r'$$E_0 = -\frac{\Delta G}{n F} \approx 1.229\text{ V}, \quad \eta_{th} = \frac{\Delta G}{\Delta H} \approx 83.0\%, \quad V_{cell} = E_0 - \Delta V_{act} - \Delta V_{ohm} - \Delta V_{conc}$$',
        "text": r'Hydrogen fuel cell converts chemical energy directly into DC electricity and water. Thermodynamic efficiency is $\Delta G / \Delta H \approx 83\%$. Polarization overpotentials comprise activation (charge transfer), ohmic (electrolyte resistance), and concentration (mass transport).'
    },
    'res-q22': {
        "eq": r'$$\text{PEMFC: } H^+ \text{ ion, } 60-80^\circ\text{C}, \ Pt \text{ catalyst}; \quad \text{SOFC: } O^{2-} \text{ ion, } 700-1000^\circ\text{C}, \ \text{YSZ ceramic}$$',
        "text": r'<strong>PEMFC:</strong> Solid polymer membrane conducts protons at $80^\circ\text{C}$ with Pt catalyst; fast startup for FCEVs, requires pure $H_2$.<br><strong>SOFC:</strong> Yttria-stabilized zirconia ceramic conducts $O^{2-}$ at $800-1000^\circ\text{C}$; fuel-flexible (internal reforming of $CH_4$), excellent for CHP baseload.'
    },
    'res-q23': {
        "eq": r'$$SoC(t) = SoC(t_0) - \frac{1}{Q_n}\int I(t)\,dt, \quad DoD = 1 - SoC, \quad \text{VRFB: } V^{2+}/V^{3+} \leftrightarrow V^{4+}/V^{5+}$$',
        "text": r'<strong>BESS:</strong> Lithium-ion ($90-95\%$ efficiency, $150-250\text{ Wh/kg}$) dominates EVs and grid support.<br><strong>Redox Flow (VRFB):</strong> Liquid vanadium electrolytes decouple power (stack area) from energy (tank volume).<br><strong>Degradation:</strong> SEI growth, lithium plating, and high DoD cycling.'
    },
    'res-q24': {
        "eq": r'$$P_{ren}(t) = P_{pv}(t) + P_{wind}(t), \quad P_{net}(t) = P_{load}(t) - P_{ren}(t) = P_{batt}(t) + P_{diesel}(t)$$',
        "text": r'Hybrid renewable systems exploit seasonal and diurnal complementarity between solar and wind.<br><strong>DC-Coupled:</strong> High battery charging efficiency via common DC bus.<br><strong>AC-Coupled:</strong> High modularity with standard grid inverters.<br><strong>EMS Dispatch:</strong> Prioritizes renewables $\to$ battery $\to$ diesel generator.'
    },
    'res-q25': {
        "eq": r'$$f = f_0 - m_p(P - P_0), \quad V = V_0 - n_q(Q - Q_0), \quad m_p = \frac{\Delta f_{\max}}{P_{\max}}$$',
        "text": r'<strong>Microgrid Modes:</strong> Grid-connected (inverters follow P-Q grid) vs Islanded (grid-forming inverters regulate $V$ and $f$).<br><strong>Droop Control:</strong> Emulates synchronous generator governor via $P-f$ active droop and $Q-V$ reactive droop, enabling decentralized power sharing without communications.'
    },
    'res-q26': {
        "eq": r'$$\frac{df}{dt} = \frac{f_0 (P_m - P_e)}{2 H S_n}, \quad I_q \ge 2\% \text{ per } 1\% \ \Delta V \ (\text{LVRT})$$',
        "text": r'<strong>Duck Curve:</strong> Midday net-load plunge followed by steep evening ramp requirement.<br><strong>Low Inertia:</strong> Non-synchronous inverters lower system inertia $H$, amplifying $RoCoF$.<br><strong>LVRT:</strong> Mandatory grid code requiring inverters to stay connected and inject reactive current $I_q$ during grid faults down to $0.15\text{ pu}$.'
    }
}

RES_EXAM_QUESTIONS = {
    "res-q1": "Explain the terms extraterrestrial and terrestrial solar radiation. Define solar constant and air mass ratio with standard values.",
    "res-q2": "Define the following solar angles with neat sketches: (i) Declination angle, (ii) Hour angle, (iii) Solar altitude angle, (iv) Zenith angle, and (v) Solar azimuth angle.",
    "res-q3": "Explain with neat sketches the construction and working principles of a Pyranometer and a Pyrheliometer for measuring solar radiation.",
    "res-q4": "Derive the single-diode equivalent circuit model and the governing I-V characteristic equation of a practical solar photovoltaic cell.",
    "res-q5": "Define Open-Circuit Voltage, Short-Circuit Current, Maximum Power Point, Fill Factor, and Conversion Efficiency of a PV cell with step-by-step numerical calculation.",
    "res-q6": "Explain the construction and working of a liquid flat-plate solar collector. Derive the Hottel-Whillier-Bliss useful energy balance equation and efficiency.",
    "res-q7": "Classify concentrating solar thermal collectors. Compare Parabolic Trough, Linear Fresnel, Solar Power Tower, and Parabolic Dish systems.",
    "res-q8": "Explain the effects of partial shading on PV module I-V and P-V characteristics. Discuss hot-spot formation and the protective role of bypass and blocking diodes.",
    "res-q9": "Explain the Maximum Power Point Tracking (MPPT) principle. Derive the mathematical formulation of Perturb & Observe (P&O) and Incremental Conductance algorithms.",
    "res-q10": "Compare grid-tied and stand-alone solar PV systems with functional block diagrams, balance of system (BOS) components, and inverter configurations.",
    "res-q11": "Derive the expression for total power in an unconstrained wind stream. Derive the Betz limit for maximum theoretical power extraction using actuator disc theory.",
    "res-q12": "Compare Horizontal Axis Wind Turbines (HAWT) and Vertical Axis Wind Turbines (VAWT) in terms of aerodynamic principles, lift vs drag, tip-speed ratio, and efficiency.",
    "res-q13": "Draw a neat cutaway diagram of a utility-scale HAWT nacelle and explain the functions of the drive train, gearbox, yaw mechanism, and pitch control.",
    "res-q14": "Compare the operation, converter sizing, and characteristics of Doubly Fed Induction Generators (DFIG) and Permanent Magnet Synchronous Generators (PMSG) for wind turbines.",
    "res-q15": "Explain the wind turbine power curve across operating Regions 1 to 4. Compare pitch control, passive stall, and active stall aerodynamic power regulation.",
    "res-q16": "Explain the thermochemical conversion pathways of biomass: Direct Combustion, Gasification (chemical reactions and gasifier types), and Pyrolysis.",
    "res-q17": "Explain the biochemical process of biogas production through anaerobic digestion detailing the four stages: Hydrolysis, Acidogenesis, Acetogenesis, and Methanogenesis.",
    "res-q18": "Compare the construction, operational gas pressure, capital cost, and maintenance of Floating Drum (KVIC) and Fixed Dome (Deenabandhu) biogas plants.",
    "res-q19": "Explain the thermodynamic principle of Ocean Thermal Energy Conversion (OTEC). Compare Open-Cycle (Claude) and Closed-Cycle (Rankine) OTEC systems with Carnot limits.",
    "res-q20": "Derive the theoretical potential energy stored in a tidal barrage basin per tidal cycle. Explain the working of an Oscillating Water Column (OWC) with a Wells turbine.",
    "res-q21": "Explain the working principle of a hydrogen-oxygen fuel cell. Derive the theoretical thermodynamic efficiency and describe the V-I polarization curve overpotentials.",
    "res-q22": "Compare Proton Exchange Membrane Fuel Cells (PEMFC) and Solid Oxide Fuel Cells (SOFC) in terms of electrolyte, operating temperature, catalysts, and applications.",
    "res-q23": "Describe Battery Energy Storage Systems (BESS). Define State of Charge (SoC), Depth of Discharge (DoD), C-rate, round-trip efficiency, and degradation mechanisms.",
    "res-q24": "Explain the architecture of a Hybrid Renewable Energy System (HRES). Compare DC-coupled and AC-coupled topologies, and describe the energy dispatch strategy.",
    "res-q25": "Explain AC and DC microgrid architectures. Discuss grid-connected and islanded modes, and derive the decentralized P-f and Q-V droop control equations.",
    "res-q26": "Discuss the major grid integration challenges of high-penetration renewables: Duck curve, loss of rotational inertia, power quality harmonics, and Low-Voltage Fault Ride-Through (LVRT)."
}
'''

with open("scratch/gen_res.py", "w", encoding="utf-8") as f:
    f.write(res_code)
print("Successfully generated scratch/gen_res.py")
