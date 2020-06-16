
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a  =vec![3, 3, 5, 0, 0, 3, 1, 4];
	println!("{:?}", question::Solution::max_profit(a));
}

