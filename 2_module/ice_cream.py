x = int(input())
if x != 0 and ((x % 8) % 3 == 0 or (x % 8) % 5 == 0 or (x % 5) % 3 == 0 or
   (x % 3) % 5 == 0):
    print("YES")
else:
    print("NO")
