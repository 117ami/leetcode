
#include "aux.cpp"
#include "c.cpp"
#include "1090.largest-values-from-labels.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi values = {8,8,7,6,9}, labels = {0,0,1,1,0};
	int num_wanted = 3, use_limit = 2;
	say(s.largestValsFromLabels(values, labels, num_wanted, use_limit));
	return 0;
}

