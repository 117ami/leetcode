
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let p = vec![3,2,6,5,0,3];
	println!("{:?}", question::Solution::max_profit(2, p));
}

