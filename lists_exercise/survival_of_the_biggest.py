number_list = input().split()
n = int(input())

for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

for i in range(n):
    min_number = min(number_list)
    number_list.remove(min_number)

for i in range(len(number_list)):
    number_list[i] = str(number_list[i])
print(", ".join(number_list))