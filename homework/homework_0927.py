# -*- coding:utf-8 -*-

print('L=[5,6,9,7]利用for循环，完成列表里所有数据的相加')
L = [5, 6, 9, 7]
s = 0
for n in L:
    s += n
print(s)
print('--------------------------------')


print('L=[5,6,9,7]利用for循环，根据L的索引，完成列表里所有数据的相加')
L = [5, 6, 7, 8, 9]
SUM = 0
for a in range(len(L)):
    SUM += L[a]
print(SUM)
print('--------------------------------')


print('利用for循环和range函数，完成1-100整数相加（包含1和100）')
SUM = 0
for i in range(1, 101):
    SUM += i
print(SUM)
print('--------------------------------')


print('L=[[11,22,33],[44,55,66,77]]输出所有数据')
L = [[11, 22, 33], [44, 55, 66, 77]]
for i in L:
    for j in i:
        print(j)
print('--------------------------------')


print('''打印直角三角形
 *
 **
 ***
 ****''')
for i in range(6):
    for j in range(i):
        print('*', end='')
    print('')
print('--------------------------------')


print('''打印
   *
  * *
 * * *
* * * *''')
num = 10
for i in range(1, num):
    print(' ' * (num-i) + '* ' * i)
print('--------------------------------')


print('写一段程序，分别求出0-100之间的所有偶数的和和所有奇数的和。')
a = 0
b = 0
for i in range(1, 101):
    if i % 2 == 0:
        a += i
    else:
        b += i
print('1-100之间所有偶数的和为{0}，所有奇数的和为{1}'.format(a, b))
print('--------------------------------')


print('输出99乘法表')
for i in range(1, 10):
    for j in range(1, (i+1)):
        print('{0} × {1} = {2}'.format(j, i, (j*i)), end='   ')
    print(' ')
print('--------------------------------')


print('''经典冒泡算法： 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序。
冒泡排序：小的排前面，大的排后面。 排序，最终使得数组中的这几个数字按照从小到大的顺序排序。''')
A = [1, 7, 4, 89, 34, 2]
for i in range(len(A)):
    for j in range(i, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            print(A)
print('--------------------------------')
