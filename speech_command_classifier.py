import speech_recognition as sr
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Predefined commands
COMMANDS = ["start", "stop", "pause", "exit"]

def process_command(command):
    """
    Function to process recognized commands.
    """
    if command in COMMANDS:
        print(f"Command recognized: {command}")
        if command == "exit":
            print("Exiting program...")
            exit(0)
        elif command == "start":
            print("Starting process...")
        elif command == "stop":
            print("Stopping process...")
        elif command == "pause":
            print("Pausing process...")
    else:
        print("Unknown command. Try again!")

def listen_for_commands():
    """
    Listen for voice commands and process them.
    """
    with sr.Microphone() as source:
        print("Listening for a command... (say 'exit' to quit)")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand that. Please try again.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    while True:
        listen_for_commands()
