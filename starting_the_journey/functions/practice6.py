#generator function with yield
def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
print(list(even_generator(10)))
print(even_generator(10)) # This will print the generator object, not the values. To see the values, you can convert it to a list or iterate through it.