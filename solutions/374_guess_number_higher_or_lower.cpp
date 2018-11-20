#include<stdio.h>
#include<map>
#include<unordered_map>
#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
/**
We are playing the Guess Game. The game is as follows: 
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.
Return 6.

 **/
using namespace std; 

static int speed_up = []() { std::ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 

// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int lower = 1, higher = n, res = (higher + lower) / 2; 
        while( guess(res) != 0) {
        	if (guess(res) == 1) 
        		lower = res + 1; 
        	else 
        		higher = res - 1;
        	res = (higher + lower) / 2; 
        }
        return res; 
    }
};

int main() { 
 Solution s; 
}
