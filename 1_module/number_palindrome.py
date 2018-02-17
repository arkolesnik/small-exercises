number = int(input())
two_first_digits = number // 100
two_last_digits_reverse = (number % 10) * 10 + number % 100 // 10
print(two_first_digits - two_last_digits_reverse + 1)
