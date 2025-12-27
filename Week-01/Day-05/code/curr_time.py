# Date time(Current)
import datetime 
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m-%d-%Y") # Github Codespace - UTC(Coordinated Universal Time)
print(now)