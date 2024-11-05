"""
Speech Recognition Module: Audio to Text

This module provides `GiveText()`, a function that listens to audio from the microphone and converts it to text using Google’s Speech Recognition API.
"""
import speech_recognition as sr

recognizer = sr.Recognizer()

def GiveText():
    with sr.Microphone() as source:
            print("\nListening...")
            text =''
            try:
                # Removing or adjusting the timeout
                audio_data = recognizer.listen(source,timeout=10, phrase_time_limit=15)
                print("Recognizing...")

                text = recognizer.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                text = "Sorry, I could not understand the audio."
                return ''
            except sr.RequestError:
                text = "Could not request results; check your network connection."
                return ''
            except sr.WaitTimeoutError:
                text = "Listening timed out, please try again."
                return ''

if __name__=='__main__':
    x = GiveText()
    print(x)