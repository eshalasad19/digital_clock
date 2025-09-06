import time 
import datetime
import os

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    os.system("cls")

    print(f"Current Time: {current_time}")

    time.sleep(1)