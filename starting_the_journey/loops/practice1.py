n = int(input("provide me a number: "))
sum_of_evens = 0
for i in range(1,n + 1):
    if(i % 2 == 0):
        sum_of_evens += i
print(sum_of_evens)