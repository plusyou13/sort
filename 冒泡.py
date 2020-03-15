from randomNum import get_randomNumber

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

list1 = get_randomNumber(20)
print(list1)
list2 = bubbleSort(list1)
print(list2)
