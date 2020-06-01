
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let tmp = vec![vec![0, 1], vec![3, 2], vec![4,3], vec![1,4]];
	println!("{:?}", question::Solution::min_reorder(5, tmp));
}

