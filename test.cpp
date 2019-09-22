
#include "aux.cpp"
#include "1200.minimum-absolute-difference.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	// vi arr = {3,8,-10,23,19,-4,-14,27}; 
	vi arr = {4,2,1,3};
	vvi res = s.minimumAbsDifference(arr); 
	say(res);
	return 0;
}

