from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient
import calendar
import datetime
from Call import Calendar
import uuid
from tkinter import filedialog
from MedicalExamination import MedicalExamination
class DodajPregled(tkinter.Frame):

	def __init__(self, parent,otac, patientKey,first, second): #first i second sluze samo da bi se vratio na prosli nivo
		self.route = ""
		self.first = first
		self.second = second
		self.patientKey = patientKey
		self.otac = otac
		self.data = {}
		self.parent = parent
		self.id = str(uuid.uuid4().int & (1<<32)-1)
		self.frame = tkinter.Frame(self.parent)
		self.initialize_insert_interface()

	def initialize_insert_interface(self):
		self.parent.title("Canvas Test")
		self.parent.grid_rowconfigure(0,weight=1)
		self.parent.grid_columnconfigure(0,weight=1)
		self.parent.config(background="lavender")
		self.naslov_label = tkinter.Label(self.parent, text = "Dodaj novi pregled")
		self.naslov_label.grid(row = 0, column = 0, sticky = tkinter.W)
		self.id_label = tkinter.Label(self.parent, text = "id: "+self.id)
		self.id_label.grid(row = 2, column = 0, sticky = tkinter.W)

		self.date_of_birth_label = tkinter.Label(self.parent, text = "datum pregleda:")
		self.date_of_birth_entry = tkinter.Entry(self.parent)
		self.date_of_birth_label.grid(row = 4, column = 0, sticky = tkinter.W)
		self.date_of_birth_entry.grid(row = 4, column = 1)

		self.date_Button = ttk.Button(self.parent, text='Izaberi',command=self.calCal)
		self.date_Button.grid(row = 4, column = 2)

		self.option_label = tkinter.Label(self.parent, text = "vrsta pregleda:")
		self.option_label.grid(row = 5, column = 0, sticky = tkinter.W)
		self.var = tkinter.StringVar()
		self.var.set("CT") # initial value
		self.optionList = ['CT', 'MR','XA','RF', 'US','ECG']
		self.option = tkinter.OptionMenu(self.parent,self.var, *self.optionList)
		self.option.grid(row = 5, column = 1)
		self.report_label = tkinter.Label(self.parent, text = "report:")
		self.report_entry = tkinter.Entry(self.parent)
		self.report_label.grid(row = 6, column = 0, sticky = tkinter.W)
		self.report_entry.grid(row = 6, column = 1)
		self.doctor_label = tkinter.Label(self.parent, text = "doktor:")
		self.doctor_entry = tkinter.Entry(self.parent)
		self.doctor_label.grid(row = 7, column = 0, sticky = tkinter.W)
		self.doctor_entry.grid(row = 7, column = 1)
		self.dicom_label = tkinter.Label(self.parent, text = "snimak:")
		self.dicom_entry = tkinter.Entry(self.parent)
		self.dicom_label.grid(row = 8, column = 0, sticky = tkinter.W)
		self.dicom_entry.grid(row = 8, column = 1)
		self.odabirSnimka = tkinter.Button(self.parent,text = '...', width = 5, command = self.klikNaodabir_snimkaDugme)
		self.odabirSnimka.grid(row = 8, column = 2)
		self.submit_button = tkinter.Button(self.parent, text = "dodaj", command = self.check)
		self.submit_button.grid(row = 9, column = 0, sticky = tkinter.W)
		self.filename =  tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("*"),("all files","*.*")))
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		self.fillDate()
		#treba ubaciti proveru da li su svi dole navedeni ispravno
		tmpMed = MedicalExamination(self.id,self.patientKey,self.date_of_birth_entry.get(),  self.var.get(), self.report_entry.get(), self.doctor_entry.get(),self.dicom_entry.get() )
		#add new]
		MedicalExamination.addNewMed(tmpMed)
		messagebox.showinfo("Uspeh", "Uspesno ste uneli pacijenta")
		self.goBack()

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow,self.first, self.second)

	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child, self.data)

	def klikNaodabir_snimkaDugme(self):

		stazaDoDatoteke = filedialog.askopenfilename(
		initialdir = "./DICOM samples",
		title = "Otvaranje",
		filetypes = (("DICOM files", "*.dcm"),))

		try:
			s = stazaDoDatoteke.split('/')

			s1 = s[-1]
			s2 = s[-2]

			s= '/'.join(['.',s2,s1])
			stazaDoDatoteke = s
		except:
			return
		self.route = stazaDoDatoteke
		self.dicom_entry.insert(tkinter.END,self.route)

	def fillDate(self):
		self.date_of_birth_entry.insert(0, str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))
