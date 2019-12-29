
#include "aux.cpp"
#include "1300.sum-of-mutated-array-closest-to-target.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr ={60864,25176,27249,21296,20204}; 
	int target = 56803; 
	arr =  {1547,83230,57084,93444,70879}, target =71237;

	say(s.findBestValue(arr, target));
	return 0;
}

