def lyrics_to_phoneme(lyrics):

    phonemes = []

    for word in lyrics.split():
        phonemes.append(word)

    return " ".join(phonemes)


with open("lyrics.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

phoneme_seq = lyrics_to_phoneme(lyrics)

print("Phoneme sequence:")
print(phoneme_seq)