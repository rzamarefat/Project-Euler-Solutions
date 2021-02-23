"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


# The Checker of Being Prime for any given number 
def check_prime(number):
    is_prime = True 
    for i in range(2, round(number / 2) + 1):
        if number % i == 0:
            is_prime = False

    return is_prime


def truncatable_prime_finder():
    target_number = 101
    list_of_trnc_primes  = []

    while len(list_of_trnc_primes) < 11:
        left_chunk = str(target_number)[:-1]
        right_chunk = str(target_number)[1:]

        if check_prime(int(left_chunk)) and check_prime(int(right_chunk)):
            list_of_trnc_primes.append(target_number)

        target_number += 1
    return list_of_trnc_primes
        

# Main launch
def main():
    print('The first 11 truncabele prime numbers is a s follows: ')
    list_of_result_truncatable_primes = truncatable_prime_finder()
    print(list_of_result_truncatable_primes)

    result = 0
    for num in list_of_result_truncatable_primes:
        result += int(num) 
    
    print(f'The result of the desired sum is: {result}')
    

if __name__=='__main__':
    main()



