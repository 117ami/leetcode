
mod question; 

fn main(){
	let s = "001110".to_string();
	println!("{:?}", question::Solution::max_score(s));
}

