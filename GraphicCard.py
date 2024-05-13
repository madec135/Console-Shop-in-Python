from Equipment import Electronics

class GraphicCard(Electronics):

    def __init__(self, name, price, producer, quantity, VRAM):
        super().__init__(name, price, producer, quantity)
        self.__VRAM=VRAM

    def __str__(self):
        return super().__str__() + " VRAM: " + str(self.__VRAM)