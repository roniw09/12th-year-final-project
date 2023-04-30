class Appraiser:

    def __init__(self, id, name, skarim):
        self.id = id
        self.name = name
        self.skarim = skarim

    def GetID(self):
        return self.id
    
    def GetName(self):
        return self.name
    
    def GetSkarim(self):
        return self.skarim


class Address:
    def __init__(self, city, street, aptnum):
        self.city = city
        self.street = street
        self.aptnum = aptnum

    def GetCity(self):
        return self.city
    
    def GetStreet(self):
        return self.street
    
    def GetAptnum(self):
        return self.aptnum
    
    def SetCity(self, city):
        self.city = city
    
    def SetStreet(self, street):
        self.street = street
    
    def SetAptnum(self, aptnum):
        self.aptnum = aptnum
       
class Client:

    def __init__(self, id, fname, lname, sekerId, phone, address, exeTime, appraiserId):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.sekerId = sekerId
        self.phone = phone
        self.address = address
        self.exeTime = exeTime
        self.appraiserId = appraiserId
    
    def GetID(self):
        return self.id
    
    def GetFirstName(self):
        return self.fname

    def GetLastName(self):
        return self.lname
    
    def GetSekerId(self):
        return self.sekerId
    
    def GetExeTime(self):
        return self.exeTime

    def SetExeTime(self, exeTime):
        self.exeTime = exeTime

    def __str__(self):
        return f"""name: {self.fname} {self.lname}\n
                    index: {self.id}
                    Exetime: {self.exeTime}"""