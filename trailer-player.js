/* ============================================================
   TRAILER PLAYER & MISSIONS ENGINE — "LE PLUS GRAND DES SECRETS"
   ============================================================ */

/* === 20 CORRECTED GUARDIAN MISSIONS DATA === */
const missionsData = [
    {
        id: 1,
        phase: "phase1",
        title: "1. Le Sauvetage du CERN",
        date: "10 juin 2025",
        location: "CERN, Genève (Suisse)",
        img: "images/cern.jpg",
        desc: "Les Gardiens s'infiltrent dans les tunnels du Super Synchrotron à Protons (SPS). Keller intercepte un cheval de Troie conçu par Burke pour simuler une surchauffe, purger l'hélium et provoquer l'effondrement du confinement magnétique du collisionneur de hadrons. Bien que piégés, ils fuient par un conduit d'évacuation cryogénique en provoquant une micro-résonance magnétique.",
        quote: "« Stabilisation hélium cryogénique achevée. Les aimants du LHC tiennent bon. L'impact subatomique est avorté. »",
        status: "RÉUSSIE"
    },
    {
        id: 2,
        phase: "phase1",
        title: "2. Le Tsunami des Açores",
        date: "3 septembre 2025",
        location: "Faille Médio-Atlantique (Açores)",
        img: "images/fault_portugal.jpg",
        desc: "Les Veilleurs font exploser des charges thermiques sur la faille sous-marine pour déclencher un méga-tsunami dévastant les terres de l'Ouest. Les Gardiens déploient in extremis des sacs géotextiles et des brise-lames gonflables sur la côte portugaise pour atténuer la puissance de la vague.",
        quote: "« Digues de retenue déployées à 45%. Ponta Delgada est épargnée. La faille se stabilise temporairement. »",
        status: "RÉUSSIE"
    },
    {
        id: 3,
        phase: "phase1",
        title: "3. Le Grand Blackout",
        date: "1er janvier 2026",
        location: "New York City, États-Unis",
        img: "images/blackout.jpg",
        desc: "Burke déploie un ver informatique pour désynchroniser le réseau électrique de la côte Est à minuit. Rébecca et Blackwood s'infiltrent dans le hub de synchronisation primaire de Grand Central Terminal et diffusent un signal mensonger de 59,98 Hz, poussant le virus à compenser l'erreur et à s'annuler lui-même.",
        quote: "« Fréquence forcée à 59,98 Hz. L'IA s'autodétruit en pensant corriger sa propre erreur. New York reste allumée. »",
        status: "RÉUSSIE"
    },
    {
        id: 4,
        phase: "phase1",
        title: "4. La Dissonance Cosmique",
        date: "21 juin 2026",
        location: "Désert d’Atacama (Chili)",
        img: "images/atacama_antennas.jpg",
        desc: "Burke utilise un réseau d'antennes ELF géantes pour perturber la magnétosphère terrestre et aveugler le GPS mondial, activant une bombe logique dans les systèmes de la FAA. Sarah Cohen s'infiltre dans le désert de l'Atacama à l'Observatoire de La Silla et plante un résonateur piézoélectrique sur une veine de quartz locale, créant une boucle de rétroaction qui fait imploser l'antenne chilienne.",
        quote: "« Résonateur quartz actif. Rétroaction ionisante en cours. Antenne ELF pulvérisée par surcharge piézoélectrique. »",
        status: "RÉUSSIE"
    },
    {
        id: 5,
        phase: "phase1",
        title: "5. La Rouille du Blé",
        date: "15 avril 2027",
        location: "Saint-Pétersbourg (Russie)",
        img: "images/wheat.jpg",
        desc: "Burke compte utiliser des oiseaux migrateurs pour répandre un champignon pathogène mortel (Krasnaya Pyl ou rouille noire) sur les champs de blé du monde. Après avoir volé la souche mère à l'Institut Vavilov (et survécu à un piège mortel au gaz argon), les Gardiens piratent les éoliennes des couloirs migratoires pour émettre des ultrasons (40,5 kHz) qui désintègrent les spores en plein vol.",
        quote: "« Émetteurs éoliens synchronisés à 40,5 kHz. Les spores de rouille noire sont neutralisées avant d'atteindre les cultures. »",
        status: "RÉUSSIE"
    },
    {
        id: 6,
        phase: "phase1",
        title: "6. La Grande Déconnexion",
        date: "10 juillet 2027",
        location: "Fosse de la Romanche",
        img: "images/deep_ocean_drones.jpg",
        desc: "Burke déploie des drones 'Mégalodon' pour sectionner simultanément les câbles transatlantiques en fibre optique (notamment le câble 'Amitié'). En pilotant le ROV Orphée, les Gardiens trompent le drone de Burke en amplifiant la signature électromagnétique d'un vieux câble télégraphique de 1858, le poussant à s'y briser les pinces. Lors de la même mission abyssale, they découvrent que le drone vaincu a relâché un bactériophage mangeur de polyéthylène visant à infecter les câbles mondiaux. Rébecca et Keller font inverser la polarité du courant du câble 'Amitié' pendant une demi-seconde, repoussant le virus électromagnétiquement.",
        quote: "« Polarité inversée. Choc électrique réussi. La colonie bactérienne est dispersée et le réseau est sauf. »",
        status: "RÉUSSIE"
    },
    {
        id: 7,
        phase: "phase2",
        title: "7. Le Discours de la Trahison",
        date: "7 septembre 2028",
        location: "Sommet de l'OTAN, Bruxelles",
        img: "images/disinformation.jpg",
        desc: "Burke diffuse un 'deepfake' d'une perfection inouïe montrant les présidents américain et chinois fomentant un complot mondial, menaçant de détruire l'OTAN. Les Gardiens repèrent un tableau de Monet qui ne devrait pas y être dans le reflet d'une pupille, et exposent la supercherie en diffusant des images en direct du musée Marmottan à Paris.",
        quote: "« Preuve de falsification pixellaire injectée en direct sur 400 chaînes mondiales. La manipulation géopolitique a échoué. »",
        status: "RÉUSSIE"
    },
    {
        id: 8,
        phase: "phase2",
        title: "8. La Chute des Abeilles",
        date: "15 mars 2029",
        location: "Vallée Centrale, Californie",
        img: "images/bees_frequencies.jpg",
        desc: "Burke émet une 'note de chaos' acoustique (240 Hz) brouillant la magnétoréception des abeilles, menaçant l'agriculture mondiale d'un effondrement pollinique. Keller pirate des millions de haut-parleurs à travers le monde pour émettre une sous-harmonique invisible (un contre-signal en opposition de phase) qui annule les ondes de Burke et sauve les essaims.",
        quote: "« Contre-chant 240 Hz activé en opposition de phase. Le bruit s'annule. Les essaims d'abeilles retrouvent leur cap. »",
        status: "RÉUSSIE"
    },
    {
        id: 9,
        phase: "phase2",
        title: "9. Le Crypto-Crash",
        date: "31 juillet 2029",
        location: "The Shard, Londres",
        img: "images/crypto_crash.jpg",
        desc: "Burke lance un 'ver quantique' capable d'effectuer des doubles dépenses sur les cryptomonnaies en exploitant le principe d'incertitude quantique. Keller et Rébecca créent des 'nœuds observateurs' qui saturent le réseau (mempool), forçant chaque transaction à figer son état initial et détruisant l'attaque fantôme (Protocole Heisenberg).",
        quote: "« Protocole Heisenberg engagé. La surveillance quantique fige les blocs transactionnels. Le crash boursier est évité. »",
        status: "RÉUSSIE"
    },
    {
        id: 10,
        phase: "phase2",
        title: "10. La Peste de l'Acier (Riposte)",
        date: "18 avril 2030",
        location: "Port de Rotterdam, Pays-Bas",
        img: "images/steel.jpg",
        desc: "Burke tente d'injecter une bactérie affaiblissant l'acier dans la chaîne de recyclage mondiale via des cargaisons de ferraille. David et Miriam utilisent un canon à micro-ondes hyperfréquence depuis une barge pour stériliser la cargaison en plein déchargement du MV Iron Queen. L'équipe échappe de justesse aux Veilleurs grâce à une diversion de Keller sur un chariot élévateur géant et vole la tablette du superviseur pour bloquer le reste de la flotte.",
        quote: "« Rayonnement micro-ondes actif. Stérilisation cristalline de la ferraille achevée à 100%. Flotte ennemie bloquée. »",
        status: "RÉUSSIE"
    },
    {
        id: 11,
        phase: "phase2",
        title: "11. Glacier du Jugement Dernier",
        date: "5 novembre 2030",
        location: "Glacier Thwaites, Antarctique",
        img: "images/glacier_detonators.jpg",
        desc: "Burke affaiblit la base du 'Glacier de l'Apocalypse' (Thwaites) avec des foreuses thermiques, prêt à provoquer son effondrement avec des explosifs. Le ROV Styx piloté par David et Keller descend dans les cavernes subglaciaires. David arrache une des charges sur le point d'exploser et la jette dans une cheminée volcanique subglaciaire, libérant la tension et stabilisant le glacier.",
        quote: "« Détonateurs coupés sous le pergélisol. Charge sismique larguée dans la fosse. Le glacier Thwaites est stabilisé. »",
        status: "RÉUSSIE"
    },
    {
        id: 12,
        phase: "phase3",
        title: "12. Le Déluge du Yangtsé",
        date: "2 mars 2031",
        location: "Barrage des Trois-Gorges, Chine",
        img: "images/three_gorges_dam.jpg",
        desc: "Burke provoque des glissements de terrain massifs pour forcer l'Intelligence Artificielle du plus grand barrage du monde à ouvrir toutes ses vannes, menaçant 400 millions de personnes. Keller pirate le réseau via le Wi-Fi d'un Starbucks à Pékin et force l'IA du barrage à se mettre en 'mode diagnostic' de niveau Oméga pendant 30 minutes, l'empêchant de s'ouvrir lors du pic de pression de la vague.",
        quote: "« Diagnostic de sécurité Oméga activé. L'IA de décharge est gelée pour 30 minutes. Le barrage encaisse le choc. »",
        status: "RÉUSSIE"
    },
    {
        id: 13,
        phase: "phase3",
        title: "13. Le Syndrome de Kessler",
        date: "22 septembre 2031",
        location: "Station de l'ESA, Kiruna (Suède)",
        img: "images/kessler.jpg",
        desc: "Burke détruit un satellite pour créer un nuage de débris incontrôlable qui doit emprisonner l'humanité sur Terre. À Kiruna, Keller s'infiltre dans le réseau de l'ESA avec des identifiants volés au Vatican et active les propulseurs du vieux satellite Envisat (la cible 'domino'), l'écartant de justesse de la trajectoire mortelle.",
        quote: "« Allumage d'Envisat réussi à T-12 secondes. Trajectoire modifiée de 350 mètres. Impact évité dans la thermosphère. »",
        status: "RÉUSSIE"
    },
    {
        id: 14,
        phase: "phase3",
        title: "14. L'Aveuglement du GPS",
        date: "20 février 2032",
        location: "Île de l'Ascension",
        img: "images/gps_ascension.jpg",
        desc: "Les Veilleurs installent des 'répéteurs fantômes' clandestins près des stations (Ascension, Kwajalein, Cap Canaveral) pour désynchroniser subtilement les horloges atomiques de la constellation GPS. Les Gardiens se déploient simultanément pour installer des 'correcteurs de phase' annulant le délai. Ils découvrent avec effroi que Burke testait et cartographiait en réalité les vulnérabilités de la planète.",
        quote: "« Boîtier correcteur de phase en ligne. Synchronisation temporelle restaurée à la nanoseconde près. GPS opérationnel. »",
        status: "RÉUSSIE"
    },
    {
        id: 15,
        phase: "phase3",
        title: "15. Le Projet Linceul",
        date: "Octobre 2032",
        location: "Cathédrale de Turin, Italie",
        img: "images/turin_shroud.jpg",
        desc: "Les Veilleurs tentent de voler le Saint-Suaire original pour le remplacer par une réplique quantique gravée au laser, prévoyant de la détruire plus tard pour briser la foi mondiale. Les Gardiens poursuivent l'ambulance des fuyards dans les galeries romaines sous-terraines de Turin et piègent les Veilleurs en simulant une fuite massive de gaz naturel, forçant la fermeture automatique des portes anti-explosion.",
        quote: "« Fuite de gaz simulée sous la Piazza. Les portes anti-explosion se feurent automatiquement. Le linceul est récupéré. »",
        status: "RÉUSSIE"
    },
    {
        id: 16,
        phase: "phase3",
        title: "16. Le Voile de Cendres",
        date: "12 novembre 2032",
        location: "Champs Phlégréens, Naples (Italie)",
        img: "images/naples_volcano.jpg",
        desc: "Le vol du Suaire n'était qu'une diversion : Burke tente de réveiller le supervolcan de Naples via 11 résonateurs sismiques profonds enfouis. Couverts par une attaque informatique massive de Keller qui plonge la baie de Naples dans le chaos numérique, les Gardiens s'infiltrent dans les 11 puits et sectionnent les câbles d'alimentation à l'aide d'obturateurs cryo-thermiques.",
        quote: "« Cyber-attaque active. Obturateurs cryo-thermiques enclenchés. La caldeira se rendort. Le supervolcan est désamorcé. »",
        status: "RÉUSSIE"
    },
    {
        id: 17,
        phase: "phase3",
        title: "17. La Cascade Sismique",
        date: "4 juillet 2033",
        location: "Monts Ozarks, Arkansas (USA)",
        img: "images/earthquake_cavern.jpg",
        desc: "Burke place des amplificateurs subsoniques dans des grottes pour décupler la puissance d'un petit séisme et détruire le Midwest (la faille de New Madrid). Keller et Blackwood traquent l'ultime résonateur sismique et le désamorcent quelques secondes avant la secousse, réduisant le cataclysme à un banal séisme de magnitude 5.4.",
        quote: "« Shunt électrique branché sur les résonateurs. L'énergie sismique est dissipée. Magnitude contenue à 5,4. »",
        status: "RÉUSSIE"
    },
    {
        id: 18,
        phase: "phase3",
        title: "18. La Souche Éridanus",
        date: "11 septembre 2033",
        location: "Sierra Nevada, Espagne",
        img: "images/sierra_nevada_lab.jpg",
        desc: "Rébecca et Blackwood s'infiltrent dans un laboratoire de haute sécurité BSL-4 (Altas Cumbres) pour voler l'antidote d'un virus mortel. Détectés et piégés dans un couloir en passe d'être inondé de gaz Halon, they fuient par un conduit d'évacuation d'eau. Rébecca brise une fiole du virus pour forcer l'IA à lancer un protocole de 'Terre Brûlée' (rayonnement gamma), qui détruit toutes les données de recherche de Burke.",
        quote: "« Fiole brisée. Protocole de confinement gamma activé. La souche et le labo de Burke sont entièrement désintégrés. »",
        status: "RÉUSSIE"
    },
    {
        id: 19,
        phase: "phase3",
        title: "19. La Menace Svalbard",
        date: "7 octobre 2033",
        location: "Bunker Arca, Svalbard (Norvège)",
        img: "images/svalbard_assault.jpg",
        desc: "Les Gardiens prennent d'assaut la forteresse personnelle de Burke cachée sous la réserve mondiale de semences. Ils découvrent l'arme ultime : le satellite Genesis-12. Thomas Blackwood se sacrifie courageusement pour retenir un énorme bloc de glace, permettant à l'équipe de fuir avec le disque dur contenant les données de l'arme orbitale.",
        quote: "« Thomas Blackwood s'est sacrifié pour la vérité. Les plans de Genesis-12 sont en sécurité. L'empire de Burke est exposé. »",
        status: "SACRIFICE"
    },
    {
        id: 20,
        phase: "phase3",
        title: "20. Le Grand Final / Genesis-12",
        date: "21 mars 2034",
        location: "Esplanade des Mosquées, Jérusalem",
        img: "images/genesis_12.jpg",
        desc: "Burke lance le satellite Genesis-12 chargé d'antimatière pour créer un micro-trou noir primordial. Depuis Jérusalem, en plaçant le médaillon de Nabonide sur la Pierre Angulaire, Rébecca crée un accordeur harmonique divin. Une particule de pure lumière transmute l'arme mortelle en une inoffensive nova céleste visible sur toute la Terre. Keller s'engouffre dans une faille de maintenance d'urgence, télécharge et diffuse au monde entier toutes les preuves criminelles de Burke, scellant sa chute définitive et l'aube d'un nouveau Millénaire de paix.",
        quote: "« L'antimatière s'est convertie en une nova de lumière céleste inoffensive. L'empire de Burke s'effondre. Le Millénaire de paix débute. »",
        status: "RÉUSSIE"
    }
];

let currentFilter = 'all';

// Dynamic Mission Renderer
function renderMissionsList() {
    const listContainer = document.getElementById('log-list-container');
    if (!listContainer) return;
    
    listContainer.innerHTML = ''; // clear previous

    const filteredData = currentFilter === 'all' 
        ? missionsData 
        : missionsData.filter(m => m.phase === currentFilter);

    // Update count label
    const countLabel = document.getElementById('log-count');
    if (countLabel) countLabel.innerText = `${filteredData.length} MISSIONS`;

    filteredData.forEach((m, idx) => {
        const item = document.createElement('div');
        item.className = `log-item ${idx === 0 ? 'active' : ''}`;
        item.setAttribute('onclick', `selectMission(${m.id}, this)`);
        
        const badgeClass = m.status === 'SACRIFICE' ? 'log-status-badge failed' : 'log-status-badge';
        
        item.innerHTML = `
            <div class="log-item-details">
                <div class="log-item-meta">
                    <span>MISSION ${m.id}</span>
                    <span class="date">${m.date}</span>
                </div>
                <div class="log-item-title">${m.title}</div>
            </div>
            <span class="${badgeClass}">${m.status}</span>
        `;
        listContainer.appendChild(item);

        if (idx === 0) {
            updateBriefingPanel(m);
        }
    });
}

function filterMissions(phase, buttonElement) {
    document.querySelectorAll('.filter-tab').forEach(tab => tab.classList.remove('active'));
    if (buttonElement) buttonElement.classList.add('active');

    currentFilter = phase;
    renderMissionsList();

    playBeep(300, 0.1, 0.02);
}

function selectMission(id, element) {
    document.querySelectorAll('.log-item').forEach(item => item.classList.remove('active'));
    if (element) element.classList.add('active');

    const m = missionsData.find(item => item.id === id);
    const briefing = document.getElementById('briefing-panel');
    if (!briefing) return;
    
    briefing.style.opacity = 0;
    briefing.style.transform = 'translateY(10px)';
    briefing.style.transition = 'all 0.3s ease';

    setTimeout(() => {
        updateBriefingPanel(m);
        briefing.style.opacity = 1;
        briefing.style.transform = 'translateY(0)';
    }, 300);

    playBeep(400 + id * 25, 0.15, 0.02);
}

function updateBriefingPanel(m) {
    const imgBox = document.getElementById('briefing-img-box');
    if (!imgBox) return;

    if (m.img) {
        imgBox.innerHTML = `<img src="${m.img}" alt="${m.title}" id="briefing-img">`;
    } else {
        imgBox.innerHTML = `
            <div class="map-radar-fallback">
                <div class="map-radar-grid"></div>
                <div class="map-radar-sweep"></div>
                <div class="map-radar-crosshair"></div>
            </div>
        `;
    }

    document.getElementById('briefing-num').innerText = `MISSION ${m.id} / 20`;
    document.getElementById('briefing-date').innerText = m.date.toUpperCase();
    document.getElementById('briefing-location').innerText = m.location.toUpperCase();
    document.getElementById('briefing-title').innerText = m.title;
    document.getElementById('briefing-desc').innerText = m.desc;
    
    const quoteCard = document.getElementById('briefing-quote');
    if (quoteCard) {
        quoteCard.innerText = m.quote;
        if (m.status === 'SACRIFICE') {
            quoteCard.className = 'briefing-quote-card failed';
        } else {
            quoteCard.className = 'briefing-quote-card';
        }
    }
}


/* === MAIN CINEMATIC PLAYER LOGIC (W01/W03) === */
document.addEventListener('DOMContentLoaded', () => {
    // Populate log entries on start
    renderMissionsList();

    const playerWrapper = document.getElementById('cinema-player-wrapper');
    const video = document.getElementById('cinema-trailer-video');
    const playOverlay = document.getElementById('custom-play-overlay');
    const progressBar = document.getElementById('custom-progress-bar');
    const progressContainer = document.getElementById('custom-progress-container');
    const viewsCountElement = document.getElementById('views-count');

    if (!video || !playerWrapper) return;

    // Simulate animated views counter
    let simulatedViews = 127640;
    setInterval(() => {
        if (Math.random() > 0.4) {
            simulatedViews += Math.floor(Math.random() * 3) + 1;
            if (viewsCountElement) {
                viewsCountElement.innerText = simulatedViews.toLocaleString('fr-FR');
            }
        }
    }, 4000);

    function togglePlay() {
        if (video.paused) {
            if (window.audioCtx && window.isPlaying) {
                toggleAudio(); // Pause synth soundscape to prevent overlap
            }
            playerWrapper.classList.add('playing');
            playerWrapper.classList.remove('loading');
            video.play();
        } else {
            video.pause();
            playerWrapper.classList.remove('playing');
        }
    }

    playOverlay.addEventListener('click', togglePlay);
    video.addEventListener('click', togglePlay);

    video.addEventListener('play', () => {
        playerWrapper.classList.add('playing');
    });

    video.addEventListener('pause', () => {
        playerWrapper.classList.remove('playing');
    });

    video.addEventListener('timeupdate', () => {
        if (video.duration) {
            const percentage = (video.currentTime / video.duration) * 100;
            progressBar.style.width = `${percentage}%`;
        }
    });

    progressContainer.addEventListener('click', (e) => {
        const rect = progressContainer.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const width = rect.width;
        const clickPercentage = clickX / width;
        video.currentTime = clickPercentage * video.duration;
    });

    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (video.muted && video.paused) {
                    playerWrapper.classList.add('playing');
                    video.play().catch(err => console.log('Autoplay blocked:', err));
                }
            } else {
                if (!video.paused) {
                    video.pause();
                    playerWrapper.classList.remove('playing');
                }
            }
        });
    }, options);

    observer.observe(video);

    // Full Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
        const rect = video.getBoundingClientRect();
        const inView = (rect.top >= -rect.height && rect.bottom <= window.innerHeight + rect.height);
        if (!inView) return;

        switch (e.key.toLowerCase()) {
            case ' ':
                e.preventDefault();
                togglePlay();
                break;
            case 'f':
                e.preventDefault();
                if (!document.fullscreenElement) {
                    playerWrapper.requestFullscreen().catch(err => {
                        console.log(`Error: ${err.message}`);
                    });
                } else {
                    document.exitFullscreen();
                }
                break;
            case 'm':
                e.preventDefault();
                video.muted = !video.muted;
                break;
        }
    });

    // Share Buttons Logic
    const shareBtns = document.querySelectorAll('.btn-share');
    shareBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const url = window.location.href;
            const text = "Découvrez la bande-annonce grandiose du thriller 'Le Plus Grand des Secrets' !";
            const btnText = btn.innerText;

            if (btnText.includes('FACEBOOK')) {
                window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
            } else if (btnText.includes('TWITTER') || btnText.includes('X')) {
                window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`, '_blank');
            } else if (btnText.includes('LIEN')) {
                navigator.clipboard.writeText(url).then(() => {
                    const origText = btn.innerText;
                    btn.innerText = "LIEN COPIÉ !";
                    btn.style.color = "var(--accent)";
                    setTimeout(() => {
                        btn.innerText = origText;
                        btn.style.color = "var(--text-muted)";
                    }, 2000);
                });
            }
        });
    });
});
