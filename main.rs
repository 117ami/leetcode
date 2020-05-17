
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "cbaebabacd".to_string(); 
	let p = "abc".to_string();
	println!("{:?}", question::Solution::find_anagrams(s,p));
	
}

