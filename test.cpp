
#include "aux.cpp"
#include "241.different-ways-to-add-parentheses.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string x = "2*3-4*5"; 
	// x = "3-4";
	say(s.diffWaysToCompute(x));
	return 0;
}

