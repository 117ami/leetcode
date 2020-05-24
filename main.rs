
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let A = vec![3,-2];
	let B = vec![2,-6,7];
	println!("{:?}", question::Solution::max_dot_product(A,B));
}

