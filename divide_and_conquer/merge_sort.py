def merge_sort(arr):
    """
    Merge Sort algorithm using the Divide & Conquer approach.
    
    Args:
    arr: The list of elements to be sorted.
    
    Returns:
    A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """
    Helper function to merge two sorted lists.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    # Example usage
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", arr)
    print("Sorted list:", merge_sort(arr))
