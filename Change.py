from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient

class Change(tkinter.Frame):

	def __init__(self, parent, otac, patient):
		self.patient = patient

		self.otac = otac
		self.parent=parent
		self.frame = tkinter.Frame(self.parent)
		self.initialize_insert_interface()

	def initialize_insert_interface(self):
		self.parent.title("Canvas Test")
		self.parent.grid_rowconfigure(0,weight=1)
		self.parent.grid_columnconfigure(0,weight=1)
		self.parent.config(background="lavender")
		self.Current_label = tkinter.Label(self.parent, text = "Trenutne vrednosti")
		self.Current_label.grid(row = 1, column = 0, sticky = tkinter.W)
		self.New_label = tkinter.Label(self.parent, text = "Nove vrednosti")
		self.New_label.grid(row = 1, column = 1, sticky = tkinter.W)
		self.LBO_label = tkinter.Label(self.parent, text = "LBO: "+self.patient.LBO)
		self.LBO_label.grid(row = 2, column = 0, sticky = tkinter.W)
		self.name_label = tkinter.Label(self.parent, text = self.patient.name)
		self.name_entry = tkinter.Entry(self.parent)
		self.name_label.grid(row = 3, column = 0, sticky = tkinter.W)
		self.name_entry.grid(row = 3, column = 1)
		self.surname_label = tkinter.Label(self.parent, text = self.patient.surname)
		self.surname_entry = tkinter.Entry(self.parent)
		self.surname_label.grid(row = 4, column = 0, sticky = tkinter.W)
		self.surname_entry.grid(row = 4, column = 1)
		self.date_of_birth_label = tkinter.Label(self.parent, text = self.patient.date_of_birth)
		self.date_of_birth_entry = tkinter.Entry(self.parent)
		self.date_of_birth_label.grid(row = 5, column = 0, sticky = tkinter.W)
		self.date_of_birth_entry.grid(row = 5, column = 1)
		self.submit_button = tkinter.Button(self.parent, text = "Potvrdi", command = self.check)
		self.submit_button.grid(row = 0, column = 0, sticky = tkinter.W)
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		tmpName = self.name_entry.get()
		tmpSurname = self.surname_entry.get()
		tmpDate_of_birth = self.date_of_birth_entry.get()
		print(tmpName,tmpSurname,tmpDate_of_birth)
		if not tmpName:
			tmpName = self.patient.name
		if not tmpSurname:
			tmpSurname = self.patient.surname
		if not tmpDate_of_birth:
			tmpDate_of_birth = self.patient.date_of_birth
			####proveraaa
		patiente = Patient.xmlToList()
		del patiente[int(self.patient.LBO)]
		Patient.saveXML(patiente)
		newPatient = Patient(self.patient.LBO, tmpName, tmpSurname, tmpDate_of_birth)
		Patient.addNewPatient(newPatient)
		messagebox.showinfo("Uspeh", "Uspesno ste izmenili")
		self.goBack()



	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow)
