#!/usr/bin/env python3
"""Bouwt een print-versie van de tuinkalender: precies 2 A4-pagina's."""
import html, io, contextlib

# build.py schrijft bij import de website weg; dat onderdrukken we hier.
with contextlib.redirect_stdout(io.StringIO()):
    from build import MONTHS, PLANTS, imgs, byk

e = html.escape

# Waarschuwingen die je op het verkeerde moment de bloei of de plant kosten.
LETOP = [
    ('panicum', "Vingergras", "Nooit vóór de winter terugknippen — pas in maart."),
    ('gaura', "Prachtkaars", "Niet in maart maar in april snoeien; de oude stelen zijn de vorstbescherming."),
    ('echinacea', "Zonnehoed", "Zaadhoofden in het najaar laten staan. Winternat is gevaarlijker dan winterkou."),
    ('clematis', "Clematis", "Alleen hard terugsnoeien als hij pas vanaf juli bloeit (groep 3)."),
    ('trachelospermum', "Toscaanse jasmijn", "Niet in oktober tot op het hout snoeien — te weinig hersteltijd."),
    ('geum', "Nagelkruid", "Groenblijvend: in het najaar niet kaalknippen."),
]

IMGCSS = "".join(f'.b-{k}{{background-image:url({v})}}' for k, v in imgs.items())


def month_html(idx, name, items):
    if not items:
        rows = '<p class="leeg">Geen onderhoud</p>'
    else:
        rows = "".join(
            f'<li><span class="th {"b-"+k if k else "ph"}"></span>'
            f'<span class="tx"><b>{e(t)}</b> {e(d)}</span></li>'
            for t, d, k in items)
        rows = f'<ul>{rows}</ul>'
    n = len(items)
    cnt = f'<span class="n">{n}</span>' if n else ''
    return (f'<section class="mo{" leegmo" if not items else ""}">'
            f'<h2>{e(name)}{cnt}</h2>{rows}</section>')


def pages(split):
    a = "".join(month_html(i, n, it) for i, (n, _, it) in enumerate(MONTHS[:split]))
    b = "".join(month_html(i + split, n, it) for i, (n, _, it) in enumerate(MONTHS[split:]))
    return a, b, MONTHS[0][0].lower(), MONTHS[split-1][0].lower(), MONTHS[split][0], MONTHS[-1][0].lower()

letop = "".join(
    f'<li><span class="th b-{k}"></span><span class="tx"><b>{e(n)}</b> {e(t)}</span></li>'
    for k, n, t in LETOP)

def keylist(plants):
    return "".join(
        f'<div class="kp"><span class="th b-{p["key"]}"></span>'
        f'<span><b>{e(p["nl"])}</b><i>{e(p["latin"])}</i></span></div>'
        for p in plants)



def doc(fs=9.0, th=9.5, gap=3.8, lh=1.36, split=7, kth=18.0, ksplit=3):
    p1, p2, m1a, m1b, m2a, m2b = pages(split)
    key_a, key_b = keylist(PLANTS[:ksplit]), keylist(PLANTS[ksplit:])
    return f'''<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 11mm 11mm 9mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", sans-serif; font-size: {fs}pt; line-height: {lh};
        color: #1f241f; margin: 0; }}
h1 {{ font-size: 17pt; margin: 0 0 4.5mm; letter-spacing: -.01em; }}
.grid {{ column-count: 2; column-gap: 7mm; }}
.mo {{ break-inside: avoid; margin-bottom: {gap}mm; border: .4pt solid #cfd4ca;
       border-radius: 2mm; padding: 2.4mm 2.8mm 2.6mm; }}
.mo.leegmo {{ background: #f5f6f3; }}
.mo h2 {{ font-size: 11pt; color: #2f6b47; margin: 0 0 1.6mm;
          padding-bottom: 1.1mm; border-bottom: .4pt solid #dfe3db; }}
.mo h2 .n {{ float: right; font-size: 7.6pt; color: #8b918a; font-weight: normal;
             border: .4pt solid #dfe3db; border-radius: 3mm; padding: 0 1.6mm; }}
.mo ul {{ list-style: none; margin: 0; padding: 0; }}
.mo li, .letop li {{ display: flex; gap: 2mm; padding: 1.1mm 0; align-items: flex-start; }}
.mo li + li, .letop li + li {{ border-top: .3pt solid #eceee9; }}
.th {{ width: {th}mm; height: {th}mm; flex: none; border-radius: 1.2mm; border: .3pt solid #cfd4ca;
       background-size: cover; background-position: center; }}
.th.ph {{ background: #eceee9; }}
.tx b {{ color: #24422f; }}
.leeg {{ margin: 0; color: #8b918a; font-style: italic; }}
.letop {{ break-inside: avoid; border: .5pt solid #d9b877; background: #fdf7ea;
          border-radius: 2mm; padding: 2.4mm 2.8mm; margin-top: 1mm; }}
.letop h2 {{ font-size: 11pt; color: #8a5a1e; margin: 0 0 1.6mm; }}
.letop ul {{ list-style: none; margin: 0; padding: 0; column-count: 2; column-gap: 6mm; }}
.letop li {{ break-inside: avoid; }}
html, body {{ height: 100%; }}
.page {{ height: 100%; display: flex; flex-direction: column; }}
.keyw {{ break-inside: avoid; border-top: .4pt solid #cfd4ca; margin-top: auto;
         padding-top: 3.5mm; }}
.keys {{ display: flex; }}
.kp {{ width: 20%; padding-right: 3mm; break-inside: avoid; }}
.kp .th {{ display: block; width: 100%; height: {kth}mm; border-radius: 1.6mm;
           margin-bottom: 1.2mm; }}
.kp b {{ display: block; line-height: 1.2; }}
.kp i {{ display: block; color: #6b7268; font-size: 7.4pt; line-height: 1.2; }}
.pg {{ break-before: page; }}
.credit {{ margin: 3mm 0 0; font-size: 7pt; color: #8b918a; }}
.kp b, .kp i {{ margin: 0; }}
.page > *:last-child {{ margin-bottom: 0; }}
{IMGCSS}
</style></head><body>

<div class="page">
<h1>Tuinkalender — {m1a} t/m {m1b}</h1>
<div class="grid">{p1}</div>
<div class="keyw"><div class="keys">{key_a}</div></div>
</div>

<div class="page pg">
<h1>{m2a} t/m {m2b}</h1>
<div class="grid">{p2}</div>
<div class="letop"><h2>Let op — dit kost je de bloei of de plant</h2><ul>{letop}</ul></div>
<div class="keyw"><div class="keys">{key_b}</div>
<p class="credit">Bron: beplantingsboekje (foto&#39;s René Koot / Harry Boven) · clematisfoto via Wikimedia Commons · onderhoud aangevuld met Nederlandse tuinbronnen.</p></div>
</div>

</body></html>'''

from weasyprint import HTML

FS, TH, GAP, LH = 9.4, 9.0, 3.4, 1.34
KTH = 34.2    # hoogte plantfoto's
KSPLIT = 5    # plantenlijst gelijk over beide pagina's
SPLIT = 7     # juli hoort bij pagina 1

d = doc(FS, TH, GAP, LH, SPLIT, KTH, KSPLIT)
open('print.html', 'w').write(d)
r = HTML(string=d, base_url='.').render()
r.write_pdf('Tuinkalender-print.pdf')
print(f'{len(r.pages)} pagina\'s')
