class Product:
    def __init__(self, productId, description, quantityOnHand, reorderThreshold, reorderAmount, deliveryLeadTime):
        self.productId = productId
        self.description = description
        self.quantityOnHand = quantityOnHand
        self.reorderThreshold = reorderThreshold
        self.reorderAmount = reorderAmount
        self.deliveryLeadTime = deliveryLeadTime