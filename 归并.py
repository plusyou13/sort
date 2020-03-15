import random

#随机生成0-->100之间的数
def get_randomNumber(num):  
    lists=[]  
    i=0  
    for i in range(num):  
        lists.append(random.randint(0,100))  
    return lists
def merge(array, low, mid, high):
    """
    两段需要归并的序列从左往右遍历，逐一比较，小的就放到
    tmp里去，再取，再比，再放。
    """
    tmp = []#申请空列表,将排好序的列表存入tmp
    i = low
    j = mid +1
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= high:
        tmp.append(array[j])
        j += 1
    array[low:high+1] = tmp#将排好序的存入array列表中
    return array
#递归实现的，效率低，占用空间大。
def merge_sort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        return merge(array, low, mid, high)
        
if __name__ == "__main__":
    list1 = get_randomNumber(20)
    print(list1)
    list2 = merge_sort(list1,0,19)
    print(list2)
