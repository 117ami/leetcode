
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = [[1, 1, 1], [1, 1, 0], [1, 0, 1]].iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();
	println!("{:?}", question::Solution::flood_fill(ns, 1, 1, 2));
}

