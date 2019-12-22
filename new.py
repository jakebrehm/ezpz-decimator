import csv
import ctypes
import platform
import tkinter as tk
from tkinter import messagebox as mb
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

		inputs = gui.InputField(
			master=primary,
			quantity='multiple',
			appearance='entry',
			width=45,
		)
		inputs.grid(row=0, column=0, pady=(0, 5), sticky='NSEW')

		outputs = gui.OutputField(
			master=primary,
			quantity='saveas',
			filetypes=[('Comma-separated Values (*.csv)', '.csv')],
			default='.csv',
			width=45,
		)
		outputs.grid(row=1, column=0, sticky='NSEW')

		# Separate the primary and secondary frames
		separator2 = ttk.Separator(self, orient='horizontal')
		separator2.grid(row=3, column=0, pady=10, sticky='NSEW')

		# Create a secondary frame to hold other fields
		secondary = tk.Frame(self)
		secondary.grid(row=4, column=0, sticky='NSEW')
		secondary.columnconfigure(0, weight=1)

		header_entry = LabeledEntry(
			master=secondary,
			text='Header rows:',
			width=5,
		)
		header_entry.grid(row=0, column=0, pady=(0, 5), sticky='NSEW')
		
		factor_entry = LabeledEntry(
			master=secondary,
			text='Decimation factor:',
			width=5,
		)
		factor_entry.grid(row=1, column=0, sticky='NSEW')

		# Separate the secondary frame from the footer
		separator3 = ttk.Separator(self, orient='horizontal')
		separator3.grid(row=5, column=0, pady=10, sticky='NSEW')

		# Create a footer frame
		footer = tk.Frame(self)
		footer.grid(row=6, column=0, sticky='NSEW')
		footer.columnconfigure(1, weight=1)

		include_check = ttk.Checkbutton(
			master=footer,
			text='Include headers',
			takefocus=False,
		)
		include_check.grid(row=0, column=0, sticky='NSW')
		include_check.state(['!alternate', 'selected'])
		
		reduce_button = ttk.Button(
			master=footer,
			text='Reduce',
			takefocus=0,
			# command=Reduce,
		)
		reduce_button.grid(row=0, column=2, sticky='NSE')

		# Add relevant key bindings
		self.bind('<Return>', reduce_button['command'])


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