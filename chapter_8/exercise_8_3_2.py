"""Campus IL self.py — exercise 8.3.2."""

from datetime import date

def main():
    person = {"first_name": "Mariah", "last_name": "Carey",
              "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
    choice = int(input("Choose an action (1-7): "))
    if choice == 1:
        print(person["last_name"])
    elif choice == 2:
        print(person["birth_date"].split(".")[1])
    elif choice == 3:
        print(len(person["hobbies"]))
    elif choice == 4:
        print(person["hobbies"][-1])
    elif choice == 5:
        person["hobbies"].append("Cooking")
    elif choice == 6:
        person["birth_date"] = tuple(int(part) for part in person["birth_date"].split("."))
        print(person["birth_date"])
    elif choice == 7:
        today = date.today()
        person["age"] = today.year - 1970 - ((today.month, today.day) < (3, 27))
        print(person["age"])


if __name__ == "__main__":
    main()
