numbers = [i for i in range(1, 1000)]

numbers = [i for i in numbers if i%3==0 or i%5==0]

print(sum(numbers))
