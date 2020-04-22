
mod question; 

fn main(){
	let v = vec![1,1,1];
	println!("{:?}", question::Solution::subarray_sum(v, 2));
}

