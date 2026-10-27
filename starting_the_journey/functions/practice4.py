# *args problem
def sum_all(*args):
    total = 0
    print(args)  # This will print the tuple of arguments passed to the function
    print(*args)  # This will unpack the tuple and print each argument separately and args is a tuple of arguments passed to the function   
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30))