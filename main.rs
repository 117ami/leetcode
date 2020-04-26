
mod question; 

fn main(){
	let cp = vec![1,2,3,4,5,6,1];
	println!("{:?}", question::Solution::max_score(cp, 3	));
}

