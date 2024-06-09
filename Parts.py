class Parts:
    def __init__(self):
        self.parts = {}

    def add_part(self, part):
        self.parts[part.get_pno()] = part

    def get_part_details(self, pno):
        return self.parts.get(pno, None)

    def __str__(self):
        return "\n".join(str(part) for part in self.parts.values())
