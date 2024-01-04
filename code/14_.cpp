#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

struct grid_object{

	char type; //#, . or O

};


std::vector<std::vector<grid_object>> exctract_objects(std::vector<std::string>&);
void print(std::vector<std::vector<grid_object>>&);

void spin(std::vector<std::vector<grid_object>>&);
void tilt_north(std::vector<std::vector<grid_object>>&);
void tilt_west(std::vector<std::vector<grid_object>>&);
void tilt_south(std::vector<std::vector<grid_object>>&);
void tilt_east(std::vector<std::vector<grid_object>>&);

int compute_sum(std::vector<std::vector<grid_object>>&);
std::string get_state(std::vector<std::vector<grid_object>>&);
void construct_from_string(std::vector<std::vector<grid_object>>&, std::string&);

int main(int argc, char** argv){

	std::string path = argv[1];

	std::ifstream file(path);

	std::vector<std::string> matrix;

	for(std::string line; std::getline(file, line);){
		matrix.push_back(line);
	}

	file.close();

	std::vector<std::vector<grid_object>> objects = exctract_objects(matrix);

	spin(objects);

	std::cout << compute_sum(objects) << "\n";



	return 0;
}

std::vector<std::vector<grid_object>> exctract_objects(std::vector<std::string>& matrix){

	std::vector<std::vector<grid_object>> back;

	int rows = matrix.size(), columns = matrix[0].size();

	for(int i = 0; i < rows; i++){

		std::vector<grid_object> row;
		for(int j = 0; j < columns; j++){

			grid_object go = {(matrix[i][j])};
			row.push_back(go);
			
		}
		back.push_back(row);

	}

	return std::move(back);

}

void spin(std::vector<std::vector<grid_object>>& objects){

	std::vector<std::string> states;
	states.push_back(get_state(objects));

	for(int i = 0; i < static_cast<int>(1E9); i++){


		tilt_north(objects);
		tilt_west(objects);
		tilt_south(objects);
		tilt_east(objects);

		std::string after = get_state(objects);

		if (std::find(states.begin(), states.end(), after) != states.end()){
			
			//state found, now getting the remaining time and performing it modulo
			std::vector<std::string>::iterator it = std::find(states.begin(), states.end(), after);
			int remaining = std::distance(it, states.end());

			int pointer = ((static_cast<int>(1E9)-i) % remaining) - 1;
			construct_from_string(objects, *(it + pointer));
			break;

		}
		states.push_back(after);


	}


}

void tilt_north(std::vector<std::vector<grid_object>>& objects){


	int rows = objects.size(), columns = objects[0].size();

	for(int i = 0; i < columns; i++){

		//going down to up
		for(int j = 0; j < rows; j++){

			if (objects[j][i].type != 'O'){
				continue;
			}


			int k = j;
			while((k-1 >= 0 && objects[k-1][i].type == '.')){
				k--;
			}
			//set to new place
			if (k != j){//object was moved
				objects[k][i].type = objects[j][i].type;

				objects[j][i].type = '.';

			}
			//if it hit a changable:

		}

	}


}

void tilt_west(std::vector<std::vector<grid_object>>& objects){


	int rows = objects.size(), columns = objects[0].size();

	for(int i = 0; i < rows; i++){

		//going down to up
		for(int j = 0; j < columns; j++){

			if (objects[i][j].type != 'O'){
				continue;
			}



			int k = j;
			while((k-1 >= 0 && objects[i][k-1].type == '.')){
				k--;
			}
			//set to new place
			if (k != j){//object was moved
				objects[i][k].type = objects[i][j].type;

				objects[i][j].type = '.';

			}

		}

	}


}

void tilt_south(std::vector<std::vector<grid_object>>& objects){


	int rows = objects.size(), columns = objects[0].size();

	for(int i = 0; i < columns; i++){

		//going down to up
		for(int j = rows-1; j >= 0; j--){

			if (objects[j][i].type != 'O'){
				continue;
			}

			int k = j;
			while((k < rows-1 && objects[k+1][i].type == '.')){
				k++;
			}
			//set to new place
			if (k != j){//object was moved
				objects[k][i].type = objects[j][i].type;

				objects[j][i].type = '.';

			}

		}

	}


}

void tilt_east(std::vector<std::vector<grid_object>>& objects){


	int rows = objects.size(), columns = objects[0].size();

	for(int i = 0; i < rows; i++){

		//going down to up
		for(int j = columns-1; j >= 0; j--){

			if (objects[i][j].type != 'O'){
				continue;
			}

			int k = j;
			while((k+1 < columns && objects[i][k+1].type == '.')){
				k++;
			}
			//set to new place
			if (k != j){//object was moved
				objects[i][k].type = objects[i][j].type;
				objects[i][j].type = '.';
			}

		}

	}


}

void print(std::vector<std::vector<grid_object>>& vec){

	for(std::vector<grid_object>& v2 : vec){

		for(grid_object& obj : v2){

			std::cout << obj.type;

		}
		std::cout << std::endl;

	}

}

int compute_sum(std::vector<std::vector<grid_object>>& objects){

	int summe = 0;
	int rows = objects.size(), columns = objects[0].size();

	for(int i = 0; i < rows; i++){

		for(int j = 0; j < columns; j++){

			if(objects[i][j].type == 'O'){
				summe += (rows-i);
			}

		}

	}
	return summe;

}
std::string get_state(std::vector<std::vector<grid_object>>& objects){

	std::string back;

	for(std::vector<grid_object>& obj_vec : objects){
		for(grid_object& obj : obj_vec){
			back += obj.type;
		}
	}
	return std::move(back);

}

void construct_from_string(std::vector<std::vector<grid_object>>& objects, std::string& s){

	int counter = 0;

	for(std::vector<grid_object>& obj_vec : objects){
		for (grid_object& obj : obj_vec){

			obj.type = s[counter++];

		}
	}

}