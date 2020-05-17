
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn capitalize(word: String) -> String { 
	let mut res = word;
	res.chars().take(1).flat_map(char::to_uppercase).chain(res.chars().skip(1)).collect()
}

fn main(){
	println!("{:?}", question::Solution::arrange_words("Glad to see you".to_string()));
	let mut fw = "lowercase".to_string();
	// fw = fw.chars().take(1).flat_map(char::to_uppercase).chain(fw.chars().skip(1)).collect(); 
	// fw = fw.chars().skip(1).collect();
	println!("{:?}", capitalize("apple".to_string()) );
}

