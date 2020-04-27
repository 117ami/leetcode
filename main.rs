
mod question; 

fn main(){
	let words = vec!["apple".to_string()];
	let wf = question::WordFilter::new(words);
	println!("{:?}", wf.f("a".to_string(), "eee".to_string()));
	
	let x = "Apple".to_string();
	println!("{:?}", vec![&x[3..], &x[..3]].join("."));
}

