#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

template<typename iterator, typename T>
void merge_sort(iterator, iterator, int(*)(T, T));
template<typename iterator, typename T>
void merge(iterator, int, iterator, int, int(*)(T, T));



std::map<char, int> vmap = {

			{'2', 1},
			{'3', 2},
			{'4', 3},
			{'5', 4},
			{'6', 7},
			{'7', 8},
			{'8', 9},
			{'9', 10},
			{'T', 11},
			{'J', 12},
			{'Q', 13},
			{'K', 14},
			{'A', 15}
};

enum combinations{

	HIGH_CARD = 1,
	ONE_PAIR = 2,
	TWO_PAIR = 3,
	THREE_KIND = 4,
	FULL_HOUSE = 5,
	FOUR_KIND = 6,
	FIVE_KIND = 7

};

struct CardsXBid{

	std::string hand;
	int bid;
};

combinations get_type(CardsXBid& cxb){

	std::map<char, int> occurences;

	for (char c : cxb.hand){

		if (occurences.find(c) == occurences.end()){
			occurences[c] = 1;
		}
		else{
			occurences[c] += 1;
		}
	}

	int three_occ = 0;
	int two_oc = 0;

	for (auto& el : occurences){
		if (el.second == 5) return combinations::FIVE_KIND;
		if (el.second == 4) return combinations::FOUR_KIND;
		if(el.second == 3) three_occ += 1;
		if (el.second == 2) two_oc += 1;

	}

	if (three_occ == 1 && two_oc == 1) return combinations::FULL_HOUSE;
	if (three_occ == 1) return combinations::THREE_KIND;
	if (two_oc == 2) return combinations::TWO_PAIR;
	if (two_oc == 1) return combinations::ONE_PAIR;

	return combinations::HIGH_CARD;

}

int handcmp(char a, char b){
	return vmap[a] - vmap[b];
}

int cxbcmp(CardsXBid a, CardsXBid b){

	combinations aval = get_type(a);
	combinations bval = get_type(b);

	if (aval < bval) return -1;
	if (bval < aval) return 1;

	for(int i = 0; i < 5; i++){
		if (vmap[a.hand[i]] < vmap[b.hand[i]]) return -1;
		if (vmap[b.hand[i]] < vmap[a.hand[i]]) return 1;
	}

	return 0;

}



int main(int argc, char** argv){

	std::string path = argv[1];

	std::vector<CardsXBid> hands;

	std::ifstream file(path);

	for(std::string line; std::getline(file, line);){

		std::string hand;
		std::string bid;

		std::string::iterator it = line.begin();
		while(*it != ' '){
			hand += (*it);
			it++;
		}
		it++;
		while(it != line.end()){
			bid += (*it);
			it++;
		}

		CardsXBid cb;
		
		cb.hand = hand;
		cb.bid = std::stoi(bid);

		hands.push_back(cb);


	}


	file.close();

	merge_sort<std::vector<CardsXBid>::iterator, CardsXBid>(hands.begin(), hands.end(), cxbcmp);

	int rank = 1;
	int value = 0;
	for(CardsXBid& cb : hands){
		value += cb.bid * (rank++);
	}
	std::cout << value << std::endl;

	return 0;
}

template<typename iterator, typename T>
void merge_sort(iterator start, iterator end, int(*comp)(T, T)){

	if (end-start <= 1) return;

	int middle = (end-start)/2;

	merge_sort<iterator, T>(start, start + middle, comp);
	merge_sort<iterator, T>(start+middle, end, comp);
	merge<iterator, T>(start, middle, start+middle, end-(start+middle), comp);

}

template<typename iterator, typename T>
void merge(iterator first, int firstlen, iterator second, int secondlen, int(*comp)(T, T)){

	iterator firstend = first + firstlen;
	iterator secondend = second + secondlen;
	iterator firstsave = first;

	std::vector<T> temp;

	while (first != firstend && second != secondend){

		T &el1 = *first, &el2 = *second;

		int cmp = comp(el1, el2);

		if (cmp <= 0){
			temp.push_back(el1);
			first++;
		}
		else{
			temp.push_back(el2);
			second++;
		}

	}

	while (first != firstend){
		temp.push_back(*first);
		first++;
	}
	while(second != secondend){
		temp.push_back(*second);
		second++;
	}

	for (T el : temp){
		*firstsave = el;
		firstsave++;
	}

}