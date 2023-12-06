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

	for draws in rest.split(";"):

		results = {}
		
		for el in draws.split(","):
			el = el[1:]
			value, key = el.split(" ")
			value, key = value.strip(), key.strip()
			results[key] = int(value)
			
	return (ID, draw_list)



if __name__ == "__main__":

	path = sys.argv[1]

	summe: int = 0
	with open(path, "r") as f:

		for line in f.readlines():
			ID, tries = deconstruct_line(line)

			possible = True

			for el in tries:

				for key in el.keys():

					if el[key] > possible_colors[key]:
						possible = False
						break

				if not possible:
					break

			if possible:

				summe += ID

	print(summe)


