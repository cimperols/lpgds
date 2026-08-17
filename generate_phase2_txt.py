import re

# Kling 3.0 Prompts file
kling_prompts = """============================================================
PROMPTS VIDÉO OPTIMISÉS POUR KLING 3.0 - "LE PLUS GRAND DES SECRETS"
============================================================

Chaque prompt ci-dessous est conçu pour exploiter au maximum les capacités de rendu photoréaliste, de gestion des mouvements rapides et de simulation physique de Kling 3.0.

---

S01 | Plan d'Ouverture : Les Ruines de Babylone
------------------------------------------------------------
[SHOT TYPE] : Aerial crane shot ultra-wide, sweeping slowly downward and pushing in.
[SUBJECT]   : The majestic archaeological ruins of ancient Babylon in Iraq at night. Desert wind gently blowing golden sand over collapsed stone pillars and brick walls.
[ACTION]    : In a deep dark excavation trench, an ancient clay tablet with concentric circular inscriptions and cuneiform symbols begins to glow with a faint, pulsing warm golden light.
[LIGHTING]  : Moody night lighting, a pale crescent moon in a dark purple sky, soft volumetric god rays catching the dust particles.
[STYLE]     : Cinematic 4K, 35mm film grain, 24fps, high contrast, anamorphic lens flares, photorealistic.
[MOTION]    : Slow, deliberate, breathtaking reveal.
[NEGATIVE]  : no text, no watermarks, no camera shake, no cartoon style, no modern elements.

---

S02 | L'Assassinat d'Elijah (Le Campement)
------------------------------------------------------------
[SHOT TYPE] : Handheld medium shot, low angle, slight camera shake.
[SUBJECT]   : An archaeological campsite tent in the desert, illuminated from inside by a flickering yellow lamp, casting dramatic shadows.
[ACTION]    : A sudden burst of gunfire flashes inside the tent, tearing the canvas, followed by an immediate blackout. A single old map stained with fresh blood drops lies on a wooden desk.
[LIGHTING]  : High contrast chiaroscuro, harsh muzzle flashes, pitch black exterior night.
[STYLE]     : Suspense thriller aesthetic, raw, gritty realism, 4K, 24fps, sharp details.
[MOTION]    : Dynamic camera movement.
[NEGATIVE]  : no text, no blur, no watermarks.

---

S03 | La Traque de Princeton : Rébecca Shepherd
------------------------------------------------------------
[SHOT TYPE] : Tight close-up tracking shot on a face.
[SUBJECT]   : A beautiful, exhausted young female mathematician (Rébecca Shepherd), her dark eyes wide with alarm, reflecting glowing green code from her screen.
[ACTION]    : She quickly shuts her laptop, grabs her leather jacket, and looks toward the office window where cold blue police lights and flashlight beams sweep through the rain-slicked glass.
[LIGHTING]  : Moody rain-slicked window light, harsh blue and white beams piercing the office darkness, high contrast.
[STYLE]     : Gritty techno-thriller aesthetic, realistic skin texture, shallow depth of field, 4K, anamorphic bokeh.
[MOTION]    : Quick push-in and panning.
[NEGATIVE]  : no text, no watermarks.

---

S04 | Le QG des Gardiens : Alex Keller
------------------------------------------------------------
[SHOT TYPE] : Low-angle medium shot, slow dolly forward.
[SUBJECT]   : A high-tech clandestine underground crypt in Prague. A bald hacker with intense steel-gray eyes (Alex Keller) wearing a black hoodie, standing before a massive wall of glowing screens displaying map logs and binary code.
[ACTION]    : He turns his head slowly towards the camera, typing one last command on a virtual holographic interface, a green checkmark flashing.
[LIGHTING]  : Cold emerald-green and warm gold backlight, dramatic rim lighting, moody industrial atmosphere.
[STYLE]     : Anamorphic lens, cyberpunk meets gothic architecture, photorealistic 4K, desaturated colors.
[MOTION]    : Smooth camera push-in.
[NEGATIVE]  : no text, no watermarks.

---

S05 | L'Échappée du CERN (Confinement)
------------------------------------------------------------
[SHOT TYPE] : Tracking action shot, handheld camera.
[SUBJECT]   : Rébecca and Alex Keller sprinting through the metallic, glowing service tunnels of the CERN Large Hadron Collider.
[ACTION]    : Behind them, massive steel guillotine-like blast doors slam shut with sparks flying, cryogenic white helium steam spraying into the red emergency lit corridor.
[LIGHTING]  : Flashing red and blue warning beacons, harsh metal reflections, high contrast.
[STYLE]     : Action thriller, immersive, 24fps with realistic motion blur, visceral, ultra-sharp 4K.
[MOTION]    : Fast-paced forward running.
[NEGATIVE]  : no cartoon, no anime, no watermarks, no cheap effects.

---

S06 | Le Tsunami des Açores (La vague)
------------------------------------------------------------
[SHOT TYPE] : Epic extreme wide aerial shot (drone).
[SUBJECT]   : A colossal ocean wave (tsunami) rising under a hellish stormy sky, approaching the rocky coast of Portugal.
[ACTION]    : Highly advanced glowing wave-barriers and geo-textile structures anchored in the water pulse with yellow light as they absorb the impact of the dark water.
[LIGHTING]  : Dim, stormy, lightning flashes illuminating the sky and the white foam of the wave.
[STYLE]     : Blockbuster disaster scale, highly photorealistic, 4K, dark color grading.
[MOTION]    : Slow majestic drone panning.
[NEGATIVE]  : no text, no watermarks, no blur.

---

S07 | La Menace Finale : Nathanaël Burke
------------------------------------------------------------
[SHOT TYPE] : Low angle reverse dolly shot.
[SUBJECT]   : The main antagonist, Nathanaël Burke, a handsome, cold billionaire in an elegant charcoal suit, standing in his penthouse office overlooking London's glowing skyscrapers.
[ACTION]    : He slowly turns around, holding an ancient gold medal in his hand, a chilling, superior smile on his face as his eyes catch the window reflections of the city lights.
[LIGHTING]  : Dark, luxurious interior, dramatic amber rim lighting from the city behind him, dark shadow foreground.
[STYLE]     : Modern villain aesthetic, sleek, photorealistic 4K, anamorphic reflection.
[MOTION]    : Slow, imposing pullback.
[NEGATIVE]  : no humor, no cartoon, no bright colors, no text.

---

S08 | KLING MULTI-SHOT : Enchaînement d'Action Élite
------------------------------------------------------------
Master context: Elite supernatural Guardians defending an ancient secret in a dark modern world. Characters wear tactical field jackets and hoodies.
Color palette: Deep gold, obsidian black, cold steel blue, electric emerald code.

[Shot 1 - 0-2s]: Dynamic tracking shot. A tactical agent (Thomas Blackwood) sliding on wet subway tracks, firing his service weapon in slow motion, muzzle flashes illuminating the dark concrete arches.
[Shot 2 - 2-4s]: Medium shot, low-angle. An engineer (David) standing in a cave, connecting shunts on a glowing seismic resonator, sparks flying as a shockwave ripples through the cavern dust.
[Shot 3 - 4-5s]: Wide shot. Rébecca Shepherd and Alex Keller standing together against a massive cyber-glitch screen, looking up at a glowing digital grid of the earth as it turns from red to emerald green.

Style: Cinematic 4K, anamorphic lens, 24fps, color graded for maximum dramatic impact. No watermarks.
"""

# Veo 3.1 Prompts file (with audio)
veo_prompts = """============================================================
PROMPTS VIDÉO OPTIMISÉS POUR VEO 3.1 (AVEC DIRECTIVES AUDIO)
============================================================

Veo 3.1 est optimisé pour les plans de paysages très détaillés, les mouvements de caméra lents et atmosphériques, et l'intégration d'un environnement sonore natif de haute qualité.

---

S01_VEO | L'Ouverture Cosmique de Babylone (Audio Inclus)
------------------------------------------------------------
[CINEMATOGRAPHY]: Slow crane shot rising above ancient brick stone ruins in the Iraqi desert, moving from low angle to high wide aerial perspective.
[SUBJECT]: The archaeological site of Babylon at night under a giant pale crescent moon, dust and sand blowing slowly over broken pillars.
[ACTION]: In a deep dark trench, a circular clay tablet with golden concentric cuneiform inscriptions pulses with a faint, warm divine light.
[STYLE]: Epic cinematic, volumetric moonlight, anamorphic lens flare, photorealistic 4K HDR.
[AMBIANCE]: Ancient, desolated, mysterious and holy.
[AUDIO]: Howling desert wind, whispers of ancient languages, deep bass drone (Braam) at the end.
[NEGATIVE]: no voiceover, no text, no modern elements.

---

S02_VEO | La Chute des Abeilles en Californie (Audio Inclus)
------------------------------------------------------------
[CINEMATOGRAPHY]: Steady camera macro tracking shot, shallow depth of field.
[SUBJECT]: A massive swarm of golden honeybees flying through a sunlit almond orchard in California.
[ACTION]: The bees are flying erratically. Ethereal, translucent concentric ripples of blue and orange soundwaves vibrate through the sunbeams, representing acoustic interference.
[STYLE]: Cinematic warm colors, high-speed camera rendering, crystalline 4K.
[AMBIANCE]: Organic, chaotic, high-pitched vibrational frequency.
[AUDIO]: Thousands of bees buzzing, low humming acoustic vibration generator, sudden static interference sound.
[NEGATIVE]: no humans, no text overlays, no cheap 3D render.

---

S03_VEO | Le Glacier du Jugement Dernier (Audio Inclus)
------------------------------------------------------------
[CINEMATOGRAPHY]: Immersive slow dolly forward, underwater to half-submerged camera view.
[SUBJECT]: The deep frozen ice caves below the Thwaites Glacier in Antarctica.
[ACTION]: Glowing orange-red high-tech isotope drills are melting holes in the dark blue ice cliffs. A remotely operated submarine (ROV Styx) with bright white searchlights moves through the bubbles.
[STYLE]: Cold cyan and deep blue color grading, realistic water physics, high detail 4K.
[AMBIANCE]: Claustrophobic, frozen tension, massive scale.
[AUDIO]: Deep groan of cracking polar ice, underwater bubbles, high-tech engine hum of the ROV, heavy metallic clank.
[NEGATIVE]: no text overlays, no cartoon, no bright sun.

---

S04_VEO | Le Climax de Jérusalem (Audio Inclus)
------------------------------------------------------------
[CINEMATOGRAPHY]: Symmetric wide static shot, perfectly centered.
[SUBJECT]: The Dome of the Rock in Jerusalem bathed in a blinding golden morning sunset.
[ACTION]: From the sacred stone courtyard, a vertical pillar of blinding white diamond light shoots straight into the heavens, parting the dark storm clouds in a ring of energy. The beam converts into a silent, sparkling nova flower of pure light.
[STYLE]: Biblical majesty, divine reveal, breathtaking photorealistic render, 4K HDR.
[AMBIANCE]: Glorious, triumphant, cosmic balance restored.
[AUDIO]: Majestic cathedral brass choir (epic crescendo), thunderous geomagnetic resonance hum, followed by crystalline wind chimes and absolute silence.
[NEGATIVE]: no text, no watermarks, no crowds.
"""

with open("prompts_kling30.txt", "w", encoding="utf-8") as f:
    f.write(kling_prompts)
print("prompts_kling30.txt generated!")

with open("prompts_veo31.txt", "w", encoding="utf-8") as f:
    f.write(veo_prompts)
print("prompts_veo31.txt generated!")
