
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![1,3,2];
	let b = vec![9,3,1];
	println!("{:?}", question::Solution::can_be_equal(a, b));
}

