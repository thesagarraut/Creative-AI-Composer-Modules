import random

# Musical scale notes
scale = ["C4","D4","E4","F4","G4","A4"]

def generate_melody(tokens):

    notes = []
    durations = []

    for t in tokens:
        notes.append(random.choice(scale))
        durations.append(round(random.uniform(0.3,0.7),2))

    return notes, durations


# Read lyrics
with open("../lyrics.txt","r",encoding="utf-8") as f:
    lyrics = f.read()

# Tokenize similar to training format
tokens = lyrics.split()

notes, durations = generate_melody(tokens)

print("\nTOKENS:\n",tokens)
print("\nNOTES:\n"," ".join(notes))
print("\nDURATIONS:\n"," ".join(map(str,durations)))


# Save outputs
with open("../notes.txt","w") as f:
    f.write(" ".join(notes))

with open("../durations.txt","w") as f:
    f.write(" ".join(map(str,durations)))