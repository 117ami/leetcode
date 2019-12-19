
#include "aux.cpp"
#include "1292.maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold.cpp"

vector<vector<int>> extractMatrixFromString(string s){
	vector<vector<int>> res; 
	int carry = INT_MIN;
	for (size_t i = 1; i < s.size() - 1; ++i) {
		if (s[i] == '[') res.push_back(vector<int>{});
		while (isdigit(s[i])) carry = max(carry, 0) * 10 + (s[i++] - '0');
		if (carry > INT_MIN) res.back().push_back(carry); 
		carry = INT_MIN;  
	}
	return res; 
}


int main(int argc, char const *argv[]) {
	Solution s;
	vvi mat = extractMatrixFromString("[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]"); 
	int t = 4; 
	say(s.maxSideLength(mat, t));
	return 0;
}

