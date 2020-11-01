import pyttsx3
import speech_recognition
from datetime import date,datetime
from gtts import gTTS
from playsound import playsound
import random
robot_ear=speech_recognition.Recognizer()
robot_brain=""
you=""
robot_mount = pyttsx3.init()
while(True):
    with speech_recognition.Microphone() as mic:
        print("Robot : Tôi đang nghe bạn đây...")
        audio=robot_ear.listen(mic)
    #print("Robot : ...")
    try:
        you=robot_ear.recognize_google(audio,language='vi-VN')
    except:
        you=""

    print("You :"+you)
    if(you==""):
        robot_brain="Bạn không muốn nói chuyện sao"
    elif "chào" in you:
        robot_brain="Chào bạn tôi là robot việt nam"
    elif 'ngày' in you:
        today=date.today()
        robot_brain=today.strftime("ngay %d thang %m nam %Y")
    elif "giờ" in you:
        now=datetime.now()
        current_time=now.strftime("%H gio %M phut %S giay")
        robot_brain=current_time
    elif "thủ tướng" in you:
        robot_brain="Thủ tướng nước việt nam hiện nay là Nguyễn Xuân Phúc"
    elif "tạm biệt" in you:
        robot_brain="Tạm biệt bạn"
        filemp3="mp3/"+datetime.now().strftime("%H-%m-%S")+".mp3"
        tts.save(filemp3)
        playsound(filemp3)
        break
    elif "Thủ đô" in you:
        robot_brain="Thủ đô việt nam là Hà Nội"
    elif "Thời tiết" in you:
        robot_brain="Thời tiết hôm nay có mưa, giông bão cấp 12, 13 bạn nên cẩn thận khi ra ngoài"
    elif "Khang" in you:
        robot_brain="Khang là thằng mập ú thích ẳng ẳng, tham ăn lười làm"
    elif "Bơ" in you:
        robot_brain="Bơ là bé múp míp, hay bơ bơ, hậu đậu"
    else: robot_brain="Bạn có thể nói lại không, tôi nghe không rõ"
    print("Robot :"+robot_brain)
    tts=gTTS(robot_brain,lang='vi')
    #filemp3=random.randint(0,1000)
    filemp3="mp3/"+datetime.now().strftime("%H-%m-%S")+".mp3"
    tts.save(filemp3)
    playsound(filemp3)
    #robot_mount.say(robot_brain)
    #robot_mount.runAndWait()