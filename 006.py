"""

The sum of the squares of the first ten natural numbers is,
$$1^2 + 2^2 + ... + 10^2 = 385$$
The square of the sum of the first ten natural numbers is,
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def sum_of_squares(nth_number):
    result = 0
    for i in range(1, nth_number + 1):
        result += i ** 2

    return result



def square_of_sum(nth_number):
    result = 0
    for i in range(1, nth_number + 1):
        result += i 

    return result ** 2


def main():
    nth_number = 100
    difference = square_of_sum(100) - sum_of_squares(100)
    print(f'The difference is: {difference}')


if __name__ == '__main__':
    main()


