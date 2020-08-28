
#include "aux.cpp"
#include "746.min-cost-climbing-stairs.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
// std::vector<int> cost = {10, 15, 20} ;

std::vector<int> cost = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1} ;
say(s.minCostClimbingStairs(cost));



	return 0;
}

