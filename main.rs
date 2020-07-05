
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let arr = vec![1,3,5];
	println!("{:?}", question::Solution::can_make_arithmetic_progression(arr));
}

