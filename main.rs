
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = vec![2,3,4]; 
	println!("{:?}", question::Solution::build_array(ns, 9));
}

