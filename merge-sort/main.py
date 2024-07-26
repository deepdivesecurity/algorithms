
def mergeSort(numList): 
    """mergeSort: Implementation of the merge sort sorting algorithm

    Args:
        numList (array): Array of unsorted numbers

    Returns:
        array: Array of sorted numbers
    """
    lengthOfArray = len(numList)

    # Base case if array contains 0 or 1 item
    if lengthOfArray <= 1: 
        return numList

    # Divide array into 2 halves
    leftHalf = numList[:int(lengthOfArray/2)]
    rightHalf = numList[int(lengthOfArray/2):]

    leftSorted = mergeSort(leftHalf)
    rightSorted = mergeSort(rightHalf)

    return merge(leftSorted, rightSorted)

def merge(leftSorted, rightSorted): 
    """merge: Merges left sorted and right sorted numbers into 1 sorted list

    Args:
        leftSorted (array): Array of left sorted numbers to be merged
        rightSorted (array): Array of right sorted numbers to be merged

    Returns:
        array: Sorted array
    """
    sorted = []
    i = 0
    j = 0

    # Determine smaller number and populate the output array
    while i < len(leftSorted) and j < len(rightSorted): 
        if leftSorted[i] < rightSorted[j]: 
            sorted.append(leftSorted[i])
            i += 1
        else: 
            sorted.append(rightSorted[j])
            j += 1

    # Add remaining from both halves
    sorted.extend(leftSorted[i:])
    sorted.extend(rightSorted[j:])

    #Return the sorted array
    return sorted

def main(): 
    nums = [7,5,3,4,2,1,6]
    sortedNums = mergeSort(nums)

    print(sortedNums)

main()