import gpiozero
from time import sleep

led1 = gpiozero.LED(18)

while True:
    led1.on()
    sleep(1)
    led1.off()
    sleep(1)

