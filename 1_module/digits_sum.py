number = int(input())

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
print(first_digit + second_digit + third_digit)
