# h1 - Spam Detector (Linear Search)

blacklist = ["spam@gmail.com", "fake@yahoo.com", "abc@gmail.com"]

sender = input("Enter sender email: ")

found = False

for email in blacklist:
    if email == sender:
        found = True
        break

if found:
    print("Spam Email")
else:
    print("Safe Email")
