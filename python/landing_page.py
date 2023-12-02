#Creator: Daniela Munoz
#Purpose: Landing page of our Profiler for ITMS-548 final project

from tkinter import *
import tkinter as tk
from tkinter import ttk
import scrapy
import json
import requests
import webbrowser
from sockets_script import ip_puller
from tkinter import filedialog as fd
from tkinter import scrolledtext
import sys

win = tk.Tk()
win.geometry("1300x700")
win.title("IMTS-X48 OSINT Application")

ip_sets = set()

#main frame
main_frame = Frame(win)
main_frame.pack(fill=BOTH, expand=1)

#canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#using scrollbar
def on_scroll(*args):
    ip_results.yview(*args)

#scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

#intro
label = tk.Label(win, text="Welcome to Sneaky Web Crawler", font=('Courier 22 bold'))
label.pack(padx=20, pady=20)

#how to use label
how_to_label = Label(win, text="How To Use:", font = ('Courier', 15))
how_to_label.pack()

#how to use info block
how_to_info = "Please select a dataset from the dropdown bar, then click on 'Select Target' to confirm dataset then 'Go Crawl' to begin\n"

how_to_use = tk.Label(win, text=how_to_info, font=('Courier', 12), justify=tk.LEFT, wraplength=win.winfo_screenwidth() - 40)
how_to_use.pack(padx=20, pady=20)

#dropdown box for target selection
def show():
    label.config( text = clicked.get() )

options = ["Benign Dataset", "Malware Dataset", "Phishing Dataset", "Spam Dataset"]

clicked = StringVar()
clicked.set ("Benign Dataset")

drop = OptionMenu( win, clicked, *options )
drop.pack()

target = Button( win, text = "Select Target", command = show ).pack()

menu = Label(win, text = " ")
menu.pack()

#button to validate
tk.Button(win, text = "Go Crawl", command = show, width = 20).pack(pady=20)

#running the crawler
def on_crawl_clicked():
    selected_option = clicked.get()
    if selected_option == "Benign List":
        ippbenign = ip_puller('python/datasets/benign_list_big_final.csv')
        print("This will take some time please allow 30 minutes to 1 hour")
        ippbenign.run_pull()
        print(ippbenign.ips)
        for row in ippbenign.ips:
            ip_sets.add(row)
        print("Checking for success")
    elif selected_option == "Malware Dataset":
        ippmal = ip_puller('python/datasets/malware_dataset.csv')
        print("This will take some time please allow 30 minutes to 1 hour")
        ippmal.run_pull()
        print(ippmal.ips)
        for row in ippmal.ips:
            ip_sets.add(row)
        print("Checking for success")
    elif selected_option == "Phishing Dataset":
        ippphish = ip_puller('python/datasets/phishing_datset.csv')
        print("This will take some time please allow 30 minutes to 1 hour")
        ippphish.run_pull()
        print(ippphish.ips)
        for row in ippphish.ips:
            ip_sets.add(row)
        print("Checking for success")
    elif selected_option == "Spam Dataset":
        ippspam = ip_puller('python/datasets/spam.csv')
        print("This will take some time please allow 30 minutes to 1 hour")
        ippspam.run_pull()
        print(ippspam.ips)
        for row in ippspam.ips:
            ip_sets.add(row)
        print("Checking for success")
    else:
        print("Please select an IP Puller")
        return
    
    #new text box for output
    output_win = tk.Toplevel(win)
    output_win.title("Crawler Output")
    
    #text box for output
    output_text = scrolledtext.ScrolledText(output_win, crap=tk.WORD, width=90, height=50)
    output_text.pack()
    
    #moving print results to text box
    def print_to_text_box(*args, **kwargs):
        output_text.insert(tk.END, *args, **kwargs)
        output_text.see(tk.END)
        
    sys.stdout = print_to_text_box
    
    on_crawl_clicked()

#report button ("Would you like to report this malicious page to Google? | -> send them to googles report page")
def link():
    url = "https://developers.google.com/search/help/report-quality-issues" 
    webbrowser.open(url)

report_button = Button(win, text = "Report Malicious Page", command=link)
report_button.pack(pady=20)

#pdf button ("Copy of Report")

win.mainloop()