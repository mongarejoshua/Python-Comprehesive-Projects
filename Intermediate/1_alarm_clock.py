import datetime
import time
import winsound

alarm_time = input("Set the alarm time in HHMM (24HRS MODE): ")


while True:
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%H%M")
    if current_time == alarm_time:
        print("Wake Up!")
        winsound.Beep(440, 1000)  # Beep at 440 Hz for 1 second
        break
    time.sleep(1)  # Check every second