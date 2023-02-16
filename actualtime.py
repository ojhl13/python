from datetime import datetime
now = datetime.now()
time =datetime.today().strftime('%H:%M') 
print(time)

print(now.date())
print(now.time())
