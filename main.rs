
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = vec![2,3,1,6,7];
	println!("{:?}", question::Solution::count_triplets(ns));
}

