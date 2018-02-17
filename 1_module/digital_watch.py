n = int(input())
m = n % 1440
minutes = m % 60
hours = m // 60
print(hours, minutes)
