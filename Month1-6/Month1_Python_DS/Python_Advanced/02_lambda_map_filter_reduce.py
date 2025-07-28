from functools import reduce

def main():
    # Task1 (Double a List)
    number = [1,2,3,4,5]
    doubled = list(map(lambda x:x * 2, number))
    print(f"Doubled :{doubled}")
    # Task2 (even number)
    evens = list(filter(lambda x: x % 2 == 0,number))
    print(f"Even Numbers: {evens}")
    # Task3 (Factorial)
    factorial = reduce(lambda x,y:x *y,number)
    print(f"Factorial of 5: {factorial}")
    # Task4 (Sortlist of tuple)
    pairs = [(1, 4), (3, 1), (5, 2), (10, 0)]
    sorted_pairs = sorted(pairs,key=lambda x: x[1])
    print(f"Sorte by second element: {sorted_pairs}")
if __name__ == "__main__":
    main()