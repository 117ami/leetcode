#include <iostream> 

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


int main() {
    std::cout << quick_pow(2, 13000000, 100000003) << std::endl; 
    return 0; 
}