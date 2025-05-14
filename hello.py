import sys

def get_name():
    """Get user name with error handling"""
    try:
        name = input("Enter your name: ")
        if not name.strip():
            print("Name cannot be empty!")
            return get_name()
        return name.strip()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

def main():
    print("Hello, Git!")
    print("Enhanced version with error handling")
    name = get_name()
    print(f"Welcome to Git, {name}!")

if __name__ == "__main__":
    main()