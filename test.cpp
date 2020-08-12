
#include "aux.cpp"
#include "26.remove-duplicates-from-sorted-array.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> v = {0,0,1,1,1,2,2,3,3,4};
	v = {1,1,2};
	// v = {};
	say(s.removeDuplicates(v));
	
	return 0;
}

