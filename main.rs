
mod question; 

fn main(){
	let g = vec![vec![1,3,1], vec![1,5,1], vec![4,2,1]];
	println!("{:?}", question::Solution::min_path_sum(g));
}

