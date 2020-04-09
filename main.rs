
mod question; 

fn main(){
	let tree = vec![1,2,3,1, 2,2];
	println!("{:?}", question::Solution::total_fruit(tree));
}

