import re

def marathi_tokenize(text):

    words = text.split()
    tokens = []

    for w in words:

        # split after matras
        parts = re.findall(r'[क-ह][्]?[ा-ौ]?|[अ-औ]|ं|ः', w)
	parts = [p for p in parts if p.strip()]

        tokens.extend(parts)

    return " ".join(tokens)


# read lyrics
with open("../lyrics.txt","r",encoding="utf-8") as f:
    lyrics = f.read().strip()

tokenized = marathi_tokenize(lyrics)

print("Tokenized:")
print(tokenized)

# save
with open("../lyrics_tokenized.txt","w",encoding="utf-8") as f:
    f.write(tokenized)