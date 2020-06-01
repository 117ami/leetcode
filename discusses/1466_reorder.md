
Width-First-Search, use a vector `visited` to keep track of visited city. 

At each time when we found a pair `(a, b)` such that city `a` has  been visited (`b` has NOT been visited since there is only one way to travel between two different cities), we should reverse `(a, b)` to make sure `b` is connected to city `0`, and thus add `cnt` by 1.

```rust 
impl Solution {
    pub fn min_reorder(n: i32, ref mut connections: Vec<Vec<i32>>) -> i32 {
        let mut cnt = 0; 
        let mut visited: Vec<bool> = vec![false; n as usize];
        visited[0] = true; 
        while true {
            let mut tmp = vec![];
            for pair in connections.iter() {
                let (a, b) = (pair[0] as usize ,pair[1] as usize);
                if visited[a] {
                    visited[b] = true; 
                    cnt += 1; 
                } else if visited[b] {
                    visited[a] = true; 
                } else {
                    tmp.push(vec![a as i32, b as i32]);
                }
            }
            *connections = tmp;
            if connections.len() == 0 { return cnt }
        }
        cnt 
    }
}
```