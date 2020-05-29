Idea behind:
1. if node `n` not been visited, then mark it as 0.
2. if node `n` is being visited, then mark it as -1. If we find a vertex marked as -1 in `dfs`, then there is a cycle.
3. if node `n` has been visited, then mark it as 1. If a vertex was marked as 1, then no circle contains `n` or its successors

```rust
impl Solution {
    pub fn dfs(n: i32, depends: &Vec<Vec<i32>>, visited: &mut Vec<i32>) -> bool {
        let n = n as usize;
        if visited[n] == -1 {
            return false;
        }
        if visited[n] == 1 {
            return true;
        }
        visited[n] = -1;
        for m in depends[n].iter() {
            if !Self::dfs(*m, depends, visited) {
                return false;
            }
        }
        visited[n] = 1;
        true
    }
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut depends: Vec<Vec<i32>> = vec![vec![]; num_courses as usize];
        for pre in prerequisites.iter() {
            depends[pre[0] as usize].push(pre[1]);
        }
        let mut visited = vec![0; num_courses as usize];

        (0..num_courses)
            .map(|n| Self::dfs(n as i32, &depends, &mut visited))
            .all(|b| b)
    }
}
```