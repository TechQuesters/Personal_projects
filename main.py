from speechText import GiveText
import webbrowser
import pyttsx3
from brain import getAnswer
from WebSearch import SearchQuery
import os
import re
import time

# model Name
model_name = "jarvis"

# for open command
def starts_with_open(sentence):
    pattern = r'^\s*open\b'
    return bool(re.match(pattern, sentence, re.IGNORECASE))

# pyttsx object
engine = pyttsx3.init()
# Slower speech rate
engine.setProperty('rate', 110)

# speak function 
def speak(text):
    engine.say(text)
    engine.runAndWait()

# functions to open external websites
def open_cmd(text):
    search = text.lower().split(' ')[1]
    speak(f'opening {search}')
    webbrowser.open_new(f"https://www.{search}.com/")

# me and my my assiatant
def creator(text):
    if 'who created you' in text.lower():
        response = 'Team of TechQuesters are my creator.They are a group of aspiring Btech student.'
        speak(response)
    elif 'who are you' in text.lower():
        response = f'I am {model_name},your personal Ai assistant, ready to accompany you with my versatile ai knowledge.'
        speak(response)
    else:
        return

if __name__=='__main__':

    while True:
        wake = GiveText().lower()
        if wake == model_name:
            speak("How can I help you,sir.")
            print(".....Alexa Activative....\n")
            time.sleep(1)  # Pause for a moment

            # gets the text from speech/voice spoken
            text = GiveText()

            if not text:
                print("\nDidn't hear you, try once more.")
            else:
                text = text.lower()

                # Handle search query
                if text == 'ai search':
                    speak("What do you want me to search?")
                    while True:
                        time.sleep(1)
                        print("\nAsk your query")
                        prompt = GiveText().lower()

                        if prompt == 'exit':
                            print("Exited Search mode....")
                            break
                        elif not prompt:
                            print("No query provided...")
                        else:
                            print(f"Your Query: {prompt}")
                            print("Searching...")
                            ans = getAnswer(f'{prompt}.Dont make it too long')
                            print(f"Query Response: {ans}")
                            speak("Here's your answer.")

                # for accessing the web browser for searches
                elif text =='web search':
                    speak("What do you want me to search?")
                    while True:
                        time.sleep(1)
                        print("\nAsk your query")
                        prompt = GiveText().lower()
                        if prompt=='exit':
                            print("exiting Web Search")
                            time.sleep(1)
                            break
                        print(f'Searching the web for {prompt}')
                        time.sleep(1)
                        SearchQuery(prompt)
                # Handle open command
                if starts_with_open(text) and len(text) > 5:
                    open_cmd(text)

                # Handle creator-related queries
                creator(text)

        # Handle exit command
        elif wake == 'exit':
            print("Bye.......")
            speak("Have a nice day sir.")
            break
