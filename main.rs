
mod question; 

fn main(){
	// let s = "Leeecode@mail.cn".to_string();
	let s = "091234567829".to_string();
	println!("{:?}", question::Solution::mask_pii(s));
}

