#!/usr/bin/env python3
import json, html, base64

imgs = json.load(open('imgs.json'))


PLANTS = [
 dict(key='actaea', latin="Actaea simplex 'Atropurpurea'", nl="Zilverkaars", type="Vaste plant",
   bloei="augustus – oktober", kleur="wit, in knop roze getint", hoogte="blad 70 cm, bloem 150 cm",
   licht="halfschaduw – geen hete middagzon", grond="humusrijk, vochtig houden",
   hard="zeer goed (−29 °C, zone 5)",
   herken="Grote, diep ingesneden roodbruine bladeren; in het najaar hoge, slanke witte bloemaren.",
   taken=[("Maart","Oud, afgestorven loof afknippen vlak vóór het uitlopen."),
          ("Maart","Laagje compost of bladaarde rondom de plant."),
          ("Juni – augustus","Water geven bij droogte — dit is de plant die als eerste slap gaat.")],
   let="Gevoelig voor droogte en felle middagzon: blad verbrandt aan de randen. Sterft elke winter bovengronds af — dat is normaal."),

 dict(key='brunnera', latin="Brunnera macrophylla 'Jack Frost'", nl="Kaukasische vergeet-mij-niet", type="Vaste plant",
   bloei="april – mei", kleur="blauw", hoogte="30–40 cm",
   licht="halfschaduw of schaduw, geen hete middagzon", grond="elke goede tuingrond, niet uitdrogend",
   hard="uitstekend (−40 °C, zone 3)",
   herken="Hartvormig blad dat zilvergrijs is met groene nerven en een smalle groene rand. Kleine blauwe bloempjes in het voorjaar.",
   taken=[("Maart","Oud loof afknippen vlak vóór het uitlopen, tot ± 5 cm boven de grond."),
          ("Juni","Uitgebloeide bloemstelen helemaal wegknippen. Soms volgt een lichte nabloei."),
          ("Juni – augustus","Bij droogte water geven; verdraagt droogte slecht.")],
   let="Verdraagt volle zon slecht — blad verschroeit. Niet te nat zetten (wortelrot)."),

 dict(key='clematis', latin="Clematis viticella", nl="Italiaanse clematis / bosrank", type="Klimplant · snoeigroep 3",
   bloei="juli – september", kleur="paars", hoogte="200–400 cm",
   licht="bloem in de zon of halfschaduw, voet in de schaduw", grond="voedzaam en doorlatend, koel en vochtig aan de voet",
   hard="goed — probleemloos winterhard",
   herken="Klimplant die zich vastmaakt met draaiende bladstelen; relatief kleine paarse bloemen met gele meeldraden, pas laat in de zomer.",
   taken=[("Februari – maart","Hard terugsnoeien tot ± 30 cm boven de grond, net boven een paar gezonde knoppen. Dit is de hele snoei voor het jaar."),
          ("Maart","Compost of organische mest rond de voet, plus mulch of een lage plant ervoor om de wortels koel te houden."),
          ("Juni – augustus","Royaal water geven bij droogte; clematis is een drinker.")],
   let="Voet in de schaduw, kop in de zon — de belangrijkste regel voor clematis. Viticella is robuust en veel minder gevoelig voor clematisverwelkingsziekte dan de grootbloemige hybriden.",
   determ=[
     ("Klopt het dat het groep 3 is?","Viticella hoort bij snoeigroep 3: de bloemen komen op scheuten die dit jaar gegroeid zijn, en de bloei begint pas in juli. Het oude hout is in het voorjaar grotendeels dood — dat hoort zo.",
      "Bloeit hij inderdaad pas vanaf juli? Dan gewoon elk voorjaar hard terugsnoeien."),
     ("Twijfelgeval: bloeit hij al in mei/juni?","Grote platte bloemen van 10–20 cm in mei/juni, op het houtige gestel van vorig jaar, met vaak een tweede ronde in september — dan is het geen viticella maar een grootbloemige hybride uit groep 2.",
      "In dat geval NIET hard terugsnoeien: alleen in februari dood hout uitdunnen. Een voorjaarssnoei kost je dan de complete bloei."),
   ],
   twijfel="Snelle check in maart: knijp in een oude stengel. Bij viticella is het meeste oude hout dood en bros — hard terugsnoeien is dan precies goed. Zitten er overal dikke, levende knoppen op het oude hout, snoei dan dit jaar niet en kijk eerst wanneer hij bloeit."),

 dict(key='echinacea', latin="Echinacea 'Green Jewel'", nl="Zonnehoed", type="Vaste plant",
   bloei="juli – september", kleur="geelgroen", hoogte="blad 50 cm, bloem 70–80 cm",
   licht="zon tot halfschaduw", grond="elke goede tuingrond — vooral in de winter niet nat",
   hard="uitstekend (−40 °C, zone 3)",
   herken="Stevige rechtopgaande stelen met geelgroene margrietachtige bloemen met een bolle hartje.",
   taken=[("Maart","Terugknippen tot 10–15 cm boven de grond; dode stelen weg."),
          ("Juli – september","Uitgebloeide bloemen wegknippen net boven een gezond blad of zijscheut — dit geeft een tweede bloeigolf."),
          ("November","Controleren of er geen water blijft staan; natte voeten in de winter is de grootste killer.")],
   let="Niet in het najaar terugknippen. Winternat is gevaarlijker dan winterkou."),

 dict(key='gaura', latin="Gaura lindheimeri", nl="Prachtkaars", type="Vaste plant",
   bloei="juni – september", kleur="wit", hoogte="blad 30–40 cm, bloem 50–70 cm",
   licht="zon tot halfschaduw", grond="goed doorlatend — beslist niet nat",
   hard="goed (−23 °C, zone 6) — de minst winterharde vaste plant in deze tuin",
   herken="Luchtige, dunne stelen met kleine witte bloemetjes die op vlindertjes lijken en bewegen in de wind.",
   taken=[("April","Pas terugknippen ná het vorstgevaar: dode stelen tot vlak boven de grond."),
          ("Juni – september","Uitgebloeide stelen licht bijknippen voor doorbloei en een vollere plant."),
          ("November","Laagje droog blad of compost rond de voet aanbrengen."),
          ("November","Controleren op droge voeten — te natte grond is dodelijk, meer nog dan de vorst.")],
   let="Knip deze plant NIET terug in het najaar. De oude stelen beschermen de kroon tegen vorst."),

 dict(key='geum', latin="Geum 'Bell Bank'", nl="Nagelkruid", type="Vaste plant, groenblijvend",
   bloei="mei – juli", kleur="koperkleurig roze, halfgevuld", hoogte="blad 20–30 cm, bloem 50 cm",
   licht="halfschaduw tot zon", grond="vruchtbaar, vochtig maar doorlatend — niet uitdrogend",
   hard="uitstekend (−40 °C, zone 3)",
   herken="Rozet van ruw, gelobd groen blad dat 's winters blijft staan; knikkende roze bloemetjes aan roodbruine stelen.",
   taken=[("Maart","Oud, lelijk geworden blad wegknippen."),
          ("April (om de 2 jaar)","Pol uitgraven en scheuren; het verhoutte hart weggooien. Houdt de plant jong en rijkbloeiend."),
          ("Mei – juli","Uitgebloeide bloemstelen wegknippen voor langere bloei."),
          ("Juli","Na de bloei alle bloemstelen terugknippen tot op het blad.")],
   let="Groenblijvend: niet kaalknippen in het najaar. Niet laten uitdrogen in de zomer."),

 dict(key='liriope', latin="Liriope muscari (waarschijnlijk)", nl="Leliegras", type="Vaste plant, groenblijvend",
   bloei="augustus – september", kleur="paars-lila", hoogte="30–45 cm",
   licht="schaduw tot halfschaduw", grond="humusrijk, vochtig maar goed doorlatend",
   hard="goed (zone 6)",
   herken="Smal, grasachtig donkergroen blad met in de nazomer rechtopstaande paarse bloemaren (lijken op hyacinten).",
   taken=[("Februari – midden maart","Alle blad — groen én bruin — afknippen op ± 5 cm boven de grond, vóór de nieuwe groei begint. Heggenschaar werkt prima."),
          ("Maart","Bemesten met compost of organische mest."),
          ("Zomer","Bij lange droogte water geven.")],
   let="Deze plant staat zonder naam in het boekje. Op basis van de foto en de alfabetische volgorde is dit vrijwel zeker Liriope muscari. Snoei jaarlijks — anders wordt de pol rommelig en schimmelgevoelig."),

 dict(key='panicum', latin="Panicum virgatum 'Northwind'", nl="Vingergras", type="Siergras",
   bloei="augustus – september", kleur="eerst groen, later lichtbruin", hoogte="blad 90–100 cm, pluim 130–150 cm",
   licht="zon tot halfschaduw", grond="elke goede tuingrond",
   hard="goed (−23 °C, zone 6)",
   herken="Strak rechtopgaande pol blauwgroen gras dat in de herfst goudgeel kleurt, met losse overhangende pluimen.",
   taken=[("Maart","Terugknippen tot 5–10 cm boven de grond. Het gras loopt daarna snel weer uit.")],
   let="NOOIT voor de winter terugknippen — dat is de meest gemaakte fout bij siergrassen en kan de pol de winter kosten."),

 dict(key='trachelospermum', latin="Trachelospermum jasminoides", nl="Toscaanse sterjasmijn", type="Klimplant, groenblijvend",
   bloei="juni – september", kleur="wit, sterk geurend", hoogte="250–400 cm",
   licht="zon tot halfschaduw, beschut tegen koude oostenwind", grond="doorlatend",
   hard="matig (−9 tot −7 °C, zone 8b) — de kwetsbaarste plant in de tuin",
   herken="Slingerende klimplant met glanzend donkergroen blad dat het hele jaar blijft, en witte stervormige bloemetjes die sterk geuren.",
   taken=[("Augustus (na de bloei)","Snoeimoment. Lange scheuten die in de weg zitten wegknippen; verder is snoei niet nodig."),
          ("November","Winterbescherming aanbrengen: laag afgevallen blad rond de voet. Staat hij in een pot? Pot inpakken."),
          ("Bij vorst onder −10 °C","Rietmat, vliesdoek of oude deken tegen de muur hangen. Dit is de plant om in de gaten te houden bij een koudegolf."),
          ("April","Winterbescherming weghalen zodra de nachtvorst voorbij is. Eventueel dan pas grondig terugsnoeien.")],
   let="Niet in oktober tot op het kale hout snoeien — te weinig hersteltijd vóór de winter. Bij een strenge winter is dit de plant die het niet redt zonder hulp."),

 dict(key='vinca', latin="Vinca minor", nl="Maagdenpalm", type="Vaste plant, bodembedekker, groenblijvend",
   bloei="februari – mei", kleur="blauw", hoogte="10–15 cm",
   licht="zon of schaduw — verdraagt alles", grond="elke goede tuingrond",
   hard="zeer goed (−26 °C, zone 5b)",
   herken="Lage, kruipende mat van klein glanzend donkergroen blad met blauwe bloempjes in het vroege voorjaar.",
   taken=[("Maart","Eén keer per jaar terugknippen: lange, houtig geworden ranken met snoeischaar of heggenschaar inkorten."),
          ("Hele jaar","Ongewenste uitlopers lostrekken — de stengels wortelen overal waar ze de grond raken.")],
   let="Woekert gestaag. Een dichte mat onderdrukt onkruid prima, maar knip hem jaarlijks terug om te voorkomen dat hij paden en buurplanten overneemt."),
]

MONTHS = [
 ("Januari","", [
   ("Toscaanse jasmijn","Winterbescherming controleren na storm; bij vorst onder −10 °C rietmat of vliesdoek aanbrengen.", 'trachelospermum'),
 ]),
 ("Februari","", [
   ("Leliegras","Eind februari mag het blad al op ± 5 cm worden afgeknipt.", 'liriope'),
   ("Clematis viticella","Hard terugsnoeien tot ± 30 cm boven de grond (mag ook nog in maart).", 'clematis'),
 ]),
 ("Maart","de grote snoeimaand", [
   ("Zilverkaars","Oud loof afknippen vlak vóór het uitlopen.", 'actaea'),
   ("Brunnera 'Jack Frost'","Oud loof afknippen tot ± 5 cm.", 'brunnera'),
   ("Zonnehoed","Terugknippen tot 10–15 cm boven de grond.", 'echinacea'),
   ("Vingergras","Terugknippen tot 5–10 cm boven de grond.", 'panicum'),
   ("Leliegras","Alle blad afknippen op ± 5 cm (uiterlijk midden maart).", 'liriope'),
   ("Maagdenpalm","Jaarlijkse terugknipbeurt: lange houtige ranken inkorten.", 'vinca'),
   ("Nagelkruid","Oud, lelijk geworden blad weghalen.", 'geum'),
   ("Clematis viticella","Uiterste snoeimoment: terug tot ± 30 cm. Daarna mulch of een lage plant ervoor voor een koele voet.", 'clematis'),
   ("Alle planten","Laagje compost of organische mest rondom.", None),
 ]),
 ("April","", [
   ("Prachtkaars","Terugknippen tot vlak boven de grond, zodra het vorstgevaar voorbij is.", 'gaura'),
   ("Nagelkruid","Om de twee jaar: pol scheuren, verhout hart weggooien.", 'geum'),
   ("Toscaanse jasmijn","Winterbescherming weghalen; eventueel nu grondiger terugsnoeien.", 'trachelospermum'),
 ]),
 ("Mei","", [
   ("Nagelkruid","Uitgebloeide bloemen wegknippen.", 'geum'),
 ]),
 ("Juni","", [
   ("Brunnera 'Jack Frost'","Uitgebloeide bloemstelen helemaal wegknippen.", 'brunnera'),
   ("Zilverkaars & Brunnera","Water geven bij droogte; deze twee gaan als eerste slap.", 'actaea'),
   ("Clematis viticella","Royaal water geven bij droogte.", 'clematis'),
 ]),
 ("Juli","", [
   ("Nagelkruid","Na de bloei alle bloemstelen terugknippen tot op het blad.", 'geum'),
   ("Zonnehoed","Uitgebloeide bloemen wegknippen boven een zijscheut, voor herbloei.", 'echinacea'),
   ("Prachtkaars","Licht bijknippen voor doorbloei.", 'gaura'),
   ("Zilverkaars","Bij droogte flink water geven.", 'actaea'),
 ]),
 ("Augustus","snoeimoment klimplant", [
   ("Toscaanse jasmijn","Na de bloei snoeien: lange scheuten die in de weg zitten wegknippen. Dit is hét moment.", 'trachelospermum'),
   ("Zonnehoed","Uitgebloeide bloemen blijven wegknippen.", 'echinacea'),
   ("Zilverkaars","Bij droogte water geven.", 'actaea'),
 ]),
 ("September","", [
   ("Prachtkaars","Licht bijknippen mag nog.", 'gaura'),
 ]),
 ("Oktober","", []),
 ("November","winterklaar maken", [
   ("Toscaanse jasmijn","Winterbescherming aanbrengen: laag blad rond de voet; pot inpakken indien van toepassing.", 'trachelospermum'),
   ("Prachtkaars","Laagje droog blad of compost rond de voet.", 'gaura'),
   ("Zonnehoed & Prachtkaars","Controleer of er geen water blijft staan — winternat is het grootste risico.", 'echinacea'),
 ]),
 ("December","", [
   ("Toscaanse jasmijn","Bij vorst onder −10 °C: rietmat of vliesdoek tegen de muur.", 'trachelospermum'),
 ]),
]

BRONNEN = [
 ("Beplantingsboekje (uw eigen tuin)", None),
 ("Actaea simplex — robs-tuinplanten.nl","https://robs-tuinplanten.nl/zilverkaars-actaea-simplex-verzorging-standplaats-planten-snoeien-en-vermeerderen"),
 ("Brunnera macrophylla — greenfingersonline.nl","https://greenfingersonline.nl/brunnera/"),
 ("Clematis snoeigroepen — groei.nl","https://groei.nl/tuin/tuinkalender/clematis-snoeien"),
 ("Clematis groep 3 (viticella) — greenfingersonline.nl","https://greenfingersonline.nl/clematis-groep-3/"),
 ("Echinacea — intratuin.nl","https://www.intratuin.nl/plantengids/zonnehoed-echinacea-verzorging-snoeien"),
 ("Gaura — tuinadvies.nl","https://www.tuinadvies.nl/tuininfo/planten/sierplanten/gaura-snoeien-winter-prachtkaars/"),
 ("Geum 'Bell Bank' — tuinadvies.nl","https://www.tuinadvies.nl/plantengids/1755/geum-bell-bank"),
 ("Liriope muscari — plantnu.nl","https://plantnu.nl/leliegras-liriope-muscari/"),
 ("Panicum 'Northwind' — bomenenzo.nl","https://www.bomenenzo.nl/panicum-virgatum-northwind"),
 ("Trachelospermum jasminoides — intratuin.nl","https://www.intratuin.nl/plantengids/toscaanse-jasmijn-trachelospermum-jasminoides-snoeien-verzorgen"),
 ("Vinca minor — snoeien.nl","https://snoeien.nl/vaste-planten/maagdenpalm/"),
]

e = html.escape
byk = {p['key']: p for p in PLANTS}

# ---------- calendar html ----------
cal = []
for i,(name, tag, items) in enumerate(MONTHS, start=1):
    rows = []
    for title, txt, k in items:
        if k:
            thumb = f'<span class="thumb bg-{k}"></span>'
            attrs = f' class="go" data-p="{k}" tabindex="0" role="link" title="Bekijk {e(byk[k]["nl"])} in de plantengids"'
            arrow = '<span class="arrow" aria-hidden="true">›</span>'
        else:
            thumb, attrs, arrow = '<span class="thumb ph">•</span>', '', ''
        rows.append(f'<li{attrs}>{thumb}<div><b>{e(title)}</b><span>{e(txt)}</span></div>{arrow}</li>')
    body = f'<ul>{"".join(rows)}</ul>' if rows else '<p class="empty">Geen onderhoud</p>'
    tagh = f'<span class="tag">{e(tag)}</span>' if tag else ''
    cls = 'month' if rows else 'month none'
    cal.append(f'''<section class="{cls}" id="m{i}">
  <header><h3>{e(name)}</h3>{tagh}</header>
  {body}
</section>''')

# ---------- plants html ----------
pl = []
for p in PLANTS:
    taken = "".join(f'<li><b>{e(w)}</b><span>{e(t)}</span></li>' for w,t in p['taken'])
    extra = ''
    if p.get('determ'):
        blk = "".join(
            f'<div class="dcase"><b>{e(t)}</b><p>{e(d)}</p><p class="do">→ {e(a)}</p></div>'
            for t, d, a in p['determ'])
        extra = (f'<div class="determ"><h4>Welke snoeigroep heb je?</h4>{blk}'
                 f'<p class="tw">{e(p["twijfel"])}</p></div>')
    if p['key'] == 'clematis':
        extra += ('<p class="note">Foto: Clematis viticella \'Étoile Violette\' in Goodnestone Park, Kent — '
                  'via Wikimedia Commons. Dit is niet jullie eigen plant; de kleur en bloemvorm kunnen '
                  'per viticella-cultivar verschillen.</p>')
    pl.append(f'''<article class="plant" id="p-{p['key']}">
  <div class="hero bg-{p['key']}" role="img" aria-label="{e(p['nl'])}"></div>
  <div class="pbody">
    <h3>{e(p['nl'])}</h3>
    <p class="latin">{e(p['latin'])}</p>
    <p class="herken">{e(p['herken'])}</p>
    <dl class="specs">
      <dt>Type</dt><dd>{e(p['type'])}</dd>
      <dt>Bloei</dt><dd>{e(p['bloei'])} · {e(p['kleur'])}</dd>
      <dt>Hoogte</dt><dd>{e(p['hoogte'])}</dd>
      <dt>Licht</dt><dd>{e(p['licht'])}</dd>
      <dt>Grond</dt><dd>{e(p['grond'])}</dd>
      <dt>Winterhard</dt><dd>{e(p['hard'])}</dd>
    </dl>
    <h4>Onderhoud</h4>
    <ul class="taken">{taken}</ul>
    <p class="let"><b>Let op:</b> {e(p['let'])}</p>
    {extra}
  </div>
</article>''')

nav_plants = "".join(
    f'<a href="#p-{p["key"]}"><span class="nimg bg-{p["key"]}"></span><span>{e(p["nl"])}</span></a>'
    for p in PLANTS)

IMGCSS = "".join(
    f'.bg-{k}{{background-image:url({v})}}' for k, v in imgs.items())

MONTHDATA = json.dumps(
    [[{"t": t, "d": d, "p": k} for t, d, k in items] for _, _, items in MONTHS],
    ensure_ascii=False)

bronnen = "".join(
    (f'<li><a href="{u}" target="_blank" rel="noopener">{e(t)}</a></li>' if u else f'<li>{e(t)}</li>')
    for t,u in BRONNEN)

DOC = f'''<!DOCTYPE html>
<html lang="nl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tuinkalender</title>
<style>
:root{{color-scheme:light;--g:#2f6b47;--g2:#4a8f66;--bg:#fbfaf6;--card:#fff;--line:#e4e2d8;--tx:#252a26;--mut:#6b7268;--warn:#8a5a1e;--warnbg:#fdf6e8}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--tx);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding:24px 20px 64px}}
h1{{font-size:30px;margin:0 0 4px;letter-spacing:-.02em}}
.sub{{color:var(--mut);margin:0 0 22px}}
.tabs{{display:flex;gap:6px;border-bottom:2px solid var(--line);margin-bottom:20px}}
.tabs button{{background:none;border:0;padding:10px 16px;font:600 15px/1 inherit;color:var(--mut);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px}}
.tabs button.on{{color:var(--g);border-color:var(--g)}}
.panel{{display:none}} .panel.on{{display:block}}
.now{{background:linear-gradient(135deg,#2f6b47,#4a8f66);color:#fff;border-radius:14px;padding:18px 20px;margin-bottom:24px}}
.now h2{{margin:0 0 10px;font-size:19px}}
.now ul{{margin:0;padding-left:18px}} .now li{{margin:4px 0}}
.now .none{{opacity:.9;font-style:italic}}
.jump{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px}}
.jump a{{font-size:13px;padding:5px 11px;border:1px solid var(--line);border-radius:99px;background:var(--card);color:var(--tx);text-decoration:none}}
.jump a:hover{{border-color:var(--g);color:var(--g)}}
.jump a.cur{{background:var(--g);color:#fff;border-color:var(--g)}}
.months{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
.month{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;scroll-margin-top:16px}}
.month.cur{{border-color:var(--g);box-shadow:0 0 0 2px rgba(47,107,71,.15)}}
.month header{{display:flex;align-items:baseline;gap:10px;margin-bottom:10px;padding-bottom:8px;border-bottom:1px solid var(--line)}}
.month h3{{margin:0;font-size:19px;color:var(--g)}}
.tag{{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.05em}}
.month ul{{list-style:none;margin:0;padding:0}}
.month.none{{opacity:.6}}
.month .empty{{margin:0;color:var(--mut);font-size:14px;font-style:italic}}
.month li{{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #f2f1ea;align-items:flex-start}}
.month li:last-child{{border:0;padding-bottom:0}}
.thumb{{width:46px;height:46px;border-radius:8px;flex:none;border:1px solid var(--line);background-size:cover;background-position:center}}
.thumb.ph{{display:flex;align-items:center;justify-content:center;background:#f1efe6;color:var(--mut)}}
.month li b{{display:block;font-size:14px}}
.month li div span{{display:block;font-size:14px;color:var(--mut);line-height:1.45}}
.month li.go{{cursor:pointer;margin:0 -8px;padding-left:8px;padding-right:8px;border-radius:8px}}
.month li.go .arrow{{margin-left:auto;align-self:center;color:var(--line);font-size:22px;line-height:1;flex:none;transition:color .12s,transform .12s}}
.month li.go:hover,.month li.go:focus{{background:#f3f7f4;outline:none}}
.month li.go:hover b,.month li.go:focus b{{color:var(--g)}}
.month li.go:hover .arrow,.month li.go:focus .arrow{{color:var(--g);transform:translateX(2px)}}
.now li{{cursor:pointer}} .now li:hover{{text-decoration:underline}}
.plant.flash{{animation:fl 1.4s ease-out}}
@keyframes fl{{0%,55%{{box-shadow:0 0 0 3px rgba(47,107,71,.45)}}100%{{box-shadow:0 0 0 3px rgba(47,107,71,0)}}}}
.back{{background:var(--card);border:1px solid var(--line);border-radius:99px;padding:6px 14px;font:600 13px/1 inherit;color:var(--g);cursor:pointer;margin-bottom:16px}}
.back:hover{{border-color:var(--g);background:#f3f7f4}}
.pnav{{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:10px;margin-bottom:26px}}
.pnav a{{text-decoration:none;color:var(--tx);text-align:center;font-size:13px}}
.pnav .nimg{{width:100%;aspect-ratio:1;border-radius:10px;border:1px solid var(--line);display:block;margin-bottom:5px;background-size:cover;background-position:center}}
.pnav a:hover .nimg{{border-color:var(--g)}}
.plant{{display:grid;grid-template-columns:300px 1fr;gap:22px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin-bottom:16px;scroll-margin-top:16px}}
.plant .hero{{width:100%;height:260px;border-radius:10px;background-size:cover;background-position:center;border:1px solid var(--line)}}
.plant h3{{margin:0;font-size:21px;color:var(--g)}}
.latin{{margin:2px 0 10px;font-style:italic;color:var(--mut);font-size:14px}}
.herken{{margin:0 0 12px;font-size:15px}}
.specs{{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;margin:0 0 14px;font-size:14px}}
.specs dt{{color:var(--mut)}} .specs dd{{margin:0}}
.plant h4{{margin:0 0 6px;font-size:14px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}}
.taken{{list-style:none;margin:0 0 12px;padding:0}}
.taken li{{padding:6px 0;border-bottom:1px solid #f2f1ea;font-size:14px}}
.taken li:last-child{{border:0}}
.taken b{{color:var(--g2);display:inline-block;min-width:150px;vertical-align:top}}
.taken span{{display:inline}}
.let{{background:var(--warnbg);border-left:3px solid var(--warn);padding:9px 12px;margin:0;font-size:14px;border-radius:0 6px 6px 0}}
.determ{{margin-top:14px;border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:#f7f9f6}}
.determ h4{{margin:0 0 8px}}
.dcase{{padding:8px 0;border-bottom:1px solid #e6eae2}}
.dcase:last-of-type{{border:0}}
.dcase b{{font-size:14px}}
.dcase p{{margin:3px 0 0;font-size:14px;color:var(--mut)}}
.dcase .do{{color:var(--g);font-weight:600}}
.determ .tw{{margin:10px 0 0;font-size:14px;padding-top:10px;border-top:1px solid #e6eae2}}
.note{{margin:12px 0 0;font-size:13px;color:var(--mut);font-style:italic}}
footer{{margin-top:34px;padding-top:16px;border-top:1px solid var(--line);font-size:13px;color:var(--mut)}}
footer ul{{margin:6px 0 0;padding-left:18px}}
footer a{{color:var(--g)}}
@media(max-width:640px){{.plant{{grid-template-columns:1fr}}.taken b{{min-width:0;display:block}}}}
{IMGCSS}
</style></head><body>
<div class="wrap">
<h1>Tuinkalender</h1>
<p class="sub">Wat moet er wanneer gebeuren — met foto's, zodat je de plant herkent zonder de naam te weten.</p>

<div class="now" id="now"></div>

<div class="tabs">
  <button class="on" data-t="cal">Kalender</button>
  <button data-t="pl">Plantengids</button>
</div>

<div class="panel on" id="cal">
  <div class="jump" id="jump"></div>
  <div class="months">{"".join(cal)}</div>
</div>

<div class="panel" id="pl">
  <button class="back" id="back">‹ Terug naar de kalender</button>
  <div class="pnav">{nav_plants}</div>
  {"".join(pl)}
</div>

<footer>Bronnen:
<ul>{bronnen}</ul>
</footer>
</div>
<script>
var MN=["Januari","Februari","Maart","April","Mei","Juni","Juli","Augustus","September","Oktober","November","December"];
var m=new Date().getMonth();
// jump bar
var j=document.getElementById('jump');
MN.forEach(function(n,i){{
  var a=document.createElement('a');a.href='#m'+(i+1);a.textContent=n;
  if(i===m)a.className='cur';j.appendChild(a);
}});
document.getElementById('m'+(m+1)).classList.add('cur');
// tabs
function tab(id){{
  document.querySelectorAll('.tabs button').forEach(function(x){{x.classList.toggle('on',x.dataset.t===id)}});
  document.querySelectorAll('.panel').forEach(function(x){{x.classList.toggle('on',x.id===id)}});
}}
document.querySelectorAll('.tabs button').forEach(function(b){{
  b.onclick=function(){{tab(b.dataset.t)}};
}});
// doorklikken naar de plantengids
function openPlant(key){{
  tab('pl');
  var el=document.getElementById('p-'+key);
  if(!el)return;
  el.scrollIntoView({{behavior:'smooth',block:'start'}});
  el.classList.remove('flash');void el.offsetWidth;el.classList.add('flash');
}}
document.querySelectorAll('li.go').forEach(function(li){{
  li.addEventListener('click',function(){{openPlant(li.dataset.p)}});
  li.addEventListener('keydown',function(ev){{
    if(ev.key==='Enter'||ev.key===' '){{ev.preventDefault();openPlant(li.dataset.p);}}
  }});
}});
document.querySelectorAll('.pnav a').forEach(function(a){{
  a.addEventListener('click',function(ev){{ev.preventDefault();openPlant(a.getAttribute('href').slice(3));}});
}});
document.getElementById('back').addEventListener('click',function(){{
  tab('cal');
  document.getElementById('m'+(m+1)).scrollIntoView({{behavior:'smooth',block:'center'}});
}});
// "now" box — opgebouwd uit de brondata, niet uit de DOM
var MD={MONTHDATA};
function esc(s){{return s.replace(/[&<>"]/g,function(c){{
  return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c];}});}}
var mine=MD[m]||[];
document.getElementById('now').innerHTML='<h2>Deze maand: '+MN[m]+'</h2>'+
  (mine.length ? '<ul>'+mine.map(function(it){{
      return '<li'+(it.p?' data-p="'+it.p+'"':'')+'><b>'+esc(it.t)+'</b> — '+esc(it.d)+'</li>';
    }}).join('')+'</ul>'
              : '<p class="none">Geen onderhoud</p>');
document.querySelectorAll('.now li[data-p]').forEach(function(li){{
  li.addEventListener('click',function(){{openPlant(li.dataset.p)}});
}});
</script>
</body></html>'''

open('tuinkalender.html','w').write(DOC)
print('ok', len(DOC)//1024, 'KB')
