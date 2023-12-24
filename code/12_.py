import sys

def rework(problems):

	back = []

	for problem in problems:

		string, numbers = problem.split(" ")
		sstring = string
		for t in range(4):
			string += "?" + sstring
		back.append([string, [int(el) for el in numbers.split(",")]*5])

	return back

def positions(string, sindex, n):#gives back all possible positions starting from sindex to place down n

	hashpos = sindex
	while(hashpos < len(string) and string[hashpos] != '#'):
		hashpos += 1
	#found the position of the first #

	back = []

	for i in range(sindex, hashpos+1): #going through all possible positions

		if (i + n > len(string)):
			continue

		if (i-1 >= 0 and string[i-1] == '#'):
			continue
			
		if (i+n < len(string) and string[i+n] == '#'):
			continue

		if (any([string[x] == '.' for x in range(i, i+n)])):
			continue

		back.append(i)

	return back



def combinations(string, numbers, sindex, nindex, memo):

	if (sindex, nindex) in memo:

		return memo[(sindex, nindex)]

	if (nindex >= len(numbers)):#all numbers placed

		if (sindex < len(string) and '#' in string[sindex:]):# is left over, should be impossible
			return 0
		else:
			return 1

	if (sindex >= len(string)): #we reached the end without placing down all numbers
		return 0

	n = numbers[nindex]

	positions_n = positions(string, sindex, n)

	total = 0
	for pos in positions_n:

		if (pos+n+1, nindex+1) in memo:

			total += memo[(pos+n+1, nindex+1)]
		else:

			back = combinations(string, numbers, pos+n+1, nindex+1, memo)
			memo[(pos+n+1, nindex+1)] = back

			total += back

	memo[(sindex, nindex)] = total

	return total 


if __name__ == "__main__":

	path = sys.argv[1]

	problems = []

	with open(path, "r") as f:

		problems = f.read().splitlines()

	problems = rework(problems)

	total = 0
	
	for problem in problems:

		string, numbers = problem[0], problem[1]

		c = combinations(string, numbers, 0, 0, {})
		#print(string, numbers, c)
		total += c


	print(total)

