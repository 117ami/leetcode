
#include "aux.cpp"
#include "699.falling-squares.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi pos = {1,2,3,5,6,8,9};
	auto i = upper_bound(pos.begin(), pos.end(), 4);
    auto j = lower_bound(pos.begin(), pos.end(), 7);
    int h = *max_element(i, j);
	vvi positions = {{1,2}, {2,3}, {6,1}};
	say(s.fallingSquares(positions));

	map<int, int> mp; 
	mp[0] = 0; 
	mp[2] = 2; 
	mp[4] = 4; 
	mp[5] = 5; 
	mp[1] = 1; 
	mp[3] = 3; 
	// for (auto it: mp) say(vi{it.first, it.second});
	
	return 0;
}

