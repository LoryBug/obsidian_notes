# Enduro Market Analytics - Guida Orale Completa

> Documento unico di ripasso per esporre il progetto in modo chiaro: obiettivo, pipeline, parte descrittiva, predittiva, prescrittiva, modelli, alternative, risultati, limiti e risposte alle domande probabili.

## 1. Pitch del progetto

Il progetto applica **Operational Analytics** al mercato delle moto enduro usate.

L'obiettivo non e stimare il prezzo esatto di una singola moto, ma capire **quando** e **per quale tipo di moto** il mercato sembra piu conveniente.

Il progetto parte da annunci usati, li pulisce, li aggrega in serie temporali mensili del prezzo mediano, confronta modelli di forecasting e infine trasforma le previsioni in raccomandazioni di acquisto tramite un indicatore chiamato `buy_score`.

Frase da orale:

> Il progetto non vuole dire quanto vale una moto specifica, ma quando un segmento del mercato enduro usato sembra piu conveniente rispetto alla propria storia.

## 2. I tre livelli di Operational Analytics

La pipeline e costruita su tre livelli:

| Livello | Domanda | Nel progetto |
|---|---|---|
| Descriptive analytics | Cosa e successo nei dati? | Pulizia, EDA, mediane, segmenti, cluster eta/km, stagionalita |
| Predictive analytics | Cosa potrebbe succedere? | Forecast del prezzo mediano generale e per cluster |
| Prescriptive analytics | Cosa conviene fare? | `buy_score` e raccomandazioni future di acquisto |

Schema mentale:

```text
annunci raw
-> preprocessing
-> serie mensile del prezzo mediano
-> forecast generale
-> segmento core
-> cluster eta/km
-> forecast per cluster
-> buy_score
-> raccomandazione futura
```

Frase da orale:

> La pipeline parte da dati descrittivi, costruisce previsioni, e poi traduce le previsioni in una decisione operativa.

## 3. Requisiti della consegna e cosa abbiamo coperto

La consegna richiede:

| Requisito | Coperto? | Dove |
|---|---:|---|
| Data preprocessing | Si | Pulizia dataset, parsing date/numeri, feature engineering |
| Exploratory analysis | Si | Distribuzioni, segmenti, cluster eta/km, heatmap, boxplot, stagionalita |
| Almeno 3 algoritmi di forecasting | Si | Seasonal Naive, Holt-Winters, Random Forest, MLP |
| Metodo statistico | Si | Holt-Winters |
| Metodo neural | Si | MLP |
| Metodo regression tree | Si | Random Forest |
| Valutazione performance | Si | MAE, RMSE, MAPE, R2 |
| Confronto statistico | Si | Sign test pairwise sugli errori assoluti |

Quindi il progetto non e sotto il minimo. E sopra il minimo perche aggiunge anche:

- segmentazione core market;
- cluster eta/km;
- forecast generale e forecast per cluster;
- raccomandazioni prescrittive;
- pipeline riproducibile;
- versione compact da consegna;
- discussione delle alternative metodologiche.

Frase da orale:

> Ho confrontato quattro modelli: Holt-Winters come metodo statistico, MLP come metodo neural, Random Forest come regression tree, e Seasonal Naive come baseline.

## 4. Versione compact della consegna

Per rispettare il limite massimo di 10 file nello zip, la consegna e stata riorganizzata in una versione compatta da 8 file.

File della versione compact:

| File | Ruolo |
|---|---|
| `README.md` | Istruzioni minime di setup e run |
| `requirements.txt` | Dipendenze Python |
| `enduro_listings_raw.csv` | Dataset raw unico |
| `utils.py` | Tutta la logica condivisa: preprocessing, modelli, metriche, cluster, grafici |
| `01_preprocess_descriptive.py` | Preprocessing, EDA, segmentazione e cluster descrittivi |
| `02_forecasting.py` | Forecast generale e forecast per cluster |
| `03_recommendations.py` | Raccomandazioni generali e future per cluster |
| `run_pipeline.py` | Entrypoint unico |

Comando:

```bash
python run_pipeline.py
```

La pipeline crea runtime folders automaticamente:

```text
data_processed/
outputs_tables/
outputs_figures/
```

Frase da orale:

> La repo completa era modulare, ma per il vincolo di massimo 10 file ho prodotto una versione compact riproducibile: pochi file nello zip, stessi step logici, output rigenerabili.

## 5. Parte descrittiva: cosa abbiamo fatto

La **descriptive analytics** serve a capire il mercato e trasformare dati grezzi in una base analitica affidabile.

Nel progetto prende il dataset raw:

```text
enduro_listings_raw.csv
```

e produce:

```text
1930 annunci raw
1891 annunci puliti
262 settimane osservate
72 mesi osservati
```

### 5.1 Pulizia dati

Operazioni principali:

| Operazione | Motivo |
|---|---|
| Parsing date | Serve una data valida per costruire serie temporali |
| Conversione numerica | Prezzo, anno, km, cilindrata devono essere numerici |
| Normalizzazione testo | Brand, modello, regione, provincia e seller type coerenti |
| Booleani | `is_2stroke`, `has_documents` resi valori booleani |
| Rimozione righe invalide | Evita distorsioni nel forecast |
| Ordinamento temporale | Necessario per serie e split cronologico |

Frase da orale:

> La prima fase trasforma annunci rumorosi in una base pulita e aggregabile. Senza questa fase il forecasting sarebbe poco affidabile.

### 5.2 Feature engineering

Feature create:

| Feature | Significato |
|---|---|
| `age` | Eta della moto rispetto al 2026 |
| `km_per_year` | Chilometri normalizzati per eta |
| `price_per_cc` | Prezzo rapportato alla cilindrata |
| `is_vintage` | Moto prima del 1995 |
| `is_youngtimer` | Moto dal 1995 al 2009 |
| `market_segment` | Segmento: modern, youngtimer, vintage |
| `observation_date` | Data usata per aggregazione temporale |
| `season` | winter, spring, summer, autumn |
| `riding_season` | true tra aprile e ottobre |

### 5.3 Perche non prevedere il singolo annuncio

Il singolo prezzo e troppo rumoroso. Dipende da fattori non osservati:

- manutenzione;
- accessori;
- stato reale;
- urgenza del venditore;
- trattabilita;
- qualita foto/descrizione;
- differenza tra prezzo richiesto e prezzo finale.

Per questo il progetto non e una regressione sul singolo annuncio.

Frase da orale:

> Non stimiamo quanto vale una moto specifica: stimiamo quando un segmento del mercato sembra piu conveniente.

### 5.4 Perche la mediana e non la media

Target principale:

```text
median_price
```

La mediana e robusta agli outlier. Nel mercato dell'usato ci sono moto molto care, vintage, annunci sovraprezzati, occasioni isolate e prezzi anomali.

Esempio:

```text
Prezzi: 3500, 4200, 4500, 4700, 15000
Media: 6380
Mediana: 4500
```

La media suggerisce un prezzo tipico troppo alto, la mediana rappresenta meglio il centro del mercato.

Frase da orale:

> La mediana riduce l'impatto degli outlier e rende piu stabile la serie temporale del prezzo.

### 5.5 Perche frequenza mensile

Alternative considerate:

| Frequenza | Problema |
|---|---|
| Giornaliera | Troppi pochi annunci, serie sparsa |
| Settimanale | Utile come controllo, ma ancora rumorosa |
| Mensile | Miglior compromesso tra dettaglio e stabilita |

Frase da orale:

> Il mese offre abbastanza osservazioni per calcolare mediane sensate senza perdere completamente la dinamica temporale del mercato.

### 5.6 Segmento core

Il mercato completo contiene moto molto diverse:

- enduro racing moderne;
- maxi enduro 690/701;
- youngtimer;
- vintage;
- annunci anomali.

Il segmento core e definito come:

```text
market_segment = modern
250 <= engine_cc <= 500
1000 <= price <= 20000
```

Risultati segmenti:

| Segmento | Mesi | Mesi affidabili | Annunci | Mediana delle mediane |
|---|---:|---:|---:|---:|
| core_modern_enduro_250_500 | 62 | 29 | 894 | 6800 |
| full_market | 72 | 67 | 1891 | 6225 |
| maxi_enduro_690_701 | 34 | 12 | 211 | 7412.5 |
| vintage_epoca | 54 | 13 | 598 | 3400 |

Frase da orale:

> Il mercato completo viene usato come benchmark, ma per una raccomandazione operativa e meglio confrontare moto comparabili.

### 5.7 Cluster eta/km

Fasce usate:

```text
eta: 0-2, 3-5, 6-10, 11-20, 20+
km: 0-5k, 5-10k, 10-15k, 15k+
```

Esempio cluster:

```text
6-10__0-5k = moto 6-10 anni con 0-5000 km
```

Motivazione:

> Eta e chilometraggio sono driver intuitivi e disponibili del valore dell'usato. I cluster permettono di confrontare moto simili.

Cluster principali:

| Eta | Km | Annunci | Mediana | Copertura |
|---|---|---:|---:|---|
| 0-2 | 0-5k | 92 | 8550 | strong |
| 3-5 | 0-5k | 274 | 7200 | strong |
| 3-5 | 5-10k | 20 | 6175 | strong |
| 6-10 | 0-5k | 267 | 6200 | strong |
| 6-10 | 5-10k | 43 | 5900 | strong |
| 6-10 | 15k+ | 20 | 4800 | strong |
| 11-20 | 0-5k | 53 | 4100 | strong |
| 11-20 | 5-10k | 20 | 4400 | strong |

## 6. Parte predittiva: cosa abbiamo fatto

La **predictive analytics** risponde alla domanda:

> Che prezzo mediano possiamo aspettarci in futuro?

Nel progetto ci sono due livelli:

| Livello | Ruolo |
|---|---|
| Forecast generale | Benchmark sul mercato aggregato |
| Forecast per cluster | Previsione piu operativa su gruppi omogenei |

### 6.1 Perche il forecast generale e solo benchmark

Il mercato aggregato cambia anche perche cambia il mix degli annunci.

Esempio:

> Se in un mese entrano piu moto recenti, la mediana generale sale anche se i prezzi delle singole tipologie non sono aumentati.

Frase da orale:

> Il forecast generale serve come baseline di mercato, ma la decisione operativa si basa sui cluster, perche riducono l'effetto del mix degli annunci.

### 6.2 Trasformazione in supervised learning

Per i modelli ML la serie temporale viene trasformata in un dataset supervisionato.

Target:

```text
median_price_t
```

Feature:

```text
median_price_lag_1
median_price_lag_2
median_price_lag_3
median_price_lag_4
rolling_mean_4
rolling_std_4
listings_count
avg_km
avg_age
vintage_share
youngtimer_share
two_stroke_share
month
week_number
riding_season_share (nei cluster)
```

Interpretazione:

> I lag trasformano una serie temporale in un problema supervisionato: il modello impara a prevedere il futuro usando il passato.

### 6.3 Split cronologico

Lo split e cronologico:

```text
train = passato
```

Non si usa split casuale per evitare leakage temporale.

Frase da orale:

> Lo split cronologico simula uno scenario reale: il modello viene addestrato sul passato e valutato sui periodi successivi.

## 7. Modelli usati e motivazione

La consegna richiede tre famiglie:

| Famiglia richiesta | Modello nel progetto |
|---|---|
| Metodo statistico | Holt-Winters |
| Metodo neural | MLP |
| Metodo regression tree | Random Forest |

In piu il progetto usa `Seasonal Naive` come baseline.

### 7.1 Seasonal Naive

Ruolo: baseline.

Prevede ripetendo il pattern recente.

Perche serve:

> Se un modello complesso non batte una regola semplice, non sta aggiungendo valore.

Frase da orale:

> La baseline serve come controllo minimo per dare significato al confronto tra modelli.

### 7.2 Holt-Winters

Ruolo: metodo statistico.

Modella:

- livello;
- trend;
- stagionalita.

Perche scelto:

- e ammesso esplicitamente nella consegna;
- e interpretabile;
- e proporzionato a serie non lunghissime;
- e meno pesante di SARIMA/SARIMAX sui cluster corti.

Frase da orale:

> Holt-Winters e il modello statistico scelto perche consente di modellare livello, trend e stagionalita con complessita contenuta.

### 7.3 Random Forest

Ruolo: metodo tree-based.

Punti forti:

- usa lag del prezzo;
- usa rolling mean/std;
- usa composizione del mercato;
- gestisce relazioni non lineari;
- funziona bene con dati tabellari;
- e piu difendibile di modelli molto complessi.

Frase da orale:

> Random Forest e utile perche il prezzo mediano non dipende solo dal tempo, ma anche dal mix degli annunci disponibili in quel mese.

### 7.4 MLP

Ruolo: metodo neural.

Perche incluso:

- copre la famiglia neural richiesta;
- permette un confronto non lineare.

Perche non e centrale:

- pochi dati mensili;
- rischio overfitting;
- risultati peggiori;
- minore interpretabilita.

Frase da orale:

> L'MLP e incluso per coprire la famiglia neural richiesta, ma non e il modello migliore perche con poche osservazioni mensili una rete neurale tende a essere instabile.

## 8. Metriche e confronto statistico

Metriche usate:

| Metrica | Significato |
|---|---|
| MAE | Errore medio assoluto in euro |
| RMSE | Penalizza errori grandi |
| MAPE | Errore percentuale medio |
| R2 | Quota di variabilita spiegata |

Confronto statistico:

Il progetto usa anche un **sign test pairwise** sugli errori assoluti.

Funzionamento:

```text
Per ogni coppia di modelli:
- conta i mesi in cui A ha errore assoluto minore di B
- conta i mesi in cui B ha errore assoluto minore di A
- calcola un p-value sotto ipotesi di pari probabilita di vittoria
```

Frase da orale:

> Oltre alle metriche aggregate, uso un confronto statistico pairwise degli errori assoluti. Questo risponde al requisito di confrontare statisticamente le performance predittive.

## 9. Risultati predittivi principali

### 9.1 Forecast generale

Risultati stabili della versione finale:

| Modello | MAE | RMSE | MAPE | R2 |
|---|---:|---:|---:|---:|
| Random Forest | 1402.22 | 1762.12 | 22.00% | 0.226 |
| Holt-Winters | 1713.03 | 2123.34 | 31.83% | -0.124 |
| Seasonal Naive | 2311.07 | 2725.96 | 39.74% | -0.853 |
| MLP | 3306.16 | 4569.68 | 53.80% | -4.206 |

Interpretazione:

> Random Forest vince sul forecast generale perche sfrutta sia la dinamica passata del prezzo sia variabili che descrivono la composizione del mercato.

### 9.2 Forecast per cluster

Risultati stabili della versione finale:

| Cluster | Best model | RMSE | MAPE | Lettura |
|---|---|---:|---:|---|
| 11-20 / 0-5k | Holt-Winters | 80.02 | 1.78% | Serie molto stabile |
| 3-5 / 0-5k | Holt-Winters | 864.97 | 9.11% | Cluster ricco ma piu variabile |
| 6-10 / 0-5k | Random Forest | 718.39 | 10.38% | Buon compromesso operativo |

Frase da orale:

> Il forecast per cluster e piu interpretabile del forecast generale, perche confronta moto piu simili tra loro.

## 10. Parte prescrittiva: cosa abbiamo fatto

La **prescriptive analytics** risponde alla domanda:

> Cosa conviene fare?

Nel progetto il forecast viene trasformato in una raccomandazione tramite `buy_score`.

Formula:

```text
buy_score = historical_cluster_median - predicted_median_price
```

Interpretazione:

| Caso | Significato |
|---|---|
| `buy_score > 0` | Prezzo previsto sotto la mediana storica del cluster |
| `buy_score circa 0` | Situazione neutrale |
| `buy_score < 0` | Prezzo previsto sopra la mediana storica |

Label:

| Condizione | Label |
|---|---|
| `score_pct >= 10%` | `strong_buy` |
| `score_pct >= 3%` | `good_buy` |
| `score_pct <= -10%` | `avoid_expensive` |
| altrimenti | `neutral` |

Risultato finale stabile:

```text
Periodo: 2026-08
Cluster: 6-10 anni / 0-5k km
Prezzo previsto: circa 5789 euro
Mediana storica: 6000 euro
Buy score: circa 211 euro
Raccomandazione: good_buy
Modello: Random Forest
```

Frase da orale:

> La raccomandazione non dice di comprare sicuramente, ma indica che quel cluster e previsto sotto la propria mediana storica, quindi puo essere una finestra conveniente.

## 11. Alternative considerate

### 11.1 SARIMA

Ha senso come alternativa statistica classica.

Pro:

- modello noto per serie temporali;
- cattura autocorrelazione e stagionalita;
- utile su serie lunghe e regolari.

Contro nel nostro caso:

- serie mensili non lunghissime;
- cluster con pochi mesi osservati;
- warning su stima parametri con poche osservazioni;
- meno difendibile se migliora poco.

Esperimento fatto:

- Sul forecast generale SARIMA non batte Random Forest.
- Su alcuni cluster migliora leggermente, ma con warning e cambiando molto la raccomandazione.

Frase da orale:

> Ho considerato SARIMA come alternativa classica. Sul generale non batte Random Forest; sui cluster puo migliorare leggermente alcuni casi, ma con poche osservazioni e warning sui parametri ho preferito una soluzione piu robusta.

### 11.2 SARIMAX

SARIMAX e SARIMA con variabili esogene.

Potrebbe usare:

- `listings_count`;
- `avg_km`;
- `avg_age`;
- `month`;
- `riding_season_share`.

Perche non incluso:

- richiede valori futuri delle variabili esogene;
- aggiunge parametri;
- aumenta rischio overfitting;
- serie cluster troppo corte.

Frase da orale:

> SARIMAX sarebbe una naturale estensione, ma richiede ipotesi sui valori futuri delle covariate e rischia overfitting con serie corte.

### 11.3 XGBoost

Ha senso come alternativa tree-based avanzata.

Esperimento fatto:

| Modello | MAE | RMSE | MAPE | R2 |
|---|---:|---:|---:|---:|
| Random Forest | 1402.22 | 1762.12 | 22.00% | 0.226 |
| XGBoost | 1483.39 | 1841.23 | 22.98% | 0.155 |

Conclusione:

> XGBoost non migliora Random Forest sul generale e aggiunge una dipendenza piu pesante. Per questo non e necessario nella consegna finale.

### 11.4 Transformer

Non e proporzionato al progetto.

Perche:

- 72 mesi generali sono pochi;
- cluster ancora piu corti;
- richiede molti dati;
- alto rischio overfitting;
- dipendenze pesanti tipo PyTorch/TensorFlow;
- bassa difendibilita rispetto all'obiettivo.

Frase da orale:

> Un Transformer sarebbe eccessivo per la scala del dataset. E adatto a molte serie lunghe o dataset temporali molto grandi, non a poche osservazioni mensili.

### 11.5 Regressione sul singolo annuncio

Alternativa possibile ma non coerente con l'obiettivo.

Pro:

- piu righe disponibili;
- target diretto.

Contro:

- target troppo rumoroso;
- variabili cruciali non osservate;
- obiettivo diverso: valutare una moto, non decidere quando comprare.

## 12. Limiti del progetto

| Limite | Impatto | Come lo gestiamo |
|---|---|---|
| Prezzi richiesti, non finali | Il prezzo reale di vendita puo essere diverso | Interpretazione come mercato degli annunci |
| Dataset non enorme | Modelli complessi meno affidabili | Mediane, baseline, modelli robusti |
| Variabili non osservate | Stato reale/accessori/manutenzione non catturati | Aggregazione mensile e mediana |
| Cluster corti | Alcuni forecast fragili | Soglia minima di mesi osservati |
| Forecast generale rumoroso | Mix annunci cambia nel tempo | Decisione finale su cluster |

Frase da orale:

> I limiti non sono nascosti: sono proprio il motivo per cui ho scelto mediana, segmentazione e modelli proporzionati ai dati.

## 13. Come spiegare descriptive, predictive e prescriptive all'esame

### Descriptive analytics

Risposta:

> Nella parte descrittiva pulisco il dataset, creo feature rilevanti, costruisco serie mensili del prezzo mediano, analizzo distribuzioni e segmenti, e creo cluster eta/km per capire quali gruppi sono piu omogenei e ricchi di dati.

Output:

- dataset pulito;
- serie settimanale e mensile;
- summary stagionale;
- segmento core;
- cluster eta/km;
- heatmap, boxplot, distribuzioni.

### Predictive analytics

Risposta:

> Nella parte predittiva confronto modelli di forecasting sul prezzo mediano. Uso Holt-Winters come metodo statistico, MLP come rete neurale, Random Forest come regression tree e Seasonal Naive come baseline. Valuto i modelli con split cronologico, MAE, RMSE, MAPE, R2 e sign test.

Output:

- previsioni generali;
- metriche modelli;
- confronto statistico;
- forecast per cluster.

### Prescriptive analytics

Risposta:

> Nella parte prescrittiva trasformo il forecast in una raccomandazione tramite buy_score. Confronto il prezzo previsto con la mediana storica dello stesso cluster: se il prezzo previsto e sotto la mediana, il mese puo essere conveniente.

Output:

- buying period recommendations;
- future cluster buy recommendations;
- buy_score;
- label `good_buy`, `neutral`, `avoid_expensive`.

## 14. Domande probabili e risposte pronte

| Domanda | Risposta breve |
|---|---|
| Qual e l'obiettivo? | Supportare decisioni di acquisto nel mercato enduro usato. |
| Qual e il target? | Prezzo mediano mensile, `median_price`. |
| Perche mediana? | E robusta agli outlier del mercato usato. |
| Perche non prezzo singolo? | Troppi fattori non osservati rendono il singolo annuncio rumoroso. |
| Perche monthly? | Compromesso tra dettaglio e stabilita. |
| Qual e il metodo statistico? | Holt-Winters. |
| Qual e il metodo neural? | MLP. |
| Qual e il metodo tree-based? | Random Forest. |
| Perche Random Forest vince? | Usa lag e feature descrittive del mercato. |
| Perche il forecast generale non basta? | Risente del mix degli annunci. |
| Cosa rende il progetto prescrittivo? | Il passaggio da forecast a `buy_score` e raccomandazione. |
| Risultato finale? | Agosto 2026, cluster 6-10 / 0-5k, `good_buy`. |
| Come eviti leakage? | Split cronologico e lag solo dal passato. |
| Perche non Transformer? | Troppi pochi dati e troppa complessita. |
| Perche compact? | Vincolo di massimo 10 file nello zip. |

## 15. Pitch completo da 60-90 secondi

Il progetto applica Operational Analytics al mercato delle enduro usate. L'obiettivo non e stimare il prezzo esatto di una singola moto, perche ogni annuncio dipende da fattori non osservati come manutenzione, accessori, stato reale e trattabilita. Invece trasformo gli annunci in serie temporali mensili del prezzo mediano, che e piu robusto agli outlier rispetto alla media.

Nella parte descrittiva pulisco i dati, creo feature come eta, chilometraggio, segmento di mercato e stagionalita, e isolo un segmento core piu coerente: enduro moderne 250-500cc. Poi creo cluster eta/km per confrontare moto simili.

Nella parte predittiva confronto modelli appartenenti alle famiglie richieste: Holt-Winters come metodo statistico, MLP come rete neurale e Random Forest come regression tree, piu Seasonal Naive come baseline. Valuto con MAE, RMSE, MAPE, R2 e sign test pairwise, usando split cronologico per evitare leakage temporale.

Infine, nella parte prescrittiva, trasformo le previsioni in raccomandazioni tramite `buy_score`, cioe la differenza tra mediana storica del cluster e prezzo previsto. Il risultato operativo finale suggerisce agosto 2026 per il cluster 6-10 anni / 0-5k km come `good_buy`, con prezzo previsto circa 5789 euro contro una mediana storica di 6000 euro.

## 16. Formula finale da ricordare

```text
mediana mensile + segmento core + cluster eta/km + forecast + buy_score
```

Questa e la logica che rende il progetto difendibile: non usare il modello piu complesso possibile, ma costruire una pipeline coerente con il problema, con i dati e con una decisione operativa reale.
