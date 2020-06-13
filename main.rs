
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let v = vec![6,7,11,7,6,8, 100_000];
	println!("{:?}", question::Solution::get_strongest(v, 5));
}

