from lxml import etree
import sys
sys.path.append('./MedicalExamination')
from MedicalExamination import MedicalExamination

class Patient(object):
    """docstring for Patient."""

    __nameSD = "patient.xsd"
    __nameXML = "Patient.xml"


    @property
    def LBO(self):
        return self.__LBO

    @LBO.setter
    def LBO(self, LBO):
        self.__LBO = LBO

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def medical_examination(self):
        return self.__medical_examination

    @medical_examination.setter
    def medical_examination(self):
        self.__medical_examination = []


    def __init__(self, LBO, name, surname, date_of_birth):
        self.__LBO = LBO
        self.__name = name
        self.__surname = surname
        self.__date_of_birth = date_of_birth

    def __str__(self):
        return "\n".join([
            "{:>12}: {}".format("LBO", self.__LBO),
            "{:>12}: {}".format("name", self.__name),
            "{:>12}: {}".format("surname", self.__surname),
            "{:>12}: {}".format("date of birth", self.__date_of_birth)])

    def writeAllExamination(self):
        for i in self.__medical_examination:
            print(i)


    def __eq__(self, other):
        return self.__LBO == other.__LBO

    def makeEL(self):
        element = etree.Element("patient") # novi Element objekat
        element.append(etree.Element("name")) # dodavanje iza poslednjeg podelementa Element objekta
        element.append(etree.Element("surname"))
        element.append(etree.Element("date_of_birth"))
        #element.insert(1, etree.Element("prezime")) # umetanje podelementa Element objekta

        element.attrib["LBO"] = str(self.__LBO)
        #element.set("jmbg", self.__jmbg) # metoda za jednostavnije postavljanje vrednosti atributa
        element[0].text = self.__name
        #element.xpath("./ime")[0].text = self.__ime
        element[1].text = self.__surname
        element[2].text = str(self.__date_of_birth)
        return element

    @classmethod
    def saveXML(_class, patiente):
        namespaces = {"xsi" : "http://www.w3.org/2001/XMLSchema-instance"}
        # nazivi elemenata/atributa sa namespace prefiksom se moraju navesti u formatu: {staza}naziv
        # naziv ogovara nazivu elementa/atributa
        # Element automatski zamenjuje stazu odgovarajućim namespace prefiksom navedenim u rečniku namespace-ova
        attributes = {"{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": _class.__nameSD}

        # Element se moze inicijalizovati nazivom i opciono rečnikom atributa i/ili rečnikom namespace-ova
        patienteEL = etree.Element("patiente", attributes, namespaces)

        for LBO in patiente.keys():
            patient = patiente[LBO]
            patientEL = _class.makeEL(patient)
            patienteEL.append(patientEL)

        xmlDoc = etree.ElementTree(patienteEL) # novi ElementTree objekat sa zadatim korenom

        schemaDoc = etree.parse(_class.__nameSD)
        schema = etree.XMLSchema(schemaDoc)
        if not schema.validate(xmlDoc):
            print(schema.error_log)
            return

        datoteka = open(_class.__nameXML, "wb") # datoteka za čuvanje se otvara u wb (write-binary) režimu. Ukoliko ne postoji, biće kreirana
        # write metoda ElementTree objekta zapisuje XML dokument u otvorenu datoteku
        # encoding parametar govori u kom će encoding formatu biti zapisana datoteka
        # xml_declaration parametar govori da li je potrebno zapisati i XML deklaraciju u datoteku
        # pretty_print parametar govori da li je dokument potrebno čuvati tako da ga čovek može pročitati
        xmlDoc.write(datoteka, encoding = "UTF-8", xml_declaration = True, pretty_print = True)
        datoteka.close()

    @classmethod
    def readXML(_class):
        try:
            xmlDoc = etree.parse(_class.__nameXML) # učitavanje XML dokumenta u ELTree objekat

            schemaDoc = etree.parse(_class.__nameSD) # učitavanje XMLSchema dokumenta u ELTree objekat
            schema = etree.XMLSchema(schemaDoc) # pretvaranje ELTree objekta u XMLSchema objekat
            if not schema.validate(xmlDoc): # validacija xml dokumenta naspram šeme
                print(schema.error_log) # prikaz svih grešaka nastalih pri poslednjoj validaciji
                return {}

            patienteEL = xmlDoc.getroot() # pristup korenskom elementu ElementTree objekta
            #osobeElement = xmlDoc.xpath("/osobe")[0]


            patiente= []
            for patientEL in patienteEL: # Element je proširenje liste, pa može da se iterira kroz njegove podelemente
                patient = _class.elToClass(patientEL)
                patiente.append(patient)

            return patiente
        except OSError:
            return {}

    @classmethod
    def elToClass(_class, element):
        LBO = element.attrib["LBO"] # attrib svojstvo obejkta tipa Element je rečnik koji sadrži sve atribute XML elementa
        #jmbg = element.xpath("./@jmbg")[0]
        # Element objekat je proširenje liste, pa njegovi podelementi mogu da se indeksiraju
        name = element[0].text # text svojstvo objekta tipa Element je string koji odgovara sadržaju XML elementa
        #ime = element.xpath("./ime")[0].text
        surname = element[1].text
        date_of_birth = element[2].text

        patient = _class(LBO, name, surname, date_of_birth)
        return patient


    def element_class(element):
        tmp = Patient(element.LBO,element.name,element.surname, element.date_of_birth)
        return (tmp)

    def xmlToList():
        patiente = Patient.readXML()

        print("prosao")
        listOfPatiente = {}
        for patient in patiente:
            tmp = Patient.element_class(patient)
            listOfPatiente[int(tmp.LBO)] = tmp

        return listOfPatiente


    def addNewPatient(patient):
        patiente = Patient.xmlToList()
        patiente[patient.LBO] = patient
        for p in patiente:
            print(p)
            print()
        Patient.saveXML(patiente)
        return ("suc")

    def changeName(patient):
        pass

    def pronadjiPreglede(patient):
        pregledi = MedicalExamination.readXML()
        for p in pregledi:
            if int(p.patient_LBO) == patient.LBO:
                print(p)
            else:
                print("nee")
                print(p.patient_LBO)
                print("ddd")
                print(patient.LBO)
                print("sss")
