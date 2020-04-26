arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

"""
    selection sort is an in-place comparison sorting algorithm. It has an O(n2) time complexity, 
    which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. 
    Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, 
    particularly where auxiliary memory is limited.
"""

# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # TO-DO: swap

    return arr

print(selection_sort(arr))


"""
Bubble sort
"""

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # set a variable to hosd swaps occured
    swaps_have_occured = True
    # loop while swaps have occured
    while swaps_have_occured:
        # set the swaps occured to false
        swaps_have_occured = False
        # inner loop to iterate over the list (loop through you array)
        for i in range(0, len(arr) - 1):
            # check if element is in wrong position
            if arr[i] > arr[i + 1]:
                # swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # set swaps occured to true
                swaps_have_occured = True
    return arr

print(bubble_sort(arr))