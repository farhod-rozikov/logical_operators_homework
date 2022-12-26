def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = a // 10000 >= 1 and a // 10000 < 10
    return answer

print(main(12345))