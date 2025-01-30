def print_odd_pyramid(N):
    for i in range(N,0,-1): 
        # Calculate spaces and stars
        spaces = " " * (N - i)
        stars = "*" * (2 * i - 1)
        
        # Print the pattern for each row
        print(spaces + stars)

# Call the function with N = 6


def main():

    test_cases = int(input("Enter the number of test cases: "))

    for t in range(test_cases):
        print(f"\nTest Case {t + 1}:")
        # Input size for each test case
        size = int(input(f"Enter size for test case {t + 1}: "))
        print_odd_pyramid(size)



# Entry point
if __name__ == "__main__":
    main()
