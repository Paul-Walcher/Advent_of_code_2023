import sys

def expand_galaxy(galaxy: list) -> list:

	row_indices = []
	for i in range(len(galaxy)):

		if all([el == '.' for el in galaxy[i]]):
			row_indices.append(i)
	
	column_indices = []

	for i in range(len(galaxy[0])):

		if all([galaxy[x][i] == '.' for x in range(len(galaxy))]):
			column_indices.append(i)

	points = ['.' for x in range(len(galaxy[0]) + len(column_indices))]
	
	new_galaxy = []
	for y in range(len(galaxy)):
		if (y in row_indices):
			new_galaxy.append(points.copy())
		liste = []
		for x in range(len(galaxy[0])):
	 		if x in column_indices:
	 			liste.append(galaxy[y][x])
	 			liste.append('.')
	 		else:
	 			liste.append(galaxy[y][x])
		new_galaxy.append(liste)


	
	return new_galaxy

class Vertex:

	def __init__(self, y, x):
		self.x = x
		self.y = y
		self.neighbors = []#in pairs of: (neighbor, distance)

	def __str__(self):
		return str(self.y) + " " + str(self.x)
#A* algorithm

#meta heuristic
def H(v1: Vertex):

	return (lambda v2: (abs(v2.y - v1.y) + abs(v2.x - v1.x)))

def reconstruct_path(came_from: dict, current: Vertex):
	
	path = []
	while current in came_from.keys():
		path.append(current)
		current = came_from[current]
	return path[::-1]


def get_lowest_fscore(open_nodes: list, fscore: dict):

	lowest = sys.maxsize
	minnode = None

	for node in open_nodes:

		if (fscore[node] < lowest):

			lowest = fscore[node]
			minnode = node
	return minnode

def Astar(startnode: Vertex, endnode: Vertex, vertices: list):

	h = H(endnode) #getting the heuristic specifically for the endnode


	open_nodes = [startnode]
	came_from = {}

	gscore = {el : sys.maxsize for el in vertices.values()}
	fscore = {el : sys.maxsize for el in vertices.values()}

	gscore[startnode] = 0
	fscore[startnode] = h(startnode)

	while (len(open_nodes) > 0):


		current = get_lowest_fscore(open_nodes, fscore)
		open_nodes.remove(current)


		if current == endnode:

			return (reconstruct_path(came_from, current), gscore[current])

		for neighbor in current.neighbors:

			tgscore = gscore[current] + neighbor[1]
			if (tgscore < gscore[neighbor[0]]):

				came_from[neighbor[0]] = current
				gscore[neighbor[0]] = tgscore
				fscore[neighbor[0]] = tgscore + h(neighbor[0])

				if(neighbor[0] not in open_nodes):
					open_nodes.append(neighbor[0])
	return None


if __name__ == "__main__":

	path = sys.argv[1]
	galaxy = []
	with open(path, "r") as f:
		galaxy = f.read().splitlines()

	galaxy = [[x for x in el] for el in galaxy]
	galaxy = expand_galaxy(galaxy)

	width, height = len(galaxy[0]), len(galaxy)
	vertices = {(y, x) : Vertex(y, x) for y in range(height) for x in range(width)}



	for key in vertices:

		node = vertices[key]


		for y_ in range(-1, 2, 1):
			for x_ in range(-1,2, 1):

				if (y_ == x_ or (x_ == -1 and y_ == 1) or (y_ == -1 and x_ == 1)):
					continue

				ypos, xpos = key[0]+y_, key[1]+x_

				if (xpos >= 0 and xpos < width and ypos >= 0 and ypos < height):

					nn = vertices[(ypos, xpos)]
					node.neighbors.append((nn, 1))


	#finding all galaxies in the cluster
	stars = []

	for y in range(height):

		for x in range(width):

			if (galaxy[y][x] == '#'):
				stars.append((y, x))

	total_sum = 0
				
	for i in range(len(stars)):
			
		for x in range(i+1, len(stars)):

			total_sum += Astar(vertices[stars[i]], vertices[stars[x]], vertices)[1]

	print(total_sum)
