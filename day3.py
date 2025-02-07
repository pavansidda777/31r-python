#strings are immutable in python
str1="pavan"
# str1[3]='e' in python str doesn't support item assignments
print(str1)

str1="sidda"
print(str1)





#set-unique,unorderd,finite
#syntax is {}
#duplicates are not allowed
#set is mutable
a={1,2,3,True,"pavan" ,"sidda",1,2,3,4}
print(a)
print(type(a))
print(a)
print(a)
print(a)
print(a)
print(a)

#dictionary-consists of keys and values
#keys can't be dulipcates but values can be dulipcates.
#dictionary is mutable.
ab={1:'html',2:'css',3:'java',4:'javascript',5:'react'}
print(ab)
print(type(ab))
ab[3]='bootstrap'
print(ab[3])
print(ab)


#None-None keyword is used to define a null value, or no value at all.
python=None
print(python)
print(type(python))



#type conversations
num1=34.58
num1=int(num1)
print(num1)
num1=float(num1)
print(num1)


#truthy values and falsy values.
#truthy values
print(bool(1))
print(bool(2))
print(bool(-1))
print(bool(str1))
print(bool(1+2j))


#falsy values
print(bool(0))
print(bool(''))
print(bool([]))



#from user input:
class1=input("enter a number A:")
class2=input("enter a number B:")
print(class1+class2)

print(type(class1+class2))

class1=int(input("enter a number A:"))
class2= int(input("enter a number B:"))
print(class1+class2)
print(type(class1+class2))


#naming conversations
#pasacal case,camel case,snake case.


#pascal case- word start with the captial letter
#camel case-first word of starting letter is small ,remaining all  word start with the captial letter
#snake case-between the word we give in the underscore-in python we use maximum snake case

#in python we dont have constant keyword.