---
title: Project 2026
date: 2026-05-18
tags:
  - operational-analytics
  - project-2026
  - esame
aliases:
  - Exam Project 2026
  - Progetto Operational Analytics 2026
---

# Project 2026

[Slide PDF](<file:///C:/UNI/Magistrale/OperationalAnalytics/project%202026.pdf>)

> [!abstract] Indice
> - [[#Obiettivo del Progetto]]
> - [[#Requisiti del Progetto]]
>   - [[#Contenuto Minimo]]
>   - [[#Requisiti Tecnici]]
> - [[#Dataset e Scelta del Caso di Studio]]
>   - [[#Progetto Standard]]
>   - [[#Progetto Avanzato o Custom]]
> - [[#Consegne e Discussione]]
> - [[#Workflow Consigliato]]
> - [[#Valutazione]]
> - [[#Consigli Pratici]]
> - [[#Errori da Evitare]]
> - [[#Collegamenti ai Moduli Utili]]

---

## Obiettivo del Progetto

> [!info] Definizione
> Il **progetto d'esame** consiste nella presentazione e discussione del codice di un progetto di **forecasting** collegato agli argomenti trattati durante il corso.

**In pratica**: bisogna costruire un piccolo studio predittivo completo, partendo dai dati, preparando le serie temporali, applicando piu modelli di previsione e confrontando i risultati in modo statistico.

Il progetto non e solo implementativo: durante l'esame bisogna saper spiegare le scelte fatte, il comportamento dei modelli, la qualita del codice e il significato dei risultati ottenuti.

---

## Requisiti del Progetto

### Contenuto Minimo

Il progetto deve includere:
- **data preprocessing** e **exploratory analysis**;
- implementazione di almeno **tre algoritmi di forecasting**;
- valutazione e confronto statistico delle performance predittive.

I tre algoritmi devono coprire queste famiglie:
- **un metodo statistico**: AR, ARMA, ARIMA, SARIMA, SARIMAX, Holt-Winters oppure theta;
- **un metodo basato su reti neurali**: MLP, LSTM oppure transformer;
- **un metodo basato su regression tree**: random forest oppure XGBoost.

> [!danger] Punto essenziale
> Il progetto deve confrontare famiglie diverse di modelli. Usare tre varianti della stessa famiglia non soddisfa il requisito indicato nel PDF.

### Requisiti Tecnici

Il progetto deve essere implementato in **Python**.

Requisiti espliciti:
- i **Jupyter notebook non sono permessi**;
- la consegna deve consistere in **script Python eseguibili**;
- gli script devono funzionare sulle **macchine del laboratorio** e sul **server del docente**;
- si possono usare solo le librerie impiegate durante il corso, incluse `pandas`, `numpy`, `matplotlib` e le librerie citate nelle slide;
- librerie aggiuntive devono essere approvate dal docente prima della consegna.

> [!warning] Robustezza
> Il codice non deve funzionare solo sul proprio computer. Percorsi locali, dipendenze non dichiarate o librerie non autorizzate possono rendere il progetto non eseguibile nell'ambiente richiesto.

---

## Dataset e Scelta del Caso di Studio

### Progetto Standard

La versione standard richiede di applicare i tre algoritmi di forecasting a **due serie temporali** selezionate dai dataset **M3**, **M4** oppure **M5**.

Le due serie devono appartenere a **due domini diversi**, per esempio:
- microeconomia;
- macroeconomia;
- industria;
- altri domini presenti nei dataset indicati.

> [!note]
> I progetti basati su dataset standard o dataset pubblici ampiamente disponibili ricevono generalmente voti fino a **27/30**.

### Progetto Avanzato o Custom

Voti piu alti possono essere ottenuti con progetti basati su:
- dataset originali;
- dati legati a interessi personali o professionali dello studente;
- case study proposti autonomamente dagli studenti e rilevanti per gli argomenti del corso.

I progetti piu avanzati possono essere sviluppati in gruppi fino a **tre studenti**. Tuttavia:
- la discussione e la valutazione restano **individuali**;
- tutte le soluzioni consegnate devono essere eseguibili sulle macchine del laboratorio e sul server del docente.

> [!tip] Scelta del tema
> Un buon caso di studio non e solo originale: deve permettere di applicare davvero forecasting, preprocessing, confronto tra modelli e valutazione statistica.

---

## Consegne e Discussione

La consegna deve contenere codice Python eseguibile, non notebook. Il PDF non indica una scadenza specifica ne un formato dettagliato di cartella, quindi questi aspetti vanno verificati con il docente se non gia comunicati altrove.

Durante la prova finale e prevista la **presentazione e discussione del codice**. Bisogna quindi essere pronti a spiegare:
- perche sono state scelte quelle serie temporali;
- quali trasformazioni e controlli sono stati applicati ai dati;
- come sono stati configurati i tre modelli;
- quali metriche e test statistici sono stati usati;
- cosa mostrano i risultati e quali limiti hanno.

Per studenti con difficolta di programmazione, il PDF consente di concentrarsi maggiormente sull'analisi e sulla discussione di case study rilevanti. Rimane comunque richiesto un **livello minimo di implementazione**.

---

## Workflow Consigliato

### 1. Definire il Caso di Studio

Scegliere prima il tipo di progetto:
- **standard**, se si usano M3, M4 o M5 con due serie di domini diversi;
- **custom**, se si propone un dataset originale o legato a un interesse personale/professionale.

Verificare subito che i dati siano adatti al forecasting: devono avere ordine temporale, frequenza interpretabile e abbastanza osservazioni per separare addestramento e test.

### 2. Preparare i Dati

Attivita tipiche:
- caricamento e pulizia dei dati;
- controllo di valori mancanti, duplicati e anomalie;
- gestione della frequenza temporale;
- separazione ordinata tra train e test, senza mescolare futuro e passato;
- analisi esplorativa con grafici e statistiche descrittive.

### 3. Implementare i Modelli

Organizzare il codice in modo semplice e ripetibile:
- una pipeline comune per preprocessing e split;
- una funzione o script per ogni famiglia di modello;
- una procedura unica per salvare previsioni e metriche;
- parametri chiari, evitando valori nascosti nel codice.

I modelli minimi da coprire sono:
- statistico: ARIMA, SARIMA, Holt-Winters, theta o alternativa ammessa;
- neurale: MLP, LSTM o transformer;
- tree-based: random forest o XGBoost.

### 4. Valutare e Confrontare

La valutazione deve permettere un confronto corretto delle performance predittive. Conviene usare le stesse finestre temporali, le stesse serie e metriche coerenti per tutti i modelli.

> [!note]
> Il PDF richiede una valutazione e un confronto statistico delle performance. Le metriche e i test specifici non sono indicati nel documento, quindi vanno scelti in modo coerente con quanto visto nel corso.

### 5. Preparare la Discussione

Prima dell'esame, controllare di saper spiegare:
- struttura del codice;
- scelte di preprocessing;
- scelta dei modelli;
- risultati principali;
- differenze tra le famiglie di metodi;
- limiti del progetto.

---

## Valutazione

> [!info] Criteri
> Il voto finale si basa sui criteri elencati nel PDF del progetto.

Criteri di valutazione indicati:
- originalita e rilevanza del case study;
- qualita e correttezza delle metodologie di forecasting;
- semplicita, qualita e robustezza dell'implementazione software;
- valutazione statistica e confronto dei risultati;
- chiarezza e qualita della presentazione;
- complessita del progetto rispetto alla dimensione del gruppo;
- eventuali bonus di partecipazione ottenuti durante il corso.

---

## Consigli Pratici

> [!tip] Strategia
> Meglio un progetto semplice, eseguibile e ben spiegato di un progetto molto complesso ma fragile.

Consigli operativi:
- iniziare da un baseline semplice prima dei modelli piu complessi;
- mantenere la stessa procedura di valutazione per tutte le famiglie di modelli;
- salvare risultati intermedi solo se rendono piu facile riprodurre l'esecuzione;
- evitare dipendenze non necessarie;
- scrivere codice leggibile, con nomi chiari e pochi passaggi manuali;
- preparare grafici che aiutino la discussione, non solo tabelle di numeri;
- verificare l'esecuzione completa degli script in un ambiente pulito.

---

## Errori da Evitare

> [!warning] Errori comuni
> Gli errori piu rischiosi sono quelli che compromettono eseguibilita, confronto corretto o aderenza ai requisiti del PDF.

Da evitare:
- consegnare notebook invece di script Python;
- usare librerie non viste nel corso senza approvazione;
- testare i modelli su dati usati anche per l'addestramento;
- confrontare modelli su split o metriche diverse;
- scegliere serie temporali senza spiegare dominio, frequenza e significato;
- presentare solo grafici senza confronto statistico;
- puntare solo alla complessita del modello trascurando robustezza e chiarezza del codice;
- in un gruppo, non saper discutere individualmente il progetto.

---

## Collegamenti ai Moduli Utili

Moduli direttamente collegati al progetto:
- [[Operational Analytics/01. Predictive Analytics|Predictive Analytics]] - inquadramento del forecasting e del processo predittivo.
- [[Operational Analytics/02. Predictive Data Preprocessing|Predictive Data Preprocessing]] - preparazione dei dati, trasformazioni e gestione delle variabili.
- [[Operational Analytics/03. Predictive Statistical Models|Predictive Statistical Models]] - AR, ARMA, ARIMA, SARIMA, SARIMAX, Holt-Winters e theta.
- [[Operational Analytics/04. Predictive Neural Models|Predictive Neural Models]] - MLP, LSTM e modelli neurali per serie temporali.
- [[Operational Analytics/05. Predictive Machine Learning Models|Predictive Machine Learning Models]] - modelli tree-based come random forest e XGBoost.
- [[Operational Analytics/06. Statistics Descriptive|Statistics Descriptive]] - analisi esplorativa e descrizione dei dati.
- [[Operational Analytics/07. Statistics Inferential|Statistics Inferential]] - confronto statistico e interpretazione dei risultati.

---
