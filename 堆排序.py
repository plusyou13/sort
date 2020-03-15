from randomNum import get_randomNumber
def HeapAdjust(arr, start, end):
    root = start    
    while True:
        # 从root开始对最大堆调整
        child = 2 * root + 1    
        if child > end:      # 后面可以看出堆的大小在减小
            break

        # 找出两个child中较大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] < arr[child]:
            # 最大堆root小于较大的child, 交换顺序
            arr[root], arr[child] = arr[child], arr[root]
            #temp=arr[root]
            #arr[root]=arr[child]
            #arr[child]=temp
            # 调整的节点设置为root
            root = child
        else:
            break


def HeapSort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆
    first = len(arr) // 2 - 1 
    for start in range(first, -1, -1):       
        HeapAdjust(arr, start, len(arr) - 1)   # 排序一次的结果

    # 将最大的放到堆的最后一个, 堆大小-1, 继续调整排序
    for end in range(len(arr) -1, 0, -1):    
        arr[0], arr[end] = arr[end], arr[0]
        HeapAdjust(arr, 0, end - 1)            #  注意start=0


if __name__ == "__main__": 
    List = get_randomNumber(20)
    print(List)
    HeapSort(List)
    print(List)

