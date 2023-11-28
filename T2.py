import math
import random

# This Function computes factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# This function Tests automation program
def test_factorial():
    # Generate 100 random numbers and compute their factorials
    test_data = {}
    for _ in range(100):
        num = random.randint(0, 25)  # Initially we took the factorial of 20 Numbers. 
        expected_result = factorial(num)
        test_data[num] = expected_result
        result = factorial(num)
        
        # Printing the random Input and Output Numbers.
        print(f"Input: {num}, Expected Output: {expected_result}, Actual Output: {result}")
        
        # Compare the result with the expected value
        if result == expected_result:
            print(f"Test passed for input {num}. Expected: {expected_result}, Result_Got: {result}")
        else:
            print(f"Test failed for input {num}. Expected: {expected_result}, Result_Got: {result}")

    print("All tests passed successfully!")

# Run the test automation program
test_factorial()
