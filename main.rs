
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "0010101".to_string();
	println!("{:?}", question::Solution::has_all_codes(s, 2));
}

