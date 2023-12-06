#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>


static char** matrix;
static int dimension = -1;

long int calculate_sum();
bool hits_symbol(int xstart, int ystart, int len);
bool is_symbol(int x, int y);


int main(int argc, char** argv){

    std::string path = argv[1];

    std::ifstream f(path);
    std::stringstream stream;

    int counter = 0;

    for(std::string line; std::getline(f, line);){

        if (dimension == -1){
            dimension = line.size();
            matrix = new char*[dimension];
            for(int i = 0; i < dimension; i++){
                matrix[i] = new char[dimension];
            }
        }

        for(int i = 0; i < line.size(); i++) matrix[counter][i] = line[i];
        ++counter;
    }


    f.close();

    long int back = calculate_sum();

    std::cout << static_cast<int>(back) << "\n";



    for(int i = 0; i < dimension; i++) delete [] matrix[i];
    delete [] matrix;

    return 0;
}



long int calculate_sum(){

    long int summe = 0L;

    for(int y = 0; y < dimension; y++){
        int x = 0;
        while(x < dimension){

            std::string number;
            char sym = matrix[y][x];
            int startx = x, starty = y;

            while((sym >= '0' && sym <= '9') && x < dimension){

                number += sym;
                x++;
                sym = matrix[y][x];

            }

            int len = number.size();
            if(len > 0 && hits_symbol(startx, starty, len)) {
                long int n = static_cast<long int>(std::stoi(number));
                summe += n;
            }


            x++;

        }
    }

    return summe;

}

bool hits_symbol(int startx, int starty, int len){

    if (is_symbol(startx-1, starty-1) || is_symbol(startx-1, starty+1) || is_symbol(startx+len, starty-1) || is_symbol(startx+len, starty+1)) return true;
    for(int x = startx; x < startx+len; x++){
        if (is_symbol(x-1, starty) || is_symbol(x+1, starty) || is_symbol(x, starty-1) || is_symbol(x, starty+1)) return true;
    }
    return false;
}

bool is_symbol(int x, int y){

    if (x < 0 || x >= dimension) return false;
    if(y < 0 || y >= dimension) return false;

    char sym = matrix[y][x];

    if(sym != '.' && (sym < '0' || sym > '9')){
        return true;
    }
    return false;

}
