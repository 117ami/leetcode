
mod question; 

fn main(){
	let s = "annabelle".to_string(); 
	// let s = "leetcode".to_string(); 
	
	println!("{:?}", question::Solution::can_construct(s, 3));
}

