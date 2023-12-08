def speak(audio):
    import pyttsx3
    Assistant = pyttsx3.init('sapi5')
    voices = Assistant.getProperty('voices')
    Assistant.setProperty('voice', voices[1].id)
    Assistant.setProperty('rate', 163)
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()
def takecommand():
    import speech_recognition as sr

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()
def timee():
    import datetime
    now = datetime.datetime.now()
    a = now.strftime("%H")
    b = now.strftime("%M")
    hour = []
    after = {"00": 12, "01": 1, "02": 2, "03": 3, "04": 4, "05": 5, "06": 6, "07": 7, "08": 8, "09": 9, "10": "10",
             "11": 11, "12": 12, "13": 1, "14": 2, "15": 3, "16": 4, "17": 5, "18": 6, "19": 7, "20": 8, "21": 9,
             "22": "10", "23": 11, "00": 12}
    for i, j in after.items():
        if i == a:
            hour.append(int(i))
            hour.append(int(j))
    for k in hour:
        if hour[0] == 0 and hour[0] <= 12:
            speak(f"The time is: {hour[1]}:{b} A M")
            break
        elif hour[0] >= 12:
            speak(f"The time is: {hour[1]} : {b} P M")
            break
        else:
            continue
def wishme():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning,Sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon,Sir!")
    else:
        speak("Good evening ,Sir!")
def Tempp():
    import requests
    from bs4 import BeautifulSoup
    tempp = 'weather in Jammu'
    url = f"https://google.com/search?q={tempp}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current {tempp} is {temp}")


def CREATOR_INFO():
    speak("Before starting , let me give you a short introduction of creator")
    speak("I am created by : Samanvay Gupta")
def WHAT_CAN_I_DO():
    speak("I can help you in:")
    speak("Telling you current time")
    speak("Current weather in Jammu")

def Function_to_be_called():
    wishme()
    timee()
    Tempp()
    CREATOR_INFO()
    WHAT_CAN_I_DO()
    speak("I am Code Assist.")
    speak("SO how may I help you!")
    while True:
        speak("Tell me what to do next")
        speak("Here is the list of Functions")
        print("CURRENT time")
        print("CURRENT WEATHER IN JAMMU")
        print("Text File")
        print("Binary File")
        print("CSV File")
        speak("say sleep or stop if you want me to shutdown!")
        command_inside = takecommand()
        print(command_inside)
        if "time" in command_inside:
            timee()
        elif "temperature" in command_inside:
            Tempp()
        elif "sleep" in command_inside or "stop" in command_inside:
            speak("I am going see you later")
            speak("to wake me up just say Wake up")
            speak("I will be there for you")
            break
Function_to_be_called()