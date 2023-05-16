class Appraiser:

    def __init__(self, id, name, skarim):
        """
            Constructor that takes parameters id, name, and skarim and initializes the Appraiser object
        """
        self.id = id
        self.name = name
        self.skarim = skarim

    def GetID(self):
        """
            Returns the ID of the appraiser
        """
        return self.id
    
    def GetName(self):
        """
            Returns the name of the appraiser
        """
        return self.name
    
    def GetSkarim(self):
        """
            Returns the surveys of the appraiser

        """
        return self.skarim


class Address:
    def __init__(self, city, street, aptnum):
        """
            Constructor that takes parameters city, street, and aptnum and initializes the Address object
        """
        self.city = city
        self.street = street
        self.aptnum = aptnum

    def GetCity(self):
        """
            Returns the city name
        """
        return self.city
    
    def GetStreet(self):
        """
            Returns the street name
        """
        return self.street
    
    def GetAptnum(self):
        """
            Returns the apartment number
        """
        return self.aptnum
    
    def SetCity(self, city):
        """
            Sets the city name
        """
        self.city = city
    
    def SetStreet(self, street):
        """
            Sets the street name
        """
        self.street = street
    
    def SetAptnum(self, aptnum):
        """
            Sets the apartment number
        """
        self.aptnum = aptnum
       
class Client:

    def __init__(self, id, fname, lname, sekerId, phone, address, exeTime, appraiserId):
        """
            Constructor that takes parameters id, fname, lname, sekerId, phone, address, exeTime, and 
            appraiserId and initializes the Client object
        """
        self.id = id
        self.fname = fname
        self.lname = lname
        self.sekerId = sekerId
        self.phone = phone
        self.address = address
        self.exeTime = exeTime
        self.appraiserId = appraiserId
    
    def GetID(self):
        """
            Returns the ID of the client
        """
        return self.id
    
    def GetFirstName(self):
        """
            Returns the first name of the client
        """
        return self.fname

    def GetLastName(self):
        """
            Returns the last name of the client
        """
        return self.lname
    
    def GetSekerId(self):
        """
            Returns the seker ID of the client
        """
        return self.sekerId
    
    def GetExeTime(self):
        """
            Returns the execution time of the client
        """
        return self.exeTime

    def SetExeTime(self, exeTime):
        """
            Sets the execution time of the client
        """
        self.exeTime = exeTime

    def __str__(self):
        """
            Returns a string representation of the client object
        """
        return f"""name: {self.fname} {self.lname}\n
                    index: {self.id}
                    Exetime: {self.exeTime}"""