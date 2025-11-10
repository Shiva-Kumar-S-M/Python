#Today I am learining about Arrays in Python
# cars=['BMW','Volvo','Ford']
# x=cars[0]
# print(x)

# cars[0]="Shivu"
# print(cars)
# print(len(cars))

cars=['BMW','Volvo','Ford']
#Append Function adds an element at the end of the list
cars.append("Honda")
for x in cars:
    print(x)

#pop() removes the last element from the list 
cars.pop()
print(cars)

#Remove() removes the specified element from the list 
cars.remove("Ford")
print(cars)