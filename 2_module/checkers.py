x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
yd = y2 - y1
if (x2 + y2) % 2 == 0 and 8 > y2 > y1 and x1 - yd <= x2 <= x1 + yd:
    print("YES")
else:
    print("NO")
