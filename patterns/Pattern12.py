def pattern12(n):
    for i in range(1, n + 1):
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print spaces
        for k in range(2 * (n - i)):
            print(" ", end="")
        
        # Print decreasing numbers
        for l in range(i, 0, -1):
            print(l, end="")
        
        # Move to the next line
        print()


       




def main():

    test_cases = int(input("Enter the number of test cases: "))

    for t in range(test_cases):
        print(f"\nTest Case {t + 1}:")
        # Input size for each test case
        size = int(input(f"Enter size for test case {t + 1}: "))
        pattern12(size)



# Entry point
if __name__ == "__main__":
    main()
