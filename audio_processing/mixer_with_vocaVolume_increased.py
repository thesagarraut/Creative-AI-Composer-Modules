from pydub import AudioSegment

print("\n===== AUDIO MIXING MODULE =====\n")

# Load instrumental
instrumental = AudioSegment.from_wav(
    "../outputs/instrumental/instrumental.wav"
)

# Load BPM aligned vocals
vocals = AudioSegment.from_wav(
    "../outputs/vocals/vocals_aligned.wav"
)

# Adjust volumes
instrumental = instrumental - 5   # reduce music volume
vocals = vocals + 3               # increase vocal volume

# Mix tracks
final_song = instrumental.overlay(vocals)

# Export final output
final_song.export(
    "../outputs/final_songs/final_song.wav",
    format="wav"
)

print("Final song created successfully")