# Tuinkalender

Onderhoudskalender voor de planten in de tuin, afgeleid van `Beplantings boekje.pdf`
(een uitdraai per plant, alfabetisch op botanische naam) en aangevuld met informatie
van Nederlandse tuinbronnen.

Twee deliverables uit dezelfde data:

- **`tuinkalender.html`** — website/artifact: maandkalender + doorklikbare plantengids.
- **`Tuinkalender-print.pdf`** — precies 2 A4'tjes om op te hangen.

## Bouwen

```bash
python3 build.py         # -> tuinkalender.html
python3 build_print.py   # -> print.html + Tuinkalender-print.pdf
```

`build_print.py` importeert `build.py`, dus een rebuild van de print-versie
regenereert ook de website. Vereist `weasyprint` en `pillow`.

## Bestanden

| Bestand | Rol |
|---|---|
| `build.py` | Bron van waarheid: `PLANTS` en `MONTHS`, plus de HTML/CSS/JS van de website |
| `build_print.py` | Print-layout; leest `PLANTS`/`MONTHS` uit `build.py` |
| `imgs.json` | Plantfoto's als base64 data-URI's, gekoppeld op plant-key |
| `imgs/*.jpg` | Dezelfde foto's als losse bestanden (bron voor `imgs.json`) |

## Datamodel

`PLANTS` is de plantengids, `MONTHS` de kalender. Ze zijn gekoppeld via de
**plant-key** (`actaea`, `brunnera`, `clematis`, …). Diezelfde key is de sleutel in
`imgs.json` en wordt een CSS-klasse (`.bg-<key>` in de website, `.b-<key>` in print)
die de foto als `background-image` zet.

```python
MONTHS = [(maandnaam, tag, [(kop, actietekst, plant_key_of_None), ...]), ...]
```

Een item met `None` als key is niet plant-specifiek (bijv. "Alle planten") en krijgt
geen foto en geen doorklik.

## Inhoudelijke afspraken

Deze zijn expliciet zo gevraagd — niet "verbeteren" zonder overleg:

- **Alleen onderhoudsacties in de kalender.** Geen bloeimomenten, geen "niets doen"-
  instructies, geen klusjes die niet over een specifieke plant gaan.
- Waarschuwingen die om een beslissing vragen (vingergras niet in het najaar knippen,
  prachtkaars pas in april) horen in het `let`-veld van de plant en in het
  `LETOP`-blok van de print-versie — niet als agenda-item.
- Bloeitijd blijft wél staan als *kenmerk* op de plantkaart.

## Print-layout

Vaste parameters bovenaan het uitvoergedeelte van `build_print.py`:

```python
FS, TH, GAP, LH = 9.4, 9.0, 3.4, 1.34   # tekstgrootte, thumbnail-mm, marge, regelhoogte
KTH    = 34.2   # hoogte plantfoto's in de strook onderaan
KSPLIT = 5      # aantal planten in de strook op pagina 1
SPLIT  = 7      # maart t/m juli op pagina 1; augustus t/m december op pagina 2
```

Er zat eerder een zoekloop in die automatisch de grootste zetting koos die nog op
2 pagina's paste. Die is er bewust uitgehaald: te traag voor een snelle
wijzigingsloop. Bij een wijziging die niet meer past meldt `build_print.py` gewoon
3 pagina's — dan handmatig `FS` of `KTH` omlaag.

Maart is met 9 taken het zwaarste blok en bepaalt in de praktijk de maximale
tekstgrootte.

## Openstaande punten

- De clematis stond niet in het beplantingsboekje. Aangenomen: **Clematis viticella**,
  snoeigroep 3. De plantkaart bevat een controleblok voor het geval het toch groep 2 is.
- De foto van de clematis is 'Étoile Violette' via Wikimedia Commons, niet de eigen
  plant. Fotograaf/licentie nog niet ingevuld.
- De plant op pagina 6 van het boekje stond zonder naam; geïdentificeerd als
  **Liriope muscari** op basis van foto en alfabetische positie. Staat gemarkeerd
  als "waarschijnlijk".
