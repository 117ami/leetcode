
mod question; 

fn main(){
	let ps = vec![5,3, 4,5];
	println!("{:?}", question::Solution::stone_game(ps));
}

