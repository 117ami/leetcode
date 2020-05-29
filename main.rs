
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let pre = vec![vec![1, 0], vec![3, 0], vec![1, 3], vec![2, 0]];
	println!("{:?}", question::Solution::can_finish(4, pre));
}

