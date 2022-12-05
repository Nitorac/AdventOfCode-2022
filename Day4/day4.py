wantFirstPart = False

numOfFullyContained = 0
for e in open("input", "r").readlines():
    firstSet, secondSet = [set(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1)) for i in e.replace('\n', '').replace('\r', '').split(',')]
    if wantFirstPart:
        numOfFullyContained += firstSet.issubset(secondSet) or secondSet.issubset(firstSet)
    else:
        numOfFullyContained += not not firstSet & secondSet

print(numOfFullyContained)