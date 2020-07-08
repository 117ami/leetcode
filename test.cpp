
#include "aux.cpp"
#include "1504.count-submatrices-with-all-ones.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi ivv = {{1,0,1}, {1,1,0}, {1,1,0}};
	ivv = {{0,1,1,0}, {0,1,1,1}, {1,1,1,0}};
	say(s.numSubmat(ivv));
	return 0;
}

