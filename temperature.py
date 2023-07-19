def has_fever(temperature):
    return temperature > 98

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    T = int(input().strip())

    # Process each test case
    for _ in range(T):
        temperature = int(input().strip())
        if has_fever(temperature):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
