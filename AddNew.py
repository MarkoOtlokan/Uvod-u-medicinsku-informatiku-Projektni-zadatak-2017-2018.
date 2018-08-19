import calendar
import datetime
from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient
import uuid
from tkinter import filedialog
from MedicalExamination import MedicalExamination


class AddNew(tkinter.Frame):

	def __init__(self, parent, otac, patienteKeys):

		self.patienteKeys = patienteKeys
		self.otac = otac
		self.parent=parent
		self.data = {}
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

		self.date_of_birth_label.grid(row = 4, column = 0, sticky = tkinter.W)

		self.date_Button = ttk.Button(self.parent, text='Izaberi',command=self.calCal)
		self.date_Button.grid(row = 4, column = 2)
		self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.check)
		self.submit_button.grid(row = 0, column = 0, sticky = tkinter.W)
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		self.fillDate()
		tmpLBO = self.LBO_entry.get()
		#print(len(tmpLBO))
		if(len(tmpLBO) != 11 or tmpLBO.isdigit() == False):
			messagebox.showinfo("Greska", "Lose unet LBO")
			return
		for key in self.patienteKeys:
			if key == self.LBO_entry.get():
				messagebox.showinfo("Greska", "Uneseni LBO vec postoji")
				return
		if len(self.name_entry.get()) < 3:
			messagebox.showinfo("Greska", "Neispravno uneto ime")
			return
		if len(self.surname_entry.get()) < 3:
			messagebox.showinfo("Greska", "Neispravno uneto prezime")
			return

		try:
		   self.date
		except :
		   messagebox.showinfo("Greska", "unesi datum")
		   return
		tmpPatient = Patient(int(tmpLBO), self.name_entry.get(), self.surname_entry.get(), str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))
		Patient.addNewPatient(tmpPatient)
		messagebox.showinfo("Uspeh", "Uspesno ste uneli pacijenta")
		self.goBack()

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow)

	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child,AddNew,self)
		print("prosao")

	def fillDate(self):
		if self.data == {}:
			return
		self.date = tkinter.Label(self.parent, text=str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))
		self.date.grid(row = 4, column = 1)

	def setDate(self,data):
		self.data = data
		self.fillDate()

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
		self.date_of_birth_label.grid(row = 4, column = 0,sticky = tkinter.W)


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
		self.odabirSnimka = tkinter.Button(self.parent,text = '...', width = 5, command = self.otvoriDicom)
		self.odabirSnimka.grid(row = 8, column = 2)
		self.goDic_button = tkinter.Button(self.parent, text = "otvori", command = self.otvori, state=tkinter.DISABLED)
		self.goDic_button.grid(row = 8, column = 3, sticky = tkinter.W)
		self.submit_button = tkinter.Button(self.parent, text = "dodaj", command = self.check)
		self.submit_button.grid(row = 9, column = 0, sticky = tkinter.W)
		self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
		self.exit_button.grid(row = 0, column = 3)

	def check(self):
		self.fillDate()
		#print(len(tmpLBO))
		if len(self.report_entry.get()) < 3:
			messagebox.showinfo("Greska", "Neispravno uneto izvestaj")
			return
		if len(self.doctor_entry.get()) < 3:
			messagebox.showinfo("Greska", "Neispravno unet doktor")
			return
	#	if len(self.dicom_entry.get()) < 3:
	#		messagebox.showinfo("Greska", "Niste uneli dciom datoteku")
	#		return

		try:
		   self.date
		except :
		   messagebox.showinfo("Greska", "unesi datum")
		   return
		#treba ubaciti proveru da li su svi dole navedeni ispravno
		tmpMed = MedicalExamination(self.id,self.patientKey,self.date.cget("text"),  self.var.get(), self.report_entry.get(), self.doctor_entry.get(),self.dicom_entry.get() )
		#add new]
		MedicalExamination.addNewMed(tmpMed)
		messagebox.showinfo("Uspeh", "Uspesno ste uneli pregled")
		self.goBack()

	def goBack(self):
		self.parent.withdraw()
		self.newWindow = tkinter.Toplevel(self.parent)
		bb = self.otac(self.newWindow,self.first, self.second)

	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child, self.data)

	def otvori(self):
		child = tkinter.Toplevel()
		dic = Dicom(child,self.otac,self.dicom_entry.get())

	def otvoriDicom(self):

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
		self.goDic_button.configure(state=tkinter.NORMAL)

	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child,DodajPregled,self)

	def fillDate(self):
		if self.data == {}:
			return
		self.date = tkinter.Label(self.parent, text=str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))
		self.date.grid(row = 4, column = 1)

	def setDate(self,data):
		self.data = data
		self.fillDate()



class Calendar:
	def __init__(self, parent,otac,selfP):
		self.values = {}
		self.selfP = selfP
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.otac = otac
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''

		self.setup(self.year, self.month)

	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			#w.destroy()
			self.wid.remove(w)

	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		#self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)

	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1

	#self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)

	def selection(self, day, name):
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = name

	#data
		if day > 9:
			self.values['day_selected'] = day
		else:
			self.values['day_selected'] = "0"+str(day)
		if self.month > 9:
			self.values['month_selected'] =  self.month
		else:
			self.values['month_selected'] = "0"+str(self.month)

		self.values['year_selected'] = self.year
		self.values['day_name'] = name
		self.values['month_name'] = calendar.month_name[self.month_selected]

		self.clear()
		self.setup(self.year, self.month)

	def setup(self, y, m):
		left = tkinter.Button(self.parent, text='<', command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1)

		header = tkinter.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)

		right = tkinter.Button(self.parent, text='>', command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5)

		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = tkinter.Label(self.parent, text=name[:3])
			self.wid.append(t)
			t.grid(row=1, column=num)

		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					#print(calendar.day_name[day])
					b = tkinter.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d)

		sel = tkinter.Label(self.parent, height=2, text='{} {} {} {}'.format(self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel.grid(row=8, column=0, columnspan=7)

		ok = tkinter.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
		self.wid.append(ok)
		ok.grid(row=9, column=2, columnspan=3, pady=10)

	def kill_and_save(self):
		self.otac.setDate(self.selfP,self.values)
		self.parent.destroy()



class Dicom(tkinter.Frame):

	def __init__(self, parent, otac, path):
		self.parent = parent
		self.otac = otac
		self.path = path
		self.initialize_insert_interface()

	def initialize_insert_interface(self):
		self.name = tkinter.IntVar()
		self.name.set(1)
		self.lbo = tkinter.IntVar()
		self.lbo.set(1)
		self.d = tkinter.IntVar() #date
		self.d.set(1)

		self.frame0 = tkinter.Frame(self.parent)
		self.frame0.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10, padx = 10)

		self.path_label = tkinter.Label(self.frame0, text=self.path)
		self.path_label.pack(side=tkinter.LEFT, padx=10)
		self.submit_button = tkinter.Button(self.frame0, text = "potvrdi", command = self.check)
		self.submit_button.pack(side = tkinter.LEFT,pady = 10,padx = 10)
		self.exit_button = tkinter.Button(self.frame0, text = "Exit", command = self.goBack)
		self.exit_button.pack(side = tkinter.LEFT, padx = 10)


		self.frame = tkinter.Frame(self.parent,bd=2, relief=tkinter.SUNKEN)
		self.frame.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10, padx = 10)

		self.frame1 = tkinter.Frame(self.frame)
		self.frame1.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.lbo_Label = tkinter.Label(self.frame1, text = "LBO: ").pack(side = tkinter.LEFT)
		self.lbo_entry = tkinter.Entry(self.frame1).pack(side = tkinter.LEFT)
		self.izostaviLbo = tkinter.Radiobutton(self.frame1, text = "izostavi", variable = self.lbo, value=1).pack(side = tkinter.LEFT)
		self.rucnoLbo = tkinter.Radiobutton(self.frame1, text="rucno", padx = 10, variable = self.lbo, value=2).pack(side = tkinter.LEFT)
		self.izsistemaLbo = tkinter.Radiobutton(self.frame1, text="iz sistema", padx = 10, variable = self.lbo, value=3).pack(side = tkinter.LEFT)

		self.frame2 = tkinter.Frame(self.frame)
		self.frame2.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.name_Label = tkinter.Label(self.frame2, text = "IME: ").pack(side = tkinter.LEFT)
		self.name_entry = tkinter.Entry(self.frame2).pack(side = tkinter.LEFT)
		self.izostaviIme = tkinter.Radiobutton(self.frame2, text = "izostavi", variable = self.name, value=1).pack(side = tkinter.LEFT)
		self.rucnoIme = tkinter.Radiobutton(self.frame2, text="rucno", padx = 10, variable = self.name, value=2).pack(side = tkinter.LEFT)
		self.izsistemaIme = tkinter.Radiobutton(self.frame2, text="iz sistema", padx = 10, variable = self.name, value=3).pack(side = tkinter.LEFT)

		self.frame3 = tkinter.Frame(self.frame)
		self.frame3.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.dateEntry = tkinter.StringVar()
		self.dateEntry.set("")
		self.date_Label = tkinter.Label(self.frame3, text = "datum rodjenja : ").pack(side = tkinter.LEFT)
		self.date_entry = tkinter.Entry(self.frame3,textvariable = self.dateEntry).pack(side = tkinter.LEFT)
		self.date_Button = ttk.Button(self.frame3, text='Izaberi',command=self.calCal).pack(side = tkinter.LEFT)
		self.izostaviDatum = tkinter.Radiobutton(self.frame3, text = "izostavi", variable = self.d, value=1).pack(side = tkinter.LEFT)
		self.rucnoDatum = tkinter.Radiobutton(self.frame3, text="rucno", padx = 10, variable = self.d, value=2).pack(side = tkinter.LEFT)
		self.izsistemaDatum = tkinter.Radiobutton(self.frame3, text="iz sistema", padx = 10, variable = self.d, value=3).pack(side = tkinter.LEFT)



#########
		self.framesec = tkinter.Frame(self.parent,bd=2, relief=tkinter.SUNKEN)
		self.framesec.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10, padx = 10)
		self.report = tkinter.IntVar()
		self.report.set(1)
		self.id = tkinter.IntVar()
		self.id.set(1)
		self.dt = tkinter.IntVar() #date
		self.dt.set(1)
		self.opt = tkinter.IntVar()
		self.opt.set(1)
		self.doc = tkinter.IntVar()
		self.doc.set(1)

		self.framesec1 = tkinter.Frame(self.framesec)
		self.framesec1.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.id_Label = tkinter.Label(self.framesec1, text = "id: ").pack(side = tkinter.LEFT)
		self.id_entry = tkinter.Entry(self.framesec1).pack(side = tkinter.LEFT)
		self.izostaviid = tkinter.Radiobutton(self.framesec1, text = "izostavi", variable = self.id, value=1).pack(side = tkinter.LEFT)
		self.rucnoid = tkinter.Radiobutton(self.framesec1, text="rucno", padx = 10, variable = self.id, value=2).pack(side = tkinter.LEFT)
		self.izsistemaid = tkinter.Radiobutton(self.framesec1, text="iz sistema", padx = 10, variable = self.id, value=3).pack(side = tkinter.LEFT)


		self.framesec3 = tkinter.Frame(self.framesec)
		self.framesec3.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.date2Entry = tkinter.StringVar()
		self.date2Entry.set("")
		self.date2_Label = tkinter.Label(self.framesec3, text = "datum : ").pack(side = tkinter.LEFT)
		self.date2_entry = tkinter.Entry(self.framesec3,textvariable = self.date2Entry).pack(side = tkinter.LEFT)
		self.date2_Button = ttk.Button(self.framesec3, text='Izaberi',command=self.calCal).pack(side = tkinter.LEFT)
		self.izostaviDatum = tkinter.Radiobutton(self.framesec3, text = "izostavi", variable = self.dt, value=1).pack(side = tkinter.LEFT)
		self.rucnoDatum = tkinter.Radiobutton(self.framesec3, text="rucno", padx = 10, variable = self.dt, value=2).pack(side = tkinter.LEFT)
		self.izsistemaDatum = tkinter.Radiobutton(self.framesec3, text="iz sistema", padx = 10, variable = self.dt, value=3).pack(side = tkinter.LEFT)

		self.framesec5 = tkinter.Frame(self.framesec)
		self.framesec5.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.option_label = tkinter.Label(self.framesec5, text = "vrsta pregleda:").pack(side = tkinter.LEFT)
		self.var = tkinter.StringVar()
		self.var.set("CT") # initial value
		self.optionList = ['CT', 'MR','XA','RF', 'US','ECG']
		self.option = tkinter.OptionMenu(self.framesec5,self.var, *self.optionList)
		self.option.pack(side = tkinter.LEFT)
		self.izostaviO = tkinter.Radiobutton(self.framesec5, text = "izostavi", variable = self.opt, value=1).pack(side = tkinter.LEFT)
		self.rucnoO = tkinter.Radiobutton(self.framesec5, text="rucno", padx = 10, variable = self.opt, value=2).pack(side = tkinter.LEFT)
		self.izsistemaO = tkinter.Radiobutton(self.framesec5, text="iz sistema", padx = 10, variable = self.opt, value=3).pack(side = tkinter.LEFT)

		self.framesec2 = tkinter.Frame(self.framesec)
		self.framesec2.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.report_Label = tkinter.Label(self.framesec2, text = "Izvestaj: ").pack(side = tkinter.LEFT)
		self.report_entry = tkinter.Entry(self.framesec2).pack(side = tkinter.LEFT)
		self.izostaviReport = tkinter.Radiobutton(self.framesec2, text = "izostavi", variable = self.report, value=1).pack(side = tkinter.LEFT)
		self.rucnoReport = tkinter.Radiobutton(self.framesec2, text="rucno", padx = 10, variable = self.report, value=2).pack(side = tkinter.LEFT)
		self.izsistemaReport = tkinter.Radiobutton(self.framesec2, text="iz sistema", padx = 10, variable = self.report, value=3).pack(side = tkinter.LEFT)

		self.framesec4 = tkinter.Frame(self.framesec)
		self.framesec4.pack(side = tkinter.TOP, fill = tkinter.X, pady = 10)

		self.doctor_Label = tkinter.Label(self.framesec4, text = "Doktor: ").pack(side = tkinter.LEFT)
		self.doctor_entry = tkinter.Entry(self.framesec4).pack(side = tkinter.LEFT)
		self.izostaviDoctor = tkinter.Radiobutton(self.framesec4, text = "izostavi", variable = self.doc, value=1).pack(side = tkinter.LEFT)
		self.rucnoDoctor = tkinter.Radiobutton(self.framesec4, text="rucno", padx = 10, variable = self.doc, value=2).pack(side = tkinter.LEFT)
		self.izsistemaDoctor = tkinter.Radiobutton(self.framesec4, text="iz sistema", padx = 10, variable = self.doc, value=3).pack(side = tkinter.LEFT)

		self.klikNaOtvoriDugme()

	def fillDate(self):

		if self.data == {}:
			return
		self.dateEntry.set(str(self.data['year_selected'])+"-"+str(self.data['month_selected'])+"-"+str(self.data['day_selected']))

	def setDate(self,data):
		self.data = data
		self.fillDate()

	def ch(self):
		self.goDic_button.configure(state=tkinter.NORMAL)


	def calCal(self):
		child = tkinter.Toplevel()
		cal = Calendar(child,Dicom,self)

	def goBack(self):
		###
		self.parent.destroy()

	def check(self):
		pass

	def klikNaOtvoriDugme(self):
	    try:
	    # otvaranje dijalog prozora za odabir datoteke
	        self.__dataset = pydicom.read_file(self.path, force = True) # otvaranje DICOM datoteke; force parametar obezbeđuje čitanje nepotpunih datoteka
	        print(self.__dataset)

	        self.title(self.path)

	        # podaci DICOM datoteke ne moraju da postoje
	        if "PatientName" in self.__dataset: # da li podatak postoji u dataset-u?
	            self.__pacijent.set(self.__dataset.PatientName) # vrednost podatka
	            self.__pacijentPrisutan.set(True) # podatak pronađen?
	        else:
	            self.__pacijentPrisutan.set(False)

	        if "PatientSex" in self.__dataset:
	            for vrednost, tekst in [("M", "muški"), ("F", "ženski"), ("O", "drugi")]: # 3 moguće vrednosti: M, F, O
	                if vrednost == self.__dataset.PatientSex:
	                    self.__pol.set(tekst)
	                    break
	            self.__polPrisutan.set(True)
	        else:
	            self.__polPrisutan.set(False)

	        if "PatientAge" in self.__dataset:
	            try:
	                self.__starost.set(int(self.__dataset.PatientAge[:-1])) # sve do poslednjeg karaktera je vrednost
	                self.__starostJedinica.set(self.__dataset.PatientAge[-1]) # poslednji karakter je jedinica mere; Y, M, W, D
	                self.__starostPrisutna.set(True)
	            except ValueError: # možda podatak postoji, ali ne može da se parsira u int
	                pass
	        else:
	            self.__starostPrisutna.set(False)

	        self.azurirajStanja() # omogućavanje polja za izmenu na osnovu pročitanih podataka
	        print("ziv-1")
	        pilSlika = pydicom_PIL.get_PIL_image(self.__dataset) # pokušaj dekompresije i čitanja slike iz dataset objekta
	        print("ziv0")
	        sirina = pilSlika.width
	        visina = pilSlika.height
	        print("originalne dimenzije:", sirina, ",", visina)

	        maksDimenzija = 900
	        if sirina > maksDimenzija or visina > maksDimenzija:
	            if sirina > visina: # smanjiti sliku po većoj od 2 dimenzije
	                odnos = maksDimenzija/sirina
	                sirina = maksDimenzija
	                visina = int(odnos*visina) # manja dimenzija se smanjuje proporcionalno
	            else:
	                odnos = maksDimenzija/visina
	                sirina = int(odnos*sirina) # manja dimenzija se smanjuje proporcionalno
	                visina = maksDimenzija
	        print("ziv1")
	        print("nove dimenzije:", sirina, ",", visina)
	        pilSlika = pilSlika.resize((sirina, visina), Image.LANCZOS) # LANCZOS metoda je najbolja za smanjivanje slike
	        slika = ImageTk.PhotoImage(pilSlika) # PIL slika se mora prevesti u TkInter sliku (ImageTk)
	        self.__slikaLabela["image"] = slika
	        self.__slikaLabela.image = slika
	    except:
	        # PIL slika se mora prevesti u TkInter sliku (ImageTk)
	        #slika = ImageTk.PhotoImage(Image.new('L', (200, 200))) # crna slika dimenzija 200x200 piksela
	        slika = ImageTk.PhotoImage(Image.open("DICOM-Logo.jpg")) # bilo koja druga podrazumevana slika
	        self.__slikaLabela["image"] = slika  # labeli se dodeljuje slika
	        self.__slikaLabela.image = slika  # referenca na TkInter sliku se mora sačuvati, inače nece biti prikazana!
	        print("nesto2")
	    self["cursor"] = "" # reset-ovanje pokazivača miša na podrazumevani
	    print("nista")
