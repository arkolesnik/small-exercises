n = int(input())
result = 1
while result <= n:
    if result == n:
        print("YES")
        break
    result = result * 2
else:
    print("NO")
