<!-- If you're familiar with [KMP algorithm](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/), then you must have heard the term **longest proper prefix**.

Finding the **longest proper prefix** of a string is an essential part of the famous KMP algorithm, and that prefix is exactly the **longest happy prefix** we're looking for.

Given a string `s` of length `n`, a brute-force method iterates each prefix of `s`, and decides whether it is also a suffix, and returns one with maximum length in the end. 

Time complexity of this method is `O(n^2)`.  -->

Finding the **longest happy prefix** of a string is actually the preprocessing part of the famous KMP algorithm. 

A great article on this topic can be found [here: KMP Algorithm for Pattern Searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/).



### Rust Solution 
Time / space complexity `O(n)`
```rust
impl Solution {
    pub fn longest_prefix(s: String) -> String {
        let (mut pre_len, mut i) = (0, 1); 
        let mut lps = vec![0; s.len()];
        let cs: Vec<char> = s.chars().collect(); 
        while i < s.len() {
            if cs[i] == cs[pre_len] {
                pre_len += 1; 
                lps[i] = pre_len; 
                i += 1; 
            } else {
                if pre_len == 0 {
                    lps[i] = 0; 
                    i += 1; 
                } else {
                    pre_len = lps[pre_len - 1] as usize; 
                }
            }
        }
        s[..*lps.last().unwrap()].to_string()
    }
}
```