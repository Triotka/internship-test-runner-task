# 

This repository contains two Python programs that interact with each other:

- **programA.py**: A pseudo-random number generator that reads commands via standard input and outputs responses.
- **programB.py**: It starts Program A, and then requests these things:
- Send the Hi command to Program A and verify the correct response.
- Retrieve 100 random numbers by sending the GetRandom command to Program A 100 times.
- Send the Shutdown command to Program A to terminate it gracefully.
- Sort the list of retrieved random numbers and print the sorted list to the console.
- Calculate and print the median and average of the numbers.

## How to Run

### Prerequisites
Ensure you have Python 3 installed on your system. 


### Clone the repository an run
#### On Windows
```bash
   git clone https://github.com/username/internship-test-runner-task.git
   cd internship-test-runner-task
   python programB.py
```
#### On Linux/Mac
   ```bash
   git clone https://github.com/username/internship-test-runner-task.git
   cd internship-test-runner-task
   python3 programB.py
```
