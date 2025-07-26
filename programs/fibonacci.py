def fibonacci_program(a, b, num):
    for i in range(0, num):
        a, b = b, a + b
        print(f"{a} and {b} values")
fibonacci_program(0, 1, 10)
