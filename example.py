# This program generates a Fibonacci sequence up to n terms

# Function to generate Fibonacci sequence
def fibonacci(n):
    # Initialize an empty list to hold the sequence
    sequence = []
    # The first two numbers in the Fibonacci sequence are 0 and 1
    a, b = 0, 1
    # Loop n times
    for _ in range(n):
        # Append the current number to the sequence
        sequence.append(a)
        # Update a and b to the next two numbers in the sequence
        a, b = b, a + b
    # Return the generated sequence
    return sequence

# Main program starts here
while True:
    # Ask the user for the number of terms in the sequence
    n = input("Enter the number of terms in the Fibonacci sequence or 'exit', 'quit', 'q', 'e' to stop: ")
    # Check if the user wants to exit the program
    if n.lower() in ['exit', 'quit', 'q', 'e']:
        break
    # Generate the Fibonacci sequence up to n terms
    fib_sequence = fibonacci(int(n))
    # Print the generated sequence
    print(fib_sequence)
