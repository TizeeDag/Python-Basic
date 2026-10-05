"""Campus IL self.py — exercise 5.4.1."""

def func(num1, num2):
    """Add two numbers.

    :param num1: The first number.
    :type num1: int or float
    :param num2: The second number.
    :type num2: int or float
    :return: The sum of the two numbers.
    :rtype: int or float
    """
    return num1 + num2

def main():
    print(func(3, 4))
    help(func)


if __name__ == "__main__":
    main()
