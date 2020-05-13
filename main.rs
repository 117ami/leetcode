
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let h = "abc".to_string(); 
	let n = "bc".to_string();
	println!("{:?}", question::Solution::str_str(h, n));
}

