import random

def quick_sort(arr):
    """
    Quick Sort algorithm using the Divide & Conquer approach.

    Args:
    arr: The list of elements to be sorted.

    Returns:
    A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr

    # Choosing a random pivot to avoid worst-case O(n^2) for already sorted data
    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Example usage
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", arr)
    print("Sorted list:", quick_sort(arr))
