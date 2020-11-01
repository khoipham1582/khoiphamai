import pyttsx3
import speech_recognition
from datetime import date,datetime

robot_ear=speech_recognition.Recognizer()
robot_brain=""
you=""
robot_mount = pyttsx3.init()
while(True):
    with speech_recognition.Microphone() as mic:
        print("Robot : I'm listening")
        audio=robot_ear.listen(mic)
    print("Robot : ...")
    try:
        you=robot_ear.recognize_google(audio)
    except:
        you=""

    print("You :"+you)
    if(you==""):
        robot_brain="I can't hear you"
    elif "hello" in you:
        robot_brain="hello khoi pham"
    elif 'today' in you:
        today=date.today()
        robot_brain=today.strftime("%B %d, %Y")
    elif "time" in you:
        now=datetime.now()
        current_time=now.strftime("%H hours %M minutes %S seconds")
        robot_brain=current_time
    elif "president" in you:
        robot_brain="President USA is Donald Trump"
    elif "bye" in you:
        robot_brain="Goodbye"
        robot_mount.say(robot_brain)
        robot_mount.runAndWait()
        break
    else: robot_brain="Can you say again"
    print("Robot :"+robot_brain)
    robot_mount.say(robot_brain)
    robot_mount.runAndWait()