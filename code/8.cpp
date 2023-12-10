#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <tuple>
#include <vector>

std::map<std::string, std::map<std::string, std::string>> vmap; //values mapped in form: {A : {L : B, R: B}}

std::tuple<std::string, int> find_way(std::string input, std::string sequence);

int main(int argc, char** argv){

	std::fstream file(argv[1]);

	bool reading_instructions = true;
	std::string instructions;

	for(std::string line; std::getline(file, line);){
		if (line.size() == 0) {reading_instructions = false; continue;}

		if(reading_instructions) instructions += line;
		else{

			std::string name = line.substr(0, 3);
			std::string left = line.substr(7, 3);
			std::string right = line.substr(12, 3);
			std::map<std::string, std::string> temp;
			temp["L"] = left;
			temp["R"] = right;
			vmap[name] = temp;
		}
	}
	

	file.close();

	std::string goal = "AAA";
	int steps = 0;
	while(goal != "ZZZ"){

		std::tuple<std::string, int> back = find_way(goal, instructions);
		std::string node = std::get<0>(back);
		int depth = std::get<1>(back);
		steps += depth;
		goal = node;
	}

	std::cout << steps << std::endl;


	return 0;
}


std::tuple<std::string, int> find_way(std::string input, std::string sequence){



	std::map<std::string, std::string>& targets = vmap[input];
	//checking if ZZZ can be reached with subsequence

	for(auto& el : targets){
		std::string way = el.first;
		std::string goal = el.second;

		if (goal == "ZZZ"){

			for(int i = 0; i < sequence.size(); i++){

				std::string sub = sequence.substr(0, sequence.size()-i);
				if (way == sub){
					
					int backlen = sequence.size()-i;
					std::tuple<std::string, int> back{"ZZZ", backlen};
					return std::move(back);
				}

			}

		}
		
	}

	std::string next = targets[sequence.substr(0, 1)];
	if (sequence.size() == 1){
		std::string vec = next;
		std::tuple<std::string, int> back{vec, 1};
		return std::move(back);
	}

	std::tuple<std::string, int> rec = find_way(next, sequence.substr(1, sequence.size()-1));
    std::string node = std::get<0>(rec);
	int depth = std::get<1>(rec);

	std::string subs = sequence.substr(0, sequence.size());
	if (targets.find(subs) == targets.end()){
		targets[subs] = node;
	}

	depth += 1;
	std::tuple<std::string, int> back{node, depth};
	return std::move(back);
}
