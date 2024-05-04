import os
import platform
import time
from sui import *
from map import *

def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

class Timer:

    def __init__(self, interval):
        self.interval = interval
    

    def start(self, traffic_lights,map_obj,cm,cp):
        for time_step in range(30):
            for tl in traffic_lights:
                tl.update()


            map_obj.print(cp, cm)

            for row in cm.map:
                print(''.join(row))

            time.sleep(1)
            clear_screen()
