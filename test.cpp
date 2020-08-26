
#include "aux.cpp"
#include "121.best-time-to-buy-and-sell-stock.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi stock = {7,1,5,3,6,4};
	say(s.maxProfit(stock));
	return 0;
}

