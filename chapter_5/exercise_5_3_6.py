"""Campus IL self.py — exercise 5.3.6."""

def fix_age(age):
    """Return zero for teenage ages except 15 and 16; otherwise return age."""
    if 13 <= age <= 19 and age not in (15, 16):
        return 0
    return age


def filter_teens(a=13, b=13, c=13):
    """Return the sum of the three ages after applying fix_age."""
    return fix_age(a) + fix_age(b) + fix_age(c)

def main():
    print(filter_teens())
    print(filter_teens(2, 1, 15))


if __name__ == "__main__":
    main()
