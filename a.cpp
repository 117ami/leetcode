#include "c.cpp"

int main(int argc, char const *argv[])
{
	VI nums {1, 2, 4, 3, 2};
	int mus = sum_(nums);
	VI dp(mus + 1, 0);
	dp[0]=1;
	for(auto &x: nums){
		DWN(i, mus, x) 
		dp[i] += dp[i-x];
		PRV(dp);
	}

	EACH(i, dp.size()-1)
		cout << i << " " << dp[i] << endl;
	return 0;
}