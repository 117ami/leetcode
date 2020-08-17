
#include "aux.cpp"
#include "446.arithmetic-slices-ii-subsequence.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> i32 = {2,4,6,8,10};
	// i32 = {0,2000000000,294967296};
	say(s.numberOfArithmeticSlices(i32));
	char str[] = "geeksforgeeks"; 
    memset(str, 't', sizeof(str)); 
	say(str);
	return 0;
}

