from tkinter import ttk
import tkinter

class AddNew(tkinter.Frame):

	def __init__(self, parent, otac):
		self.otac = otac
		self.parent=parent
		self.frame = tkinter.Frame(self.parent)
		self.initialize_insert_interface()

	def initialize_insert_interface(self):
		self.parent.title("Canvas Test")
		self.parent.grid_rowconfigure(0,weight=1)
		self.parent.grid_columnconfigure(0,weight=1)
		self.parent.config(background="lavender")
		self.dose_label = tkinter.Label(self.parent, text = "LBO:")
		self.dose_entry = tkinter.Entry(self.parent)
		self.dose_label.grid(row = 1, column = 0, sticky = tkinter.W)
		self.dose_entry.grid(row = 1, column = 1)
		self.modified_label = tkinter.Label(self.parent, text = "ime:")
		self.modified_entry = tkinter.Entry(self.parent)
		self.modified_label.grid(row = 2, column = 0, sticky = tkinter.W)
		self.modified_entry.grid(row = 2, column = 1)
		self.dose_label = tkinter.Label(self.parent, text = "prezime:")
		self.dose_entry = tkinter.Entry(self.parent)
		self.dose_label.grid(row = 3, column = 0, sticky = tkinter.W)
		self.dose_entry.grid(row = 3, column = 1)
		self.modified_label = tkinter.Label(self.parent, text = "datum rodjenja:")
		self.modified_entry = tkinter.Entry(self.parent)
		self.modified_label.grid(row = 4, column = 0, sticky = tkinter.W)
		self.modified_entry.grid(row = 4, column = 1)
		self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.check)
		self.submit_button.grid(row = 0, column = 0, sticky = tkinter.W)
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		print("check")
		self.goBack()

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow)
