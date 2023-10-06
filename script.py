from transformers import pipeline
import os
import time

os.environ["REQUESTS_CA_BUNDLE"] = "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"

filename = "2023_10_05-0710-siste_nytt_vg"

asr = pipeline(
    "automatic-speech-recognition",
    "NbAiLab/nb-whisper-medium-beta",
    chunk_length_s=10
)
# Record the start time
start_time = time.time()
text = asr(
    f"data/{filename}.wav",
    generate_kwargs={'task': 'transcribe', 'language': 'no'},
    return_timestamps=True,
    batch_size=2
)
# Record the end time
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the result
print(f'Elapsed time: {elapsed_time} seconds')

for chunk in text['chunks']:
    print(chunk['timestamp'])
    print(chunk['text'])

with open(f"{filename}.txt", 'w') as f:
    f.write(f"data/{text}")

print("done")
