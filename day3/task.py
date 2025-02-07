#type conversions
#int

input_number=1
print(float(input_number))
print(int(input_number))
print(str(input_number))
print(bool(input_number))
 #print(list(input_number))-'int' object is not iterable
#print(tuple(input_number))-'int' object is not iterable
#print(set(input_number))-'int' object is not iterable
#print(dict(input_number))-'int' object is not iterable
print(complex(input_number))
print(range(input_number))

#float
input_number=11.0
print(float(input_number))
print(int(input_number))
print(str(input_number))
print(bool(input_number))
 #print(list(input_number))-'float' object is not iterable
#print(tuple(input_number))-'float' object is not iterable
#print(set(input_number))-'float' object is not iterable
#print(dict(input_number))-'float' object is not iterable
print(complex(input_number))
#print(range(input_number))-'float' object cannot be interpreted as an integer


#string
input_number="pavan"
#print(float(input_number))-could not convert string to float: 'pavan'
#print(int(input_number))-invalid literal for int() with base 10: 'pavan'
print(str(input_number))
print(bool(input_number))
print(list(input_number))
print(tuple(input_number))
print(set(input_number))
#print(dict(input_number))-dictionary update sequence element #0 has length 1; 2 is required
#print(complex(input_number))-complex() arg is a malformed string
#print(range(input_number))-str' object cannot be interpreted as an integer


#list
input_number=[1,2,3,4]
#print(float(input_number))-float() argument must be a string or a real number, not 'list'
#print(int(input_number))-int() argument must be a string, a bytes-like object or a real number, not 'list'
print(str(input_number))
print(bool(input_number))
print(list(input_number))
print(tuple(input_number))
print(set(input_number))
#print(dict(input_number))-cannot convert dictionary update sequence element #0 to a sequence
#print(complex(input_number))-complex() first argument must be a string or a number, not 'list'
#print(range(input_number))-'list' object cannot be interpreted as an integer



#tuple
input_number=(1,2,3,4)
#print(float(input_number))-float() argument must be a string or a real number, not 'tuple'
#print(int(input_number))-int() argument must be a string, a bytes-like object or a real number, not 'tuple'
print(str(input_number))
print(bool(input_number))
print(list(input_number))
print(tuple(input_number))
print(set(input_number))
#print(dict(input_number))-cannot convert dictionary update sequence element #0 to a sequence
#print(complex(input_number))-complex() first argument must be a string or a number, not 'tuple'
#print(range(input_number))-'tuple' object cannot be interpreted as an integer




#complex
input_number=2+3j
#print(float(input_number))-float() argument must be a string or a real number, not 'complex'
#print(int(input_number))-int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(str(input_number))
print(bool(input_number))
#print(list(input_number))-'complex' object is not iterable
#print(tuple(input_number))-'complex' object is not iterable
#print(set(input_number))-'complex' object is not iterable
#print(dict(input_number))-'complex' object is not iterable
print(complex(input_number))
#print(range(input_number))-'complex' object cannot be interpreted as an integer






#set
input_number={1,2,3,4}
#print(float(input_number))-float() argument must be a string or a real number, not 'set'
#print(int(input_number))-int() argument must be a string, a bytes-like object or a real number, not 'set'
print(str(input_number))
print(bool(input_number))
print(list(input_number))
print(tuple(input_number))
print(set(input_number))
#print(dict(input_number))-cannot convert dictionary update sequence element #0 to a sequence
#print(complex(input_number))-complex() first argument must be a string or a number, not 'set'
#print(range(input_number))-'set' object cannot be interpreted as an integer



#dictionary
input_number={1:"pavan",2:"ammu"}
#print(float(input_number))-float() argument must be a string or a real number, not 'dict'
#print(int(input_number))-int() argument must be a string, a bytes-like object or a real number, not 'dict'
print(str(input_number))
print(bool(input_number))
print(list(input_number))
print(tuple(input_number))
print(set(input_number))
print(dict(input_number))
#print(complex(input_number))-complex() first argument must be a string or a number, not 'dict'
#print(range(input_number))-'dict' object cannot be interpreted as an integer