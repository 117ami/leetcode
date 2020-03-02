
mod aux; 
mod question; 

fn main(){
	// let nums = vec![8,1,2,2,3];
	let nums = vec![6,5,4,8];
	println!("{:?}", question::Solution::smaller_numbers_than_current(nums));
}

