
#include "aux.cpp"
#include "516.longest-palindromic-subsequence.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	std::vector<int> nums = {2, 3, 4, 5, 6, 1};
	nums = {3, 1, 3, 3, 3};
	int res = s.longestPalindromeSubseq("adam");
	say(res);
	return 0;
}

