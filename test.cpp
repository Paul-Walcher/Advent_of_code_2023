#include <iostream>
#include <string>

void print(int** matrix, int size);

int main(int argc, char** argv){

    std::string size = argv[1];
    int mdim = std::stoi(size);

    int** matrix = new int*[mdim];
    for(int i = 0; i < mdim; i++) matrix[i] = new int[mdim];

    for(int x = 0; x < mdim; x++){
        for(int y = 0; y < mdim; y++){
            matrix[x][y] = 1;
        }
    }

    print(matrix, mdim);

    for(int i = 0; i < mdim; i++) delete [] matrix[i];
    delete [] matrix;

    return 0;
}

void print(int** matrix, int size){

    for(int x = 0; x < size; x++){
        for(int y = 0; y < size; y++){
            std::cout << matrix[x][y] << " ";
        }
        std::cout << "\n";
    }

}