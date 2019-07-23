
#include "aux.cpp"
#include "1131.maximum-of-absolute-value-expression.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {1,-2,-5,0,10}, b = {0,-2,-1,-7,-4};
	say(s.maxAbsValExpr(a, b));

	return 0;
}

