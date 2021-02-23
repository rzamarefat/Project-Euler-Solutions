"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def check_prime(number):

    for i in range(2, round(number / 2)):
        if number % i == 0:
            return False

    return True


def main(nth_number):
    prime_numbers = []
    
    i = 2
    while len(prime_numbers) < nth_number:
        i += 1
        if check_prime(i):
            prime_numbers.append(i)
    
    print(prime_numbers)
    print(f'The {nth_number}st prime number is: ', prime_numbers[-1])




if __name__ == '__main__':
    nth_number = 6
    main(nth_number)