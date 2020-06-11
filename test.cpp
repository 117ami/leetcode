
#include "aux.cpp"
#include "75.sort-colors.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<int> v = {2,1,0};
	s.sortColors(v);
	say(v);
	return 0;
}

