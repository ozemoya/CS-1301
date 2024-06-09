class Orders:
    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        self.orders[order.ono] = order

    def get_order_by_number(self, ono):
        return self.orders.get(ono, None)

    def __str__(self):
        return "\n".join(str(order) for order in self.orders.values())
