first_app = int(input())
last_app = int(input())
if (first_app - 1) % (last_app - first_app + 1) == 0:
    print("YES")
else:
    print("NO")
