from datetime import datetime
from zoneinfo import ZoneInfo

# Replace 'Asia/Kolkata' with your specific timezone if different
india_now = datetime.now(ZoneInfo("Asia/Kolkata"))
print("Today's Date in India:", india_now.date()) 
# Output: 2025-12-28

india_now = datetime.now(ZoneInfo("Asia/Kolkata"))
print("Current Time in India:", india_now.time())

# now = datetime.datetime.now()
# now = now.strftime("%H:%M:%S %m-%d-%Y")
# print(now)