def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    answer = (x // 100 < 1 and x // 10 == x % 10) or (x // 100 > 1 and x // 100 == x % 10)
    return answer

print(main(535))