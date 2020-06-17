
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![9,9,9];
	println!("{:?}", question::Solution::plus_one(x));
}

