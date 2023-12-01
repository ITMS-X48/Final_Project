#Creator: Daniela Munoz
#Purpose: Landing page of our Profiler for ITMS-548 final project

from tkinter import *
import tkinter as tk
from tkinter import ttk
import scrapy
from my_spiders import spider_one
from my_spiders import spider_two
from my_spiders import spider_three
import json
import requests
import webbrowser

window = tk.Tk()
window.geometry("900x700")
window.title("IMTS-X48")

#intro
label = tk.Label(window, text="Welcome to Sneaky Web Crawler", font=('Courier 22 bold'))
label.pack(padx=20, pady=20)

#how to use label
how_to_label = Label(window, text="How To Use:", font = ('Courier', 15))
how_to_label.pack()

#how to use info block
how_to_info = "Enter a website URL in the target box below to run the crawler. Example targets include:\n" "https://www.reddit.com/ or https://www.nytimes.com/\n"

how_to_use = tk.Label(window, text=how_to_info, font=('Courier', 12), justify=tk.LEFT, wraplength=window.winfo_screenwidth() - 40)
how_to_use.pack(padx=20, pady=20)

#dropdown box for target selection
def show():
    label.config( text = clicked.get() )

#benign= spider 1, malware= spider 2, phishing= spider 3
options = ["Benign List", "Malware Dataset", "Phishing Dataset"]

clicked = StringVar()
clicked.set ("Benign List")

drop = OptionMenu( window, clicked, *options )
drop.pack()

target = Button( window, text = "Select Target", command = show ).pack()

menu = Label(window, text = " ")
menu.pack()

#button to validate
tk.Button(window, text = "Go Crawl", command = show, width = 20).pack(pady=20)

#running the spider
def on_crawl_clicked():
    selected_option = clicked.get()
    if selected_option == "Benign List":
        spider_one.run_spider_one()
        print("Checking for success")
    elif selected_option == "Malware Dataset":
        spider_two.run_spider_two()
        print("Checking for success")
    elif selected_option == "Phishing Dataset":
        spider_three.run_spider_three()
        print("Checking for success")
    else:
        print("Please select a spider")
        return

# from url in list, pull the ip, append to the api url, pull all json info


# Pulling JSON info

#report button ("Would you like to report this malicious page to Google? | -> send them to googles report page")
def link():
    url = "https://developers.google.com/search/help/report-quality-issues" 
    webbrowser.open(url)

report_button = Button(window, text = "Report Malicious Page", command=link)
report_button.pack(pady=20)

#pdf button ("Copy of Report")

#Requirements: IP, Web certifications, Domain information, Location, Direct URLs, Images (if availiable), and Video

window.mainloop()