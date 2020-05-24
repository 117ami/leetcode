
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "leetcode".to_string(); 
	println!("{:?}", question::Solution::max_vowels(s, 2));
}

