
mod question; 

fn main(){
	let ns = vec![vec![1_i32,4], vec![2_i32,3], vec![3_i32,4]];
	println!("{:?}", question::Solution::find_right_interval(ns));
}

