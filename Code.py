import time
from plyer import notification

title='Hey Ally Here'
message='Your eyes are stressed out ,take a break.Let your beautiful eyes shine  more'

while True:
    notification.notify(title = title,message = message, timeout =10, toast = False)
    time.sleep(1200)