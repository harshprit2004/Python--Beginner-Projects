import datetime
import time
import pygame

def alarm_app():
    alarm_time = input("1 Enter alarm time (HH:MM:SS - 24hr format): ")
    print(f" Alarm set for {alarm_time}...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}", end="\r")
        if current_time == alarm_time:
            print("\n Alarm Time Reached!")
            break
        time.sleep(1)

    # Initialize pygame mixer and play the alarm sound in a loop
    pygame.mixer.init()
    pygame.mixer.music.load("ADD YOUR MUSIC.mp3")
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    input("Press ENTER to stop the alarm...")
    pygame.mixer.music.stop()
    print("Alarm stopped. Have a good day!")

# Run the alarm
alarm_app()
