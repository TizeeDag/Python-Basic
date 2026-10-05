"""Campus IL self.py — exercise 7.2.6."""

def main():
    products = input("Enter products separated by commas: ").split(",")
    while True:
        choice = int(input("Choose an action (1-9): "))
        if choice == 1:
            print(products)
        elif choice == 2:
            print(len(products))
        elif choice == 3:
            print(input("Enter a product: ") in products)
        elif choice == 4:
            print(products.count(input("Enter a product: ")))
        elif choice == 5:
            product = input("Enter a product: ")
            if product in products:
                products.remove(product)
        elif choice == 6:
            products.append(input("Enter a product: "))
        elif choice == 7:
            for product in products:
                if len(product) < 3 or not product.isalpha():
                    print(product)
        elif choice == 8:
            unique = []
            for product in products:
                if product not in unique:
                    unique.append(product)
            products = unique
        elif choice == 9:
            break


if __name__ == "__main__":
    main()
