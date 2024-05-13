class Electronics:
    listOfEquipment=[]

    def __init__(self, name, price, producer, quantity):
        self.__name=name
        self.__price=price
        self.__producer=producer
        self.__quantity=quantity

    def __str__(self):
        return self.__name + " " + self.__producer + " Price: " + str(self.__price) + " Quantity in stock: " + str(self.__quantity)
    
    def getQuantity(self):
        return self.__quantity
    
    def getPrice(self):
        return self.__price
    
    def getName(self):
        return self.__name
    
    def setQuantity(self, number):
        self.__quantity=number

    @staticmethod
    def addEquipment(eq):
        Electronics.listOfEquipment.append(eq)