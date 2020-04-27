
mod question; 

fn main(){
	let mat = vec!["10100".chars().collect::<Vec<char>>(), "10111".chars().collect::<Vec<char>>(), "11111".chars().collect::<Vec<char>>(), "10010".chars().collect::<Vec<char>>()];
	// println!("{:?}", mat);
	println!("{:?}", question::Solution::maximal_square(mat));
}

