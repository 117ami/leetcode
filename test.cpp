
#include "aux.cpp"
#include "1537.get-the-maximum-score.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi na = {1,4,5,8,9,11,19}, nb={2,3,4,11,12};
	say(s.maxSum(na, nb));
	return 0;
}

