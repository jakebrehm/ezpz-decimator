import csv
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk

import lemons.gui as gui


class Main(gui.Application):

	def __init__(self, *args, **kwargs):

		# Initialize the application
		gui.Application.__init__(self, *args, **kwargs)
		self.configure(
			title='EZPZ Reducer',
			icon=gui.ResourcePath(r'Assets\icon.ico'),
			resizable=False,
		)

		# Add a logo to the top of the application
		header = gui.Header(
			master=self,
			logo=gui.ResourcePath(r'Assets\logo.png'),
			downscale=10,
		)
		header.grid(row=0, column=0, sticky='NSEW')

		# Separate the logo from what's below it
		separator1 = ttk.Separator(self, orient='horizontal')
		separator1.grid(row=1, column=0, pady=10, sticky='NSEW')

		# Create a primary frame to hold input/output fields
		primary = tk.Frame(self)
		primary.grid(row=2, column=0, sticky='NSEW')

		self.inputs = gui.InputField(
			master=primary,
			quantity='multiple',
			appearance='entry',
			width=45,
		)
		self.inputs.grid(row=0, column=0, pady=(0, 5), sticky='NSEW')

		self.output = gui.OutputField(
			master=primary,
			quantity='saveas',
			filetypes=[('Comma-separated Values (*.csv)', '.csv')],
			default='.csv',
			width=45,
		)
		self.output.grid(row=1, column=0, sticky='NSEW')

		# Separate the primary and secondary frames
		separator2 = ttk.Separator(self, orient='horizontal')
		separator2.grid(row=3, column=0, pady=10, sticky='NSEW')

		# Create a secondary frame to hold other fields
		secondary = tk.Frame(self)
		secondary.grid(row=4, column=0, sticky='NSEW')
		secondary.columnconfigure(0, weight=1)

		self.header_entry = LabeledEntry(
			master=secondary,
			text='Header rows:',
			width=5,
		)
		self.header_entry.grid(row=0, column=0, pady=(0, 5), sticky='NSEW')
		
		self.factor_entry = LabeledEntry(
			master=secondary,
			text='Decimation factor:',
			width=5,
		)
		self.factor_entry.grid(row=1, column=0, sticky='NSEW')

		# Separate the secondary frame from the footer
		separator3 = ttk.Separator(self, orient='horizontal')
		separator3.grid(row=5, column=0, pady=10, sticky='NSEW')

		# Create a footer frame
		footer = tk.Frame(self)
		footer.grid(row=6, column=0, sticky='NSEW')
		footer.columnconfigure(1, weight=1)

		self.include_check = ttk.Checkbutton(
			master=footer,
			text='Include headers',
			takefocus=False,
		)
		self.include_check.grid(row=0, column=0, sticky='NSW')
		self.include_check.state(['!alternate', 'selected'])
		
		reduce_button = ttk.Button(
			master=footer,
			text='Reduce',
			takefocus=0,
			command=self._reduce,
		)
		reduce_button.grid(row=0, column=2, sticky='NSE')

		# Add relevant key bindings
		self.bind('<Return>', reduce_button['command'])

	def _get_inputs(self):
		return {
			'filepaths': self.inputs.get(),
			'destination': self.output.get(),
			'header rows': int(self.header_entry.get()),
			'include header': self.include_check.instate(['selected']),
			'factor': int(self.factor_entry.get()),
		}

	def _separate_data(self, inputs):

		# Extract relevant information from the inputs
		filepaths = inputs['filepaths']
		HEADER_ROWS = inputs['header rows']
		INCLUDE_HEADER = inputs['include header']

		# Initialize variables
		overall_row = 0
		header = []
		data = []
		
		# Iterate through the files
		for f, filepath in enumerate(filepaths, start=1):
			with open(filepath, 'r') as data_file:
				# Initialize the csv reader
				reader = csv.reader(data_file, delimiter=',')
				# If the header has not yet been stored, store it
				if not header and INCLUDE_HEADER:
					for row in range(HEADER_ROWS):
						header_row = next(reader)
						header.append(header_row)
				# Otherwise, skip over the header
				else:
					for row in range(HEADER_ROWS):
						next(reader)
				# Store the data from the file and add the file number
				for row in reader:
					data.append(row)
					data[-1].insert(0, f)
					overall_row += 1
		
		# Add labels to the file number column of the header
		for h, row in enumerate(header):
			string = 'File' if (h == 0) else '#' if (h == 1) else ''
			row.insert(0, string)

		# Return the header and data lists
		return header, data

	def _write(self, inputs, header, data):

		# Extract relevant information from the inputs
		DESTINATION = inputs['destination']
		DECIMATION_FACTOR = inputs['factor']

		# Initialize the csv writer
		with open(DESTINATION, 'w', newline='') as output:
			writer = csv.writer(output, delimiter=',')
			# Write the header
			writer.writerows(header)
			# Decimate and write the data
			for r, row in enumerate(data):
				if not r % DECIMATION_FACTOR:
					writer.writerow(row)

	def _reduce(self):
		# Grab the user's inputs and reduce
		inputs = self._get_inputs()
		header, data = self._separate_data(inputs)
		self._write(inputs, header, data)
		# Display a message letting the user know it was a success
		msg.showinfo(
			title='Success!',
			message='Please navigate to where you chose to save the file.'
		)


class LabeledEntry(tk.Frame):
	
	def __init__(self, master, text, *args, **kwargs):

		tk.Frame.__init__(self, master)
		self.columnconfigure(0, weight=1)

		self.label = tk.Label(self, text=text)
		self.label.grid(row=0, column=0, padx=(0, 5), sticky='NSE')

		self.entry = ttk.Entry(self, *args, **kwargs)
		self.entry.grid(row=0, column=1, sticky='NSEW')

	def get(self):
		return self.entry.get()

	def set(self, value):
		self.entry.delete(0, 'end')
		self.entry.insert(0, value)


if __name__ == '__main__':
	app = Main(padding=10)
	app.mainloop()