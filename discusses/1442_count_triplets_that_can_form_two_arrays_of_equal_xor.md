
Observe the following facts: 

1. if `a[p] ^ a[p+1] ^ ... ^ a[q] = 0`, then for any `p <= i < q`, we have `n1 = a[p] ^ ... ^ a[i] == n2 = a[i+1] ^ ... a[q]`. The number of such `i` is at most `q - p`.  

2. if `a[0] ^ ... ^ a[i] = n` and `a[0] ^ ... ^ a[j] = n` for some integer `n`,  and `i < j`, then `a[i+1] ^ ... ^ a[j] = 0`.

Then the question turns into finding all pairs `(i, j)` such that `a[0] ^ ... ^ a[i] == a[0] ^ ... ^ a[j]`, and the sum of those `j - i - 1` is the result. 

The rest is straightforward. 

### Rust Code
```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        let (mut res, mut cur) = (0, 0); 
        let mut cc: HashMap<i32, (i32, i32)> = HashMap::new(); 
        cc.insert(0, (-1, 1));

        for (i, a) in arr.iter().enumerate() {
            cur ^= a; 
            if ! cc.contains_key(&cur) {
                cc.insert(cur, (i as i32, 1)); 
            } else {
                let old = cc[&cur];
                let pre_sum = old.0;
                let cnt_cur = old.1; 
                res += (i as i32 - 1) * cnt_cur - pre_sum; 
                cc.insert(cur, (i as i32 + pre_sum, cnt_cur + 1));
            }
        }
        res 
    }
}
```