// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

using namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

class UF {
  int *id, cnt, *sz;

public:
  UF(int N) {
    cnt = N;
    id = new int[N], sz = new int[N];
    for (int i = 0; i < N; i++) id[i] = i, sz[i] = 1;
  }

  ~UF() {
    delete[] id;
    delete[] sz;
  }

  int find(int p) {
    if (p != id[p]) id[p] = find(id[p]);
    return id[p];
  }

  void merge(int x, int y) {
    int i = find(x), j = find(y);
    if (i == j) return;
    id[j] = id[i] = min(i, j);
  }
};

// --------------------------------------------------------
class Solution {
public:
  string smallestEquivalentString(string A, string B, string S) {
    UF uf(26);
    for (int i = 0; i < A.size(); i++) uf.merge(A[i] - 'a', B[i] - 'a');
    string res(S.length(), 'a');
    for (int i = 0; i < S.length(); i++) res[i] = uf.find(S[i] - 'a') + 'a';
    return res;
  }
};

int main() {
  Solution s;
  string A = "leetcode", B = "programs", S = "sourcecode";
  say(s.smallestEquivalentString(A, B, S));
}