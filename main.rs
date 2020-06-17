
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ws = vec!["word".to_string(), "world".into(), "row".into()];
	let o = "worldabcefghijkmnpqstuvxyz".to_string();
	println!("{:?}", question::Solution::is_alien_sorted(ws, o));
}

