#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int move_and_sum_rocks(std::vector<std::string>& matrix);

int main(int argc, char** argv){

	std::string path = argv[1];

	std::ifstream file(path);

	std::vector<std::string> matrix;

	for(std::string line; std::getline(file, line);){
		matrix.push_back(line);
	}

	file.close();

	int summe = move_and_sum_rocks(matrix);
	std::cout << summe << "\n";


	return 0;
}

int move_and_sum_rocks(std::vector<std::string>& matrix){

	if(matrix.size() == 0) return 0;

	int summe = 0;

	int columns = matrix[0].size();
	int rows = matrix.size();

	//iterating over all columns
	for(int i = 0; i < columns; i++){

		int lastindex = 0;

		//going from top to bottom
		for(int j = 0; j < rows; j++){

			switch(matrix[j][i]){

			case 'O': 	{
							summe += (rows-lastindex);
							lastindex++;
							break;
						}
			case '#': 	{
							lastindex = j+1;
							break;
						}

			}

		}

	}
	return summe;

}