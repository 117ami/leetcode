// C library
#include <cassert>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <ctime>

// Containers
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

// Input/Output
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <fstream>
#include <ios>
#include <iomanip>

// Other
#include <tuple>
#include <string>
#include <tuple>
#include <bitset>
#include <algorithm>
#include <utility>
#include <type_traits>
#include <iterator>
#include <limits>
#include <stdexcept>
#include <random>
#include <chrono>

// ==================================================

using namespace std;

// constants
const double EPS = 1e-9;
const int MOD = 1000000007;

// type alias
using PII = pair<int, int>;
using LL = long long;
using uLL = unsigned long long; 
using VI = vector<int>;
using VB = vector<bool>;
using VC = vector<char>;
using VS = vector<string>;
using VVI = vector<VI>;
using VVB = vector<VB>; 
using MII = map<int, int>;
using MCI = map<char, int>;
using SI = set<int>;
using SPII = set<pair<int, int>>;
using UMII = unordered_map<int, int>;
using UMCI = unordered_map<char, int>;
using USI = unordered_set<int>;

typedef struct TreeNode TreeNode;
using ptn = TreeNode*;
using tn = TreeNode;

// ==================================================

// fast IO
static auto __2333__ = []() {
                         ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();

// ==================================================

// some macro for less typing
#define INF 0x3f3f3f3f                         
#define max_(x, y) ((x) > (y) ? (x) : (y))
#define min_(x, y) ((x) > (y) ? (y) : (x))

#define MK make_pair

#define fori(n) for (int i = 0; i <=int(n); ++i) // [0, n)
#define EACH(i, n) for (int i = 0; i <=int(n); ++i) // [0, n)
#define EACHV(i, n) for (int i = int(n); i >= 0; --i)   // reverse [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)
#define DOWN(i, b, a) for (int i = int(b); i >= int(a); --i) // reverse [a, b)
#define unfold(i, arr) for (auto &i: arr)
                         
// DEBUG PRINT macro
#define P(x) cerr << (x) << endl
#define NLL cerr << endl
#define PR(x) cerr << #x " = " << (x) << "\t"

#define NL cout << "\n"

#define PR1(x) PR(x), NLL
#define PR2(x1, x2) PR(x1), PR1(x2)
#define PR3(x1, x2, x3) PR(x1), PR2(x2, x3)
#define PR4(x1, x2, x3, x4) PR(x1), PR3(x2, x3, x4)

int direction[8][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1},
  {-1, -1}, {-1, 1}, {1, -1}, {1, 1} };

// ==================================================

// simplest print
template<typename T>
void PRC(const T& a) { cout << a << " "; }
void PRB(bool a) { cout << boolalpha << a << " "; }

// print container
template<typename T>
void PRCO(const T& c) { for (auto x : c) PRC(x); NL; }

// print vector
template<typename T>
void PRV(const vector<T>& c) { PRCO<vector<T>>(c); }

// print C-style array
template<typename T, size_t N>
void PRA(const T (&ar)[N]) {
  for (auto x : ar) PRC(x); NL;
}

// print pair
template<typename T1, typename T2>
void PRP(const pair<T1, T2>& p) { PRC(p.first); PRLN(p.second); }

// print a value and a new line
template<typename T>
void PRLN(const T& a) { cout << a << "\n"; }


// ==================================================
// math
bool is_prime(LL x) {
  if (x == 1 || x <= 0) return false;
  if (x == 2) return true;
  assert(x > 1);
  LL m = ceil(sqrt(x));
  UP(i, 2, m) { if (!(x % i)) return false; }
  return true;
}

// prime table
const int PRIME_MAX = 10;
VI prime_table;
vector<bool> prime_table_bool(PRIME_MAX, true);

void get_prime() {
  UP(i, 2, PRIME_MAX) 
  {
    if (prime_table_bool[i]) 
    {
      prime_table.push_back(i);
      for (int j = i << 1; j <= PRIME_MAX; j += i) prime_table_bool[j] = false;
    }
  }
}

// double equals
bool eq(double a, double b) { return fabs(a - b) < EPS; }

double random_() {
  // generate random number in [0, 1]
  return double(rand()) / RAND_MAX;
}

int random_(int m) {
  // generate random int between [0, m - 1]
  return int(random_() * (m - 1) + 0.5);
}


// ======================================================
// CONVENIENT FUNCTIONS
// whether s is substring of t
bool is_sub(string s, string t) {
  if (s.size() > t.size()) return false;

  int i = 0, j = 0;
  while (i < s.size() && j < t.size()) 
    if (s[i] == t[j++]) 
      i++;

  return (i == s.size());
}

string join(VS &arr, string del=" ") {string res; for(auto &s: arr) res += s + del; return res.substr(0, res.size() -1);}

// sort vector of vector<int> by first element
void sort_by_last(VVI & a){
  sort(a.begin(), a.end(), [](const VI &p, const VI &q){return p.back() < q.back();});
}

// quick sum, product, max, min elemnt of a vector<int>
int sum_(VI &a) { return accumulate(a.begin(), a.end(), 0); }

template <class T> void reverse_(const vector<T> &vect) { reverse(vect.begin(), vect.end()); }

unsigned long long product(vector<int> &a) { unsigned long long res = 1; for (auto &i: a) res *= i; return res; }

int vec_max(VI &a) { return *max_element(a.begin(), a.end()); }

int vec_min(VI &a) { return *min_element(a.begin(), a.end()); }

UMII counter(VI &a) { UMII c = {};  for (auto &x: a) ++ c[x];  return c; }

bool isodd(int &n) { return n % 2 == 1; }
bool iseven(int &n) { return n % 2 == 0; }

// whether two rectangles a = {x1,x2,y1,y2} and b = {s1,s2,t1,t2} overlap
bool isRectangleOverlap(vector<int>& a, vector<int>& b) {
  if (a[0] > b[0]) return isRectangleOverlap(b, a);
  return !(a[2] <= b[0] || a[3] <= b[1] || a[1] >= b[3]);
}




// =========================================================================
// This class represents a directed graph using adjacency list representation
class Graph {
  int V; // No. of vertices
  list<PII> *adj;  // In a weighted graph, we need to store vertex and weight pair for every edge

public:
  Graph(int V); // Constructor
  void addEdge(int u, int v, int w);
  VI shortestPath(int s);
};

// Allocates memory for adjacency list
Graph::Graph(int V) {
  this->V = V;
  adj = new list<PII>[V];
}

void Graph::addEdge(int u, int v, int w) {
  adj[u].push_back(make_pair(v, w));
  adj[v].push_back(make_pair(u, w));
}

// Get shortest paths from src to all other vertices using Dijkstra's algorithm
VI Graph::shortestPath(int src) {
  // Create a priority queue to store vertices that
  // are being preprocessed. This is weird syntax in C++.
  // Refer below link for details of this syntax
  // https://www.geeksforgeeks.org/implement-min-heap-using-stl/
  priority_queue<PII, vector<PII>, greater<PII>> pq;

  VI dist(V, INF);

  pq.push(make_pair(0, src));
  dist[src] = 0;

  while (!pq.empty()) {
    int u = pq.top().second;
    pq.pop();

    for (auto &i : adj[u]) {
      int v = i.first;
      int weight = i.second;

      if (dist[v] > dist[u] + weight) {
        dist[v] = dist[u] + weight;
        pq.push(make_pair(dist[v], v));
      }
    }
  }

  // Print shortest distances stored in dist[]
  // printf("Vertex   Distance from Source\n");
  // for (int i = 0; i < V; ++i)
  //   printf("%d \t\t %d\n", i, dist[i]);

    return dist; 
}


// ==================================================


#ifdef DEBUG
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
#endif



