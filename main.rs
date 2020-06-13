
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	// let x = vec![1,3,9,18,90,180,360,720,54, 108];
	let x=vec![1];
	println!("{:?}", question::Solution::largest_divisible_subset(x));
}

