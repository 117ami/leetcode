
#include "aux.cpp"
#include "1498.number-of-subsequences-that-satisfy-the-given-sum-condition.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi x = {5,2,4,1,7,6,8}; 
	x = {14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14};
	say(s.numSubseq(x, 22));
	return 0;
}

