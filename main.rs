
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let s = "i use triple pillow".to_string(); 
	let t= "pil".to_string();
	println!("{:?}", question::Solution::is_prefix_of_word(s, t));
}

