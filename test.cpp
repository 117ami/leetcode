
#include "aux.cpp"
#include "1515.best-position-for-a-service-centre.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vvi p = {{1,1},{0,0},{2,0}};
	say(s.getMinDistSum(p));
	return 0;
}

