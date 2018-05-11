# -*- coding: UTF-8 -*-


from Tkinter import *
import ttk
import datetime
import time
import os

cwd = os.getcwd()
custom_font = ('Helvetica', 32)
HourVar = 0
MinuteVar = 0
SecondVar = 0

# Definitions For Clock, Timer, and Stopwatch


def start_timer():
    timer_var = (HourVar * 3600) + (MinuteVar * 60) + SecondVar
    spinbox_hr.config(state='disabled')
    spinbox_min.config(state='disabled')
    spinbox_sec.config(state='disabled')
    while timer_var > 0:
        timer_var = timer_var - 1
        time.sleep(1)


def clock():
    # get the current local time from the PC
    time_string = datetime.datetime.now()
    # if time string has changed, update it
    clock_lbl.config(text=(str(time_string.hour) + ":" + str(time_string.minute) + ":" + str(time_string.second)))
    clock_lbl.after(200, clock)


def timer():

    MainWindow.after(500, timer)


def stopwatch():

    MainWindow.after(500, stopwatch)


def startup(code):
    # Codes:
    # 0 - Normal
    # 1 - Error Reset
    # 2 - Emergency Reset
    if code == 0:
        print("Loading Up:")
        clock()
        timer()
        stopwatch()
    elif code == 1:
        print("Error: Resetting")
        # Add Defaults Here
        clock()
        timer()
        stopwatch()


########################################
# Make Main Window#######################
MainWindow = Tk()
########################################
# Tool Tabs#############################
Tab_Renderer = ttk.Notebook(MainWindow)
toolbar = Frame(MainWindow)
Clock_Child = Frame(Tab_Renderer)
Timer_Child = Frame(Tab_Renderer)
Stopwatch_Child = Frame(Tab_Renderer)
Settings_Child = Frame(Tab_Renderer)
########################################
clock_lbl = Label(Clock_Child, text="", font=custom_font)
inside_frame_timer = LabelFrame(Timer_Child, text="Setup Timer")
spinbox_hr = Spinbox(inside_frame_timer, from_=0, to=24, width=2, font=custom_font, state='readonly', textvariable=HourVar)
spinbox_min = Spinbox(inside_frame_timer, from_=0, to=59, width=2, font=custom_font, state='readonly', textvariable=MinuteVar)
spinbox_sec = Spinbox(inside_frame_timer, from_=0, to=59, width=2, font=custom_font, state='readonly', textvariable=SecondVar)
lbl_hr_bottom = Label(inside_frame_timer, text="Hours")
lbl_min_bottom = Label(inside_frame_timer, text="Minutes")
lbl_sec_bottom = Label(inside_frame_timer, text="Seconds")
colon_label_hr = Label(inside_frame_timer, text=":", font=custom_font)
colon_label_min = Label(inside_frame_timer, text=":", font=custom_font)
Tab_Renderer.add(Clock_Child, text="Clock")
Tab_Renderer.add(Timer_Child, text="Timer")
Tab_Renderer.add(Stopwatch_Child, text="Stopwatch")
Tab_Renderer.add(Settings_Child, text="Settings")
# Pack Everything Up ##########
Tab_Renderer.pack()
clock_lbl.pack()

# Timer Screen######################
inside_frame_timer.pack()
spinbox_hr.grid(row=0, column=0)
colon_label_hr.grid(row=0, column=1)
spinbox_min.grid(row=0, column=2)
colon_label_min.grid(row=0, column=3)
spinbox_sec.grid(row=0, column=4)
lbl_hr_bottom.grid(row=1, column=0)
lbl_min_bottom.grid(row=1, column=2)
lbl_sec_bottom.grid(row=1, column=4)
####################################
icon = (cwd + '\\assets\clock.ico')
MainWindow.iconbitmap(icon)
MainWindow.after(1000, lambda: startup(0))
MainWindow.mainloop()
