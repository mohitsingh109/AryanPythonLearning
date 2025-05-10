class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    # Overriding Method...
    def speak(self):
        print("Woof!")


animal = Animal()
animal.speak()

animal = Dog()
animal.speak()


"""
Car: change_gear(),  open_doors()
- on_off_head_light()
- color
- wheel
- doors
- etc...

Tesla (Car): 
    change_gear()
    
AryanCars (Car)
    open_doors()
"""