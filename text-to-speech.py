# Python Text to speech
from text_to_speech import save
s = input("Please enter any text for speech:")
text = s
language = "en"
output_file = "text_speech.mp3"

save(text, language, slow=True, file=output_file)

import pyttsx3
s = input("Please enter any text for speech:")
engine = pyttsx3.init()
engine.say(s)
engine.runAndWait()
