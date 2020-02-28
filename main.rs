
mod aux; 
mod question; 

fn main() {
	let nums = vec![555,901,482,1771]; 
	println!("{:?}", question::Solution::find_numbers(nums) ); 
}

