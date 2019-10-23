
#include "aux.cpp"
#include "1004.max-consecutive-ones-iii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> A = {1,1,1,0,0,0,0};
	int K = 2; 
	say(s.longestOnes(A, K));
	return 0;
}

