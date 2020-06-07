
// let vg = grid.iter().map(|c| c.to_vec()).collect::<Vec<Vec<_>>>();

fn main(){
	let arr = vec![1,2,3,4];
	for n in arr.iter() {
		println!("{}", n);
	}
	println!("{:?}", arr);
}

