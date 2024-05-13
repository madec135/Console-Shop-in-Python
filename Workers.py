from People import People

class Worker(People):

    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.__position=position

    def __str__(self):
        return super().__str__() + " " + self.__position