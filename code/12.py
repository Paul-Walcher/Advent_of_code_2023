import sys



def format_lines(lines):

	back = []
	for line in lines:

		seq, ns = line.split(" ")

		ns = [int(el) for el in ns.split(",")]

		back.append([seq, ns])

	return back

	return steps

def possible(seq, numbers):

	#a sequence is possible when there is no # left
	
	lens = []
	lenc = 0
	for el in seq:

		if el == '.':
			if (lenc != 0):
				lens.append(lenc)
				lenc = 0
		if (el == '#'):
			lenc = lenc +1

	if (lenc != 0):
		lens.append(lenc)


	return (lens==numbers)

def all_possibilities(line):

	ps = []
	if (line[0] == '?'):
		ps = ['#', '.']
	else:
		ps.append(line[0])
	for i in range(1, len(line)):

		n = []
		for el in ps:

			if (line[i] == '?'):
				n.append(el+'#')
				n.append(el+'.')
			else:
				n.append(el+line[i])

		ps = n
	return ps






if __name__ == "__main__":

	path = sys.argv[1]

	lines = []
	with open(path, "r") as f:
		lines = f.read().splitlines()

	lines = format_lines(lines)

	total = 0
	for line in lines:

		X, N = line[0], line[1]

		s =  sum([possible(x, N) for x in all_possibilities(X)])

		print(X, N, s)

		total += s
	
	print(total)