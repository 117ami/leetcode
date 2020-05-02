
mod question; 

fn main(){
	let a = vec![2,-1,2];
	println!("{:?}", question::Solution::shortest_subarray(a, 3));
}

