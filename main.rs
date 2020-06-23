
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let v = vec![1,2,3,2,1];
	println!("{:?}", question::Solution::single_number(v));
}

