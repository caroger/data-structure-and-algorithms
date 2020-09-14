""" Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise. """


def is_mutiple(n, m):
    return n % m == 0


""" R-1.2 Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function  cannot use the multiplication, modulo, or division operators. """


def is_even(k):
    return k & 1 == 0


""" R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution. """


def minmax(data_list):
    small = big = data_list[0]
    for i in data_list:
        if i < small:
            small = i
        if i > big:
            big = i
    return (small, big)


""" R-1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n. """


def sum_squares(n):
    ss = 0
    for i in range(1, n):
        ss += i ** 2
    return ss


""" R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function. """


def sum_sequence(n):
    return sum([x for x in range(1, n)])


""" R-1.6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n. """


def sum_squares_odd(n):
    return sum([x ** 2 for x in range(1, n + 1, 2)])


""" R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function. """

""" R-1.8 Python allows negative integers to be used as indices into a sequence such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element? """

"""  j = n+k """


""" R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80? """


def custom_range():
    return [x for x in range(50, 81, 10)]


""" R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8? """


def custom_range2():
    return [x for x in range(8, -9, -2)]


""" R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]. """


def list_com():
    return [2 ** x for x in range(9)]


""" R-1.12 Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function. """

from random import randrange


def my_rand(data):
    idx = randrange(0, len(data))
    return data[idx]


def main():
    # print(f"6 is a multiple of 3? {is_mutiple(6,3)}")
    # print(f"6 is even? {is_even(6)}")
    # input = [1, 3, 5, 6, 8, 2, 3, 4, 7]
    # print(f"the min,max of {input} is {minmax(input)}")
    # print(f"the sum squares of {[x for x in range(1,11)]} is {sum_squares(11)}")
    # print(f"the sum of {[x for x in range(1,11)]} is {sum_sequence(11)}")
    # print(
    #     f"the sum of the squares of all the odd positive integers smaller than 10 is {sum_squares_odd(10)}"
    # )

    # print(f"50,60,70,80? {custom_range()}")
    # print(f"8,6,4,2,0,-2,-4,-6,-8? {custom_range2()}")
    # print(f"1,2,4 ...,128,256? {list_com()}")
    from collections import Counter

    dice = [1, 2, 3, 4, 5, 6]
    cnt = Counter()
    for i in range(100):
        cnt[my_rand(dice)] += 1
    print(cnt.sort())


if __name__ == "__main__":
    main()
