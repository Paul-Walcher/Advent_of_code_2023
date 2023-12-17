import sys

def expand_galaxy(galaxy: list) -> tuple:

	row_indices = []
	for i in range(len(galaxy)):

		if all([el == '.' for el in galaxy[i]]):
			row_indices.append(i)
	
	column_indices = []

	for i in range(len(galaxy[0])):

		if all([galaxy[x][i] == '.' for x in range(len(galaxy))]):
			column_indices.append(i)


	
	return row_indices, column_indices

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
	expand_rows, expand_columns = expand_galaxy(galaxy)

	width, height = len(galaxy[0]), len(galaxy)

	expand_factor = 1000000-1

	#finding all galaxies in the cluster
	stars = []

	for y in range(height):

		for x in range(width):

			if (galaxy[y][x] == '#'):
				stars.append((y, x))

	total_sum = 0
				
	for i in range(len(stars)):
			
		for x in range(i+1, len(stars)):

			X, Y = stars[i], stars[x]
			#check how many expanded rows there are between X and Y,
			#and how many columns there are
			difference_x = abs(X[1]-Y[1])
			difference_y = abs(X[0]-Y[0])

			starty = min(Y[0], X[0])
			startx = min(Y[1], X[1])

			#checking for rows and columns
			rows_to_expand = 0
			columns_to_expand = 0

			for t in range(startx+1, startx+difference_x):
				if (t in expand_columns):
					columns_to_expand += 1

			for t in range(starty+1, starty+difference_y):
				if (t in expand_rows):
					rows_to_expand += 1


			#now adding the difference
			if (X[0] < Y[0]):

				Y = (Y[0]+rows_to_expand*expand_factor, Y[1])
			else:

				X = (X[0]+rows_to_expand*expand_factor, X[1])

			if (X[1] < Y[1]):

				Y = (Y[0], Y[1]+columns_to_expand*expand_factor)
			else:
				X = (X[0], X[1]+columns_to_expand*expand_factor)

			total_sum += compute(X, Y)

	print(total_sum)

