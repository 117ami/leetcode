
#include "aux.cpp"
#include "638.shopping-offers.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi price={2,3,4};
	vvi special = {{1,1,0,4}, {2,2,1,9}};
	vi needs= {1,2,1};
	
	price={2,5}, special={{3,0,5},{1,2,10}}, needs={3,2};
	price  = {4,3,2,9,8,8}, special = {{1,5,5,1,4,0,18}, {3,3,6,6,4,2,32}}, needs = {6,5,5,6,4,1};
	say(s.shoppingOffers(price, special,needs));

	return 0;
}

