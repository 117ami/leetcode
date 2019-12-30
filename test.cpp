
#include "aux.cpp"
#include "990.satisfiability-of-equality-equations.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vs eqs = {"z!=b", "a==b", "b!=c", "c==a"};
	eqs = {"c==c","b==d","x!=z"};
	say(s.equationsPossible(eqs));
	return 0;
}

