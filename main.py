# Copyright (c) 2014 Swapnil Agarwal
# Licensed under the MIT license: http://opensource.org/licenses/MIT

import Tkinter as tk
import tkFileDialog
import datetime
import os

def select_program():
    program_name = tkFileDialog.askopenfilename()
    t01.config(text=program_name.split('/')[-1])

def start():
    f = open('monitor.pyw','w')
    f.write('from time import sleep\n')
    f.write('import subprocess,os\n')
    f.write('\n')
    f.write('time_elapsed = 0\n')
    f.write('polling_time = 5\n')
    max_time = e11.get().split(':')
    f.write('max_time = '+str(int(max_time[0])*3600+int(max_time[1])*60)+'\n')
    program_name = t01.cget("text")
    f.write('program_name = "'+program_name+'"\n')
    f.write('startupinfo = subprocess.STARTUPINFO()\n')
    f.write('startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW\n')
    f.write('\n')
    f.write('while 1:\n')
    f.write('\tsleep(polling_time)\n')
    f.write('\ttmp = os.popen("tasklist").read()\n')
    f.write('\tif tmp.count(program_name) > 0:\n')
    f.write('\t\ttime_elapsed += polling_time\n')
    f.write('\t\tif time_elapsed > max_time:\n')
    f.write('\t\t\tsubprocess.call("taskkill /F /IM "+program_name, startupinfo=startupinfo)\n')
    f.close()
    t30.config(text="Open monitor.pyw to start monitoring!")

root = tk.Tk()
root.geometry("400x200")
root.title("Controllr : Take Control of usage time")
root.grid()

t00 = tk.Label(text="Select a program to monitor:")
t00.grid(column=0,row=0)

t01 = tk.Label(text="")
t01.grid(column=1,row=0)

b02 = tk.Button(text="Browse...",command=select_program)
b02.grid(column=2,row=0)

t10 = tk.Label(text="Set maximum usage time (hh:mm):")
t10.grid(column=0,row=1)

e11 = tk.Entry()
e11.config(justify="center")
e11.grid(column=1,row=1)

b20 = tk.Button(text="Click here to generate!",command=start)
b20.grid(column=0,row=2)

t30 = tk.Label(text="")
t30.grid(column=0,row=3)

root.mainloop()
