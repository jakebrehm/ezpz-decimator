#####################################################################################################
#####################################################################################################
#################          _____            _                 _                     #################
#################         |  __ \          (_)               | |                    #################
#################         | |  | | ___  ___ _ _ __ ___   __ _| |_ ___  _ __         #################
#################         | |  | |/ _ \/ __| | '_ ` _ \ / _` | __/ _ \| '__|        #################
#################         | |__| |  __/ (__| | | | | | | (_| | || (_) | |           #################
#################         |_____/ \___|\___|_|_| |_| |_|\__,_|\__\___/|_|           #################
#################                                                                   #################
#################                                        Author: Jacob Brehm (2019) #################
#####################################################################################################
#####################################################################################################                                               
                                                   
import csv
import ctypes
import platform
import lemons.gui as gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

#####################################################################################################
#################                         MAIN FUNCTIONALITY                        #################
#####################################################################################################

def MessageBox(title, text):
	''' Displays a message box with the desired title and text. '''
	return ctypes.windll.user32.MessageBoxW(0, text, title, 0)

def Reduce(event=None):
	''' Concatenates and reduces data based on user inputs that are read from the GUI. '''

	# Store user inputs
	try:
		filepaths = inputs.get()
		output = outputs.get()
		HEADERS = int(header_entry.get())
		KEEP = int(factor_entry.get())
	except:
		MessageBox('Sorry!', 'There was a problem trying to store your inputs.')

	# Initialize variables
	headers = []
	data = []
	overall_row = 0

	# Read the data from each file, only storing the header once
	try:
		for file, filepath in enumerate(filepaths, start=1):
			reader = csv.reader(open(filepath, 'r'), delimiter=',')
			if not headers:
				if include_check.instate(['selected']):
					for row in range(HEADERS):
						header = next(reader)
						headers.append(header)
				else:
					[next(reader) for row in range(HEADERS)]
			else:
				[next(reader) for row in range(HEADERS)]
			# Add a new column which contains the file number
			for r, row in enumerate(reader, start=overall_row):
				data.append(row)
				data[r].insert(0, file)
				overall_row += 1
	except:
		MessageBox('Sorry!', 'There was a problem reading and storing the data.')

	# Add information to the header for the new file number column
	try:
		for i in range(len(headers)):
			string = 'File' if i == 0 else ('#' if i == 1 else '')
			headers[i].insert(0, string)
	except:
		MessageBox('Sorry!', 'There was a problem adding new header information.')

	# Write the data to a new csv, applying data reduction
	try:
		with open(output, 'w', newline='') as decimated:
			writer = csv.writer(decimated, delimiter=',')
			[writer.writerow(row) for row in headers]
			for r, row in enumerate(data, start=0):
				if r % KEEP == 0:
					writer.writerow(row)
	except:
		MessageBox('Sorry!', 'There was a problem writing the data to a new file.')

	# Let the user know that the process has been completed successfully
	MessageBox('Success!', 'Please navigate to where you chose to save the output file.')

#####################################################################################################
#################                                GUI                                #################
#####################################################################################################

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
inputs = gui.InputField(primary, quantity='multiple', appearance='entry', width=45)
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
include_check = ttk.Checkbutton(footer, text='Include headers', takefocus=False)
include_check.grid(row=0, column=0, sticky="W")
include_check.state(['!alternate','selected'])
reduce_button = ttk.Button(footer, text='Reduce', takefocus=False, command=Reduce)
reduce_button.grid(row=0, column=1, sticky="E")
footer.grid(row=app_row, column=0, sticky="EW")
footer.columnconfigure(0, weight=1)

app.bind('<Return>', Reduce)

app.mainloop()

#####################################################################################################
#####################################################################################################
##############################  ______ _       _     _              _  ##############################
##############################  |  ___(_)     (_)   | |            | | ##############################
##############################  | |_   _ _ __  _ ___| |__   ___  __| | ##############################
##############################  |  _| | | '_ \| / __| '_ \ / _ \/ _` | ##############################
##############################  | |   | | | | | \__ \ | | |  __/ (_| | ##############################
##############################  \_|   |_|_| |_|_|___/_| |_|\___|\__,_| ##############################
##############################                                         ##############################
#####################################################################################################
#####################################################################################################