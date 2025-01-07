def counting_sort(array, exp):
    n = len(array)
    output = [0] * n  # output array to hold sorted values
    count = [0] * 10  # count array to store count of occurrences

    # Store count of occurrences of each digit
    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] contains the actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to array[], so that array now
    # contains sorted numbers according to current digit
    for i in range(n):
        array[i] = output[i]

def radix_sort(array):
    # Find the maximum number to know the number of digits
    max_num = max(array)
    exp = 1  # Initialize the exponent to the least significant digit

    # Perform counting sort for each digit
    while max_num // exp > 0:
        counting_sort(array, exp)
        exp *= 10

# Get list of numbers from the user
user_input = input("Enter numbers separated by space: ")
array = list(map(int, user_input.split()))

# Perform radix sort
radix_sort(array)

# Print the sorted array
print("Sorted array:", array)
