
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	for i in 808200..808209 {
		println!("{:?}", if question::Solution::is_perfect_square(i) { i} else { 0 });
	}
}

