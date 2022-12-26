from numpy import ma


def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = a > 9 and a < 100
    return answer

print(main(10))