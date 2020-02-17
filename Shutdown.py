import os
from time import sleep


def shutdown():
    ans = input("Do you Love me ? Y/N \n")
    if ans == 'Y' or ans == 'y':
        print("I love you to !!")
        sleep(2)
    else:
        print("That's Rude !")
        sleep(1)
        os.system("shutdown /s /t 30")          #("shutdown /s /t 30")
                                                #(/s) -> to shutdown, replace with /r to restart
shutdown()                                      #(/t) -> represents time
                                                #(30) -> time in seconds
