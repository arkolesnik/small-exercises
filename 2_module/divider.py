n = int(input())
number = 1
while number < n:
    number += 1
    if n % number == 0:
        print(number)
        break
