import sys

def generate_map(f):

	text = [el.strip() for el in f.readlines()]
	
	seeds = text[0].split(":")[1][1:]
	seeds = list(int(el)for el in seeds.split(" ")) 

	seeds2 = []
	for x in range(int(len(seeds) / 2)):

		seeds2.append([seeds[x*2], seeds[x*2+1], False])

	seeds = seeds2
	
	i = 3
	maximum = len(text[2:]) + 2

	while (i < maximum):


		if not text[i]:

			for el in seeds:

				el[2] = False

			i += 2
			continue

		linesplits = text[i].split(" ")
		dest, src, length = int(linesplits[0]), int(linesplits[1]), int(linesplits[2])

		seeds2 = []

		for el in seeds:

			start, seedlength = el[0], el[1]

			#if the seeds were not transformed, and there is an overlap with transformation range
			if not el[2] and not (start+seedlength < src or start >= src+length):

				#transform
				leftpart = src-start
				rightpart = (start+seedlength) - (src+length)

				#if the seeds and its range begins before the transformation source, split this part away
				if leftpart > 0:

					seeds2.append([start, leftpart, False])

				#actual transformation
				tstart = max(src, start)
				tend = min(src+length, start+seedlength)

				seeds2.append([dest + tstart-src, tend-tstart, True])

				#split right part away
				if rightpart > 0:

					seeds2.append([src+length, rightpart, False])


			else:

				seeds2.append(el)

		seeds = seeds2
		

		i += 1


	return seeds


if __name__ == "__main__":

	path = sys.argv[1]

	with open(path, "r") as f:

		seeds = generate_map(f)

		print(min([el[0] for el in seeds]))