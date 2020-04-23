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