with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update togglePlay in initCinemaPlayer
old_toggle_play = """             function togglePlay() {
                 if (video.paused) {
                     if (window.audioCtx && window.isPlaying) {
                         toggleAudio(); // Pause synth soundscape to prevent overlap
                     }
                     playerWrapper.classList.add('playing');
                     playerWrapper.classList.remove('loading');
                     const p = video.play();
                     if (p && typeof p.catch === 'function') {
                         p.catch(err => console.log('Playback error:', err));
                     }
                 } else {
                     video.pause();
                     playerWrapper.classList.remove('playing');
                 }
             }"""

new_toggle_play = """             function togglePlay() {
                 const overlay = document.getElementById('lights-out-overlay');
                 if (video.paused) {
                     if (window.audioCtx && window.isPlaying) {
                         toggleAudio(); // Pause synth soundscape to prevent overlap
                     }
                     playerWrapper.classList.add('playing');
                     playerWrapper.classList.remove('loading');
                     if (overlay) {
                         overlay.classList.add('active');
                         playerWrapper.classList.add('lights-out');
                     }
                     const p = video.play();
                     if (p && typeof p.catch === 'function') {
                         p.catch(err => console.log('Playback error:', err));
                     }
                 } else {
                     video.pause();
                     playerWrapper.classList.remove('playing');
                     if (overlay) {
                         overlay.classList.remove('active');
                         playerWrapper.classList.remove('lights-out');
                     }
                 }
             }"""

if old_toggle_play in html:
    html = html.replace(old_toggle_play, new_toggle_play)
    print("togglePlay updated!")
else:
    # Try fuzzy spacing
    print("Old togglePlay not found exactly!")

# 2. Add pause and ended listeners inside initCinemaPlayer
old_play_listener = """             video.addEventListener('play', () => {
                 playerWrapper.classList.add('playing');
             });"""

new_play_listeners = """             video.addEventListener('play', () => {
                 playerWrapper.classList.add('playing');
             });

             video.addEventListener('pause', () => {
                 const overlay = document.getElementById('lights-out-overlay');
                 playerWrapper.classList.remove('playing');
                 if (overlay) {
                     overlay.classList.remove('active');
                     playerWrapper.classList.remove('lights-out');
                 }
             });

             video.addEventListener('ended', () => {
                 const overlay = document.getElementById('lights-out-overlay');
                 playerWrapper.classList.remove('playing');
                 if (overlay) {
                     overlay.classList.remove('active');
                     playerWrapper.classList.remove('lights-out');
                 }
             });"""

if old_play_listener in html:
    html = html.replace(old_play_listener, new_play_listeners)
    print("Video play/pause/ended listeners updated!")
else:
    print("Old play listener not found!")

# 3. Add premium setups and preloader listener
old_setups = """        /* === TASK REVEALS & MENUS INTERACTION CODES === */
        function setupHamburgerMenu() {"""

new_setups_and_preloader = """        /* === TASK REVEALS & MENUS INTERACTION CODES === */
        // Task 1: Preloader fade-out
        window.addEventListener('load', () => {
            const preloader = document.getElementById('preloader');
            if (preloader) {
                setTimeout(() => {
                    preloader.style.opacity = '0';
                    preloader.style.pointerEvents = 'none';
                }, 800);
            }
        });

        // Task 3: 3D Magnetic Tilt effect
        function setupBookTilt() {
            const isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
            if (isTouch) return;

            const targets = [
                { parent: '.book-wrapper', element: '#flippable-book-hero' },
                { parent: '.promo-book-stand', element: '.promo-book-3d' }
            ];

            targets.forEach(t => {
                const parent = document.querySelector(t.parent);
                const el = document.querySelector(t.element);
                if (!parent || !el) return;

                parent.addEventListener('mousemove', (e) => {
                    if (el.style.transform && el.style.transform.includes('rotateY(180deg)')) return;

                    const rect = el.getBoundingClientRect();
                    const elX = rect.left + rect.width / 2;
                    const elY = rect.top + rect.height / 2;

                    const mouseX = e.clientX;
                    const mouseY = e.clientY;

                    const rotY = ((mouseX - elX) / (rect.width / 2)) * 15;
                    const rotX = -((mouseY - elY) / (rect.height / 2)) * 15;

                    el.style.transition = 'none';
                    el.style.transform = `rotateY(${rotY}deg) rotateX(${rotX}deg)`;
                });

                parent.addEventListener('mouseleave', () => {
                    if (el.style.transform && el.style.transform.includes('rotateY(180deg)')) return;
                    el.style.transition = 'transform 0.5s ease';
                    el.style.transform = 'rotateY(-15deg) rotateX(10deg)';
                });
            });
        }

        function setupHamburgerMenu() {"""

if old_setups in html:
    html = html.replace(old_setups, new_setups_and_preloader)
    print("Premium setups and preloader added successfully!")
else:
    print("Old setups starting line not found!")

# 4. Update initAll to include setups
old_init_all = """        function initAll() {
            renderMissionsList();
            initCinemaPlayer();
            selectInventoryCategory('artifacts', document.querySelector('.inventory-tab-btn'));
            selectLoreCategory('factions', document.querySelector('.lore-tab-btn'));
            
            // Init mobile/UX additions
            setupHamburgerMenu();
            setupFloatingCTA();
            setupScrollReveal();
        }"""

new_init_all = """        function initAll() {
            renderMissionsList();
            initCinemaPlayer();
            selectInventoryCategory('artifacts', document.querySelector('.inventory-tab-btn'));
            selectLoreCategory('factions', document.querySelector('.lore-tab-btn'));
            
            // Init mobile/UX additions
            setupHamburgerMenu();
            setupFloatingCTA();
            setupScrollReveal();
            
            // Init premium interactions
            setupBookTilt();
            
            // Link sound-toggle-btn with Web Audio API
            const soundBtn = document.getElementById('sound-toggle-btn');
            if (soundBtn) {
                soundBtn.addEventListener('click', toggleAudio);
            }
        }"""

if old_init_all in html:
    html = html.replace(old_init_all, new_init_all)
    print("initAll modified with premium features!")
else:
    print("Old initAll block not found exactly!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
