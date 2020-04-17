
mod question; 

fn main(){
	let sample = vec![0, 1, 4, 2, 2];
	println!("{:?}", question::Solution::sample_stats(sample));
}

