number_of_lines = int(input())
even_number = []
odd_number = []
positive_number = []
negative_number = []
for _ in range(number_of_lines):
    current_num = int(input())
    if current_num % 2 == 0:
        even_number.append(current_num)
    if current_num % 2 == 1:
        odd_number.append(current_num)
    if current_num >= 0:
        positive_number.append(current_num)
    if current_num < 0:
        negative_number.append(current_num)
command = input()
if command == "even":
    print(even_number)
if command == "odd":
    print(odd_number)
if command == "positive":
    print(positive_number)
if command == "negative":
    print(negative_number)

