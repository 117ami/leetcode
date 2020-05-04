
We use `preidx` to cache the index of previous `1`. 

Iterate over vector `num`, if the current value is `1`, then check if the distance of previous `1` if larger than `k`, i.e., `assert(i - preidx) > k`. If the distance is larger than `k`, then reset `preidx`; if not, return `false`. 

### Rust Code
```rust
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut preidx = -k - 1; 
        for (i, n) in nums.iter().enumerate() {
            if *n == 1 {
                if i as i32 - preidx <= k { return false }
                preidx = i as i32 
            }
        }
        true 
    }
}
```

If you like this post, please vote up, it would be really encouraging. 
And if you have any thoughts, please leave a comment. 
