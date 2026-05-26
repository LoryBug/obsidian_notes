---
title: Lab. Jason
date: 2026-05-25
tags:
  - intelligent-system-eng
  - lab-jason
  - laboratorio
aliases:
  - Jason
  - Programming Intentional Agents
---

# Lab. Jason

Slide: <file:///C:/UNI/Magistrale/ISE/Lab/ise-lab-jason.pdf>

> [!abstract] Indice
> - [[#Obiettivo del Lab Jason]]
> - [[#Struttura di un MAS Jason]]
> - [[#Basi di AgentSpeak(L)]]
>   - [[#Goal Piani e Guardie]]
>   - [[#Belief Base e Test Goals]]
> - [[#Interazione tra Agenti]]
> - [[#Percezione e Attuazione]]
> - [[#Esercizi Significativi]]
> - [[#Prossimi Argomenti]]

---

## Obiettivo del Lab Jason

> [!info] Definizione
> **Jason** è una piattaforma per programmare sistemi multi-agente in AgentSpeak(L), un linguaggio orientato ad agenti BDI basato su credenze, obiettivi e piani.

Il laboratorio mostra come realizzare agenti intenzionali, cioè agenti che reagiscono a eventi, perseguono goal, mantengono credenze e interagiscono con altri agenti e con l'ambiente.

Nel corso non si segue l'installazione manuale classica di Jason. Si usa Gradle per rendere l'esecuzione riproducibile e si evita la dipendenza dal vecchio plugin Eclipse. Il repository principale degli esercizi è `https://github.com/unibo-fc-isi-ise/code-jason`.

> [!tip]
> Per ogni file `X.mas2j`, Gradle definisce un task del tipo `runXMas`, che avvia il MAS corrispondente.

---

## Struttura di un MAS Jason

> [!info] Definizione
> Un **MAS Jason** è descritto da un file `.mas2j`, che specifica infrastruttura, agenti, file AgentSpeak e, se presente, ambiente.

Esempio minimale:

```asl
MAS helloworld {
    infrastructure: Centralised

    agents:
        agent1 hello_agent;

    aslSourcePath: "src/main/asl";
}
```

Un file `.asl` contiene:
- credenze iniziali e regole;
- goal iniziali;
- piani che reagiscono a eventi.

Esempio "hello world":

```asl
!start.

+!start : true <- .print("hello world").
```

**In pratica**: il MAS definisce chi esiste; il file `.asl` definisce come ragiona e agisce ciascun agente.

---

## Basi di AgentSpeak(L)

### Goal Piani e Guardie

> [!info] Definizione
> Un **piano** Jason specifica come reagire a un evento, eventualmente solo quando una guardia logica è soddisfatta.

La forma generale è:

```asl
+!goal(Arg) : Condizione <- Azione1; Azione2; !SottoGoal.
```

Concetti fondamentali:
- `!goal` indica un achievement goal, cioè qualcosa da ottenere;
- `?goal` indica un test goal, cioè una richiesta di conoscenza;
- la guardia dopo `:` seleziona quando il piano è applicabile;
- i piani sono scelti tramite unificazione logica;
- `;` separa sottogoal e azioni, mentre `.` termina il piano.

Jason supporta ricorsione, `while`, `for`, `if-then-else` e gestione dei fallimenti. La ricorsione resta però il mattone concettuale per comportamenti lunghi.

> [!example] Esempio
> Un agente può contare ricorsivamente da 0 a 10 usando due piani: uno per il caso base e uno per il passo ricorsivo. Le guardie decidono quale piano è selezionabile.

### Belief Base e Test Goals

> [!info] Definizione
> La **belief base** è l'insieme di credenze e regole logiche che l'agente usa per ragionare.

Le credenze possono essere aggiornate con operazioni come aggiunta, rimozione e aggiornamento atomico. I test goal interrogano la belief base o attivano piani specifici per ottenere informazione.

Un pattern ricorrente è usare la belief base come memoria. Nell'esercizio Fibonacci, ad esempio, si suggerisce di salvare valori già calcolati per evitare ricalcoli inefficienti.

---

## Interazione tra Agenti

> [!info] Definizione
> L'**interazione in Jason** avviene tramite messaggi con forza illocutoria, cioè un'etichetta che specifica il significato pragmatico del messaggio.

Azioni interne principali:
- `.send/3` e `.send/5` per messaggi punto-a-punto;
- `.broadcast/2` per inviare a tutti;
- `.wait` per sospendere un'intenzione fino a un evento, una query o un timeout.

Forze illocutorie importanti:
- `tell`: il mittente vuole che il ricevente creda un fatto;
- `untell`: il mittente vuole rimuovere una credenza;
- `achieve`: il mittente chiede di perseguire un goal;
- `askOne` e `askAll`: il mittente chiede risposte a query;
- `tellHow` e `askHow`: scambio di piani.

> [!example] Esempio
> Nel ping-pong asincrono, un agente invia `ball` con `.send(Receiver, tell, ball)`. Il ricevente vede una credenza annotata con `source(Sender)` e può rispondere con un altro messaggio.

---

## Percezione e Attuazione

> [!info] Definizione
> In Jason, la **percezione** è gestita come aggiornamento automatico di credenze, mentre l'**attuazione** avviene tramite azioni che l'ambiente implementa.

I percetti hanno forma logica, ad esempio:

```asl
temperature(19.7)[source(percept)]
```

Dal punto di vista dell'agente sono credenze normali. Dal punto di vista dell'ambiente, bisogna decidere quali percetti ogni agente può vedere e quando.

Le azioni sono termini nei piani, ad esempio `spray_air(hot)`. Se l'ambiente riconosce l'azione, può eseguirla e produrre effetti; se non la riconosce o fallisce, il piano fallisce.

> [!example] Esempio
> Nel termostato, l'agente percepisce `temperature(T)` e sceglie `spray_air(cold)` o `spray_air(hot)` per mantenersi vicino a 20 gradi. Non serve un loop esplicito: i nuovi percetti generano nuovi eventi.

---

## Esercizi Significativi

Gli esercizi coprono:
- programmazione pura AgentSpeak(L) con ricorsione e guardie;
- gestione dei fallimenti con piani `-!goal`;
- più intenzioni concorrenti nello stesso agente;
- messaggi asincroni, sincroni e request-response;
- broadcast e scoperta di agenti;
- ambienti custom in Java;
- scenario "Rescue the Lost Robot" con percezioni, vincoli di comunicazione, movimento e coordinate relative.

> [!warning] Punto Critico
> Le intenzioni Jason non sono thread Java. Sono unità di esecuzione interne all'agente, schedulate in modo cooperativo. Questo evita una parte della complessità, ma richiede di ragionare bene su eventi, piani e interleaving.

---

## Prossimi Argomenti

Continueremo con:
- [[Lab. STRIPS|STRIPS]] - planning simbolico in Prolog e rappresentazione di azioni con precondizioni ed effetti.
- [[S3. Towards Agent Explainability|Agent Explainability]] - spiegazione di comportamenti agentivi e intenzioni attribuite.
- [[Lab. About|About Lab]] - regole operative, esercizi e progetto finale.

---
