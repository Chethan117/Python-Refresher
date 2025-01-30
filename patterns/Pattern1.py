
def print1(n):

    for i in range(n):
        print('* '*n)


def main():

    test_cases = int(input("Enter the number of test cases: "))

    for t in range(test_cases):
        print(f"\nTest Case {t + 1}:")
        # Input size for each test case
        size = int(input(f"Enter size for test case {t + 1}: "))
        print(f"Grid of size {size}x{size}:")
        print1(size)



# Entry point
if __name__ == "__main__":
    main()