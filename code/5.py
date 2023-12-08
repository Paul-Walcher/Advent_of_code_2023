import sys

def generate_map(f) -> dict:

	text = [el.strip() for el in f.readlines()]
	
	seeds = text[0].split(":")[1][1:]
	seeds = list(int(el) for el in seeds.split(" "))

	
	i = 3
	maximum = len(text[2:]) + 2

	seeds_mapped = [False for i in range(len(seeds))]

	while (i < maximum):

		if not text[i]:
			seeds_mapped = [False for i in range(len(seeds))]
			i += 2
			continue

		linesplits = text[i].split(" ")
		dest, src, length = int(linesplits[0]), int(linesplits[1]), int(linesplits[2])

		for seedindex in range(len(seeds)):

			if seeds_mapped[seedindex]:
			seed = seeds[seedindex]

			if (seed >= src and seed < src+length):

				seeds[seedindex] = dest + (seed-src)
				seeds_mapped[seedindex] = True


		i += 1


	return seeds


if __name__ == "__main__":

	path = sys.argv[1]

	with open(path, "r") as f:

		seeds = generate_map(f)

		print(min(seeds))