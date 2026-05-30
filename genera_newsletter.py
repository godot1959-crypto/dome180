"""
Generatore prototipo newsletter Substack - "Il Mondo di Dome"
Periodo: 1-15 maggio 2026 (esempio dimostrativo)
Nota: i contenuti sono FITTIZI/ILLUSTRATIVI per mostrare il layout.
      Nella versione operativa verranno sostituiti con dati reali da fonti verificate.
"""

import datetime

def genera_html():
    oggi = datetime.date(2026, 5, 15)
    numero = 1

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Il Mondo di Dome - N.{numero}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Charter:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;600;700&display=swap');

  * {{ margin:0; padding:0; box-sizing:border-box; }}

  body {{
    font-family: Charter, Georgia, 'Times New Roman', serif;
    background: #f7f5f2;
    color: #1a1a1a;
    line-height: 1.7;
  }}

  .container {{
    max-width: 680px;
    margin: 0 auto;
    background: #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  }}

  /* HEADER */
  .header {{
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: #fff;
    padding: 40px 32px 32px;
    text-align: center;
  }}
  .header h1 {{
    font-family: Inter, Helvetica, sans-serif;
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
    margin-bottom: 6px;
  }}
  .header .subtitle {{
    font-size: 14px;
    opacity: 0.8;
    font-style: italic;
  }}
  .header .meta {{
    margin-top: 16px;
    font-family: Inter, sans-serif;
    font-size: 12px;
    opacity: 0.6;
  }}

  /* NAV periodicita */
  .nav-bar {{
    background: #e63946;
    color: #fff;
    font-family: Inter, sans-serif;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 10px 32px;
    display: flex;
    justify-content: space-between;
  }}

  /* CONTENT */
  .content {{ padding: 0 32px 40px; }}

  /* PAGE SECTIONS */
  .page-break {{
    border-top: 3px solid #0f3460;
    margin: 36px 0 28px;
    position: relative;
  }}
  .page-label {{
    font-family: Inter, sans-serif;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #0f3460;
    background: #fff;
    position: absolute;
    top: -8px;
    left: 0;
    padding-right: 12px;
  }}

  /* SECTION HEADERS */
  .section-title {{
    font-family: Inter, sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #1a1a2e;
    margin: 28px 0 6px;
    padding-bottom: 6px;
    border-bottom: 2px solid #e63946;
  }}
  .section-icon {{
    margin-right: 8px;
  }}

  /* CARDS */
  .card {{
    background: #fafafa;
    border-left: 4px solid #0f3460;
    padding: 14px 16px;
    margin: 14px 0;
    border-radius: 0 6px 6px 0;
  }}
  .card h3 {{
    font-family: Inter, sans-serif;
    font-size: 14px;
    font-weight: 700;
    color: #0f3460;
    margin-bottom: 4px;
  }}
  .card p {{
    font-size: 14px;
    line-height: 1.6;
  }}
  .card .fonte {{
    font-size: 11px;
    color: #888;
    margin-top: 6px;
    font-style: italic;
  }}

  /* BANDO */
  .bando {{
    border-left-color: #e63946;
  }}
  .bando-meta {{
    display: flex;
    gap: 16px;
    margin-top: 6px;
    font-family: Inter, sans-serif;
    font-size: 12px;
  }}
  .bando-meta span {{
    background: #f0f0f0;
    padding: 2px 8px;
    border-radius: 3px;
    font-weight: 600;
  }}
  .bando-meta .valore {{ color: #2d6a4f; }}
  .bando-meta .scadenza {{ color: #e63946; }}

  /* NORMATIVA */
  .normativa {{
    border-left-color: #457b9d;
  }}

  /* WORLD */
  .world-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
  }}
  .world-flag {{
    font-size: 24px;
    min-width: 36px;
    text-align: center;
  }}
  .world-text {{
    flex: 1;
  }}
  .world-text .paese {{
    font-family: Inter, sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #888;
  }}
  .world-text .testata {{
    font-size: 11px;
    color: #aaa;
    font-style: italic;
  }}
  .world-text .titolo {{
    font-size: 14px;
    font-weight: 700;
    color: #1a1a2e;
    margin-top: 2px;
  }}
  .world-text .fonte {{
    font-size: 11px;
    color: #888;
    margin-top: 2px;
    font-style: italic;
  }}

  /* PILLOLE */
  .pillola {{
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px 16px;
    margin: 10px 0;
  }}
  .pillola-cat {{
    font-family: Inter, sans-serif;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #e63946;
    margin-bottom: 4px;
  }}
  .pillola p {{
    font-size: 13px;
    line-height: 1.5;
  }}
  .pillola .fonte {{
    font-size: 11px;
    color: #888;
    margin-top: 4px;
    font-style: italic;
  }}

  /* FOOTER */
  .footer {{
    background: #1a1a2e;
    color: rgba(255,255,255,0.7);
    padding: 28px 32px;
    font-family: Inter, sans-serif;
    font-size: 12px;
    text-align: center;
    line-height: 1.8;
  }}
  .footer a {{ color: #e63946; text-decoration: none; }}

  .disclaimer {{
    background: #fff3cd;
    border: 1px solid #ffc107;
    padding: 12px 16px;
    margin: 20px 0;
    border-radius: 6px;
    font-size: 12px;
    font-style: italic;
    color: #664d03;
  }}

  .separator {{
    text-align: center;
    margin: 24px 0;
    color: #ccc;
    letter-spacing: 8px;
  }}

  .subscribe-cta {{
    background: #e63946;
    color: #fff;
    text-align: center;
    padding: 20px 32px;
    font-family: Inter, sans-serif;
  }}
  .subscribe-cta a {{
    display: inline-block;
    background: #fff;
    color: #e63946;
    font-weight: 700;
    padding: 10px 28px;
    border-radius: 20px;
    text-decoration: none;
    font-size: 14px;
    margin-top: 8px;
  }}
</style>
</head>
<body>

<div class="container">

  <!-- HEADER -->
  <div class="header">
    <h1>IL MONDO DI DOME</h1>
    <div class="subtitle">Scienza &middot; Normativa &middot; Economia Globale &middot; Curiosit&agrave;</div>
    <div class="meta">N.{numero} &mdash; 15 maggio 2026 &nbsp;|&nbsp; Periodo: 1-15 maggio 2026 &nbsp;|&nbsp; Cadenza quindicinale</div>
  </div>

  <div class="nav-bar">
    <span>Prima Pagina &rarr; Approfondimento &rarr; Curiosit&agrave;</span>
    <span>4 di 4 numeri</span>
  </div>

  <div class="content">

    <div class="disclaimer">
      <strong>Nota editoriale:</strong> Questo &egrave; un PROTOTIPO di layout per la newsletter Substack.
      I contenuti sotto riportati sono a scopo illustrativo per mostrare la struttura.
      Ogni notizia nella versione operativa sar&agrave; verificata e riporter&agrave; fonte, autore e link diretto.
      I testi NON riproducono articoli originali ma sintetizzano dati pubblici nel rispetto del copyright.
    </div>

    <!-- ==================== PRIMA PAGINA ==================== -->
    <div class="page-break">
      <span class="page-label">Prima Pagina</span>
    </div>

    <h2 class="section-title">
      <span class="section-icon">&#129514;</span>Scoperte Scientifiche
    </h2>
    <p style="font-size:13px; color:#666; margin-bottom:12px;">
      Medicina &amp; Energia &mdash; Focus su ricercatori italiani
    </p>

    <!-- Scienziato 1 -->
    <div class="card">
      <h3>Prof.ssa Elena Bhatt &mdash; Immunoterapia di nuova generazione</h3>
      <p>
        <strong>Chi &egrave;:</strong> Oncologa e immunologa presso l'Istituto Europeo di Oncologia (IEO), Milano.
        Laurea in Medicina all'Universit&agrave; di Padova, specializzazione al Dana-Farber Cancer Institute (Boston).<br>
        <strong>Cosa ha sviluppato:</strong> Un protocollo di immunoterapia combinata (anticorpi bispecifici + CAR-T modificate)
        che in fase II ha mostrato risposte nel trattamento di linfomi resistenti alle terapie standard.<br>
        <strong>A cosa serve:</strong> Potrebbe offrire nuove opzioni per pazienti oncologici che non rispondono ai trattamenti attuali.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Per dati reali consultare: <em>ClinicalTrials.gov</em>, pubblicazioni IEO, <em>The Lancet Oncology</em>
      </div>
    </div>

    <!-- Scienziato 2 -->
    <div class="card">
      <h3>Prof. Marco Delgado &mdash; Celle solari a perovskite tandem</h3>
      <p>
        <strong>Chi &egrave;:</strong> Fisico dei materiali, Politecnico di Torino. Ricercatore presso il Centro Italiano Ricerche Aerospaziali (CIRA).<br>
        <strong>Cosa ha sviluppato:</strong> Una nuova architettura di celle fotovoltaiche tandem silicio-perovskite
        con efficienza di conversione superiore al 30% in condizioni di laboratorio.<br>
        <strong>A cosa serve:</strong> Ridurre i costi dell'energia solare e accelerare la transizione energetica europea.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Per dati reali consultare: <em>Nature Energy</em>, pubblicazioni ENEA/Polito, <em>EU PV Status Report</em>
      </div>
    </div>

    <div class="separator">&bull; &bull; &bull;</div>

    <h2 class="section-title">
      <span class="section-icon">&#127466;&#127482;</span>Bandi Europei &mdash; Ricerca &amp; Innovazione
    </h2>

    <div class="card bando">
      <h3>Horizon Europe &mdash; Cluster 1: Health</h3>
      <p>Bando per progetti di ricerca su terapie avanzate e medicina personalizzata nell'ambito del programma Horizon Europe 2025-2027.</p>
      <div class="bando-meta">
        <span class="valore">Valore: &euro; 120 milioni (budget indicativo)</span>
        <span class="scadenza">Scadenza: settembre 2026</span>
      </div>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Verificare su: <em>ec.europa.eu/funding-tenders</em> (portale ufficiale bandi UE)
      </div>
    </div>

    <div class="card bando">
      <h3>EIC Accelerator &mdash; Clean Energy Transition</h3>
      <p>Sostegno a PMI e startup per tecnologie di accumulo energetico e idrogeno verde, con grant e equity blended finance.</p>
      <div class="bando-meta">
        <span class="valore">Valore: fino a &euro; 2,5 mln (grant) + &euro; 15 mln (equity)</span>
        <span class="scadenza">Scadenza: ottobre 2026</span>
      </div>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Verificare su: <em>eic.ec.europa.eu</em>
      </div>
    </div>

    <div class="card bando">
      <h3>LIFE Programme &mdash; Clean Energy Transition</h3>
      <p>Co-finanziamento per progetti pilota di efficienza energetica in edilizia pubblica e comunit&agrave; energetiche rinnovabili.</p>
      <div class="bando-meta">
        <span class="valore">Valore: &euro; 80 milioni (dotazione totale call)</span>
        <span class="scadenza">Scadenza: novembre 2026</span>
      </div>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Verificare su: <em>cinea.ec.europa.eu/programmes/life</em>
      </div>
    </div>


    <!-- ==================== SECONDA PAGINA ==================== -->
    <div class="page-break">
      <span class="page-label">Seconda Pagina &mdash; Approfondimento</span>
    </div>

    <h2 class="section-title">
      <span class="section-icon">&#9878;</span>Novit&agrave; Normative
    </h2>

    <div class="card normativa">
      <h3>&#127466;&#127482; UE &mdash; Sanit&agrave;: Regolamento Spazio Europeo dei Dati Sanitari</h3>
      <p>
        Il Regolamento EHDS (European Health Data Space) disciplina l'accesso e la portabilit&agrave;
        dei dati sanitari elettronici tra gli Stati membri. Prevede diritti per i pazienti e obblighi
        per i fornitori di cartelle cliniche elettroniche.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Fonte ufficiale: <em>eur-lex.europa.eu</em>, Reg. (UE) 2025/XXX; sintesi su <em>europarl.europa.eu</em>
      </div>
    </div>

    <div class="card normativa">
      <h3>&#127466;&#127482; UE &mdash; Energia: Revisione Direttiva Rinnovabili (RED III)</h3>
      <p>
        Nuovi obiettivi vincolanti per la quota di energie rinnovabili nei trasporti e nel riscaldamento.
        Semplificazione delle procedure autorizzative per impianti FER sotto i 150 kW.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Fonte: <em>energy.ec.europa.eu</em>; Direttiva (UE) 2023/2413 e successive modifiche
      </div>
    </div>

    <div class="card normativa">
      <h3>&#127470;&#127481; Italia &mdash; Fiscale/Societario: Riforma IRES e incentivi PMI</h3>
      <p>
        Il D.Lgs. attuativo della delega fiscale interviene sulle aliquote IRES per utili reinvestiti
        e introduce un credito d'imposta per PMI innovative che investono in R&amp;S.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Fonte: <em>gazzettaufficiale.it</em>, <em>agenziaentrate.gov.it</em>
      </div>
    </div>

    <div class="card normativa">
      <h3>&#127470;&#127481; Italia &mdash; Immobiliare: Aggiornamento Catasto e Bonus Ristrutturazione</h3>
      <p>
        Nuove disposizioni sull'aggiornamento delle rendite catastali per immobili ristrutturati con Superbonus.
        Proroga con aliquota ridotta del bonus ristrutturazione ordinario per il 2026.
      </p>
      <div class="fonte">
        [Esempio illustrativo] &mdash; Fonte: <em>gazzettaufficiale.it</em>, <em>mise.gov.it</em>
      </div>
    </div>

    <div class="separator">&bull; &bull; &bull;</div>

    <h2 class="section-title">
      <span class="section-icon">&#127758;</span>Rapido Sguardo nel Mondo
    </h2>
    <p style="font-size:13px; color:#666; margin-bottom:16px;">
      Titoli dai principali quotidiani economici &mdash; prima quindicina di maggio 2026
    </p>

    <div class="world-item">
      <div class="world-flag">&#127465;&#127466;</div>
      <div class="world-text">
        <div class="paese">Germania</div>
        <div class="testata">Handelsblatt</div>
        <div class="titolo">[Titolo illustrativo] Industria tedesca: piano di investimenti da 50 miliardi per la transizione digitale</div>
        <div class="fonte">Verificare su: <em>handelsblatt.com</em></div>
      </div>
    </div>

    <div class="world-item">
      <div class="world-flag">&#127487;&#127462;</div>
      <div class="world-text">
        <div class="paese">Sud Africa</div>
        <div class="testata">Business Day</div>
        <div class="titolo">[Titolo illustrativo] Johannesburg Stock Exchange: rally del settore minerario sui prezzi del platino</div>
        <div class="fonte">Verificare su: <em>businesslive.co.za</em></div>
      </div>
    </div>

    <div class="world-item">
      <div class="world-flag">&#127472;&#127479;</div>
      <div class="world-text">
        <div class="paese">Corea del Sud</div>
        <div class="testata">Maeil Business Newspaper</div>
        <div class="titolo">[Titolo illustrativo] Samsung e Hyundai investono nell'AI per semiconduttori di nuova generazione</div>
        <div class="fonte">Verificare su: <em>mk.co.kr</em> (ed. inglese)</div>
      </div>
    </div>

    <div class="world-item">
      <div class="world-flag">&#127463;&#127479;</div>
      <div class="world-text">
        <div class="paese">Brasile</div>
        <div class="testata">Valor Econ&ocirc;mico</div>
        <div class="titolo">[Titolo illustrativo] Banca Centrale brasiliana: tassi fermi, focus su inflazione alimentare</div>
        <div class="fonte">Verificare su: <em>valor.globo.com</em></div>
      </div>
    </div>

    <div class="world-item">
      <div class="world-flag">&#127462;&#127482;</div>
      <div class="world-text">
        <div class="paese">Australia</div>
        <div class="testata">The Australian Financial Review</div>
        <div class="titolo">[Titolo illustrativo] Boom del litio australiano: nuovi accordi di fornitura con il Giappone</div>
        <div class="fonte">Verificare su: <em>afr.com</em></div>
      </div>
    </div>


    <!-- ==================== TERZA PAGINA ==================== -->
    <div class="page-break">
      <span class="page-label">Terza Pagina &mdash; Curiosit&agrave;</span>
    </div>

    <h2 class="section-title">
      <span class="section-icon">&#128640;</span>Startup &amp; Round (1-50 mln &euro;)
    </h2>
    <p style="font-size:13px; color:#666; margin-bottom:12px;">
      Italia, Spagna, Olanda, Polonia
    </p>

    <div class="pillola">
      <div class="pillola-cat">&#127470;&#127481; Italia</div>
      <p><strong>[Nome startup illustrativo]</strong> &mdash; Healthtech milanese, chiude un Series A da &euro;8 mln
      per la sua piattaforma di diagnostica AI applicata alla radiologia.</p>
      <div class="fonte">Fonti reali da consultare: <em>startupitalia.eu</em>, <em>dealroom.co</em>, <em>crunchbase.com</em></div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127466;&#127480; Spagna</div>
      <p><strong>[Nome startup illustrativo]</strong> &mdash; Fintech di Barcellona, raccoglie &euro;12 mln in Series B
      per espandere il suo servizio di pagamenti B2B in America Latina.</p>
      <div class="fonte">Fonti reali da consultare: <em>novobrief.com</em>, <em>dealroom.co</em></div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127475;&#127473; Olanda</div>
      <p><strong>[Nome startup illustrativo]</strong> &mdash; Cleantech di Amsterdam, round da &euro;22 mln per
      tecnologia di cattura della CO2 da processi industriali.</p>
      <div class="fonte">Fonti reali da consultare: <em>siliconcanals.com</em>, <em>dealroom.co</em></div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127477;&#127473; Polonia</div>
      <p><strong>[Nome startup illustrativo]</strong> &mdash; SaaS cybersecurity di Varsavia, chiude &euro;5 mln seed
      per protezione anti-phishing basata su AI generativa.</p>
      <div class="fonte">Fonti reali da consultare: <em>therecursive.com</em>, <em>dealroom.co</em></div>
    </div>

    <div class="separator">&bull; &bull; &bull;</div>

    <h2 class="section-title">
      <span class="section-icon">&#127909;</span>Content Creator &mdash; Oltre 1 mln follower su YouTube
    </h2>

    <div class="pillola">
      <div class="pillola-cat">&#127470;&#127481; Italia</div>
      <p><strong>[Nome creator illustrativo]</strong> &mdash; Supera 1,5 mln di iscritti con contenuti di divulgazione scientifica.
      Collaborazione annunciata con un'universit&agrave; pubblica per un format educativo.</p>
      <div class="fonte">Dati reali da: <em>socialblade.com</em>, canali YouTube verificati</div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127466;&#127480; Spagna</div>
      <p><strong>[Nome creator illustrativo]</strong> &mdash; Creator tech spagnolo raggiunge 2 mln di iscritti.
      Lancia una linea di merchandise in collaborazione con un brand locale.</p>
      <div class="fonte">Dati reali da: <em>socialblade.com</em>, canali YouTube verificati</div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127475;&#127473; Olanda</div>
      <p><strong>[Nome creator illustrativo]</strong> &mdash; Canale gaming olandese tocca 1,2 mln. Primo creator NL
      invitato come speaker a un evento istituzionale sull'educazione digitale.</p>
      <div class="fonte">Dati reali da: <em>socialblade.com</em>, canali YouTube verificati</div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">&#127477;&#127473; Polonia</div>
      <p><strong>[Nome creator illustrativo]</strong> &mdash; Creator polacco di cucina supera 1,1 mln.
      Pubblica un libro di ricette tradizionali rivisitate, bestseller in Polonia.</p>
      <div class="fonte">Dati reali da: <em>socialblade.com</em>, canali YouTube verificati</div>
    </div>

    <div class="separator">&bull; &bull; &bull;</div>

    <h2 class="section-title">
      <span class="section-icon">&#127912;</span>Mercato dell'Arte Europeo
    </h2>

    <div class="pillola">
      <div class="pillola-cat">Aste &amp; Fiere</div>
      <p><strong>[Evento illustrativo]</strong> &mdash; La fiera TEFAF Maastricht registra un incremento
      di gallerie partecipanti. Forte interesse per arte contemporanea dell'Europa dell'Est.</p>
      <div class="fonte">Fonti reali: <em>artnet.com</em>, <em>artnews.com</em>, <em>tefaf.com</em></div>
    </div>

    <div class="pillola">
      <div class="pillola-cat">Tendenza</div>
      <p><strong>[Trend illustrativo]</strong> &mdash; Crescita del mercato dell'arte digitale certificata (NFT 2.0)
      in UK e Germania, con volumi in aumento del 15% nel Q1 2026 rispetto al Q4 2025.</p>
      <div class="fonte">Fonti reali: <em>artprice.com</em>, report <em>Art Basel &amp; UBS Art Market</em></div>
    </div>

  </div><!-- /content -->

  <!-- CTA -->
  <div class="subscribe-cta">
    <div style="font-size:16px; font-weight:700;">Ti &egrave; piaciuto? Iscriviti gratuitamente.</div>
    <div style="font-size:13px; margin-top:4px; opacity:0.9;">Ogni 15 giorni nella tua casella email.</div>
    <a href="#">Iscriviti a Il Mondo di Dome</a>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <strong>Il Mondo di Dome</strong> &mdash; Newsletter quindicinale<br>
    Scienza &middot; Normativa &middot; Economia Globale &middot; Curiosit&agrave;<br><br>

    <strong>Prossime uscite:</strong> 1 giu &middot; 15 giu &middot; 1 lug &middot; 15 lug 2026<br><br>

    <strong>Avviso copyright:</strong> Questa newsletter non riproduce articoli o testi protetti da copyright.<br>
    Le notizie sono sintetizzate in forma originale con citazione della fonte.<br>
    I link rimandano sempre alla pubblicazione originale per la lettura integrale.<br><br>

    <strong>Fonti principali consultate:</strong><br>
    Scienza: PubMed, Nature, The Lancet, ENEA, CNR<br>
    Bandi: ec.europa.eu/funding-tenders, CINEA, EIC<br>
    Normativa UE: eur-lex.europa.eu, europarl.europa.eu<br>
    Normativa IT: gazzettaufficiale.it, agenziaentrate.gov.it<br>
    Economia globale: Handelsblatt, Business Day, MBN, Valor, AFR<br>
    Startup: Dealroom, Crunchbase, TechCrunch<br>
    Creator: SocialBlade, YouTube<br>
    Arte: Artnet, ArtPrice, Art Basel Report<br><br>

    <span style="opacity:0.5;">&copy; 2026 Il Mondo di Dome. Tutti i diritti riservati.</span>
  </div>

</div><!-- /container -->

</body>
</html>"""

    return html


def genera_piano_editoriale():
    """Genera un riepilogo del piano editoriale"""

    piano = """
╔══════════════════════════════════════════════════════════════════╗
║              IL MONDO DI DOME — PIANO EDITORIALE                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  Frequenza: Quindicinale (ogni 15 giorni)                       ║
║  Numeri previsti: 4                                              ║
║  Periodo: 15 mag — 15 lug 2026                                  ║
║                                                                  ║
║  N.1 → 15 maggio 2026  (periodo: 1-15 mag)                     ║
║  N.2 → 1 giugno 2026   (periodo: 16-31 mag)                    ║
║  N.3 → 15 giugno 2026  (periodo: 1-15 giu)                     ║
║  N.4 → 1 luglio 2026   (periodo: 16-30 giu)                    ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  STRUTTURA (3 pagine)                                            ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  PRIMA PAGINA                                                    ║
║  ├─ Scoperte scientifiche (medicina + energia)                  ║
║  │   → 2 scienziati, prevalenza italiani, 10 righe ciascuno    ║
║  │   → Chi è, cosa ha inventato, a cosa serve                  ║
║  └─ Bandi europei (ricerca/innovazione)                         ║
║      → Titolo, valore, scadenza                                 ║
║                                                                  ║
║  SECONDA PAGINA — Approfondimento                               ║
║  ├─ Novità normative                                            ║
║  │   → Sanità UE, Energia UE, Fiscale IT, Immobiliare IT      ║
║  └─ Rapido sguardo nel mondo                                    ║
║      → Titoli da: Handelsblatt (DE), Business Day (ZA),        ║
║        Maeil Business (KR), Valor Econômico (BR), AFR (AU)     ║
║                                                                  ║
║  TERZA PAGINA — Curiosità (pillole max 3 righe)                ║
║  ├─ Startup: round 1-50 mln (IT, ES, NL, PL)                  ║
║  ├─ Content creator: >1 mln follower YT (IT, ES, NL, PL)      ║
║  └─ Mercato dell'arte europeo                                   ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  LINGUE (future): IT (principale), DE, ES, EN                   ║
║  COPYRIGHT: nessun testo riprodotto, solo sintesi + fonte       ║
╚══════════════════════════════════════════════════════════════════╝
"""
    return piano


if __name__ == "__main__":
    # Stampa piano editoriale
    print(genera_piano_editoriale())

    # Genera HTML
    html = genera_html()
    output_path = r"C:\Users\Domenico\Desktop\cartella per claude code\Utilità\magazine di dome\newsletter_prototipo.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n✓ Newsletter HTML generata: {output_path}")
    print("  Aprire il file nel browser per visualizzare il prototipo.")
