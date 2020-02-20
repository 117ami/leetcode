#include <vector> 
using namespace std; 

class MaxHeap{
	public:
	int heapSize;
    
    int left(int i) {
        return (i << 1) + 1;
    }
    
    int right(int i) {
        return (i << 1) + 2;
    }
    
    void maxHeapify(vector<int>& nums, int i) {
        int largest = i, l = left(i), r = right(i);
        if (l < heapSize && nums[l] > nums[largest]) {
            largest = l;
        }
        if (r < heapSize && nums[r] > nums[largest]) {
            largest = r;
        }
        if (largest != i) {
            swap(nums[i], nums[largest]);
            maxHeapify(nums, largest);
        }
    }
    
    void heapify(vector<int>& nums) {
        heapSize = nums.size();
        for (int i = (heapSize >> 1) - 1; i >= 0; i--) 
            maxHeapify(nums, i);
    }

	void push(vector<int> & nums, int n){
		nums.push_back(n);
		heapify(nums);
	}

	int pop(vector<int> & nums) {
		int n = nums.front(), m = nums.back(); 
		nums[0] = m; 
		nums.pop_back(); 
		heapify(nums);
		return n; 
	}
};
int main(int arg, char const *argv[]){
    return 0;
}