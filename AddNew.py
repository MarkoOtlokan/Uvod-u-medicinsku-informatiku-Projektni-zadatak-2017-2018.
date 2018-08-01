import calendar
import datetime
from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient
from Call import Calendar

class AddNew(tkinter.Frame):

	def __init__(self, parent, otac, patienteKeys):
		self.patienteKeys = patienteKeys
		self.data = {}
		self.otac = otac
		self.parent=parent
		self.frame = tkinter.Frame(self.parent)
		self.initialize_insert_interface()

	def initialize_insert_interface(self):
		self.v = ''
		self.parent.title("Canvas Test")
		self.parent.grid_rowconfigure(0,weight=1)
		self.parent.grid_columnconfigure(0,weight=1)
		self.parent.config(background="lavender")
		self.LBO_label = tkinter.Label(self.parent, text = "LBO:")
		self.LBO_entry = tkinter.Entry(self.parent)
		self.LBO_label.grid(row = 1, column = 0, sticky = tkinter.W)
		self.LBO_entry.grid(row = 1, column = 1)
		self.name_label = tkinter.Label(self.parent, text = "ime:")
		self.name_entry = tkinter.Entry(self.parent)
		self.name_label.grid(row = 2, column = 0, sticky = tkinter.W)
		self.name_entry.grid(row = 2, column = 1)
		self.surname_label = tkinter.Label(self.parent, text = "prezime:")
		self.surname_entry = tkinter.Entry(self.parent)
		self.surname_label.grid(row = 3, column = 0, sticky = tkinter.W)
		self.surname_entry.grid(row = 3, column = 1)
		self.date_of_birth_label = tkinter.Label(self.parent, text = "datum rodjenja:")
		self.date_of_birth_entry = tkinter.Entry(self.parent)
		self.date_of_birth_label.grid(row = 4, column = 0, sticky = tkinter.W)
		self.date_of_birth_entry.grid(row = 4, column = 1)
		self.date_Button = ttk.Button(self.parent, text='Choose',command=self.calCal)
		self.date_Button.grid(row = 4, column = 2)
		self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.check)
		self.submit_button.grid(row = 0, column = 0, sticky = tkinter.W)
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		self.fillDate() # treba ga postaviti negde da cim se popuni kalendar, da se on izvrsi
		tmpLBO = self.LBO_entry.get()
		print(len(tmpLBO))
		if(len(tmpLBO) != 11 or tmpLBO.isdigit() == False):
			messagebox.showinfo("Greska", "Lose unet LBO")
			return
		for key in self.patienteKeys:
			if key == self.LBO_entry.get():
				messagebox.showinfo("Greska", "Uneseni LBO vec postoji")
				return
		tmpPatient = Patient(int(tmpLBO), self.name_entry.get(), self.surname_entry.get(),self.date_of_birth_entry.get() )
		Patient.addNewPatient(tmpPatient)
		messagebox.showinfo("Uspeh", "Uspesno ste uneli pacijenta")
		self.goBack()

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow)

	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child, self.data)

	def fillDate(self):
		self.date_of_birth_entry.insert(0, str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))
