
#include "aux.cpp"
#include "1562.find-latest-group-of-size-m.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// std::vector<int> arr = {3,5,1,2,4} ;
	// int m = 1 ;

	// std::vector<int> arr = {3,1,5,4,2} ;
	// int m = 2 ;

	// std::vector<int> arr = {1} ;
	// int m = 1 ;

	std::vector<int> arr = {2,1} ;
	int m = 2 ;

	say(s.findLatestStep(arr, m));

	return 0;
}

