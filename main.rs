
mod aux; 
mod question; 

fn main() {
	let p = vec![vec![1,1], vec![3,4], vec![-1,0]];
	println!("{:?}", question::Solution::min_time_to_visit_all_points(p) ); 

	let sum = (1..10).fold(0, |_sum, n| _sum + n);
	println!("{}", sum);
}

