number = int(input())
wanted_word = input()
full_list = []
limited_list = []

for _ in range(number):
    current_word = input()
    full_list.append(current_word)
    if wanted_word in current_word:
        limited_list.append(current_word)
print(full_list)
print(limited_list)