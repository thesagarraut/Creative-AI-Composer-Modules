import json

# read tokenized lyrics
with open("../lyrics_tokenized.txt","r",encoding="utf-8") as f:
    text = f.read().strip()

# read notes
with open("../notes.txt","r") as f:
    note_seq = f.read().strip()

# read durations
with open("../durations.txt","r") as f:
    note_dur = f.read().strip()

# for simplicity ph_seq = text
ph_seq = text

# phoneme duration same as note duration
ph_dur = note_dur

# simple f0 sequence (can be improved later)
num_notes = len(note_seq.split())
f0_values = [220 + i*5 for i in range(num_notes)]
f0_seq = " ".join(str(v) for v in f0_values)

data = [{
    "name": "sample1",
    "text": text,
    "ph_seq": ph_seq,
    "note_seq": note_seq,
    "note_dur": note_dur,
    "ph_dur": ph_dur,
    "f0_seq": f0_seq,
    "f0_timestep": 0.01
}]

# save .ds
with open("../diffsinger_module/input.ds","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

print("DiffSinger JSON created successfully")