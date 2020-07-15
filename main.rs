
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = " just some ran      e  ".to_string();
	println!("{:?}", question::Solution::reverse_words(x));
}

