
"""
Week 6 Program, About Recursion Only
"""
def factorial(n):
    """Recursive function to calculate factorial of a number"""
    if n == 0 or n == 1:
        print(f"Reached base case: factorial({n}) = 1")
        return 1
    else:
        print(f"Calculating factorial({n}) = {n} * factorial({n-1})")
        return n * factorial(n - 1)

def tower_of_hanoi(n, start_pole, end_pole, middle_pole):
    """Recursive function to solve Tower of Hanoi problem."""
    if n == 1:
        print(f"Move disk 1 from pole {start_pole} to pole {end_pole}")
        return
    tower_of_hanoi(n - 1, start_pole, middle_pole, end_pole)
    print(f"Move disk {n} from pole {start_pole} to pole {end_pole}")
    tower_of_hanoi(n - 1, middle_pole, end_pole, start_pole)

def main():
    """Main function to provide user menu and execute choices."""
    while True:
        print("\nRecursion Demonstration Program")
        print("1. Calculate Factorial (Recursion)")
        print("2. Solve Tower of Hanoi (Recursion)")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is {factorial(num)}")

        elif choice == '2':
            num_discs = int(input("Enter the number of discs: "))
            start_pole = input("Enter the start pole: ")
            middle_pole = input("Enter the middle pole: ")
            end_pole = input("Enter the end pole: ")
            tower_of_hanoi(num_discs, start_pole, end_pole, middle_pole)

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
