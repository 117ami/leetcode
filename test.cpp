
#include "aux.cpp"
#include "1578.minimum-deletion-cost-to-avoid-repeating-letters.cpp"

int main(int argc, char const *argv[]) {
	Solution sol;
	string s = "abaac" ;
	std::vector<int> cost = {1,2,3,4,5} ;

	// string s = "abc" ;
	// std::vector<int> cost = {1,2,3} ;

	say(sol.minCost(s, cost));


	return 0;
}

