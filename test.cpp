
#include "aux.cpp"
#include "956.tallest-billboard.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi pods = {1, 2, 3, 4, 4, 5, 6}; 
	pods = {96,112,101,100,104,93,106,99,114,81,94};
	say(s.tallestBillboard(pods));
	return 0;
}

