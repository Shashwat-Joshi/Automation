import os
from time import sleep

def restart():
    os.shutdown("shutdown /r /t 5")

restart()
