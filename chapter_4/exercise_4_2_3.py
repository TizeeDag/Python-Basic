"""Campus IL self.py — exercise 4.2.3."""

def main():
    temperature = input("Insert the temperature you would like to convert: ")
    value = float(temperature[:-1])
    if temperature[-1].upper() == "F":
        print(f"{(value - 32) * 5 / 9:g}C")
    else:
        print(f"{value * 9 / 5 + 32:g}F")


if __name__ == "__main__":
    main()
