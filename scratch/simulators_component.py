# scratch/simulators_component.py
# High-performance 60fps Interactive Engineering Simulators with Slider Bars
# Designed for ACS, Electric Drives, and Mobile Computing standalone pages and animations.html

def get_acs_simulators_html():
    return r"""
    <!-- 60fps Interactive Simulator Hub: Advanced Control Systems -->
    <section class="subject-sim-hub" id="acs-sim-hub">
        <div class="sim-hub-header">
            <div class="sim-hub-title-group">
                <span class="sim-hub-icon">🌀</span>
                <div>
                    <h3 class="sim-hub-title">60fps Interactive Simulators: Advanced Control Systems</h3>
                    <p class="sim-hub-desc">Interact with state space dynamics, nonlinear limit cycles, and closed-loop pole placement in real time using the slider bars.</p>
                </div>
            </div>
            <div class="sim-tab-selectors" role="tablist">
                <button type="button" class="sim-tab-btn active" onclick="switchAcsSim('phase')">1. Phase Plane &amp; Limit Cycles</button>
                <button type="button" class="sim-tab-btn" onclick="switchAcsSim('pole')">2. State Feedback &amp; Transient Response</button>
            </div>
        </div>

        <!-- Simulator 1: Phase Plane & Limit Cycle -->
        <div class="sim-container" id="acs-sim-phase">
            <div class="sim-canvas-wrap">
                <canvas id="acs-phase-canvas"></canvas>
            </div>
            <div class="sim-controls-bar">
                <div class="sim-control-item">
                    <label for="acs-select-sys">Nonlinear System:</label>
                    <select id="acs-select-sys" class="sim-select" onchange="resetAcsPhase()">
                        <option value="vanderpol">Van der Pol Oscillator (Limit Cycle)</option>
                        <option value="relay">Relay with Dead Zone (Chatter)</option>
                        <option value="saddle">Unstable Saddle Point</option>
                        <option value="harmonic">Undamped Center (Ellipses)</option>
                    </select>
                </div>
                <div class="sim-control-item">
                    <label for="acs-slider-mu">Damping $\mu$: <span id="acs-val-mu" class="slider-val">0.8</span></label>
                    <input type="range" id="acs-slider-mu" class="sim-slider" min="0.1" max="2.5" step="0.1" value="0.8">
                </div>
                <div class="sim-control-item">
                    <label for="acs-slider-speed">Simulation Speed: <span id="acs-val-speed" class="slider-val">1.0x</span></label>
                    <input type="range" id="acs-slider-speed" class="sim-slider" min="0.5" max="2.5" step="0.25" value="1.0">
                </div>
                <button type="button" class="sim-action-btn" onclick="clearAcsPhase()">🧹 Clear Trajectories</button>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight:</strong> Click anywhere on the 2D grid to inject state disturbances $(x_1, x_2)$! Watch the trajectory automatically spiral onto the stable limit cycle orbit where non-linear energy dissipation balances energy generation.
            </div>
        </div>

        <!-- Simulator 2: Pole Placement & Transient Response -->
        <div class="sim-container" id="acs-sim-pole" style="display:none;">
            <div class="sim-dual-canvas-grid">
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Time-Domain Step Response $x_1(t)$ &amp; Velocity $x_2(t)$</div>
                    <canvas id="acs-transient-canvas"></canvas>
                </div>
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Complex $s$-Plane Closed-Loop Poles $s = -\zeta\omega_n \pm j\omega_d$</div>
                    <canvas id="acs-splane-canvas"></canvas>
                </div>
            </div>
            <div class="sim-controls-bar">
                <div class="sim-control-item">
                    <label for="acs-slider-wn">Natural Frequency $\omega_n$: <span id="acs-val-wn" class="slider-val">3.0 rad/s</span></label>
                    <input type="range" id="acs-slider-wn" class="sim-slider" min="1.0" max="6.0" step="0.2" value="3.0">
                </div>
                <div class="sim-control-item">
                    <label for="acs-slider-zeta">Damping Ratio $\zeta$: <span id="acs-val-zeta" class="slider-val">0.45</span></label>
                    <input type="range" id="acs-slider-zeta" class="sim-slider" min="0.05" max="1.8" step="0.05" value="0.45">
                </div>
                <button type="button" class="sim-action-btn" onclick="injectAcsStep()">⚡ Step Input</button>
                <span id="acs-damping-type" class="sim-type-badge">Underdamped ($\zeta < 1$)</span>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight (Ackermann's Formula):</strong> As you increase damping ratio $\zeta$ past $1.0$, the complex conjugate poles split into two distinct real poles on the negative real axis (Overdamped), completely eliminating overshoot $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$.
            </div>
        </div>
    </section>
    """

def get_drives_simulators_html():
    return r"""
    <!-- 60fps Interactive Simulator Hub: Electric Drives -->
    <section class="subject-sim-hub" id="drives-sim-hub">
        <div class="sim-hub-header">
            <div class="sim-hub-title-group">
                <span class="sim-hub-icon">⚡</span>
                <div>
                    <h3 class="sim-hub-title">60fps Interactive Simulators: Electric Drives</h3>
                    <p class="sim-hub-desc">Explore sinusoidal inverter PWM modulation, converter firing angle speed control, and conduction modes using real-time slider bars.</p>
                </div>
            </div>
            <div class="sim-tab-selectors" role="tablist">
                <button type="button" class="sim-tab-btn active" onclick="switchDriveSim('pwm')">1. Inverter SPWM Synthesizer</button>
                <button type="button" class="sim-tab-btn" onclick="switchDriveSim('converter')">2. Converter DC Drive Firing Angle</button>
            </div>
        </div>

        <!-- Simulator 1: Inverter SPWM -->
        <div class="sim-container" id="drives-sim-pwm">
            <div class="sim-canvas-wrap">
                <canvas id="drives-pwm-canvas"></canvas>
            </div>
            <div class="sim-controls-bar">
                <div class="sim-control-item">
                    <label for="drives-slider-ma">Modulation Index $m_a = V_m/V_c$: <span id="drives-val-ma" class="slider-val">0.85</span></label>
                    <input type="range" id="drives-slider-ma" class="sim-slider" min="0.2" max="1.4" step="0.05" value="0.85" style="accent-color:#f59e0b;">
                </div>
                <div class="sim-control-item">
                    <label for="drives-slider-mf">Carrier Ratio $m_f = f_c/f_m$: <span id="drives-val-mf" class="slider-val">15</span></label>
                    <input type="range" id="drives-slider-mf" class="sim-slider" min="9" max="27" step="2" value="15" style="accent-color:#f59e0b;">
                </div>
                <button type="button" class="sim-action-btn" id="drives-btn-pause" onclick="toggleDrivePWMPause()">⏸️ Pause Wave</button>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight:</strong> When $m_a \le 1.0$, fundamental AC output voltage scales linearly $V_{AO1} = m_a \frac{V_{dc}}{2}$. When $m_a > 1.0$ (Overmodulation), the pulse widths saturate at the peaks, pushing the inverter into square-wave six-step mode.
            </div>
        </div>

        <!-- Simulator 2: Converter DC Drive Firing Angle & Conduction Mode -->
        <div class="sim-container" id="drives-sim-converter" style="display:none;">
            <div class="sim-dual-canvas-grid">
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Armature Current $i_a(t)$ &amp; Terminal Voltage $v_o(t)$</div>
                    <canvas id="drives-converter-canvas"></canvas>
                </div>
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Motor Torque-Speed Curve $(T_e, \omega_m)$</div>
                    <canvas id="drives-speedtorque-canvas"></canvas>
                </div>
            </div>
            <div class="sim-controls-bar">
                <div class="sim-control-item">
                    <label for="drives-slider-alpha">Firing Angle $\alpha$: <span id="drives-val-alpha" class="slider-val">45&deg;</span></label>
                    <input type="range" id="drives-slider-alpha" class="sim-slider" min="0" max="150" step="5" value="45" style="accent-color:#f59e0b;">
                </div>
                <div class="sim-control-item">
                    <label for="drives-slider-torque">Load Torque $T_L$: <span id="drives-val-torque" class="slider-val">1.0 p.u.</span></label>
                    <input type="range" id="drives-slider-torque" class="sim-slider" min="0.1" max="2.0" step="0.1" value="1.0" style="accent-color:#f59e0b;">
                </div>
                <div class="sim-control-item">
                    <label for="drives-slider-induct">Armature Inductance $L_a$: <span id="drives-val-induct" class="slider-val">Medium</span></label>
                    <input type="range" id="drives-slider-induct" class="sim-slider" min="1" max="3" step="1" value="2" style="accent-color:#f59e0b;">
                </div>
                <span id="drives-conduction-mode" class="sim-type-badge" style="background:rgba(16,185,129,0.2); color:#34d399;">Continuous (CCM)</span>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight:</strong> Notice what happens when you lower load torque $T_L$ with low inductance: current drops to zero before the next firing pulse (Discontinuous Conduction Mode DCM)! Speed shoots up sharply due to lack of load current extinction.
            </div>
        </div>
    </section>
    """

def get_mobile_simulators_html():
    return r"""
    <!-- 60fps Interactive Simulator Hub: Mobile Computing -->
    <section class="subject-sim-hub" id="mobile-sim-hub">
        <div class="sim-hub-header">
            <div class="sim-hub-title-group">
                <span class="sim-hub-icon">📡</span>
                <div>
                    <h3 class="sim-hub-title">60fps Interactive Simulators: Mobile Computing</h3>
                    <p class="sim-hub-desc">Visualize cellular frequency reuse geometry, dynamic handover signal thresholds, and wireless CSMA/CA MAC packet contention.</p>
                </div>
            </div>
            <div class="sim-tab-selectors" role="tablist">
                <button type="button" class="sim-tab-btn active" onclick="switchMobileSim('handover')">1. Cellular Handover &amp; Hysteresis</button>
                <button type="button" class="sim-tab-btn" onclick="switchMobileSim('mac')">2. CSMA/CA Virtual Carrier Sensing (RTS/CTS)</button>
            </div>
        </div>

        <!-- Simulator 1: Cellular Handover & RSSI -->
        <div class="sim-container" id="mobile-sim-handover">
            <div class="sim-dual-canvas-grid">
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Cellular Hexagonal Grid &amp; Moving Vehicle</div>
                    <canvas id="mobile-hex-canvas"></canvas>
                </div>
                <div class="sim-sub-canvas-wrap">
                    <div class="sub-canvas-title">Received Signal Strength (RSSI) &amp; Handover Margin $\Delta$</div>
                    <canvas id="mobile-rssi-canvas"></canvas>
                </div>
            </div>
            <div class="sim-controls-bar">
                <div class="sim-control-item">
                    <label for="mobile-slider-speed">Vehicle Speed $v$: <span id="mobile-val-speed" class="slider-val">50 km/h</span></label>
                    <input type="range" id="mobile-slider-speed" class="sim-slider" min="20" max="120" step="10" value="50" style="accent-color:#ec4899;">
                </div>
                <div class="sim-control-item">
                    <label for="mobile-slider-margin">Hysteresis Margin $\Delta$: <span id="mobile-val-margin" class="slider-val">6 dB</span></label>
                    <input type="range" id="mobile-slider-margin" class="sim-slider" min="1" max="14" step="1" value="6" style="accent-color:#ec4899;">
                </div>
                <button type="button" class="sim-action-btn" onclick="resetMobileCar()">🚗 Restart Vehicle</button>
                <span id="mobile-ho-status" class="sim-type-badge" style="background:rgba(56,189,248,0.2); color:#38bdf8;">Connected: Base Station A</span>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight:</strong> The <strong>hysteresis margin $\Delta = P_{ho} - P_{min}$</strong> prevents the "Ping-Pong effect" (repeated unnecessary handovers between two base stations due to rapid shadow fading fluctuations).
            </div>
        </div>

        <!-- Simulator 2: CSMA/CA MAC Handshake -->
        <div class="sim-container" id="mobile-sim-mac" style="display:none;">
            <div class="sim-canvas-wrap">
                <canvas id="mobile-mac-canvas"></canvas>
            </div>
            <div class="sim-controls-bar">
                <button type="button" class="sim-action-btn" id="mobile-btn-toggle-rts" onclick="toggleMobileRTS()">Mode: With RTS/CTS (Collision Free)</button>
                <button type="button" class="sim-action-btn" onclick="triggerMobileTransmit()">🚀 Trigger Packet Transmission</button>
                <span id="mobile-mac-status-text" class="sim-type-badge" style="background:rgba(16,185,129,0.2); color:#34d399;">Medium Status: Idle</span>
            </div>
            <div class="sim-insight-box">
                💡 <strong>Exam Insight:</strong> Without RTS/CTS, hidden terminals Node A and Node C collide at the Access Point because wireless radios cannot perform Ethernet-style Collision Detection (CSMA/CD) while transmitting.
            </div>
        </div>
    </section>
    """

def get_simulators_css():
    return r"""
/* ==========================================================================
   60fps Interactive Simulator Hub Styles & Slider Controls
   ========================================================================== */
.subject-sim-hub {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 20px;
    padding: 1.5rem;
    margin-bottom: 2.5rem;
    box-shadow: var(--card-shadow);
}

.sim-hub-header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border-subtle);
}

.sim-hub-title-group {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.sim-hub-icon {
    font-size: 1.6rem;
}

.sim-hub-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -0.02em;
}

.sim-hub-desc {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-top: 0.15rem;
}

.sim-tab-selectors {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--bg-surface);
    padding: 0.3rem;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
}

.sim-tab-btn {
    background: transparent;
    border: none;
    color: var(--text-muted);
    font-size: 0.82rem;
    font-weight: 600;
    padding: 0.4rem 0.85rem;
    border-radius: 7px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.sim-tab-btn:hover {
    color: var(--text-main);
}

.sim-tab-btn.active {
    background: var(--bg-card);
    color: #ffffff;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.sim-canvas-wrap {
    background: #060910;
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    position: relative;
    overflow: hidden;
    height: 360px;
    margin-bottom: 1rem;
}

.sim-canvas-wrap canvas {
    width: 100%;
    height: 100%;
    display: block;
}

.sim-dual-canvas-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
}

.sim-sub-canvas-wrap {
    background: #060910;
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
}

.sub-canvas-title {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
}

.sim-sub-canvas-wrap canvas {
    width: 100%;
    height: 280px;
    display: block;
    border-radius: 8px;
}

.sim-controls-bar {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 0.85rem 1.25rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 1.25rem;
    margin-bottom: 0.85rem;
}

.sim-control-item {
    display: flex;
    align-items: center;
    gap: 0.65rem;
}

.sim-control-item label {
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-main);
}

.slider-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #38bdf8;
    min-width: 45px;
}

.sim-slider {
    width: 125px;
    cursor: pointer;
    accent-color: #38bdf8;
}

.sim-select {
    background: var(--bg-card);
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
    font-size: 0.82rem;
    font-weight: 600;
    padding: 0.35rem 0.65rem;
    border-radius: 6px;
    outline: none;
    cursor: pointer;
}

.sim-action-btn {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid var(--border-subtle);
    color: var(--text-main);
    padding: 0.4rem 0.85rem;
    border-radius: 8px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.sim-action-btn:hover {
    background: rgba(255, 255, 255, 0.16);
    border-color: #38bdf8;
}

.sim-type-badge {
    font-size: 0.78rem;
    font-weight: 700;
    padding: 0.25rem 0.65rem;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    white-space: nowrap;
}

.sim-insight-box {
    background: rgba(0, 0, 0, 0.25);
    border-left: 3px solid #38bdf8;
    border-radius: 0 8px 8px 0;
    padding: 0.65rem 0.95rem;
    font-size: 0.82rem;
    color: var(--text-body);
    line-height: 1.45;
}

@media (max-width: 850px) {
    .sim-dual-canvas-grid {
        grid-template-columns: 1fr;
    }
    .sim-sub-canvas-wrap canvas {
        height: 220px;
    }
    .sim-canvas-wrap {
        height: 280px;
    }
    .sim-controls-bar {
        gap: 0.75rem;
    }
}
"""

def get_simulators_js():
    return r"""
// =========================================================================
// 60FPS SIMULATOR HUB SCRIPTS (ACS, DRIVES, MOBILE)
// =========================================================================

// --- ACS SIMULATOR SWITCHER ---
function switchAcsSim(name) {
    document.querySelectorAll('#acs-sim-hub .sim-tab-btn').forEach((btn, idx) => {
        if ((name === 'phase' && idx === 0) || (name === 'pole' && idx === 1)) btn.classList.add('active');
        else btn.classList.remove('active');
    });
    const phaseEl = document.getElementById('acs-sim-phase');
    const poleEl = document.getElementById('acs-sim-pole');
    if (phaseEl && poleEl) {
        phaseEl.style.display = name === 'phase' ? 'block' : 'none';
        poleEl.style.display = name === 'pole' ? 'block' : 'none';
    }
}

// --- DRIVES SIMULATOR SWITCHER ---
function switchDriveSim(name) {
    document.querySelectorAll('#drives-sim-hub .sim-tab-btn').forEach((btn, idx) => {
        if ((name === 'pwm' && idx === 0) || (name === 'converter' && idx === 1)) btn.classList.add('active');
        else btn.classList.remove('active');
    });
    const pwmEl = document.getElementById('drives-sim-pwm');
    const convEl = document.getElementById('drives-sim-converter');
    if (pwmEl && convEl) {
        pwmEl.style.display = name === 'pwm' ? 'block' : 'none';
        convEl.style.display = name === 'converter' ? 'block' : 'none';
    }
}

// --- MOBILE SIMULATOR SWITCHER ---
function switchMobileSim(name) {
    document.querySelectorAll('#mobile-sim-hub .sim-tab-btn').forEach((btn, idx) => {
        if ((name === 'handover' && idx === 0) || (name === 'mac' && idx === 1)) btn.classList.add('active');
        else btn.classList.remove('active');
    });
    const hoEl = document.getElementById('mobile-sim-handover');
    const macEl = document.getElementById('mobile-sim-mac');
    if (hoEl && macEl) {
        hoEl.style.display = name === 'handover' ? 'block' : 'none';
        macEl.style.display = name === 'mac' ? 'block' : 'none';
    }
}

// =========================================================================
// ACS SIMULATOR 1: PHASE PLANE & LIMIT CYCLES
// =========================================================================
(function initAcsPhase() {
    const canvas = document.getElementById('acs-phase-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const selectSys = document.getElementById('acs-select-sys');
    const sliderMu = document.getElementById('acs-slider-mu');
    const valMu = document.getElementById('acs-val-mu');
    const sliderSpeed = document.getElementById('acs-slider-speed');
    const valSpeed = document.getElementById('acs-val-speed');

    let trajectories = [];
    let particles = [];

    function resize() {
        if (!canvas.parentElement) return;
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = 360;
        reset();
    }
    window.addEventListener('resize', resize);

    function reset() {
        trajectories = [];
        particles = [];
        spawn(-1.8, -0.4);
        spawn(0.2, 0.2);
        spawn(2.2, 1.2);
    }
    window.resetAcsPhase = reset;
    window.clearAcsPhase = () => { trajectories = []; particles = []; };

    sliderMu.addEventListener('input', e => {
        valMu.textContent = parseFloat(e.target.value).toFixed(1);
    });
    sliderSpeed.addEventListener('input', e => {
        valSpeed.textContent = parseFloat(e.target.value).toFixed(2) + 'x';
    });

    function spawn(x0, y0) {
        const path = [{ x: x0, y: y0 }];
        let curX = x0, curY = y0;
        const dt = 0.02;
        const mu = parseFloat(sliderMu.value);
        const sys = selectSys.value;

        for (let i = 0; i < 400; i++) {
            let dx, dy;
            if (sys === 'vanderpol') {
                dx = curY;
                dy = mu * (1 - curX * curX) * curY - curX;
            } else if (sys === 'relay') {
                dx = curY;
                const dead = 0.4;
                let u = 0;
                if (curX > dead) u = -1.2;
                else if (curX < -dead) u = 1.2;
                dy = -0.3 * curY + u;
            } else if (sys === 'saddle') {
                dx = 1.2 * curX;
                dy = -1.2 * curY;
            } else {
                dx = curY;
                dy = -curX;
            }
            curX += dx * dt;
            curY += dy * dt;
            path.push({ x: curX, y: curY });
            if (Math.abs(curX) > 4 || Math.abs(curY) > 4) break;
        }
        trajectories.push(path);
        particles.push({ path, idx: 0 });
    }

    canvas.addEventListener('click', e => {
        const rect = canvas.getBoundingClientRect();
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        const scale = 55;
        const clickX = (e.clientX - rect.left - cx) / scale;
        const clickY = -(e.clientY - rect.top - cy) / scale;
        spawn(clickX, clickY);
    });

    function draw() {
        const w = canvas.width, h = canvas.height;
        ctx.clearRect(0, 0, w, h);
        const cx = w / 2, cy = h / 2, scale = 55;

        // Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
        ctx.lineWidth = 1;
        for (let x = cx % 40; x < w; x += 40) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
        }
        for (let y = cy % 40; y < h; y += 40) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
        }

        // Axes
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(0, cy); ctx.lineTo(w, cy);
        ctx.moveTo(cx, 0); ctx.lineTo(cx, h);
        ctx.stroke();

        ctx.fillStyle = '#8292a8';
        ctx.font = '11px Inter';
        ctx.fillText('x\u2081 (State)', w - 70, cy - 8);
        ctx.fillText('x\u2082 (Velocity)', cx + 8, 20);

        // Trajectories
        trajectories.forEach(path => {
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.45)';
            ctx.lineWidth = 1.6;
            ctx.beginPath();
            path.forEach((pt, idx) => {
                const sx = cx + pt.x * scale;
                const sy = cy - pt.y * scale;
                if (idx === 0) ctx.moveTo(sx, sy);
                else ctx.lineTo(sx, sy);
            });
            ctx.stroke();
        });

        // Moving particles
        const speed = parseFloat(sliderSpeed.value);
        particles.forEach(p => {
            p.idx = (p.idx + speed) % p.path.length;
            const pt = p.path[Math.floor(p.idx)];
            if (!pt) return;
            const sx = cx + pt.x * scale;
            const sy = cy - pt.y * scale;

            ctx.shadowBlur = 10;
            ctx.shadowColor = '#38bdf8';
            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(sx, sy, 3.5, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;
        });

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();

// =========================================================================
// ACS SIMULATOR 2: POLE PLACEMENT & TRANSIENT RESPONSE
// =========================================================================
(function initAcsPolePlacement() {
    const tCanvas = document.getElementById('acs-transient-canvas');
    const sCanvas = document.getElementById('acs-splane-canvas');
    if (!tCanvas || !sCanvas) return;

    const tCtx = tCanvas.getContext('2d');
    const sCtx = sCanvas.getContext('2d');
    const sliderWn = document.getElementById('acs-slider-wn');
    const valWn = document.getElementById('acs-val-wn');
    const sliderZeta = document.getElementById('acs-slider-zeta');
    const valZeta = document.getElementById('acs-val-zeta');
    const typeBadge = document.getElementById('acs-damping-type');

    let animTime = 0;

    function resize() {
        if (!tCanvas.parentElement || !sCanvas.parentElement) return;
        tCanvas.width = tCanvas.parentElement.clientWidth - 20;
        tCanvas.height = 280;
        sCanvas.width = sCanvas.parentElement.clientWidth - 20;
        sCanvas.height = 280;
    }
    window.addEventListener('resize', resize);

    sliderWn.addEventListener('input', e => {
        valWn.textContent = parseFloat(e.target.value).toFixed(1) + ' rad/s';
    });
    sliderZeta.addEventListener('input', e => {
        const z = parseFloat(e.target.value);
        valZeta.textContent = z.toFixed(2);
        if (z < 1.0) {
            typeBadge.textContent = 'Underdamped (\u03b6 < 1)';
            typeBadge.style.color = '#38bdf8';
        } else if (Math.abs(z - 1.0) < 0.05) {
            typeBadge.textContent = 'Critically Damped (\u03b6 = 1)';
            typeBadge.style.color = '#34d399';
        } else {
            typeBadge.textContent = 'Overdamped (\u03b6 > 1)';
            typeBadge.style.color = '#fbbf24';
        }
    });

    window.injectAcsStep = () => { animTime = 0; };

    function draw() {
        animTime += 0.02;
        const wn = parseFloat(sliderWn.value);
        const z = parseFloat(sliderZeta.value);

        // 1. Time Domain Canvas
        const tw = tCanvas.width, th = tCanvas.height;
        tCtx.clearRect(0, 0, tw, th);

        // Reference input line y = 1.0
        const yRef = th * 0.4;
        tCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        tCtx.lineWidth = 1;
        tCtx.setLineDash([4, 4]);
        tCtx.beginPath(); tCtx.moveTo(0, yRef); tCtx.lineTo(tw, yRef); tCtx.stroke();
        tCtx.setLineDash([]);

        tCtx.fillStyle = '#8292a8';
        tCtx.font = '10px Inter';
        tCtx.fillText('Step Target y(t) = 1.0', 10, yRef - 6);

        // Waveform
        tCtx.strokeStyle = '#38bdf8';
        tCtx.lineWidth = 2.4;
        tCtx.beginPath();

        const maxT = 6.0;
        for (let px = 0; px < tw; px++) {
            const t = (px / tw) * maxT;
            let yVal = 0;
            if (z < 1.0) {
                const wd = wn * Math.sqrt(1 - z * z);
                const phi = Math.acos(z);
                yVal = 1 - (Math.exp(-z * wn * t) / Math.sqrt(1 - z * z)) * Math.sin(wd * t + phi);
            } else if (Math.abs(z - 1.0) < 0.05) {
                yVal = 1 - (1 + wn * t) * Math.exp(-wn * t);
            } else {
                const s1 = -wn * (z - Math.sqrt(z * z - 1));
                const s2 = -wn * (z + Math.sqrt(z * z - 1));
                yVal = 1 - (s2 * Math.exp(s1 * t) - s1 * Math.exp(s2 * t)) / (s2 - s1);
            }
            const py = (th * 0.85) - yVal * (th * 0.45);
            if (px === 0) tCtx.moveTo(px, py);
            else tCtx.lineTo(px, py);
        }
        tCtx.stroke();

        // 2. Complex S-Plane Canvas
        const sw = sCanvas.width, sh = sCanvas.height;
        sCtx.clearRect(0, 0, sw, sh);
        const scx = sw * 0.7, scy = sh / 2;

        // Background LHP
        sCtx.fillStyle = 'rgba(16, 185, 129, 0.06)';
        sCtx.fillRect(0, 0, scx, sh);

        // Axes
        sCtx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        sCtx.lineWidth = 1;
        sCtx.beginPath();
        sCtx.moveTo(0, scy); sCtx.lineTo(sw, scy);
        sCtx.moveTo(scx, 0); sCtx.lineTo(scx, sh);
        sCtx.stroke();

        // Poles Crosses
        const scale = 25;
        sCtx.strokeStyle = '#38bdf8';
        sCtx.lineWidth = 3;
        const pSize = 7;

        if (z < 1.0) {
            const sigma = -z * wn;
            const wd = wn * Math.sqrt(1 - z * z);
            const poles = [
                { x: scx + sigma * scale, y: scy - wd * scale },
                { x: scx + sigma * scale, y: scy + wd * scale }
            ];
            poles.forEach(p => {
                sCtx.beginPath();
                sCtx.moveTo(p.x - pSize, p.y - pSize); sCtx.lineTo(p.x + pSize, p.y + pSize);
                sCtx.moveTo(p.x + pSize, p.y - pSize); sCtx.lineTo(p.x - pSize, p.y + pSize);
                sCtx.stroke();
            });
        } else {
            const s1 = -wn * (z - Math.sqrt(z * z - 1));
            const s2 = -wn * (z + Math.sqrt(z * z - 1));
            [s1, s2].forEach(sVal => {
                const px = scx + sVal * scale;
                sCtx.beginPath();
                sCtx.moveTo(px - pSize, scy - pSize); sCtx.lineTo(px + pSize, scy + pSize);
                sCtx.moveTo(px + pSize, scy - pSize); sCtx.lineTo(px - pSize, scy + pSize);
                sCtx.stroke();
            });
        }

        sCtx.fillStyle = '#8292a8';
        sCtx.font = '10px Inter';
        sCtx.fillText('j\u03c9', scx + 6, 16);
        sCtx.fillText('\u03c3', sw - 20, scy - 6);

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();

// =========================================================================
// DRIVES SIMULATOR 1: SPWM INVERTER
// =========================================================================
(function initDrivePWM() {
    const canvas = document.getElementById('drives-pwm-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const sliderMa = document.getElementById('drives-slider-ma');
    const valMa = document.getElementById('drives-val-ma');
    const sliderMf = document.getElementById('drives-slider-mf');
    const valMf = document.getElementById('drives-val-mf');

    let time = 0;
    let isPaused = false;

    function resize() {
        if (!canvas.parentElement) return;
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = 360;
    }
    window.addEventListener('resize', resize);

    sliderMa.addEventListener('input', e => { valMa.textContent = parseFloat(e.target.value).toFixed(2); });
    sliderMf.addEventListener('input', e => { valMf.textContent = e.target.value; });
    window.toggleDrivePWMPause = () => {
        isPaused = !isPaused;
        const btn = document.getElementById('drives-btn-pause');
        if (btn) btn.textContent = isPaused ? '▶️ Resume' : '⏸️ Pause Wave';
    };

    function draw() {
        if (!isPaused) time += 0.02;
        const w = canvas.width, h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        const ma = parseFloat(sliderMa.value);
        const mf = parseInt(sliderMf.value);
        const topH = h * 0.45;
        const botH = h * 0.45;
        const cy1 = topH / 2;
        const cy2 = topH + (botH / 2);

        // Separator
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.beginPath(); ctx.moveTo(0, topH); ctx.lineTo(w, topH); ctx.stroke();

        ctx.fillStyle = '#8292a8';
        ctx.font = '11px Inter';
        ctx.fillText('Carrier Wave (Triangle) vs Modulating Wave (Sine)', 15, 20);
        ctx.fillText('Inverter Phase Voltage V_AO(t) Output', 15, topH + 20);

        // Carrier
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        const period = w / (mf / 2);
        for (let x = 0; x < w; x++) {
            const ph = (x % period) / period;
            const tri = (ph < 0.5) ? (4 * ph - 1) : (3 - 4 * ph);
            const y = cy1 - tri * (cy1 * 0.75);
            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Modulating Sine
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.2;
        ctx.beginPath();
        for (let x = 0; x < w; x++) {
            const theta = (x / w) * (Math.PI * 2) + time;
            const sVal = Math.sin(theta) * ma;
            const y = cy1 - sVal * (cy1 * 0.75);
            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // PWM Output Square Wave
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.beginPath();
        let lastHigh = false;
        for (let x = 0; x < w; x++) {
            const ph = (x % period) / period;
            const tri = (ph < 0.5) ? (4 * ph - 1) : (3 - 4 * ph);
            const theta = (x / w) * (Math.PI * 2) + time;
            const sVal = Math.sin(theta) * ma;

            const isHigh = sVal > tri;
            const yVal = isHigh ? (cy2 - botH * 0.32) : (cy2 + botH * 0.32);

            if (x === 0) ctx.moveTo(x, yVal);
            else {
                if (isHigh !== lastHigh) {
                    ctx.lineTo(x, isHigh ? (cy2 + botH * 0.32) : (cy2 - botH * 0.32));
                }
                ctx.lineTo(x, yVal);
            }
            lastHigh = isHigh;
        }
        ctx.stroke();

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();

// =========================================================================
// DRIVES SIMULATOR 2: CONVERTER DC DRIVE FIRING ANGLE & CONDUCTION
// =========================================================================
(function initDriveConverter() {
    const cCanvas = document.getElementById('drives-converter-canvas');
    const sCanvas = document.getElementById('drives-speedtorque-canvas');
    if (!cCanvas || !sCanvas) return;

    const cCtx = cCanvas.getContext('2d');
    const sCtx = sCanvas.getContext('2d');
    const sliderAlpha = document.getElementById('drives-slider-alpha');
    const valAlpha = document.getElementById('drives-val-alpha');
    const sliderTorque = document.getElementById('drives-slider-torque');
    const valTorque = document.getElementById('drives-val-torque');
    const sliderInduct = document.getElementById('drives-slider-induct');
    const valInduct = document.getElementById('drives-val-induct');
    const modeBadge = document.getElementById('drives-conduction-mode');

    function resize() {
        if (!cCanvas.parentElement || !sCanvas.parentElement) return;
        cCanvas.width = cCanvas.parentElement.clientWidth - 20;
        cCanvas.height = 280;
        sCanvas.width = sCanvas.parentElement.clientWidth - 20;
        sCanvas.height = 280;
    }
    window.addEventListener('resize', resize);

    sliderAlpha.addEventListener('input', e => { valAlpha.textContent = e.target.value + '\u00b0'; });
    sliderTorque.addEventListener('input', e => { valTorque.textContent = parseFloat(e.target.value).toFixed(1) + ' p.u.'; });
    sliderInduct.addEventListener('input', e => {
        const v = parseInt(e.target.value);
        valInduct.textContent = v === 1 ? 'Low' : (v === 2 ? 'Medium' : 'High');
    });

    function draw() {
        const alphaDeg = parseFloat(sliderAlpha.value);
        const torque = parseFloat(sliderTorque.value);
        const induct = parseInt(sliderInduct.value);

        // Check if conduction is discontinuous (DCM)
        const isDiscontinuous = (torque < 0.6 && induct === 1) || (torque < 0.35 && induct === 2);
        if (isDiscontinuous) {
            modeBadge.textContent = 'Discontinuous (DCM)';
            modeBadge.style.background = 'rgba(239, 68, 68, 0.2)';
            modeBadge.style.color = '#f87171';
        } else {
            modeBadge.textContent = 'Continuous (CCM)';
            modeBadge.style.background = 'rgba(16, 185, 129, 0.2)';
            modeBadge.style.color = '#34d399';
        }

        // 1. Current Waveform
        const cw = cCanvas.width, ch = cCanvas.height;
        cCtx.clearRect(0, 0, cw, ch);

        cCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        cCtx.beginPath(); cCtx.moveTo(0, ch * 0.7); cCtx.lineTo(cw, ch * 0.7); cCtx.stroke();

        cCtx.strokeStyle = '#f59e0b';
        cCtx.lineWidth = 2.4;
        cCtx.beginPath();
        const baseCurrent = torque * (ch * 0.35);
        for (let x = 0; x < cw; x++) {
            const cycleX = (x % 120) / 120;
            let cur = 0;
            if (isDiscontinuous) {
                // Current drops to zero before cycle ends
                if (cycleX < 0.65) cur = Math.sin(cycleX / 0.65 * Math.PI) * baseCurrent * 1.6;
                else cur = 0;
            } else {
                cur = baseCurrent + Math.sin(cycleX * Math.PI * 2) * (18 / induct);
            }
            const py = (ch * 0.7) - cur;
            if (x === 0) cCtx.moveTo(x, py); else cCtx.lineTo(x, py);
        }
        cCtx.stroke();

        cCtx.fillStyle = '#8292a8';
        cCtx.font = '10px Inter';
        cCtx.fillText('Armature Current i_a(t)', 10, 20);

        // 2. Speed-Torque Curve
        const sw = sCanvas.width, sh = sCanvas.height;
        sCtx.clearRect(0, 0, sw, sh);

        sCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        sCtx.beginPath(); sCtx.moveTo(35, sh - 30); sCtx.lineTo(sw - 10, sh - 30); sCtx.stroke();
        sCtx.beginPath(); sCtx.moveTo(35, sh - 30); sCtx.lineTo(35, 10); sCtx.stroke();

        sCtx.fillStyle = '#8292a8';
        sCtx.font = '10px Inter';
        sCtx.fillText('Torque T_e', sw - 60, sh - 15);
        sCtx.fillText('Speed \u03c9_m', 42, 20);

        // Linear CCM line
        const noLoadSpeed = (sh - 40) - Math.cos(alphaDeg * Math.PI / 180) * (sh * 0.4);
        sCtx.strokeStyle = 'rgba(245, 158, 11, 0.6)';
        sCtx.lineWidth = 2;
        sCtx.beginPath();
        sCtx.moveTo(35, noLoadSpeed);
        sCtx.lineTo(sw - 20, noLoadSpeed + 45);
        sCtx.stroke();

        // Active operating point dot
        const ptX = 35 + torque * ((sw - 60) / 2.0);
        let ptY = noLoadSpeed + (torque * 22);
        if (isDiscontinuous) ptY -= 25; // Sharp speed rise in DCM

        sCtx.fillStyle = '#38bdf8';
        sCtx.shadowBlur = 10;
        sCtx.shadowColor = '#38bdf8';
        sCtx.beginPath();
        sCtx.arc(ptX, ptY, 6, 0, Math.PI * 2);
        sCtx.fill();
        sCtx.shadowBlur = 0;

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();

// =========================================================================
// MOBILE SIMULATOR 1: CELLULAR HANDOVER & RSSI
// =========================================================================
(function initMobileHandover() {
    const hCanvas = document.getElementById('mobile-hex-canvas');
    const rCanvas = document.getElementById('mobile-rssi-canvas');
    if (!hCanvas || !rCanvas) return;

    const hCtx = hCanvas.getContext('2d');
    const rCtx = rCanvas.getContext('2d');
    const sliderSpeed = document.getElementById('mobile-slider-speed');
    const valSpeed = document.getElementById('mobile-val-speed');
    const sliderMargin = document.getElementById('mobile-slider-margin');
    const valMargin = document.getElementById('mobile-val-margin');
    const hoStatus = document.getElementById('mobile-ho-status');

    let carDist = 0.15; // 0.0 to 1.0 (from BTS A to BTS B)
    let connectedBTS = 'A';

    function resize() {
        if (!hCanvas.parentElement || !rCanvas.parentElement) return;
        hCanvas.width = hCanvas.parentElement.clientWidth - 20;
        hCanvas.height = 280;
        rCanvas.width = rCanvas.parentElement.clientWidth - 20;
        rCanvas.height = 280;
    }
    window.addEventListener('resize', resize);

    sliderSpeed.addEventListener('input', e => { valSpeed.textContent = e.target.value + ' km/h'; });
    sliderMargin.addEventListener('input', e => { valMargin.textContent = e.target.value + ' dB'; });
    window.resetMobileCar = () => { carDist = 0.1; connectedBTS = 'A'; };

    function drawHex(ctx, x, y, r, color) {
        ctx.strokeStyle = color;
        ctx.fillStyle = color.replace(')', ', 0.05)').replace('rgb', 'rgba');
        ctx.lineWidth = 1.4;
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            const angle = (i * 60) * Math.PI / 180;
            const hx = x + r * Math.cos(angle);
            const hy = y + r * Math.sin(angle);
            if (i === 0) ctx.moveTo(hx, hy); else ctx.lineTo(hx, hy);
        }
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
    }

    function draw() {
        const hw = hCanvas.width, hh = hCanvas.height;
        hCtx.clearRect(0, 0, hw, hh);

        const vSpeed = parseFloat(sliderSpeed.value);
        const margin = parseFloat(sliderMargin.value);

        // Move car
        carDist += (vSpeed / 120) * 0.003;
        if (carDist > 0.95) carDist = 0.05;

        // Base Stations positions
        const btsA = { x: hw * 0.28, y: hh * 0.5 };
        const btsB = { x: hw * 0.72, y: hh * 0.5 };
        const hexR = hw * 0.22;

        drawHex(hCtx, btsA.x, btsA.y, hexR, 'rgb(56, 189, 248)');
        drawHex(hCtx, btsB.x, btsB.y, hexR, 'rgb(236, 72, 153)');

        // Tower icons
        [btsA, btsB].forEach((bts, idx) => {
            hCtx.fillStyle = idx === 0 ? '#38bdf8' : '#ec4899';
            hCtx.beginPath(); hCtx.arc(bts.x, bts.y, 8, 0, Math.PI * 2); hCtx.fill();
            hCtx.fillStyle = '#ffffff';
            hCtx.font = 'bold 11px Inter';
            hCtx.textAlign = 'center';
            hCtx.fillText(idx === 0 ? 'BTS A' : 'BTS B', bts.x, bts.y - 14);
        });

        // Vehicle
        const carX = btsA.x + (btsB.x - btsA.x) * carDist;
        const carY = hh * 0.5;

        hCtx.fillStyle = '#fbbf24';
        hCtx.shadowBlur = 12;
        hCtx.shadowColor = '#fbbf24';
        hCtx.beginPath();
        hCtx.arc(carX, carY, 6, 0, Math.PI * 2);
        hCtx.fill();
        hCtx.shadowBlur = 0;

        // Signal Calculations
        const rssiA = -40 - (carDist * 60);
        const rssiB = -100 + (carDist * 60);

        // Handover Decision with Hysteresis
        if (connectedBTS === 'A' && rssiB > (rssiA + margin)) {
            connectedBTS = 'B';
        } else if (connectedBTS === 'B' && rssiA > (rssiB + margin)) {
            connectedBTS = 'A';
        }

        hoStatus.textContent = `Connected: Base Station ${connectedBTS}`;
        hoStatus.style.color = connectedBTS === 'A' ? '#38bdf8' : '#ec4899';
        hoStatus.style.background = connectedBTS === 'A' ? 'rgba(56,189,248,0.2)' : 'rgba(236,72,153,0.2)';

        // 2. RSSI Curve Canvas
        const rw = rCanvas.width, rh = rCanvas.height;
        rCtx.clearRect(0, 0, rw, rh);

        rCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
        rCtx.beginPath(); rCtx.moveTo(35, rh - 30); rCtx.lineTo(rw - 10, rh - 30); rCtx.stroke();
        rCtx.beginPath(); rCtx.moveTo(35, rh - 30); rCtx.lineTo(35, 15); rCtx.stroke();

        // Curve A (Cyan)
        rCtx.strokeStyle = '#38bdf8';
        rCtx.lineWidth = 2;
        rCtx.beginPath();
        for (let x = 35; x < rw - 10; x++) {
            const frac = (x - 35) / (rw - 45);
            const rVal = -40 - frac * 60;
            const py = (rh - 30) - (rVal + 110) * (rh * 0.65 / 80);
            if (x === 35) rCtx.moveTo(x, py); else rCtx.lineTo(x, py);
        }
        rCtx.stroke();

        // Curve B (Pink)
        rCtx.strokeStyle = '#ec4899';
        rCtx.lineWidth = 2;
        rCtx.beginPath();
        for (let x = 35; x < rw - 10; x++) {
            const frac = (x - 35) / (rw - 45);
            const rVal = -100 + frac * 60;
            const py = (rh - 30) - (rVal + 110) * (rh * 0.65 / 80);
            if (x === 35) rCtx.moveTo(x, py); else rCtx.lineTo(x, py);
        }
        rCtx.stroke();

        // Vertical car position marker on RSSI graph
        const curPx = 35 + carDist * (rw - 45);
        rCtx.strokeStyle = '#fbbf24';
        rCtx.lineWidth = 1.5;
        rCtx.setLineDash([3, 3]);
        rCtx.beginPath(); rCtx.moveTo(curPx, 15); rCtx.lineTo(curPx, rh - 30); rCtx.stroke();
        rCtx.setLineDash([]);

        rCtx.fillStyle = '#8292a8';
        rCtx.font = '10px Inter';
        rCtx.textAlign = 'left';
        rCtx.fillText('Signal A', 45, 30);
        rCtx.fillText('Signal B', rw - 60, 30);

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();

// =========================================================================
// MOBILE SIMULATOR 2: CSMA/CA MAC RTS/CTS
// =========================================================================
(function initMobileMAC() {
    const canvas = document.getElementById('mobile-mac-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const statusText = document.getElementById('mobile-mac-status-text');

    let rtsEnabled = true;
    let packetProgress = 0;
    let macState = 'idle';

    function resize() {
        if (!canvas.parentElement) return;
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = 360;
    }
    window.addEventListener('resize', resize);

    window.toggleMobileRTS = () => {
        rtsEnabled = !rtsEnabled;
        const btn = document.getElementById('mobile-btn-toggle-rts');
        if (btn) btn.textContent = rtsEnabled ? 'Mode: With RTS/CTS (Collision Free)' : 'Mode: Without RTS/CTS (Collisions)';
    };

    window.triggerMobileTransmit = () => {
        packetProgress = 0;
        macState = 'transmitting';
        statusText.textContent = rtsEnabled ? 'RTS Active: NAV Quiet Zone Set' : 'Transmitting: Collision Imminent!';
        statusText.style.color = rtsEnabled ? '#38bdf8' : '#f87171';
    };

    function draw() {
        const w = canvas.width, h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        const nodeA = { x: w * 0.2, y: h * 0.5, name: 'Node A' };
        const nodeAP = { x: w * 0.5, y: h * 0.5, name: 'Access Point (AP)' };
        const nodeC = { x: w * 0.8, y: h * 0.5, name: 'Node C' };

        const rRange = w * 0.35;
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.15)';
        ctx.beginPath(); ctx.arc(nodeA.x, nodeA.y, rRange, 0, Math.PI * 2); ctx.stroke();

        ctx.strokeStyle = 'rgba(236, 72, 153, 0.15)';
        ctx.beginPath(); ctx.arc(nodeC.x, nodeC.y, rRange, 0, Math.PI * 2); ctx.stroke();

        [nodeA, nodeAP, nodeC].forEach((n, idx) => {
            ctx.fillStyle = idx === 1 ? '#fbbf24' : (idx === 0 ? '#38bdf8' : '#ec4899');
            ctx.beginPath(); ctx.arc(n.x, n.y, 14, 0, Math.PI * 2); ctx.fill();
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 11px Inter';
            ctx.textAlign = 'center';
            ctx.fillText(n.name, n.x, n.y + 26);
        });

        if (macState === 'transmitting') {
            packetProgress += 0.015;
            if (packetProgress > 1) {
                macState = 'idle';
                statusText.textContent = rtsEnabled ? 'Success! ACK Received' : 'Collision Occurred at AP!';
                statusText.style.color = rtsEnabled ? '#34d399' : '#f87171';
            }

            const curAx = nodeA.x + (nodeAP.x - nodeA.x) * packetProgress;
            ctx.fillStyle = '#38bdf8';
            ctx.beginPath(); ctx.arc(curAx, nodeA.y, 6, 0, Math.PI * 2); ctx.fill();

            if (!rtsEnabled) {
                const curCx = nodeC.x + (nodeAP.x - nodeC.x) * packetProgress;
                ctx.fillStyle = '#ec4899';
                ctx.beginPath(); ctx.arc(curCx, nodeC.y, 6, 0, Math.PI * 2); ctx.fill();
                if (packetProgress > 0.85) {
                    ctx.fillStyle = 'rgba(239, 68, 68, 0.4)';
                    ctx.beginPath(); ctx.arc(nodeAP.x, nodeAP.y, 30, 0, Math.PI * 2); ctx.fill();
                }
            } else {
                ctx.fillStyle = '#34d399';
                ctx.fillRect(nodeC.x - 30, nodeC.y - 32, 60 * (1 - packetProgress), 6);
            }
        }

        requestAnimationFrame(draw);
    }
    resize();
    draw();
})();
"""
