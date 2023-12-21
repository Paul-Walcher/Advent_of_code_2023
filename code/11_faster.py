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

def compute(a, b):

	#shortest path between two points:
	#go the smallest amount diagonally until you are on the same x or y axis as the endnode
	#from there go straight

	dx1, dx2, gx1, gx2 = 0, 0, 0, 0
	if (abs(a[0] - b[0]) < abs(a[1]-b[1])):

		#y distance was smaller
		dx1, dx2 = a[0], b[0]
		gx1, gx2 = a[1], b[1]
	else:

		dx1, dx2 = a[1], b[1]
		gx1, gx2 = a[0], b[0]

	diagonal = abs(dx1-dx2)-1
	straight = abs(gx1-gx2) - diagonal + 1

	return 2*diagonal + straight


if __name__ == "__main__":

	path = sys.argv[1]
	galaxy = []
	with open(path, "r") as f:
		galaxy = f.read().splitlines()

	galaxy = [[x for x in el] for el in galaxy]
	galaxy = expand_galaxy(galaxy)

	width, height = len(galaxy[0]), len(galaxy)



	#finding all galaxies in the cluster
	stars = []

	for y in range(height):

		for x in range(width):

			if (galaxy[y][x] == '#'):
				stars.append((y, x))

	total_sum = 0
				
	for i in range(len(stars)):
			
		for x in range(i+1, len(stars)):

			total_sum += compute(stars[i], stars[x])

	print(total_sum)

