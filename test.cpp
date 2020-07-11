
#include "aux.cpp"
#include "78.subsets.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi x = {1,2,3};
	vvi r = s.subsets(x);
	say(r);
	return 0;
}

