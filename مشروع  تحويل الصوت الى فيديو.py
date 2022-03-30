import speech_recognition as speech_recog

import webbrowser

as wbrwser

def voiceRecognitionWebSearch():

person1 = speech_recog.Recognizer() person2 = speech_recog.Recognizer()

with speech_recog.Microphone () as mySource:

print('[Search Python: search youtube]') print('Start speaking') myAudio = person2.listen (my Source)

if 'video' in person1.recognize_google (myAudio):


with speech_recog.Microphone () as mySource: print('Searching') myAudio = person1.listen (mySource)

try:

get_Data = person1.recognize_google (myAudio)

print (get_Data)

wbrwser.get().open_new (myUrl+get_Data)

except speech_recog.UnknownValueError: print('Error')

except speech_recog.RequestError as req_er: print('Request not found {}'. format (req_er))

voiceRecognitionWebSearch()