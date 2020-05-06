
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let nums = vec![8,9,8,9,8];
	println!("{:?}", question::Solution::majority_element(nums));
}

