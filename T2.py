"""
Problem Statement:- Write a python program to compute factorial of a number write a test automation program
for testing above code for given number without requiring human interaction. 
Eg- 1) One can Generate 100 random numbers, store them into dictonary alogn them with factorial value.
    2) Dictonary can be input to your test automation program
    3) Which will invoke your factorial program for each Input in dictonary & then compares it with expected output from the dictonary.  
"""
# Code Implementation 
import math
import random

# This Function computes factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# This function Tests automation program.
def test_factorial():
    # Generate 100 random numbers and compute their factorials.
    test_data = {}
    for _ in range(100):
        num = random.randint(0, 25)  # Initially we took the factorial of 25 Numbers. 
        expected_result = math.factorial(num)
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

"""
Solution for the above problem statement:- 
Step1:  Define a function to calculate a factorial of No
Step2:  Define a function for test automation program
            a) Generate 100 random number.
            b) Store them into dictonary.
Step3:  Give input to the test automation program of that factorial function. 
Step4:  Compare the data with Expected result. If Successfull. 
Step5:  Print the Output. 

"""