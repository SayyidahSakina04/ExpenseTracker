class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: Name: {self.name}, Category: {self.category}, Amount: {self.amount:.2f}>"