import csv
import ctypes
import platform
import lemons.gui as gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

def MessageBox(title, text):
	''' Displays a message box with the desired title and text. '''
	return ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def Reduce(event=None):

	filepaths = inputs.get
	output = outputs.get
	HEADERS = int(header_entry.get())
	KEEP = int(factor_entry.get())

	headers = []
	data = []

	for file, filepath in enumerate(filepaths, start=1):
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
		for r, row in enumerate(reader, start=0):
			data.append(row)
			data[r].insert(0, file)

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
		for r, row in enumerate(data, start=0):
			if r % KEEP == 0:
				writer.writerow(row)
			r += 1

	MessageBox('Success!', 'Please navigate to where you chose to save the output file.')

app = gui.Application(padding=20)
app.configure(title='EZPZ Decimator',
	icon=gui.ResourcePath('Assets\\icon.ico'),
	resizable=False)
app_row = 0

path = gui.ResourcePath('Assets\\logo.png')
header = gui.Header(app, logo=path, downscale=10)
header.grid(row=app_row, column=0, sticky='NSEW')
app_row += 1

gui.Separator(app, padding=(0, 20)).grid(row=app_row, column=0, sticky='NSEW')
app_row += 1

primary = tk.Frame(app)
inputs = gui.InputField(primary, quantity='multiple', appearance='entry', width=40)
inputs.grid(row=0, column=0, sticky='NSEW')
gui.Space(primary, row=1, column=0, padding=5)
filetypes = [('Comma-separated Values (*.csv)', '.csv')]
default = '.csv'
outputs = gui.OutputField(primary, quantity='saveas', filetypes=filetypes, default=default)
outputs.grid(row=2, column=0, sticky='NSEW')
primary.columnconfigure(0, weight=1)
primary.grid(row=app_row, column=0, sticky='NSEW')
app_row += 1

gui.Separator(app, padding=(0, 20)).grid(row=app_row, column=0, sticky='NSEW')
app_row += 1

secondary = tk.Frame(app)
header_label = ttk.Label(secondary, text='Header rows:')
header_label.grid(row=0, column=0, sticky="E")
header_entry = ttk.Entry(secondary, width=5)
header_entry.grid(row=0, column=2)
gui.Space(secondary, row=1, column=0, direction='horizontal', columnspan=2, padding=5)
gui.Space(secondary, row=0, column=1, direction='vertical', rowspan=3, padding=5)
factor_label = ttk.Label(secondary, text='Decimation factor:')
factor_label.grid(row=2, column=0, pady=(5,0), sticky="E")
factor_entry = ttk.Entry(secondary, width=5)
factor_entry.grid(row=2, column=2)
secondary.grid(row=app_row, column=0, sticky="EW")
secondary.columnconfigure(0, weight=1)
app_row += 1

gui.Separator(app, padding=(0, 20)).grid(row=app_row, column=0, sticky='NSEW')
app_row += 1

footer = tk.Frame(app)
include_check = ttk.Checkbutton(footer, text='Include headers')
include_check.grid(row=0, column=0, sticky="W")
include_check.state(['!alternate','selected'])
reduce_button = ttk.Button(footer, text='Reduce', command=Reduce)
reduce_button.grid(row=0, column=1, sticky="E")
footer.grid(row=app_row, column=0, sticky="EW")
footer.columnconfigure(0, weight=1)

app.bind('<Return>', Reduce)

app.mainloop()