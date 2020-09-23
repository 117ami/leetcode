// Containers
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <numeric>



using namespace std; 
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
class SparseVector {
public:
    std::vector<pair<int, int>> cc; 
    SparseVector(vector<int> &nums) {
        for(int i=0; i<nums.size(); i++){
          if (nums[i]>0) cc.push_back({i, nums[i]});
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int i=0, j=0, res=0;
        while(i<cc.size() && j < vec.cc.size()){
          if(cc[i].first == vec.cc[j].first)  res += cc[i].second * vec.cc[j].second, i++,j++;
          else if(cc[i].first < vec.cc[j].first)  i++; 
          else j++;
        }
        return res; 
    }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);

