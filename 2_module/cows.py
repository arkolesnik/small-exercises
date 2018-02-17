n = int(input())
ending = ""
if n // 10 != 1:
    if n % 10 == 1:
        ending = "a"
    elif 1 < n % 10 < 5:
        ending = "y"
print(str(n) + " korov" + ending)
