n = int(input())
result = 1
k = 0
while n > 1 and result < n:
    result = result * 2
    k += 1
print(k)
