
#include "aux.cpp"
#include "1177.can-make-palindrome-from-substring.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string expr = "xebyvmjqbmbs"; 
	vvi qs = extractMatrixFromString("[[9,9,1],[6,9,3],[11,11,1],[0,3,3],[9,10,0],[10,11,2],[3,3,1],[4,11,8],[1,10,3],[2,9,7],[11,11,1]]");
	say(s.canMakePaliQueries(expr, qs));
	return 0;
}

