elfIdx = 0
elfs = [0]
for e in open("input", "r").readlines():
    line = e.replace('\n', '').replace('\r', '')
    if line == '':
        elfIdx += 1
        elfs.append(0)
        continue
    elfs[elfIdx] += int(line)

elfs.sort(reverse=True)
# 1st part
print(elfs[0])

# 2nd part
print(sum(elfs[:3]))
