import os
import sys


def main():
    print("Hello from backend-fastapi!")


if __name__ == "__main__":
    print(f"cwd:{os.getcwd()}")
    print(f"package:{__package__}")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    main()
