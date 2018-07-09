import sys
from tkinter import ttk
import tkinter
from AddNew import AddNew
sys.path.append('../Patient.py')
from Patient import Patient

class Main(tkinter.Frame):
    patiente = Patient.readXML()
    '''
    classdocs
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent

        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Canvas Test")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")


        # Define the different GUI widgets
        self.dose_label = tkinter.Label(self.parent, text = "Dose:")
        self.dose_entry = tkinter.Entry(self.parent)
        self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        self.dose_entry.grid(row = 0, column = 1)

        self.modified_label = tkinter.Label(self.parent, text = "Date Modified:")
        self.modified_entry = tkinter.Entry(self.parent)
        self.modified_label.grid(row = 1, column = 0, sticky = tkinter.W)
        self.modified_entry.grid(row = 1, column = 1)

        self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.showInsert)
        self.submit_button.grid(row = 2, column = 1, sticky = tkinter.W)
        self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 0, column = 3)

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
        bb = AddNew(self.newWindow, Main)


    def insert_data(self):
        """
        Insertion method.
        """
        for patientElement in self.patiente:

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

        print(patient.surname)



def main():
    root=tkinter.Tk()
    d=Main(root)
    root.mainloop()

if __name__=="__main__":
    main()