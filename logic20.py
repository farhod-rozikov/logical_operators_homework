def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    d_1 = n % 10 == 1
    d_1 += n // 10 % 10 == 1
    d_1 += n // 100 % 10 == 1
    d_1 += n // 1000 % 10 == 1
    d_1 += n // 10000

    d_0 = n % 10 == 0
    d_0 += n // 10 % 10 == 0
    d_0 += n // 100 % 10 == 0
    d_0 += n // 1000 % 10 == 0
    
    answer = d_1 > d_0
    return answer

print(main(100))