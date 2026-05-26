---
title: Lab. STRIPS
date: 2026-05-25
tags:
  - intelligent-system-eng
  - lab-strips
  - laboratorio
aliases:
  - STRIPS
  - Planning in STRIPS with Prolog
---

# Lab. STRIPS

Slide: <file:///C:/UNI/Magistrale/ISE/Lab/ise-lab-strips.pdf>

> [!abstract] Indice
> - [[#Obiettivo del Lab STRIPS]]
> - [[#Modello STRIPS]]
>   - [[#Stati e Goal]]
>   - [[#Azioni]]
> - [[#Rappresentazione in Prolog]]
> - [[#Applicazione delle Azioni]]
> - [[#Algoritmo STRIPS]]
> - [[#Choice Point e IDDFS]]
> - [[#Prossimi Argomenti]]

---

## Obiettivo del Lab STRIPS

> [!info] Definizione
> **STRIPS** è uno dei primi approcci di successo al planning automatico, basato su stati, azioni con precondizioni ed effetti, e ricerca di un piano che raggiunga un goal.

Il laboratorio usa Prolog per implementare un planner STRIPS. Il repository indicato è `https://github.com/unibo-fc-isi-ise/code-strips`, con un sottoprogetto `strips` che contiene file `.pl` come `Strips.pl`, `Utils.pl` e mondi di esempio come `BlockWorld.pl`.

**In pratica**: si impara a rappresentare problemi di pianificazione in modo simbolico e a costruire un algoritmo che cerca una sequenza di azioni valida.

---

## Modello STRIPS

### Stati e Goal

> [!info] Definizione
> Uno **stato STRIPS** è un insieme di fluenti ground, cioè fatti logici veri in quel momento.

STRIPS usa la **Closed World Assumption**: ciò che non è esplicitamente presente nello stato è considerato falso o non noto come vero.

Un goal è anch'esso un insieme di fluenti. Il goal vale in uno stato se tutti i fluenti del goal sono contenuti nello stato:

```text
G holds in S <=> G subseteq S
```

> [!example] Esempio
> Nel Block World, uno stato può contenere `ontable(b)`, `on(a,c)`, `clear(a)` e `holding(d)`. Questo descrive blocchi sul tavolo, blocchi impilati e mano robotica.

### Azioni

> [!info] Definizione
> Un'**azione STRIPS** è una quadrupla `<N, P, A, D>`, dove `N` è il nome, `P` sono le precondizioni, `A` è la add list e `D` è la delete list.

L'ipotesi STRIPS è semplice: tutto ciò che non è in add list o delete list rimane invariato. Questo evita il frame problem nella sua forma più pesante.

Un'azione è applicabile se le sue precondizioni unificano con un sottoinsieme dello stato corrente. Applicarla significa rimuovere gli effetti negativi e aggiungere quelli positivi:

```text
apply(S1, action) = (S1 - D/theta) union A/theta
```

---

## Rappresentazione in Prolog

> [!info] Definizione
> Nel laboratorio, le azioni STRIPS sono rappresentate come fatti Prolog della forma `action(N, if(P), '+'(A), '-'(D)).`

Esempio semplificato per `stack(X,Y)`:

```prolog
action(
    stack(X, Y),
    if([clear(Y), holding(X)]),
    '+'([on(X, Y), clear(X), handempty]),
    '-'([clear(Y), holding(X)])
).
```

Nel Block World le azioni principali sono:
- `stack`: mette un blocco tenuto in mano sopra un blocco libero;
- `unstack`: prende un blocco da sopra un altro blocco;
- `pick`: prende un blocco dal tavolo;
- `put`: mette sul tavolo un blocco tenuto in mano.

> [!note]
> In Prolog gli insiemi sono rappresentati come liste. Questo è comodo, ma richiede funzioni di utilità per subset, union, difference e confronto.

---

## Applicazione delle Azioni

> [!info] Definizione
> La relazione `apply(+State, +ActionName, -NewState)` calcola il nuovo stato ottenuto applicando un'azione applicabile allo stato corrente.

Per implementarla bisogna:
- trovare un fatto `action` con nome compatibile;
- verificare che le precondizioni siano soddisfatte nello stato;
- calcolare lo stato senza delete list;
- aggiungere la add list;
- produrre `NewState`.

> [!example] Esempio
> `apply([ontable(a), clear(a), handempty], pick(a), S)` dovrebbe produrre uno stato in cui la mano tiene `a`, quindi con `holding(a)` e senza `ontable(a)`, `clear(a)` e `handempty` se modellati come effetti negativi.

La libreria `Utils.pl` fornisce operazioni su insiemi come `subset`, `subseteq`, `union`, `intersection`, `difference`, `member` e `in`. Queste non vanno reimplementate: vanno capite e usate.

---

## Algoritmo STRIPS

> [!info] Definizione
> L'**algoritmo STRIPS** costruisce un piano lavorando all'indietro dai goal: se un goal non è già vero, sceglie un'azione che può produrlo e pianifica le precondizioni di quell'azione.

L'algoritmo usa tre strutture:
- **State**: lo stato simulato corrente;
- **Stack**: goal ancora da soddisfare e azioni da applicare;
- **Plan**: azioni già selezionate, da invertire alla fine.

Schema intuitivo:
- se la testa dello stack è già vera nello stato, la si rimuove;
- se può essere prodotta da un'azione, si mette sullo stack l'azione e prima le sue precondizioni;
- se è una congiunzione, la si spezza in sottogoal;
- se è un'azione, la si applica allo stato e la si aggiunge al piano;
- se nessuna regola vale, il tentativo fallisce.

> [!example] Esempio
> Per raggiungere `on(c,b)`, il planner può scegliere `stack(c,b)`. Prima però deve ottenere `holding(c)` e `clear(b)`. Per ottenere `holding(c)`, può scegliere `unstack(c,a)` se `c` è sopra `a`.

---

## Choice Point e IDDFS

> [!warning] Sfide Principali
> I choice point contano molto: scegliere sempre la prima azione disponibile può portare a loop o piani inutili.

Prolog usa ricerca depth-first. Questo può divergere, ad esempio alternando azioni inverse come `stack` e `unstack`, oppure scegliendo infinite volte un'azione sempre applicabile.

Il laboratorio introduce due idee:
- **BadActions trick**: blacklist temporanea per evitare di scegliere sempre la stessa azione;
- **Iterative Deepening Depth-First Search (IDDFS)**: ricerca a profondità crescente, utile quando non si conosce la profondità della soluzione.

> [!info] Definizione
> **IDDFS** combina il basso consumo di memoria della depth-first search con la completezza pratica di una ricerca a profondità limitata crescente.

Con IDDFS, il limite massimo può essere impostato con `max_depth(MD)` e il trucco `BadActions` diventa meno necessario, perché la profondità limita naturalmente cicli e piani troppo lunghi.

---

## Prossimi Argomenti

Collegamenti utili:
- [[Lab. Jason|Jason]] - agenti intenzionali che possono usare planning e azioni simboliche.
- [[S3. Towards Agent Explainability|Agent Explainability]] - spiegare azioni in termini di obiettivi, intenzioni e policy.
- [[Lab. About|About Lab]] - indicazioni su esercizi, repository e progetto finale.

---
