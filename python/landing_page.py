#Creator: Daniela Munoz
#Purpose: Landing page of our Profiler for ITMS-548 final project

from tkinter import *
import tkinter as tk

window = tk.Tk()
window.geometry("900x700")
window.title("Dummy Name")

#intro
label = tk.Label(window, text="Welcome to Dummy Name", font=('Courier 22 bold'))
label.pack(padx=20, pady=20)

#how to use label
how_to_label = Label(window, text="How To Use:", font = ('Courier', 15))
how_to_label.pack()

#how to use info block
how_to_info = "Enter a website URL in the target box below to run the crawler. Example targets include:\n" "https://www.reddit.com/ or https://www.nytimes.com/\n"

how_to_use = tk.Label(window, text=how_to_info, font=('Courier', 12), justify=tk.LEFT, wraplength=window.winfo_screenwidth() - 40)
how_to_use.pack(padx=20, pady=20)

#target label for user input
target = Label(window, text="Target:", font = ('Courier', 15))
target.pack()

#accepting target input
input = Entry(window, width = 40)
input.focus_set()
input.pack()

#button to validate
tk.Button(window, text = "Go Crawl", width = 20).pack(pady=20)

#output (in same page)

#analysis (in same page)

#output portion

#report button ("Would you like to report this malicious page to Google? | -> send them to googles report page")

#pdf button ("Copy of Report")

window.mainloop()

#Requirements: IP, Web certifications, Domain information, Location, Direct URLs, Images (if availiable), and Video
