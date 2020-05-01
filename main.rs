
mod question; 

fn main(){
	let ns = vec![2,3,1,2,4,3]; 
	println!("{:?}", question::Solution::min_sub_array_len(7, ns));
}

