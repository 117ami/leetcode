
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![1,2,3,4];
	println!("{:?}", question::Solution::can_partition(a));
}

