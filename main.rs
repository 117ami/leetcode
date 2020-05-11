
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let mat = [[1,10,10],[1,4,5],[2,3,6]].iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();
	println!("{:?}", question::Solution::kth_smallest(mat, 12));
}

