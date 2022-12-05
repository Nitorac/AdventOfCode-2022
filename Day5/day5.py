import numpy as np
import re

finput = open("input", "r")
keepMultipleCrateOrder = False


lines = [line.replace('\n', '') for line in finput.readlines()]
numOfStacks = (len(lines[0]) + 1) // 4
maxStackSize = lines.index('') - 1
stacks = [[] for _ in range(numOfStacks)]

for stackLine in range(maxStackSize - 1, -1, -1):
    for i in range(numOfStacks):
        chrIdx = 1 + i * 4
        if lines[stackLine][chrIdx] != ' ':
            stacks[i].append(lines[stackLine][chrIdx])

stacks = [e for e in stacks]

print(stacks)

# Apply instructions
for e in lines[maxStackSize + 2:]:
    found = re.search("move ([0-9]+) from ([0-9]+) to ([0-9]+)", e)
    numOfCrates, fromStack, toStack = [int(e) for e in found.groups()]
    # Get crates to append to new stack
    cratesToAppend = stacks[fromStack-1][-numOfCrates:]
    cratesToAppend = cratesToAppend if keepMultipleCrateOrder else list(reversed(cratesToAppend))
    # Delete crates from fromStack
    stacks[fromStack-1] = stacks[fromStack-1][:-numOfCrates]
    # Append crates to toStack
    stacks[toStack-1] = stacks[toStack-1] + cratesToAppend

print(stacks)

print(''.join([e[-1] for e in stacks]))