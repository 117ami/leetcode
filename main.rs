
mod question; 

fn main(){
	let queries = vec![3,1,2,1];
	println!("{:?}", question::Solution::process_queries(queries, 5));
}

