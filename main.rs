
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![2,5,3,6,3];
	println!("{:?}", question::Solution::max_product(a));
}

