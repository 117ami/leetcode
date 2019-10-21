
#include "aux.cpp"
#include "718.maximum-length-of-repeated-subarray.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> A = {1,2,3,2,1}, B = {3,2,1,4,7}; 
	A = {0,0,0,0,1}, B = {1,0,0,0,0}; 
	say(s.findLength(A, B));
	return 0;
}

