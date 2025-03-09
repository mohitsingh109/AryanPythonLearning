# Input function
# Syntax input("String") it always return a string

msg = "Enter the product name: "
product_name = input(msg)
price = int(input("Enter the price: ")) # Convert input to int
print(product_name, price)
# The product {product_name} costs {price}
print("The product " + product_name + " costs " + str(price))
print(f"The product {product_name} costs {price}")