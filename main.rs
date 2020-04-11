
mod question; 

fn main(){
	let s = "11000".to_string();
	println!("{:?}", question::Solution::num_steps(s));
}

