
mod question; 

fn main(){
	// let text = "leetcode.com&frasl;problemset&frasl;all".to_string(); 
	let text = "x &gt; y &amp;&amp; x &lt; y is always false".to_string();
	println!("{:?}", question::Solution::entity_parser(text));
}

