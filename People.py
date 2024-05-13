class People:
    listOfPeople=[]

    def __init__(self, name, surname):
        self.__name=name
        self.__surname=surname
    
    def __str__(self):
        return self.__name + " " + self.__surname
    
    def getName(self):
        return self.__name
    
    @staticmethod
    def addPerson(human):
        People.listOfPeople.append(human)