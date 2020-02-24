
#include "aux.cpp"
#include "1359.count-all-valid-pickup-and-delivery-options.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	for(int i = 1; i < 501; i++) say(s.countOrders(i));
	return 0;
}

