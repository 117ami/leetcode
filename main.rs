
mod question; 

fn main(){
	let stones = vec![2,3,5,4, 1];
	println!("{:?}", question::Solution::last_stone_weight(stones));
}

