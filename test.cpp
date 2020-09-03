
#include "aux.cpp"
#include "931.minimum-falling-path-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<std::vector<int>> ns = {{1,2,3},{4,5,7},{7,8,9}};
	ns = {{35,94,-89,35,69}, {-32,-50,19,-12,-65}, {-6,-18,14,2,-38}, {-29,68,-50,12,-98}, {49,-33,-91,-44,-52}};
	say(s.minFallingPathSum(ns));
	return 0;
}

