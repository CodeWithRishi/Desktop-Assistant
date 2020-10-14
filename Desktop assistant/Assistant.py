import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random 
import Privacy as p


#setting voice
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)



#songs
randomesongs = random.randint(0,15)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <= 12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    speak("Iam your desktop assistant i can do many things")

def takecommmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source , duration=0.4)
        audio = r.listen(source)

    try:
        print("Recognising your voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
    except Exception as e:
        # print(e)    
        speak("Sorry did you say anything")
        return "None"
    return query


def sendEmail(reciever , content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login(p.email , p.password )
    server.sendmail(p.email , reciever , content)
    server.close()

if __name__ == "__main__":
    wishme() 
    while True:
        query = takecommmand().lower()

        if "wikipedia" in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError :
                print("Sorry..!!Unable to find in Wikipedia")
                speak("Sorry , Unable to find in Wikipedia")

        elif "bye" in query:
            speak("Nice talking with you bye")
            break

        elif "open youtube" in query:
            speak("Searching and opening Youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Searching and opening Google")
            webbrowser.open("google.com")

        elif "open programming hero" in query:
            speak("Searching and opening Programming hero")
            webbrowser.open("programming-hero.com")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"The time is {time}")

        elif "who" in query:
            print("Iam a desktop assistant made by Rishikesh on 12-10-2020 . He is a great man.")
            speak("Iam a desktop assistant made by Rishikesh on 12-10-2020 . He is a great man.")

        elif 'code' in query:
            speak("Opening code editor")
            codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif "name" in query:
            print("My name is Desktop assistant but you can call me Zara")
            speak("My name is Desktop assistant but you can call me Zara")

        elif "old" in query:
            print("i actually don't know my age i should ask Rishikesh.")
            speak("i actually don't know my age i should ask Rishikesh.")

        elif " can you do" in query:
            print("1.) I can open any thing for you\n2.) I can say the accurate time\n3.) I can search on wikipedia\n4.) I can send email to anyone\n5.) I can play a song for you ")
            speak(" I can open any thing for you . I can say the accurate time . I can search on wikipedia . I can send email to anyone .  I can play a song for you")

        elif "thank you" in query:
            print("Iam always active to help you at any time..")
            speak("Iam always active to help you at any time.")

        elif "good" in query:
            print("Thank you i will always keep trying to improve myself")
            speak("Thank you , i will always keep trying to improve myself")

        elif "i love you" in query:
            print("I love you too..")
            speak("I love you too..")

        elif "hate you" in query:
            print("But i like you , but you hate me so iam going . Bye")
            speak("But i like you , but you hate me so iam going . Bye")
            break

        elif "email" in query:
            try:
                speak("Type the email you want to send..")
                reciever = input("Enter the recievers email:-")
                speak("Done!")
                speak("What should i say..??")
                content =takecommmand()
                sendEmail(reciever , content)
                speak("Email has been sent..")
            except Exception as e:
                print(e)
                speak("Sorry , Unable to send the mail.. Try again later")
                speak("It could be due to that you didn't allow acsess to 'Less secure apps'")
                #this will come if there is an error or if you have not unable "Less secure app(dangerous thing to do but after unablong it you have to turn it off..Okay)"

        elif "song" in query:
            music_dir = 'C:\\Users\\tpana\\Desktop\\Python Project By Rishikesh\\Desktop assistant\\Songs'
            songs = os.listdir(music_dir)
            print("Playing song")
            speak("Playing song")
            os.startfile(os.path.join(music_dir , songs[randomesongs]))

        elif "doing" in query:
            print("Iam currently helping a person in the server")
            speak("Iam currently helping a person in the server")
        #THIS WILL NEVER END IT HAS A MILLION THINGS YOU CAN DO WITH ZARA AND PYTHON WITH MANY OTHER SERVERS

        
