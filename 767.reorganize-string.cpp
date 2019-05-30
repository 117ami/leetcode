/*
 * @lc app=leetcode id=767 lang=cpp
 *
 * [767] Reorganize String
 *
 * https://leetcode.com/problems/reorganize-string/description/
 *
 * algorithms
 * Medium (42.02%)
 * Total Accepted:    26.5K
 * Total Submissions: 62.8K
 * Testcase Example:  '"aab"'
 *
 * Given a string S, check if the letters can be rearranged so that two
 * characters that are adjacent to each other are not the same.
 * 
 * If possible, output any possible result.  If not possible, return the empty
 * string.
 * 
 * Example 1:
 * 
 * 
 * Input: S = "aab"
 * Output: "aba"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: S = "aaab"
 * Output: ""
 * 
 * 
 * Note:
 * 
 * 
 * S will consist of lowercase letters and have length in range [1, 500].
 * 
 * 
 * 
 * 
 */
using namespace std; 
using LL = long long; 
using VI = vector<int>; 
using VB = vector<bool>; 
const int MOD = 1000000007;


class Solution {
public:
    string reorganizeString(string S) {
    	MOD;
    	VI vi(100, 0);
    	VB vb(100, false);
    	unordered_map<char, int> counter;
    	for (auto &c:S) ++counter[c];
    	vector<pair<int, char>> vp; 
    	for (auto p = counter.begin(); p != counter.end(); p++){
    		vp.push_back(make_pair(p->second, p->first));
    		// cout << p->first << " " << p->second << endl; 
    	}

		sort(vp.begin(), vp.end(), [](pair<int, char> &p, pair<int, char> &q){return p.first > q.first;});    	
		
		string res(S.size(), '#');
		int i = 0;

		for (auto p = vp.begin(); p != vp.end(); p++){
			EACH(j, p->first - 1){
				res[i] = p->second;
				if (i > 0 && i < S.size() - 1 && (res[i] == res[i-1] || res[i] == res[i+1]))
					return "";
				i += 2;
				if (i >= S.size()) i = 1;
			}
		}

		return res;
    }
};

static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
