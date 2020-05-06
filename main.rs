
mod question; 

fn main(){
	let v = vec![1_i32, 7, 11]; 
	let v2 = vec![2_i32, 4, 6];
	println!("{:?}", question::Solution::k_smallest_pairs(v, v2, 3));
}

