import sys
from math import gcd
from functools import reduce
from itertools import product


def follow_instructions(node, instructions, maps):

	for el in instructions:
		node = maps[node][el]
	return node

def lcm(a, b):

	return a*b // gcd(a, b)

if __name__ == "__main__":

	filename = sys.argv[1]
	lines = []
	maps = {}

	with open(filename, "r") as f:
		lines = f.read().splitlines()
	instructions = lines[0]

	for el in lines[2:]:
		el = el.split(" ")
		maps[el[0]] = {"L": el[2][1:-1], "R":el[3][:-1]}

	startnodes = [el for el in maps.keys() if el[-1]=="A"]
	
	steps = 0
	inslen = len(instructions)

	steps_used = {el : {} for el in startnodes}

	scp = [el for el in startnodes]

	while startnodes:

		steps += inslen

		second = []
		counter = -1
		for i in range(len(startnodes)):
			counter += 1

			snode = follow_instructions(startnodes[i], instructions, maps)

			if (snode[-1] == "Z"):

				if snode in steps_used[scp[i]].keys():
					scp.pop(counter)
					continue
				steps_used[scp[i]][snode] = steps
			
			second.append(snode)


		startnodes = second


	cycles = []
	for el in steps_used.values():

		cycles.append(list(el.values()))
	
	minval = -1

	endlist = [[el] for el in cycles[0]]

	print(endlist)

	for i in range(len(cycles)-1):

		nlist = []

		for el in cycles[i+1]:
			
			for l in endlist.copy():


				l.append(el)
				nlist.append(l)

		endlist = nlist

	for el in endlist:

		minv = reduce(lcm, el)
		if (minval == -1 or minv < minval):
			minval = minv

	print(minv)





