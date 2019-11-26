
#include "aux.cpp"
#include "1268.search-suggestions-system.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<string> products = {"mobile","mouse","moneypot","monitor","mousepad"};
	string sw = "mouse"; 
	vector<vector<string>> res = s.suggestedProducts(products, sw); 
	say(res);
	return 0;
}

