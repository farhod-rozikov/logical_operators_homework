def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    d_1 = a % 10
    d_2 = a // 10 % 10
    d_3 = a // 100 % 10
    d_4 = a // 1000 % 10
    d_5 = a // 10000
    answer = d_5 > d_4 and d_4 > d_3 and d_3 > d_2 and d_2 > d_1
    return answer

print(main(12345))