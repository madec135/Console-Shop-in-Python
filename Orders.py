from Equipment import Electronics
from Clients import Client

class Order:

    orderList=[]

    def __init__(self, orderName, orderingClient, productOrdered, quantityOrdered):
        if productOrdered.getQuantity()>quantityOrdered and orderingClient.getBudget()>(quantityOrdered*productOrdered.getPrice()):
            self.__orderName=orderName
            self.__orderingClient=orderingClient.getName()
            self.__productOrdered=productOrdered.getName()
            self.__quantityOrdered=quantityOrdered
            self.__orderPrice=(quantityOrdered*productOrdered.getPrice())
            quantityLeft=(productOrdered.getQuantity()-quantityOrdered)
            productOrdered.setQuantity(quantityLeft)
            budgetLeft=(orderingClient.getBudget()-(quantityOrdered*productOrdered.getPrice()))
            orderingClient.setBudget(budgetLeft)
            print("Quantity left in stock for product: ", productOrdered.getName(), " is: ", productOrdered.getQuantity())
            print("Budget left for a client: ", orderingClient.getName(), " is: ", orderingClient.getBudget())
        else:
            print("Cannot process order. Not enough product quantity left in stock or not enough client's budget.")

    def returnPrice(self):
        return self.__orderPrice
    
    def returnName(self):
        return self.__orderName
    
    def returnClient(self):
        return self.__orderingClient
    
    def returnQuantity(self):
        return self.__quantityOrdered
    
    def returnProduct(self):
        return self.__productOrdered
    
    def __str__(self):
        return self.__orderName + " Ordering client: " + self.__orderingClient + " Product ordered: " + self.__productOrdered + " Quantity ordered: " + str(self.__quantityOrdered) + " Order price: " + str(self.__orderPrice)
    
    @staticmethod
    def addOrder(element):
        Order.orderList.append(element)
        
    

