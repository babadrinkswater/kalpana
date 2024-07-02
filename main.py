from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

from TTS.api import TTS

assets_path = f'{os.path.dirname(os.path.abspath(__file__))}/assets'
text_data = ("Once there lived a mighty warrior named Rana Sangha. He was a great cavalry commander of the glorious "
             "rajupt kingdom. He led a force of formidable horses which were imported from arabia.")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
tts.tts_to_file(text=text_data, file_path=f'{assets_path}/output.wav')

app = FastAPI()


@app.get("/image")
async def image():
    return FileResponse(f'{assets_path}/img1.png')


@app.get("/text")
async def text():
    return text_data


@app.get("/audio")
async def audio():
    return FileResponse(f'{assets_path}/output.wav')
