import speech_recognition as sr
import os
import pyautogui
import time
text = "nothing"


def afterburner():
    os.system("cls")
    pyautogui.press("backspace")
    print(text)
    
def takeoff():
    os.system("cls")
    pyautogui.keyDown("down")
    time.sleep(2)
    pyautogui.keyUp("down")
    print(text)
    
def level():
    os.system("cls")
    pyautogui.typewrite(["L"])
    print(text)

def fire():
    os.system("cls")
    pyautogui.keyDown("space")
    time.sleep(2)
    pyautogui.keyUp("space")
    print(text)

def missile():
    pyautogui.typewrite(["3"])
    print(text)
    
def bomb():
    pyautogui.typewrite(["5"])
    print(text)
    
def harpoon():
    pyautogui.typewrite(["4"])
    print(text)
    
def gun():
    pyautogui.typewrite(["2"])
    print(text)

def right():
    pyautogui.keyDown("right")
    time.sleep(1)
    pyautogui.keyUp("right")

def left():
    pyautogui.keyDown("left")
    time.sleep(6)
    pyautogui.keyUp("left")

def bailout():
    pyautogui.hotkey("ctrl","E")

active = True
while active:
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak :")
        audio = r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            print("could not recognize your voice")
    
    
    if text == "backspace":
        afterburner()
        
    elif text == "fly":
        takeoff()
        
    elif text == "level":
        level()
        
    elif text == "space":
        fire()
        
    elif text == "missile":
        missile()
        
    elif text == "bomb":
        bomb()
    
    elif text == "harpoon":
        harpoon()
        
    elif text == "gun":
        gun()
    
    elif text == "right":
        right()
    
    elif text == "left":
        left()
    
    elif text == "bailout":
        bailout()
    