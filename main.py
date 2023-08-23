from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.messagebox as tmsg
from tkinter import simpledialog
import helper1 as he
from queue import Queue
import ast

color_one = "orange"
color_two = "white"

helvita = ("Helvetica", 15,"bold")

great = ("Helvetica", 40,"bold")

def open_file():
    global srcpath
    srcpath = simpledialog.askstring(title="Input", prompt="Enter chemical name:")
    # askopenfilename(filetypes=[("raw files", "*.raw")])
    if srcpath == "" or srcpath == "()":
        print("no file name detected")
        pass
        #lbl = Label(window, text = f"Source {srcpath}",font = helvita, bg = "green").pack()
        # Button(window, text = "Start",font = helvita, bg = "orange", command = start_pro).pack(pady = 100)

def close_file():
    global srcpath
    srcpath = ""
    msg = "File is Unselected"
    tmsg.showinfo("Unselect", msg)

def start_pro():
    if (srcpath == "" or srcpath == "()"):
        msg = "No chemical name is entered"
        tmsg.showinfo("Chemical", msg)
    # elif (destpath == "" or destpath == "()") :
    #     msg = "No Destination Folder is Selected"
    #     tmsg.showinfo("Recovered", msg)
    else: 
        destpath = "image/"
        print(srcpath)
        print(destpath)
        ans = he.Create_graph(srcpath)
        msg = f"file stored in image Directory"
        tmsg.showinfo("chemical", msg)

def makeExit():
    res = tmsg.askquestion('Exit Application', 'Do you really want to exit')
    if res == 'yes' :
        window.destroy()
    else :
        tmsg.showinfo('Return', 'Returning to main application')

def ask_dest():
    global destpath
    destpath = askdirectory()

def forget_dest():
    global destpath
    destpath = ""
    msg = "Folder is Unselected"
    tmsg.showinfo("Unselect", msg)

def rate():
    msg = "Rate Us on Software Store"
    tmsg.showinfo("Rate us", msg)

def feedback():
    msg = "Sorry to hear that\nWrite us on princeydv1999@gmail.com"
    tmsg.showinfo("Feedback", msg)

def get_name(compound_name):
	compound_name = compound_name.split()
	print("starting importing data")
	count = 0
	n = len(compound_name)

	for i in range(n):
		compound_name[i] = compound_name[i].lower()
		#print(word)
	compound_name[0] = compound_name[0].capitalize()
	print(compound_name)

	name = "_".join(compound_name)
	return name

def odd_even_compare():
	global first
	global second
	global third

	first = simpledialog.askstring(title="Input", prompt="Enter chemical name:")
	if first == "" or first == "()":
		print("no file name detected")
		pass
	second = simpledialog.askstring(title="Input", prompt="Enter chemical name:")
	if second == "" or second == "()":
		print("no file name detected")
	third = simpledialog.askstring(title="Input", prompt="Enter chemical name:")
	if third == "" or third == "()":
		print("no file name detected")
	first = get_name(first)
	second = get_name(second)
	third = get_name(third)
	num1 = maptoint[first]
	num2 = maptoint[second]
	num3 = maptoint[third]
	dist12 = he.leastDistance(graph, num1, num2)
	dist23 = he.leastDistance(graph, num2, num3)
	dist13 = he.leastDistance(graph, num1, num3)
	msg = f"{first} {second} {dist12}\n {second} {third} {dist23}\n {first} {third} {dist13}"
	tmsg.showinfo("Conclusion", msg)


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x550")
        self.maxsize(1100,800)
        self.minsize(850,550)
        self.title("Knowledge Graph of Chemical Compounds")
        self.configure(background = color_one)
    

if __name__ == "__main__":
	filename = "chemicals.txt"
	with open(filename) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]
	maptoint = {}
	j = 0
	for i in lines:
		if i in maptoint.keys():
			pass
		else:
			maptoint[i] = j
			j += 1
	with open('graph.txt') as f:
		data = f.read()
	  
	print("Data type before reconstruction : ", type(data))
		  
	# reconstructing the data as a dictionary
	graph = ast.literal_eval(data)
	global srcpath
	global destpath
	srcpath = ""
	destpath = ""
	window = GUI()
	menubar = Menu(window)

	m1 = Menu(menubar, tearoff = 0)
	# m1.add_command(label = "Enter_name", font = helvita, command = open_file)
	# m1.add_separator()
	# m1.add_command(label = "Unselect Source File", font = helvita, command = close_file)
	# m1.add_separator()
	# m1.add_command(label = "Select Destination Folder", font = helvita, command = ask_dest)
	# m1.add_separator()
	# m1.add_command(label = "Unselect Destination Folder", font = helvita, command = forget_dest)
	window.config(menu = menubar)
	menubar.add_command(label="Enter_name",font = helvita, command = open_file)
	# inputtxt = window.Text(frame,height = 5,width = 20)
	# inputtxt.pack()

	menubar.add_command(label = "Create_graph", font = helvita, command = start_pro)
	menubar.add_command(label = "odd_even", font = helvita, command = odd_even_compare)
	window.config(menu = menubar)

	m3 = Menu(menubar, tearoff = 0)
	m3.add_command(label = "Feedback", font = helvita, command = feedback)
	m3.add_separator()
	m3.add_command(label = "Rate Us", font = helvita, command = rate)
	window.config(menu = menubar)
	menubar.add_cascade(label="Rate", font = helvita, menu = m3)

	Label(window, text = "Knowledge Graph of Chemicals",bg = color_one, fg = "blue", font = great).pack()
	Label(window, text = "-Prince, Swastika, Suman", bg = color_one, font = helvita).pack(padx = 10, anchor = 'e')

	try:
		photo = PhotoImage(file="logo.png")
		l1 = Label(image=photo)
		l1.pack()
	except:
		pass


	Label(window, text = "Quick Guide",bg = color_one, fg = "blue", font = great).pack(padx = 10,pady = (10,0), anchor='w')
	Label(window, text = "1.Click create graph",bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')
	Label(window, text = "2.Enter the chemical compound name", bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')
	Label(window, text = "3. graph will created in img/ directory", bg = color_one, font = helvita).pack(padx = 10, anchor = 'w')

	menubar.add_command(label = "Exit", font = helvita, command = makeExit)
	window.config(menu = menubar)

	window.mainloop()
