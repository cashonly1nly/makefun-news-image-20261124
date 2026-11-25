#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261124.
One 1024x1024 infographic summarising world news of Tue 24 Nov 2026.
News verified 25 Nov 2026 (CST) against: Daily Summary of World,
Al Jazeera, Reuters, CNBC, Arab News, AP, ANI/Tribune India, The National.
Run: python3 build_image.py  -> writes entry.png (1024x1024, <1 MiB).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 241, 231)      # cream paper
INK = (16, 35, 63)        # navy
RED = (178, 34, 34)
GREY = (74, 74, 74)
CARD = (255, 255, 255)
NAVY = (16, 35, 63)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

STORIES = [
    ("TECH & TRADE", (200, 80, 20),
     "US jury convicts Huawei of trade-secret theft",
     "Guilty on 10 of 12 counts, incl. bank fraud and sanctions "
     "breaches; acquitted of racketeering. Huawei will appeal."),
    ("MIDDLE EAST", (178, 34, 34),
     "Riyadh tower hit again; 11 injured",
     "A Houthi drone hits the PIF tower, the Saudi capital's "
     "tallest, for the second time in under a week."),
    ("GULF", (31, 111, 183),
     "Iran says four tankers hit mines in Hormuz",
     "Tehran says four oil tankers caught fire after striking "
     "naval mines in the Strait of Hormuz. Unverified."),
    ("EUROPE", (90, 60, 140),
     "Ukraine confirms sea-drone hits on Russian ships",
     "Kyiv says its drones sank the corvette Merkury off Libya "
     "and hit Sparta II in the Gulf of Finland."),
    ("AMERICAS", (0, 128, 96),
     "Gunmen hold 25 hostage in Cartagena supermarket",
     "A botched armoured-car robbery ends in a siege at an "
     "Exito store; five elderly women are released."),
    ("GAZA", (176, 120, 20),
     "Israel kills Hamas internal security chief",
     "An airstrike in Gaza City kills Naeem Abu Nahal; six "
     "others die in separate strikes despite the ceasefire."),
]

FOOTER = ("Turkish helicopter crash kills 5 crew  \u2022  Senegal "
          "regains Africa Cup title on CAS appeal  \u2022  Nvidia "
          "shares cool after Monday's 31% surge")

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- masthead ---
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((36, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
d.text((36, 92), "TUESDAY  \u00b7  24 NOVEMBER 2026", font=font(BOLD, 30), fill=(232, 197, 120))
d.rectangle([0, 148, W, 154], fill=RED)
d.text((36, 168), "Six stories that defined the day \u2014 verdicts, strikes, sieges and ships",
       font=font(REG, 22), fill=GREY)

# --- story grid: 2 cols x 3 rows ---
x0, y0 = 28, 212
cw, ch, gx, gy = 474, 208, 20, 16
for i, (tag, colour, head, body) in enumerate(STORIES):
    x = x0 + (i % 2) * (cw + gx)
    y = y0 + (i // 2) * (ch + gy)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=CARD,
                        outline=(210, 200, 180), width=1)
    d.rectangle([x, y + 10, x + 9, y + ch - 10], fill=colour)
    d.text((x + 26, y + 16), tag, font=font(BOLD, 18), fill=colour)
    hl = wrap(d, head, font(BOLD, 27), cw - 52)
    yy = y + 46
    for ln in hl[:2]:
        d.text((x + 26, yy), ln, font=font(BOLD, 27), fill=INK)
        yy += 33
    bl = wrap(d, body, font(REG, 20), cw - 52)
    for ln in bl[:3]:
        d.text((x + 26, yy), ln, font=font(REG, 20), fill=(40, 40, 40))
        yy += 27

# --- footer ---
fy = y0 + 3 * ch + 2 * gy + 18  # 886
d.rectangle([0, fy, W, fy + 96], fill=NAVY)
d.text((36, fy + 12), "ALSO ON 24 NOVEMBER", font=font(BOLD, 19), fill=(232, 197, 120))
fl = wrap(d, FOOTER, font(REG, 19), W - 72)
yy = fy + 40
for ln in fl[:2]:
    d.text((36, yy), ln, font=font(REG, 19), fill=(255, 255, 255))
    yy += 25
d.text((36, H - 26), "Sources: Daily Summary of World, Al Jazeera, Reuters, "
       "CNBC, Arab News, AP, ANI \u2014 24 Nov 2026",
       font=font(REG, 13), fill=(120, 110, 95))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
