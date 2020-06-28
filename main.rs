
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = vec![1,2,3,4];
	println!("{:?}", question::Solution::average(s));
}

