from Equipment import Electronics

class RAM(Electronics):

    def __init__(self, name, price, producer, quantity, memoryType):
        super().__init__(name, price, producer, quantity)
        self.__memoryType=memoryType

    def __str__(self):
        return super().__str__() + " Memory Type: " + str(self.__memoryType)