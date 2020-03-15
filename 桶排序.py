from  randomNum import get_randomNumber

def bucketSort(arr):
    # 选择一个最大的数
    max_num = max(arr)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in arr:
        bucket[i] += 1
    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


list1 = get_randomNumber(20)
print(list1)
list2 = bucketSort(list1)
print(list2)