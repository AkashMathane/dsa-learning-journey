# Bubble sort is a simple comparison-based sorting algorithm. It works by repeatedly comparing adjacent elements and
# swapping them if they are in the wrong order.
#
# In each pass through the array, the largest element moves (or “bubbles”) to the right end of the array. After each
# pass, one element is placed in its correct position, and the unsorted portion of the array becomes smaller.
#
# Bubble sort performs many comparisons between adjacent elements, which leads to a time complexity of O(n²) in the
# average and worst cases. If the array is already sorted and an early-stop optimization is used, the best-case time
# complexity is O(n).
#
# Bubble sort sorts the array in ascending order, is stable, and works in-place, but it is very slow for large datasets.
# Therefore, it is mainly used for learning, reasoning, and very small or nearly sorted inputs.
#
# Bubble sort = “swap adjacent elements until the largest bubbles to the right.”
#   
# In Bubble Sort, we use two loops.
# The outer loop runs from index 0 to n-1. This loop counts how many passes we do.

# Inside that, we use another loop with j. The inner loop runs from index 0 to n-i-1.

# In the inner loop, we compare adjacent elements, that is arr[j] and arr[j+1].

# If arr[j] is greater than arr[j+1], then we swap them.

# Because of this swapping, the bigger value moves one step to the right, just like a bubble moving up.

# We repeat these comparisons many times. After each pass, the biggest value goes to the right side.

#  When all bigger values reach the right side, the array becomes sorted.
