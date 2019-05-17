
#include "aux.cpp"
#include "299.bulls-and-cows.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string secret = "7810", guess = "1807";
	string res = s.getHint(secret, guess);
	say(res);
	return 0;
}

