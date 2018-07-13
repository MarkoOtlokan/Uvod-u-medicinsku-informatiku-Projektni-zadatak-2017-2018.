import sys
sys.path.append('./MedicalExamination')
sys.path.append('./Patient.py')
from MedicalExamination import MedicalExamination
from Patient import Patient


def Test():
    med2 = MedicalExamination(12346,17162739481,"2015-04-29T04:16:49.792-04:00","pregled","ne uspesan","pocek")
    med =  MedicalExamination(12345,17162739481,"2013-04-29T04:16:49.792-04:00","pregled","uspesan","pocek")
    med3 = MedicalExamination(12349,17162722281,"2015-04-29T04:16:49.792-04:00","pregled","ne uspesan","pocek")

    meds = {}
    meds[med2.id] = med2
    meds[med3.id] = med3
    meds[med.id] = med
    MedicalExamination.saveXML(meds)
    natasa = Patient(17162739481,'s','ss','sd')

    medL = MedicalExamination.readXML()
    Patient.pronadjiPreglede(natasa)

if __name__ == '__main__':
    Test()
