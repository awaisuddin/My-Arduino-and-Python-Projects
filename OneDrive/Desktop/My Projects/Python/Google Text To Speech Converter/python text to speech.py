from gtts import gTTS 

import os 

language = 'en'

myobj = gTTS(text=" tumharey baava hi who are you", lang=language, slow=False) 

myobj.save("output.mp3") 

os.system("start output.mp3") 
