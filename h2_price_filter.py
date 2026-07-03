# h2 - E-Commerce Price Filter (Binary Search)

prices = [20000, 30000, 40000, 50000, 60000]

target = int(input("Enter target price: "))

low = 0
high = len(prices) - 1
answer = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

if answer != -1:
    print("First price is:", prices[answer])
else:
    print("No product found")
