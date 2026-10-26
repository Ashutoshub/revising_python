fruit = input("What fruit do you have? ")
color = input("What color is the fruit? ")
if fruit == "banana":
    if color == "yellow":
        print("ripe")
    elif color == "green":
        print("unripe")
    elif color == "brown":
        print("overripe")
    else:
        print("unknown")