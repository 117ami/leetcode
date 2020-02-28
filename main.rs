
mod aux; 
mod question; 

fn main() {
	let v = vec![1,2,3,4];
	println!("{:?}", question::Solution::decompress_rl_elist(v) ); 
}

