
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = "aba".to_string();
	println!("{:?}", question::Solution::valid_palindrome(a));
}

