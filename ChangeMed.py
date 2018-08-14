from tkinter import ttk
from tkinter import messagebox
import tkinter
from MedicalExamination import MedicalExamination

class ChangeMed(tkinter.Frame):

    def __init__(self, parent, otac, med, pat,ot):
        self.ot = ot
        self.med = med
        self.pat = pat
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

        self.name_label = tkinter.Label(self.parent, text = self.med.date)
        self.name_entry = tkinter.Entry(self.parent)
        self.name_label.grid(row = 2, column = 0, sticky = tkinter.W)
        self.name_entry.grid(row = 2, column = 1)

        self.option_label = tkinter.Label(self.parent, text = self.med.type)
        self.var = tkinter.StringVar()
        self.var.set("CT") # initial value
        self.optionList = ['CT', 'MR','XA','RF', 'US','ECG']
        self.option = tkinter.OptionMenu(self.parent,self.var, *self.optionList)
        self.option.grid(row = 3, column = 1)
        self.option_label.grid(row = 3, column = 0, sticky = tkinter.W)


        self.report_label = tkinter.Label(self.parent, text = self.med.report)
        self.report_entry = tkinter.Entry(self.parent)
        self.report_label.grid(row = 4, column = 0, sticky = tkinter.W)
        self.report_entry.grid(row = 4, column = 1)

        self.doctor_label = tkinter.Label(self.parent, text = self.med.doctor)
        self.doctor_entry = tkinter.Entry(self.parent)
        self.doctor_label.grid(row = 5, column = 0, sticky = tkinter.W)
        self.doctor_entry.grid(row = 5, column = 1)

        self.dicom_label = tkinter.Label(self.parent, text = self.med.dicom)
        self.dicom_label.grid(row = 6, column = 0, sticky = tkinter.W)

        self.dicom_entry = tkinter.Entry(self.parent)
        self.dicom_entry.grid(row = 6, column = 1)
        self.odabirSnimka = tkinter.Button(self.parent,text = '...', width = 5, command = self.klikNaodabir_snimkaDugme)
        self.odabirSnimka.grid(row = 6, column = 2)


        self.submit_button = tkinter.Button(self.parent, text = "Potvrdi", command = self.check)
        self.submit_button.grid(row = 0, column = 0, sticky = tkinter.W)
        self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.goBack)
        self.exit_button.grid(row = 0, column = 3)

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

        patiente = Patient.xmlToList()
        del patiente[int(self.patient.LBO)]
        Patient.saveXML(patiente)
        newPatient = Patient(self.patient.LBO, tmpName, tmpSurname, tmpDate_of_birth)
        Patient.addNewPatient(newPatient)
        messagebox.showinfo("Uspeh", "Uspesno ste izmenili")
        self.goBack()

    def findPatient(self):
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
        messagebox.showinfo("Uspeh", "Uspesno ste izmenili")
        self.goBack()

    def goBack(self):
        self.parent.withdraw()
        self.newWindow = tkinter.Toplevel(self.parent)
        bb = self.otac(self.newWindow, self.ot,self.pat)
