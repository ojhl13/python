import tkinter as tk
import serial
ser = serial.Serial()

def config_ser():
    

    ser.port = 'COM26'
    ser.baudrate = '115200'
    ser.open()

def serial_Send(data):
    ser.write(data.encode('utf-8'))
    endline=b'\n'
    ser.write(endline)

    
def previous_song():
    print("previous")
    serial_Send("2")

def play_song():
   print("play")
   serial_Send("1")
   
def next_song():
    print("next")
    serial_Send("3")

config_ser()
window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_prev = tk.Button(master=window, text="prev", command=previous_song)
btn_prev.grid(row=0, column=0, sticky="nsew")

btn_play = tk.Button(master=window, text="play", command=play_song)
btn_play.grid(row=0, column=1, sticky="nsew")

btn_next = tk.Button(master=window, text="next", command=next_song)
btn_next.grid(row=0, column=2, sticky="nsew")

window.mainloop()
ser.close()