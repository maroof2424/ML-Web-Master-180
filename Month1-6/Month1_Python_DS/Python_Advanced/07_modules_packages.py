import type_hinting_docstrings as cal

x = float(input("Enter x: "))
y = float(input("Enter y: "))

print("\nSelect operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print("Result:", cal.add(x, y))
elif choice == "2":
    print("Result:", cal.subtract(x, y))
elif choice == "3":
    print("Result:", cal.multiply(x, y))
elif choice == "4":
    try:
        print("Result:", cal.divide(x, y))
    except ZeroDivisionError as e:
        print("Error:", e)
else:
    print("Invalid choice.")
