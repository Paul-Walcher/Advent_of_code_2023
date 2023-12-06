import sys

def compute_value(line):
	
	first, second = line.split("|")
	first = first.split(":")[1][1:]
	second = second.strip()

	winners = set(int(el) for el in first.split(" ") if el != "")
	guesses = set(int(el) for el in second.split(" ") if el != "")
	
	correct = len(winners.intersection(guesses))
	
	if (correct > 0):

		return (0x1 << (correct-1))

	else:
		return 0
	
	

if __name__ == "__main__":

	path = sys.argv[1]

	with open(path, "r") as f:

		summe = 0

		for line in f.readlines():

			summe += compute_value(line)

		print(summe)