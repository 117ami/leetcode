
mod question; 

fn main(){
	let matrix = vec![vec![1,2,3], vec![4,5,6], vec![7,8,9]];
	println!("{:?}", question::Solution::find_diagonal_order(matrix));
}

