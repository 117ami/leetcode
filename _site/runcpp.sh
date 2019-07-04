
if [ -f a.out ]; then 
	rm a.out
fi

g++ -std=c++11 test.cpp 
time ./a.out
