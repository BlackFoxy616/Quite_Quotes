from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
from pyrogram import Client, filters
import requests,os,csv
import openai
import os 



os.environ["SUNO_OFFLOAD_CPU"] = True
os.environ["SUNO_USE_SMALL_MODELS"] = True


preload_models()

openai.api_key = "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"


api_id = 3702208
api_hash = "3ee1acb7c7622166cf06bb38a19698a9"
bot_token = "6117259818:AAFdPMrVrrycE1Sc0GkhxIQE6vtfU2xYs2M"

app = Client(
    "QuotePull",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)




@app.on_message(filters.command("audio"))
async def start_command(client,message):
      prompt= message.text[7:]
      audio_array = generate_audio(prompt, history="v2/en_speaker_6")
      write_wav("generation.wav",320, audio_array)
      await send_audio(message.chat_id,"generation.wav",caption=prompt)
      os.remove("generation.wav")
     

 
    

print("Bot Started ..!!")

app.run()