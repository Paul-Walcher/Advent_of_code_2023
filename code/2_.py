import sys

possible_colors = {
	
					'red': 12,
					'green': 13,
					'blue': 14
					}


def deconstruct_line(line: str) -> tuple:

	#returns (ID, {R, G, B})
	game, rest = line.split(":")
	ID = int(game.split(" ")[1])

	draw_list = []

	colors = {"red":0, "green":0, "blue":0}

	for draws in rest.split(";"):

		results = {}
		
		for el in draws.split(","):
			el = el[1:]
			value, key = el.split(" ")
			value, key = value.strip(), key.strip()
			intval = int(value)

			if (intval > colors[key]):
				colors[key] = intval 
			
	return colors["red"] * colors["green"] * colors["blue"]



if __name__ == "__main__":

	path = sys.argv[1]

	summe: int = 0
	with open(path, "r") as f:

		for line in f.readlines():
			linesum = deconstruct_line(line)
			summe += linesum

	print(summe)


