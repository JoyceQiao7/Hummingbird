from fish_audio_sdk import Session, TTSRequest, ReferenceAudio
import os

session = Session("2532b1a62f144983b5adf45e4a625f19")

# Option 1: Using a reference_id
with open("output1.mp3", "wb") as f:
    for chunk in session.tts(TTSRequest(
        reference_id="03397b4c4be74759b72533b663fbd001",
        # insert text here:
        text="But on the edge of town, drills were driven out of his mind by something else. As he sat in the usual morning traffic jam, he couldn’t help noticing that there seemed to be a lot of strangely dressed people about. People in cloaks. Mr Dursley couldn’t bear people who dressed in funny clothes — the getups you saw on young people! He supposed this was some stupid new fashion. He drummed his fingers on the steering wheel and his eyes fell on a huddle of these weirdos standing quite close by."
    )):
        f.write(chunk)

'''
# Option 2: Using reference audio
with open("reference_audio.mp3", "rb") as audio_file:
    with open("output2.mp3", "wb") as f:
        for chunk in session.tts(TTSRequest(
            text="Hello, world!",
            references=[
                ReferenceAudio(
                    audio=audio_file.read(),
                    text="Text in reference audio",
                )
            ]
        )):
            f.write(chunk)
'''

