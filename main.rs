
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let ps = vec![vec![0, 0],vec![3, 0], vec![9, 2]];
	println!("{:?}", question::Solution::find_max_value_of_equation(ps, 3	));
}

