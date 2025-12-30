Selection sort works by repeatedly selecting the minimum element from the unsorted part of the array and placing it 
at the beginning.

Initially, the entire array is unsorted. In the first pass, the algorithm scans the whole array to find the smallest 
element and swaps it with the first element.
In the second pass, it scans the remaining unsorted portion to find the next smallest element and swaps it with the second 
position.

This process continues until the array is sorted from left to right in ascending order.

Selection sort performs only one swap per pass, but it makes many comparisons, which results in a time complexity of 
O(n²) in all cases.

Selection sort = “select minimum + place it correctly”
# First, I start from the first index of the array and assume that element is the smallest, so I store its index in min_index.
# Then, I scan the remaining part of the array to find if there is any element smaller than the current minimum.
# If I find a smaller element, I update min_index.
# After scanning the unsorted part, I swap the element at the current index with the element at min_index.
# I repeat this process for the next index until the entire array becomes sorted.
#
#for each index i from 0 to n-1:
    # set min_index = i
    #
    # for each index j from i+1 to n-1:
    #     if array[j] is smaller than array[min_index]:
    #         update min_index to j
    #
    # swap array[i] with array[min_index]

# 🔹 Line 1: “for each index i from 0 to n-1”
# Python
# for i in range(n):
#
# What is happening?
#
# for → loop (repeat steps)
#
# i → variable that stores index
#
# range(n) → gives numbers 0 to n-1
#
# 🧠 Meaning:
# “Repeat the steps for each position in the array”
#
# 🔹 Line 2: “set min_index = i”
# Python
# min_index = i
#
# What is happening?
#
# min_index → variable (stores position of smallest element)
#
# = → assignment (store value)
#
# 🧠 Meaning:
# “Assume the current position holds the smallest element”
# 🔹 Line 3: “for each index j from i+1 to n-1”
# Python
# for j in range(i + 1, n):
#
# What is happening?
#
# j → another loop variable
#
# range(i+1, n) → scans only the unsorted part
#
# 🧠 Meaning:
# “Look at the remaining elements after position i”
# 🔹 Line 4: “if array[j] is smaller than array[min_index]”
# Python
# if arr[j] < arr[min_index]:
#
# What is happening?
#
# if → condition check
#
# < → comparison operator
#
# arr[j] → value at index j
#
# 🧠 Meaning:
# “If I found a smaller element, remember it”
# 🔹 Line 5: “update min_index to j”
# Python
# min_index = j
#
#
# 🧠 Meaning:
# “Now this position has the smallest element so far”
# 🔹 Line 6: “swap array[i] with array[min_index]”
# Python
# arr[i], arr[min_index] = arr[min_index], arr[i]
#
# What is happening?
#
# Python tuple swap
#
# No temporary variable needed
#
# 🧠 Meaning:
# “Place the smallest element at the correct position”
# STEP 4️⃣ Wrap it inside a FUNCTION
# Why function?
#
# Groups logic
#
# Reusable
#
# Clean
#
# Python function structure
# def selection_sort(arr):
#
#
# def → define function
#
# selection_sort → function name
#
# arr → input array (parameter)
#
# FINAL COMPLETE PYTHON CODE (nothing magical)
# def selection_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         min_index = i
#
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#
# Every line came directly from English.
#
# STEP 5️⃣ How to practice writing algorithms (THIS IS YOUR METHOD)
#
# Use this exact checklist every time:
#
# 1️⃣ Write explanation in English
# 2️⃣ Write pseudocode
# 3️⃣ Convert pseudocode → Python line by line
# 4️⃣ Ask: “Which Python tool do I need?”
#
# loop → for
#
# decision → if
#
# memory → variable
#
# repeat → loop
#
# input/output → function

# Python TOOLS you used (important clarity)
# Tool	Purpose
# variable	store data
# for loop	repeat steps
# if	decision making
# function	group logic
# indexing	access elements
# 
# No magic. Just tools.