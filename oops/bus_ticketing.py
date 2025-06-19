class Passenger:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ticket_price(self):
        if self.age < 5:
            return 0
        elif 5 <= self.age <= 18:
            return 10
        else:
            return 20

def create_passenger():
    name = input("Who else is getting on the bus? ")
    age = int(input("How old are they? "))
    return Passenger(name, age)

passengers = [
    Passenger("Aryan", 13),
    Passenger("Mohit", 28),
    Passenger("Arjun", 9),
    create_passenger(),
    create_passenger()
]

for person in passengers:
    price = person.ticket_price()
    print(f"{person.name} has to pay {price} rupees to get on the bus.")