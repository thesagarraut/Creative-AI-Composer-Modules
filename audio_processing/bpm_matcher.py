import librosa
import soundfile as sf

# File paths
instrumental_path = "../outputs/instrumental/instrumental.wav"
vocals_path = "../outputs/vocals/vocals.wav"
aligned_vocals_path = "../outputs/vocals/vocals_aligned.wav"

print("\n===== BPM MATCHING MODULE =====\n")

# Load instrumental
print("Loading instrumental...")
y_inst, sr_inst = librosa.load(instrumental_path)

# Detect BPM of instrumental
tempo_inst, _ = librosa.beat.beat_track(y=y_inst, sr=sr_inst)
print(f"Instrumental BPM: {tempo_inst:.2f}")

# Load vocals
print("Loading vocals...")
y_voc, sr_voc = librosa.load(vocals_path)

# Detect BPM of vocals
tempo_voc, _ = librosa.beat.beat_track(y=y_voc, sr=sr_voc)
print(f"Vocals BPM: {tempo_voc:.2f}")

# Calculate stretch factor
stretch_factor = tempo_voc / tempo_inst

print(f"Stretch factor: {stretch_factor:.3f}")

# Time-stretch vocals
print("Aligning vocals tempo...")
y_voc_aligned = librosa.effects.time_stretch(y_voc, rate=stretch_factor)

# Save aligned vocals
sf.write(aligned_vocals_path, y_voc_aligned, sr_voc)

print("\nVocals aligned successfully!")
print("Saved file:", aligned_vocals_path)