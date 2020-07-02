
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	// let x = vec![2,3,3,4,6,7];
	let x = vec![7,10,7,3,7,5,4]; 
	println!("{:?}", question::Solution::num_subseq(x, 12));
}

