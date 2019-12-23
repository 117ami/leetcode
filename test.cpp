
#include "aux.cpp"
#include "712.minimum-ascii-delete-sum-for-two-strings.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string s1 = "leet", s2 = "delete";
	say(s.minimumDeleteSum(s1, s2));
	return 0;
}

