# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matrix[0][1]=20
# print(matrix)

# for mat in matrix:
#     for item in mat:
#         print(item)

# list methods append,insert,remove,pop,copy,index,count


# numbers=[5,8,9,14,3]
# numbers.append(100)
# print(numbers)
# numbers.insert(0,18)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.remove(5)
# print(numbers)
# num=numbers.copy()
# print(num)
# print(num.index(14))
# print(num.count(8))
# num.sort()
# print(num)
# num.reverse()
# print(num)

# wap to delete duplicate from list
# num=[2,5,8,9,1,2,1,4,8]
# unique=[]
# for i in num:
#     if i not in unique:
#         unique.append(i)
#         unique.sort()
# print(unique)

# tuples which are immutable
number=(1,2,3)
# can have only 2 methods count and index and expect these are advanced topics


# # unpacking
# #  num=(1,2,3,4)  applicable for list also
# a,b,c,d=num
# print(a+b+c+d)