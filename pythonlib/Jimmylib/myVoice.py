'''
Created on 2020年1月31日

@author: zjf
'''
import speech_recognition as sr
from aip import AipSpeech
from playsound import playsound
import os


#pip install SpeechRecognition
#pip install PocketSphinx
#pip install pyaudio
#pip install baidu-aip

#https://cloud.tencent.com/developer/article/1149294


class myVoice(object):

    def __init__(self):
        pass
    
    def getVoice(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            x = r.recognize_sphinx(audio)
            return x
    
    def playVoice(self, strs):
        """ 你的 APPID AK SK """
        APP_ID = '18360185'
        API_KEY = 'GGa4gj9upEP671RW6xvBtmiR'
        SECRET_KEY = 'Nt4nAOuxFpZzlS0G1LtalOO0IlsnOGLP'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        
        result = client.synthesis(strs, 'zh', 1, {
        'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('tmp.mp3', 'wb') as f:
                f.write(result)
         
        playsound("tmp.mp3")
        os.remove("tmp.mp3")
