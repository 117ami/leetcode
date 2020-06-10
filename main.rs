
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![1,3,5,6];
	println!("{:?}", question::Solution::search_insert(x, 7));
}

