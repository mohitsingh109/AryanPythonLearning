# 1. Higher Order Function - The Function Factory

# Cookie factory that can bake different type of cookies
# if you give it the recipe

# The recipe = a function
# The factory = another function that uses your recipe


def chocolate_cookie_by_aryan(name):
    return f"🍫 Chocolate cooke for {name}"

def dry_fruit_cookie_by_mohit(name):
    return f"🍫 Dry fruit cooke for {name}"

def ice_cream_recipe(name):
    return f"🍧 Ice cream for {name}"

def cookie_factory(recipe, name):
    return recipe(name) # is calling chocolate_cookie(name)

print(cookie_factory(chocolate_cookie_by_aryan, "Aryan"))
print(cookie_factory(dry_fruit_cookie_by_mohit, "Mohit"))
print(cookie_factory(ice_cream_recipe, "Mohit"))

# 2. Lambda Functions - "Quick Snacks"

# def add_two(num):
#     return num + 2
#
# print(add_two(10))

add_two = lambda num: num + 2
print(add_two(10))

# Make square a number using lambda
make_square = lambda num: num * num
print(make_square(5))

#3. Closures - "Personal Chef"
# Imagine having a personal check who remember your taste

def chef(favorite_dish):
    def cook():
        return f"Cooking {favorite_dish} just for you!"
    return cook

mohit_chef = chef("Pasta")
print(mohit_chef())

aryan_chef = chef("Coffee")
print(aryan_chef())

# 4. map(), filter(), reduce() -- "Supermarket Scanner"
# map() ==> Convert one type to another
# map() ==> Apply change to all items(like changing prices)

prices = [100, 200, 300]
# discount of 10%
discount_by_9_percent = lambda p: p * 0.9
discounted = list(map(discount_by_9_percent, prices))
print(discounted)

# filter() == Keep only what you want
only_expensive = list(filter(lambda p: p > 150, prices))
print(only_expensive) #  200, 300

# reduce() == Combine into one bill (Combine all value in one value)

from functools import reduce
total = reduce(lambda a, b: a + b, prices)
print(total)

