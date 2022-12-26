def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = a // 100 >=1 and a // 100 < 10
    return answer

print(main(1500))