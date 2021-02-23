"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def find_sum(range_upper_limit):
    result_of_sum = 0
    for i in range(range_upper_limit + 1):
        string_as_int = int(f'{i}{i}')
        result_of_sum += string_as_int
    print(result_of_sum)
    return result_of_sum 

def find_last_digits(number):
    number_as_str = str(number)
    number_as_list = list(number_as_str)
    print(number_as_list[-10:])


range_number = 1000
find_last_digits(find_sum(range_number))