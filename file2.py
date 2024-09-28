def process_data(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            if isinstance(item, int):
                total += item
            elif isinstance(item, float):
                total += int(item)
            else:
                continue
        return total
    elif isinstance(data, dict):
        total = 0
        for key, value in data.items():
            if isinstance(value, int):
                total += value
            elif isinstance(value, str) and value.isdigit():
                total += int(value)
            else:
                continue
        return total
    else:
        return None

def handle_user_input(option):
    if option == 1:
        print("Option 1 selected.")
    elif option == 2:
        print("Option 2 selected.")
    elif option == 3:
        print("Option 3 selected.")
    elif option == 4:
        print("Option 4 selected.")
    else:
        print("Invalid option!")

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        if len(lines) > 100:
            print("Large file!")
        elif len(lines) < 10:
            print("Small file!")
        else:
            print("Medium file!")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def complex_function(input_data, mode):
    result = None
    if mode == 'A':
        if isinstance(input_data, list):
            result = process_data(input_data)
        elif isinstance(input_data, dict):
            result = process_data(input_data)
    elif mode == 'B':
        if isinstance(input_data, str):
            if input_data.isdigit():
                result = int(input_data) * 2
            else:
                result = len(input_data)
        else:
            result = 0
    elif mode == 'C':
        result = handle_user_input(input_data)
    return result

def main():
    option = int(input("Enter option (1-4): "))
    handle_user_input(option)

    file_path = input("Enter file path: ")
    analyze_file(file_path)

    data = [10, '15', 20.5, 'invalid', 30]
    result = complex_function(data, 'A')
    print(f"Processed result: {result}")

    string_data = "12345"
    string_result = complex_function(string_data, 'B')
    print(f"String result: {string_result}")

    option_data = 3
    option_result = complex_function(option_data, 'C')
    print(f"Option result: {option_result}")

if __name__ == "__main__":
    main()
