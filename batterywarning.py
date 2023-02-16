import psutil 
import time
from tkinter import messagebox
from datetime import datetime


  
def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 
  

  


def printed():
    battery = psutil.sensors_battery() 
    print("Power plugged in : ", battery.power_plugged) 
    print("Battery left : ", convertTime(battery.secsleft))
    print("Battery percentage : ", battery.percent) 


def waitXminutes(minutestowait):
    timehour =datetime.today().strftime('%H:%M') 
    #print(timehour)
    for x in range(minutestowait):
        time.sleep(60)
        x+=1
        #print(x)
    


def main():
    battery = psutil.sensors_battery() 
    while 1:
        
        battery = psutil.sensors_battery() 
        if(battery.power_plugged):
            if battery.percent == 100 :
                #print("desconectar cargador")
                messagebox.showinfo(message="desconectar cargador", title="")
            #print("cargador conectado")
        else:
            if battery.percent < 20 :
                #print("conecta cargador")
                messagebox.showinfo(message="cargador conectado", title="")
            


        waitXminutes(60)
                
if __name__ == '__main__':
    main()
