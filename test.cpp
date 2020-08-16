
#include "aux.cpp"
#include "930.binary-subarrays-with-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> a = {1,0,1,0,1}; 
	int i32 = 2; 
	say(s.numSubarraysWithSum(a, i32));
	return 0;
}

