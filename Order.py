class Order:
    def __init__(self, orderId, status, dateCreated, items):
        self.orderId = orderId
        self.status = status
        self.dateCreated = dateCreated
        self.items = items