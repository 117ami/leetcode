use std::collections::HashMap;
use std::fmt::Debug;
use std::hash::Hash;

#[allow(dead_code)]
pub fn print_map<K: Debug + Eq + Hash, V: Debug>(map: &HashMap<K, V>) {
    for (k, v) in map.iter() {
        println!("{:?}: {:?}", k, v);
    }
}

#[allow(dead_code)]
pub fn say_vec(nums: Vec<i32>){
	println!("{:?}", nums);
}

// #[allow(dead_code)]
// pub fn buildVecOfVec(s: String)->Vec<Vec<i32>>{
//     let mut res: Vec<Vec<i32>> = vec![]; 
//     res 
// }
