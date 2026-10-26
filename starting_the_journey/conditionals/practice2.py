age = int(input("provide me an age: "))
day = str(input("tell me the day of the week: "))
price = 12 if age >= 18 else 8
if day == "Wednesday":
    price -= 2
print("The price of the movie ticket is: $" + str(price))
