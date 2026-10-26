input_string = input("Please enter a string: ")
for ch in input_string:
    if input_string.count(ch) == 1:
        print(ch)
        break
