
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let a = vec![1,2,3,4,5];
	println!("{:?}", question::Solution::running_sum(a));
}

