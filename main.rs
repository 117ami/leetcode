
mod question; 

fn main(){
	// let votes = vec!["ABC".to_string(),"ACB".to_string(),"ABC".to_string(),"ACB".to_string(),"ACB".to_string()];
	// let votes = vec!["BCA".to_string(),"CAB".to_string(),"CBA".to_string(),"ABC".to_string(),"ACB".to_string(),"BAC".into()]; 
	let votes = vec!["ZMNAGUEDSJYLBOPHRQICWFXTVK".to_string()];
	println!("{:?}", question::Solution::rank_teams(votes));
}

