
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x = vec![2,3,4,5,6,7]; 
	println!("{:?}", question::Solution::shuffle(x, 3));
}

