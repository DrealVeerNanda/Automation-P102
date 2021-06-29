from playsound import playsound

import gtts
#modules(gtts used to create the mp3 file and playsound to play the mp3 file)

texttospeech = gtts.gTTS("Automation") #what the text to speech bot will say

texttospeech.save("automationproject.mp3") #saves the file for the text to speech


playsound("automationproject.mp3") #plays automation sound
