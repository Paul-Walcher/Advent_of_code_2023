import sys

def nextline(line):

	return [line[i+1] - line[i] for i in range(len(line)-1)]

def full_history(line):

	if(all([n == 0 for n in line])):
		return 0

	return line[-1] + full_history(nextline(line))



if __name__ == "__main__":

	path = sys.argv[1]

	inputs = []

	with open(path, "r") as file:

		inputs = file.read().splitlines()

	inputs = [[int(x) for x in el.split(" ")] for el in inputs]	
	
	fullsum = 0

	for el in inputs:

		fullsum += full_history(el)
		



	print(fullsum)