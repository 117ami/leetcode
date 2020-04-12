
mod question; 

fn main(){
	let words = vec!["mass".to_string(),"as".to_string(),"hero".into(),"superhero".into()];
	println!("{:?}", question::Solution::string_matching(words));
}

