#include "aux.cpp"
/**
Design a class to findthe kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
YourKthLargestclass will have a constructor which accepts an integer k and an integer array nums, which contains initial elements fromthe stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3); // returns 4
kthLargest.add(5); // returns 5
kthLargest.add(10); // returns 5
kthLargest.add(9); // returns 8
kthLargest.add(4); // returns 8
Note: 
You may assume thatnums' length>=k-1and k >=1.

 https://leetcode.com/problems/kth-largest-element-in-a-stream/description/ 
 **/
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 

class KthLargest {
public:
    KthLargest(int k, vector<int> nums) {
        
    }
    
    int add(int val) {
        
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */

int main() { 
 Solution s; 
}
