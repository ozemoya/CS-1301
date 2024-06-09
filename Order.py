class Order:
    def __init__(self, ono, cust, d):
        self.ono = ono
        self.placed_by = cust
        self.order_date = d
        self.items = []  # will contain tuples (Part, quantity, discount)

    def add_item(self, part, quantity, discount):
        self.items.append((part, quantity, discount))

    def get_order_details(self):
        return {
            "ono": self.ono,
            "placed_by": self.placed_by,
            "order_date": self.order_date,
            "items": self.items
        }

    def __str__(self):
        order_details = f"Order no: {self.ono}\nPlaced by: {self.placed_by}\nOrder date: {self.order_date}\n"
        for item in self.items:
            part, quantity, discount = item
            order_details += f"PNO: {part.get_pno()} PNAME: {part.get_pname()} PRICE: {part.get_price()} QTY: {quantity} %DISCOUNT: {discount}\n"
        return order_details
