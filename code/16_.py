import sys

class Direction:

	LEFT = 0
	RIGHT = 1
	UP = 2
	DOWN = 3

	#numbers for indexing in the DP array in compute_lit_matrix

class Ray:

	def __init__(self, x, y, direction):

		self.x = x
		self.y = y
		self.direction = direction

	def step(self, matrix: list) -> list:#returns a list of rays coming back
		
		back = []

		width, height = len(matrix[0]), len(matrix)
		next_x, next_y = self.x, self.y

		if(self.direction == Direction.RIGHT):

			next_x += 1

		elif (self.direction == Direction.LEFT):

			next_x -= 1

		elif (self.direction == Direction.UP):

			next_y -= 1

		elif (self.direction == Direction.DOWN):

			next_y += 1

		#now the next position is determined.

		#checking if we're stepping out of bounds
		if (next_x < 0 or next_x >= width or next_y < 0 or next_y >= height):

			return back

		#if not out of bounds, get the next action
		field: str = matrix[next_y][next_x]
		self.x = next_x
		self.y = next_y

		if (field == '.'):

			#nothing to be done
			back.append(self)

		elif (field == '|'):


			back.append(self)

			if (self.direction == Direction.LEFT or self.direction == Direction.RIGHT):

				self.direction = Direction.UP
				splitray: Ray = Ray(self.x, self.y, Direction.DOWN)
				back.append(splitray)


		elif (field == '-'):

			back.append(self)

			if (self.direction == Direction.UP or self.direction == Direction.DOWN):

				self.direction = Direction.RIGHT
				splitray: Ray = Ray(self.x, self.y, Direction.LEFT)
				back.append(splitray)

		elif (field == '\\'):

			#changing direction
			if(self.direction == Direction.RIGHT):

				self.direction = Direction.DOWN

			elif(self.direction == Direction.LEFT):

				self.direction = Direction.UP

			elif(self.direction == Direction.UP):

				self.direction = Direction.LEFT

			elif(self.direction == Direction.DOWN):

				self.direction = Direction.RIGHT

			back.append(self)



		elif (field == '/'):

			#changing direction
			if(self.direction == Direction.RIGHT):

				self.direction = Direction.UP

			elif(self.direction == Direction.LEFT):

				self.direction = Direction.DOWN

			elif(self.direction == Direction.UP):

				self.direction = Direction.RIGHT

			elif(self.direction == Direction.DOWN):

				self.direction = Direction.LEFT

			back.append(self)


		return back


def load_matrix(path: str):

	#loads the input matrix
	matrix = []
	with open(path, "r") as f:

		matrix = f.read().splitlines()

	for i in range(len(matrix)):

		matrix[i] = [el for el in matrix[i]]	

	return matrix

def compute_lit_matrix(matrix: list, startrays: list) -> list:

	height, width = len(matrix), len(matrix[0])

	lit_matrix = [[False for j in range(len(matrix[i]))] for i in range(len(matrix))]

	DP = [[[False for k in range(4)] for j in range(len(matrix[i]))] for i in range(len(matrix))]#list to keep track of rays having similar trajectories
	
	current_rays = [] #queue to keep track of all rays

	current_rays.extend(startrays) #adding the startrays

	while (len(current_rays)): #as long as rays exist

		raycp = []

		for ray in current_rays:

			#light up current position
			lit_matrix[ray.y][ray.x] = True

			#mark encountered state
			DP[ray.y][ray.x][ray.direction] = True

			#do ray step
			rays_back = ray.step(matrix)

			#now checking if all rays gotten back can be safely added
			for ray_ in rays_back:

				#if ray stepped out of bounds stop
				if (ray_.x < 0 or ray_.x >= width or ray_.y < 0 or ray_.y >= height):
					continue

				#check if similar ray was cast a while ago
				if (DP[ray_.y][ray_.x][ray_.direction]):
					continue

				raycp.append(ray_)

		current_rays = raycp

	return lit_matrix


def print_lit(lit_matrix):

	for i in range(len(lit_matrix)):

		for j in range(len(lit_matrix[i])):

			sign = ('#' if lit_matrix[i][j] else '.')

			print(sign, end="")
		print()

def sum_up(lit_matrix: list):

	summe: int = 0

	for i in range(len(lit_matrix)):

		for j in range(len(lit_matrix[i])):

			if lit_matrix[i][j]:

				summe += 1

	return summe

def get_maxray(matrix: list) -> int:

	width, height = len(matrix[0]), len(matrix)
	maxval: int = -1

	#starting top row
	for x in range(width):

		#computing initial direction
		initial_direction = Direction.DOWN
		
		field: str = matrix[0][x]

		rays = []

		if (field == "\\"):

			initial_direction = Direction.RIGHT

		elif (field == '-'):

			initial_direction = Direction.RIGHT
			rays.append(Ray(x, 0, Direction.LEFT))

		elif (field == '/'):

			initial_direction = Direction.LEFT

		ray: Ray = Ray(x, 0, initial_direction)
		rays.append(ray)

		achieved: int = sum_up(compute_lit_matrix(matrix, rays))
		if(achieved > maxval):

			maxval = achieved

	#starting bottom row
	for x in range(width):

		#computing initial direction
		initial_direction = Direction.UP
		
		field: str = matrix[height-1][x]

		rays = []

		if (field == "\\"):

			initial_direction = Direction.LEFT

		elif (field == '-'):

			initial_direction = Direction.RIGHT
			rays.append(Ray(x, height-1, Direction.LEFT))

		elif (field == '/'):

			initial_direction = Direction.RIGHT

		ray: Ray = Ray(x, height-1, initial_direction)
		rays.append(ray)

		achieved: int = sum_up(compute_lit_matrix(matrix, rays))
		if(achieved > maxval):

			maxval = achieved

	#starting left column
	for y in range(height):

		#computing initial direction
		initial_direction = Direction.RIGHT
		
		field: str = matrix[y][0]

		rays = []

		if (field == "\\"):

			initial_direction = Direction.DOWN

		elif (field == '|'):

			initial_direction = Direction.UP
			rays.append(Ray(0, y, Direction.DOWN))

		elif (field == '/'):

			initial_direction = Direction.UP

		ray: Ray = Ray(0, y, initial_direction)
		rays.append(ray)

		achieved: int = sum_up(compute_lit_matrix(matrix, rays))
		if(achieved > maxval):

			maxval = achieved

	#starting right column
	for y in range(height):

		#computing initial direction
		initial_direction = Direction.LEFT
		
		field: str = matrix[y][width-1]

		rays = []

		if (field == "\\"):

			initial_direction = Direction.UP

		elif (field == '|'):

			initial_direction = Direction.UP
			rays.append(Ray(width-1, y, Direction.DOWN))

		elif (field == '/'):

			initial_direction = Direction.DOWN

		ray: Ray = Ray(width-1, y, initial_direction)
		rays.append(ray)

		achieved: int = sum_up(compute_lit_matrix(matrix, rays))
		if(achieved > maxval):

			maxval = achieved

	return maxval



if __name__ == "__main__":

	path = sys.argv[1]

	matrix = load_matrix(path)

	print(get_maxray(matrix))