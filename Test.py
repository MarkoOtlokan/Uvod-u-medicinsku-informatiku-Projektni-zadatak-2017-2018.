import sys
sys.path.append('./MedicalExamination')
sys.path.append('./Patient.py')
from MedicalExamination import MedicalExamination
from Patient import Patient


def Test():
    sara = Patient(12345678912, 'Sara', 'Nikolic', 2000)
    greg = Patient(12312312312, 'sdfsara', 'Niddddc', 2001)
    patiente = {}
    patiente[sara.LBO] = sara
    patiente[greg.LBO] = greg
    Patient.saveXML(patiente)

    print("proslo")

    print()
    print("ucitavanje...")
    patiente = Patient.readXML()

    for patientElement in patiente:
        print (patientElement.name)
