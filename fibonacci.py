def fibonacci(n):
    """Generates the Fibonacci sequence up to the nth term."""
    sequence = [0, 1]

    if n <= 1:
        return sequence[:n+1]

    for i in range(2, n+1):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)

    return sequence

# Generate and print the Fibonacci sequence up to the 10th term
fib_sequence = fibonacci(10)
print(fib_sequence)
