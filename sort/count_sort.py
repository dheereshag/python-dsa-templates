def count_sort(arr):
    mx = max(arr)
    n = len(arr)
    output = [0] * n
    count = [0] * (mx + 1)

    # Count frequencies
    for num in arr:
        count[num] += 1

    # Convert to cumulative count
    for i in range(1, mx + 1):
        count[i] += count[i - 1]

    # Build output array (iterate from right to left)
    for num in reversed(arr):
        count[num] -= 1
        output[count[num]] = num

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


arr = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
count_sort(arr)
print(arr)
