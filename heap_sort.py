import datetime # We need this for type hints

# --- Min-Heap Priority Queue Implementation ---
# (This is the custom heap algorithm we built)

def heap_push(heap, item):
    """
    Pushes an item onto the heap (a list) while maintaining the
    min-heap property. This is the "sift-up" operation.
    """
    heap.append(item)
    pos = len(heap) - 1
    while pos > 0:
        parent_pos = (pos - 1) // 2
        if heap[pos] < heap[parent_pos]:
            heap[pos], heap[parent_pos] = heap[parent_pos], heap[pos]
            pos = parent_pos
        else:
            break

def heap_pop(heap):
    """
    Removes and returns the smallest item (the root) from the heap
    while maintaining the min-heap property. This is the "sift-down" operation.
    """
    if not heap:
        raise IndexError("pop from an empty heap")
        
    # Store the top item (highest priority) to return later
    return_item = heap[0]
    
    # Get the last item in the heap
    last_item = heap.pop()
    
    if heap:
        # Move the last item to the root
        heap[0] = last_item
        pos = 0
        last_index = len(heap) - 1
        
        # --- Sift-down logic ---
        while True:
            left_child_pos = 2 * pos + 1
            right_child_pos = 2 * pos + 2
            smallest_child_pos = pos
            
            # Check if left child exists and is smaller than the current node
            if left_child_pos <= last_index and heap[left_child_pos] < heap[smallest_child_pos]:
                smallest_child_pos = left_child_pos
                
            # Check if right child exists and is smaller than the smallest so far
            if right_child_pos <= last_index and heap[right_child_pos] < heap[smallest_child_pos]:
                smallest_child_pos = right_child_pos
                
            # If the smallest is still the parent, the heap is in order
            if smallest_child_pos == pos:
                break
            else:
                # Otherwise, swap the parent with the smallest child and continue
                heap[pos], heap[smallest_child_pos] = heap[smallest_child_pos], heap[pos]
                pos = smallest_child_pos
    
    return return_item

# --- End of Min-Heap Implementation ---