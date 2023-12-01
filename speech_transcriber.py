import argparse
from google.cloud import speech

def transcribe_file_with_auto_punctuation(path: str) -> speech.RecognizeResponse:
    client = speech.SpeechClient()

    with open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=8000,
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)
    return response
