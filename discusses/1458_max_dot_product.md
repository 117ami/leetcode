
A typical DP problem, where `dp[i][j]` is the maximum dot product we can get from `A[0:i]` (not including `i`) x `B[0:j]` (not including `j`).

Base case `dp[0][0]` is trivial, we can not do anything but assuming it contains a very small number, `-inf` for instance. 

When `i > 0 and j > 0`, we consider cases where:
1. `A[i-1]` is not chosen, then `dp[i][j] = max(dp[i][j], dp[i-1][j])`, 
2. `B[j-1]` is not chosen, then `dp[i][j] = max(dp[i][j], dp[i][j-1])`, 
3. none of `A[i-1]` and `B[j-1]` is chosen, then `dp[i][j] = max(dp[i][j], dp[i-1][j-1])`, 
4. otherwise, `dp[i][j] = max(dp[i][j], A[i-1] * B[j-1] + max(0, dp[i-1][j-1]))`

Time complexity `O(mn)`, space `O(mn)`. 

We can reduce space complexity to `O(n)` by using an auxiliary vector, as shown in codes below, to cache previous calculated results.

### Rust solution

```rust
impl Solution {
    pub fn max_dot_product(A: Vec<i32>, B: Vec<i32>) -> i32 {
        let m = A.len();
        let n = B.len();
        let mut dp = vec![-0x3f3f3f3f; n + 1];
        
        for i in 1..m + 1 {
            let old = dp.to_vec();
            for j in 1..n + 1 {
                dp[j] = max(old[j], dp[j]);
                dp[j] = max(old[j - 1], dp[j]);
                dp[j] = max(dp[j - 1], dp[j]);
                dp[j] = max(dp[j], max(old[j - 1], 0) + A[i - 1] * B[j - 1]);
            }
        }
        *dp.last().unwrap()
    }
}
```