### Cbir, semantic gap e relevance feedback
Cbir, ovvero Context based Image retrieval è una tecnica che permette di recuperare le immagine in base al contenuto visivo di una determinata immagine.
L'architettura del sistema è spesso fatta da 3 parti:
1. estrattore di feature, ogni immagine del dataset viene trasformato in un vettore numerico di feature sia tradizionali, locali e deep
2. query engine, confronta le immagine del dataset con quelle proposte dall'utente, vari tipi di query come query by example, by sketch e anche keywords
3. interfaccia utente che consenta iterazione e feedback con utente finale
Il problema principale dei sistemi CBIR è il semantica gap ovvero la discrepanza che l'utente trova tra quello che lui intende come somiglianza semantica e quella che le varie feature estraggono dalla immagini come bordi, colori e altro. Ad esempio gli edifici di oxford sono spesso con lo stesso stile architettonico e colori simili, in questo modo le feature rappresentano edifici diversi in maniera simile perché non in grado di generalizzare e avere un contesto semantico adeguato.
Per venire in contro a questo problema sono nati algoritmi di relevance feedback, che attraverso il feedback dell'utente consentono di migliorare i risultati delle query in modo iterativo, i modi principali in cui funzionano questi sistemi sono due:
* query point movement, si sposta il vettore query verso gli esempi che sono risultati positivi
* re-weighting, si cambiano i pesi delle feature per rendere più discriminanti le migliori
Alcuni di questi algoritmi sono per esempio Rocchio (q.p.e), MARS (q.p.e + r.w) e Mind reader.
### Metriche di valutazione per retrieval e classificazione
Per valutare le prestazione del retrieval mi sono appoggiato a varie indicatori come average precision, per valutare prestazione su singola query, mean AP per valutare su tutte le query e avere una media delle prestazioni su tutte le query, inoltre ho deciso di utilizzare anche la P@k ovvero la precisione ad un determinato valore k(1-5-10) che consente di misurare la frazione di immagini rilevanti tra i primi k risultati.
L'uso di mAP e P@k è per mostrare la stabilità delle risposte del modello, infatti consente di andare oltre la riposta secca che per qualsiasi motivo può essere giusta ma allunga l'osservazione dei risultati su k valori, rendendo anche più validi i risultati ottenuti.
Per misurare la distanza dei vari vettori, e quindi la metrica di similarità, fatti alla base delle varie feature ho usato diversi metodi:
- Intersezione per color histogram
- Distanza chi-squared per LBP, che valuta differenza tra due distribuzioni di frequenza
- Coseno per tutte le altre
### Feature
Le feature sono caratteristiche estratte dalla immagini, solitamente si punta ad avere feature invarianti in questo modo rimangono costanti rispetto a trasformazioni, cambi di luminosità, cambi scala e prospettiva. Le feature possono essere scelte a mano nel caso delle Hand-crafted feature (colore, forma, texture) oppure apprese automaticamente da reti neurali e in questo caso vengono chiamate representation learning.
#### Colore
La prima e più semplice è sicuramente il **color histogram**, nel nostro caso si è scelto un unico istogramma 3d che riesce anche a mantenere una certa correlazione relativa ai canali, in pratica si rappresenta la distribuzione dei colori quantizzando i canali nello spazio colori in bin e si conta quanti pixel cadono in ciascun bin, il problema principale di questa tecnica è che non tiene conto della disposizione spaziale dei pixel. Un altro descrittore per le feature di colore sono i **color moments** ovvero descrittori statistici che trattano la distribuzione del colore come una distribuzione di probabilità, calcolando moda, deviazione standard e skewness.
#### Texture
Si passa poi alle feature di texture, come più semplice nel progetto abbiamo scelto **Local Binary pattern** che consente in maniera efficiente di descrivere la texture locale attraverso una stringa binaria confrontando un pixel con il suo intorno (1 se maggiore del pixel centrale, 0 altrimenti), nel nostro caso abbiamo usato la versione circolare con P=24 e R=3 dove P è il numero di punti campione sul cerchio e R è il raggio dell'intorno circolare, abbiamo ingrandito la zona di ricerca perché i pattern architetturali sono più ampi di solo qualche pixel. Abbiamo considerato solo i pattern uniformi ovvero con al massimo due transizione 0/1 per catturare solo le strutture locali più significative.
Uno molto simile è il **Binarized Statistical Image Features (BSIF)** dove i filtri sono appresi via ICA invece di essere regole fisse.
Un altro metodo sono le **matrici di co-occorrenza (GLCM)** ovvero istogrammi 2D che descrivono con quale frequenza due livelli di grigio compaiono vicini secondo una direzione e una distanza specificata.
Esiste poi l'approccio a **banchi di filtri** che applica all'immagine una serie di filtri e ne estrae indicatori statistici, per generare il banco si discretizzano varie orientazioni e scale e si applica la convoluzione che produce una serie di vettori feature che sono poi concatenati.
Le **Haar Like features** sono maschere binarie rettangolari che codificano variazioni di intensità luminosa, sono molto efficienti grazie all'utilizzo dell'immagine integrale che dice che ogni elemento di un rettangolo è la somma di tutti i pixel sopra e a sinistra e viene calcolato in una sola passata con formule ricorsive.
#### Forma
Si parte dall'estrazione del contorno, poi si applicano varie tecniche come ad esempio la **chain code** che rappresenta il contorno come una sequenza di direzioni (4/8) di spostamento tra pixel adiacenti. Si passa poi alla **Shape matrix** ovvero una matrice binaria MxN che descrive se ciascuna cella della griglia sovrapposta alla forma contiene o meno una porzione significativa dell'oggetto.
Il **Beam Angle Statistics** descrive la forma locale di ciascun punto del contorno misurando l'angolo tra i raggi che collegano quel punto ai suoi vicini di distanza k.
Le **Shape signatures** sono funzioni 1D derivate dalle coordinate del contorno che forniscono una descrizione della forma, alcune sono:
- complex coordinate, ogni punto del contorno diventa un numero complesso relativo al centroide
- centroid distance function, per ogni punto si calcola distanza dal centroide
- area function, area del triangolo formati da due punti consecutivi del contorno e il centroide
#### Feature locali
Per le feature locali è stato scelto **SIFT (Scale Invariant Feature Transform)** è il descrittore locale più noto, combina localizzatore basato su Difference of Gaussian (DoG) con un descrittore robusto basato su istogrammi di gradienti orientati, è invariante a scale, rotazione e variazioni di illuminazione. La struttura del descrittore è la seguente: la regione attorno al kepoint viene partizionata in 4x4 sotto-regioni, per ognuna si costruisce istogramma di 8 bin delle orientazioni, pesate per la magnitudo, i valori vengono distribuiti nei bin adiacenti tramite interpolazione, i 4x4x8 ì=128 valori concatenati formano il vettore descrittore che viene poi normalizzato per aggiungere invarianza all'illuminazione.

Queste feature sono state utilizzate per creare il dizionario del **Bag of Visual Words**, ovvero un dizionario di k parole visive che partizionano lo spazio delle feature. Dopo aver raccolto i vari descrittori dal training set, si proiettano tutti vettori dei descrittori nello spazio delle features N-dimensionale e tramite algoritmo di K-means di vanno a raggruppare i nostri descrittori in cluster, il centroide del cluster rappresenta una parola visiva.
Abbiamo applicato l'algoritmo TD-IDF al nostro dizionario per misurare l'importanza di un termine rispetto a tutto il dizionario, grazie a questo algoritmo si vanno a pulire parole troppo frequenti come possono essere cielo, nuvole o altre cose non troppo significative ma molto presenti.
#### Feature deep
Nel progetto ho utilizzato **VGG16** che è stata la prima rete ad esplorare l'aspetto deep utilizzando 13 layer convoluzionali tutti 3x3, questo perché due convoluzioni 3x3 in sequenza hanno le stesso campo ricettivo di una 5x5, ma con meno parametri e una non linearità in più. Il limite di questa rete è il costo in memoria dovuto soprattutto ai 3 layer fully connected.
Abbiamo poi esplorato **ResNet**(50 che sono i livelli), anche questa è una rete molto profonda e introduce i residual block/skip connection che sommano l'input del blocco al suo output F(x) + x, in questo modo non deve imparare tutta la trasformazione ma solo il residuo. Questo permetta al gradiente di propagarsi facilmente cancellando così l'effetto del gradient vanishing presente nelle reti molto profonde, introduce anche il batch normalization che normalizza output di ogni layer rispetto al mini-batch corrente rendendo addestramento più veloce.
Inoltre abbiamo esplorato anche **Clip Vit**, ovvero un modello multimodale che mappa testo e immagini in uno spazio vettoriale condiviso, è basato su transformer Vit con self-attention e utilizza patch visivo di 32x32 (token) e un encoder testuale per massimizzare similarità tra coppie immagine-testo.
### Borda count
Borda count è un sistema di re-ranking basato sulla posizione che ha ottenuto l'immagine con il retrieval di varie feature. Molto utile perché utilizzabile anche quando punteggi delle varie feature hanno scale incompatibili, nella versione uniforme tutte le feature hanno lo stesso peso, in quella pesata è proporzionale al mAP delle feature, nel nostro caso non abbiamo ottenuti notevoli miglioramenti, anzi, in alcuni casi abbiamo subito peggioramenti infatti feature deboli e poco correlate rischiano di introdurre solamente del rumore.
### CLIP e text to image retrieval
Clip Vit, ovvero un modello multimodale che mappa testo e immagini in uno spazio vettoriale condiviso, è basato su transformer Vit con self-attention e utilizza patch visivo di 32x32 (token) e un encoder testuale per massimizzare similarità tra coppie immagine-testo.
Questo modello consente di fare text to image retrieval ovvero descrivendo brevemente un'immagine a parole è possibile recuperare un insieme di immagine correlate.
### Visual RAG
Il visual rag usa il nostro sistema CBIR come parte di retrieval che supporta un piccolo VLM, in pratica il sistema recupera le immagini e stima una confidenza con la quale l'immagine data nella query è un landmark e viene iniettato come contesto testuale al VLM
In pratica viene fornita un'immagine al VLM e questo risponde con breve descrizione e non prende mai il nome dell'edificio, poi si fa la stessa chiamata andando a confrontare l'immagine con quelle presenti nel nostro dataset e si fornisce al VLM una livello di confidenza testuale in modo che possa dare una risposta grounded, Questo sistema permetta ad un semplice VLM di riconoscere e dare informazioni verificate all'utente senza però doverlo fine-tunare.

## Difesa orale del progetto: scelte, alternative e motivazioni

### Idea centrale da comunicare

Il progetto non nasce solo per ottenere il valore di mAP più alto possibile, ma per costruire un confronto ragionato tra diversi livelli di rappresentazione visuale in un sistema CBIR per immagini architettoniche. La domanda principale è: quanto si riduce il semantic gap passando da feature low-level, a feature locali, a feature deep e multimodali?

La scelta di Oxford Buildings 5K è coerente con questa domanda perché il dataset è difficile per un CBIR: lo stesso landmark può essere fotografato da punti di vista, distanze, condizioni di luce e livelli di occlusione diversi, mentre landmark diversi possono condividere materiali, colori e strutture architettoniche simili. Quindi è un contesto adatto per osservare il limite delle feature semplici e il vantaggio di rappresentazioni più semantiche.

Una frase utile da dire all'orale:

> Ho progettato il sistema in modo modulare per confrontare descrittori molto diversi sotto lo stesso protocollo sperimentale. In questo modo il punto non è solo quale metodo vince, ma capire perché alcuni descrittori funzionano in certi casi, perché falliscono in altri e quando la fusione o il feedback dell'utente possono migliorare il retrieval.

### Scelte progettuali principali

| Scelta fatta | Perché è stata fatta | Alternativa possibile | Perché non è stata scelta |
| ------------ | -------------------- | --------------------- | ------------------------- |
| Dataset Oxford Buildings 5K | Benchmark classico per landmark retrieval, con ground truth e ROI | Dataset generico tipo CIFAR/ImageNet | Troppo orientato alla classificazione, meno adatto a retrieval di istanze architettoniche |
| Uso della ROI della query | Concentra la feature sul landmark e riduce cielo, persone, strada, alberi | Usare immagine intera | Avrebbe introdotto rumore visuale non legato all'edificio cercato |
| Pipeline modulare | Permette confronto controllato tra feature diverse | Sistema unico ottimizzato end-to-end | Meno interpretabile e meno adatto a discutere il contributo delle singole feature |
| Feature tradizionali + locali + deep | Coprono livelli diversi del contenuto visivo | Usare solo CLIP o solo deep features | Avrebbe dato buoni risultati ma meno analisi sul semantic gap |
| HSV per colore | Separa tinta, saturazione e luminosità meglio di RGB | RGB, Lab | RGB è meno robusto a variazioni di luce; Lab era possibile ma meno immediato e non necessario per una baseline semplice |
| LBP uniform P=24 R=3 | Cattura texture architettoniche più ampie di un intorno 3x3 | GLCM, BSIF, Gabor | Più costosi o meno compatti; LBP è semplice, interpretabile e adatto come baseline texture |
| Edge histogram con griglia 4x4 | Mantiene una forma approssimata del layout dei bordi | Istogramma globale o HOG completo | Globale perde posizione; HOG sarebbe più ricco ma anche più vicino a un detector e più pesante |
| SIFT + BoVW con TF-IDF | Cattura dettagli locali robusti a scala/rotazione e riduce peso di pattern comuni | Matching diretto SIFT + RANSAC, VLAD, Fisher Vector | Più accurati ma più complessi; BoVW è più coerente con CBIR classico e più semplice da confrontare |
| VGG16 e ResNet50 off-the-shelf | Valutano transfer learning CNN senza fine-tuning | Addestrare/fine-tunare su landmark | Richiede più dati, tempo e rischio overfitting; l'obiettivo era confrontare rappresentazioni già apprese |
| CLIP ViT-B/32 | Aggiunge rappresentazione multimodale e text-to-image retrieval | Modelli più grandi o fine-tuned | Più costosi; CLIP ViT-B/32 è un buon compromesso zero-shot |
| Similarità coseno per deep features | Standard per embedding normalizzati e confronti angolari | Euclidea, Mahalanobis | Coseno è semplice, stabile e adatta a embedding deep |
| Borda Count | Fonde ranking con punteggi su scale diverse | Fusione score-level, learning-to-rank | I punteggi delle feature non erano direttamente confrontabili; learning-to-rank richiedeva training supervisionato |
| Rocchio su ResNet50 | Valuta miglioramento interattivo su embedding compatto e robusto | Rocchio su CLIP o su tutte le feature fuse | CLIP era già molto forte; ResNet mostra meglio il guadagno del feedback rispetto a una baseline migliorabile |
| Visual RAG con voting top-k | Usa CBIR come grounding per ridurre risposte generiche del VLM | Fine-tuning del VLM | Fine-tuning è più costoso; RAG permette specializzazione rapida usando database verificato |

### Come presentare la pipeline

La pipeline può essere raccontata in questo ordine:

1. Si parte da una query con ROI fornita dal benchmark.
2. Si estrae la feature della query e delle immagini del database.
3. Ogni descrittore produce un ranking tramite la propria metrica di similarità.
4. Si valutano i ranking con mAP e P@k.
5. Si confrontano feature singole, fusioni Borda, relevance feedback e Visual RAG.

Il punto importante è che dataset, query e metriche restano invariati. Cambia solo la rappresentazione visuale. Questo rende il confronto più corretto e più difendibile.

### Motivazione delle feature tradizionali

Le feature tradizionali sono state inserite non perché mi aspettassi che superassero le deep features, ma perché sono interpretabili e permettono di capire quali informazioni low-level sono ancora utili.

Il **color histogram HSV** misura la distribuzione dei colori. È molto semplice e infatti ha mAP basso, però raggiunge una P@1 alta. Questo significa che in alcune query il colore è sufficiente a recuperare subito un'immagine corretta, ma non basta a ordinare bene tutto il ranking. È un comportamento coerente: quando un landmark ha colori distintivi, funziona; quando molti edifici condividono pietra chiara e cielo simile, confonde.

L'alternativa era usare RGB, ma HSV è più sensato perché separa tinta, saturazione e luminosità. In un dataset fotografico reale la luminosità cambia molto, quindi usare uno spazio colore più vicino alla percezione rende il descrittore leggermente più robusto.

**LBP** è stato scelto come descrittore di **texture** perché edifici e facciate hanno pattern ripetitivi: mattoni, pietra, finestre, decorazioni. Ho usato P=24 e R=3 perché i pattern architettonici non sono solo micro-texture 3x3, ma strutture più larghe. La variante uniform riduce la dimensionalità e mantiene pattern frequenti come bordi, angoli e zone uniformi.

GLCM, BSIF o Gabor erano alternative valide. Non le ho scelte come feature principali perché avrebbero aumentato il numero di descrittori e il costo computazionale; LBP era un compromesso più semplice e interpretabile per rappresentare la texture.

L'**edge histogram** è stato introdotto perché negli edifici la geometria conta: facciate, colonne, tetti e finestre generano orientazioni di bordo caratteristiche. La griglia 4x4 evita di perdere completamente la posizione spaziale dei bordi. Un istogramma globale sarebbe stato troppo debole; un HOG completo sarebbe stato più ricco, ma anche più pesante e meno immediato come baseline.

### Motivazione di SIFT + BoVW

SIFT + BoVW rappresenta il passaggio intermedio tra feature globali semplici e deep learning. SIFT è utile perché descrive dettagli locali ed è robusto a scala, rotazione e parzialmente a illuminazione. Questo è importante in Oxford Buildings, dove lo stesso edificio può essere fotografato da prospettive diverse.

Il problema è che ogni immagine produce un numero variabile di descrittori SIFT. BoVW risolve questo trasformando l'insieme di descrittori locali in un vettore di lunghezza fissa: si costruisce un vocabolario visuale con k-means e ogni descrittore viene assegnato alla parola visiva più vicina.

La pesatura **TF-IDF** è stata scelta perché non tutte le parole visive hanno lo stesso valore. Pattern molto frequenti, come cielo, strada, finestre generiche o texture comuni, devono pesare meno; dettagli più discriminativi devono pesare di più.

Alternative possibili:

- **Matching diretto SIFT + RANSAC**: più preciso perché verifica anche la coerenza geometrica, ma molto più costoso per retrieval su database.
- **Vocabolario più grande**: avrebbe migliorato la discriminatività, ma aumentato memoria e tempi di clustering.
- **VLAD o Fisher Vector**: più potenti di BoVW classico, ma meno semplici da spiegare e implementare.

Il risultato è coerente: BoVW ha P@1 pari a CLIP, quindi spesso trova subito un match corretto, ma ha mAP più basso perché il ranking completo è meno stabile.

### Motivazione delle feature deep

Le feature deep sono state usate off-the-shelf per valutare quanto rappresentazioni apprese su grandi dataset siano trasferibili al landmark retrieval senza addestramento specifico.

**VGG16** è una baseline storica. Il layer fc6 produce un vettore ricco e ad alta dimensionalità, ma la rete è meno profonda e più pesante. È utile come confronto con la letteratura sulle CNN off-the-shelf.

**ResNet50** è stata scelta perché introduce residual connections e produce una rappresentazione più compatta dal global average pooling. Rispetto a VGG16, è più profonda, più moderna e nei risultati ottiene mAP migliore con meno dimensioni.

**CLIP** è la scelta più importante perché cambia il tipo di rappresentazione: non è addestrato solo su classi visive, ma su coppie immagine-testo. Questo gli permette di catturare concetti più semantici e di supportare anche text-to-image retrieval. Il risultato migliore di CLIP conferma che per il landmark retrieval non basta la somiglianza low-level: serve una rappresentazione più vicina al significato dell'immagine.

Alternative possibili:

- **Fine-tuning di ResNet o CLIP su landmark**: probabilmente avrebbe migliorato il mAP, ma avrebbe cambiato il focus del progetto da confronto di feature a training di modello.
- **GeM, R-MAC o pooling regionali**: più adatti al landmark retrieval e infatti migliori in letteratura, ma più specialistici.
- **Modelli CLIP più grandi**: possibili, ma più costosi e meno leggeri.

La scelta off-the-shelf è difendibile perché permette di misurare il potere delle rappresentazioni pre-addestrate senza introdurre variabili di training.

### Motivazione del Borda Count

Il Borda Count è stato scelto perché i vari descrittori producono punteggi non confrontabili: intersezione tra istogrammi, chi-squared, coseno e distanze su BoVW non hanno la stessa scala. Fondere direttamente gli score avrebbe richiesto normalizzazioni arbitrarie.

Borda lavora invece sui ranking: se un'immagine compare in alto per più feature, riceve un punteggio migliore. Questo rende la fusione semplice e indipendente dalle scale dei punteggi.

Il risultato è interessante perché mostra un limite: la fusione non migliora automaticamente. La fusione delle sole feature deep migliora P@1, P@5 e P@10, ma non supera CLIP in mAP. La fusione di tutte le feature peggiora perché descrittori deboli introducono rumore nel ranking. Questo è un punto importante da dire all'orale: il progetto non nasconde il risultato negativo, ma lo interpreta.

Alternative possibili:

- **Score-level fusion**: richiede normalizzare punteggi eterogenei.
- **Learning-to-rank**: richiede dati supervisionati e training.
- **Fusione query-adaptive**: sarebbe uno sviluppo futuro, perché alcune feature funzionano bene solo per certe query.

### Motivazione del relevance feedback

Il relevance feedback con Rocchio è stato usato per simulare un sistema interattivo. Nel retrieval l'utente spesso non vuole solo una risposta statica, ma può correggere progressivamente il sistema indicando quali risultati sono rilevanti.

Rocchio sposta il vettore query verso i positivi e lontano dai negativi:

```text
q' = alpha q + beta media(positivi) - gamma media(negativi)
```

Nel progetto il feedback è simulato usando il ground truth: good e ok sono positivi, gli altri sono negativi. Questa non è un'interfaccia reale, ma misura il potenziale massimo di un sistema con feedback corretto.

Il risultato è molto forte: ResNet50 passa da mAP 0.3560 a 0.5929 dopo tre iterazioni, migliorando 54 query su 55. Questo mostra che anche una rappresentazione non perfetta può diventare molto efficace se l'utente fornisce un segnale di correzione.

Limite da riconoscere:

> Se nei primi risultati non compare nessun positivo, Rocchio ha poco segnale utile e può non migliorare. Il relevance feedback funziona quando il ranking iniziale contiene almeno qualche risultato corretto.

Alternative possibili:

- **Re-weighting delle feature**: invece di spostare la query, cambia il peso dei descrittori.
- **MARS o MindReader**: più sofisticati, ma anche più complessi.
- **Feedback reale da utente**: più realistico, ma meno controllabile sperimentalmente.

### Motivazione del Visual RAG

Il Visual RAG è stato introdotto per mostrare che il CBIR può essere usato non solo per recuperare immagini, ma anche come memoria esterna per un Vision-Language Model.

Il problema osservato è che BLIP-2 da solo produce descrizioni generiche e non identifica correttamente i landmark. Questo è un caso di risposta plausibile ma non grounded: il modello vede un edificio, ma non ha una base affidabile per dire quale landmark sia.

La soluzione è usare il CBIR come retrieval component:

1. CLIP recupera le top-k immagini più simili.
2. Le immagini recuperate vengono associate ai landmark noti tramite knowledge base costruita dal ground truth.
3. Si usa voto di maggioranza per stimare il landmark più probabile.
4. Questa informazione viene passata al VLM come contesto.

Il voto di maggioranza è più robusto del solo top-1 perché riduce il rischio che un falso positivo isolato condizioni la risposta. Se più risultati tra i primi k concordano sul landmark, il contesto è più affidabile.

Alternative possibili:

- **Fine-tuning del VLM**: più costoso e meno immediato.
- **Prompting senza retrieval**: non risolve il problema della conoscenza specifica del dataset.
- **Classificatore supervisionato sui landmark**: funzionerebbe nel benchmark chiuso, ma sarebbe meno flessibile e meno interessante come sistema retrieval-based.

La scelta Visual RAG è difendibile perché specializza un modello piccolo senza riaddestrarlo, usando evidenza recuperata da un database controllato.

### Come interpretare i risultati all'orale

La gerarchia dei risultati è coerente con il semantic gap:

| Tipo feature | Risultato osservato | Interpretazione |
| ------------ | ------------------ | --------------- |
| Colore | mAP basso, P@1 alta | Utile quando il landmark ha colori distintivi, debole sul ranking completo |
| LBP | Peggiore tra le feature | Texture architettoniche troppo condivise tra edifici diversi |
| Edge | Simile al colore in mAP | Cattura geometria ma soffre punto di vista e clutter |
| SIFT + BoVW | Forte miglioramento, P@1 alta | I dettagli locali sono discriminativi, ma la quantizzazione limita il ranking |
| VGG16 | Buona baseline deep | Feature più semantiche ma rete meno compatta e meno moderna |
| ResNet50 | Migliore di VGG16 | Più profonda, residual, embedding compatto |
| CLIP | Migliore singola feature | Rappresentazione multimodale più vicina al significato del landmark |
| Borda | Non sempre migliora | La fusione aiuta solo se i descrittori sono affidabili e comparabili |
| Rocchio | Grande miglioramento | Il feedback utente corregge efficacemente la direzione della query |
| Visual RAG | BLIP-2 passa da generico a grounded | Il retrieval fornisce contesto verificabile al VLM |

Una lettura matura dei risultati è questa:

> Il progetto mostra che non esiste una feature universalmente migliore in ogni condizione. CLIP è la migliore in media, ma BoVW e colore restano utili in casi specifici. La fusione non va applicata automaticamente perché feature deboli possono aggiungere rumore. Il relevance feedback, invece, dimostra che l'interazione può compensare i limiti del descrittore iniziale.

### Domande probabili all'orale e risposte

**Perché non hai usato solo CLIP se è il migliore?**

Perché l'obiettivo del progetto era confrontare livelli diversi di rappresentazione e capire il semantic gap. Usare solo CLIP avrebbe dato una buona baseline, ma non avrebbe spiegato quali informazioni low-level o locali rimangono utili e perché alcuni metodi falliscono.

**Perché Borda Count peggiora quando fondi tutte le feature?**

Perché la complementarità non basta. Se una feature è molto debole, può portare in alto immagini sbagliate. Anche con peso ridotto, questi errori possono disturbare il ranking finale. Borda funziona meglio quando i ranking fusi hanno qualità comparabile.

**Perché Rocchio migliora più della fusione?**

Perché Rocchio usa informazione specifica della query. La fusione usa pesi globali, mentre il feedback dice al sistema quali risultati sono rilevanti per quella query precisa. Quindi sposta la query nella direzione giusta nello spazio delle feature.

**Perché usare la ROI?**

Perché il benchmark fornisce il bounding box del landmark e l'obiettivo è recuperare lo stesso edificio, non confrontare cielo, strada, persone o alberi. Usare la ROI riduce rumore e rende il confronto più centrato sull'oggetto di interesse.

**Perché SIFT + BoVW è più debole della letteratura?**

Perché la letteratura usa vocabolari molto più grandi, anche da 1M visual words, e spesso include verifica geometrica. Nel progetto ho scelto 5000 parole per mantenere il sistema più leggero e gestibile.

**Perché CLIP funziona così bene su landmark?**

Perché è addestrato su coppie immagine-testo e quindi impara uno spazio più semantico rispetto alle CNN classiche. Non guarda solo pattern visivi, ma associa immagini a concetti descrivibili linguisticamente, come chiese, cupole, college o edifici gotici.

**Qual è il limite principale del progetto?**

Il limite principale è che non c'è fine-tuning sul dominio landmark e alcune scelte sono volutamente semplici per mantenere il confronto interpretabile. Metodi specifici come GeM, R-MAC o re-ranking geometrico probabilmente migliorerebbero molto le prestazioni.

**Quale sviluppo futuro è più importante?**

Il re-ranking geometrico con SIFT + RANSAC è probabilmente il più coerente, perché i keypoint sono già estratti e permetterebbero di verificare se query e risultato condividono una geometria plausibile. Questo ridurrebbe falsi positivi visivamente simili ma geometricamente incoerenti.
