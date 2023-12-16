#include <iostream>
#include <fstream>
#include <string>
#include <tuple>
#include <cstring>
#include <vector>
#include <cmath>

enum direction{
	LEFT,
	RIGHT,
	UP,
	DOWN
};

struct Point{

	int x;
	int y;

	direction d; //the point is facing

	bool operator==(Point& other){
		return (x == other.x && y == other.y);
	}
	bool operator!=(Point& other){
		return !((*this) == other);
	}
};

void map_point(Point& p, char c){

	switch(c){

	case '.': break;
	case '-': 	{
					if (p.d == direction::LEFT) p.x -= 1;
					else if (p.d == direction::RIGHT) p.x += 1;
					break;
				}
	case '|':	{
					if(p.d == direction::UP) p.y -= 1;
					else if(p.d == direction::DOWN) p.y += 1;
					break;
				}
	case 'F':	{
					if(p.d == direction::UP) {p.x += 1; p.d = direction::RIGHT;}
					else if(p.d == direction::LEFT) {p.y += 1; p.d = direction::DOWN;}
					break;
				}
	case '7':	{
					if(p.d == direction::RIGHT) {p.y += 1; p.d = direction::DOWN;}
					else if(p.d == direction::UP) {p.x -= 1; p.d = direction::LEFT;}
					break;
				}
	case 'J':	{
					if(p.d == direction::RIGHT) {p.y -= 1;p.d = direction::UP;}
					else if(p.d == direction::DOWN) {p.x -= 1; p.d = direction::LEFT;}
					break;
				}
	case 'L':	{
					if(p.d == direction::DOWN) {p.x += 1; p.d = direction::RIGHT;}
					else if(p.d == direction::LEFT) {p.y -= 1; p.d = direction::UP;}
					break;
				}


	}

}




std::tuple<char**, int, int> get_matrix(std::string&);//tuple<matrix, height, width>
void delete_matrix(std::tuple<char**, int, int>&);

int traverse(char**, int, int);
bool all_equal(std::vector<Point>& vec){
	
	for(int i = 0; i < vec.size()-1; i++){
		if (vec[i] != vec[i+1]) return false;
	}
	return true;
}

Point find_startpoint(char**, int, int);
std::vector<Point> find_branchpoints(Point& S, char**, int, int);

int main(int argc, char** argv){

	std::string path = argv[1];

	std::tuple<char**, int, int> data = get_matrix(path);

	char** matrix = std::get<0>(data);
	int height = std::get<1>(data), width = std::get<2>(data);

	int needed_steps = traverse(matrix, height, width);

	std::cout << needed_steps << std::endl;

	delete_matrix(data);

	return 0;
}

std::tuple<char**, int, int> get_matrix(std::string& path){

	char** matrix = nullptr;
	int width=0, height=0;

	std::ifstream file(path);


	for(std::string line; std::getline(file, line);){
		width = line.size();
		height++;
	}

	file.close();

	matrix = new char*[height];
	for(int i = 0; i < height; i++){
		matrix[i] = new char[width+1];
	}

	std::ifstream file2(path);

	int counter = 0;

	for(std::string line; std::getline(file2, line);){

		strcpy(matrix[counter++], line.c_str());

	}
	file2.close();


	file.close();
	std::tuple<char**, int, int> back{matrix, height, width};
	return std::move(back);
}

void delete_matrix(std::tuple<char**, int, int>& data){

	int height = std::get<1>(data);
	char** matrix = std::get<0>(data);

	for(int i = 0; i < 0; i++) delete [] matrix[i];
	delete [] matrix;

}

int traverse(char** matrix, int height, int width){

	Point S = find_startpoint(matrix, height, width);

	std::vector<Point> branches = find_branchpoints(S, matrix, height, width);

	Point s = branches[0];

	int steps = 0;

	while (s != S){
		map_point(s, matrix[s.y][s.x]);
		steps++;
	}


	


	return static_cast<int>(std::ceil(static_cast<float>(steps) / 2));
}

Point find_startpoint(char** matrix, int height, int width){

	Point p;

	for(int y = 0; y < height; y++){
		for(int x = 0; x < width; x++){
			if (matrix[y][x] == 'S'){

				p.x = x;
				p.y = y;
				return std::move(p);

			}
		}
	}

	return std::move(p);

}

std::vector<Point> find_branchpoints(Point& S, char** matrix, int height, int width){

	std::vector<Point> back;

	if (S.x > 0 && (matrix[S.y][S.x-1] == '-' || matrix[S.y][S.x-1] == 'L') || matrix[S.y][S.x-1] == 'F'){


		Point p;
		p.x = S.x-1;
		p.y = S.y;
		p.d = direction::LEFT;
		back.push_back(p);
	}
	if (S.x < width-1 && (matrix[S.y][S.x+1] == '-' || matrix[S.y][S.x+1] == '7' || matrix[S.y][S.x+1] == 'J')){


		Point p;
		p.x = S.x+1;
		p.y = S.y;
		p.d = direction::RIGHT;
		back.push_back(p);
	}
	if (S.y > 0 && (matrix[S.y-1][S.x] == '|' || matrix[S.y-1][S.x] == 'F' || matrix[S.y-1][S.x] == '7')){


		Point p;
		p.x = S.x;
		p.y = S.y-1;
		p.d = direction::UP;
		back.push_back(p);
	}
	if (S.y < height-1 && (matrix[S.y+1][S.x] == '|' || matrix[S.y+1][S.x] == 'J' || matrix[S.y+1][S.x] == 'L')){


		Point p;
		p.x = S.x;
		p.y = S.y+1;
		p.d = direction::DOWN;
		back.push_back(p);
	}


	return std::move(back);

}