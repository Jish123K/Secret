import pyttsx3

import time

import playsound

# Function used to encrypt plain text into morse code and play the resulting audio

def encryptor(text):

    engine = pyttsx3.init()

    morse_code = ""

    for letter in text:

        if letter != " ":

            morse_code += dict.MORSE_CODE_DICT.get(letter) + " "

        else:

            morse_code += "  "

    engine.say(morse_code)

    engine.runAndWait()

    time.sleep(0.5)

    playsound.playsound('morse_code.wav')

    return morse_code

