#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

struct Placeholder{

    size_t pos;
    int len;
    const std::string* with;

};

void preprocess(std::string&);
int getnum(std::string&);

void replace_all(std::string&, const std::string&, const std::string&, std::vector<Placeholder>&);
static std::map<std::string, std::string> nmap = {

    {"one", "1"},
    {"two", "2"},
    {"three", "3"},
    {"four", "4"},
    {"five", "5"}, 
    {"six", "6"},
    {"seven", "7"},
    {"eight", "8"},
    {"nine", "9"}

};

int main(int argc, char** argv){

    std::string path = argv[1];

    std::fstream f(path);

    long int summe = 0L;

    for(std::string line; std::getline(f, line);){

        preprocess(line);
        int n = getnum(line);
        summe += n;

    }

    f.close();

    std::cout << summe << "\n";

    return 0;
}

int getnum(std::string& line){

    std::string number;

    //forward
    std::string::iterator pos = line.begin();

    while(pos != line.end()){


        if (*pos >= '0' && *pos <= '9'){
            number += *pos;
            break;
        }

        pos++;
    }
    pos = line.end()-1;
    while(pos != line.begin()-1){



        if (*pos >= '0' && *pos <= '9'){
            number += *pos;
            break;
        }

        pos--;

    }

    //backward
    int back = 0;
    try{
        back = std::stoi(number);
    }
    catch(...){}


    return back;

}

void preprocess(std::string& line){

    std::vector<Placeholder> vec;

    for(auto& el: nmap){
        replace_all(line, el.first, el.second, vec);
    }

    std::sort(vec.begin(), vec.end(), [&](Placeholder& a, Placeholder& b){return a.pos < b.pos;});

    while(vec.size() > 0){

        Placeholder first = vec[0];
        std::vector<int> to_erase;
        for(int i = 1; i < vec.size(); i++){
            if(vec[i].pos >= first.pos && vec[i].pos <= first.pos + first.len){
                to_erase.push_back(i);
            }
        }

        for(int i : to_erase){
            vec.erase(vec.begin() + i);
        }
        vec.erase(vec.begin());

        line.replace(first.pos, first.len, (*first.with));

    }

}

void replace_all(std::string& line, const std::string& from, const std::string& to, std::vector<Placeholder>& vec){

    size_t found = 0;
    while((found = line.find(from, found)) != std::string::npos){
       Placeholder p;
       p.pos = found;
       p.len = to.size();
       p.with = &to;
       vec.push_back(p);
       found += from.size();
    }


}