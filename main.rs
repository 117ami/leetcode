
mod question; 

fn main(){
	let A = vec![-5266,4019,7336,-3681,-5767];
	println!("{:?}", question::Solution::constrained_subset_sum(A, 2));
}

