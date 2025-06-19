class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price if self.price <= 1000 else self.price * 9/10

    def has_been_discounted(self):
        return self.price > 1000

    def statement(self):
        common_string = f"{self.name} costs {self.price} dollars."
        if self.has_been_discounted():
            print(f"{common_string} The discount makes it {self.final_price()} dollars.")
        else:
            print(common_string)

products = [
    Product("Banana",10),
    Product("Rolex", 15000),
    Product("Cricket Bat", 350)
]

for p in products:
    p.statement()