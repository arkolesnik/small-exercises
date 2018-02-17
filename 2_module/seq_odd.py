now = int(input())
seqOddCount = 0
while now != 0:
    if now % 2 == 0:
        seqOddCount += 1
    now = int(input())
print(seqOddCount)
