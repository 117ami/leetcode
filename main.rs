
mod question; 

fn main(){
	// let nums = vec![vec![1,2,3,4,5],vec![6,7],vec![8],vec![9,10,11],vec![12,13,14,15,16]];
	let nums = vec![vec![1,2,3], vec![4,5,6], vec![7,8,9]];
	println!("{:?}", question::Solution::find_diagonal_order(nums));
}

