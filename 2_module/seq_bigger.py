now = int(input())
next_num = 0
seqBiggerCount = 0
while next_num != 0:
    next_num = int(input())
    if next_num > now:
        seqBiggerCount += 1
    now = next_num
print(seqBiggerCount)
