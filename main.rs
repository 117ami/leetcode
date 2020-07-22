
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![9, 12, 3];
	println!("{:?}", question::Solution::closest_to_target(x, 5));
}

