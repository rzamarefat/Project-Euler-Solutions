"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def finder(number_of_digits):
    low = 10 ** number_of_digits
    high = 10 ** (number_of_digits + 1) + 1
    desired_num = 0

    for number in range(low, high):
        if reverse_string(str(number)) == str(number):
            desired_num = number
    
    return desired_num

        
def reverse_string(string):
    string_as_list = list(string)
    reversed_list = []
    
    for i in range(1,len(string_as_list)+1):
        reversed_list.append(string_as_list[-i])
    
    return ''.join(reversed_list)


if __name__ == '__main__':
    print(finder(4))
