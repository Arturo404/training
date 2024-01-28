from functools import reduce


if __name__ == "__main__":
    fibonacci = lambda n: reduce(lambda fib_list, _: fib_list + [ fib_list[-1]+fib_list[-2] ], range(n-1), [0,1])[n]
    

    n = input("Input a number: ")

    print(fibonacci(int(n)))
