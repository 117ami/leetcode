
#include "aux.cpp"
#include "1043.partition-array-for-maximum-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> A = {1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3};
	int K = 4; 
	say(s.maxSumAfterPartitioning(A, K));
	return 0;
}

