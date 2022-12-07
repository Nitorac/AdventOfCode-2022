from treebuilder import TreeBuilder

wantFirstPart = False

# Read file
f = [e.replace('\n', '').replace('\r', '').strip() for e in open("input", "r").readlines()]

# Parse file in "[(command, ['resline1', 'resline2', ...]), (...]
command_and_res = []
lastCommand = ""
tmpRes = []
for line in f:
    if line.startswith('$'):
        if lastCommand != "":
            command_and_res.append((
                lastCommand,
                tmpRes
            ))
        lastCommand = line
        tmpRes = []
    else:
        tmpRes.append(line)
command_and_res.append((
    lastCommand,
    tmpRes
))

print(command_and_res)

# Construct fs
curPath = []
fs = TreeBuilder()
for e in command_and_res:
    cmd = e[0]
    if cmd.startswith('$ cd'):
        destDir = cmd.split(' ')[2]
        if destDir == '/':
            curPath = []
        elif destDir == '..':
            curPath = curPath[:-1] if len(curPath) > 0 else []
        else:
            curPath.append(destDir)
    elif cmd == '$ ls':
        for res in e[1]:
            element = res.split(' ')
            if element[0] == 'dir':
                fs.add_dir(curPath + [element[1]])
            else:
                fs.add_file(curPath + [element[1]], int(element[0]))

# Get all dir sizes
dirSizes = fs.get_dir_sizes()

# Answers
if wantFirstPart:
    sum = 0
    for e in dirSizes.values():
        sum += 0 if e > 100000 else e
    print(sum)
else:
    freeLeft = 70000000 - dirSizes['/']
    selectedDirs = []
    for k,v in dirSizes.items():
        if freeLeft + v >= 30000000:
            print(k, v/1000)
            selectedDirs.append((k, v))
    print(min(selectedDirs, key=lambda x: x[1]))
