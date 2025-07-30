def main():
    # 04_exception_handling.py

    # ----------------------------
    # 1. Division with exception handling
    # ----------------------------

    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
        else:
            print(f"✅ Division result: {result}")
        finally:
            print("📌 Division attempt complete.\n")

    divide_numbers(10, 2)
    divide_numbers(5, 0)

    # ----------------------------
    # 2. Raise exception if input is not a number
    # ----------------------------

    def input_number(value):
        try:
            number = float(value)
        except ValueError:
            raise ValueError("❌ Input must be a number.")
        else:
            print(f"✅ You entered the number: {number}")
        finally:
            print("📌 Input check complete.\n")

    # Example usage
    try:
        input_number("42")
        input_number("hello")
    except ValueError as e:
        print(e)

    # ----------------------------
    # 3. Create a custom InvalidAgeError exception
    # ----------------------------

    class InvalidAgeError(Exception):
        """Custom exception for invalid age input."""
        def __init__(self, message="❌ Age must be between 0 and 120."):
            super().__init__(message)

    def check_age(age):
        try:
            if not (0 <= age <= 120):
                raise InvalidAgeError()
        except InvalidAgeError as e:
            print(e)
        else:
            print(f"✅ Valid age: {age}")
        finally:
            print("📌 Age validation complete.\n")

    check_age(25)
    check_age(-3)
    check_age(150)

    # ----------------------------
    # 4. Try/except with else and finally
    # ----------------------------

    def process_file(filename):
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("❌ File not found.")
        else:
            content = file.read()
            print("✅ File content read successfully:")
            print(content)
            file.close()
        finally:
            print("📌 File processing complete.\n")

    with open("sample.txt", "w") as f:
        f.write("This is a sample file.\nHello, Exception Handling!")

    process_file("sample.txt")
    process_file("missing.txt")

    # ----------------------------
    # 5. Handling multiple exceptions
    # ----------------------------

    def risky_operation(value):
        try:
            number = int(value)
            result = 10 / number
        except ValueError:
            print("❌ ValueError: Input must be an integer.")
        except ZeroDivisionError:
            print("❌ ZeroDivisionError: Cannot divide by zero.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        else:
            print(f"✅ Result is {result}")
        finally:
            print("📌 Risky operation attempt complete.\n")

    risky_operation("5")
    risky_operation("0")
    risky_operation("abc")


if __name__ == "__main__":
    main()