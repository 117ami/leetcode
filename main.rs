
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![1,2,3];
	println!("{:?}", question::Solution::subsets(x));
}

