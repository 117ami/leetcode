
#include "aux.cpp"
#include "1357.apply-discount-every-n-orders.cpp"

int main(int argc, char const *argv[]) {
	int n = 3, discount = 50; 
	vi products = {1,2,3,4,5,6,7}, prices = {100,200,300,400,300,200,100};
	Cashier* obj = new Cashier(n, discount, products, prices);
	
	return 0;
}

