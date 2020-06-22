
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	// let x = vec!["gta".to_string(),"gta(1)".into(),"gta".into(),"avalon".into()]; 
	let x = vec!["wano".to_string(),"wano".into(),"wano".into(),"wano".into()];
	println!("{:?}", question::Solution::get_folder_names(x	));
}

