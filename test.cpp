
#include "aux.cpp"
#include "957.prison-cells-after-n-days.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi x = {1,0,0,1,0,0,1,0}; int N = 1000000000;
	say(s.prisonAfterNDays(x, N));
	string xxs = bitset<8>(12).to_string(); 
	vector<char> vcs (xxs.begin(), xxs.end());
	
	say(vcs);
	return 0;
}

