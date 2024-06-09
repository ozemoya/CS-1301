class Customer:
    # constructor
    def __init__(self, cnum, name, cty):
        self.cno = cnum
        self.cname = name
        self.city = cty

    # getter for customer number
    def get_cno(self):
        return self.cno

    # getter for customer name
    def get_cname(self):
        return self.cname

    # getter for city
    def get_city(self):
        return self.city

    # setter for customer number
    def set_cno(self, cnum):
        self.cno = cnum

    # setter for customer name
    def set_cname(self, name):
        self.cname = name

    # setter for city
    def set_city(self, cty):
        self.city = cty

    # return string representation of Customer object
    def __str__(self):
        return f"CNO: {self.cno}\nCNAME: {self.cname}\nCITY: {self.city}"
