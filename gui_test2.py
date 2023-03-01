from tkinter import *
from tkinter import ttk
from aggresive import agg_scan
from deep import deep_scan
from port import port_scan

root = Tk()
root.title('Vulnerability Scanner using N-Map')
root.geometry("500x350")



root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(2,weight=1)



#creating the main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


#creating the canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#adding the scrollbar
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame inside the canvas
second_frame = Frame(my_canvas)
second_frame.grid(row=1,column=1)

#add that new frame to a window in the canvas
my_canvas.create_window((900,0), window=second_frame, anchor="nw")

#creating the button functions
def submit1():
	greet = agg_scan(my_box.get())
	my_label.config(text=greet)

def submit2():
	greet = deep_scan(my_box.get())
	my_label.config(text=greet)

def submit3():
	greet = port_scan(my_box.get())
	my_label.config(text=greet)

my_box = Entry(second_frame)
my_box.pack(pady=20)

my_label = Label(second_frame, text="Enter the target website or its IP address", font=("Helvetica", 10))
my_label.pack(pady=0)

my_button = Button(second_frame, text="Aggressive Scan(2-5 minutes)", command=submit1)
my_button.pack(pady=20)

my_button1 = Button(second_frame, text="Deep Scan(20-25 minutes)", command=submit2)
my_button1.pack(pady=20)

my_button1 = Button(second_frame, text="Port Scan(2-5 minutes)", command=submit3)
my_button1.pack(pady=20)


root.mainloop()