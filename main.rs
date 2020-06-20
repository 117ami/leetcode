
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	// let cs = vec![3, 0, 1, 5,6];
	let cs = vec![100];
	println!("{:?}", question::Solution::h_index(cs));
}

