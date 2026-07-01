# Program 1: Amazon Fulfillment Centre using Array

belt = ["Laptop", "Mobile", "Mouse", None, None, None, None, None]

slot = int(input("Enter slot number (0-7): "))
print("Product at slot", slot, ":", belt[slot])

product = input("Enter product to search: ")
if product in belt:
    print(product, "found at slot", belt.index(product))
else:
    print("Product not found")

slot = int(input("Enter slot number to update: "))
new_product = input("Enter new product: ")
belt[slot] = new_product

print("Updated Belt:", belt)

if None in belt:
    print("Belt is not full")
else:
    print("Belt is full")
