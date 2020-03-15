import random

#随机生成0-->100之间的数
def get_randomNumber(num):  
    lists=[]  
    i=0  
    for i in range(num):  
        lists.append(random.randint(0,100))  
    return lists

#插入排序,递增
def shellSort(list):  
    length=len(list)  
    inc=0  
    while inc<=length/3:  
        inc=inc*3+1    
    while inc>=1:  
        for i in range(inc,length):  
            tmp=list[i]  
            for j in range(i,0,-inc):  
                if tmp<list[j-inc]:  
                    list[j]=list[j-inc]  
                else:  
                    j+=inc  
                    break  
            list[j-inc]=tmp  
        inc//=3
    return list
list1 = get_randomNumber(10)
print(list1)
list2 = shellSort(list1)
print(list2)

