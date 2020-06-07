import speech_recognition as sr
import os
import pyautogui
import time
text = "nothing"


i=0
while i!=1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak :")
        audio = r.listen(source)
        try:
            text=r.recognize_google(audio)
        except:
            print("could not recognize your voice")
            #break
    
    if text =="backspace":
        pyautogui.press("backspace")
        print("backspace")
        
        
    if text == "down":
        pyautogui.keyDown("up")
        time.sleep(3)
        pyautogui.keyUp("up")
        
    if text == "fly":
        pyautogui.keyDown("down")
        time.sleep(3)
        pyautogui.keyUp("down")
        
        

    if text == "left":
        pyautogui.keyDown("left")
        time.sleep(6)
        pyautogui.keyUp("left")
        
    if text == "right":
        pyautogui.keyDown("right")
        time.sleep(6)
        pyautogui.keyUp("right")

    if text == "shopping":
        print("crazy")
        pyautogui.keyDown("right")
        time.sleep(1)
        pyautogui.keyDown("left")
        time.sleep(1)
        pyautogui.keyDown("right")
        time.sleep(1)
        pyautogui.keyDown("left")
        time.sleep(1)
        pyautogui.keyDown("right")
        time.sleep(1)
        pyautogui.keyDown("left")
        time.sleep(1)
        break
        
    if text == "land":
        pyautogui.typewrite(["A"])
        pyautogui.typewrite(["7"])
        
    if text == "level":
        pyautogui.typewrite(["L"])
            
    if text == "shop":
        pyautogui.typewrite(["spacebar"])
        
    if text == "gun":
        pyautogui.typewrite(["2"])
        
    if text == "missile":
        pyautogui.typewrite(["3"])
        
    if text == "ground":
        pyautogui.typewrite(["4"])
        
    if text == "bomb":
        pyautogui.typewrite(["5"])
        
    if text == "bail":
        pyautogui.hotkey("ctrl","E")
        
    