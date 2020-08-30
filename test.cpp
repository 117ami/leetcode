
#include "aux.cpp"
#include "1566.detect-pattern-of-length-m-repeated-k-or-more-times.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> arr = {1,2,4,4,4,4} ;
	int m = 1 ;
	int k = 3 ;

	arr = {1,2,1,2,1,1,1,3} ;
	m = 2 ;
	k = 2 ;

	arr = {3,2,2,1,2,2,1,1,1,2,3,2,2};
	m = 3, k = 2; 

	// std::vector<int> arr = {1,2,3,1,2} ;
	// int m = 2 ;
	// int k = 2 ;

	// std::vector<int> arr = {2,2,2,2} ;
	// int m = 2 ;
	// int k = 3 ;

	say(s.containsPattern(arr, m, k));


	return 0;
}

