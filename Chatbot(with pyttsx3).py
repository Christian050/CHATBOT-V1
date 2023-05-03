import pyttsx3 as tts
import random

voice = tts.init()
female_voice = voice.getProperty('voices')
voice.setProperty('rate', 150)
voice.setProperty('voice', female_voice[0].id)

intro = 'Hello. Welcome to the FBN Bank Chatbot'
voice.say(intro)
voice.runAndWait()

response = input().capitalize()
if 'hi' or 'hello' or 'good day' in response:
    assistant_response = 'What can i do for you?'
    voice.say(assistant_response)
    voice.runAndWait()
    print(assistant_response)
    response2 = input().capitalize()
    if 'create' or 'create account' in response2:
        assistant_response2 = 'Alright, enter your First name.'
        voice.say(assistant_response2)
        voice.runAndWait()
        print(assistant_response2)
        response3 = input().capitalize()
        if response3.isalpha():
            assistant_response3 = 'Enter your Last name.'
            voice.say(assistant_response3)
            voice.runAndWait()
            print(assistant_response3)
            response4 = input().capitalize()
            if response4.isalpha():
                assistant_response4 = "Now, enter your other name or type 'skip' to continue."
                if 'skip' in response4:
                    response4 = 'N/A'
                voice.say(assistant_response4)
                voice.runAndWait()
                print(assistant_response4)
                response5 = input().capitalize()
                if response5.isalpha():
                    assistant_response5 = 'Enter your email address'
                    voice.say(assistant_response5)
                    voice.runAndWait()
                    print(assistant_response5)
                    response6 = input().lower()
                    if '@' and '.com' in response6:
                        assistant_response6 = 'Finally enter your phone number with country code.'
                        voice.say(assistant_response6)
                        voice.runAndWait()
                        print(assistant_response6)
                        response7 = input().capitalize()
                        if '+' in response7 and response7.isdigit():
                            assistant_response7 = 'Here\'s your 6 digit password.Type password to confirm.'
                            password = random.randrange(000000, 000000)
                            print(password)
                            voice.say(assistant_response7)
                            voice.runAndWait()
                            print(assistant_response7)
                            response8 = input()
                            if response8 == password:
                                assistant_response8 = 'Here\'s your 6 digit password.Type password to confirm.'
                                voice.say(assistant_response8)
                                voice.runAndWait()
                                print(assistant_response8)
                                
        if response3 == 'No':
            assistant_response6 = 'Okay, download the FBN Bank app on google playstore or the apple app store' \
                                  'or open the FBN Bank webpage to create an account'
            voice.say(assistant_response6)
            voice.runAndWait()
assistant_done = 'Are you satisfied with the responses?'
voice.say(assistant_done)
voice.runAndWait()
print(assistant_done)
response_done = input('Yes/No\n').capitalize()
if response_done == 'Yes':
    assistant_done2 = 'Thank you for using FBN Bank chat bot. Goodbye'
    voice.say(assistant_done2)
    voice.runAndWait()
    voice.stop()
    print(assistant_done2)
else:
    assistant_done3 = 'Please visit the nearest FBN branch or click this link to direct you to the FBN bank website.' \
                      ' Goodbye'
    voice.say(assistant_done3)
    voice.runAndWait()
    voice.stop()
    print(assistant_done3)
    link = 'www.fbnbank.com'
    print(link)
