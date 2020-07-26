
#include "aux.cpp"
#include "1528.shuffle-string.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string t = "codeleet";
	vi indices = {4, 5, 6, 7, 0, 2, 1, 3};
	say(s.restoreString(t, indices));
	return 0;
}

