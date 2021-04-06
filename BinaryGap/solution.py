# import random

def solution(N):
    n_stringified = str(bin(N))
    longest_bin_gap = 0
    temp_str = ''
    for n in range(len(n_stringified) - 1):
        if temp_str and n_stringified[n+1] == '0':
            temp_str += '0'
        elif n_stringified[n] + n_stringified[n+1] == '10':
            temp_str = '0'
        else:
            if len(temp_str) > longest_bin_gap:
                longest_bin_gap = len(temp_str)
            temp_str = ''
    return longest_bin_gap


if __name__ == "__main__":
    class colours:
        GREEN = '\033[92m'
        FAIL = '\033[91m'
        END = '\033[0m'

    # for generating samples
    # sample_tests = random.sample(range(1, 2147483647), 10)
    sample_tests = [1502095624, 934639188, 1721916112, 711207191, 1005624420, 1957471340, 1503517929, 451792506, 1704575297, 1099217942, 561892, 74901729, 1376796946]
    expected_results = [5, 2, 3, 4, 4, 3, 2, 2, 5, 5, 3, 4, 5]
    pass_count = 0
    for i in range(len(sample_tests)):
        print(f'sample: {sample_tests[i]}')
        print(f'sample in bin: {bin(sample_tests[i])}')
        given_result = solution(sample_tests[i])
        print(f'given result: {given_result}')
        print(f'expected result: {expected_results[i]}')
        if given_result == expected_results[i]:
            print(f"{colours.GREEN}PASS{colours.END}")
            pass_count += 1
        else:
            print(f"{colours.FAIL}FAIL{colours.END}")
        print('\n')
    
    print(f'{colours.GREEN}PASSED TESTS{colours.END}: {pass_count}, {colours.FAIL}FAILED TESTS{colours.END}: {len(sample_tests) - pass_count}')