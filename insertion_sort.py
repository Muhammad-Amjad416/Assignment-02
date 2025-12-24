# Function to perform insertion sort
def insertion_sort(arr):
    # Loop through array starting from index 1
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        # Insert key at correct position
        arr[j + 1] = key


# Driver code
arr = [5, 3, 4, 1]
print("Original list:", arr)

insertion_sort(arr)

print("Sorted list:", arr)
