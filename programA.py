import sys
import random

# Generates a pseudo-random integer and prints it to stout
def print_random_int():
        print(random.randint(1, 1000))
        sys.stdout.flush()

# Prints hi to stout
def print_hi():
    print("Hi")
    sys.stdout.flush()

# Reads commands from stdin and processes them, prints 'unknown command' if unknown is present    
def proccess_commands():
    while True:
        command = input().strip()
    
        if command == "Hi":
            print_hi()
        elif command == "GetRandom":
            print_random_int()
        elif command == "Shutdown":
            break  # terminates program
        else:
            print("unknown command")
            continue

def main():
   proccess_commands()

if __name__ == "__main__":
    main()
