
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	// let a = vec![1,1,1,2,2,3];
	let a = vec![4,3,1,1,3,3,2];
	println!("{:?}", question::Solution::find_least_num_of_unique_ints(a,3));
}

