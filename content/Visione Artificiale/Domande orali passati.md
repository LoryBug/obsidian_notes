# Domande orali passati

## Domande passate

- Trasformata di Hough, un metodo che usi rette/circonferenze/ellissi.
- Object detection, come si valutano le prestazioni e ha chiesto metodo che andasse bene per utilizzo real time.
- Semantic segmentation, come si valutano prestazioni e come sono fatte le reti, dinne una
- keypoint e descrittori, spiegane alcuni e come funzionano, racconta SIFT
- Descrittore di DoG come funziona e cos'è.
- Bag of words
- Mobile net
- Che layer usi quando passi da ultimo layer di convoluzione alla parte fully connected? descrivilo

## Simulazione per capitolo

### 00. Introduzione al corso

- Visione artificiale vs pattern recognition.
- Perché il pattern recognition è difficile?
- Mapping opaco e mapping trasparente, differenze.
- Che step usi per progettare un sistema VA/PR, descrivili.

### 01. Sistemi di visione

- Proiezione prospettica, come funziona.
- Come scegli FoV, working distance e DoF?
- CCD vs CMOS.
- Acquisizione 3D: stereo, structured light e time of flight.

### 02. Immagini digitali

- Campionamento e quantizzazione.
- RGB, HSV e YCbCr, quando li usi?
- Cross-correlation e convoluzione, differenze.
- Sobel, Prewitt e Roberts: spiegali e confrontali.

### 03. Segmentazione

- Soglia globale e soglia adattiva.
- Morfologia matematica: apertura e chiusura.
- Superpixel, a cosa servono?
- K-means vs mean shift nella segmentazione.

### 05. Estrazione feature 1

- Feature invarianti, cosa vuol dire.
- Istogrammi colore, vantaggi e limite principale.
- GLCM: cosa descrive e che misure estrai.
- LBP vs BSIF, cosa cambia sostanzialmente.

### 06. Estrazione feature 2

- Shape features, quali puoi usare?
- Chain code e problemi principali.
- Shape signatures e descrittori di Fourier.
- CBIR, semantic gap e relevance feedback.

### 07. Keypoint

- Harris detector, come trova gli angoli.
- SIFT, come trovi scala e orientazione.
- SURF vs SIFT.
- Ratio test e RANSAC nel matching.

### 08. Trasformazioni 2D e image stitching

- Coordinate omogenee, perché le usi?
- Gerarchia delle trasformazioni 2D.
- Omografia: cosa preserva e quanti DOF ha.
- Image stitching: pipeline completa.

### 09. Template matching rigido

- Template matching, come valuti le prestazioni.
- SSD e cross-correlation.
- Viola e Jones: quali sono i 3 ingredienti.
- Hough transform: come voti per una retta.

### 10. Bag of Words

- Bag of words.
- Come costruisci il dizionario visuale?
- Come rappresenti un'immagine con BoW?
- Che limiti ha BoW sull'informazione spaziale?

### 11. V-SLAM

- Cos'è il Visual SLAM.
- Pipeline della Visual Odometry.
- 3D-3D, 3D-2D, 2D-2D: differenze.
- Loop closing e drift, spiegali brevemente.

### 12. Deep learning for image classification

- CNN: perché non usi un MLP sulle immagini?
- Convoluzione: stride, padding e feature map.
- ResNet: a cosa servono le skip connection?
- ViT vs CNN: cosa cambia nel modo di vedere l'immagine?

### 13. Deep learning for object detection

- AP e mAP, come si valutano le prestazioni.
- R-CNN, Fast R-CNN e Faster R-CNN.
- YOLO, perché va bene per real time?
- SSD e default box.

### 14. Deep learning for semantic segmentation

- Segmentazione semantica vs instance segmentation.
- IoU e Dice, quando li usi?
- Encoder-decoder per segmentazione, descrivilo.
- U-Net e skip connection, perché servono?

### 15. Video content analysis

- Background subtraction.
- GMM per stimare il background.
- Kalman filter nel tracking.
- MEI e MHI, differenza?
