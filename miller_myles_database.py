class SimpleDatabase:
    def __init__(self):
        self.customers = {}
        self.products = {}
        self.next_customer_id = 1
        self.next_product_id = 1

    def add_customer(self):
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        total_purchases = float(input("Enter total purchases: "))
        self.customers[self.next_customer_id] = {
            "Name": name,
            "Address": address,
            "Phone Number": phone,
            "Email Address": email,
            "Total Purchases": total_purchases
        }
        print(f"Customer added with ID {self.next_customer_id}.")
        self.next_customer_id += 1

    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity available: "))
        rating = float(input("Enter rating: "))
        self.products[self.next_product_id] = {
            "Name": name,
            "Category": category,
            "Price": price,
            "Quantity Available": quantity,
            "Rating": rating
        }
        print(f"Product added with ID {self.next_product_id}.")
        self.next_product_id += 1

    def remove_customer(self):
        customer_id = int(input("Enter customer ID: "))
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} removed successfully.")
        else:
            print("Customer ID not found.")

    def remove_product(self):
        product_id = int(input("Enter product ID: "))
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} removed successfully.")
        else:
            print("Product ID not found.")

    def print_customers(self):
        if self.customers:
            for customer_id, info in self.customers.items():
                print(f"ID: {customer_id}, Info: {info}")
        else:
            print("No customers in the database.")

    def print_customer(self):
        customer_id = int(input("Enter customer ID: "))
        if customer_id in self.customers:
            print(f"ID: {customer_id}, Info: {self.customers[customer_id]}")
        else:
            print("Customer ID not found.")

    def print_products(self):
        if self.products:
            for product_id, info in self.products.items():
                print(f"ID: {product_id}, Info: {info}")
        else:
            print("No products in the database.")

    def print_product(self):
        product_id = int(input("Enter product ID: "))
        if product_id in self.products:
            print(f"ID: {product_id}, Info: {self.products[product_id]}")
        else:
            print("Product ID not found.")

    def update_customer(self):
        customer_id = int(input("Enter customer ID: "))
        if customer_id in self.customers:
            print("Available fields to update: " + ", ".join(self.customers[customer_id].keys()))
            field = input("Enter the field to update: ")
            if field in self.customers[customer_id]:
                new_value = input(f"Enter new value for {field}: ")
                # For simplicity, we are not type-checking new values here
                self.customers[customer_id][field] = new_value
                print(f"Customer {customer_id}'s {field} updated to {new_value}.")
            else:
                print("Invalid field name.")
        else:
            print("Customer ID not found.")

    def update_product(self):
        product_id = int(input("Enter product ID: "))
        if product_id in self.products:
            print("Available fields to update: " + ", ".join(self.products[product_id].keys()))
            field = input("Enter the field to update: ")
            if field in self.products[product_id]:
                new_value = input(f"Enter new value for {field}: ")
                # For simplicity, we are not type-checking new values here
                self.products[product_id][field] = new_value
                print(f"Product {product_id}'s {field} updated to {new_value}.")
            else:
                print("Invalid field name.")
        else:
            print("Product ID not found.")

    def run(self):
        print("Welcome to the Simple Database. Enter 'quit' or 'q' to exit.")
        while True:
            command = input("Enter command: ").lower().strip()
            if command in ['quit', 'q']:
                print("Exiting the database.")
                break
            elif command in ['add customer', 'ac']:
                self.add_customer()
            elif command in ['add product', 'ap']:
                self.add_product()
            elif command in ['remove customer', 'rc']:
                self.remove_customer()
            elif command in ['remove product', 'rp']:
                self.remove_product()
            elif command in ['print customers', 'pc']:
                self.print_customers()
            elif command in ['print customer', 'pc']:
                self.print_customer()
            elif command in ['print products', 'pp']:
                self.print_products()
            elif command in ['print product', 'pp']:
                self.print_product()
            elif command in ['update customer', 'uc']:
                self.update_customer()
            elif command in ['update product', 'up']:
                self.update_product()
            else:
                print("Invalid command.")

# To run the database
db = SimpleDatabase()
db.run()
