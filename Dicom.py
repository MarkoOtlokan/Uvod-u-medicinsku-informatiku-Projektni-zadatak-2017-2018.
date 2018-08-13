from tkinter import ttk
from tkinter import messagebox
import tkinter
from Patient import Patient
from MedicalExamination import MedicalExamination
from AddNew import DodajPregled

class Dicom(tkinter.Frame):

	def __init__(self, parent, otac, path):
        self.parent = parent
        self.otac = otac
        self.path = path
