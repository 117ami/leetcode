
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = "1000".to_string(); 
	println!("{:?}", question::Solution::remove_kdigits(ns, 3));
}

