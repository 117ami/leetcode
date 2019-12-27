
#include "aux.cpp"
#include "736.parse-lisp-expression.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string expr = "(let x (add 1 23) x)"; 
	// expr = "(let x 3 x 2 x)";
	say(s.evaluate(expr));
	return 0;
}

