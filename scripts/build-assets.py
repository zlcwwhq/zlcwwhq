#!/usr/bin/env python3
"""Rebuild the original vector assets with the Python standard library.

Run: python3 scripts/build-assets.py
The separate AI-generated Springfield illustration is never modified here.
"""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)
INK, IVORY, AMBER, BLUE, MUTED = "#141e28", "#eee7db", "#cf9e62", "#90b5c8", "#a3adb5"


def text(x, y, content, size=14, color=IVORY, weight="normal", spacing=0, mono=False):
    font = "'Courier New', monospace" if mono else "Arial, Helvetica, sans-serif"
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" '
            f'font-size="{size}" font-weight="{weight}" '
            f'letter-spacing="{spacing}">{escape(content)}</text>')


def save(name, width, height, title, description, body):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
           f'<title id="title">{escape(title)}</title>\n'
           f'<desc id="desc">{escape(description)}</desc>\n{body}\n</svg>\n')
    (ASSETS / name).write_text(svg, encoding="utf-8")


save("open-repositories.svg", 240, 44, "Explore repositories", "Browse zlcwwhq's GitHub repositories.",
     f'<path d="M0 0H230L240 10V44H0Z" fill="{INK}"/>'
     f'<path d="M0 0H4V44H0Z" fill="{AMBER}"/>'
     + text(20, 27, "EXPLORE REPOSITORIES", 12, IVORY, "bold", .6, True)
     + f'<path d="M213 27l9-9m-8 0h8v8" fill="none" stroke="{AMBER}" stroke-width="1.5"/>')

for name, label, index, color in [("c", "C", "01", BLUE), ("cpp", "C++", "02", BLUE),
                                  ("go", "Go", "03", BLUE), ("rust", "Rust", "04", AMBER)]:
    save(f"lang-{name}.svg", 126, 54, label, f"Programming toolkit: {label}. No proficiency rating implied.",
         f'<path d="M0 0H117L126 9V54H0Z" fill="{INK}"/>'
         f'<path d="M.5 53.5H125.5M.5.5V53.5" fill="none" stroke="#34424e"/>'
         f'<path d="M1 1H35" stroke="{color}" stroke-width="2"/>'
         + text(13, 36, label, 23, IVORY, "bold")
         + text(101, 18, index, 10, color, mono=True))

# Original abstract mineral/landship drawing, not an official faction logo.
grid = '<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#89aabd" stroke-opacity=".07"/></pattern></defs>'
ark_body = (grid
    + f'<path d="M0 0H414L440 26V236H0Z" fill="{INK}"/>'
    + '<path d="M0 0H414L440 26V236H0Z" fill="url(#grid)"/>'
    + '<path d="M.5.5H413.8L439.5 26.2V235.5H.5Z" fill="none" stroke="#425562"/>'
    + f'<path d="M0 0H6V236H0Z" fill="{BLUE}"/>'
    + '<g fill="none" stroke="#7495a9" stroke-opacity=".36" stroke-width="1">'
      '<circle cx="355" cy="111" r="55"/><circle cx="355" cy="111" r="70" stroke-dasharray="2 7"/>'
      '<path d="M355 30V192M274 111H436M312 153L355 44L397 153ZM329 132L355 65L380 132Z"/>'
      '<path d="M319 151V168H391V151M327 168V179H383V168M338 111L355 87L372 111L355 137Z"/></g>'
    + text(24, 32, "AFFINITY / 01", 11, BLUE, spacing=1.5, mono=True)
    + text(24, 97, "ARKNIGHTS", 37, IVORY, "bold", -.8)
    + text(26, 123, "RHODES ISLAND", 12, BLUE, spacing=2.8, mono=True)
    + '<path d="M25 154H160" stroke="#405867"/>'
    + text(25, 181, "A WORLD WORTH EXPLORING.", 11, MUTED, spacing=.5, mono=True)
    + text(25, 215, "DOCTOR / ON BOARD", 10, BLUE, spacing=1, mono=True)
    + text(394, 215, "↗", 20, BLUE))
save("arknights-dossier.svg", 440, 236, "Arknights / Rhodes Island", "Personal Arknights affinity card, with original abstract landship and mineral line art.", ark_body)

gfl_body = (grid
    + '<path d="M0 0H414L440 26V236H0Z" fill="#211f20"/>'
    + '<path d="M0 0H414L440 26V236H0Z" fill="url(#grid)"/>'
    + '<path d="M.5.5H413.8L439.5 26.2V235.5H.5Z" fill="none" stroke="#5c4b3d"/>'
    + f'<path d="M0 0H6V236H0Z" fill="{AMBER}"/>'
    + '<g fill="none" stroke="#b88d60" stroke-opacity=".36" stroke-width="1.2">'
      '<circle cx="354" cy="112" r="55"/><circle cx="354" cy="112" r="70" stroke-dasharray="2 7"/>'
      '<path d="M322 100H376V123Q376 149 349 149Q322 149 322 123ZM376 105H388Q401 105 401 120Q401 136 374 136M313 155H389"/>'
      '<path d="M336 90C321 77 351 72 336 58M354 90C339 77 369 72 354 58M372 90C357 77 387 72 372 58"/></g>'
    + text(24, 32, "AFFINITY / 02", 11, AMBER, spacing=1.5, mono=True)
    + text(24, 85, "GIRLS'", 35, IVORY, "bold", -.5)
    + text(24, 121, "FRONTLINE", 35, IVORY, "bold", -.5)
    + '<path d="M25 154H160" stroke="#5c4b3d"/>'
    + text(25, 181, "SPRINGFIELD / COFFEE BREAK", 11, MUTED, spacing=.2, mono=True)
    + text(25, 215, "COMMANDER / AT EASE", 10, AMBER, spacing=1, mono=True)
    + text(394, 215, "↗", 20, AMBER))
save("gfl-dossier.svg", 440, 236, "Girls' Frontline / Springfield", "Personal Girls' Frontline affinity card. Springfield's coffee break is represented by an original line-art cup.", gfl_body)

save("terminal-footer.svg", 900, 114, "End of transmission", "Keep learning. Keep building. Stay curious.",
     f'<rect width="900" height="114" fill="{INK}"/>'
     '<path d="M0 .5H900" stroke="#3f4e5a"/>'
     f'<path d="M0 0H88V3H0Z" fill="{AMBER}"/>'
     + text(28, 35, "END OF TRANSMISSION", 11, AMBER, spacing=2, mono=True)
     + text(28, 77, "Keep learning. Keep building. Stay curious.", 23, IVORY)
     + '<g stroke="#7c95a6" stroke-opacity=".4" fill="none">'
       '<circle cx="821" cy="58" r="27"/><path d="M821 24V92M787 58H855M802 77L840 39"/></g>'
     + text(756, 106, "Z / ARCHIVE 001", 9, MUTED, spacing=1, mono=True))

print(f"Built {len(list(ASSETS.glob('*.svg')))} SVG assets in {ASSETS}")
