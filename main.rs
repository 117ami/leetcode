
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "ab".to_string();
	let t = "bcooooazbccc".to_string();
	println!("{:?}", question::Solution::check_inclusion(s, t));
}

