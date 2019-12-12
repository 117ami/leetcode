# https://leetcode.com/problems/fizz-buzz-multithreaded
# Medium (Difficulty)

# Write a program that outputs the string representation of numbers from 1 to n, however:
# For example, for n = 15, we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.
# Suppose you are given the following code:
# Implement a multithreaded version of FizzBuzz with four threads. The same instance of FizzBuzz will be passed to four different threads:
# class FizzBuzz {
#   public FizzBuzz(int n) { ... }               // constructor
#   public void fizz(printFizz) { ... }          // only output "fizz"
#   public void buzz(printBuzz) { ... }          // only output "buzz"
#   public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
#   public void number(printNumber) { ... }      // only output the numbers
# }
# xxxxxxxxxx
# class FizzBuzz {
# private:
#     int n;
# ​
# public:
#     FizzBuzz(int n) {
#         this->n = n;
#     }
# ​
#     // printFizz() outputs "fizz".
#     void fizz(function<void()> printFizz) {
#         
#     }
# ​
#     // printBuzz() outputs "buzz".
#     void buzz(function<void()> printBuzz) {
#         
#     }
# ​
#     // printFizzBuzz() outputs "fizzbuzz".
#     void fizzbuzz(function<void()> printFizzBuzz) {
#         
#     }
# ​
#     // printNumber(x) outputs "x", where x is an integer.
#     void number(function<void(int)> printNumber) {
#         
#     }
# };
import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.f = threading.Semaphore(0)
        self.b = threading.Semaphore(0)
        self.fb = threading.Semaphore(0)
        self.n = threading.Semaphore(0)
        self.c = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 > 0:
                self.f.acquire()
                printFizz()
                self.c += 1
                if self.c % 5 == 0:
                    self.b.release()
                else:
                    self.n.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 5 == 0 and i % 3 > 0:
                self.b.acquire()
                printBuzz()
                self.c += 1
                if self.c % 3 == 0:
                    self.f.release()
                else:
                    self.n.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 15 == 0:
                self.fb.acquire()
                printFizzBuzz()
                self.c += 1 
                self.n.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            if i % 5 and i % 3:
                self.n.acquire()
                printNumber(i)
                self.c += 1
                if self.c % 15 == 0:
                    self.fb.release()
                elif self.c % 5 == 0:
                    self.b.release()
                elif self.c % 3 == 0:
                    self.b.release()
                else:
                    self.n.release()

        

