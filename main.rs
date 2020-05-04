
mod question; 

fn main(){
	let ns = vec![1,1,1,1];
	println!("{:?}", question::Solution::k_length_apart(ns, 0));
}

