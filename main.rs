
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![1,-2,1];
	println!("{:?}", question::Solution::k_concatenation_max_sum(x, 2));
}

