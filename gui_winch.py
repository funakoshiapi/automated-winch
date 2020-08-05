from tkinter import *
import os
from winch_new_noflip import *
from test import *

window = Tk()

window.configure(background='#95f8b2')

window.title("Automated Winch")

window.geometry('350x200')




def clicked_move_up( ):
    
  
    
    btn_up.configure(bg="red")
    btn_stop.configure(bg='#e2e2e2')
    btn_down.configure(bg='#e2e2e2')
    btn_depth.configure(bg='#e2e2e2')
    move_up()
    print("Down")
    


def clicked_move_down():

    #lbl.configure(text="Button was clicked !!")
    print("Up")
    btn_down.configure(bg="red")
    btn_stop.configure(bg='#e2e2e2')
    btn_up.configure(bg='#e2e2e2')
    btn_depth.configure(bg='#e2e2e2')
    move_down()
    
def clicked_stop():
    
    btn_stop.configure(bg="red")
    btn_up.configure(bg='#e2e2e2')
    btn_down.configure(bg='#e2e2e2')
    btn_depth.configure(bg='#e2e2e2')
    print("Stop")
    stop()

def clicked_depth():
    
    btn_depth.configure(bg="red")
    btn_up.configure(bg='#e2e2e2')
    btn_down.configure(bg='#e2e2e2')
    btn_stop.configure(bg='#e2e2e2')
    

    #lbl.configure(text="Button was clicked !!")
    depth_sensor(float(txt.get()))
    
   

btn_up = Button(window, text="Down", width = 10, height=3, command=clicked_move_up,  activebackground='red')

btn_up.grid(column=0, row=0)

btn_down = Button(window, text="Up", width = 10, height=3, command=clicked_move_down, activebackground='red')

btn_down.grid(column=1, row=0)

btn_stop = Button(window, text="Stop", width = 10, height=3, command=clicked_stop, activebackground='red')

btn_stop.grid(column=2, row=0)


btn_depth = Button(window, text="Depth", width = 10, height=3, command=clicked_depth, activebackground='red')

btn_depth.grid(column=0, row=1)

txt = Entry(window,width=10 )

txt.grid(column=1, row=1)


window.mainloop()
