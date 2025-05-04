# PizzaOrder
# - customer, toppings: (Aryan, ["cheese", "olives])

class PizzaOrder:

    def __init__(self, customer, toppings):
        self.customer = customer
        self.toppings = toppings

    def summary(self):
        print(f"{self.customer} ordered pizza with: {', '.join(self.toppings)}")


# Task1: List of 3 pizza order
# Task2: function that will print the customer name, and it's order details
# Aryan ordered pizza with: cheese, tomato

orders = [
    PizzaOrder("Aryan", ["cheese", "tomato"]), # it's calling the contractor of PizzaOrder class to initialize the instance variable
    PizzaOrder("Mohit", ["pepperoni", "olives"]),
    PizzaOrder("Kabir", ["onions", "mushrooms"])
]

for order in orders:
    order.summary()

# print all the Customer name what has onions in their order
for order in orders:
    if 'mushrooms' in order.toppings:
        print(order.customer)

