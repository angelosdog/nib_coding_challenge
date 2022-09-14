import sys, json
from Order import Order
from OrderStatus import OrderStatus
from Product import Product

inventory = []
orders = []
unfulfilledOrderIds = []

# Assumed to be have already been implemented, as per the spec
def restock():
    # things I would think about including in the implementation:
        # this could be a restock of the whole inventory
        # see if the reorderAmount is enough to satisfy all unfulfillable orders
        # only order more if the reorderAmount is not enough
    return

# Assumed to be have already been implemented, as per the spec
def restockProduct(productId):
    # this would probably be used in the restock() method, but only restocks a single product
    return

def fulfillOrder(order):
    productsToBuy = []
    # check that the order can be fulfilled
    for orderProduct in order.items:
        for inventoryProduct in inventory:
            # find the product in the inventory
            if orderProduct['productId'] == inventoryProduct.productId:
                # if the product is not in stock, reorder and mark the order as unfulfilled
                if inventoryProduct.quantityOnHand < orderProduct['quantity'] or inventoryProduct.quantityOnHand <= 0:
                    restockProduct(orderProduct['productId'])
                    order.status = OrderStatus.Unfulfillable.name
                    # continue the loop in case other products need restocking
                else:
                    # save the amount of products to buy so we can deduct it from the inventory if the order can be fulfilled
                    productsToBuy.append((inventoryProduct, orderProduct['quantity']))
    # fulfill the order if it is Pending
    if order.status == OrderStatus.Pending.name:
        for i in productsToBuy:
            i[0].quantityOnHand = i[0].quantityOnHand - i[1]
        # mark order as fulfulled
        order.status = OrderStatus.Fulfilled.name
    else:
        unfulfilledOrderIds.append(order.orderId)
        
def processOrders():
    for order in orders:
        fulfillOrder(order)
        
# # for testing
# def printInventory():
#     for i in inventory:
#         print("productId:", i.productId)
#         print("description:", i.description)
#         print("quantityOnHand:", i.quantityOnHand)
#         print("reorderThreshold:", i.reorderThreshold)
#         print("reorderAmount:", i.reorderAmount)
#         print("deliveryLeadTime:", i.deliveryLeadTime)

# # for testing
# def printOrders():
#     for o in orders:
#         print("orderId:", o.orderId)
#         print("status:", o.status)
#         print("dateCreated:", o.dateCreated)
#         printOrderProducts(o)

# # for testing
# def printOrderProducts(order):
#     for i in order.items:
#         print("orderId", i['orderId'])
#         print("productId", i['productId'])
#         print("quantity", i['quantity'])
#         print("costPerItem", i['costPerItem'])

class main:
    f = open('data.json')
    data = json.load(f)

    for p in data['products']:
        currProduct = Product(p['productId'], p['description'], p['quantityOnHand'], p['reorderThreshold'], p['reorderAmount'], p['deliveryLeadTime'])
        inventory.append(currProduct)

    for o in data['orders']:
        currOrder = Order(o['orderId'], o['status'], o['dateCreated'], o['items'])
        orders.append(currOrder)

    f.close()

    restock()
    processOrders()
    # for testing
    # printInventory()
    # printOrders()
    print(unfulfilledOrderIds)
