import sys
from math import sqrt, ceil, floor

def generate_data(f) -> dict:


	time = f.readline()
	time = time.split(":")[1].strip().split(" ")
	time = [el for el in time if el]

	distance = f.readline()
	distance = distance.split(":")[1].strip().split(" ")
	distance = [el for el in distance if el]

	timestr = ""
	diststr = ""

	for i in range(len(time)):

		timestr += time[i]
		diststr += distance[i]


	data = {int(timestr): int(diststr)}


	return data


def get_solution(data: dict) -> int:

	#the distance travelled is a function: f(x) = (time-x)*x
	#where x stands for the time you use winding up
	#
	#now, consider g(x) = (time-x)*x - dist
	#this function is positive only when f(x) >= dist
	#so, compute the points where g(x) hits zero, and compute the distance
	#between. 

	back = 1

	nulls = lambda t, d: [ceil((-t + sqrt(t*t - 4*d))/(-2)), ceil((-t - sqrt(t*t - 4*d))/(-2))]

	for key in data.keys():

		value = data[key]
		nullpoints = nulls(key, value)

		val = abs(nullpoints[1]-nullpoints[0])

		if (((key-nullpoints[1])*nullpoints[1]) == value) or (((key-nullpoints[0])*nullpoints[0]) == value):
			val -= 1
		back *= val




	return back




if __name__ == "__main__":

	path = sys.argv[1]

	with open(path, "r") as f:

		data = generate_data(f)
		solution = get_solution(data)

		print(solution)
