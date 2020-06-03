
mod question; 

// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let input = vec![vec![10,20],vec![30_i32,200],vec![400_i32,50],vec![30_i32,20]];
	println!("{:?}", question::Solution::two_city_sched_cost(input));
}

