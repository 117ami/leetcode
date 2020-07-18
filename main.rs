
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![vec![3, 1], vec![3, 2], vec![2, 0], vec![1, 0], vec![0, 2]];
	println!("{:?}", question::Solution::find_order(4, x));
}

