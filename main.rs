
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let x= vec![vec![0, 0, 1, 0], vec![0, 1, 1, 0]];
	let grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]];
	let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();
	println!("{:?}", question::Solution::island_perimeter(vg));
}

