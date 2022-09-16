import sys, json
from Order import Order
from OrderStatus import OrderStatus
from Product import Product

inventory = []
orders = []

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

# takes in a single 'order' and adds its id to 'unfulfilledOrderIds' if it cannot be fulfilled
# checks that each item being ordered is in stock
# marks unfulfillable orders as Unfulfillable
# fulfills fulfillable orders
def fulfillOrder(order, unfulfilledOrderIds):
    # check that the order can be fulfilled
    for orderProduct in order.items:
        # in case the shopping cart has a weird value
        if orderProduct['quantity'] <= 0:
            break
        for inventoryProduct in inventory:
            # find the product in the inventory
            if orderProduct['productId'] == inventoryProduct.productId:
                # if the product is not in stock, reorder and mark the order as unfulfilled
                if inventoryProduct.quantityOnHand < orderProduct['quantity'] or inventoryProduct.quantityOnHand <= 0:
                    restockProduct(orderProduct['productId'])
                    order.status = OrderStatus.Unfulfillable.name
                    # reduce inventory to 0, and reduce order quantity by the current stock left
                    orderProduct['quantity'] = orderProduct['quantity'] - inventoryProduct.quantityOnHand
                    inventoryProduct.quantityOnHand = 0
                # product is in stock
                else:
                    # deduct from inventory quantityOnHand, and reduce quantity left to buy to 0
                    inventoryProduct.quantityOnHand = inventoryProduct.quantityOnHand - orderProduct['quantity']
                    orderProduct['quantity'] = 0
                break
    # fulfill the order if it is Pending
    if order.status == OrderStatus.Pending.name:
        order.status = OrderStatus.Fulfilled.name
    else:
        unfulfilledOrderIds.append(order.orderId)

# takes in 'orderIds' to process and returns an array of all unfulfilled orderIds
def processOrders(orderIds):
    unfulfilledOrderIds = []
    for orderId in orderIds:
        for order in orders:
            if int(orderId) == order.orderId:
                fulfillOrder(order, unfulfilledOrderIds)
                break
    return unfulfilledOrderIds
        
# # for testing
# def printInventory():
#     for i in inventory:
#         print("productId:", i.productId)
#         print("description:", i.description)
#         print("quantityOnHand:", i.quantityOnHand)
#         print("reorderThreshold:", i.reorderThreshold)
#         print("reorderAmount:", i.reorderAmount)
#         print("deliveryLeadTime:", i.deliveryLeadTime)
#         print()

# # for testing
# def printOrders():
#     for o in orders:
#         print("orderId:", o.orderId)
#         print("status:", o.status)
#         print("dateCreated:", o.dateCreated)
#         printOrderProducts(o)
#     print()

# # for testing
# def printOrderProducts(order):
#     for i in order.items:
#         print("   orderId", i['orderId'])
#         print("   productId", i['productId'])
#         print("   quantity", i['quantity'])
#         print("   costPerItem", i['costPerItem'])
#         print("   ##################")

class main:
    f = open('data.json')
    data = json.load(f)
    f.close()

    # create inventory array of products
    for p in data['products']:
        currProduct = Product(p['productId'], p['description'], p['quantityOnHand'], p['reorderThreshold'], p['reorderAmount'], p['deliveryLeadTime'])
        inventory.append(currProduct)

    allOrderIds = []
    # create array of orders
    for o in data['orders']:
        currOrder = Order(o['orderId'], o['status'], o['dateCreated'], o['items'])
        allOrderIds.append(str(o['orderId']))
        orders.append(currOrder)

    print("Enter comma-delimited productIds to process. Leave blank to process all orders")
    orderIdsToProcess = input()
    if orderIdsToProcess == '':
        orderIdsToProcess = ",".join(allOrderIds)
    print("Processing", orderIdsToProcess)

    restock()
    unfulfilledOrderIds = processOrders(orderIdsToProcess.split(","))
    # for testing
    # printInventory()
    # printOrders()
    print("Unfulfillable orderIds:", unfulfilledOrderIds)
