---
title: Template e Guida di Stile per gli Appunti ISE
type: template
---

# Template di Stile per Appunti Intelligent System Engineering

Questo documento definisce lo stile, la struttura e le convenzioni per mantenere coerenza in tutti gli appunti del corso.

---

## Struttura Generale di Ogni Modulo

### 1. Frontmatter (YAML)

```yaml
---
title: [Numero]. [Titolo Descrittivo]
date: YYYY-MM-DD
tags:
  - visione-artificiale
  - modulo-[numero]
  - [categoria: fondamenti/applicazioni/tecnica]
aliases:
  - [Nome alternativo breve]
---
```

**Regole**:
- Il titolo deve essere descrittivo e conciso
- Tags sempre: `intelligent-system-eng` + `modulo-XX` + categoria
- Alias per facilitare i wikilink

### 2. Indice del Modulo

Subito dopo il link alle slide, si inserisce un callout `[!abstract]` con l'indice del modulo come wikilink alle sezioni interne:

```markdown
> [!abstract] Indice
> - [[#Sezione Principale 1]]
>   - [[#Sottosezione 1a]]
>   - [[#Sottosezione 1b]]
> - [[#Sezione Principale 2]]
>   - [[#Sottosezione 2a]]
> - [[#Sezione Principale 3]]
```

**Regole**:
- Usa SEMPRE il callout `[!abstract]` con titolo "Indice"
- Ogni voce è un wikilink alla sezione corrispondente (`[[#Nome Sezione]]`)
- Due livelli di profondità: H2 come voci principali, H3 come indentate
- Segui il separatore `---` dopo l'indice

### 3. Definizioni Fondamentali (H2)

Struttura per ogni concetto:

```markdown
### [Nome Concetto] (H3)

> [!info] Definizione
> La **[termine]** è [definizione formale breve e precisa].

**In pratica**: [Spiegazione intuitiva con analogi o esempi semplici]

#### [Sottoconcetto se necessario]
[Spiegazione di sottoconcetti correlati con bullet points]

---
```

**Regole**:
- Inizia SEMPRE con una definizione formale (callout info)
- Segui con una spiegazione pratica e intuitiva
- Includi almeno un esempio semplice

### 3. Concetti Chiave (H2)

```markdown
## [Titolo Concetto]

> [!note]
> Osservazione o approfondimento importante

**Aspetto 1**: [Spiegazione]
- Punto 1
- Punto 2

**Aspetto 2**: [Spiegazione]
- Punto 1
- Punto 2

---
```

**Regole**:
- Usa callout `[!note]` per informazioni importanti
- Raggruppa concetti correlati
- Usa liste per enumerazioni
- Evita approfondimenti inutili per l'esame

### 4. Sfide/Difficoltà (se presenti)

```markdown
## Perché è Difficile?

> [!warning] Sfide Principali
> [Descrizione sfida principale]

**Esempio**: [Caso concreto che illustra il problema]

---
```

**Regole**:
- Usa callout `[!warning]` per sfide
- Usa `[!danger]` per punti critici
- Illustra con esempi visivi o pratici

### 5. Approcci/Soluzioni (se presenti)

```markdown
## [Approccio A] vs [Approccio B]

### [Approccio A]
- Vantaggio 1
- Vantaggio 2
- Svantaggio 1

### [Approccio B]
- Vantaggio 1
- Vantaggio 2
- Svantaggio 1

---
```

**Regole**:
- Confronta i diversi approcci
- Includi pro e contro
- Spiega quando usare uno vs l'altro

### 6. Applicazioni Pratiche (opzionale)

```markdown
## Applicazioni Pratiche

### Categoria: [Nome Categoria]

**[Sottocategoria]**:
- Applicazione 1: breve descrizione
- Applicazione 2: breve descrizione

---
```

**Regole**:
- Organizza per categoria
- Includi casi d'uso reali
- Descrizioni brevi e pratiche

### 7. Prossimi Argomenti (sempre H2)

```markdown
## Prossimi Argomenti

Continueremo con:
- [[NN. Titolo Modulo|Nome Breve]] - breve descrizione
- [[NN. Titolo Modulo|Nome Breve]] - breve descrizione

---
```

**Regole**:
- Usa SEMPRE wikilinks ai moduli successivi
- Includi breve descrizione di cosa tratteranno
- Aiuta la navigazione tra i moduli

---

## Stile Linguistico

### Tono
- Intuitivo e pratico
- Linguaggio naturale ma preciso
- Evita gerghi tecnici senza spiegazione
- Usa analogie dal mondo reale

### Esempi
- Includi almeno un esempio per ogni concetto principale
- Semplici e concreti (non astratti)
- Reali quando possibile (visi, lettere, immagini)
- Uno o due è abbastanza, non esagerare

### Cosa Includere
✓ Definizioni chiare
✓ Spiegazioni intuitive
✓ Esempi pratici
✓ Pro e contro
✓ Applicazioni nel mondo reale
✓ Wikilink ai moduli correlati

### Cosa Escludere
✗ Emoji
✗ Formalismo eccessivo (formule complesse senza necessità)
✗ Approfondimenti inutili per l'esame
✗ Digressioni su argomenti marginali
✗ Troppi dettagli implementativi

---

## Callout Obsidian Disponibili

| Tipo | Uso | Quando |
|------|-----|--------|
| `[!info]` | Definizioni formali | All'inizio di ogni concetto |
| `[!note]` | Approfondimenti | Per punti importanti da ricordare |
| `[!example]` | Esempi pratici | Per illustrare un concetto |
| `[!warning]` | Avvertenze/Sfide | Per difficoltà o problemi |
| `[!danger]` | Punti critici | Per cose **essenziali** da capire |
| `[!tip]` | Best practices | Per consigli pratici |

**Regola**: Non abusare, usa solo quando serve davvero a mettere in evidenza.

---

## Link Interni (Wikilinks)

### Quando Lineare
- A moduli correlati
- A concetti spiegati in altri moduli
- A sezioni specifiche di un modulo

### Come Scrivere

```markdown
[[Nome Modulo]]              # Link semplice
[[Nome Modulo|Testo]]        # Link con display text
[[Nome Modulo#Heading]]      # Link a sezione specifica
```

**Regola**: Usa display text breve quando il nome è lungo.

---

## Formattazione Testo

```markdown
**concetto chiave**         # Bold per enfasi
==concetto importante==     # Highlight per evidenza
`codice_o_variabile`        # Code per riferimenti tecnici
```

**Regola**: Usa bold per termini, highlight per cose da ricordare.

---

## Lunghezza e Densità

- **Paragrafi**: Brevi, 2-4 frasi max
- **Sezioni**: 2-5 paragrafi
- **Modulo completo**: 1500-2500 parole approssimativamente
- **Densità**: Spiegazioni chiare ma concise

---

## Checklist per Ogni Modulo

Prima di considerare finito un modulo:

- [ ] Frontmatter completo con title, date, tags, aliases
- [ ] Definizioni fondamentali con callout info
- [ ] Spiegazioni intuitive (non formali)
- [ ] Almeno un esempio per concetto principale
- [ ] Sezioni con callout appropriati (note, warning, example, etc.)
- [ ] NO emoji
- [ ] Wikilinks ai moduli correlati
- [ ] Link alla slide PDF all'inizio
- [ ] Prossimi argomenti con wikilinks
- [ ] Niente approfondimenti inutili per l'esame

---

## Esempio Completo di Sezione

```markdown
### Pattern Recognition (PR) - Riconoscimento di Forme

> [!info] Definizione
> Il **Pattern Recognition** è una delle più importanti sotto-discipline della VA.
> In italiano viene tradotto come "**Riconoscimento di Forme**".

**In pratica**: Significa insegnare al computer a riconoscere e classificare
cose diverse - come un bambino impara a riconoscere che una cosa è una
"mela" indipendentemente dal colore, forma esatta, o angolazione.

#### Che cosa è un Pattern?

Secondo **Watanabe**, un pattern è:
- **L'opposto del caos** - qualcosa di cui puoi dare un nome
- **Qualcosa di riconoscibile** - potrebbe essere un volto, una firma, un'impronta

**Esempi**:
- Il tuo viso è un pattern visivo
- La tua firma è un pattern di tratti
- Un'impronta digitale è un pattern biometrico
```

---

## Note di Implementazione

Quando generi appunti per un nuovo modulo:

1. Leggi le slide PDF associate
2. Estrai i concetti principali dall'indice
3. Segui la struttura di cui sopra
4. Usa il tono intuitivo-pratico
5. Includi esempi semplici
6. Aggiungi wikilink ai moduli correlati
7. Rimuovi emoji
8. Verifica con la checklist

**Ordine**: Definizioni → Concetti chiave → Sfide (se presenti) → Applicazioni → Prossimi
