
mod question; 

fn main(){
	let s = "abd".to_string(); 
	let t = "aab".to_string();
	println!("{:?}", question::Solution::can_construct(s, t));
}

