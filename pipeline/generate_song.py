import subprocess

print("\n===== AI Composer Pipeline Started =====\n")

# Step 1: Generate instrumental using MusicGen
print("Step 1: Generating instrumental...")
subprocess.run(
    ["python", "../musicgen_module/generate_instrumental.py"]
)

print("Step 2.0: Tokenizing lyrics...")
subprocess.run(
["python","../lyrics_processing/tokenizer.py"]
)

# Step 2.1: Generate melody (notes + durations)
print("Step 2.1: Generating melody...")
subprocess.run(
    ["python", "../lyrics_processing/melody_generator.py"]
)

print("Step 3.0:Creating DiffSinger .ds...")
subprocess.run(
["python","../lyrics_processing/create_diffsinger_json.py"]
)

# Step 3.1: Generate vocals using DiffSinger
print("Step 3.1: Generating vocals...")
subprocess.run(
    ["python", "../diffsinger_module/generate_vocals.py"]
)

#Step 4: BPM matching
print("Step 4: Matching BPM...")
subprocess.run(
    ["python", "../audio_processing/bpm_matcher.py"]
)


# Step 5: Mix instrumental and vocals
print("Step 5: Mixing audio...")
subprocess.run(
    ["python", "../audio_processing/mixer.py"]
)

print("\n===== SONG GENERATION COMPLETE =====\n")
print("Final song saved in: outputs/final_songs/")