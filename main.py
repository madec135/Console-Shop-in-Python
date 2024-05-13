from Clients import Client
from People import People
from Workers import Worker
from printFunctions import printClients, printWorkers, printEquipment, printOrdersWithValueMoreThan5000, saveOrdersToFile
from Equipment import Electronics
from GraphicCard import GraphicCard
from Processor import Processor
from RAM import RAM
from Orders import Order

client1=Client("Michal", "Dec", 10000)
client2=Client("Malcom", "Smith", 5000)
client3=Client("Nadia", "Macieja", 7500)
client4=Client("Michael", "Trevis", 20000)

worker1=Worker("Kamil", "Baranek", "IT Support Desk")
worker2=Worker("Maciej", "Tak", "Accountant")
worker3=Worker("Jakub", "Kama", "Seller")

People.addPerson(client1)
People.addPerson(client2)
People.addPerson(client3)
People.addPerson(client4)
People.addPerson(worker1)
People.addPerson(worker2)
People.addPerson(worker3)

print("Clients:")
printClients()

print("\nWorkers: ")
printWorkers()

graphic1=GraphicCard("RTX 4070", 5000, "NVIDIA", 10, 12)
graphic2=GraphicCard("RTX 4090", 10000, "NVIDIA", 5, 20)
graphic3=GraphicCard("RTX 4080", 7000, "NVIDIA", 3, 10)

processor1=Processor("Intel Core i7", 3000, "Intel", 5, "4.0 GHz")

ram1=RAM("Gigabyte", 500, "DDR5", 20, "256bit")

Electronics.addEquipment(graphic1)
Electronics.addEquipment(graphic2)
Electronics.addEquipment(graphic3)
Electronics.addEquipment(processor1)
Electronics.addEquipment(ram1)

print("\nEquipment in stock: ")
printEquipment()

print("\nPrinting orders: ")
order1=Order("Order 1", client1, ram1, 10)
order2=Order("Order 2", client2, processor1, 1)
order3=Order("Order 3", client3, graphic2, 1)
order4=Order("Order 4", client4, graphic1, 2)

Order.addOrder(order1)
Order.addOrder(order2)
Order.addOrder(order4)

print("\nOrders that are more expensive than 5000: ")
printOrdersWithValueMoreThan5000()

print("\nSaving orders to file...")
saveOrdersToFile()
