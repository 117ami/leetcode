#include <iostream> 
#include <vector>
#include <unordered_set>

const int p = 233, MOD = 1e9+7; 

int64_t quick_pow(int base, int len, int MOD) {
    // Quick pow method to compute (base ^ len % MOD) 
    int64_t res = 1, tmp = base;
    while (len > 0) {
        if ((len & 1) != 0) res = res * tmp % MOD;
        tmp = tmp * tmp % MOD;
        len >>= 1;
	}
    return res;
}

bool rabin_karp(std::vector<int>& A, std::vector<int>& B, int len) {
    // Use Rabin Karp method to check whether A / B share a sub vector with length len
    if (len <= 0) return false; 
    int64_t offset = quick_pow(p, len - 1, MOD), hash = 0; 
    std::unordered_set<int> hashes  ; 
    for (int i = 0; i < A.size(); i++) {
        if (i >= len) hash += MOD - A[i-len] * offset % MOD; 
        hash = (hash * p + A[i]) % MOD; 
        if (i >= len - 1) hashes.insert(hash);
    }

    hash = 0; 
    for (int i = 0; i < B.size(); i++) {
        if (i >= len) hash += MOD - B[i-len] * offset % MOD; 
        hash = (hash * p + B[i]) % MOD; 
        if (i >= len - 1 && hashes.count(hash) > 0) return true; 
    }

    return false; 
}

bool rabin_karp(std::string &s, std::string &t, int len) {
    // Whether s and t share a common substring with length len 
    std::vector<int> vs, vt; 
    for(char &c: s) vs.push_back(c - 'a');
    for(char &c: t) vt.push_back(c - 'a');
    return rabin_karp(vs, vt, len);
}


int main() {
    std::cout << quick_pow(2, 13000000, 100000003) << std::endl; 
    std::string sa = "bluelight", sb = "yellowlueght";
    std::cout << rabin_karp(sa, sb, 3) << std::endl; 
    return 0; 
}