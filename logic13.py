def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = (a // 10 + a % 10) % 2 == 0
    return answer

print(main(31))