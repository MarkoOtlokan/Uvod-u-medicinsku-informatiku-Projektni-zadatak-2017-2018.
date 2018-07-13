import sys
from tkinter import ttk
import tkinter
from AddNew import AddNew
from Change import Change
sys.path.append('../Patient.py')
from Patient import Patient

from tkinter import messagebox

class Main(tkinter.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        self.patiente = []
        self.patienteKeys=[]
        tkinter.Frame.__init__(self, parent)
        self.parent=parent

        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.patiente = Patient.readXML() # stoji ovde zbog update
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Canvas Test")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")


        # Define the different GUI widgets

        self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.showInsert)
        self.submit_button.grid(row = 1, column = 1, sticky = tkinter.W)
        self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 0, column = 1)

        # Set the treeview
        self.tree = ttk.Treeview(self.parent, columns=('surname', 'name','LBO'))
        self.tree.heading('surname', text='Prezime')
        self.tree.heading('name', text='Ime')
        self.tree.heading('LBO', text='LBO')
        self.tree.column('surname')
        self.tree.column('name')
        self.tree.column('LBO')
        self.tree.grid(row=3, column=0, sticky='nsew')
        self.tree['show'] = 'headings'

        # Initialize the counter

        self.insert_data()



    def showInsert(self):
        self.parent.withdraw()
        self.newWindow = tkinter.Toplevel(self.parent)
        bb = AddNew(self.newWindow, Main, self.patienteKeys)

    def showChange(self,patient):
        self.parent.withdraw()
        self.newWindow = tkinter.Toplevel(self.parent)
        bb = Change(self.newWindow, Main, patient)

    def insert_data(self):
        """
        Insertion method.
        """
        for patientElement in self.patiente:
            self.patienteKeys.append(patientElement.LBO)
            self.tree.insert('', '0', values=(patientElement.surname,patientElement.name,patientElement.LBO))
        self.tree.bind('<<TreeviewSelect>>', self.OnClick)

    def OnClick(self, event):
        item = self.tree.selection()[0]
        tmp = self.tree.item(item)
        list = tmp.get('values')
        tmpLBO = list[2]
        for patient in self.patiente:
            if str(tmpLBO) == str(patient.LBO): ##################### jedan je string jedan nije treba proveriti !!!!!!!!!!!!!!!!!!!!!!!
                self.writeDataOfPatient(patient)
                return

    def writeDataOfPatient(self,patient):
        self.dose_label = tkinter.Label(self.parent, text = "Prezime:" + patient.surname)
        self.dose_label.grid(row = 1, column = 2, sticky = tkinter.W)
        self.dose_label = tkinter.Label(self.parent, text = "ime:" + patient.name)
        self.dose_label.grid(row = 2, column = 2, sticky = tkinter.W)
        self.dose_label = tkinter.Label(self.parent, text = "LBO:" + patient.LBO)
        self.dose_label.grid(row = 3, column = 2, sticky = tkinter.W)
        self.dose_label = tkinter.Label(self.parent, text = "Datum rodjenja:" + str(patient.date_of_birth))
        self.dose_label.grid(row = 4, column = 2, sticky = tkinter.W)
        self.submit_button = tkinter.Button(self.parent, text = "pregledi", command = lambda: self.goToPregledi(patient.LBO))
        self.submit_button.grid(row = 5, column = 2, sticky = tkinter.W)
        self.submit_button = tkinter.Button(self.parent, text = "Obrisi pacijeta", command = lambda: self.dd(patient.LBO))
        self.submit_button.grid(row = 5, column = 2, sticky = tkinter.W)
        self.submit_button = tkinter.Button(self.parent, text = "izmeni", command = lambda: self.showChange(patient))
        self.submit_button.grid(row = 5, column = 3, sticky = tkinter.W)


    def goToPregledi(self,LBO):
        print(LBO)

    def dd(self,lbo):
        self.win = tkinter.Toplevel()
        self.win.title('warning')
        message = "Da li ste sigurni da zelite da obrisete pacijenta ?"
        tkinter.Label(self.win, text=message).pack()
        tkinter.Button(self.win, text='obrisi', command=lambda:self.deletePatient(lbo)).pack()
        tkinter.Button(self.win, text='odustani', command=self.win.destroy).pack()

    def deletePatient(self, LBO):
        self.win.destroy()
        patiente = Patient.xmlToList()
        i = 0
        print(patiente)
        del patiente[int(LBO)]
        Patient.saveXML(patiente)

        messagebox.showinfo("Uspeh", "Uspesno ste obrisali pacijenta")
        self.parent.update()

def main():
    root=tkinter.Tk()
    d=Main(root)
    root.mainloop()

if __name__=="__main__":
    main()
