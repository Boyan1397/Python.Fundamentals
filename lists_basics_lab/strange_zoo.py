head = input()
body = input()
tail = input()
zoo = [tail, body, head]
temp = zoo[0]
zoo[0] = zoo[2]
zoo[2] = temp

print(zoo)