################################################################################
## Your task is to write the pseudocode and implementation of the 4 sorts:
## Bubble sort, Insertion sort, Merge soft, and Quick sort
## Some parts of the code has already been written for you to make the task focus
## on the sorting part of the algorithm. Search for "TODO:" to find where the
## instructions are, and where you should be writing code.
## The output for this program is found at the bottom of this file when all 4
## sorts are completely implemented
################################################################################





########## Bubble sort ##########
# Input: Array of numbers
# Process: It will sort the array of numbers from lowest to highest using the
#          bubble sort algorithm
# Output: Array of (sorted) numbers
#def bubble_sort(arr):
    # TODO: 1. Write your bubble sort alorithm here as comments first
    # TODO: 2. Then use it to write your code
    #return arr

def bubble_sort(arr):
    x = len(arr)
    for i in range(x):
        for l in range(0, (x-i)-1):
            if arr[l] > arr[l+1] : 
                arr[l], arr[l+1] = arr[l+1], arr[l]
        print(arr)
    return arr


########## Insertion sort ##########
# Input: Array of numbers
# Process: It will sort the array of numbers from lowest to highest using the
#          insertion sort algorithm
# Output: Array of (sorted) numbers
def insertion_sort(arr):
    # TODO: 3. Write your insertion sort alorithm here as comments first
    # TODO: 4. Then use it to write your code
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)): 
        current = arr[i] #current index
        prev = i-1 #previous index
        while prev >=0 and current < arr[prev] :  #while the previous index is not 0 and the current index is less than the previous index 
            arr[prev+1] = arr[prev] # make the current index equal to the previous index 
            prev -= 1
        arr[prev+1] = current
        print(arr)
    return arr


########## Merge sort ##########
# Input: Array of numbers
# Process: It will sort the array of numbers from lowest to highest using the
#          merge sort algorithm. This uses a divide-and-conquer approach,
#          so this makes use of recursion to make it work.
# Output: Array of (sorted) numbers
#def merge_sort(arr):
    #if len(arr) == 1:
        # When down to 1 element, no need to sort, just return it
        #return arr

    # This splits the array into a left and right sub-array

    # When merging the left and right sub-arrays back together, you will need
    # to put the results in the sorted_arr declared below
    #sorted_arr = []

    # TODO: 5. Write your merge sort alorithm here as comments first
    # TODO: 6. Then use it to write your code

    #return sorted_arr

# This function splits the incoming array (arr) into 2 sub-arrays (left and right)

def split_arr(arr):
    midpoint = len(arr) // 2
    left = []
    for i in range(0, midpoint):
        left.append(arr[i])
    right = []
    for i in range(midpoint, len(arr)):
        right.append(arr[i])
    return (left, right)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    (left, right) = split_arr(arr)
    merge_sort(left)
    merge_sort(right)

    leftCount = 0
    rightCount = 0
    arrayCount = 0
    leftSize = len(left)
    rightSize = len(right)    
    while leftCount < leftSize and rightCount < rightSize:
        if left[leftCount] < right[rightCount]:
            arr[arrayCount] = left[leftCount]
            leftCount += 1 
        else:
            arr[arrayCount] = right[rightCount]
            rightCount += 1 

        arrayCount += 1 
        

    while leftCount < leftSize:
        arr[arrayCount] = left[leftCount]
        leftCount += 1
        arrayCount += 1 
        print(left, right)
    
    while rightCount < rightSize:
        arr[arrayCount] = right[rightCount]
        rightCount += 1 
        arrayCount += 1 
        print(left, right)
    return arr



########## Quick sort ##########
# Input: Array of numbers
# Process: It will sort the array of numbers from lowest to highest using the
#          quick sort algorithm. This uses a divide-and-conquer approach,
#          so this makes use of recursion to make it work.
#          This method calls quick_iteration()
# Output: Array of (sorted) numbers
#def quick_sort(arr):
#    quick_iteration(arr, 0, 1, len(arr) - 1)
#    return arr

# This function expects the following:
# 1. The original array of numbers (arr)
# 2. The index of the pivot value (pivot_index), which is assumed to be the
#    first index of the sub-array to sort
# 3. The first index of the sub-array to sort (not counting the pivot index)
# 4. The last index of the sub-array to sort

    # TODO: 7. Write your quick sort alorithm here as comments first
    # TODO: 8. Then use it to write your code

    # After the pivot value has been moved to its correct place,
    # call quick_iteration() on the 2 sub-arrays - the left side of the pivot
    # value, and the right side of the pivot value


"""
def quick_sort(arr):
    quick_iteration(arr, 0, 1, len(arr) - 1)
    return arr


def quick_iteration(arr, pivot_index, first_index, last_index):
    if pivot_index >= last_index or first_index >= last_index:
        # This checks whether the value of the pivot index or left first index
        # exceeds the value of the last index. If it does, there is only 1 or 2
        # left and do a check with the pivot value and swap if necessary
        if arr[last_index] < arr[pivot_index]:
            temp = arr[pivot_index]
            arr[pivot_index] = arr[last_index]
            arr[last_index] = temp
        return

    pivot = arr[pivot_index]
    left = first_index
    right = last_index

    quick_iteration(arr, pivot_index, first_index, right)
    quick_iteration(arr, right + 1, right + 2, last_index)

quick_sort(arr)
"""

def main():
    execute_sort(bubble_sort)
    execute_sort(insertion_sort)
    execute_sort(merge_sort)

def execute_sort(fn):
    arr = [12, 11, 13, 5, 6, 19, 2]
    print('####################################################')
    print("Before " + fn.__name__ + "():", arr)
    sorted_arr = fn(arr)
    print("After " + fn.__name__ + "():", sorted_arr)
    print()

main()