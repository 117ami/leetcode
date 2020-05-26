
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a  = vec![8,7,9];
	println!("{:?}", question::Solution::partition_disjoint(a));
}

