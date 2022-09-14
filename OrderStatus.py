from enum import Enum

class OrderStatus(Enum):
    Unfulfillable = 0
    Pending = 1
    Fulfilled = 2