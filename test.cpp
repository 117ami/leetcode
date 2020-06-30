
#include "aux.cpp"
#include "1499.max-value-of-equation.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi ps = {{0, 0}, {3, 0}, {9, 2}}; 
	say(s.findMaxValueOfEquation(ps, 3));
	return 0;
}

