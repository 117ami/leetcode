`O(n)` time complexity algorithm is trivial, since every element appears exactly twice except one. `xor` all elements gives us the result.

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
```

But we can do better than `O(n)` with binary search.

The key point is, every time we meet an index `mid`, we need to check whether the number `nums[mid]` appears twice. Based on the parity of `mid`, two cases to consider: 

1. `mid % 2 == 0`, we need to compare `nums[mid] == nums[mid+1]`
2. `mid % 2 == 1`, we need to compare `nums[mid] == nums[mid-1]`

The above two steps can merge into one `nums[mid] == nums[mid ^ 1]`, the rest is straightforward. 


### Rust Solution 
```rust
impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {
        let (mut lo, mut hi, mut mid) = (0, nums.len() - 1, 0);
        while lo < hi {
            mid = lo + (hi - lo) / 2; 
            if nums[mid] == nums[mid ^ 1] { lo = mid + 1 }
            else { hi = mid }
        }
        nums[lo]
    }
}
```