from transformers import MusicgenForConditionalGeneration, AutoProcessor
import torch
import scipy.io.wavfile as wavfile

print("\n===== MUSICGEN MODULE =====\n")

# Load saved MusicGen model
model_path = "../musicgen_model"

processor = AutoProcessor.from_pretrained(model_path)
model = MusicgenForConditionalGeneration.from_pretrained(model_path)

model.eval()

# Read prompt from UI input file
with open("../prompt.txt","r",encoding="utf-8") as f:
    prompt = f.read().strip()

print("Prompt:", prompt)

# Process input
inputs = processor(
    text=[prompt],
    padding=True,
    return_tensors="pt"
)

# Generate music
audio_values = model.generate(**inputs, max_new_tokens=1024)

sampling_rate = model.config.audio_encoder.sampling_rate

# Save instrumental
wavfile.write(
    "../outputs/instrumental/instrumental.wav",
    rate=sampling_rate,
    data=audio_values[0,0].cpu().numpy()
)

print("Instrumental generated successfully")