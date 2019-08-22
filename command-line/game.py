"""
		paper,scissors,rock,lizard,spock
paper      X      -1      1    -1     1
scissors   1       X      -1    1     -1
rock       -1       1      X     1     -1
lizard     1       -1      -1    X    1
spock      -1      1      1     -1      X

"""

import random

res = [  [ {"r": 0, "t": "draws"}, {"r": -1, "t": "is cut"}, {"r": 1, "t": "covers"}, {"r": -1, "t": "is eaten"}, {"r": 1, "t": "disproves"} ],
		 [ {"r": 1, "t": "cuts"}, {"r": 0, "t": "draws"}, {"r": -1, "t": "are crushed"}, {"r": 1, "t": "decapitates"}, {"r": -1, "t": "are smashed"} ],
		 [ {"r": -1, "t": "is covered"}, {"r": 1, "t": "crushes"}, {"r": 0, "t": "draws"}, {"r": 1, "t": "crashes"}, {"r": -1, "t": "is vaporized"} ],
		 [ {"r": 1, "t": "eats"}, {"r": -1, "t": "is decapitated"}, {"r": -1, "t": "is crushed"}, {"r": 0, "t": "draws"}, {"r": 1, "t": "poisons"} ],
		 [ {"r": -1, "t": "is disproved"}, {"r": 1, "t": "smashes"}, {"r": 1, "t": "vaportizes"}, {"r": -1, "t": "is poisoned"}, {"r": 0, "t": "draws"} ] ]

moves = {"paper": 0, "scissors":1, "rock": 2, "lizard": 3, "Spock": 4}

def playMe(playerChoice):
	k, v = random.choice(list(moves.items()))
	print("Your choice: " + playerChoice +  ", opponent choice: " + k)

	r = res[moves[playerChoice]][moves[k]]

	if r["r"] == -1:
		print("You lose, {} {} by {}".format(playerChoice, r["t"], k))
	elif r["r"] == 1:
		print("You won, {} {} {}".format(playerChoice, r["t"], k))
	else:
		print("draw")
		
def play():
	ch = input("Choose\n 0 for paper,\n 1 for scissors,\n 2 for rock,\n 3 for lizard and\n 4 for Spock: ")
	sanitize(ch)
	playMe(list(moves.keys())[int(ch)])

def sanitize(ch):
	if not str.isnumeric(ch):
		raise Exception('Argument not a number', ch)
	if int(ch) < 0 or int (ch) > 4:
		raise Exception('Argument outside of accepted range 0 - 4', ch)

if __name__ == "__main__":
	play()