
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![23,2,4,6,7];
	println!("{:?}", question::Solution::check_subarray_sum(a, 6));
}

