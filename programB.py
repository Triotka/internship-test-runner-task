import platform
import subprocess
import statistics
import sys

# Sends a command to process and returns the response.
def send_command(process, command):
    process.stdin.write(f"{command}\n")
    process.stdin.flush()
    return process.stdout.readline().strip()

# Sends 'Hi' and verifies the correct response.
def verify_hi_response(process):
    response = send_command(process, "Hi")
    if response != "Hi":
        print("Error: Program A did not respond correctly to 'Hi'")
        process.terminate()
        return False
    return True

 # Gets a list of n random numbers from given procces
def get_random_numbers(process, n=100):
    random_numbers = []
    for _ in range(n):
        response = send_command(process, "GetRandom")
        try:
            number = int(response)
            random_numbers.append(number)
        except ValueError:
            print("Error: Invalid number received")
            process.terminate()
            return None
    return random_numbers

#Sends the 'Shutdown' command to process and waits for terminating
def shutdown_program(process):
    send_command(process, "Shutdown")
    process.wait()


# Given list of numbers
# Prints the sorted list, median, and average.
def print_statistics(num_list):
    num_list.sort()
    print("Sorted Numbers:", num_list)
    print("Median:", statistics.median(num_list))
    print("Average:", statistics.mean(num_list))

# Returns the appropriate Python command based on the operating system.
def get_python_command():
    if platform.system() == "Windows":
        return "python"  # Use 'python' on Windows
    else:
        return "python3"  # Use 'python3' on Linux/Mac
def main():
    
    process_a = subprocess.Popen(
        [get_python_command(), "programA.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    if not verify_hi_response(process_a):
        return

    random_numbers = get_random_numbers(process_a)
    if random_numbers is None:
        return  # Exit if an error occurred

    shutdown_program(process_a)
    print_statistics(random_numbers)

if __name__ == "__main__":
    main()
