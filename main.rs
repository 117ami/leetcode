
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let fc = vec![vec!["leetcode","google","facebook"],vec!["google","microsoft"],vec!["google","facebook"],vec!["google"],vec!["amazon"]].iter().map(|c| c.iter().map(|z| z.to_string()).collect() ).collect::<Vec<Vec<_>>>();
	println!("{:?}", question::Solution::people_indexes(fc));
}

