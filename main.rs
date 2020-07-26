
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "codeleet".to_string();
	let indices = vec![4, 5, 6, 7, 0, 2, 1, 3];
	println!("{:?}", question::Solution::restore_string(s, indices));
}

