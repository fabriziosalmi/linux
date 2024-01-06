import time

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    fib_gen = fibonacci_generator()
    start_time = time.time()
    count = 0

    # Generating Fibonacci numbers as quickly as possible
    while time.time() - start_time <= 10:
        next(fib_gen)
        count += 1

    end_time = time.time()
    duration = end_time - start_time
    rate = count / duration

    print(f"\nGenerated {count} Fibonacci numbers in {duration:.6f} seconds.")
    print(f"Average rate: {rate:.2f} numbers/second")

if __name__ == "__main__":
    main()
