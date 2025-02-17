from datetime import date,timedelta,datetime

time = datetime.now()
withoutmiliseconds = time.strftime("%d-%m-%Y, %H:%M:%S")

print(withoutmiliseconds)