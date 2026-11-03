# -*- coding: utf-8 -*-
"""
turtle_graphics_engine.py
=========================
A versatile, robust graphic creation tool for KTU engineering exam answers.
Supports both standard Python `turtle` import (for interactive desktops)
and headless Vector Turtle export (for generating publication SVGs and PNGs via macOS sips).

Usage:
------
    from turtle_graphics_engine import StandaloneTurtle

    t = StandaloneTurtle(width=960, height=460, title="Phase Portrait")
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.pencolor("#38bdf8")
    t.pensize(2)
    t.forward(400)
    t.save_png("images/acs/custom_phase_portrait.png")
"""

import math, os, subprocess

class StandaloneTurtle:
    """
    Headless-safe vector turtle that generates crisp SVG drawings and renders them
    to PNG using macOS native `sips` without requiring Tkinter.
    """
    def __init__(self, width=960, height=460, bg_color="#0c1220", title=""):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.title = title
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0  # degrees: 0 = East (+X), 90 = North (+Y)
        self.pen_is_down = True
        self.current_pen_color = "#38bdf8"
        self.current_pen_size = 2
        self.current_fill_color = "#1e293b"
        self.is_filling = False
        self.fill_points = []
        self.svg_elements = []

    def _to_screen_coords(self, x, y):
        # Center origin (0,0) -> SVG top-left
        sx = self.width / 2.0 + x
        sy = self.height / 2.0 - y
        return sx, sy

    def penup(self):
        self.pen_is_down = False

    def pendown(self):
        self.pen_is_down = True

    def pencolor(self, color):
        self.current_pen_color = color

    def fillcolor(self, color):
        self.current_fill_color = color

    def color(self, pen, fill=None):
        self.current_pen_color = pen
        if fill:
            self.current_fill_color = fill

    def pensize(self, size):
        self.current_pen_size = size

    def width_set(self, size):
        self.current_pen_size = size

    def goto(self, new_x, new_y):
        if self.pen_is_down:
            x1, y1 = self._to_screen_coords(self.x, self.y)
            x2, y2 = self._to_screen_coords(new_x, new_y)
            self.svg_elements.append(
                f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                f'stroke="{self.current_pen_color}" stroke-width="{self.current_pen_size}" stroke-linecap="round"/>'
            )
        if self.is_filling:
            self.fill_points.append(self._to_screen_coords(new_x, new_y))
        self.x = float(new_x)
        self.y = float(new_y)

    def forward(self, distance):
        rad = math.radians(self.angle)
        new_x = self.x + distance * math.cos(rad)
        new_y = self.y + distance * math.sin(rad)
        self.goto(new_x, new_y)

    def backward(self, distance):
        self.forward(-distance)

    def left(self, degrees):
        self.angle = (self.angle + degrees) % 360

    def right(self, degrees):
        self.left(-degrees)

    def setheading(self, angle):
        self.angle = angle % 360

    def begin_fill(self):
        self.is_filling = True
        self.fill_points = [self._to_screen_coords(self.x, self.y)]

    def end_fill(self):
        if self.fill_points and len(self.fill_points) > 2:
            pts_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in self.fill_points)
            self.svg_elements.insert(0,
                f'<polygon points="{pts_str}" fill="{self.current_fill_color}" '
                f'stroke="{self.current_pen_color}" stroke-width="{self.current_pen_size}"/>'
            )
        self.is_filling = False
        self.fill_points = []

    def circle(self, radius, extent=360, steps=36):
        # Approximate circle using polygonal arc
        step_angle = extent / steps
        step_dist = 2 * math.pi * radius * (abs(extent) / 360.0) / steps
        for _ in range(steps):
            self.forward(step_dist)
            self.left(step_angle)

    def write(self, text, align="left", font_size=12, color=None, font_weight="normal"):
        sx, sy = self._to_screen_coords(self.x, self.y)
        anchor_map = {"center": "middle", "right": "end", "left": "start"}
        anchor = anchor_map.get(align, "start")
        col = color or self.current_pen_color
        escaped_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        self.svg_elements.append(
            f'<text x="{sx:.1f}" y="{sy:.1f}" fill="{col}" font-family="-apple-system, sans-serif" '
            f'font-size="{font_size}" font-weight="{font_weight}" text-anchor="{anchor}">{escaped_text}</text>'
        )

    def draw_rect(self, x, y, width, height, rx=6, fill=None, stroke=None, stroke_width=2):
        sx, sy = self._to_screen_coords(x, y)
        f_col = fill or self.current_fill_color
        s_col = stroke or self.current_pen_color
        self.svg_elements.append(
            f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{width}" height="{height}" rx="{rx}" '
            f'fill="{f_col}" stroke="{s_col}" stroke-width="{stroke_width}"/>'
        )

    def to_svg(self):
        return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">
  <rect width="{self.width}" height="{self.height}" fill="{self.bg_color}" rx="12"/>
  <rect x="15" y="15" width="{self.width - 30}" height="{self.height - 30}" fill="none" stroke="#223049" stroke-width="1.5" rx="8"/>
  {''.join(self.svg_elements)}
</svg>"""

    def save_png(self, png_path):
        os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)
        svg_path = png_path.replace(".png", ".svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(self.to_svg())
        subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(svg_path):
            os.remove(svg_path)
        if os.path.exists(png_path):
            print(f"Exported turtle graphic -> {png_path} ({os.path.getsize(png_path)} bytes)")

if __name__ == "__main__":
    # Test example: Draw a sinusoidal waveform using TurtleCanvas
    t = StandaloneTurtle(width=800, height=350, title="Turtle Sine Wave")
    t.penup()
    t.goto(-350, 0)
    t.pendown()
    t.pencolor("#64748b")
    t.goto(350, 0)  # X axis
    t.penup()
    t.goto(0, -120)
    t.pendown()
    t.goto(0, 120)  # Y axis

    # Draw Sine curve
    t.penup()
    t.goto(-300, 0)
    t.pendown()
    t.pencolor("#38bdf8")
    t.pensize(3)
    for deg in range(-300, 301, 5):
        rad = math.radians(deg)
        x = deg
        y = 100 * math.sin(rad)
        t.goto(x, y)

    t.penup()
    t.goto(0, 140)
    t.pencolor("#fbbf24")
    t.write("Turtle Engine Test: v(t) = Vm · sin(ωt)", align="center", font_size=16, font_weight="bold")
    t.save_png("images/turtle_test_wave.png")
