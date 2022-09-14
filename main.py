import sys, json
from Order import Order
from Product import Product

inventory = []
orders = []

# for testing
def printInventory():
    for i in inventory:
        print("productId:", i.productId)
        print("description:", i.description)
        print("quantityOnHand:", i.quantityOnHand)
        print("reorderThreshold:", i.reorderThreshold)
        print("reorderAmount:", i.reorderAmount)
        print("deliveryLeadTime:", i.deliveryLeadTime)

# for testing
def printOrders():
    for o in orders:
        print("orderId:", o.orderId)
        print("status:", o.status)
        print("dateCreated:", o.dateCreated)
        printOrderProducts(o)

# for testing
def printOrderProducts(order):
    for i in order.items:
        print("orderId", i['orderId'])
        print("productId", i['productId'])
        print("quantity", i['quantity'])
        print("costPerItem", i['costPerItem'])

class main:
    data = json.load(sys.stdin)

    for p in data['products']:
        currProduct = Product(p['productId'], p['description'], p['quantityOnHand'], p['reorderThreshold'], p['reorderAmount'], p['deliveryLeadTime'])
        inventory.append(currProduct)

    for o in data['orders']:
        currOrder = Order(o['orderId'], o['status'], o['dateCreated'], o['items'])
        orders.append(currOrder)

    # for testing
    printInventory()
    printOrders()
