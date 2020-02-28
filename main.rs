
mod aux; 
mod question; 

fn main() {
	println!("{:?}", question::Solution::balanced_string_split("RLLLLRRRLR".to_string()) ); 
}

