// C libraries
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// Containers
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Input/Output
#include <fstream>
#include <iomanip>
#include <ios>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>

// Other
#include <algorithm>
#include <bitset>
#include <chrono>
#include <iterator>
#include <limits>
#include <random>
#include <stdexcept>
#include <string>
#include <tuple>
#include <type_traits>
#include <utility>

// ==================================================

using namespace std;

// constants
const double EPS = 1e-9;
const int MOD = 1000000007;

// type alias
using pii = pair<int, int>;
using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vb = vector<bool>;
using vc = vector<char>;
using vs = vector<string>;
using vvb = vector<vector<bool>>;
using vvc = vector<vector<char>>;
using vvi = vector<vector<int>>;
using vvs = vector<vector<string>>;
using mii = map<int, int>;
using mci = map<char, int>;
using si = set<int>;
using spii = set<pair<int, int>>;
using umii = unordered_map<int, int>;
using umci = unordered_map<char, int>;
using umsi = unordered_map<string, int>;
using usi = unordered_set<int>;
using usc = unordered_set<char>;
using uss = unordered_set<string>;
using vpii = vector<pair<int, int>>;

typedef struct TreeNode TreeNode;
using ptn = TreeNode *;
using tn = TreeNode;

// ==================================================

// fast IO
static auto __speedup__ = []() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return 0;
}();

// ==================================================

// some macro for less typing
#define forloop(i, n) for (int i = 0; i < n; i++)             //[0, n)
#define forloopr(i, n) for (int i = n - 1; i >= 0; --i)       // reverse [0, n)
#define forloopup(i, a, b) for (int i = a; i < b; ++i)        // [a, b)
#define forloopdown(i, a, b) for (int i = b - 1; i >= a; --i) // reverse [a, b)
#define forunfold(i, arr) for (auto &i : arr)

#define INF 0x3f3f3f3f
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define ef emplace_front
#define eb emplace_back
#define qall(v) v.begin(), v.end()
#define qsize(v) (int)v.size()
#define qsort(v) sort(v.begin(), v.end())
#define rqsort(v) sort(v.rbegin(), v.rend())
#define qreverse(v) reverse(v.begin(), v.end())

// int to string
string itos(int n) { return to_string(n); }
// char to string
string ctos(char c) { return string(1, c); };

inline string upper(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::toupper);
  return t;
}
inline string lower(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::tolower);
  return t;
}

int dirs[5] = {-1, 0, 1, 0, -1};

// ==================================================
/*
 * @lc app=leetcode id=1592 lang=cpp
 *
 * [1592] Rearrange Spaces Between Words
 *
 * https://leetcode.com/problems/rearrange-spaces-between-words/description/
 *
 * algorithms
 * Easy (42.97%)
 * Total Accepted:    7.3K
 * Total Submissions: 16.7K
 * Testcase Example:  '"  this   is  a sentence "'
 *
 * You are given a string text of words that are placed among some number of
 * spaces. Each word consists of one or more lowercase English letters and are
 * separated by at least one space. It's guaranteed that text contains at least
 * one word.
 *
 * Rearrange the spaces so that there is an equal number of spaces between
 * every pair of adjacent words and that number is maximized. If you cannot
 * redistribute all the spaces equally, place the extra spaces at the end,
 * meaning the returned string should be the same length as text.
 *
 * Return the string after rearranging the spaces.
 *
 *
 * Example 1:
 *
 *
 * Input: text = "  this   is  a sentence "
 * Output: "this   is   a   sentence"
 * Explanation: There are a total of 9 spaces and 4 words. We can evenly divide
 * the 9 spaces between the words: 9 / (4-1) = 3 spaces.
 *
 *
 * Example 2:
 *
 *
 * Input: text = " practice   makes   perfect"
 * Output: "practice   makes   perfect "
 * Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces
 * plus 1 extra space. We place this extra space at the end of the string.
 *
 *
 * Example 3:
 *
 *
 * Input: text = "hello   world"
 * Output: "hello   world"
 *
 *
 * Example 4:
 *
 *
 * Input: text = "  walks  udp package   into  bar a"
 * Output: "walks  udp  package  into  bar  a "
 *
 *
 * Example 5:
 *
 *
 * Input: text = "a"
 * Output: "a"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= text.length <= 100
 * text consists of lowercase English letters and ' '.
 * text contains at least one word.
 *
 *
 */
class Solution {
public:
  string reorderSpaces(string text) {
    int cnt = 0;
    std::vector<string> ws;
    string tmp;
    for (char &c : text) {
      if (c == ' ') {
        cnt++;
        if (tmp.size() > 0) ws.push_back(tmp);
        tmp.clear();
      } else
        tmp.push_back(c);
    }
    if (tmp.size() > 0) ws.push_back(tmp);


    if (ws.size() == 1) return ws[0] + std::string(cnt, ' ');
    std::string res = "";
    int space = cnt / (ws.size() - 1);
    cnt -= space * (ws.size() - 1);
    
    for (auto it = ws.begin(); it < ws.end() - 1; it++)
      res += *it + std::string(space, ' ');
    res += ws.back() + std::string(cnt, ' ');
    
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
