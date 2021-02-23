"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

def make_permutations(list_of_items):
    if len(list_of_items) == 0:
        # return []
        yield []
    elif len(list_of_items) == 1:
        # return list_of_items
        yield list_of_items
    else:
        list_ = []
        for i in range(len(list_of_items)):
            target = list_of_items[i]
            rest = list_of_items[:i] + list_of_items[i+1:]

            
            for permutation in make_permutations(rest):
                yield [target] + permutation
        return list_




def main():
    target_string = '0123456789'
    string_as_list = list(target_string)
    string_as_list.sort()

    nth_number = 1000000
    list_of_perms = []
    
    for p in make_permutations(string_as_list):
        list_of_perms.append(p)

    term = ''.join(list_of_perms[nth_number])
    print(f'The {nth_number}th permutations is {term}')
        

main()

