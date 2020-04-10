
mod question; 

fn main(){
	let s = "LEETCODE".to_string();
	println!("{:?}", question::Solution::unique_letter_string(s));
}

