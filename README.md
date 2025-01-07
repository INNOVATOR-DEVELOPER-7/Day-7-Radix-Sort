# Day-7-Radix-Sort
Here Python Program for Radix Sort. Day 7 of Day 365.
_ Initial Setup: Determine the maximum number of digits (or bits) in the largest number in the array.
- Sorting by Digit: Start sorting the array by the least significant digit (LSD) to the most significant digit (MSD). Use a stable counting sort for each digit:
  - Counting Sort: For each digit position:
    - Count the occurrences of each digit.
    - Use this count to determine the positions of each digit in the sorted array.
    - Place the numbers in the correct order based on the current digit.
- Repetition: Repeat the sorting process for each subsequent digit.

Here's a visual representation using the example array [170, 45, 75, 90, 802, 24, 2, 66]:

1. Initial Array: [170, 45, 75, 90, 802, 24, 2, 66]
2. Sort by 1st Digit (LSD):
   - Counting Sort on LSD: [170, 90, 802, 2, 24, 45, 75, 66]
3. Sort by 2nd Digit:
   - Counting Sort on 2nd Digit: [802, 2, 24, 45, 66, 170, 75, 90]
4. Sort by 3rd Digit (MSD):
   - Counting Sort on 3rd Digit: [2, 24, 45, 66, 75, 90, 170, 802]

The final sorted array is [2, 24, 45, 66, 75, 90, 170, 802].
