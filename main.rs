
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![1,2,1,8,2,1,2,12,0];
	println!("{:?}", question::Solution::top_k_frequent(x, 2));
}

