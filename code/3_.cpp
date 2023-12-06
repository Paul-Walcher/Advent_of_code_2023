#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>



static char** matrix;
static int dimension = -1;
static std::map<int, std::vector<int>> nmap;//for each symbol this contains the numbers adjacent to each symbol

long int calculate_sum();
bool hits_symbol(int xstart, int ystart, int len);
std::vector<int> symbols_hit(int startx, int starty, int len);
bool is_symbol(int x, int y);


void  generate_map();


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


void generate_map(){

    for(int i = 0; i < dimension; i++){
        for(int x = 0; x < dimension; x++){

            std::vector<int> temp;
            nmap[i*dimension + x] = temp;

        }
    }


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
            if(len > 0) {
                long int n = static_cast<long int>(std::stoi(number));
                std::vector<int> hitsyms = symbols_hit(startx, starty, len);
                for(int el : hitsyms){
                    nmap[el].push_back(n);
                }

            }


            x++;

        }
    }


}

long int calculate_sum(){

    long int summe = 0L;

    generate_map();

    for(auto& el : nmap){
        
        std::vector<int> hits = el.second;
        if (hits.size() == 2){
            summe += hits[0]*hits[1];
        }

    }


    return summe;

}

std::vector<int> symbols_hit(int startx, int starty, int len){

    std::vector<int> back;

    for(int i = startx-1; i < startx+len+1; i++){
        if (is_symbol(i, starty-1)) back.push_back((starty-1)*dimension+i);
        if(is_symbol(i, starty+1)) back.push_back((starty+1)*dimension+i);
    }


    if (is_symbol(startx-1, starty)) back.push_back((starty)*dimension+startx-1);
    if (is_symbol(startx+len, starty)) back.push_back((starty)*dimension+startx+len);

    return std::move(back);

}

bool hits_symbol(int startx, int starty, int len){

    if (is_symbol(startx-1, starty-1) || is_symbol(startx-1, starty+1) || is_symbol(startx+len, starty-1) || is_symbol(startx+len, starty+1)
        || is_symbol(startx-1, starty) || is_symbol(startx+len, starty)) return true;
    for(int x = startx; x < startx+len; x++){
        if (is_symbol(x, starty-1) || is_symbol(x, starty+1)) return true;
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
