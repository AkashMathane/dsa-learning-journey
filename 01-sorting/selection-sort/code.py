def selection_sort(arr):    # Function
    n = len(arr)
    for i in range (n):     # outer loop
        min_index = i

        for j  in range (i+1, n): # inner loop
            if arr[j] < arr[min_index]: # condition
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i] # swap
