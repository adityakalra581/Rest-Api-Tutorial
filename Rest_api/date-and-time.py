import datetime
import pytz
import time 



# print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%A"))
# print(datetime.date.today().strftime("%d-%m-%Y"))
# print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).time().strftime("%H:%M:%S"))
# print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')))
# print(datetime.datetime.utcnow())
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().strftime('%B'))
# print(datetime.datetime.now().strftime('%h'))
# print(datetime.datetime.now())

def t_time():
    t = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).time().strftime("%H:%M:%S")
    print(t)

t_time()
  
  
# curr_time = time.localtime() 
# curr_clock = time.strftime("%H:%M:%S", curr_time) 
  
# print(curr_clock) 
# print(time.strftime("%H:%M:%S", time.localtime()))


