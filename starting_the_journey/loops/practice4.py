num = int(input("Please enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("factorial is ", factorial)