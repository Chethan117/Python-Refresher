def erect_pyramid(N):
    for i in range(1,N+1):
        print('*'*i)

def revert_pyramid(N):
    for i in range(N-1,0,-1):
        print('*'*i)




def main():

    test_cases = int(input("Enter the number of test cases: "))

    for t in range(test_cases):
        print(f"\nTest Case {t + 1}:")
        # Input size for each test case
        size = int(input(f"Enter size for test case {t + 1}: "))
        erect_pyramid(size)
        revert_pyramid(size)



# Entry point
if __name__ == "__main__":
    main()
