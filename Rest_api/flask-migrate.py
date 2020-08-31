import datetime
import pytz

print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%A"))
print(datetime.date.today().strftime("%d/%m/%Y"))
print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).time().strftime("%H:%M:%S"))
print(datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')))