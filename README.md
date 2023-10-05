# whispers_at_home

Project to learn how to use ready-made models from huggingface. This one is for running the Norwegian Whisper model. 

## First:

```bash
python3.9 -m venv .venv/ # create a venv to install deps. 
source .venv/bin/activate.fish # source the activate script for your shell
pip3.9 install --upgrade pip # make sure to have the latest pip
pip3.9 install -r requirements.txt
python3.9 script.py
```
## Using IntelliJ
- start a new project, from existing sources (select git repo directory.) 
- Create project from existing sources (in import project window)
- Select SDK home path "whispers_at_home/.venv/bin/python" (must be done after creating .venv)
  - Remember to select System Interpeter on the type of interpeter to add, then select the python binary in the venv. 
- unselect any frameworks it finds. there are none in this project.  

## Convert to wav
```bash 
docker run --rm -it -v ./data:/data linuxserver/ffmpeg -i /data/2023_10_05-0710-siste_nytt_vg.mp3  -ac 1 -ar 16000 /data/2023_10_05-0710-siste_nytt_vg.wav
```


