import json

# Phase 1.1: gardiens_profil.json
gardiens_profil = {
    "gardiens": [
        {
            "id": "RS",
            "nom_complet": "Dr. Rébecca Shepherd",
            "titre_rang": "Enseignante-chercheuse en mathématiques appliquées (Princeton) / Cryptologue en chef des Gardiens",
            "description_physique": "Jeune femme brillante, regard sombre et d'une intensité rare, cheveux bruns ondulés attachés à la hâte, tenue académique sobre alternant avec une veste en cuir noir résistante en mission.",
            "couleurs_associees": ["Bleu cobalt (analyse)", "Or antique (la tablette)", "Émeraude (les terminaux)"],
            "pouvoir_capacite": "Cryptographie avancée, reconnaissance instantanée de modèles mathématiques complexes, déchiffrement quantique et modélisation géophysique.",
            "arc_narratif": "Universitaire effacée vivant dans l'ombre de son génie -> Propulsée dans l'action par l'assassinat de son père -> Accepte le rôle de Gardienne -> Décrypte la tablette à travers le monde -> Triomphe à Jérusalem en neutralisant Genesis-12 -> Devient une figure légendaire de paix en 2074.",
            "scenes_memorables": [
                "Fuite spectaculaire de son bureau de Princeton sous le feu des mercenaires de Burke.",
                "Infiltration nocturne dans les Archives Secrètes du Vatican pour récupérer le manuscrit d'Ain Karim.",
                "Activation de l'amulette de Nabonide sur l'Esplanade des Mosquées à Jérusalem pour transmuter l'antimatière en lumière."
            ],
            "replique_iconique": "Les troupes de Burke mentent rarement, Keller. C'est nous qui refusons de lire ce que les chiffres crient."
        },
        {
            "id": "AK",
            "nom_complet": "Alex Keller",
            "titre_rang": "Le Fantôme du MIT / Cyber-activiste et Hacker en chef des Gardiens",
            "description_physique": "Visage anguleux, crâne rasé, yeux gris perçants d'acier, porte un sweat à capuche noir de cyber-ghost, une veste technique sombre et des mitaines de hacker, toujours entouré d'écrans.",
            "couleurs_associees": ["Vert émeraude (code)", "Gris anthracite (les ombres)", "Noir d'encre (cyberespace)"],
            "pouvoir_capacite": "Infiltration de réseaux isolés, piratage quantique, déblocage de pare-feu militaires, sabotage informatique et contournement logiciel en temps réel.",
            "arc_narratif": "Loner cynique et asocial fuyant les autorités -> Répond à l'appel de détresse de Rébecca en activant le Protocole Prométhée -> S'engage corps et âme pour la confrérie -> Pirate les Trois-Gorges, Kiruna et Baïkonour -> Infiltre le satellite de Burke et expose ses crimes au monde entier.",
            "scenes_memorables": [
                "Sauvetage de Rébecca en berline noire au milieu d'une ruelle de Princeton.",
                "Sabotage du barrage des Trois-Gorges depuis le Wi-Fi d'un Starbucks à Pékin.",
                "Piratage de la station spatiale de l'ESA à Kiruna pour manœuvrer le vieux satellite Envisat."
            ],
            "replique_iconique": "Monte. Et prie pour que ton apocalypse personnelle ne salisse pas les sièges de ma bagnole."
        },
        {
            "id": "TB",
            "nom_complet": "Thomas Blackwood",
            "titre_rang": "Agent Spécial d'Interpol / Protecteur tactique des Gardiens",
            "description_physique": "Silhouette athlétique et imposante, mâchoire carrée et barbe de trois jours grisonnante, porte un trench-coat anthracite sous lequel il cache un revolver de service et un gilet tactique.",
            "couleurs_associees": ["Gris plomb (armes)", "Bleu acier (tactique)", "Noir charbon (la nuit)"],
            "pouvoir_capacite": "Combat au corps-à-corps, maniement d'armes à feu, techniques d'infiltration, extraction sous le feu et résistance physique extrême.",
            "arc_narratif": "Agent d'Interpol enquêtant sur le meurtre d'Elijah -> Se révèle être un Gardien infiltré de longue date -> Assure la survie physique de Rébecca face aux tueurs de Burke -> Se sacrifie héroïquement à Svalbard en retenant un bloc de glace pour sauver David et Rébecca.",
            "scenes_memorables": [
                "Échange de tirs nourris avec les mercenaires de Burke dans le hub souterrain de Grand Central.",
                "Infiltration tactique dans le laboratoire BSL-4 en Espagne en tenue de l'OMS.",
                "Sacrifice dans le bunker Projet Arca à Svalbard, écrasé par la glace en sauvant l'équipe."
            ],
            "replique_iconique": "Parce que je vais risquer ma vie pour vous donner le temps de vous échapper."
        },
        {
            "id": "SC",
            "nom_complet": "Dr. Sarah Cohen",
            "titre_rang": "Érudite et Archéologue des manuscrits / Gardienne de la Mémoire",
            "description_physique": "Femme mûre, cheveux foncés bouclés, lunettes d'intellectuelle sur le nez, porte des chemises en lin clair de terrain et une écharpe de couleur sable.",
            "couleurs_associees": ["Violet améthyste (religion)", "Sable du désert (archéologie)", "Bleu saphir"],
            "pouvoir_capacite": "Déchiffrement d'écritures anciennes (cunéiforme, araméen, grec), archéologie biblique et modélisation de résonances géologiques.",
            "arc_narratif": "Chercheuse au Vatican -> Accueille Rébecca et Keller -> Traduit le code d'Ain Karim -> Se rend sur le terrain au Chili et à Saint-Pétersbourg pour contrecarrer les attaques environnementales de Burke.",
            "scenes_memorables": [
                "Tient en joue un traître (Michael) avec un petit pistolet de sa veste dans les Archives du Vatican.",
                "Infiltration dans le désert d'Atacama pour détruire l'antenne ELF de Burke.",
                "Piratage de la diffusion du sommet de l'OTAN pour exposer le deepfake géopolitique."
            ],
            "replique_iconique": "J’ai perdu ma famille à cause des mensonges des Veilleurs. La vérité doit être connue."
        },
        {
            "id": "DV",
            "nom_complet": "David",
            "titre_rang": "Ingénieur en chef / Physicien de terrain des Gardiens",
            "description_physique": "Jeune homme athlétique aux cheveux bruns courts, visage énergique et déterminé, porte un gilet de terrain multiboches, des gants de protection et des rangers.",
            "couleurs_associees": ["Gris industriel (métal)", "Orange de sécurité (danger)", "Bleu glacier"],
            "pouvoir_capacite": "Génie mécanique, thermodynamique, pilotage de drones sous-marins (ROV) et neutralisation de charges explosives/sismiques.",
            "arc_narratif": "Jeune physicien du QG de Prague -> Conçoit les shunts énergétiques -> Devient le bras opérationnel sur le terrain (Rotterdam, Antarctique, Naples, Svalbard) -> Survit au sacrifice de Blackwood pour assister Rébecca dans l'acte final.",
            "scenes_memorables": [
                "Conception instantanée du système de déviation magnétique du LHC au CERN.",
                "Sauvetage du glacier Thwaites en jetant une charge sismique dans une faille volcanique.",
                "Neutralisation des résonateurs sismiques dans la caldeira de Naples sous une pluie de cendres."
            ],
            "replique_iconique": "Nous courons de catastrophe en catastrophe. Nous sauvons des millions de gens... C'est une victoire de la lumière."
        },
        {
            "id": "MR",
            "nom_complet": "Miriam",
            "titre_rang": "Théologienne et Archiviste / Coordinatrice logistique des Gardiens",
            "description_physique": "Femme d'un grand calme, cheveux parsemés d'argent attachés en chignon, vêtue d'un élégant manteau de velours bordeaux, regard bienveillant mais inflexible.",
            "couleurs_associees": ["Bordeaux profond (théologie)", "Crème (vieux parchemins)", "Bronze antique"],
            "pouvoir_capacite": "Interprétation des prophéties bibliques, archivage herméneutique et logistique clandestine internationale.",
            "arc_narratif": "Archiviste en chef de la crypte de Prague -> Fait le pont entre la tablette de Babylone et l'Apocalypse de Jean -> Gère les liaisons radio et les transports des Gardiens -> Pilote les véhicules de fuite et les défenses de terrain à Rotterdam et Jérusalem.",
            "scenes_memorables": [
                "Déchiffre les plaques de la Peste de l'Acier et les corrèle à l'Apocalypse.",
                "Stérilise 60 000 tonnes de ferraille infectée au port de Rotterdam avec un canon micro-ondes.",
                "Conduit la berline d'extraction des Gardiens à travers les ruelles escarpées de Turin."
            ],
            "replique_iconique": "Des millions de vies sauvées... C’est une victoire de la lumière. N’en doutez jamais."
        }
    ]
}

with open("gardiens_profil.json", "w", encoding="utf-8") as f:
    json.dump(gardiens_profil, f, ensure_ascii=False, indent=2)
print("gardiens_profil.json generated!")

# Phase 1.2: lieux_atmospheres.json
lieux_atmospheres = {
    "lieux": [
        {
            "nom": "Babylone, Irak",
            "description_atmospherique": "Ruines millénaires ensablées, colonnes de briques cuites brisées, désert infini balayé par un vent chargé de secrets historiques poussiéreux.",
            "conditions_climatiques": "Nuit noire à 4h14, vent du désert sec et froid, lune en pâle faucille suspendue.",
            "palette_couleurs": ["Noir d'ébène", "Or de la lune", "Sable ocre", "Terre d'ombre"],
            "niveau_danger_tension": "HAUT - Présence de mercenaires infiltrés et traque mortelle au milieu des tombes.",
            "moments_action": "Découverte de la tablette d'argile par le Pr. Elijah Shepherd, suivi immédiatement de son meurtre dans son campement dévasté."
        },
        {
            "nom": "Université de Princeton, USA",
            "description_atmospherique": "Département de mathématiques, campus d'architecture gothique enveloppé de silence monacal, bureaux feutrés de bois sombre et lumière bleutée d'écrans.",
            "conditions_climatiques": "21h21 heure de N.Y., pluie battante et froide sur les vitres, atmosphère de tempête.",
            "palette_couleurs": ["Teal (écrans)", "Gris ardoise (pluie)", "Brun acajou (boiseries)", "Bleu électrique (confinement)"],
            "niveau_danger_tension": "CRITIQUE - Ennemis armés infiltrant les couloirs, traque silencieuse.",
            "moments_action": "Rébecca reçoit le colis de son père, son bureau est forcé par des tueurs de Burke, elle s'enfuit par une porte secrète de la bibliothèque."
        },
        {
            "nom": "Tunnels du CERN, Genève (Suisse)",
            "description_atmospherique": "Infrastructures souterraines du SPS/LHC, kilomètres de tubes en acier rutilants, aimants cryogéniques bleus géants, sifflement de l'hélium sous pression.",
            "conditions_climatiques": "Froid industriel contrôlé, alarmes de confinement clignotant rouge vif, buée cryogénique.",
            "palette_couleurs": ["Bleu industriel", "Rouge d'alarme", "Blanc de buée d'hélium", "Gris titane"],
            "niveau_danger_tension": "EXTRÊME - Risque d'explosion subatomique et d'asphyxie par hélium liquide.",
            "moments_action": "Piratage du confinement magnétique, Keller intercepte le cheval de Troie de Burke, évacuation d'urgence sous pression."
        },
        {
            "nom": "Fosse de la Romanche, Océan Atlantique",
            "description_atmospherique": "Abysses marins à 7 700 mètres de profondeur, obscurité totale, pression gigantesque du fond de l'océan, sédiments troubles remués par les hélices de drones.",
            "conditions_climatiques": "Froid glacial des profondeurs, absence totale de lumière naturelle, courants marins puissants.",
            "palette_couleurs": ["Noir d'encre", "Bleu marine profond", "Blanc chirurgical (projecteurs du ROV)", "Vert bioluminescent"],
            "niveau_danger_tension": "HAUT - Pression destructive, attaque de drones sous-marins hostiles.",
            "moments_action": "Pilotage du ROV Orphée, combat contre les drones 'Mégalodons' ennemis, inversion électromagnétique du câble 'Amitié' pour repousser la peste bactérienne de l'acier."
        },
        {
            "nom": "Champs Phlégréens, Naples (Italie)",
            "description_atmospherique": "Supervolcan actif, fumerolles de soufre âcres s'élevant de failles terrestres, puits de forage géothermiques profonds et vibrants de magma.",
            "conditions_climatiques": "Ciel de cendre lourd, pluie acide, vibrations sismiques constantes sous les pieds.",
            "palette_couleurs": ["Orange lave", "Jaune soufre", "Gris de cendre volcanique", "Noir d'obsidienne"],
            "niveau_danger_tension": "APOCALYPTIQUE - Risque d'éruption cataclysmique et d'hiver volcanique mondial.",
            "moments_action": "Infiltration des 11 puits de forage sous le black-out de Keller, gèlement des résonateurs de Burke au plasma et coupe cryogénique des câbles."
        },
        {
            "nom": "Bunker Projet Arca, Svalbard (Norvège)",
            "description_atmospherique": "Forteresse de béton et de glace enfouie sous le pergélisol de l'Arctique, à côté de la réserve mondiale de semences, couloirs gelés hautement technologiques.",
            "conditions_climatiques": "Tempête de neige polaire dehors par -35°C, aurores boréales vertes dansant dans le ciel sombre.",
            "palette_couleurs": ["Cyan (glace)", "Gris béton brut", "Vert aurore boréale", "Blanc de neige"],
            "niveau_danger_tension": "CRITIQUE - Température mortelle, systèmes de défense cryogéniques et radioactifs.",
            "moments_action": "Opération Icebreaker, assaut du bunker souterrain de Burke, Thomas Blackwood se sacrifie en retenant un mur de glace pour sauver l'équipe fuyant avec le disque dur."
        },
        {
            "nom": "Esplanade des Mosquées, Jérusalem",
            "description_atmospherique": "Esplanade sacrée de pierre dorée millénaire, Dôme du Rocher resplendissant sous le soleil, carrefour mystique et géomagnétique mondial.",
            "conditions_climatiques": "Midi pile le 21 mars, soleil éclatant se reflétant sur la coupole d'or, atmosphère chargée d'électricité géomagnétique.",
            "palette_couleurs": ["Or étincelant", "Blanc de calcaire ancien", "Bleu azur du ciel", "Lumière pure (nova)"],
            "niveau_danger_tension": "MAXIMAL - Lancement de l'antimatière orbitale, destin final de l'humanité en jeu.",
            "moments_action": "Rébecca pose le médaillon de Nabonide sur la Pierre Angulaire, canalise la résonance de Schumann à 7,83 Hz pour neutraliser Genesis-12, transformant l'arme en nova lumineuse."
        }
    ]
}

with open("lieux_atmospheres.json", "w", encoding="utf-8") as f:
    json.dump(lieux_atmospheres, f, ensure_ascii=False, indent=2)
print("lieux_atmospheres.json generated!")
