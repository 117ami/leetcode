
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = vec![1,1,2,2,2,2];
	println!("{:?}", question::Solution::three_sum_multi(ns, 5));
}

