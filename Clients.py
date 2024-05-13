from People import People

class Client(People):

    def __init__(self, name, surname, budget):
        super().__init__(name, surname)
        self.__budget=budget

    def getBudget(self):
        return self.__budget
    
    def setBudget(self, value):
        self.__budget=value
    
    def __str__(self):
        return super().__str__() + str(self.__budget) + " zl"
    
    