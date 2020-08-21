
def splitArraySameAverage(A: List[int]) -> bool:
    ''' Use Python's big number to solve the problem. 
    Given A = [1, 2, 3, 4, 5], all possible sums of all sublists are  
    {1} = 1, {2} = 2, ...
    {1, 2} = 3, {1, 3} = 4, ...
    {1, 2, 3} = 6, {1, 2, 4} = 7, ...
    We can compress the sums of lists with same length k in a single number s_k by
    doing 'bit or' operation. For A = [1,2,3,4,5], sums of lists with length 1 is
    1, 2, 3, 4, 5, which can be independently represented by 1<<1, 1<<2, 1<<3, 1<<4,
    1<<5. The sum is 62, which is stored in cc[1] = 62 

    Compressed sums of lists with length 2 is stored in cc[2] = 1016. In detail
    1016 = 1 << 3 + 1 << 4 + 1 << 5 * 2 + 1 << 6 * 2 + 1 << 7 + 1 << 8 + 1 << 9 
    ... 
    
    Finally, to check if there is a sublist with length k and sum M, we can simply do
    cc[k] & (1 << M).
    '''
    _sum, n = sum(A), len(A)
    cc = [1] + [0] * n
    for a in A:
        for k in range(n - 1, 0, -1):
            cc[k] |= cc[k - 1] << a
            print(cc)

    return any(_sum * i % n == 0 and cc[i] & (1 << (_sum * i // n))
                for i in range(1, n))

