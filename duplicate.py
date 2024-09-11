import pyautogui as pag
import random
import time
from TimeCalc import *
from VariableTime import t

print(time.time())
duration = timeRequested(t)

end_time = time.time() + Calc(duration)

while time.time() < end_time:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    pag.moveTo(x, y, 0.5)
    print(time.time())

    time.sleep(5)
