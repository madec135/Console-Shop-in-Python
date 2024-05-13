from People import People
from Clients import Client
from Workers import Worker
from Equipment import Electronics
from Orders import Order


def printClients():

    for clients in People.listOfPeople:
        if isinstance(clients, Client):
            print(clients)
        else:
            continue


def printWorkers():

    for workers in People.listOfPeople:
        if isinstance(workers, Worker):
            print(workers)
        else:
            continue


def printEquipment():

    for product in Electronics.listOfEquipment:
        print(product)


def printOrder():

    for order in Order.orderList:
        print(order)


def ordersWithValueMoreThan5000():

    listWithOrdersWorthMoreThan5000=list(filter(lambda totalPrice: totalPrice.returnPrice()>5000, Order.orderList))
    return listWithOrdersWorthMoreThan5000


def printOrdersWithValueMoreThan5000():

    for order in ordersWithValueMoreThan5000():
        print(order)


def saveOrdersToFile():

    with open("order_info.txt", "wt") as save:
        for element in Order.orderList:
            save.write(f"Product ordered: {element.returnProduct()} Quantity ordered: {element.returnQuantity()} Ordering client: {element.returnClient()} Order price: {element.returnPrice()}\n")
