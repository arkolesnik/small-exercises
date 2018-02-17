a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0:
    if (a >= b) and (a >= c):
        squared_largest = a ** 2
        squared_two = b ** 2 + c ** 2
    elif (b >= a) and (b >= c):
        squared_largest = b ** 2
        squared_two = a ** 2 + c ** 2
    else:
        squared_largest = c ** 2
        squared_two = a ** 2 + b ** 2
    if squared_largest == squared_two:
        print("rectangular")
    elif squared_largest < squared_two:
        print("acute")
    elif squared_largest > squared_two:
        print("obtuse")
else:
    print("impossible")
