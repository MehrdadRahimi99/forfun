import time
import os
import datetime

os.system("cls")

def countdown(h, m, s):
    second = h*3600 + m*60 + s
    while second > 0 :
        timer = datetime.timedelta(seconds = second)
        print(timer, end="\r")
        time.sleep(1)
        second -= 1
    print("time over!!")

countdown(0,0,20)