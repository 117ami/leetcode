
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = vec![2,2,3,3,4,5,5,6,6];
	println!("{:?}", question::Solution::single_non_duplicate(ns));
}

