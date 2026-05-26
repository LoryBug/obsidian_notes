---
title: Lab. About
date: 2026-05-25
tags:
  - intelligent-system-eng
  - lab-about
  - laboratorio
aliases:
  - About the Lab
  - Laboratorio ISE
---

# Lab. About

Slide: <file:///C:/UNI/Magistrale/ISE/Lab/ise-lab-about.pdf>

> [!abstract] Indice
> - [[#Obiettivo del Laboratorio]]
> - [[#Tecnologie Richieste]]
> - [[#Esercizi e Modalità di Lavoro]]
> - [[#Progetto Finale]]
> - [[#Tipi di Progetto]]
> - [[#Prossimi Argomenti]]

---

## Obiettivo del Laboratorio

> [!info] Definizione
> Il **laboratorio di Intelligent Systems Engineering** è la parte pratica del corso dedicata alla progettazione, programmazione e valutazione di sistemi agentivi e tecnologie correlate.

Storicamente il modulo copriva logica computazionale, programmazione logica, agenti BDI in Jason, planning simbolico con STRIPS e temi come argomentazione o XAI. Nell'anno corrente il focus include:
- agenti BDI e programmazione in Jason;
- planning simbolico e STRIPS;
- fondamenti di tecnologie per agenti basati su LLM, come API, tool e structured outputs.

**In pratica**: il laboratorio collega la teoria sugli agenti intelligenti con strumenti concreti per costruire, testare e discutere sistemi software.

---

## Tecnologie Richieste

Le competenze considerate necessarie sono:
- **Git e DVCS**, per lavorare su repository, fork, branch e pull request;
- **Gradle**, per automatizzare build ed esecuzione;
- **programmazione a oggetti su JVM 17+**, soprattutto Java o Kotlin;
- **Python 3.10.x**, con strumenti come Pip, Virtualenv, Pyenv e librerie come scikit-learn.

Sono utili anche scripting shell di base e configurazione autonoma dell'IDE. VS Code, IntelliJ o Eclipse sono accettabili: l'importante è saper aprire progetti, lanciare task e leggere errori.

> [!tip]
> Il laboratorio non valuta l'IDE scelto. Valuta la capacità di riprodurre il progetto, capirne la struttura e lavorare in modo ordinato.

---

## Esercizi e Modalità di Lavoro

> [!info] Definizione
> Gli **esercizi di laboratorio** sono attività pratiche opzionali pensate per costruire competenze utili al progetto finale.

Gli esercizi possono iniziare durante la lezione e non essere completati subito. L'aspettativa è che lo studente li completi autonomamente, chiedendo aiuto sul forum e confrontandosi con i colleghi.

Regole operative:
- non c'è deadline o voto sugli esercizi;
- le soluzioni non vanno inviate come zip o snippet isolati;
- il codice va gestito tramite repository Git;
- per proporre soluzioni si usa fork e pull request;
- richieste generali, dubbi e commenti vanno preferibilmente sul forum.

> [!note]
> Lo scopo è imparare, non risolvere puzzle. Un esercizio incompleto ma compreso bene vale più di una soluzione copiata e non capita.

---

## Progetto Finale

Il workflow del progetto è:
- scegliere un progetto o proporne uno;
- aprire un post sul forum Projects per prenotarlo o proporlo;
- attendere approvazione;
- creare un repository Git e pubblicarne l'URL;
- sviluppare il progetto;
- scrivere il report finale;
- inviare il PDF del report sul forum Projects;
- fissare un appuntamento per la discussione.

I progetti di gruppo sono ammessi fino a 4 persone. La regola indicativa è circa 90 ore di lavoro per persona.

---

## Tipi di Progetto

Le categorie principali sono:
- **Classic ISE Project**: progettare e sviluppare un artefatto software basato su MAS o logic programming, con design solido, implementazione completa e test pervasivi.
- **Advanced ISE Project**: implementare un framework scientificamente rilevante dalla letteratura, anche con prototipo non perfetto ma design convincente.
- **Research ISE Project**: sviluppare una feature o idea di ricerca con prototipo ed eventuale valutazione empirica; richiede pratiche software mature.
- **Systematic Literature Review**: produrre un report scientifico su un obiettivo di ricerca, con esplorazione bibliografica riproducibile e conclusioni chiare.

> [!example] Esempio
> Un progetto STRIPS completo e testato può essere un Classic ISE Project. Un prototipo di framework per agenti LLM tratto da un paper recente può essere Advanced. Una SLR su explainability per agenti BDI ricade nella categoria Systematic Literature Review.

---

## Prossimi Argomenti

Continueremo con:
- [[Lab. Jason|Jason]] - programmazione di agenti intenzionali in AgentSpeak(L)/Jason.
- [[Lab. STRIPS|STRIPS]] - planning simbolico e implementazione in Prolog.
- [[S2. Systematic Literature Review|SLR]] - metodo utile per la categoria di progetto bibliografica.

---
