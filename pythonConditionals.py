# pythonConditionals
# Victor Sullivan
# 20210913
# Create statements using conditionals in python. Have the results print to the screen. 

# ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.
       
import ctypes

# Declared Variables

MessageBox = ctypes.windll.user32.MessageBoxW

a = 7
b = 15

if a==b:
    print("a and b are equal!")
    MessageBox(None, 'a and b are equal!', 'Window title', 0)
elif a!=b:
    print("a and b are nothing alike")
    MessageBox(None, 'Same a and b are not', 'Window title', 0)

if a<b:
    print("a is smaller than b :)")
    MessageBox(None, 'Bigger than b, a is not', 'Window title', 0)
elif a>b: 
    print("Larger than b a is")
    MessageBox(None, 'a is larger than b', 'Window title', 0)

if a <= b:
    print("Smaller than or equal to b a is")
    MessageBox(None, 'Smaller than or equal to b a is') 
elif a>b: 
    print("Smaller than or equal to b a is not")
    MessageBox(None, 'Smaller than or equal to b a is not')
else: 
    print("Does not compute")