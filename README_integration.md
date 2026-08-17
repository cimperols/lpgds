# Guide d'Intégration du Lecteur Vidéo Cinématique

Ce guide explique comment le lecteur vidéo cinématique de haute qualité et le trailer généré s'intègrent dans le site HTML existant de votre roman **"Le Plus Grand des Secrets"**.

---

## 1. Fichiers et Assets créés dans le Workspace

*   `assets/videos/trailer_gardiens.mp4` : Le fichier vidéo rendu complet (résolution optimisée, transitions douces, textes cinématiques incrustés et sound design de basses).
*   `trailer-player.css` : Feuille de style CSS autonome gérant le design du lecteur vidéo avec vignette noire, lueurs dorées, états d'interactivité et flexibilité responsive.
*   `trailer-player.js` : Moteur de script d'interactivité gérant le Intersection Observer (lecture automatique), les raccourcis clavier cinéma, l'arpeggio sonore et le compteur de vues simulé dynamique.
*   `trailer_thumbnail.png` : Miniature d'affiche cinématique de haute qualité servant d'image de chargement (poster) avant le démarrage de la vidéo.

---

## 2. Intégration dans le Code HTML existant (`index.html`)

La section vidéo a été insérée de manière fluide à la racine de `index.html` juste après la section **L'Artéfact de Babylone (La Tablette)** et avant le **Tableau de Bord Tactique des 20 Missions**. Ce placement garantit une montée en tension parfaite de l'utilisateur : il décode les secrets millénaires puis plonge dans la bande-annonce animée pour voir le monde s'embraser de lumière !

Le code HTML injecté comprend :
1.  Les balises de métadonnées SEO complètes (`og:video`, `twitter:card`, etc.) ainsi que le schéma JSON-LD structuré pour le référencement vidéo Google.
2.  La section `#trailer-section` avec le conteneur cinéma plein écran.
3.  L'intégration de la miniature `trailer_thumbnail.png` comme poster natif.
4.  L'option de fallback d'intégration YouTube (commentée) s'appuyant sur un conteneur responsive à lazyness de chargement (lazy-loading).
5.  Les CTAs d'achat direct et de partage social couplés aux métriques de vues simulées.

---

## 3. Raccourcis Clavier activés en Lecture (Mode Cinéma)

Lorsque l'utilisateur fait défiler le site et s'arrête devant le lecteur vidéo :
*   **Barre d'espace (`Space`) :** Met en pause ou lance le trailer sans faire défiler la page.
*   **Touche `F` (Fullscreen) :** Active ou désactive le mode cinéma plein écran pour une immersion maximale.
*   **Touche `M` (Mute) :** Active ou désactive instantanément le son pour une écoute discrète.

*Remarque : Pour éviter toute superposition de sons désagréables, le script JS interrompt automatiquement la musique d'ambiance de fond (générée par l'API Web Audio du bouton en bas à droite) dès que l'utilisateur lance la lecture sonore du trailer.*
