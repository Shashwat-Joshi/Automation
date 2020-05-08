import os
from time import sleep


def shutdown():
    ans = input("Shutdown System ? Y/N \n")
    if ans == 'Y' or ans == 'y':
        print("System will shut down in 30 sec !!")
        sleep(2)
        os.system("shutdown /s /t 30")                       #("shutdown /s /t 30")
    else:                                                    #(/s) -> to shutdown, replace with /r to restart
        print("BYE BYE !")                                   #(/t) -> represents time
        sleep(1)                                             #(30) -> time in seconds
                                                                                 
shutdown()                                     
                                                
