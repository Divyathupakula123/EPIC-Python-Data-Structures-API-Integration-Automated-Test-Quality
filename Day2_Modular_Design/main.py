from parser import parse_json
from validator import validate_book


def main():
    user_input = input("Enter book data as JSON: ")

    try:
        data = parse_json(user_input)
        validate_book(data)
        print("Success! Book data is valid.")
        print(data)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()