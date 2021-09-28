import time
from plyer import notification

title='Hey Ally here'
message='Your eyes are stressed out, take a break. Let your beautiful eyes shine more'
while True:
    notification.notify(title=title, message=message,app_icon="IMAGES\\eyeclock.ico", timeout= 10, toast= False)
    time.sleep(1200)