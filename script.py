from transformers import pipeline
import os

os.environ["REQUESTS_CA_BUNDLE"] = "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"

asr = pipeline(
    "automatic-speech-recognition",
    "NbAiLab/nb-whisper-medium-beta"
)
text = asr(
    "data/2023_10_05-0710-siste_nytt_vg.mp3",
    generate_kwargs={'task': 'transcribe', 'language': 'no'},
    return_timestamps=True,
)
print(text)