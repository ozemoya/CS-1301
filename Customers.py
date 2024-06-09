class Customers:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.get_cno()] = customer

    def get_customer_details(self, cno):
        return self.customers.get(cno, None)

    def __str__(self):
        return "\n".join(str(customer) for customer in self.customers.values())
