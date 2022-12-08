import numpy as np

wantFirstPart = True

f = [[int(i) for i in e.replace('\n', '').replace('\r', '')] for e in open("input", "r").readlines()]
tab = np.array(f)
aux = np.zeros(tab.shape)

if wantFirstPart:
    # From-Left visible
    for i in range(tab.shape[0]):
        maxHeight = -1
        for j in range(tab.shape[1]):
            if tab[i][j] > maxHeight:
                maxHeight = tab[i][j]
                aux[i][j] = 1

    # From-Right visible
    for i in range(tab.shape[0]):
        maxHeight = -1
        for j in range(tab.shape[1] - 1, -1, -1):
            if tab[i][j] > maxHeight:
                maxHeight = tab[i][j]
                aux[i][j] = 1

    # From-Top visible
    for j in range(tab.shape[1]):
        maxHeight = -1
        for i in range(tab.shape[0]):
            if tab[i][j] > maxHeight:
                maxHeight = tab[i][j]
                aux[i][j] = 1

    # From-Bottom visible
    for j in range(tab.shape[1]):
        maxHeight = -1
        for i in range(tab.shape[0] - 1, -1, -1):
            if tab[i][j] > maxHeight:
                maxHeight = tab[i][j]
                aux[i][j] = 1

    print(int(aux.sum()))
else:
    for i in range(tab.shape[0]):
        for j in range(tab.shape[1]):
            localProd = 1

            # To-Top
            count = None
            for e in range(i - 1, -1, -1):
                if tab[i][j] <= tab[e][j]:
                    count = (i - 1) - e
                    count += 1
                    break
            if count is None:
                count = i
            localProd *= count

            # To-Left
            count = None
            for e in range(j - 1, -1, -1):
                if tab[i][j] <= tab[i][e]:
                    count = (j - 1) - e
                    count += 1
                    break
            if count is None:
                count = j
            localProd *= count

            # To-Bottom
            count = None
            for e in range(i + 1, tab.shape[0]):
                if tab[i][j] <= tab[e][j]:
                    count = e - (i + 1)
                    count += 1
                    break
            if count is None:
                count = tab.shape[0] - (i + 1)
            localProd *= count

            # To-Right
            count = None
            for e in range(j + 1, tab.shape[1]):
                if tab[i][j] <= tab[i][e]:
                    count = e - (j + 1)
                    count += 1
                    break
            if count is None:
                count = tab.shape[1] - (j + 1)
            localProd *= count

            aux[i][j] = localProd

    print(int(aux.max()))