
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "ababab".to_string(); 
	let cs:Vec<char> = s.chars().collect();
	
	println!("{:?}", question::Solution::longest_prefix(s));
}

