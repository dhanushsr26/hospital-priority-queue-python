# --- Merge Sort Implementation ---

def merge_sort(arr, key_index):
    """
    Sorts a list of tuples recursively using the Merge Sort algorithm.
    Sorts based on the element at 'key_index' within each tuple.
    """
    
    # Base case: A list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    
    # 1. Divide: Find the midpoint and split the list
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 2. Conquer: Recursively sort both halves
    sorted_left = merge_sort(left_half, key_index)
    sorted_right = merge_sort(right_half, key_index)
    
    # 3. Combine: Merge the two sorted halves
    return merge(sorted_left, sorted_right, key_index)

def merge(left, right, key_index):
    """
    Merges two sorted lists (left and right) into a single sorted list.
    Compares elements based on the 'key_index'.
    """
    
    merged_list = []
    left_pointer = 0
    right_pointer = 0
    
    # Loop while both lists have elements to compare
    while left_pointer < len(left) and right_pointer < len(right):
        
        # Compare the elements at the specified key_index
        if left[left_pointer][key_index] <= right[right_pointer][key_index]:
            # The left element is smaller or equal, add it to our list
            merged_list.append(left[left_pointer])
            left_pointer += 1
        else:
            # The right element is smaller, add it to our list
            merged_list.append(right[right_pointer])
            right_pointer += 1
            
    # At this point, one of the lists is empty.
    # Add all remaining elements from the other list (they are already sorted).
    
    # Add remaining elements from the left list (if any)
    while left_pointer < len(left):
        merged_list.append(left[left_pointer])
        left_pointer += 1
        
    # Add remaining elements from the right list (if any)
    while right_pointer < len(right):
        merged_list.append(right[right_pointer])
        right_pointer += 1
        
    return merged_list

# --- End of Merge Sort Implementation ---