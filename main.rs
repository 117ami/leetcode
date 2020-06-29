
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ns = vec![1,2,3,4,5,-6];
	println!("{:?}", question::Solution::can_arrange(ns, 7));
}

