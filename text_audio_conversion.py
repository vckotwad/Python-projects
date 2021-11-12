from gtts import gTTS
import os
f= open("sample.txt") # give string or file path
text=f.read()

language='en'
obj = gTTS(text=text,lang=language, slow=False)
obj.save("sample.mp3") #mp3 file output