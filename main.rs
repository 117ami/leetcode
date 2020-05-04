
mod question; 

fn main(){
	let path = vec![vec!["London".to_string(),"New York".into()], vec!["New York".into(),"Lima".into()], vec!["Lima".into(),"Sao Paulo".into()]];
	println!("{:?}", question::Solution::dest_city(path));
}

