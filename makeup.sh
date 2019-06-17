#
cppfile=$1

cmd='using namespace std;'

add_alias() {
	extra=$(grep $1 'c.cpp' | head -n 1)
	cmd="$cmd $extra \n"
}

extras=('vi' 'vb' 'vc' 'vs' 'vvi' 'vvb' 'pii' 'll' 'ull' 'mii' 'mci' 'si' 'spii' 'umii' 'umci' 'umsi'\
	'vpii'\
	'usi' 'EPS' 'MOD' 'INF' 'MK' 'each' 'eachv' 'up' 'dwn' \
	'reverse_' 'join' 'sum_' 'counter' 'isodd' 'iseven' 'vec_max' 'vec_min' 'unfold' 'isPalindrome' \
	'fi' 'se' 'mp' 'pb' 'dall' 'dsize' 'dsort' 'rdsort' 'dreverse' 'MAX' 'MIN' \
	'reverseStr' 'upper' 'lower' 'exist'\
	'product' 'itos')

for c in ${extras[@]}; do 
	grep --quiet $c $cppfile && add_alias $c 
done

insert_cmd_to_cpp() {
	echo ">>making up for $1"	
	insertline=$(nl $1 | grep 'class' | tail -n 1 | awk '{print $1}')	
	pre=$((insertline - 1))
	head -n $pre $1 > cpp.tmp
	echo -e $cmd >> cpp.tmp
	tail -n +$insertline $1 >> cpp.tmp
	mv cpp.tmp $1
}


insert_cmd_to_cpp $cppfile

# Tidy up
clang-format -i $cppfile


