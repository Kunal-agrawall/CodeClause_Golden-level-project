import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3
from PIL import Image, ImageTk

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x400")

        self.label = tk.Label(root, text="Voice Assistant", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.output_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.output_label.pack(pady=20)

        self.mic_button = tk.Button(root, text="🎤", font=("Helvetica", 24), command=self.record_voice)
        self.mic_button.pack(pady=20)

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def record_voice(self):
        with sr.Microphone() as source:
            self.output_label.config(text="Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio)
                self.output_label.config(text=f"You said: {command}")
                self.process_command(command)
            except sr.UnknownValueError:
                self.output_label.config(text="Could not understand the audio.")
            except sr.RequestError:
                self.output_label.config(text="Could not request results; check your network connection.")
            except sr.WaitTimeoutError:
                self.output_label.config(text="Listening timed out.")

    def process_command(self, command):
        response = ""
        if "hello" in command.lower():
            response = "Hello! How can I help you?"
        elif "how are you" in command.lower():
            response = "I'm an AI, so I don't have feelings, but thank you for asking!"
        elif "what is your name" in command.lower():
            response = "I'm your friendly voice assistant."
        else:
            response = "I'm not sure how to respond to that."

        self.output_label.config(text=f"Assistant: {response}")
        self.speak(response)

    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.system("start response.mp3")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
