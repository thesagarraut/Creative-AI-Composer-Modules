import subprocess
import shutil
import os

print("\n===== DIFFSINGER INFERENCE =====\n")

command = [
    "python",
    "scripts/infer.py",
    "acoustic",
    "input.ds",
    "--exp", "marathi_exp",
    "--ckpt", "20000",
    "--out", "generated_vocals"
]

subprocess.run(command, cwd="/home/sagar/DiffSinger")

print("Vocals generated successfully")

# Copy generated audio to project output folder
src = "/home/sagar/DiffSinger/generated_vocals/test.wav"
dst = "../outputs/vocals/vocals.wav"

if os.path.exists(src):
    shutil.copy(src, dst)
    print("Vocals copied to outputs/vocals/vocals.wav")
else:
    print("Error: generated vocals not found")