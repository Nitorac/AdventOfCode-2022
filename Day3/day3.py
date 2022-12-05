wantFirstPart = False

def compute_prio(letter):
    return ord(letter) - (ord('a') - 1 if letter == letter.lower() else ord('A') - 27)

totalScore = 0
elfIdx = 0
lastSet = {}
for e in open("input", "r").readlines():
    line = e.replace('\n', '').replace('\r', '')
    if wantFirstPart:
        common = set(line[:len(line) // 2]).intersection(line[len(line) // 2:]).pop()
        totalScore += compute_prio(common)
    else:
        lastSet = set(line) if lastSet == {} else lastSet.intersection(line)
        if elfIdx == 2:
            elfIdx = -1
            totalScore += compute_prio(lastSet.pop())
            lastSet = {}
        elfIdx += 1

print(totalScore)
