from datetime import date,datetime
#print(datetime.now().strftime("%H-%m-%S"))
now=datetime.now()
#now=now.time()
current_time=str(now.hour)+" giờ "+str(now.minute)+" phút "+str(now.second)+" giây."
print(current_time)