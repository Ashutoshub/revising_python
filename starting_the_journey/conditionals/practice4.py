order_size = input("tell me size of coffee order: ")
want_extra_shot = bool(input("do you want an extra shot? (True/False): "))
if order_size == "small" and want_extra_shot:
    print("The price of the coffee is: $3.00")
elif order_size == "small" and not want_extra_shot:
    print("The price of the coffee is: $2.50")
elif order_size == "medium" and want_extra_shot:
    print("The price of the coffee is: $4.00")
elif order_size == "medium" and not want_extra_shot:
    print("The price of the coffee is: $3.50")
elif order_size == "large" and want_extra_shot:
    print("The price of the coffee is: $5.00")
elif order_size == "large" and not want_extra_shot:
    print("The price of the coffee is: $4.50")  
