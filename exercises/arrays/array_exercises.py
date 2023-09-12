import array as arr

"""
initialize array in python in this way
arr.array(typecode, [initializers])  
typecode :- The data type is specified at the array creation time by using a single character
is called the type code.

‘c’	char	
‘b’	signed char
‘B’	unsigned char
‘u’	Py_UNICODE	
‘h’	signed short
‘H’	unsigned short
‘i’	signed int
‘I’	unsigned int
‘l’	signed long
‘L’	unsigned long
‘f’	float
‘d’	double
"""
a = arr.array("i", [1, 2, 3, 4, 5, -20])
print(a)
print(a[0])
print(a[1])
a[2] = 10
print(a[2])
del a[3]
for i in range(len(a)):
    print(a[i])
