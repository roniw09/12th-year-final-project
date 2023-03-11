class Appraiser:

    def __init__(self, username, name, work_days):
        self.username = username
        self.name = name
        self.work_days = work_days

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

    def __init__(self, index, fname, lname, sekerId, phone, address, exeTime, appraiserId):
        self.index = index
        self.fname = fname
        self.lname = lname
        self.sekerId = sekerId
        self.phone = phone
        self.address = address
        self.exeTime = exeTime
        self.appraiserId = appraiserId
    
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