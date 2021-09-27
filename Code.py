import time
from plyer import notification

title=' Hey Ally Here'
message='Hey your eyes are stressed out ,take rest , Let your beautiful eyes bright more'
while True:
    notification.notify(title = title,message = message, timeout =10, toast = False)
    time.sleep(1200)