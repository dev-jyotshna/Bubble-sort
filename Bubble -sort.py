# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
 
 
# Driver code to test above
arr = [124,45,78,74,22,1,0,90]
 
bubbleSort(arr)
 
print("Sorted array is:")
print(arr)