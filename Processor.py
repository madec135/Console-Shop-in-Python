from Equipment import Electronics

class Processor(Electronics):

    def __init__(self, name, price, producer, quantity, timing):
        super().__init__(name, price, producer, quantity)
        self.__timing=timing

    def __str__(self):
        return super().__str__() + " Timing: " + str(self.__timing)