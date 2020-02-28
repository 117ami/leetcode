
mod aux; 
mod question; 

fn main() {
	println!("{:?}", question::Solution::num_jewels_in_stones("aA".to_string(), "aAAAACC".to_string())); 
}

