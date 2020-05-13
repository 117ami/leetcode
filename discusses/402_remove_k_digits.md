
Code explanation: 
1. Treat string `res` as a stack 
2. `res.pop()` in `while` loop to make sure digits in `res` are in ascending order 
3. `if` condition in `for` loop to remove leading `0`s

### Rust Solution 
```rust
impl Solution {
    pub fn remove_kdigits(num: String, k: i32) -> String {
        // Treat string `res` as a stack 
        let (mut k, mut res) = (k as usize, "".to_string()); 

        for n in num.chars() {
            // `res.pop()` to make sure digits in `res` are in ascending order 
            while k > 0 && !res.is_empty() && n < res.chars().last().unwrap() {
                k -= 1;
                res.pop(); 
            }
            // removing leading zeros 
            if !res.is_empty() || n != '0' { res.push(n); }
        }

        // make sure remove k digits in total
        while !res.is_empty() && k > 0 { res.pop(); k -= 1;}

        if !res.is_empty() { res } else { "0".to_string() }
    }
}
```