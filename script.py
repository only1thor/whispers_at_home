from transformers import pipeline
import os

os.environ["REQUESTS_CA_BUNDLE"] = "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"

asr = pipeline(
    "automatic-speech-recognition",
    "NbAiLab/nb-whisper-medium-beta",
    chunk_length_s=10
)
text = asr(
    "data/out.wav",
    generate_kwargs={'task': 'transcribe', 'language': 'no'},
    return_timestamps=True,
    batch_size=2
)
for chunk in text['chunks']:
    print(chunk['timestamp'])
    print(chunk['text'])
print("done")
