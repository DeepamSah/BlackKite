entered_numbers = []  # Use a more descriptive variable name

while True:
    x = input("Enter a number, or 'stop' to end: ")
    if x.lower() == "stop":
        break

    if x.strip() == "":
        print("Please enter a number or 'stop'.")
        continue

    try:
        x = int(x)
        entered_numbers.append(x)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


num_elements = len(entered_numbers)
for i in range(num_elements - 1):
    for j in range(num_elements - 1 - i):
        if entered_numbers[j] > entered_numbers[j + 1]:
            entered_numbers[j], entered_numbers[j + 1] = entered_numbers[j + 1], entered_numbers[j]

print("After sorting:")
for i in range(0, num_elements):
    print(entered_numbers[i])
