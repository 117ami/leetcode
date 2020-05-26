
This problem is actually asking us to find the minimum index `i` such that the **maximum** element of the sub-array `a[:i]` (not including `a[i]`) is less than or equal to the **minimum** element of the right part `a[i:]`. 

Given this, we can find the answer in one pass with the help of two auxiliary variables, (1) `pre_max`: the maximum value of `a[:pos]` for an index `pos`, and (2) `total_max`: the current maximum value as we loop over the array.

During the iteration, when we find the current value `n` is smaller than `pre_max`, we know `pos` can NOT be the answer, since `max(a[:pos] = pre_max > n`. We have to update our index `pos` to current index `i` and `pre_max` to the maximum value of `a[:i]`, which is exactly `total_max`. 

Since it is guaranteed there is at least one way to partition A as described. We do not need to worry about corner cases where we find no such valid index.

### Rust solution

```rust
impl Solution {
    pub fn partition_disjoint(a: Vec<i32>) -> i32 {
        let mut pre_max = a[0]; 
        let mut total_max = a[0];
        let mut pos = 0; 
        for (i, n) in a.iter().enumerate() {
            if pre_max > *n {
                pre_max = total_max; 
                pos = i; 
            } else if total_max < *n {
                total_max = *n ;
            }
        }
        1 + pos as i32 
    }
}
```