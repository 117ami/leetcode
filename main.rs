
mod aux; 
mod question; 

fn main() {
	let grid = vec![vec![4,3,2,-1],vec![3,2,1,-1],vec![1,1,-1,-2],vec![-1,-1,-2,-3]];
	println!("{:?}", question::Solution::count_negatives(grid) ); 
}

