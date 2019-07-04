#include "aux.cpp"
#include <algorithm>
#include <bitset>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>

/**

Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Note:

    1 <= A.length = B.length <= 10000
    0 <= A[i] <= 10^9
    0 <= B[i] <= 10^9
**/
using namespace std;

class Solution {
public:
  vector<int> advantageCount(vector<int> &A, vector<int> &B) {
    say(A);
    say(B);
    vector<vector<int>> bwithindex(B.size());
    for (int i = 0; i < B.size(); i++)
      bwithindex[i] = {i, B[i]};

    sort(
        bwithindex.begin(), bwithindex.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[1] < b[1]; });

    say(bwithindex);
    vector<int> res(bwithindex.size(), -1);
    int i = -1, j = 0;
    sort(A.begin(), A.end());
    say(A);
    while (++i < bwithindex.size()) {
      if (A[i] > bwithindex[j].back()) {
        res[bwithindex[j][0]] = A[i];
        A[i] = -1;
        j++;
      }
    }
    say(res);
    say(A);

    i = j = 0;
    while (i < res.size()) {
      while (i < res.size() && res[i] != -1)
        i++;
      while (j < res.size() && -1 == A[j])
        j++;
      if (i < res.size() && j < res.size()) {
        res[i] = A[j];
        j++;
      }
    }
    say(res);
    return res;
  }
};

int main() {
  Solution s;
  vector<int> A = {8, 2, 4, 4, 5, 6, 6, 0, 4, 7};
  vector<int> B = {0, 8, 7, 4, 4, 2, 8, 5, 2, 0};
  A = {718967141, 189971378, 341560426, 23521218, 339517772};
  B = {967482459, 978798455, 744530040, 3454610, 940238504};
  s.advantageCount(A, B);
}
