import gpiozero
from time import sleep

led1 = gpiozero.LED(18)
led2 = gpiozero.LED(23)
led3 = gpiozero.LED(24)

while True:
    led1.on()
    led2.on()
    led3.on()
    sleep(1)
    led1.off()
    led2.off()
    led3.off()
    sleep(1)

