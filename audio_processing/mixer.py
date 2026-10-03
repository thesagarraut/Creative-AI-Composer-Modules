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

# Volume balancing
#instrumental = instrumental - 5
#vocals = vocals + 3

# Duration matching
inst_len = len(instrumental)
voc_len = len(vocals)

if voc_len < inst_len:
    print("Padding vocals with silence")
    silence = AudioSegment.silent(duration=(inst_len - voc_len))
    vocals = vocals + silence

elif voc_len > inst_len:
    print("Trimming vocals")
    vocals = vocals[:inst_len]

# Mix tracks
final_song = instrumental.overlay(vocals)

# Export final output
final_song.export(
    "../outputs/final_songs/final_song.wav",
    format="wav"
)

print("Final song created successfully")