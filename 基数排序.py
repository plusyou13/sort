from randomNum import get_randomNumber

def radix_sort(arr):
    """基数排序"""
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(arr)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in arr:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        arr.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                arr.append(y)
        i += 1
    return arr


list1 = get_randomNumber(20)
print(list1)
list2 = radix_sort(list1)
print(list2)