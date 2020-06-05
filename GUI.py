from tkinter import *
import RPi.GPIO as GPIO
import time

window = Tk()
window.geometry("1000x600")
window.title("LED control GUI")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

def red():
    GPIO.output(18, True)
    GPIO.output(7, False)
    GPIO.output(13, False)
    
def blue():
    GPIO.output(13, True)
    GPIO.output(18, False)
    GPIO.output(7, False)
    
def green():
    GPIO.output(7, True)
    GPIO.output(18, False)
    GPIO.output(13, False)
    
def all_off():
    GPIO.output(7, False)
    GPIO.output(18, False)
    GPIO.output(13, False)
    
def all_on():
    GPIO.output(7, True)
    GPIO.output(13, True)
    GPIO.output(18, True)

B1 = Button(window, text = "RED", width = 20, bg = "yellow", fg="black", command=red)
B1.place(x=400,y=50)

B2 = Button(window, text = "BLUE", width = 20, bg = "yellow", fg="black", command=blue)
B2.place(x=400,y=150)

B3 = Button(window, text = "GREEN", width = 20, bg = "yellow", fg="black", command=green)
B3.place(x=400,y=250)

B4 = Button(window, text = "ALL OFF", width = 20, bg = "yellow", fg="black", command=all_off)
B4.place(x=400,y=350)

B5 = Button(window, text = "ALL ON", width = 20, bg = "yellow", fg="black", command=all_on)
B5.place(x=400,y=450)

window.mainloop()

