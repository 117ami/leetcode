
mod question; 

fn main(){
	let ns = vec![1,3,-1,-3,5,3,6,7];
	println!("{:?}", question::Solution::max_sliding_window(ns, 3));
}

