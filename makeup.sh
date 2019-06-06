#
cppfile=$1
echo "making up for $cppfile"

class_line=$(nl $cppfile | grep 'class' | awk '{print $1}')

cmd=' using namespace std;'
grep --quiet 'PII'  $cppfile && cmd="$cmd \n using PII = pair<int, int>;"
grep --quiet 'LL' 	$cppfile && cmd="$cmd \n using LL = long long;"
grep --quiet 'uLL' 	$cppfile && cmd="$cmd \n using uLL = unsigned long long;"
grep --quiet 'VI' 	$cppfile && cmd="$cmd \n using VI = vector<int>;"
grep --quiet 'VB' 	$cppfile && cmd="$cmd \n using VB = vector<bool>;"
grep --quiet 'VC' 	$cppfile && cmd="$cmd \n using VC = vector<char>;"
grep --quiet 'VS' 	$cppfile && cmd="$cmd \n using VS = vector<string>;"
grep --quiet 'VVI' 	$cppfile && cmd="$cmd \n using VVI = vector<VI>;"
grep --quiet 'VVB' 	$cppfile && cmd="$cmd \n using VVB = vector<VB>;"
grep --quiet 'MII' 	$cppfile && cmd="$cmd \n using MII = map<int, int>;"
grep --quiet 'MCI' 	$cppfile && cmd="$cmd \n using MCI = map<char, int>;"
grep --quiet 'SI' 	$cppfile && cmd="$cmd \n using SI = set<int>;"
grep --quiet 'SPII' $cppfile && cmd="$cmd \n using SPII = set<pair<int, int>>;"
grep --quiet 'UMII' $cppfile && cmd="$cmd \n using UMII = unordered_map<int, int>;"
grep --quiet 'USI' 	$cppfile && cmd="$cmd \n using using = unordered_set<int>;"

grep --quiet 'EPS' 	$cppfile && cmd="$cmd \n const double EPS = 1e-9;"
grep --quiet 'MOD' 	$cppfile && cmd="$cmd \n const int MOD = 1000000007;"
grep --quiet 'INF' 	$cppfile && cmd="$cmd \n #define INF 0x3f3f3f3f;"
grep --quiet 'MK' 	$cppfile && cmd="$cmd \n #define MK make_pair;"
grep --quiet 'EACH' $cppfile && cmd="$cmd \n #define EACH(i, n) for (int i = 0; i <=int(n); ++i) \n #define EACHV(i, n) for (int i = int(n); i >= 0; --i)"
grep --quiet 'unfold' $cppfile && cmd="$cmd \n #define unfold(i, arr) for (auto &i: arr)"


grep --quiet 'UP' 	$cppfile && cmd="$cmd \n #define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b]"
grep --quiet 'DWN' 	$cppfile && cmd="$cmd \n #define DWN(i, b, a) for (int i = int(b); i >= int(a); --i) // reverse [a, b]"

grep --quiet 'sum_' $cppfile && cmd="$cmd \n int sum_(VI &a) { return accumulate(a.begin(), a.end(), 0); }"
grep --quiet 'reverse_' $cppfile && cmd="$cmd \n void reverse_(VI &a) { reverse(a.begin(), a.end()); } "
grep --quiet 'vec_max' $cppfile && cmd="$cmd \n int vec_max(VI &a) { return *max_element(a.begin(), a.end()); }"
grep --quiet 'vec_min' $cppfile && cmd="$cmd \n int vec_min(VI &a) { return *min_element(a.begin(), a.end()); }"

grep --quiet 'counter' $cppfile && cmd="$cmd \n unordered_map<int, int> counter(vector<int> &a) { unordered_map c = {}; for (auto &x: a) ++ c[x]; return c; }"

# finally insert those typedefs 
gsed -i "$class_line i $cmd\n\n" $cppfile

# Tidy up
clang-format -i $cppfile


