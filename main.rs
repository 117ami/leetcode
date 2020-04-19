
mod question; 

fn main(){
	let nums = vec![1, -2, -3];
	println!("{:?}", question::Solution::min_start_value(nums));
}

