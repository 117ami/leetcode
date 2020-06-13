
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![8,4,6,2,3];
	println!("{:?}", question::Solution::final_prices(a));
}

