
### Observations

1. The graph is in a form of tree, and there is no cycles
2. The time of collecting apples of a node depends on and only on its children node

On these two facts, the first idea comes to my mind is **DFS**: at each node we check if its children has any apples, and accumulate the time of collecting apples to our final result `res`. To illustrate, let's consider a child `c`,
1. if `c` has apple or someone from its offspring has an apple, then the total time of traversing this subtree is `2 + dfs(c)`. Here `2` means the time of walking down to `c` + the time of walking back; 
2. none of `c` and its children has an apple, then no value is added to `res`


### Rust Solution
The returned value of `dfs()` has 3 possibilities:
1. `dfs(c) = -1`, means `c` has no apple and none of its offspring, if any, has an apple
2. `dfs(c) = 0`, means `c` has an apple and it is a **leaf node**
3. `dfs(c) > 0`, means `c` has at least one offspring that has an apple

```rust
impl Solution {
    pub fn dfs(node: i32, cc: &HashMap<i32, Vec<i32>>, has_apple: &Vec<bool>) -> i32 {
        if !cc.contains_key(&node) {
            if has_apple[node as usize] { 0 } else { -1 }
        } else {
            let mut res = 0; 
            for c in &cc[&node] {
                let m = Solution::dfs(*c, cc, has_apple); 
                res += if m >= 0 { m + 2 } else { 0 };
            }
            if res > 0 || has_apple[node as usize] { res } else { -1 }
        }
    }

    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        let mut cc:HashMap<i32, Vec<i32>> = HashMap::new();
        for e in edges.iter() {
            if !cc.contains_key(&e[0]){
                cc.insert(e[0], Vec::new());
            }
            cc.get_mut(&e[0]).unwrap().push(e[1]);
        }
        max(Self::dfs(0, &cc, &has_apple), 0)
    }
}
```
