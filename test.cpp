
#include "aux.cpp"
#include "848.shifting-letters.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string S = "abc" ;
	std::vector<int> shifts = {3,5,9} ;
	S = "ruu"; 
	shifts={26,9,17};
	say(s.shiftingLetters(S, shifts));
	return 0;
}

