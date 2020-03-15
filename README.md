# 十大排序

![Snipaste_2020-03-15_18-10-09](C:\Users\lic\Desktop\demo\sort\Snipaste_2020-03-15_18-10-09.png)

![Snipaste_2020-03-15_18-10-27](C:\Users\lic\Desktop\demo\sort\Snipaste_2020-03-15_18-10-27.png)

术语说明：

- 稳定 ：如果a原本在b前面，而a=b，排序之后a仍然在b的前面；
- 不稳定 ：如果a原本在b的前面，而a=b，排序之后a可能会出现在b的后面；
- 内排序 ：所有排序操作都在内存中完成；
- 外排序 ：由于数据太大，因此把数据放在磁盘中，而排序通过磁盘和内存的数据传输才能进行；
- 时间复杂度 ： 一个算法执行所耗费的时间。
- 空间复杂度 ：运行完一个程序所需内存的大小。
- In-place: 占用常数内存，不占用额外内存
- Out-place: 占用额外内存



##  比较和非比较的区别

    常见的快速排序、归并排序、堆排序、冒泡排序 等属于比较排序 。在排序的最终结果里，元素之间的次序依赖于它们之间的比较。每个数都必须和其他数进行比较，才能确定自己的位置 。
    
    在冒泡排序之类的排序中，问题规模为n，又因为需要比较n次，所以平均时间复杂度为O(n²)。在归并排序、快速排序之类的排序中，问题规模通过分治法消减为logN次，所以时间复杂度平均O(nlogn)。
    
    比较排序的优势是，适用于各种规模的数据，也不在乎数据的分布，都能进行排序。可以说，比较排序适用于一切需要排序的情况。
    
    计数排序、基数排序、桶排序则属于非比较排序 。非比较排序是通过确定每个元素之前，应该有多少个元素来排序。针对数组arr，计算arr[i]之前有多少个元素，则唯一确定了arr[i]在排序后数组中的位置 。
    
    非比较排序只要确定每个元素之前的已有的元素个数即可，所有一次遍历即可解决。算法时间复杂度O(n)。
    
    非比较排序时间复杂度底，但由于非比较排序需要占用空间来确定唯一位置。所以对数据规模和数据分布有一定的要求。


1. 冒泡排序（Bubble Sort）
       冒泡排序 是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

2. 选择排序（Selection Sort）
       选择排序 是表现最稳定的排序算法之一 ，因为无论什么数据进去都是O(n2)的时间复杂度 ，所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。理论上讲，选择排序可能也是平时排序一般人想到的最多的排序方法了吧。 选择排序(Selection-sort) 是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

3. 插入排序（Insertion Sort）
       插入排序（Insertion-Sort） 的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

4. 希尔排序（Shell Sort）
       希尔排序是希尔（Donald Shell） 于1959年提出的一种排序算法。希尔排序也是一种插入排序，它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序，同时该算法是冲破O(n2）的第一批算法之一。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。希尔排序是把记录按下表的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

5. 归并排序（Merge Sort）
       和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。归并排序 是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

6. 快速排序（Quick Sort）
       快速排序 的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

   ​	算法描述:

   快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
   步骤1：从数列中挑出一个元素，称为 “基准”（pivot ）；
   步骤2：重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
   步骤3：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

7. 堆排序（Heap Sort）
       堆排序（Heapsort） 是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

   ​	算法描述:
   步骤1：将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
   步骤2：将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
   步骤3：由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

8. 计数排序（Counting Sort）
       计数排序 的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。计数排序(Counting sort) 是一种稳定的排序算法。计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。然后根据数组C来将A中的元素排到正确的位置。它只能对整数进行排序。

   ​     算法描述:
   步骤1：找出待排序的数组中最大和最小的元素；
   步骤2：统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
   步骤3：对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
   步骤4：反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

9. 9、桶排序（Bucket Sort）
       桶排序 是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。

   桶排序 (Bucket sort)的工作的原理：

   ​	假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排

   ​    算法描述:
   步骤1：人为设置一个BucketSize，作为每个桶所能放置多少个不同数值（例如当BucketSize==5时，该桶可以存放｛1,2,3,4,5｝这几种数字，但是容量不限，即可以存放100个3）；
   步骤2：遍历输入数据，并且把数据一个一个放到对应的桶里去；
   步骤3：对每个不是空的桶进行排序，可以使用其它排序方法，也可以递归使用桶排序；
   步骤4：从不是空的桶里把排好序的数据拼接起来。 

10. 基数排序（Radix Sort）
        基数排序也是非比较的排序算法，对每一位进行排序，从最低位开始排序，复杂度为O(kn),为数组长度，k为数组中的数的最大的位数；基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。基数排序基于分别排序，分别收集，所以是稳定的。

    ​	 算法描述:
    步骤1：取得数组中的最大数，并取得位数；
    步骤2：arr为原始数组，从最低位开始取每个位组成radix数组；
    步骤3：对radix进行计数排序（利用计数排序适用于小范围数的特点）；
