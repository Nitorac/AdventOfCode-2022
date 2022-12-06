wantFirstPart = False

numOfDifferent = 4 if wantFirstPart else 14
line = open("input", "r").readline().replace('\n', '').replace('\r', '')
res = 0
for i in range(len(line) - numOfDifferent):
    if len(set(line[i:i+numOfDifferent])) == numOfDifferent:
        res = i + numOfDifferent
        break

print(res)