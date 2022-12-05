import re

wantFirstPart = False

game_map_me = {
    "X": "C",  # rock wins
    "Y": "A",  # paper wins
    "Z": "B",  # scissors wins
}

game_map_you = {
    "A": "Z",  # rock wins
    "B": "X",  # paper wins
    "C": "Y",  # scissors wins
}

inv_game_map_me = {v: k for k, v in game_map_me.items()}

score = {
    "X": 1,
    "A": 1,
    "Y": 2,
    "B": 2,
    "Z": 3,
    "C": 3
}

totalScore = 0
for e in open("input", "r").readlines():
    line = e.replace('\n', '').replace('\r', '')
    you, me = re.search("([ABC]) ([XYZ])", line).groups()
    if wantFirstPart:
        totalScore += score[me]
        if me == game_map_you[you]:
            # you win
            totalScore += 0
        elif you == game_map_me[me]:
            totalScore += 6
        else:
            totalScore += 3
    else:
        if me == "Z":
            totalScore += 6 + score[inv_game_map_me[you]]
        elif me == "Y":
            totalScore += 3 + score[you]
        elif me == "X":
            totalScore += score[game_map_you[you]]

print(totalScore)