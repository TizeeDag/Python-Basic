"""Campus IL self.py — exercise 8.2.4."""

def sort_anagrams(list_of_strings):
    """Group anagrams, preserving first group appearance and word order."""
    groups = {}
    for word in list_of_strings:
        signature = "".join(sorted(word))
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)
    return list(groups.values())

def main():
    print(sort_anagrams(["deltas", "desalt", "pants", "salted"]))


if __name__ == "__main__":
    main()
