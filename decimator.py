import csv
import glob
import re
import os
import sys
import ctypes
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import filedialog as fd
from PIL import Image, ImageTk

# To learn how to keep the window icon when using PyInstaller, read:
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile

PROGRAM_WIDTH = 300
PROGRAM_HEIGHT = 334
MARGIN_SIZE = 10

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def ResourcePath(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

def MessageBox(title, text):
	''' Displays a message box with the desired title and text. '''
	return ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def Input():
	global inputs
	files = fd.askopenfilenames(initialdir=desktop, title='Choose the files to concatenate and reduce')
	inputs = list(files)
	if len(files) != 0:
		input_entry.config(state='normal')
		input_entry.delete(0,'end')
		input_entry.insert(0,files)
		input_entry.config(state='readonly')
		input_entry.update_idletasks()
		input_entry.xview_moveto(1)

def Output():
	output = fd.asksaveasfilename(initialdir=desktop, title="Choose where to save output file", defaultextension="*.*", filetypes=[('Comma-separated Values', '.csv'), ('All Files', '.*')])
	if len(output) != 0:
		output_entry.config(state='normal')
		output_entry.delete(0,'end')
		output_entry.insert(0,output)
		output_entry.config(state='readonly')
		output_entry.update_idletasks()
		output_entry.xview_moveto(1)

def Reduce(event=None):
	global inputs
	try:
		output = output_entry.get()
		HEADERS = int(header_entry.get())
		KEEP = int(keep_entry.get())

		headers = []
		data = []
		i = 0
		index = 0
		file = 1

		for filepath in inputs:
			reader = csv.reader(open(filepath, 'r'), delimiter=',')
			if not headers:
				if include_check.instate(['selected']):
					for row in range(HEADERS):
						header = next(reader)
						headers.append(header)
				else:
					for row in range(HEADERS):
						next(reader)
			else:
				for row in range(HEADERS):
					next(reader)
			for row in reader:
				data.append(row)
				data[i].insert(0, file)
				i += 1
			file += 1

		for i in range(len(headers)):
			if i == 0:
				headers[i].insert(0, 'File')
			elif i == 1:
				headers[i].insert(0, '#')
			else:
				headers[i].insert(0, '')

		with open(output, 'w', newline='') as reduced:
			writer = csv.writer(reduced, delimiter=',')
			for row in headers:
				writer.writerow(row)
			for row in data:
				if index % KEEP == 0:
					writer.writerow(row)
				index += 1

		MessageBox('Success!', 'Please navigate to where you chose to save the output file.')

	except:
		MessageBox('Something went wrong...', 'Make sure you have filled in all parts of the form.')

root = tk.Tk()

# title = tk.Frame(root)
# title_label = ttk.Label(title, text="Data Reducer", font='Helvetica 22 bold').grid(row=0, column=0, sticky="EW")
# title.grid(row=1, column=1)

header = tk.Frame(root)
header.grid_rowconfigure(0, minsize=MARGIN_SIZE)
logo_title = tk.Frame(header)
logo_load = Image.open(ResourcePath('Assets\\logo.png'))
logo_load = logo_load.resize((int(2448/10),int(505/10)), Image.ANTIALIAS)
logo_render = ImageTk.PhotoImage(logo_load)
logo = ttk.Label(logo_title, image=logo_render)
logo.photo = logo_render
logo.grid(row=0, column=0)
logo_title.grid(row=1, column=0, sticky='EW')
header.grid_rowconfigure(2, minsize=MARGIN_SIZE)
header.grid(row=1, column=1)

root.grid_rowconfigure(2, minsize=MARGIN_SIZE)
ttk.Separator(root).grid(row=3, column=0, columnspan=3, sticky="WE")
root.grid_rowconfigure(4, minsize=MARGIN_SIZE)

subtitle = tk.Frame(root)
description = tk.StringVar()
description.set('Select multiple similarly-formatted csv files to\nconcatenate them and apply data reduction.')
description_label = tk.Label(subtitle, textvariable=description, width=39)
description_label.grid(row=0, column=0, sticky="EW")
description_label.configure(anchor='center')
subtitle.grid(row=5, column=1, sticky="EW")

root.grid_rowconfigure(6, minsize=MARGIN_SIZE)
ttk.Separator(root).grid(row=7, column=0, columnspan=3, sticky="WE")
root.grid_rowconfigure(8, minsize=MARGIN_SIZE)

primary = tk.Frame(root)
input_label = ttk.Label(primary, text='Input:').grid(row=0, column=0, sticky="E")
input_entry = ttk.Entry(primary, state='disabled')
input_entry.grid(row=0, column=1, padx=MARGIN_SIZE, sticky="EW")
input_button = ttk.Button(primary, text='Browse...', command=Input).grid(row=0, column=2)
output_label = ttk.Label(primary, text='Output:').grid(row=1, column=0, pady=(5,0), sticky="E")
output_entry = ttk.Entry(primary, state='disabled')
output_entry.grid(row=1, column=1, padx=MARGIN_SIZE, pady=(5,0), sticky="EW")
output_button = ttk.Button(primary, text='Browse...', command=Output).grid(row=1, column=2, pady=(5,0))
primary.grid(row=9, column=1, sticky="EW")
primary.columnconfigure(1, weight=1000)

root.grid_rowconfigure(10, minsize=MARGIN_SIZE)

secondary = tk.Frame(root)
header_label = ttk.Label(secondary, text='Number of rows in the header:').grid(row=0, column=0, sticky="E")
header_entry = ttk.Entry(secondary, width=5)
header_entry.grid(row=0, column=1, padx=(MARGIN_SIZE,0))
keep_label = ttk.Label(secondary, text='Keep one out of every ___ rows:').grid(row=1, column=0, pady=(5,0), sticky="E")
keep_entry = ttk.Entry(secondary, width=5)
keep_entry.grid(row=1, column=1, padx=(MARGIN_SIZE,0), pady=(5,0))
secondary.grid(row=11, column=1, sticky="EW")
secondary.columnconfigure(0, weight=1000)

root.grid_rowconfigure(12, minsize=MARGIN_SIZE)
ttk.Separator(root).grid(row=13, column=0, columnspan=3, sticky="WE")
root.grid_rowconfigure(14, minsize=MARGIN_SIZE)

footer = tk.Frame(root)
include_check = ttk.Checkbutton(footer, text='Include headers')
include_check.grid(row=0, column=0, sticky="W")
include_check.state(['!alternate','selected'])
reduce_button = ttk.Button(footer, text='Reduce', command=Reduce).grid(row=0, column=1, sticky="E")
footer.grid(row=15, column=1, sticky="EW")
footer.columnconfigure(0, weight=1000)

root.geometry(str(PROGRAM_WIDTH) + "x" + str(PROGRAM_HEIGHT))
root.resizable(width=False, height=False)
root.title('EZPZ Decimator')
root.grid_columnconfigure(0, minsize=MARGIN_SIZE)
root.grid_columnconfigure(1, minsize=PROGRAM_WIDTH-2*MARGIN_SIZE)
root.grid_columnconfigure(2, minsize=MARGIN_SIZE)
root.grid_rowconfigure(0, minsize=MARGIN_SIZE)

root.bind('<Return>', Reduce)

root.iconbitmap(default=ResourcePath('Assets\\icon.ico'))

root.mainloop()