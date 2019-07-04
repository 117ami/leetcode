/*
 * @lc app=leetcode id=313 lang=cpp
 *
 * [313] Super Ugly Number
 *
 * https://leetcode.com/problems/super-ugly-number/description/
 *
 * algorithms
 * Medium (41.44%)
 * Total Accepted:    60.5K
 * Total Submissions: 145.8K
 * Testcase Example:  '12\n[2,7,13,19]'
 *
 * Write a program to find the nth super ugly number.
 *
 * Super ugly numbers are positive numbers whose all prime factors are in the
 * given prime list primes of size k.
 *
 * Example:
 *
 *
 * Input: n = 12, primes = [2,7,13,19]
 * Output: 32
 * Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
 * 12
 * ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
 *
 * Note:
 *
 *
 * 1 is a super ugly number for any given primes.
 * The given numbers in primes are in ascending order.
 * 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
 * The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
 *
 *
 */
using namespace std;
using vi = vector<int>;
using ll = long long;
#define INF 0x3f3f3f3f
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)       // [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)
#define fori(n) for (int i = 0; i <= int(n); ++i)          // [0, n)
#include <cassert>
#define mp make_pair
int vec_min(vi &a) { int r = INT_MAX; for(auto &i: a) r = min(r, i); return r; }


class Solution {
public:
  int nthSuperUglyNumber(int n, vector<int> &primes) {
	   vector<int> ugly(n, 1), factors(primes), idx(primes.size(),0);
     for(int i = 1; i < n; i ++) {
            ugly[i] = vec_min(factors);
            for (int j = 0; j < primes.size(); j ++){
                if (factors[j] == ugly[i]) {
                  idx[j] ++; 
                  factors[j] = primes[j] * ugly[idx[j]];
                }
            }
      }
      return ugly[n - 1];
  }
};1

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();


