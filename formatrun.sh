# 
if [[ $1 == *.cpp ]]; then	# for cpp program
    # clang-format -i $1
    if [ -f a.out ]; then 
	rm a.out
    fi
    g++ -std=c++11 $1

    if [ -f a.out ];then	# in case the compile procedure failed
	time ./a.out
    fi
else				# for ruby program
    #rubocop -i $1
    time ruby $1 
fi

