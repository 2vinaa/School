class Product:
    def __init__(self, description:str, price:int):
        self.description = description
        self.price = price

class Element:
    def __init__(self, product: Product, number:int):
        self.Selected_Prod = product
        self.numberofitems = number

class Invoice:
    def __init__(self, invoice: List[Element]):
        self.invoice = invoice
        self.amount = 0
    def calculate_val(self):
        for element in self.invoice:
            self.amount += element.Selected_Prod.price * element.numberofitems
        return self.amount
