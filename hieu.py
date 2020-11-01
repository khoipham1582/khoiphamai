from datetime import date,datetime
import time
#print(datetime.now().strftime("%H-%m-%S"))
now=datetime.now()
#now=now.time()
current_time=str(now.hour)+" giờ "+str(now.minute)+" phút "+str(now.second)+" giây."
print(current_time)
file=str(now.time()).replace(":","")
file=file.replace(".","")
print(file)
