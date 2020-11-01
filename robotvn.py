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
        robot_brain="Chào bạn tôi là robot funny tôi có thể nghe hiểu và nói tiếng việt"
    elif 'ngày' in you:
        today=date.today()
        robot_brain="Ngày "+str(today.day)+" tháng "+str(today.month)+" năm "+str(today.year)
    elif "giờ" in you:
        now=datetime.now()
        current_time=str(now.hour)+" giờ "+str(now.minute)+" phút "+str(now.second)+" giây."
        robot_brain=current_time
    elif "Thủ tướng" in you:
        robot_brain="Thủ tướng nước việt nam hiện nay là Nguyễn Xuân Phúc"
    elif "Chủ tịch nước" in you:
        robot_brain="chủ tịch nước việt nam hiện nay là Nguyễn Phú Trọng"
    elif "Chủ tịch quốc hội" in you:
        robot_brain="chủ tịch quốc hội nước việt nam hiện nay là Nguyễn Thị Kim Ngân"
    elif "Ai tạo ra bạn" in you:
        robot_brain="Ông chủ khôi phạm"
    elif "Tên bạn " in you:
        robot_brain="tên tôi là robot funny"
    elif "tạm biệt" in you or "thoát" in you:
        robot_brain="Tạm biệt bạn, chúc ngủ ngon"
        tts=gTTS(robot_brain,lang='vi')
        filemp3="mp3/"+datetime.now().strftime("%H-%m-%S")+str(random.randint(0,1000))+".mp3"
        tts.save(filemp3)
        playsound(filemp3)
        break
    elif "Thủ đô" in you:
        robot_brain="Thủ đô việt nam là Hà Nội"
    elif "Thời tiết" in you:
        robot_brain="Thời tiết hôm nay có mưa, giông bão cấp 12 bạn nên cẩn thận khi ra ngoài"
    elif "Khang" in you:
        robot_brain="Khang là thằng mập ú thích ẳng ẳng, tham ăn lười làm"
    elif "ú" in you:
        robot_brain="Là thằng Khang mập ú thích ẳng ẳng, tham ăn lười làm"
    elif "bơ" in you:
        robot_brain="Bé Lam Bơ là bé múp míp, hay bơ bơ, hậu đậu"
    elif "bé bơ" in you:
        robot_brain="Bé Lam Bơ là bé múp míp, hay bơ bơ, hậu đậu"
    elif "bé bơ" in you:
        robot_brain="Bé Lam Bơ là bé múp míp, hay bơ bơ, hậu đậu"
    else: robot_brain="Bạn có thể nói lại không, tôi nghe không rõ"
    print("Robot :"+robot_brain)
    try:
        tts=gTTS(robot_brain,lang='vi')
        #filemp3=random.randint(0,1000)
        #file1=str(now.time()).replace(":","")
        #file1=file1.replace(".","")
        filemp3="mp3/"+datetime.now().strftime("%H-%m-%S")+str(random.randint(0,1000))+".mp3"
        tts.save(filemp3)
        playsound(filemp3)
    except:
        print("không thể lưu mp3")
    
    #robot_mount.say(robot_brain)
    #robot_mount.runAndWait()