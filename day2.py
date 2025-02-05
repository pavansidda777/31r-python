#complex numbers
a=2+4j
b=4+5j

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
#print(a % b)
# print(a // b)
# in complex numbers % module,// floor division cant be executed. we will get the error.

#boolean
#boolean is consists of True & False. where True=1,False=0.
x=2
y=3

print(x > y)
print(x != y)
print(x < y)
print(x >= y)
print(x == y)
print(x <= y)

x=True
print(type(x))
print(type(True))



#sequences-List,Tuple,Strings,Range.




#list-collection of heterogenous  elements which are indexable.list should be given in the square brackets[].
#list is Mutable:change is allowed
#list is slower than Tuple
pavan=[[1,2,3],"sidda",5,-1,0.7,True,False,[1,3,9]]
print(type(pavan))
print(len(pavan))
print(pavan[3])#index
print(pavan[6])
print(pavan[-4])#negative indexing in list
print(pavan[0:7])#slicing
print(pavan[-4:-2])
print(pavan[2:7:2])#step
print(pavan[-7:-1:2])
print(pavan[-2:-7:-1])#-1 in step. it print the list reverse direction.
print(pavan[7][1])#indexing in list of list.
pavan[3]=3 #adding new element in the list by using index number in that index position.
print(pavan)
#[[1, 2, 3], 'sidda', 5, 3, 0.7, True, False, [1, 3, 9]]







#Tuple-collection of heterogenous  elements which are indexable.list should be given in the curely brackets().
#Tuple is Immutable:change is not allowed.
#tuple is faster than list.
sidda=(1,2,True,3,4,"pavan",(2,3),7,False)
print(type(sidda))
print(len(sidda))
print(sidda[3])#index
print(sidda[6])
print(sidda[-4])#negative indexing in tuple
print(sidda[0:7])#slicing
print(sidda[-4:-2])
print(sidda[2:7:2])#step
print(sidda[-7:-1:2])
print(sidda[-2:-7:-1])#-1 in step. it print the tuple reverse direction.
print(sidda[-3][1])#indexing in tuple of tuple.
#in tuple we cant change the elements using index numbers.



# Range

print(list(range(0,100)))
print(tuple(range(0,45)))

print(list(range(0,25,-1)))
print(list(range(0,30,3)))#step=3