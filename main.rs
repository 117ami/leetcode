
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "15.(9)".to_string(); 
	let t = "16".to_string();
	println!("{:?}", question::Solution::is_rational_equal(s, t));
}

