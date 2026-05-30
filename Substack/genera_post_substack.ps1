# ============================================================
# INNESCO — Generatore automatico post Substack
# Eseguito ogni mattina alle 7:00 da Windows Task Scheduler
# ============================================================

$substackDir = "C:\Users\Domenico\Desktop\cartella per claude code\Utilità\magazine di dome\Substack"
$claudeExe   = "C:\Users\Domenico\AppData\Roaming\npm\claude.cmd"
$logFile     = "$substackDir\log_generazione.txt"
$topicsFile  = "$substackDir\topics_beta.json"

# --- Log helper ---
function Log($msg) {
    $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -Encoding UTF8
}

# --- Avvio ---
Log "===== AVVIO GENERAZIONE POST INNESCO ====="

# --- Leggi la data di oggi ---
$today = (Get-Date).ToString("yyyy-MM-dd")
Log "Data odierna: $today"

# --- Leggi il file dei topic ---
if (-not (Test-Path $topicsFile)) {
    Log "ERRORE: topics_beta.json non trovato in $substackDir"
    exit 1
}

$topicsJson = Get-Content $topicsFile -Raw -Encoding UTF8
$topics = ($topicsJson | ConvertFrom-Json).posts

# --- Trova il topic di oggi ---
$topic = $topics | Where-Object { $_.data -eq $today -and $_.completato -eq $false }

if (-not $topic) {
    Log "Nessun topic da generare per oggi ($today). Uscita."
    exit 0
}

Log "Topic trovato: Post #$($topic.n) — $($topic.tema) — $($topic.ricercatore)"
Log "File di output: $($topic.file)"

# --- Costruisci il prompt ---
$prompt = @"
Sei Claude Code. Genera il post #$($topic.n) della newsletter Substack 'Innesco' per oggi $today.

== DATI DEL POST ==
Numero post: $($topic.n) di 8
Tema: $($topic.tema)
Ricercatore / Soggetto: $($topic.ricercatore)
Scoperta / Argomento: $($topic.scoperta)
Istituzione: $($topic.istituzione)
Bando da citare: $($topic.bando)
Note operative: $($topic.note)

== ISTRUZIONI OPERATIVE ==

PASSO 1 — Cerca le fonti con WebSearch (4 ricerche):
  a) "$($topic.ricercatore) $($topic.istituzione)" — per la bio e il profilo ufficiale
  b) "$($topic.scoperta) research paper 2024 2025" — per la fonte scientifica
  c) "$($topic.bando) official" — per la pagina ufficiale del bando
  d) "$($topic.tema) statistics Europe 2025" — per dati di contesto/mercato

PASSO 2 — Scrivi il post con questa struttura esatta:

  TITOLO (maiuscolo, con nome proprio O numero concreto):
  [TEMA]: [COSA HA FATTO/SCOPERTO] — [DATO O NUMERO]

  SOTTOTITOLO (max 120 caratteri, 2 keyword SEO):
  [istituzione + scoperta + opportunita finanziamento]

  BLOCCO 1 - LA SCOPERTA (4-6 righe):
  [Nome], [ruolo], [istituzione] — [scoperta in una frase]. [Dato tecnico concreto]. [Stato brevetto/pubblicazione]. (Fonte 1)

  BLOCCO 2 - L'IDEA IMPLICITA (1-2 righe, NO call to action):
  [Frase visiva che apre lo spazio mentale del lettore]

  BLOCCO 3 - IL BANDO (4-5 righe):
  [Nome bando in grassetto] — [cosa finanzia], [importo], [percentuale copertura], [scadenza o sessioni]. [Come costituire la societa nel paese]. (Fonte 2)

  FONTI (link reali trovati con WebSearch):
  1 [Titolo — Istituzione](URL)
  2 [Titolo — Ente finanziatore](URL)
  3 [eventuale]
  4 [eventuale]

  ABSTRACT IN ENGLISH (3-4 righe, stile Reuters):
  [Stesso contenuto in inglese sintetico]

PASSO 3 — Leggi il file esistente per usare lo stesso stile CSS:
  Percorso riferimento: $substackDir\BOZZA_POST_001_2026-05-08.html

PASSO 4 — Salva il file HTML:
  Percorso: $substackDir\$($topic.file)

  Il file deve avere:
  - Barra in cima: "BOZZA #$($topic.n) . $today . Beta test"
  - Header con "Innesco" arancione (#ff6719)
  - Meta: tag [$($topic.tema)], data, "Post #$($topic.n) di 8", "Beta test"
  - Blocco scoperta con sfondo bianco
  - Blocco idea con sfondo #fff8f4 e bordo arancione a sinistra
  - Blocco bando con sfondo #f0f7f0 e bordo verde a sinistra
  - Sezione FONTI con tutti i link cliccabili
  - Abstract in inglese su sfondo scuro #1a1a1a
  - Sezione finale "Copia per Substack" con i campi:
      TITOLO, SOTTOTITOLO, OGGETTO EMAIL, CORPO DEL POST (testo puro senza HTML), TAG (5 tag)

PASSO 5 — Aggiorna topics_beta.json:
  Cambia "completato": false in "completato": true per il post #$($topic.n) (data $today).

REGOLA ASSOLUTA: usa SOLO fonti reali trovate con WebSearch.
Se non trovi una fonte, scrivi [fonte da verificare — sito: URL principale istituzione].
"@

# --- Salva il prompt su file temporaneo per evitare problemi di escaping ---
$promptFile = "$substackDir\_prompt_temp.txt"
$prompt | Out-File -FilePath $promptFile -Encoding UTF8

Log "Prompt scritto in: $promptFile"
Log "Avvio Claude Code CLI..."

# --- Esegui Claude Code ---
$env:CLAUDE_CODE_WORKING_DIR = $substackDir
Set-Location $substackDir

& $claudeExe `
    --print `
    --allowedTools "Write,Read,WebSearch,Bash" `
    --output-format text `
    --add-dir $substackDir `
    (Get-Content $promptFile -Raw) `
    2>&1 | Tee-Object -FilePath $logFile -Append

$exitCode = $LASTEXITCODE
Log "Claude Code terminato con codice: $exitCode"

# --- Rimuovi file temporaneo ---
if (Test-Path $promptFile) { Remove-Item $promptFile -Force }

if ($exitCode -eq 0) {
    Log "Post #$($topic.n) generato con successo: $($topic.file)"
} else {
    Log "ERRORE durante la generazione del post. Controlla il log."
}

Log "===== FINE GENERAZIONE ====="
exit $exitCode
