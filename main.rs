
mod question; 

fn main(){
	let nums = vec![1_i32, 2, 3, 4];
	println!("{:?}", question::Solution::product_except_self(nums));
}

