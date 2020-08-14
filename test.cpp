
#include "aux.cpp"
#include "592.fraction-addition-and-subtraction.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string input = "-3/10-10/5+2/3";
	input = "-1/2+1/2-1/3";
	input = "1/3-1/2";
	// input = "";
	say(s.fractionAddition(input));
	return 0;
}

