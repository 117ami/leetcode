
mod question; 

fn main(){
	let ns = vec![2,3,1,1,4];
	println!("{:?}", question::Solution::can_jump(ns));
}

