import pyautogui
from time import sleep

sleep(5)
# for i in range(10):
#     pyautogui.alert('Your PC is Hacked')
    
# a = "Assalamu Alaikum", "Kemon asen?", "Ki Obostha?", "Apnar bashar sobai kemon ase?"
# for i in range(0, 4):
#     pyautogui.write(a[i], interval=0.15)
#     pyautogui.press("enter")

distance = 500
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.05)  # move right
    distance -= 10
    pyautogui.drag(0, distance, duration=0.05)  # move down
    pyautogui.drag(-distance, 0, duration=0.05)  # move left
    distance -= 10
    pyautogui.drag(0, -distance, duration=0.05)  # move up

# import cv2
# cam= cv2.VideoCapture(0)
# while True:
#     _,frame =cam.read()
#     cv2.imshow('my cam',frame)
#     cv2.waitKey(1)
