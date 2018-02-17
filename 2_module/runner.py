x = int(input())
y = int(input())
days = 1
while x < y:
    x = x + (10 * x) / 100
    days += 1
print(days)
