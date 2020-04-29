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
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list,
 compares adjacent elements and swaps them if they are in the wrong order. 
 The pass through the list is repeated until the list is sorted. The algorithm, which is a comparison sort, 
 is named for the way smaller or larger elements "bubble" to the top of the list.
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


#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr

  def counting_sort(the_list, max_value):

    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # etc.
    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1

    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(the_list)

    # Run through the input list
    for item in the_list:

        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list