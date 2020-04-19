
mod question; 

fn main(){
	let s = "0123dcafd".to_string();
	// let s = "leetcode".to_string();
	println!("{:?}", question::Solution::reformat(s));
}


