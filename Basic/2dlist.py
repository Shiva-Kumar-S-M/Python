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
# number=(1,2,3)
# can have only 2 methods count and index and expect these are advanced topics


# # unpacking
# #  num=(1,2,3,4)  applicable for list also
# a,b,c,d=num
# print(a+b+c+d)


# Dictionaries =  key value pairs
# customer={
#     "Name":"Shivu",
#     "age":19,
#     "Email":"Shivu@gmail.com"
# }
# customer["Name"]="virat"
# print(customer["Name"])
# print(customer.get("Phone",897146987))



# phone=input("Phone:")
# digits_map={
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }

# output=''
# for num in phone:
#     output+= digits_map.get(num,"!")+ " "
# print(output)


# Functions : breaks code to smaller reusable 

# def greet_user():
#     print("Hi There !")
#     print("Welcome to alvas")

# print("Start")
# greet_user()
# print("Finish")

# use of arguments
# def greet_user(name , age):     parameters --placeholder for info
    # print(f'Hi {name} !')
    # print("Welcome to my broken Heart")

# greet_user("Sanjana",19)     arguments --the info we supply

#  1st positional arguments and  then use keyword arguments