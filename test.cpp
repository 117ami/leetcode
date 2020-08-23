
#include "aux.cpp"
#include "1561.maximum-number-of-coins-you-can-get.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
std::vector<int> piles = {2,4,1,2,7,8} ;

// std::vector<int> piles = {2,4,5} ;

// std::vector<int> piles = {9,8,7,6,5,1,2,3,4} ;

say(s.maxCoins(piles));

	return 0;
}

