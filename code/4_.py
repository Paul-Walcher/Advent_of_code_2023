import sys
from collections import deque

def compute_value(line, queue):
	
	first, second = line.split("|")
	first = first.split(":")[1][1:]
	second = second.strip()

	winners = set(int(el) for el in first.split(" ") if el != "")
	guesses = set(int(el) for el in second.split(" ") if el != "")
	
	correct = len(winners.intersection(guesses))
	
	own_times = queue.popleft()
	queue.append(1)
	for i in range(correct):

		queue[i] += own_times

	return own_times
	
	

if __name__ == "__main__":

	path = sys.argv[1]

	queue = deque((1 for i in range(20)))

	with open(path, "r") as f:

		summe = 0

		for line in f.readlines():

			summe += compute_value(line, queue)

		print(summe)