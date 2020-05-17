
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let st = vec![9,8,7,6,5,4,3,2,1]; 
	let et = vec![10,10,10,10,10,10,10,10,10]; 
	println!("{:?}", question::Solution::busy_student(st, et, 5));
}

