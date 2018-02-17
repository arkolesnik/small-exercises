horizontal1 = int(input())
vertical1 = int(input())
horizontal2 = int(input())
vertical2 = int(input())
if (horizontal1 - horizontal2) ** 2 < 2 and (vertical1 - vertical2) ** 2 < 2:
    print("YES")
else:
    print("NO")
