now = int(input())
seqCount = 0
seqSum = 0
while now != 0:
    seqSum = seqSum + now
    now = int(input())
    seqCount += 1
print(seqSum / seqCount)
