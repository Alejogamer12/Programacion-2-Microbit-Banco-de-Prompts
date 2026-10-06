from microbit import *
import random

def tirar_dado():
    numero = random.randint(1, 6)
    display.show(numero)

while True:
    if accelerometer.was_gesture("shake"):
        tirar_dado()

    sleep(100)
