
#include "aux.cpp"
#include "1289.minimum-falling-path-sum-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi arr = {{1, 2, 3},{4,5,6},{7,8,9}};
	say(s.minFallingPathSum(arr));
	return 0;
}

