import random

#随机生成0-->100之间的数
def get_randomNumber(num):  
    lists=[]  
    i=0  
    for i in range(num):  
        lists.append(random.randint(0,100))  
    return lists

#插入排序,递增
def insert_sort(list):  
    for i in range(len(list)):  
        for j in range(i):  
            if list[i] < list[j]:  
                list.insert(j, list.pop(i))
                #insert(1,'A')将A元素插入到1位置
                #pop()删除元素                       
                break  
    return list  
  
list1 = get_randomNumber(20)
print(list1)
list2 = insert_sort(list1)
print(list2)

