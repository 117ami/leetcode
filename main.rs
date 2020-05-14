
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let mut obj = question::Trie::new();
	obj.insert("apple".to_string());
	println!("{:?}", obj.prefixes);

	println!("{}", obj.search("apple".to_string()));
	println!("{}", obj.search("app".to_string()));
	println!("{}", obj.starts_with("app".to_string()));
	obj.insert("app".to_string());
	println!("{}", obj.search("app".to_string()));

}

