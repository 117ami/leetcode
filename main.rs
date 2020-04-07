
mod question; 

fn main(){
	let s = "tree".to_string(); 
	println!("{:?}", question::Solution::frequency_sort(s));
}

