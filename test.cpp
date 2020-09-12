
#include "aux.cpp"
#include "518.coin-change-2.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int amount = 5 ;
	std::vector<int> coins = {1, 2, 5} ;

	// int amount = 3 ;
	// std::vector<int> coins = {2} ;

	// int amount = 10 ;
	// std::vector<int> coins = {10} ;
	say(s.change(amount, coins));
	return 0;
}

