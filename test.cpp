
#include "aux.cpp"
#include "c.cpp"
#include "97.interleaving-string.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
	say(s.isInterleave(s1,s2,s3));
	return 0;
}

