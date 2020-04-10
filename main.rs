
mod question; 

fn main(){
	let s:String = "11011000".to_string();
	let parts = &s[1..6];
	println!("{:?}", question::Solution::make_largest_special(s));
	let x = "1".to_string() + &"001".to_string();
	// println!("{:?}", x);
}

