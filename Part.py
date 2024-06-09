class Part:
    def __init__(self, pnum, name, price):
        self.pno = pnum
        self.pname = name
        self.price = price

    def get_pno(self):
        return self.pno

    def get_pname(self):
        return self.pname

    def get_price(self):
        return self.price

    def set_pno(self, pnum):
        self.pno = pnum

    def set_pname(self, name):
        self.pname = name

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"PNO: {self.pno}\nPNAME: {self.pname}\nPRICE: {self.price}"
