factorial_dict = {}
def factorial(n):
    if n<0:
        return 0 #factorial is not difined for negative numbers
    elif n == 0 or n== 1:
        return 1
    elif n in factorial_dict:
        return factorial_dict[n] #return result if available 
    else:
        result = 1
        for i  in range(2,n+1):
            result *= i
            factorial_dict[n] = result # Result for future use
            return result 
def main():
    for num in range(1,11): #calculate the factorial of the number 1 to 10 
        factorial_result = factorial(num)
        factorial_dict[num] = factorial_result
    print("Factorial stored in the dictonary:", factorial_dict)
if __name__ == "__main__":
    main() 
