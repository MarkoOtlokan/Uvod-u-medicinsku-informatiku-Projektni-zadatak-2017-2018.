from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient
from MedicalExamination import MedicalExamination
from DodajPregled import DodajPregled

class Pregledi(tkinter.Frame):

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
		self.LBO_label = tkinter.Label(self.parent, text = self.patient.name)

		self.LBO_label.grid(row = 1, column = 0, sticky = tkinter.W)

		self.name_label = tkinter.Label(self.parent, text = self.patient.surname)

		self.name_label.grid(row = 2, column = 0, sticky = tkinter.W)

		self.surname_label = tkinter.Label(self.parent, text = self.patient.LBO)

		self.surname_label.grid(row = 3, column = 0, sticky = tkinter.W)

		self.exit_button = tkinter.Button(self.parent, text = "dodaj pregled", command = self.addExamination)
		self.exit_button.grid(row = 0, column = 2)

		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

		self.tree = ttk.Treeview(self.parent, columns=('date', 'type','id'))
		self.tree.heading('date', text='Datum')
		self.tree.heading('type', text='tip')
		self.tree.heading('id', text='id')
		self.tree.column('date')
		self.tree.column('type')
		self.tree.column('id')
		self.tree.grid(row=3, column=0, sticky='nsew')

		self.tree['show'] = 'headings'

		self.writeMedicalExamination(self.patient.LBO)

	def addExamination(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = DodajPregled(self.newWindow, Pregledi,self.patient.LBO,self.otac,self.patient)

	def writeMedicalExamination(self,LBO):
		self.medL = MedicalExamination.readXML()
		for med in self.medL:

			if(med.patient_LBO == self.patient.LBO):
				self.tree.insert('', '0', values=(med.date,med.type,med.id))
				self.tree.bind('<<TreeviewSelect>>', self.OnClick)

	def OnClick(self):
		print("hej")

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow)
