from tkinter import *
import pyttsx3
import random


class ChatBot(Tk):  # Class name should start with a capital letter
    def __init__(self):
        super().__init__()
        self.geometry('600x200')
        self.title('Chatbot')
        self.font = 'Calibri 25 bold'
        self.BtnFont = 'Calibri 15 bold'

        # Initialize the voice engine only once when the GUI is created
        self.voice = pyttsx3.init()
        self.female_voice = self.voice.getProperty('voices')
        self.voice.setProperty('rate', 150)
        self.voice.setProperty('voice', self.female_voice[0].id)

    def chatbotResponse(self, message):
        # Always call the method to say the intro message
        self.say_message('Hello. Welcome to the FBN Bank Chatbot')

        # Use "in" with multiple conditions separated by "or"
        if 'hi' in message or 'hello' in message or 'good day' in message:
            assistant_message = 'Hello, what can I do for you?'
            self.say_message(assistant_message)
            self.label.config(text='Chatbot: ' + assistant_message)

            # Use "in" with multiple conditions separated by "or"
            if 'create' in message or 'create account' in message:
                assistant_message2 = 'Alright, enter your First name.'
                self.say_message(assistant_message2)
                self.label.config(text='Chatbot: ' + assistant_message2)

                # Use "if message.isalpha()" to check if the input contains only alphabetic characters
                if message.isalpha():
                    assistant_message3 = 'Enter your Last name.'
                    self.say_message(assistant_message3)
                    self.label.config(text='Chatbot: ' + assistant_message3)

                    # Use "if message.isalpha()" to check if the input contains only alphabetic characters
                    if message.isalpha():
                        assistant_message4 = "Now, enter your other name or type 'skip' to continue."
                        self.say_message(assistant_message4)
                        self.label.config(
                            text='Chatbot: ' + assistant_message4)

                        # Use "if 'skip' in message" to check if the input contains the string 'skip'
                        if 'skip' in message:
                            message = 'N/A'

                        assistant_message5 = 'Enter your email address'
                        self.say_message(assistant_message5)
                        self.label.config(
                            text='Chatbot: ' + assistant_message5)

                        # Use "if '@' in message and '.com' in message" to check if the input contains an email address
                        if '@' in message and '.com' in message:
                            assistant_message6 = 'Finally enter your phone number with country code.'
                            self.say_message(assistant_message6)
                            self.label.config(
                                text='Chatbot: ' + assistant_message6)

                            # Use "if message.startswith('+') and message[1:].isdigit()" to check if the input starts with a plus sign and the remaining characters are digits
                            if message.startswith('+') and message[1:].isdigit():
                                assistant_message7 = 'Here\'s your 6 digit password. Type password to confirm.'
                                # Generate a random 6-digit number
                                password = random.randrange(100000, 1000000)
                                print(password)
                                self.say_message(assistant_message7)
                                self.label.config(
                                    text='Chatbot: ' + assistant_message7)

                                # Use "if message.isdigit() and len(message) == 6" to check if the input is a 6-digit number
                                if message.isdigit() and len(message) == 6:
                                    assistant_message8 = 'Your account has been created successfully. Thank you for choosing FBN Bank.'
                                    self.say_message(assistant_message8)
                                    self.label.config(
                                        text='Chatbot: ' + assistant_message8)
                                else:
                                    assistant_message_error = 'Error: Invalid input. Please enter a 6-digit password.'
                                    self.say_message(assistant_message_error)
                                    self.label.config(
                                        text='Chatbot: ' + assistant_message_error)
                            else:
                                assistant_message_error = 'Error: Invalid input. Please enter your phone number with country code (e.g. +1234567890).'
                                self.say_message(assistant_message_error)
                                self.label.config(
                                    text='Chatbot: ' + assistant_message_error)
                        else:
                            assistant_message_error = 'Error: Invalid input. Please enter a valid email address (e.g. john@example.com).'
                            self.say_message(assistant_message_error)
                            self.label.config(
                                text='Chatbot: ' + assistant_message_error)
                    else:
                        assistant_message_error = 'Error: Invalid input. Please enter only alphabetic characters.'
                        self.say_message(assistant_message_error)
                        self.label.config(
                            text='Chatbot: ' + assistant_message_error)
                else:
                    assistant_message_error = 'Error: Invalid input. Please enter only alphabetic characters.'
                    self.say_message(assistant_message_error)
                    self.label.config(text='Chatbot: ' +
                                      assistant_message_error)
            else:
                assistant_message_error = 'Error: I am not programmed to perform that task. Please try again.'
                self.say_message(assistant_message_error)
                self.label.config(text='Chatbot: ' + assistant_message_error)
        else:
            assistant_message_error = 'Error: I did not understand what you said. Please try again.'
            self.say_message(assistant_message_error)
            self.label.config(text='Chatbot: ' + assistant_message_error)

    def say_message(self, message):
        self.voice.say(message)
        self.voice.runAndWait()

    def create_widgets(self):
        self.label = Label(self, font=self.font, wraplength=500)
        self.label.pack(side=TOP, pady=10)

        self.btn = Button(self, text='Ask', font=self.BtnFont,
                          command=self.get_input)
        self.btn.pack(side=BOTTOM, pady=10)

        self.entry = Entry(self, font=self.font)
        self.entry.pack(side=BOTTOM, pady=10)

    def get_input(self):
        message = self.entry.get().lower()
        self.entry.delete(0, END)
        self.chatbotResponse(message)


if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.create_widgets()
    chatbot.mainloop()
