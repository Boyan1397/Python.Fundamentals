factor = int(input())
count = int(input())

list_of_numbers = []
for number in range(factor, (count * factor) + 1, factor):
    list_of_numbers.append(number)
print(list_of_numbers)
