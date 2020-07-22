
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){	
	println!("{:?}", question::Solution::num_sub("011".to_string()));
}

