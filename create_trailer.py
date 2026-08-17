import os
import subprocess

scene_duration = 4.0  # 20 seconds total

scenes = [
    {
        "img": "images/babylon.jpg",
        "text": "Un secret vieux de 4000 ans...",
        "font_size": "32",
        "tone": 110,
    },
    {
        "img": "images/princeton.jpg",
        "text": "Une confrerie millenaire - Les Gardiens.",
        "font_size": "28",
        "tone": 130,
    },
    {
        "img": "images/cern.jpg",
        "text": "Un compte a rebours ineluctable vers 2034.",
        "font_size": "26",
        "tone": 160,
    },
    {
        "img": "images/jerusalem.jpg",
        "text": "L apocalypse n est pas une fin. C est un rendez-vous.",
        "font_size": "22",
        "tone": 220,
    },
    {
        "img": "book_cover.jpg",
        "text": "LE PLUS GRAND DES SECRETS",
        "font_size": "34",
        "font_color": "yellow",
        "tone": 147,
    }
]

clips = []
for idx, scene in enumerate(scenes):
    out_clip = f"scene_{idx}.mp4"
    img = scene["img"]
    txt = scene["text"]
    size = scene["font_size"]
    color = scene.get("font_color", "white")
    tone_f = scene["tone"]
    
    # Scale down scale=3000:-1 instead of 8000 to drastically optimize RAM / cpu usage and prevent SIGKILL!
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", img,
        "-f", "lavfi", "-i", f"sine=frequency={tone_f}:duration={scene_duration}",
        "-filter_complex",
        f"[0:v]scale=3000:-1,zoompan=z='zoom+0.0015':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=240:s=1280x720,"
        f"drawtext=text='{txt}':x=(w-text_w)/2:y=h-100:fontcolor={color}:fontsize={size}:"
        f"box=1:boxcolor=black@0.65:boxborderw=15,fade=t=in:st=0:d=1,fade=t=out:st=3:d=1[v];"
        f"[1:a]afade=t=in:st=0:d=1,afade=t=out:st=3:d=1[a]",
        "-map", "[v]", "-map", "[a]",
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-r", "60", "-c:a", "aac", "-b:a", "192k",
        "-t", str(scene_duration), out_clip
    ]
    
    print(f"Generating scene {idx+1}...")
    subprocess.run(cmd, check=True)
    clips.append(out_clip)

# Concatenate all clips
with open("list.txt", "w") as f:
    for c in clips:
        f.write(f"file '{c}'\n")

print("Concatenating clips into final trailer...")
concat_cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0", "-i", "list.txt",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
    "assets/videos/trailer_gardiens.mp4"
]
subprocess.run(concat_cmd, check=True)

# Cleanup
for c in clips:
    os.remove(c)
os.remove("list.txt")
print("Trailer successfully generated at assets/videos/trailer_gardiens.mp4!")
