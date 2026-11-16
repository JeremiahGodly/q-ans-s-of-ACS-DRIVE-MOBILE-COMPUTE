# -*- coding: utf-8 -*-
"""
Script to update animations.html:
1. Adds LCS (Linear Control Systems) 60fps Step Response & S-Plane Pole Migration Simulator
2. Adds Power Electronics DC-DC Buck / Boost Converter Switching Synthesizer
3. Adds URL parameter filtering (?subject=acs, drive, mobile, lcs, pe)
4. Adds tab buttons and active CSS styling
"""

import re

LCS_SIM_HTML = """
            <!-- SIMULATION 7: Linear Control Systems 2nd-Order Step Response & S-Plane Poles -->
            <article class="sim-card sim-item-lcs" style="--card-focus-color:#10b981;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">🎛️</span>
                        <div>
                            <h2 class="sim-title">Linear Control Systems: 2nd-Order Step Response &amp; S-Plane Dynamics</h2>
                        </div>
                    </div>
                    <span class="sim-badge" style="background:rgba(16,185,129,0.15); color:#34d399; border-color:rgba(16,185,129,0.3);">LCS EET302: Module 2 &amp; 3</span>
                </div>
                <div class="sim-body">
                    <div class="canvas-viewport" style="height:360px;">
                        <canvas id="canvas-lcs" width="800" height="360"></canvas>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label">Damping Ratio (ζ): <span id="val-lcs-zeta" style="color:#10b981; font-weight:700;">0.45</span></label>
                            <input type="range" id="slider-lcs-zeta" min="0" max="2.0" step="0.05" value="0.45" oninput="updateLCSSim()">
                        </div>
                        <div class="control-group">
                            <label class="control-label">Natural Frequency (ωₙ): <span id="val-lcs-wn" style="color:#10b981; font-weight:700;">4.0 rad/s</span></label>
                            <input type="range" id="slider-lcs-wn" min="1.0" max="10.0" step="0.5" value="4.0" oninput="updateLCSSim()">
                        </div>
                        <button type="button" class="action-btn" onclick="resetLCSSim()" style="border-color:#10b981;">🔄 Reset Step</button>
                    </div>

                    <div class="metrics-panel">
                        <div class="metric-box">
                            <div class="metric-label">Peak Overshoot (M_p)</div>
                            <div class="metric-val" id="metric-lcs-mp" style="color:#34d399;">20.5%</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Peak Time (t_p)</div>
                            <div class="metric-val" id="metric-lcs-tp" style="color:#38bdf8;">0.88 s</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Settling Time (t_s 2%)</div>
                            <div class="metric-val" id="metric-lcs-ts" style="color:#f59e0b;">2.22 s</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Poles (s₁,₂)</div>
                            <div class="metric-val" id="metric-lcs-poles" style="color:#ec4899; font-size:0.85rem;">-1.80 ± j3.57</div>
                        </div>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#10b981;">
                        <strong>KTU Exam Core Concept:</strong> The closed-loop transfer function is 
                        <code>T(s) = ωₙ² / (s² + 2ζωₙs + ωₙ²)</code>.
                        When <code>0 &lt; ζ &lt; 1</code>, the response is <em>underdamped</em> with complex conjugate poles producing overshoot.
                        When <code>ζ = 1</code>, the response is <em>critically damped</em> with coincident real poles.
                        When <code>ζ &gt; 1</code>, it is <em>overdamped</em> and sluggish. The canvas also plots the dynamic S-plane pole migration in the top-right radar inset.
                    </div>
                </div>
            </article>
"""

PE_SIM_HTML = """
            <!-- SIMULATION 8: Power Electronics DC-DC Buck / Boost Switching Converter -->
            <article class="sim-card sim-item-pe" style="--card-focus-color:#8b5cf6;">
                <div class="sim-header">
                    <div class="sim-title-group">
                        <span class="sim-icon">🔋</span>
                        <div>
                            <h2 class="sim-title">Power Electronics: DC-DC Buck / Boost Converter Switching Synthesizer</h2>
                        </div>
                    </div>
                    <span class="sim-badge" style="background:rgba(139,92,246,0.15); color:#a78bfa; border-color:rgba(139,92,246,0.3);">PE EET306: Module 3: Choppers</span>
                </div>
                <div class="sim-body">
                    <div class="canvas-viewport" style="height:360px;">
                        <canvas id="canvas-pe" width="800" height="360"></canvas>
                    </div>

                    <div class="sim-controls-panel">
                        <div class="control-group">
                            <label class="control-label">Topology Mode:</label>
                            <select id="pe-mode-select" class="action-btn" style="background:var(--bg-card);" onchange="updatePESim()">
                                <option value="buck">Buck Converter (Step-Down: Vₒ = D·Vᵢₙ)</option>
                                <option value="boost">Boost Converter (Step-Up: Vₒ = Vᵢₙ / (1-D))</option>
                            </select>
                        </div>
                        <div class="control-group">
                            <label class="control-label">Duty Ratio (D): <span id="val-pe-duty" style="color:#a78bfa; font-weight:700;">0.50</span></label>
                            <input type="range" id="slider-pe-duty" min="0.10" max="0.85" step="0.02" value="0.50" oninput="updatePESim()">
                        </div>
                        <div class="control-group">
                            <label class="control-label">Switching Freq (f_s): <span id="val-pe-fs" style="color:#a78bfa; font-weight:700;">25 kHz</span></label>
                            <input type="range" id="slider-pe-fs" min="10" max="80" step="5" value="25" oninput="updatePESim()">
                        </div>
                    </div>

                    <div class="metrics-panel">
                        <div class="metric-box">
                            <div class="metric-label">Input Voltage (V_in)</div>
                            <div class="metric-val" style="color:#38bdf8;">24.0 V</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Output Voltage (V_o)</div>
                            <div class="metric-val" id="metric-pe-vo" style="color:#34d399;">12.0 V</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Ripple Current (ΔI_L)</div>
                            <div class="metric-val" id="metric-pe-ripple" style="color:#f59e0b;">1.20 A</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-label">Conduction Regime</div>
                            <div class="metric-val" id="metric-pe-regime" style="color:#a78bfa; font-weight:700;">CCM Mode</div>
                        </div>
                    </div>

                    <div class="explanation-drawer" style="border-left-color:#8b5cf6;">
                        <strong>KTU Exam Core Concept:</strong> Operates by the <strong>Volt-Second Balance Principle</strong> across the inductor: 
                        <code>⟨v_L⟩ = 0</code> in steady state. 
                        Top waveform tracks gate switching pulses <code>V_GS(t)</code>. Bottom waveform tracks inductor triangular ripple current <code>i_L(t)</code> ramping up when the semiconductor switch is ON and discharging into the load when OFF.
                    </div>
                </div>
            </article>
"""

LCS_PE_SCRIPTS = """
        // ======================================================================
        // SIMULATION 7: LCS 2nd-Order Step Response & S-Plane Pole Migration
        // ======================================================================
        const lcsCanvas = document.getElementById('canvas-lcs');
        const lcsCtx = lcsCanvas.getContext('2d');
        let lcsZeta = 0.45;
        let lcsWn = 4.0;
        let lcsTimeOffset = 0;

        function updateLCSSim() {
            lcsZeta = parseFloat(document.getElementById('slider-lcs-zeta').value);
            lcsWn = parseFloat(document.getElementById('slider-lcs-wn').value);
            document.getElementById('val-lcs-zeta').innerText = lcsZeta.toFixed(2);
            document.getElementById('val-lcs-wn').innerText = lcsWn.toFixed(1) + ' rad/s';

            // Calculate metrics
            let mpText = '0.0% (No Overshoot)';
            let tpText = 'N/A';
            let wd = lcsWn * Math.sqrt(Math.max(0, 1 - lcsZeta * lcsZeta));
            let ts = (4 / (Math.max(0.01, lcsZeta * lcsWn))).toFixed(2) + ' s';
            let polesText = '';

            if (lcsZeta < 1.0) {
                let mp = Math.exp(-Math.PI * lcsZeta / Math.sqrt(1 - lcsZeta * lcsZeta)) * 100;
                mpText = mp.toFixed(1) + '%';
                let tp = (Math.PI / wd).toFixed(2) + ' s';
                tpText = tp;
                polesText = `-${(lcsZeta * lcsWn).toFixed(2)} ± j${wd.toFixed(2)}`;
            } else if (lcsZeta === 1.0) {
                polesText = `-${(lcsWn).toFixed(2)} (Coincident)`;
            } else {
                let s1 = -lcsZeta * lcsWn + lcsWn * Math.sqrt(lcsZeta * lcsZeta - 1);
                let s2 = -lcsZeta * lcsWn - lcsWn * Math.sqrt(lcsZeta * lcsZeta - 1);
                polesText = `${s1.toFixed(2)}, ${s2.toFixed(2)}`;
            }

            document.getElementById('metric-lcs-mp').innerText = mpText;
            document.getElementById('metric-lcs-tp').innerText = tpText;
            document.getElementById('metric-lcs-ts').innerText = ts;
            document.getElementById('metric-lcs-poles').innerText = polesText;
        }

        function resetLCSSim() {
            lcsTimeOffset = 0;
        }

        function stepResponse(t, zeta, wn) {
            if (t <= 0) return 0;
            if (zeta < 1.0) {
                let wd = wn * Math.sqrt(1 - zeta * zeta);
                let phi = Math.atan2(Math.sqrt(1 - zeta * zeta), zeta);
                return 1 - (Math.exp(-zeta * wn * t) / Math.sqrt(1 - zeta * zeta)) * Math.sin(wd * t + phi);
            } else if (zeta === 1.0) {
                return 1 - (1 + wn * t) * Math.exp(-wn * t);
            } else {
                let s1 = -zeta * wn + wn * Math.sqrt(zeta * zeta - 1);
                let s2 = -zeta * wn - wn * Math.sqrt(zeta * zeta - 1);
                return 1 + (s2 * Math.exp(s1 * t) - s1 * Math.exp(s2 * t)) / (s1 - s2);
            }
        }

        function drawLCS() {
            if (!lcsCanvas) return;
            lcsCtx.fillStyle = '#090d16';
            lcsCtx.fillRect(0, 0, lcsCanvas.width, lcsCanvas.height);

            const W = lcsCanvas.width;
            const H = lcsCanvas.height;
            const plotW = W - 220; // reserve right 200px for S-plane inset
            const originY = H - 50;
            const originX = 50;
            const scaleY = 160;
            const maxTime = 3.5;

            // Grid lines
            lcsCtx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
            lcsCtx.lineWidth = 1;
            for (let t = 0.5; t <= maxTime; t += 0.5) {
                let gx = originX + (t / maxTime) * (plotW - originX);
                lcsCtx.beginPath();
                lcsCtx.moveTo(gx, 30);
                lcsCtx.lineTo(gx, originY);
                lcsCtx.stroke();
                lcsCtx.fillStyle = '#64748b';
                lcsCtx.font = '10px monospace';
                lcsCtx.fillText(t.toFixed(1) + 's', gx - 10, originY + 16);
            }

            // Reference line y = 1.0
            const refY = originY - scaleY;
            lcsCtx.strokeStyle = 'rgba(56, 189, 248, 0.5)';
            lcsCtx.setLineDash([4, 4]);
            lcsCtx.beginPath();
            lcsCtx.moveTo(originX, refY);
            lcsCtx.lineTo(plotW, refY);
            lcsCtx.stroke();
            lcsCtx.setLineDash([]);
            lcsCtx.fillStyle = '#38bdf8';
            lcsCtx.font = '11px sans-serif';
            lcsCtx.fillText('Step Input r(t) = 1.0', originX + 5, refY - 6);

            // ±2% settling band
            lcsCtx.fillStyle = 'rgba(16, 185, 129, 0.06)';
            lcsCtx.fillRect(originX, refY - scaleY * 0.02, plotW - originX, scaleY * 0.04);

            // Time response curve
            lcsCtx.strokeStyle = '#10b981';
            lcsCtx.lineWidth = 3;
            lcsCtx.beginPath();
            for (let px = 0; px <= plotW - originX; px += 2) {
                let t = (px / (plotW - originX)) * maxTime;
                let cVal = stepResponse(t, lcsZeta, lcsWn);
                let cy = originY - cVal * scaleY;
                if (px === 0) lcsCtx.moveTo(originX + px, cy);
                else lcsCtx.lineTo(originX + px, cy);
            }
            lcsCtx.stroke();

            // Animated live tracer dot
            lcsTimeOffset += 0.015;
            let tracerT = lcsTimeOffset % maxTime;
            let tracerC = stepResponse(tracerT, lcsZeta, lcsWn);
            let tracerX = originX + (tracerT / maxTime) * (plotW - originX);
            let tracerY = originY - tracerC * scaleY;

            lcsCtx.fillStyle = '#34d399';
            lcsCtx.shadowColor = '#10b981';
            lcsCtx.shadowBlur = 12;
            lcsCtx.beginPath();
            lcsCtx.arc(tracerX, tracerY, 6, 0, Math.PI * 2);
            lcsCtx.fill();
            lcsCtx.shadowBlur = 0;

            // S-PLANE INSET (Right side)
            const insetX = plotW + 20;
            const insetY = 30;
            const insetW = 180;
            const insetH = H - 60;
            lcsCtx.fillStyle = '#0f172a';
            lcsCtx.fillRect(insetX, insetY, insetW, insetH);
            lcsCtx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
            lcsCtx.strokeRect(insetX, insetY, insetW, insetH);

            const spCenterX = insetX + insetW * 0.75;
            const spCenterY = insetY + insetH / 2;

            // S-Plane Axes
            lcsCtx.strokeStyle = '#475569';
            lcsCtx.lineWidth = 1;
            lcsCtx.beginPath();
            lcsCtx.moveTo(insetX, spCenterY);
            lcsCtx.lineTo(insetX + insetW, spCenterY);
            lcsCtx.moveTo(spCenterX, insetY);
            lcsCtx.lineTo(spCenterX, insetY + insetH);
            lcsCtx.stroke();

            lcsCtx.fillStyle = '#94a3b8';
            lcsCtx.font = '10px sans-serif';
            lcsCtx.fillText('σ (Real)', insetX + 10, spCenterY - 6);
            lcsCtx.fillText('+jω', spCenterX + 5, insetY + 14);
            lcsCtx.fillText('Complex S-Plane', insetX + 45, insetY + insetH - 8);

            // Draw Poles
            const sScale = 12;
            lcsCtx.fillStyle = '#ec4899';
            lcsCtx.font = 'bold 15px sans-serif';
            if (lcsZeta < 1.0) {
                let sigma = -lcsZeta * lcsWn;
                let wd = lcsWn * Math.sqrt(1 - lcsZeta * lcsZeta);
                let p1x = spCenterX + sigma * sScale;
                let p1y = spCenterY - wd * sScale;
                let p2y = spCenterY + wd * sScale;
                lcsCtx.fillText('×', p1x - 5, p1y + 5);
                lcsCtx.fillText('×', p1x - 5, p2y + 5);
            } else if (lcsZeta === 1.0) {
                let p1x = spCenterX - lcsWn * sScale;
                lcsCtx.fillText('××', p1x - 8, spCenterY + 5);
            } else {
                let s1 = -lcsZeta * lcsWn + lcsWn * Math.sqrt(lcsZeta * lcsZeta - 1);
                let s2 = -lcsZeta * lcsWn - lcsWn * Math.sqrt(lcsZeta * lcsZeta - 1);
                lcsCtx.fillText('×', spCenterX + s1 * sScale - 5, spCenterY + 5);
                lcsCtx.fillText('×', spCenterX + s2 * sScale - 5, spCenterY + 5);
            }

            requestAnimationFrame(drawLCS);
        }

        // ======================================================================
        // SIMULATION 8: Power Electronics DC-DC Buck / Boost Converter
        // ======================================================================
        const peCanvas = document.getElementById('canvas-pe');
        const peCtx = peCanvas.getContext('2d');
        let peMode = 'buck';
        let peDuty = 0.50;
        let peFs = 25;
        let peScrollOffset = 0;

        function updatePESim() {
            peMode = document.getElementById('pe-mode-select').value;
            peDuty = parseFloat(document.getElementById('slider-pe-duty').value);
            peFs = parseInt(document.getElementById('slider-pe-fs').value);

            document.getElementById('val-pe-duty').innerText = peDuty.toFixed(2);
            document.getElementById('val-pe-fs').innerText = peFs + ' kHz';

            const Vin = 24.0;
            let Vo = peMode === 'buck' ? Vin * peDuty : Vin / (1 - peDuty);
            let ripple = (peMode === 'buck' ? (Vin - Vo) * peDuty / (peFs * 1000 * 200e-6) : (Vin * peDuty) / (peFs * 1000 * 200e-6));

            document.getElementById('metric-pe-vo').innerText = Vo.toFixed(1) + ' V';
            document.getElementById('metric-pe-ripple').innerText = ripple.toFixed(2) + ' A';
            document.getElementById('metric-pe-regime').innerText = ripple < 4.0 ? 'CCM Mode (Continuous)' : 'DCM Threshold';
        }

        function drawPE() {
            if (!peCanvas) return;
            peCtx.fillStyle = '#080c14';
            peCtx.fillRect(0, 0, peCanvas.width, peCanvas.height);

            const W = peCanvas.width;
            const H = peCanvas.height;
            peScrollOffset += 1.5;

            // Channel 1: Gate Pulses V_GS(t) (Top Half)
            peCtx.fillStyle = '#0f172a';
            peCtx.fillRect(20, 20, W - 40, 130);
            peCtx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            peCtx.strokeRect(20, 20, W - 40, 130);

            peCtx.fillStyle = '#c084fc';
            peCtx.font = '11px sans-serif';
            peCtx.fillText('Gate Voltage V_GS(t) [Switch State: High = ON, Low = OFF]', 35, 42);

            peCtx.strokeStyle = '#a855f7';
            peCtx.lineWidth = 2.5;
            peCtx.beginPath();
            const periodPx = 100;
            for (let x = 25; x < W - 25; x += 1) {
                let relX = (x + peScrollOffset) % periodPx;
                let isHigh = relX < (peDuty * periodPx);
                let y = isHigh ? 55 : 125;
                if (x === 25) peCtx.moveTo(x, y);
                else peCtx.lineTo(x, y);
            }
            peCtx.stroke();

            // Channel 2: Inductor Current i_L(t) (Bottom Half)
            peCtx.fillStyle = '#0f172a';
            peCtx.fillRect(20, 180, W - 40, 150);
            peCtx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            peCtx.strokeRect(20, 180, W - 40, 150);

            peCtx.fillStyle = '#fbbf24';
            peCtx.font = '11px sans-serif';
            peCtx.fillText(`Inductor Triangular Ripple Current i_L(t) [${peMode.toUpperCase()} Conduction]`, 35, 202);

            peCtx.strokeStyle = '#fbbf24';
            peCtx.lineWidth = 3;
            peCtx.beginPath();
            const baseIL = 280;
            const rampHeight = 65;
            for (let x = 25; x < W - 25; x += 1) {
                let relX = (x + peScrollOffset) % periodPx;
                let y;
                if (relX < (peDuty * periodPx)) {
                    // Charging slope: increases linearly
                    y = baseIL - (relX / (peDuty * periodPx)) * rampHeight;
                } else {
                    // Discharging slope: decreases linearly
                    let offProgress = (relX - peDuty * periodPx) / ((1 - peDuty) * periodPx);
                    y = (baseIL - rampHeight) + offProgress * rampHeight;
                }
                if (x === 25) peCtx.moveTo(x, y);
                else peCtx.lineTo(x, y);
            }
            peCtx.stroke();

            requestAnimationFrame(drawPE);
        }

        // URL Query Parameter Listener for pre-filtering simulators
        window.addEventListener('DOMContentLoaded', () => {
            const params = new URLSearchParams(window.location.search);
            const sub = params.get('subject');
            if (sub) {
                filterSimSubject(sub);
            }
            updateLCSSim();
            updatePESim();
            drawLCS();
            drawPE();
        });
"""

def update_animations():
    with open('animations.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    css_old = '''.sub-filter-tab[data-subject="mobile"].active {
            background: #db2777;
            box-shadow: 0 0 14px rgba(219, 39, 119, 0.4);
        }'''
    css_new = '''.sub-filter-tab[data-subject="mobile"].active {
            background: #db2777;
            box-shadow: 0 0 14px rgba(219, 39, 119, 0.4);
        }
        .sub-filter-tab[data-subject="lcs"].active {
            background: #10b981;
            box-shadow: 0 0 14px rgba(16, 185, 129, 0.4);
        }
        .sub-filter-tab[data-subject="pe"].active {
            background: #8b5cf6;
            box-shadow: 0 0 14px rgba(139, 92, 246, 0.4);
        }'''
    if css_old in content and '.sub-filter-tab[data-subject="lcs"].active' not in content:
        content = content.replace(css_old, css_new, 1)

    # 2. Update Tab Buttons
    tabs_old = '''<button class="sub-filter-tab active" data-subject="all" onclick="filterSimSubject('all')">🌟 All Simulators (6 Lab Stations)</button>
                <button class="sub-filter-tab" data-subject="acs" onclick="filterSimSubject('acs')">⚡ ACS Simulators</button>
                <button class="sub-filter-tab" data-subject="drive" onclick="filterSimSubject('drive')">🏎️ Electric Drives Simulators</button>
                <button class="sub-filter-tab" data-subject="mobile" onclick="filterSimSubject('mobile')">📡 Mobile Computing Simulators</button>'''

    tabs_new = '''<button class="sub-filter-tab active" data-subject="all" onclick="filterSimSubject('all')">🌟 All Simulators (8 Lab Stations)</button>
                <button class="sub-filter-tab" data-subject="acs" onclick="filterSimSubject('acs')">⚡ ACS Simulators</button>
                <button class="sub-filter-tab" data-subject="drive" onclick="filterSimSubject('drive')">🏎️ Electric Drives Simulators</button>
                <button class="sub-filter-tab" data-subject="mobile" onclick="filterSimSubject('mobile')">📡 Mobile Computing Simulators</button>
                <button class="sub-filter-tab" data-subject="lcs" onclick="filterSimSubject('lcs')">🎛️ LCS Simulators</button>
                <button class="sub-filter-tab" data-subject="pe" onclick="filterSimSubject('pe')">🔋 Power Electronics Simulators</button>'''

    if tabs_old in content:
        content = content.replace(tabs_old, tabs_new, 1)

    # 3. Add Simulations 7 and 8 before </main>
    sim6_end = content.find('<!-- SIMULATION 6: Mobile Computing CSMA/CA')
    if sim6_end != -1:
        article_end = content.find('</article>', sim6_end)
        if article_end != -1 and 'sim-item-lcs' not in content:
            insert_pos = article_end + len('</article>')
            content = content[:insert_pos] + '\n' + LCS_SIM_HTML + '\n' + PE_SIM_HTML + content[insert_pos:]

    # 4. Add scripts before </script>
    if 'drawLCS()' not in content:
        last_script_end = content.rfind('</script>')
        if last_script_end != -1:
            content = content[:last_script_end] + '\n' + LCS_PE_SCRIPTS + '\n' + content[last_script_end:]

    with open('animations.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Updated animations.html with 8 60fps simulators and URL parameter filtering successfully!')

if __name__ == '__main__':
    update_animations()
