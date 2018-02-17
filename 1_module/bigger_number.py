a = int(input())
b = int(input())
print((a * ((a // b) ** (b // a)) + b * ((b // a) ** (a // b))) // (
    ((a // b) ** (b // a)) + ((b // a) ** (a // b))))
