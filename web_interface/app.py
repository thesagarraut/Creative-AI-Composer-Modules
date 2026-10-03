import gradio as gr
import subprocess

def generate_song(prompt, lyrics):

    # Save lyrics
    with open("../lyrics.txt","w",encoding="utf-8") as f:
        f.write(lyrics)

    # Save prompt
    with open("../prompt.txt","w",encoding="utf-8") as f:
        f.write(prompt)

    # Run pipeline
    subprocess.run(["python","../pipeline/generate_song.py"])

    return "../outputs/final_songs/final_song.wav"


interface = gr.Interface(

    fn=generate_song,

    inputs=[
        gr.Textbox(label="Music Prompt"),
        gr.Textbox(label="Lyrics")
    ],

    outputs=gr.Audio(label="Generated Song"),

    title="Creative AI Composer",
    description="Generate original songs from prompts and lyrics"
    flagging_mode="never"
)

interface.launch()