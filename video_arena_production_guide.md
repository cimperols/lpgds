# Guide de Production de la Bande-Annonce - "Le Plus Grand des Secrets"

Ce guide complet est conçu pour vous accompagner pas à pas dans la génération, le montage et l'intégration sonore du trailer cinématographique officiel de 90 secondes de votre roman, en exploitant les dernières avancées des générateurs vidéo IA d'Arena.

---

## 1. Accès et Configuration de Video Arena

Pour commencer la génération de vos séquences vidéo :
1.  **Rendez-vous sur l'adresse :** `arena.ai/video` (ou l'onglet Video Arena dédié de votre espace).
2.  **Sélectionnez le mode :** **Text-to-Video** (ou Image-to-Video si vous souhaitez utiliser l'une des affiches de la Phase 3 comme point de départ).
3.  **Paramètres recommandés :**
    *   **Résolution :** 4K (ou 1080p Upscaled pour économiser des crédits de calcul lors des premiers essais).
    *   **Fréquence de trame :** 60 FPS (pour un rendu d'une fluidité absolue d'action).
    *   **Ratio d'aspect :** 16:9 (Format horizontal cinéma standard).
4.  **Gestion de la limite de quotas :**
    *   L'offre gratuite d'Arena Video Arena offre **3 générations gratuites toutes les 24 heures**.
    *   Pour les 11 séquences vidéo requises du storyboard, la production s'étalera sur environ **4 jours** si vous utilisez uniquement le quota gratuit de base.
    *   Il est fortement conseillé de générer en priorité les plans les plus complexes (S01 d'ouverture, S10 du lancement, S11 du final à Jérusalem) et d'utiliser des shunts ou des ralentis fluides au montage.

---

## 2. Stratégie de Génération par Modèle IA

Différents modèles IA excellent dans différents domaines. Voici comment répartir vos prompts :

### A. Quand utiliser KLING 3.0 ?
*   **Idéal pour :** Les scènes d'action rapides, la manipulation d'objets (mains), les mouvements de caméra dynamiques (caméra épaule) et le multi-shot.
*   **Séquences assignées :**
    *   **S02 (Assassinat d'Elijah)** : Kling simule à merveille le vacillement de l'éclairage et la fumée.
    *   **S03 (Princeton)** : Excellente gestion de l'expression d'alerte et des mouvements fluides de caméra de poursuite.
    *   **S05 (CERN)** : Kling gère parfaitement les mouvements fluides rapides de course et les débris physiques (étincelles, vapeur d'hélium).
    *   **S08 (Multi-shot)** : Utilisez spécifiquement le prompt multi-shot fourni dans `prompts_kling30.txt` sur le moteur Kling pour générer une séquence de combat rapide en 3 plans cohérents.

### B. Quand utiliser VEO 3.1 ?
*   **Idéal pour :** Les plans larges lents d'établissement (Establishing shots), les effets atmosphériques, la lumière volumétrique géante et l'**audio natif synchronisé** (Sound design direct).
*   **Séquences assignées :**
    *   **S01 (Babylone)** : Le rendu de la brume du désert et le zoompan lent y sont d'une qualité d'éclairage inégalable.
    *   **S06 (Açores)** : Veo excelle dans la modélisation de fluides à grande échelle (la vague de tsunami) et de foudre.
    *   **S11 (Jérusalem - Climax)** : La dispersion des nuages et le rayon de lumière pure exigent la puissance géométrique volumétrique de Veo.
    *   **Audio natif :** Veo 3.1 génère des bruits de vent, de vagues et d'impacts synchronisés à l'action si les balises `[AUDIO]` sont spécifiées dans le prompt.

### C. Stratégie de Retry (Si la génération échoue ou est imparfaite)
*   **Si S01 (Babylone) n'affiche pas la lueur dorée :** Téléchargez l'image `images/babylon.jpg` générée dans votre workspace, passez en mode **Image-to-Video**, importez cette image comme guide d'image initial (image-prompts), et entrez le prompt : *« slow zoompan inside the glowing trench, gold light rippling on cuneiform, desert wind, hyperrealistic 4K »*.
*   **Si S05 (CERN) fait trop cartoon/VFX bas de gamme :** Ajoutez le mot-clé *« 35mm lens, realistic metallic reflections, documentary photography style, high-end commercial grading »* au début du prompt et réduisez l'intensité du mouvement (Motion setting) de 85% à 60% pour stabiliser la physique des objets.

---

## 3. Téléchargement et Organisation locale

Pour mener à bien votre montage sans vous perdre dans vos fichiers, suivez cette nomenclature rigoureuse :
1.  Créez un dossier nommé `PROJET_TRAILER/` sur votre ordinateur local.
2.  Sous-divisez-le en trois sous-dossiers : `01_CLIPS/`, `02_IMAGES/` et `03_AUDIO/`.
3.  Renommez chaque clip téléchargé depuis Video Arena de la façon suivante :
    *   `S01_opening_babylon.mp4`
    *   `S02_assassinat_camp.mp4`
    *   `S03_rebecca_princeton.mp4`
    *   `S04_keller_crypt_prague.mp4`
    *   `S05_cern_escape.mp4`
    *   `S06_tsunami_azores.mp4`
    *   `S07_atacama_antennas.mp4`
    *   `S08_burke_villain.mp4`
    *   `S09_kling_multishot_action.mp4`
    *   `S10_svalbard_ice_bunker.mp4`
    *   `S11_baikonur_launch.mp4`
    *   `S12_jerusalem_climax.mp4`
4.  Enregistrez l'image `title_card_finale.png` générée dans la Phase 3 dans votre dossier `02_IMAGES/`.

---

## 4. Assemblage Vidéo Pas-à-Pas (Logiciels Gratuits)

Vous n'avez pas besoin d'un logiciel professionnel complexe pour monter votre bande-annonce de 90 secondes. Choisissez l'une de ces trois solutions :

### Option A : Microsoft Clipchamp (Gratuit - Intégré à Windows 11)
*   **Avantages :** Très simple, interface intuitive par glisser-déposer, transitions automatiques de fondu.
*   **Méthode :** Importez vos 12 clips MP4. Alignez-les sur la timeline dans l'ordre chronologique des séquences. Ajoutez une transition « Fondu au noir » (Fade to black) d'une durée de 0,5 seconde entre la S09 (Svalbard) et la S10 (Baïkonour) pour créer une rupture dramatique d'une seconde.

### Option B : CapCut Web (Gratuit - Dans votre navigateur)
*   **Avantages :** Filtres cinématiques Teal & Orange pré-enregistrés, calques de grain de pellicule 35mm rétro faciles à appliquer en superposition.
*   **Méthode :** Importez la `title_card_finale.png` à la fin de la timeline et étirez sa durée sur **4 secondes**. Appliquez un effet d'apparition en fondu (Fade in) de 1,5 seconde sur le titre pour simuler la gravure dorée s'allumant progressivement.

### Option C : DaVinci Resolve (Professionnel - Gratuit)
*   **Avantages :** Qualité d'étalonnage de niveau hollywoodien, contrôle de courbe de remappage temporel (Speed ramp) pour ralentir les scènes clés (comme le sacrifice de Blackwood) sur le beat de la musique.

---

## 5. Intégration Sonore et Sound Design Épique

La musique et le sound design représentent 50 % de l'impact émotionnel d'une bande-annonce.

### Où trouver des musiques de trailer de qualité professionnelle libres de droits ?
1.  **Pixabay Music :** Cherchez les tags `cinematic trailer`, `epic dark brass orchestration` ou `mystery strings crescendo`. Tout y est gratuit et libre de droits.
2.  **FreePD.com :** Catégorie **Epic Dramatic** (Public Domain CC0, idéal pour les gros budgets indépendants).
3.  **Epidemic Sound / Artlist :** Offre d'essai de 30 jours (haute qualité de violoncelles et d'orchestration symphonique).

### Comment monter le son ?
*   **Le rythme :** Coupez vos clips précisément sur les percussions lourdes de la musique (les kicks).
*   **La voix off (Optionnelle) :** Vous pouvez utiliser l'outil `generate_speech` d'Arena pour générer une voix narrative française sombre et grave (voix masculine, intonations lentes), l'exporter en MP3 et la superposer sur la bande-son.
*   **La cassure de l'Acte II :** À 52 secondes, juste avant le sacrifice de Blackwood, coupez brusquement la musique instrumentale pour ne laisser que le son de la tempête de neige et le craquement de glace de Svalbard (S09). Relancez l'orchestration à pleine puissance et en fanfare majestueuse lors du décollage de Baïkonour (S10).
