import gpiozero
from time import sleep


led3 = gpiozero.LED(24)

while True:

    led3.on()
    sleep(1)

    led3.off()
    sleep(1)

