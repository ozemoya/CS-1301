
import sys
from Customer import Customer
from Customers import Customers
from Part import Part
from Parts import Parts
from Order import Order
from Orders import Orders

# Load Customers
def load_customers(customers, filename):
    with open(filename, 'r') as file:
        for line in file:
            cno, cname, city = line.strip().split(':')
            customers.add_customer(Customer(cno, cname, city))

# Load Parts
def load_parts(parts, filename):
    with open(filename, 'r') as file:
        for line in file:
            pno, pname, price = line.strip().split(':')
            parts.add_part(Part(pno, pname, float(price)))

# Load Orders
def load_orders(orders, customers, parts, filename):
    with open(filename, 'r') as file:
        for line in file:
            ono, cno, date, *items = line.strip().split(':')
            if cno not in customers.customers:
                print(f"Customer number {cno} from order {ono} does not exist.")
                continue
            order = Order(ono, customers.customers[cno], date)
            for item in items:
                pno, qty, discount = map(int, item.split(','))
                if pno not in parts.parts:
                    print(f"Part number {pno} from order {ono} does not exist.")
                    continue
                order.add_item((parts.parts[pno], qty, discount))
            orders.add_order(order)

# Process Command
def process_command(customers, parts, orders, command):
    args = command.split()
    cmd = args[0]
    if cmd == 'c':
        # Customer related command
        if len(args) == 1:
            # List all customers
            for cno in customers.customers:
                print(customers.customers[cno])
        elif len(args) == 2:
            # Details for a single customer
            cno = args[1]
            if cno in customers.customers:
                print(customers.customers[cno])
            else:
                print(f"Customer number {cno} does not exist.")
    elif cmd == 'o':
        # Order related command
        ono = args[1]
        if ono in orders.orders:
            order = orders.orders[ono]
            print(order)
        else:
            print(f"Order number {ono} does not exist.")
    elif cmd == 'u':
        # Update order discount
        ono, pno, discount = args[1], int(args[2]), int(args[3])
        if ono in orders.orders:
            order = orders.orders[ono]
            order.update_discount(pno, discount)
            print("Discount updated!")
        else:
            print(f"Order number {ono} does not exist.")
    elif cmd == 'd':
        # Delete part from order
        ono, pno = args[1], int(args[2])
        if ono in orders.orders:
            order = orders.orders[ono]
            order.remove_part(pno)
            print("Part deleted from order!")
    else:
        print("Unknown command.")

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python Driver.py <data_folder>")
        return
    data_folder = sys.argv[1]
    customers = Customers()
    parts = Parts()
    orders = Orders()
    load_customers(customers, f"{data_folder}/customers.dat")
    load_parts(parts, f"{data_folder}/parts.dat")
    load_orders(orders, customers, parts, f"{data_folder}/orders.dat")
    print("Welcome to the Orders Database Program.")
    while True:
        command = input("c, c cno, o ono, u ono pno discount, d ono pno, q: ").lower()
        if command == 'q':
            print("Bye!")
            break
        process_command(customers, parts, orders, command)

if __name__ == "__main__":
    main()
